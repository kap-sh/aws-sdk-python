"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.global_secondary_index_update

GlobalSecondaryIndexUpdateList: TypeAlias = list[
    "capo_dynamodb.types.global_secondary_index_update.GlobalSecondaryIndexUpdate"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalSecondaryIndexUpdateList) -> list:
    import capo_dynamodb.types.global_secondary_index_update

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.global_secondary_index_update.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GlobalSecondaryIndexUpdateList:
    import capo_dynamodb.types.global_secondary_index_update

    out: GlobalSecondaryIndexUpdateList = []
    for item in data:
        out.append(
            capo_dynamodb.types.global_secondary_index_update.deserialize_aws_json_1_0(
                item
            )
        )
    return out
