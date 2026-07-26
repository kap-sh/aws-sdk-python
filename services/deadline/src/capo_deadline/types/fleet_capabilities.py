"""Generated from Smithy shape ``com.amazonaws.deadline#FleetCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.fleet_amount_capabilities
    import capo_deadline.types.fleet_attribute_capabilities


class FleetCapabilities(TypedDict, closed=True):
    amounts: NotRequired[
        "capo_deadline.types.fleet_amount_capabilities.FleetAmountCapabilities"
    ]
    """<p>Amount capabilities of the fleet.</p>"""
    attributes: NotRequired[
        "capo_deadline.types.fleet_attribute_capabilities.FleetAttributeCapabilities"
    ]
    """<p>Attribute capabilities of the fleet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FleetCapabilities) -> dict:
    out: dict = {}
    if "amounts" in value:
        import capo_deadline.types.fleet_amount_capabilities

        out["amounts"] = capo_deadline.types.fleet_amount_capabilities.serialize_json(
            value["amounts"]
        )
    if "attributes" in value:
        import capo_deadline.types.fleet_attribute_capabilities

        out["attributes"] = (
            capo_deadline.types.fleet_attribute_capabilities.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> FleetCapabilities:
    out: FleetCapabilities = {}  # type: ignore[typeddict-item]
    if "amounts" in data:
        import capo_deadline.types.fleet_amount_capabilities

        out["amounts"] = capo_deadline.types.fleet_amount_capabilities.deserialize_json(
            data["amounts"]
        )
    if "attributes" in data:
        import capo_deadline.types.fleet_attribute_capabilities

        out["attributes"] = (
            capo_deadline.types.fleet_attribute_capabilities.deserialize_json(
                data["attributes"]
            )
        )
    return out
