"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactWriteItemsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity_multiple
    import aws_sdk_dynamodb.types.item_collection_metrics_per_table


class TransactWriteItemsOutput(TypedDict):
    consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.consumed_capacity_multiple.ConsumedCapacityMultiple"
    ]
    """<p>The capacity units consumed by the entire <code>TransactWriteItems</code> operation. The values of the list are ordered according to the ordering of the <code>TransactItems</code> request parameter. </p>"""
    item_collection_metrics: NotRequired[
        "aws_sdk_dynamodb.types.item_collection_metrics_per_table.ItemCollectionMetricsPerTable"
    ]
    """<p>A list of tables that were processed by <code>TransactWriteItems</code> and, for each table, information about any item collections that were affected by individual <code>UpdateItem</code>, <code>PutItem</code>, or <code>DeleteItem</code> operations. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactWriteItemsOutput) -> dict:
    out: dict = {}
    if "consumed_capacity" in value:
        import aws_sdk_dynamodb.types.consumed_capacity_multiple

        out["ConsumedCapacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity_multiple.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    if "item_collection_metrics" in value:
        import aws_sdk_dynamodb.types.item_collection_metrics_per_table

        out["ItemCollectionMetrics"] = (
            aws_sdk_dynamodb.types.item_collection_metrics_per_table.serialize_aws_json_1_0(
                value["item_collection_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransactWriteItemsOutput:
    out: TransactWriteItemsOutput = {}  # type: ignore[typeddict-item]
    if "ConsumedCapacity" in data:
        import aws_sdk_dynamodb.types.consumed_capacity_multiple

        out["consumed_capacity"] = (
            aws_sdk_dynamodb.types.consumed_capacity_multiple.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    if "ItemCollectionMetrics" in data:
        import aws_sdk_dynamodb.types.item_collection_metrics_per_table

        out["item_collection_metrics"] = (
            aws_sdk_dynamodb.types.item_collection_metrics_per_table.deserialize_aws_json_1_0(
                data["ItemCollectionMetrics"]
            )
        )
    return out
