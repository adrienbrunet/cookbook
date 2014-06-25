# UNTESTED
# Not sure what video_buffer stands for

import magic
import re

from django.forms.fields import FileField, ValidationError
from django.utils.translation import ugettext_lazy as _

HEADER = 4096
mime = magic.open(magic.MAGIC_MIME)
mime.load()
video_re = re.compile("^video\/.+")


def is_video(path):
	type = mime.file(path)
	return video_re.match(type) != None


def is_video_buffer(buffer):
	type = mime.buffer(buffer)
	return video_re.match(type) != None


class VideoField(FileField):
	default_error_messages = {
		'invalid_video': _(u"Upload a valid video. The file you uploaded was either not a video or a corrupted video."),
	}

	def clean(self, data, initial=None):
		cleaned_data = super(VideoField, self).clean(data, initial)
		if cleaned_data is None:
			return None
		elif not data and initial:
			return initial

		file_path = None
		buffer = None

		try:
			if hasattr(data, 'temporary_file_path'):
				file_path = data.temporary_file_path()
			else:
				if hasattr(data, 'read'):
					buffer = data.read(HEADER)
				else:
					buffer = data['content']
						
			if file_path:
				if not is_video(file_path):
					raise ValidationError("")
			elif buffer:
				if not is_video_buffer(buffer):
					raise ValidationError("")
			else:
				raise Exception("Can't get uploaded file's contents in usual way.")
		except ValidationError:
			raise ValidationError(self.error_messages['invalid_video'])

		if hasattr(cleaned_data, 'seek') and callable(cleaned_data.seek):
			cleaned_data.seek(0)
		return cleaned_data

