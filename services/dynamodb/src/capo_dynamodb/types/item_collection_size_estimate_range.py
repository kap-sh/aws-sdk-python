"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionSizeEstimateRange``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.item_collection_size_estimate_bound

ItemCollectionSizeEstimateRange: TypeAlias = list[
    "capo_dynamodb.types.item_collection_size_estimate_bound.ItemCollectionSizeEstimateBound"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemCollectionSizeEstimateRange) -> list:
    return [
        (
            "NaN"
            if item != item
            else "Infinity"
            if item == float("inf")
            else "-Infinity"
            if item == float("-inf")
            else item
        )
        for item in value
    ]


def deserialize_aws_json_1_0(data: list) -> ItemCollectionSizeEstimateRange:
    return [float(item) for item in data if item is not None]
