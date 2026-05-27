"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionSizeEstimateRange``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.item_collection_size_estimate_bound

ItemCollectionSizeEstimateRange: TypeAlias = list[
    "aws_sdk_dynamodb.types.item_collection_size_estimate_bound.ItemCollectionSizeEstimateBound"
]
