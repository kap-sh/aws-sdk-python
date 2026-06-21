"""Generated from Smithy shape ``com.amazonaws.b2bi#X12GS05TimeFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the time format in the GS05 element (time) of the functional group header. The following formats use 24-hour clock time:</p> <ul> <li> <p> <code>HHMM</code> - Hours and minutes</p> </li> <li> <p> <code>HHMMSS</code> - Hours, minutes, and seconds</p> </li> <li> <p> <code>HHMMSSDD</code> - Hours, minutes, seconds, and decimal seconds</p> </li> </ul> <p>Where:</p> <ul> <li> <p> <code>HH</code> - Hours (00-23)</p> </li> <li> <p> <code>MM</code> - Minutes (00-59)</p> </li> <li> <p> <code>SS</code> - Seconds (00-59)</p> </li> <li> <p> <code>DD</code> - Hundredths of seconds (00-99)</p> </li> </ul>"""
X12GS05TimeFormat: TypeAlias = Literal[
    "HHMM",
    "HHMMSS",
    "HHMMSSDD",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12GS05TimeFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> X12GS05TimeFormat:
    return cast(X12GS05TimeFormat, data)
