"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_name


class AttributeItem(TypedDict):
    name: "aws_sdk_customer_profiles.types.attribute_name.attributeName"
    """<p>The name of an attribute defined in a profile object type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeItem) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AttributeItem:
    out: AttributeItem = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AttributeItem.name required")
    return out
