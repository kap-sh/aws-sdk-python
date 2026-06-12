"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeNameAndValue``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_name
    import aws_sdk_clouddirectory.types.typed_attribute_value


class AttributeNameAndValue(TypedDict):
    attribute_name: "aws_sdk_clouddirectory.types.attribute_name.AttributeName"
    """<p>The attribute name of the typed link.</p>"""
    value: "aws_sdk_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    """<p>The value for the typed link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeNameAndValue) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import aws_sdk_clouddirectory.types.typed_attribute_value

    out["Value"] = aws_sdk_clouddirectory.types.typed_attribute_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> AttributeNameAndValue:
    out: AttributeNameAndValue = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("AttributeNameAndValue.attribute_name required")
    if "Value" in data:
        import aws_sdk_clouddirectory.types.typed_attribute_value

        out["value"] = (
            aws_sdk_clouddirectory.types.typed_attribute_value.deserialize_json(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("AttributeNameAndValue.value required")
    return out
