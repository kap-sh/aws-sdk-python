"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionMetricsMultiple``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.item_collection_metrics

ItemCollectionMetricsMultiple: TypeAlias = list[
    "capo_dynamodb.types.item_collection_metrics.ItemCollectionMetrics"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemCollectionMetricsMultiple) -> list:
    import capo_dynamodb.types.item_collection_metrics

    out: list = []
    for item in value:
        out.append(
            capo_dynamodb.types.item_collection_metrics.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ItemCollectionMetricsMultiple:
    import capo_dynamodb.types.item_collection_metrics

    out: ItemCollectionMetricsMultiple = []
    for item in data:
        out.append(
            capo_dynamodb.types.item_collection_metrics.deserialize_aws_json_1_0(item)
        )
    return out
