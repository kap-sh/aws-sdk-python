"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionSizeEstimateRange``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.item_collection_size_estimate_bound

ItemCollectionSizeEstimateRange: TypeAlias = list[
    "aws_sdk_dynamodb.types.item_collection_size_estimate_bound.ItemCollectionSizeEstimateBound"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemCollectionSizeEstimateRange) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ItemCollectionSizeEstimateRange:
    return list(data)
