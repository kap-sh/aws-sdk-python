"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableAttributeDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_dynamo_db_table_attribute_definition

AwsDynamoDbTableAttributeDefinitionList: TypeAlias = list[
    "capo_securityhub.types.aws_dynamo_db_table_attribute_definition.AwsDynamoDbTableAttributeDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableAttributeDefinitionList) -> list:
    import capo_securityhub.types.aws_dynamo_db_table_attribute_definition

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_dynamo_db_table_attribute_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsDynamoDbTableAttributeDefinitionList:
    import capo_securityhub.types.aws_dynamo_db_table_attribute_definition

    out: AwsDynamoDbTableAttributeDefinitionList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_dynamo_db_table_attribute_definition.deserialize_json(
                item
            )
        )
    return out
