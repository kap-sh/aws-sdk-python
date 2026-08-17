"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchWriteItemOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.batch_write_item_request_map
    import capo_dynamodb.types.consumed_capacity_multiple
    import capo_dynamodb.types.item_collection_metrics_per_table


class BatchWriteItemOutput(TypedDict, closed=True):
    unprocessed_items: NotRequired[
        "capo_dynamodb.types.batch_write_item_request_map.BatchWriteItemRequestMap"
    ]
    """<p>A map of tables and requests against those tables that were not processed. The <code>UnprocessedItems</code> value is in the same form as <code>RequestItems</code>, so you can provide this value directly to a subsequent <code>BatchWriteItem</code> operation. For more information, see <code>RequestItems</code> in the Request Parameters section.</p> <p>Each <code>UnprocessedItems</code> entry consists of a table name or table ARN and, for that table, a list of operations to perform (<code>DeleteRequest</code> or <code>PutRequest</code>).</p> <ul> <li> <p> <code>DeleteRequest</code> - Perform a <code>DeleteItem</code> operation on the specified item. The item to be deleted is identified by a <code>Key</code> subelement:</p> <ul> <li> <p> <code>Key</code> - A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value.</p> </li> </ul> </li> <li> <p> <code>PutRequest</code> - Perform a <code>PutItem</code> operation on the specified item. The item to be put is identified by an <code>Item</code> subelement:</p> <ul> <li> <p> <code>Item</code> - A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values will be rejected with a <code>ValidationException</code> exception.</p> <p>If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table's attribute definition.</p> </li> </ul> </li> </ul> <p>If there are no unprocessed items remaining, the response contains an empty <code>UnprocessedItems</code> map.</p>"""
    item_collection_metrics: NotRequired[
        "capo_dynamodb.types.item_collection_metrics_per_table.ItemCollectionMetricsPerTable"
    ]
    """<p>A list of tables that were processed by <code>BatchWriteItem</code> and, for each table, information about any item collections that were affected by individual <code>DeleteItem</code> or <code>PutItem</code> operations.</p> <p>Each entry consists of the following subelements:</p> <ul> <li> <p> <code>ItemCollectionKey</code> - The partition key value of the item collection. This is the same as the partition key value of the item.</p> </li> <li> <p> <code>SizeEstimateRangeGB</code> - An estimate of item collection size, expressed in GB. This is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on the table. Use this estimate to measure whether a local secondary index is approaching its size limit.</p> <p>The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.</p> </li> </ul>"""
    consumed_capacity: NotRequired[
        "capo_dynamodb.types.consumed_capacity_multiple.ConsumedCapacityMultiple"
    ]
    """<p>The capacity units consumed by the entire <code>BatchWriteItem</code> operation.</p> <p>Each element consists of:</p> <ul> <li> <p> <code>TableName</code> - The table that consumed the provisioned throughput.</p> </li> <li> <p> <code>CapacityUnits</code> - The total number of capacity units consumed.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchWriteItemOutput) -> dict:
    out: dict = {}
    if "unprocessed_items" in value:
        import capo_dynamodb.types.batch_write_item_request_map

        out["UnprocessedItems"] = (
            capo_dynamodb.types.batch_write_item_request_map.serialize_aws_json_1_0(
                value["unprocessed_items"]
            )
        )
    if "item_collection_metrics" in value:
        import capo_dynamodb.types.item_collection_metrics_per_table

        out["ItemCollectionMetrics"] = (
            capo_dynamodb.types.item_collection_metrics_per_table.serialize_aws_json_1_0(
                value["item_collection_metrics"]
            )
        )
    if "consumed_capacity" in value:
        import capo_dynamodb.types.consumed_capacity_multiple

        out["ConsumedCapacity"] = (
            capo_dynamodb.types.consumed_capacity_multiple.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchWriteItemOutput:
    out: BatchWriteItemOutput = {}  # type: ignore[typeddict-item]
    if data.get("UnprocessedItems") is not None:
        import capo_dynamodb.types.batch_write_item_request_map

        out["unprocessed_items"] = (
            capo_dynamodb.types.batch_write_item_request_map.deserialize_aws_json_1_0(
                data["UnprocessedItems"]
            )
        )
    if data.get("ItemCollectionMetrics") is not None:
        import capo_dynamodb.types.item_collection_metrics_per_table

        out["item_collection_metrics"] = (
            capo_dynamodb.types.item_collection_metrics_per_table.deserialize_aws_json_1_0(
                data["ItemCollectionMetrics"]
            )
        )
    if data.get("ConsumedCapacity") is not None:
        import capo_dynamodb.types.consumed_capacity_multiple

        out["consumed_capacity"] = (
            capo_dynamodb.types.consumed_capacity_multiple.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    return out
