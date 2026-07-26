"""Generated from Smithy shape ``com.amazonaws.deadline#FleetAttributeCapability``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.attribute_capability_name
    import capo_deadline.types.attribute_capability_values_list


class FleetAttributeCapability(TypedDict, closed=True):
    name: "capo_deadline.types.attribute_capability_name.AttributeCapabilityName"
    """<p>The name of the fleet attribute capability for the worker.</p>"""
    values: "capo_deadline.types.attribute_capability_values_list.AttributeCapabilityValuesList"
    """<p>The number of fleet attribute capabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FleetAttributeCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_deadline.types.attribute_capability_values_list

    out["values"] = capo_deadline.types.attribute_capability_values_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> FleetAttributeCapability:
    out: FleetAttributeCapability = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FleetAttributeCapability.name required")
    if "values" in data:
        import capo_deadline.types.attribute_capability_values_list

        out["values"] = (
            capo_deadline.types.attribute_capability_values_list.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("FleetAttributeCapability.values required")
    return out
