"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.global_secondary_index_info

GlobalSecondaryIndexes: TypeAlias = list[
    "capo_dynamodb.types.global_secondary_index_info.GlobalSecondaryIndexInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalSecondaryIndexes) -> list:
    import capo_dynamodb.types.global_secondary_index_info

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.global_secondary_index_info.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GlobalSecondaryIndexes:
    import capo_dynamodb.types.global_secondary_index_info

    out: GlobalSecondaryIndexes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.global_secondary_index_info.deserialize_aws_json_1_0(
                item
            )
        )
    return out
