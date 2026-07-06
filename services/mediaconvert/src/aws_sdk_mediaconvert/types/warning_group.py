"""Generated from Smithy shape ``com.amazonaws.mediaconvert#WarningGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer


class WarningGroup(TypedDict, closed=True):
    code: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Warning code that identifies a specific warning in the job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/warning_codes.html"""
    count: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The number of times this warning occurred in the job."""


# --- restJson1 ser/de ---
def serialize_json(value: WarningGroup) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> WarningGroup:
    out: WarningGroup = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "count" in data:
        out["count"] = data["count"]
    return out
