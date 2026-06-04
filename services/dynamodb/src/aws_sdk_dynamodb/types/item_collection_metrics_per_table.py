"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionMetricsPerTable``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.item_collection_metrics_multiple

ItemCollectionMetricsPerTable: TypeAlias = dict[
    "aws_sdk_dynamodb.types.table_arn.TableArn",
    "aws_sdk_dynamodb.types.item_collection_metrics_multiple.ItemCollectionMetricsMultiple",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ItemCollectionMetricsPerTable) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_dynamodb.types.item_collection_metrics_multiple

        out[key] = (
            aws_sdk_dynamodb.types.item_collection_metrics_multiple.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ItemCollectionMetricsPerTable:
    out: ItemCollectionMetricsPerTable = {}
    for key, value in data.items():
        import aws_sdk_dynamodb.types.item_collection_metrics_multiple

        out[key] = (
            aws_sdk_dynamodb.types.item_collection_metrics_multiple.deserialize_aws_json_1_0(
                value
            )
        )
    return out
