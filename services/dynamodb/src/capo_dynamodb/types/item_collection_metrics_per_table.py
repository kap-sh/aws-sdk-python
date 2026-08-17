"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionMetricsPerTable``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.item_collection_metrics_multiple
    import capo_dynamodb.types.table_arn

ItemCollectionMetricsPerTable: TypeAlias = dict[
    "capo_dynamodb.types.table_arn.TableArn",
    "capo_dynamodb.types.item_collection_metrics_multiple.ItemCollectionMetricsMultiple",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ItemCollectionMetricsPerTable) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.item_collection_metrics_multiple

        out[key] = (
            capo_dynamodb.types.item_collection_metrics_multiple.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ItemCollectionMetricsPerTable:
    out: ItemCollectionMetricsPerTable = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_dynamodb.types.item_collection_metrics_multiple

        out[key] = (
            capo_dynamodb.types.item_collection_metrics_multiple.deserialize_aws_json_1_0(
                value
            )
        )
    return out
