"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NielsenConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max0
    import aws_sdk_mediaconvert.types.__string


class NielsenConfiguration(TypedDict):
    breakout_code: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max0.__integerMin0Max0"
    ]
    """Nielsen has discontinued the use of breakout code functionality. If you must include this property, set the value to zero."""
    distributor_id: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Use Distributor ID to specify the distributor ID that is assigned to your organization by Nielsen."""


# --- restJson1 ser/de ---
def serialize_json(value: NielsenConfiguration) -> dict:
    out: dict = {}
    if "breakout_code" in value:
        out["breakoutCode"] = value["breakout_code"]
    if "distributor_id" in value:
        out["distributorId"] = value["distributor_id"]
    return out


def deserialize_json(data: dict) -> NielsenConfiguration:
    out: NielsenConfiguration = {}  # type: ignore[typeddict-item]
    if "breakoutCode" in data:
        out["breakout_code"] = data["breakoutCode"]
    if "distributorId" in data:
        out["distributor_id"] = data["distributorId"]
    return out
