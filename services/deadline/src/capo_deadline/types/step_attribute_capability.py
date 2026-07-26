"""Generated from Smithy shape ``com.amazonaws.deadline#StepAttributeCapability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.attribute_capability_name
    import capo_deadline.types.list_attribute_capability_value


class StepAttributeCapability(TypedDict, closed=True):
    name: "capo_deadline.types.attribute_capability_name.AttributeCapabilityName"
    """<p>The name of the step attribute.</p>"""
    any_of: NotRequired[
        "capo_deadline.types.list_attribute_capability_value.ListAttributeCapabilityValue"
    ]
    """<p>Requires any of the step attributes in a given list.</p>"""
    all_of: NotRequired[
        "capo_deadline.types.list_attribute_capability_value.ListAttributeCapabilityValue"
    ]
    """<p>Requires all of the step attribute values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepAttributeCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "any_of" in value:
        import capo_deadline.types.list_attribute_capability_value

        out["anyOf"] = (
            capo_deadline.types.list_attribute_capability_value.serialize_json(
                value["any_of"]
            )
        )
    if "all_of" in value:
        import capo_deadline.types.list_attribute_capability_value

        out["allOf"] = (
            capo_deadline.types.list_attribute_capability_value.serialize_json(
                value["all_of"]
            )
        )
    return out


def deserialize_json(data: dict) -> StepAttributeCapability:
    out: StepAttributeCapability = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StepAttributeCapability.name required")
    if "anyOf" in data:
        import capo_deadline.types.list_attribute_capability_value

        out["any_of"] = (
            capo_deadline.types.list_attribute_capability_value.deserialize_json(
                data["anyOf"]
            )
        )
    if "allOf" in data:
        import capo_deadline.types.list_attribute_capability_value

        out["all_of"] = (
            capo_deadline.types.list_attribute_capability_value.deserialize_json(
                data["allOf"]
            )
        )
    return out
