"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableAttributeDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition

AwsDynamoDbTableAttributeDefinitionList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition.AwsDynamoDbTableAttributeDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableAttributeDefinitionList) -> list:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsDynamoDbTableAttributeDefinitionList:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition

    out: AwsDynamoDbTableAttributeDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_dynamo_db_table_attribute_definition.deserialize_json(
                item
            )
        )
    return out
