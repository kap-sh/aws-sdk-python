"""Generated from Smithy shape ``com.amazonaws.connect#TemplateAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.attributes
    import aws_sdk_connect.types.customer_profile_attributes_serialized


class TemplateAttributes(TypedDict, closed=True):
    custom_attributes: NotRequired["aws_sdk_connect.types.attributes.Attributes"]
    """<p>An object that specifies the custom attributes values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. </p>"""
    customer_profile_attributes: NotRequired[
        "aws_sdk_connect.types.customer_profile_attributes_serialized.CustomerProfileAttributesSerialized"
    ]
    """<p>An object that specifies the customer profile attributes values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateAttributes) -> dict:
    out: dict = {}
    if "custom_attributes" in value:
        import aws_sdk_connect.types.attributes

        out["CustomAttributes"] = aws_sdk_connect.types.attributes.serialize_json(
            value["custom_attributes"]
        )
    if "customer_profile_attributes" in value:
        out["CustomerProfileAttributes"] = value["customer_profile_attributes"]
    return out


def deserialize_json(data: dict) -> TemplateAttributes:
    out: TemplateAttributes = {}  # type: ignore[typeddict-item]
    if "CustomAttributes" in data:
        import aws_sdk_connect.types.attributes

        out["custom_attributes"] = aws_sdk_connect.types.attributes.deserialize_json(
            data["CustomAttributes"]
        )
    if "CustomerProfileAttributes" in data:
        out["customer_profile_attributes"] = data["CustomerProfileAttributes"]
    return out
