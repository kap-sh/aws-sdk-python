"""Generated from Smithy shape ``com.amazonaws.iotwireless#Positioning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.f_port


class Positioning(TypedDict, closed=True):
    clock_sync: NotRequired["capo_iot_wireless.types.f_port.FPort"]
    stream: NotRequired["capo_iot_wireless.types.f_port.FPort"]
    gnss: NotRequired["capo_iot_wireless.types.f_port.FPort"]


# --- restJson1 ser/de ---
def serialize_json(value: Positioning) -> dict:
    out: dict = {}
    if "clock_sync" in value:
        out["ClockSync"] = value["clock_sync"]
    if "stream" in value:
        out["Stream"] = value["stream"]
    if "gnss" in value:
        out["Gnss"] = value["gnss"]
    return out


def deserialize_json(data: dict) -> Positioning:
    out: Positioning = {}  # type: ignore[typeddict-item]
    if "ClockSync" in data:
        out["clock_sync"] = data["ClockSync"]
    if "Stream" in data:
        out["stream"] = data["Stream"]
    if "Gnss" in data:
        out["gnss"] = data["Gnss"]
    return out
