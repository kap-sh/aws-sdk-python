"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BilledResourceUtilization``."""

from typing import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError


class BilledResourceUtilization(TypedDict):
    units: "float"
    """<p> The number of Clean Rooms Processing Unit (CRPU) hours that have been billed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BilledResourceUtilization) -> dict:
    out: dict = {}
    out["units"] = value["units"]
    return out


def deserialize_json(data: dict) -> BilledResourceUtilization:
    out: BilledResourceUtilization = {}  # type: ignore[typeddict-item]
    if "units" in data:
        out["units"] = data["units"]
    else:
        raise DeserializationError("BilledResourceUtilization.units required")
    return out
