"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableLocalSecondaryIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index

AwsDynamoDbTableLocalSecondaryIndexList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index.AwsDynamoDbTableLocalSecondaryIndex"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableLocalSecondaryIndexList) -> list:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsDynamoDbTableLocalSecondaryIndexList:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index

    out: AwsDynamoDbTableLocalSecondaryIndexList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_dynamo_db_table_local_secondary_index.deserialize_json(
                item
            )
        )
    return out
