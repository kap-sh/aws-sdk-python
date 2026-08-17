"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalSecondaryIndexDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.global_secondary_index_description

GlobalSecondaryIndexDescriptionList: TypeAlias = list[
    "capo_dynamodb.types.global_secondary_index_description.GlobalSecondaryIndexDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalSecondaryIndexDescriptionList) -> list:
    import capo_dynamodb.types.global_secondary_index_description

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.global_secondary_index_description.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GlobalSecondaryIndexDescriptionList:
    import capo_dynamodb.types.global_secondary_index_description

    out: GlobalSecondaryIndexDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.global_secondary_index_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out
