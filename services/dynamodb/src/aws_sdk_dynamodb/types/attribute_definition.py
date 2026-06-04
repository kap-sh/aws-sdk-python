"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeDefinition``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.key_schema_attribute_name
    import aws_sdk_dynamodb.types.scalar_attribute_type


class AttributeDefinition(TypedDict):
    attribute_name: (
        "aws_sdk_dynamodb.types.key_schema_attribute_name.KeySchemaAttributeName"
    )
    """<p>A name for the attribute.</p>"""
    attribute_type: "aws_sdk_dynamodb.types.scalar_attribute_type.ScalarAttributeType"
    """<p>The data type for the attribute, where:</p> <ul> <li> <p> <code>S</code> - the attribute is of type String</p> </li> <li> <p> <code>N</code> - the attribute is of type Number</p> </li> <li> <p> <code>B</code> - the attribute is of type Binary</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeDefinition) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import aws_sdk_dynamodb.types.scalar_attribute_type

    out["AttributeType"] = (
        aws_sdk_dynamodb.types.scalar_attribute_type.serialize_aws_json_1_0(
            value["attribute_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AttributeDefinition:
    out: AttributeDefinition = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("AttributeDefinition.attribute_name required")
    if "AttributeType" in data:
        import aws_sdk_dynamodb.types.scalar_attribute_type

        out["attribute_type"] = (
            aws_sdk_dynamodb.types.scalar_attribute_type.deserialize_aws_json_1_0(
                data["AttributeType"]
            )
        )
    else:
        raise DeserializationError("AttributeDefinition.attribute_type required")
    return out
