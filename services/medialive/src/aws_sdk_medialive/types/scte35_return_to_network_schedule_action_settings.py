"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35ReturnToNetworkScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__long_min0_max4294967295


class Scte35ReturnToNetworkScheduleActionSettings(TypedDict, closed=True):
    splice_event_id: NotRequired[
        "aws_sdk_medialive.types.__long_min0_max4294967295.__longMin0Max4294967295"
    ]
    """The splice_event_id for the SCTE-35 splice_insert, as defined in SCTE-35."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte35ReturnToNetworkScheduleActionSettings) -> dict:
    out: dict = {}
    if "splice_event_id" in value:
        out["spliceEventId"] = value["splice_event_id"]
    return out


def deserialize_json(data: dict) -> Scte35ReturnToNetworkScheduleActionSettings:
    out: Scte35ReturnToNetworkScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "spliceEventId" in data:
        out["splice_event_id"] = data["spliceEventId"]
    return out
