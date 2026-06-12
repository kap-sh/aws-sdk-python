"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_attribute_key
    import aws_sdk_kendra.types.document_attribute_value


class DocumentAttribute(TypedDict):
    key: "aws_sdk_kendra.types.document_attribute_key.DocumentAttributeKey"
    """<p>The identifier for the attribute.</p>"""
    value: "aws_sdk_kendra.types.document_attribute_value.DocumentAttributeValue"
    """<p>The value of the attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttribute) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_kendra.types.document_attribute_value

    out["Value"] = aws_sdk_kendra.types.document_attribute_value.serialize_aws_json_1_1(
        value["value"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentAttribute:
    out: DocumentAttribute = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("DocumentAttribute.key required")
    if "Value" in data:
        import aws_sdk_kendra.types.document_attribute_value

        out["value"] = (
            aws_sdk_kendra.types.document_attribute_value.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("DocumentAttribute.value required")
    return out
