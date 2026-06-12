"""Generated from Smithy shape ``com.amazonaws.deadline#StepAttributeCapability``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.attribute_capability_name
    import aws_sdk_deadline.types.list_attribute_capability_value


class StepAttributeCapability(TypedDict):
    name: "aws_sdk_deadline.types.attribute_capability_name.AttributeCapabilityName"
    """<p>The name of the step attribute.</p>"""
    any_of: NotRequired[
        "aws_sdk_deadline.types.list_attribute_capability_value.ListAttributeCapabilityValue"
    ]
    """<p>Requires any of the step attributes in a given list.</p>"""
    all_of: NotRequired[
        "aws_sdk_deadline.types.list_attribute_capability_value.ListAttributeCapabilityValue"
    ]
    """<p>Requires all of the step attribute values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StepAttributeCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "any_of" in value:
        import aws_sdk_deadline.types.list_attribute_capability_value

        out["anyOf"] = (
            aws_sdk_deadline.types.list_attribute_capability_value.serialize_json(
                value["any_of"]
            )
        )
    if "all_of" in value:
        import aws_sdk_deadline.types.list_attribute_capability_value

        out["allOf"] = (
            aws_sdk_deadline.types.list_attribute_capability_value.serialize_json(
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
        import aws_sdk_deadline.types.list_attribute_capability_value

        out["any_of"] = (
            aws_sdk_deadline.types.list_attribute_capability_value.deserialize_json(
                data["anyOf"]
            )
        )
    if "allOf" in data:
        import aws_sdk_deadline.types.list_attribute_capability_value

        out["all_of"] = (
            aws_sdk_deadline.types.list_attribute_capability_value.deserialize_json(
                data["allOf"]
            )
        )
    return out
