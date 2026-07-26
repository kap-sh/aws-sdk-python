"""Generated from Smithy shape ``com.amazonaws.deadline#FleetAmountCapability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.amount_capability_name


class FleetAmountCapability(TypedDict, closed=True):
    name: "capo_deadline.types.amount_capability_name.AmountCapabilityName"
    """<p>The name of the fleet capability.</p>"""
    min: "float"
    """<p>The minimum amount of fleet worker capability.</p>"""
    max: NotRequired["float"]
    """<p>The maximum amount of the fleet worker capability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FleetAmountCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> FleetAmountCapability:
    out: FleetAmountCapability = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FleetAmountCapability.name required")
    if "min" in data:
        out["min"] = data["min"]
    else:
        raise DeserializationError("FleetAmountCapability.min required")
    if "max" in data:
        out["max"] = data["max"]
    return out
