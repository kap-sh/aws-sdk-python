"""Generated from Smithy shape ``com.amazonaws.iot#AssetPropertyTimestamp``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.asset_property_offset_in_nanos
    import capo_iot.types.asset_property_time_in_seconds


class AssetPropertyTimestamp(TypedDict, closed=True):
    time_in_seconds: (
        "capo_iot.types.asset_property_time_in_seconds.AssetPropertyTimeInSeconds"
    )
    """<p>A string that contains the time in seconds since epoch. Accepts substitution templates.</p>"""
    offset_in_nanos: NotRequired[
        "capo_iot.types.asset_property_offset_in_nanos.AssetPropertyOffsetInNanos"
    ]
    """<p>Optional. A string that contains the nanosecond time offset. Accepts substitution templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyTimestamp) -> dict:
    out: dict = {}
    out["timeInSeconds"] = value["time_in_seconds"]
    if "offset_in_nanos" in value:
        out["offsetInNanos"] = value["offset_in_nanos"]
    return out


def deserialize_json(data: dict) -> AssetPropertyTimestamp:
    out: AssetPropertyTimestamp = {}  # type: ignore[typeddict-item]
    if "timeInSeconds" in data:
        out["time_in_seconds"] = data["timeInSeconds"]
    else:
        raise DeserializationError("AssetPropertyTimestamp.time_in_seconds required")
    if "offsetInNanos" in data:
        out["offset_in_nanos"] = data["offsetInNanos"]
    return out
