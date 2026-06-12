"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeKeyAndValue``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_key
    import aws_sdk_clouddirectory.types.typed_attribute_value


class AttributeKeyAndValue(TypedDict):
    key: "aws_sdk_clouddirectory.types.attribute_key.AttributeKey"
    """<p>The key of the attribute.</p>"""
    value: "aws_sdk_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    """<p>The value of the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeKeyAndValue) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.attribute_key

    out["Key"] = aws_sdk_clouddirectory.types.attribute_key.serialize_json(value["key"])
    import aws_sdk_clouddirectory.types.typed_attribute_value

    out["Value"] = aws_sdk_clouddirectory.types.typed_attribute_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> AttributeKeyAndValue:
    out: AttributeKeyAndValue = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_clouddirectory.types.attribute_key

        out["key"] = aws_sdk_clouddirectory.types.attribute_key.deserialize_json(
            data["Key"]
        )
    else:
        raise DeserializationError("AttributeKeyAndValue.key required")
    if "Value" in data:
        import aws_sdk_clouddirectory.types.typed_attribute_value

        out["value"] = (
            aws_sdk_clouddirectory.types.typed_attribute_value.deserialize_json(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("AttributeKeyAndValue.value required")
    return out
