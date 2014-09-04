# coding: utf-8

def convert_from_camel_case(name):
    # Handles the case where multiple uppercase are next to each other
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # lower the uppercase and add a '_'
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
