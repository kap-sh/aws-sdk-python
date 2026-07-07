"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BilledJobResourceUtilization``."""

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError


class BilledJobResourceUtilization(TypedDict, closed=True):
    units: "float"
    """<p> The number of Clean Rooms Processing Unit (CRPU) hours that have been billed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BilledJobResourceUtilization) -> dict:
    out: dict = {}
    out["units"] = value["units"]
    return out


def deserialize_json(data: dict) -> BilledJobResourceUtilization:
    out: BilledJobResourceUtilization = {}  # type: ignore[typeddict-item]
    if "units" in data:
        out["units"] = data["units"]
    else:
        raise DeserializationError("BilledJobResourceUtilization.units required")
    return out
