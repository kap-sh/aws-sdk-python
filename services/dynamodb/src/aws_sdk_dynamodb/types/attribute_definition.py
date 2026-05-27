"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeDefinition``."""

from typing import TYPE_CHECKING, TypedDict

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
