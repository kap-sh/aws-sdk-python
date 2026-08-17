"""Generated from Smithy shape ``com.amazonaws.dynamodb#LocalSecondaryIndexes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.local_secondary_index_info

LocalSecondaryIndexes: TypeAlias = list[
    "capo_dynamodb.types.local_secondary_index_info.LocalSecondaryIndexInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LocalSecondaryIndexes) -> list:
    import capo_dynamodb.types.local_secondary_index_info

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.local_secondary_index_info.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LocalSecondaryIndexes:
    import capo_dynamodb.types.local_secondary_index_info

    out: LocalSecondaryIndexes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.local_secondary_index_info.deserialize_aws_json_1_0(
                item
            )
        )
    return out
