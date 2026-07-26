"""Generated from Smithy shape ``com.amazonaws.connect#Attribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_attribute_type
    import capo_connect.types.instance_attribute_value


class Attribute(TypedDict, closed=True):
    attribute_type: NotRequired[
        "capo_connect.types.instance_attribute_type.InstanceAttributeType"
    ]
    """<p>The type of attribute.</p>"""
    value: NotRequired[
        "capo_connect.types.instance_attribute_value.InstanceAttributeValue"
    ]
    """<p>The value of the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attribute) -> dict:
    out: dict = {}
    if "attribute_type" in value:
        import capo_connect.types.instance_attribute_type

        out["AttributeType"] = (
            capo_connect.types.instance_attribute_type.serialize_json(
                value["attribute_type"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if "AttributeType" in data:
        import capo_connect.types.instance_attribute_type

        out["attribute_type"] = (
            capo_connect.types.instance_attribute_type.deserialize_json(
                data["AttributeType"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
