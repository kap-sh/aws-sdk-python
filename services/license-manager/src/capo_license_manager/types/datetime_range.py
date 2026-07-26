"""Generated from Smithy shape ``com.amazonaws.licensemanager#DatetimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.iso8601_date_time


class DatetimeRange(TypedDict, closed=True):
    begin: "capo_license_manager.types.iso8601_date_time.ISO8601DateTime"
    """<p>Start of the time range.</p>"""
    end: NotRequired["capo_license_manager.types.iso8601_date_time.ISO8601DateTime"]
    """<p>End of the time range.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatetimeRange) -> dict:
    out: dict = {}
    out["Begin"] = value["begin"]
    if "end" in value:
        out["End"] = value["end"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatetimeRange:
    out: DatetimeRange = {}  # type: ignore[typeddict-item]
    if "Begin" in data:
        out["begin"] = data["Begin"]
    else:
        raise DeserializationError("DatetimeRange.begin required")
    if "End" in data:
        out["end"] = data["End"]
    return out
