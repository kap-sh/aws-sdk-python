"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableGlobalSecondaryIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_dynamo_db_table_global_secondary_index

AwsDynamoDbTableGlobalSecondaryIndexList: TypeAlias = list[
    "capo_securityhub.types.aws_dynamo_db_table_global_secondary_index.AwsDynamoDbTableGlobalSecondaryIndex"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableGlobalSecondaryIndexList) -> list:
    import capo_securityhub.types.aws_dynamo_db_table_global_secondary_index

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_dynamo_db_table_global_secondary_index.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsDynamoDbTableGlobalSecondaryIndexList:
    import capo_securityhub.types.aws_dynamo_db_table_global_secondary_index

    out: AwsDynamoDbTableGlobalSecondaryIndexList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_dynamo_db_table_global_secondary_index.deserialize_json(
                item
            )
        )
    return out
