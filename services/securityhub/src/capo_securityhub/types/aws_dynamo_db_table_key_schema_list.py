"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableKeySchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_dynamo_db_table_key_schema

AwsDynamoDbTableKeySchemaList: TypeAlias = list[
    "capo_securityhub.types.aws_dynamo_db_table_key_schema.AwsDynamoDbTableKeySchema"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableKeySchemaList) -> list:
    import capo_securityhub.types.aws_dynamo_db_table_key_schema

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_dynamo_db_table_key_schema.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsDynamoDbTableKeySchemaList:
    import capo_securityhub.types.aws_dynamo_db_table_key_schema

    out: AwsDynamoDbTableKeySchemaList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_dynamo_db_table_key_schema.deserialize_json(item)
        )
    return out
