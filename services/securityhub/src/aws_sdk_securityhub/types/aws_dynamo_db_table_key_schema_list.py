"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableKeySchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema

AwsDynamoDbTableKeySchemaList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema.AwsDynamoDbTableKeySchema"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableKeySchemaList) -> list:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsDynamoDbTableKeySchemaList:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema

    out: AwsDynamoDbTableKeySchemaList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema.deserialize_json(
                item
            )
        )
    return out
