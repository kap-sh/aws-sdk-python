"""Generated from Smithy shape ``com.amazonaws.support#DateInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_support.types.validated_date_time


class DateInterval(TypedDict, closed=True):
    start_date_time: NotRequired[
        "aws_sdk_support.types.validated_date_time.ValidatedDateTime"
    ]
    """<p> A JSON object containing start and date time (UTC). Date and time format is RFC 3339 : 'yyyy-MM-dd'T'HH:mm:ss.SSSZZ'. </p>"""
    end_date_time: NotRequired[
        "aws_sdk_support.types.validated_date_time.ValidatedDateTime"
    ]
    """<p> End Date Time (UTC). RFC 3339 format : 'yyyy-MM-dd'T'HH:mm:ss.SSSZZ'. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DateInterval) -> dict:
    out: dict = {}
    if "start_date_time" in value:
        out["startDateTime"] = value["start_date_time"]
    if "end_date_time" in value:
        out["endDateTime"] = value["end_date_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DateInterval:
    out: DateInterval = {}  # type: ignore[typeddict-item]
    if "startDateTime" in data:
        out["start_date_time"] = data["startDateTime"]
    if "endDateTime" in data:
        out["end_date_time"] = data["endDateTime"]
    return out
