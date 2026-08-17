"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.global_secondary_index

GlobalSecondaryIndexList: TypeAlias = list[
    "capo_dynamodb.types.global_secondary_index.GlobalSecondaryIndex"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalSecondaryIndexList) -> list:
    import capo_dynamodb.types.global_secondary_index

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.global_secondary_index.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GlobalSecondaryIndexList:
    import capo_dynamodb.types.global_secondary_index

    out: GlobalSecondaryIndexList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.global_secondary_index.deserialize_aws_json_1_0(item)
        )
    return out
