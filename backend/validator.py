import re
from dateutil.parser import parse

GST_PATTERN = r"\d{2}[A-Z]{5}\d{4}[A-Z]\d[Z][A-Z0-9]"

def validate_gst(gst):

    if not gst:
        return False

    return bool(
        re.fullmatch(
            GST_PATTERN,
            gst
        )
    )


def validate_date(date_string):

    try:
        parse(date_string)
        return True

    except:
        return False