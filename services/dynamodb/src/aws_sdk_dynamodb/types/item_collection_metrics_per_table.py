"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionMetricsPerTable``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.item_collection_metrics_multiple

ItemCollectionMetricsPerTable: TypeAlias = dict[
    "aws_sdk_dynamodb.types.table_arn.TableArn",
    "aws_sdk_dynamodb.types.item_collection_metrics_multiple.ItemCollectionMetricsMultiple",
]
