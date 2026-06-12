"""Generated from Smithy shape ``com.amazonaws.deadline#FleetCapabilities``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.fleet_amount_capabilities
    import aws_sdk_deadline.types.fleet_attribute_capabilities


class FleetCapabilities(TypedDict):
    amounts: NotRequired[
        "aws_sdk_deadline.types.fleet_amount_capabilities.FleetAmountCapabilities"
    ]
    """<p>Amount capabilities of the fleet.</p>"""
    attributes: NotRequired[
        "aws_sdk_deadline.types.fleet_attribute_capabilities.FleetAttributeCapabilities"
    ]
    """<p>Attribute capabilities of the fleet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FleetCapabilities) -> dict:
    out: dict = {}
    if "amounts" in value:
        import aws_sdk_deadline.types.fleet_amount_capabilities

        out["amounts"] = (
            aws_sdk_deadline.types.fleet_amount_capabilities.serialize_json(
                value["amounts"]
            )
        )
    if "attributes" in value:
        import aws_sdk_deadline.types.fleet_attribute_capabilities

        out["attributes"] = (
            aws_sdk_deadline.types.fleet_attribute_capabilities.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> FleetCapabilities:
    out: FleetCapabilities = {}  # type: ignore[typeddict-item]
    if "amounts" in data:
        import aws_sdk_deadline.types.fleet_amount_capabilities

        out["amounts"] = (
            aws_sdk_deadline.types.fleet_amount_capabilities.deserialize_json(
                data["amounts"]
            )
        )
    if "attributes" in data:
        import aws_sdk_deadline.types.fleet_attribute_capabilities

        out["attributes"] = (
            aws_sdk_deadline.types.fleet_attribute_capabilities.deserialize_json(
                data["attributes"]
            )
        )
    return out
