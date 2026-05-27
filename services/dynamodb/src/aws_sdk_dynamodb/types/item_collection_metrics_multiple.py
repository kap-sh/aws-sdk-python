"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionMetricsMultiple``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.item_collection_metrics

ItemCollectionMetricsMultiple: TypeAlias = list[
    "aws_sdk_dynamodb.types.item_collection_metrics.ItemCollectionMetrics"
]
