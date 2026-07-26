"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchGetItemOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.batch_get_request_map
    import capo_dynamodb.types.batch_get_response_map
    import capo_dynamodb.types.consumed_capacity_multiple


class BatchGetItemOutput(TypedDict, closed=True):
    responses: NotRequired[
        "capo_dynamodb.types.batch_get_response_map.BatchGetResponseMap"
    ]
    """<p>A map of table name or table ARN to a list of items. Each object in <code>Responses</code> consists of a table name or ARN, along with a map of attribute data consisting of the data type and attribute value.</p>"""
    unprocessed_keys: NotRequired[
        "capo_dynamodb.types.batch_get_request_map.BatchGetRequestMap"
    ]
    """<p>A map of tables and their respective keys that were not processed with the current response. The <code>UnprocessedKeys</code> value is in the same form as <code>RequestItems</code>, so the value can be provided directly to a subsequent <code>BatchGetItem</code> operation. For more information, see <code>RequestItems</code> in the Request Parameters section.</p> <p>Each element consists of:</p> <ul> <li> <p> <code>Keys</code> - An array of primary key attribute values that define specific items in the table.</p> </li> <li> <p> <code>ProjectionExpression</code> - One or more attributes to be retrieved from the table or index. By default, all attributes are returned. If a requested attribute is not found, it does not appear in the result.</p> </li> <li> <p> <code>ConsistentRead</code> - The consistency of a read operation. If set to <code>true</code>, then a strongly consistent read is used; otherwise, an eventually consistent read is used.</p> </li> </ul> <p>If there are no unprocessed keys remaining, the response contains an empty <code>UnprocessedKeys</code> map.</p>"""
    consumed_capacity: NotRequired[
        "capo_dynamodb.types.consumed_capacity_multiple.ConsumedCapacityMultiple"
    ]
    """<p>The read capacity units consumed by the entire <code>BatchGetItem</code> operation.</p> <p>Each element consists of:</p> <ul> <li> <p> <code>TableName</code> - The table that consumed the provisioned throughput.</p> </li> <li> <p> <code>CapacityUnits</code> - The total number of capacity units consumed.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetItemOutput) -> dict:
    out: dict = {}
    if "responses" in value:
        import capo_dynamodb.types.batch_get_response_map

        out["Responses"] = (
            capo_dynamodb.types.batch_get_response_map.serialize_aws_json_1_0(
                value["responses"]
            )
        )
    if "unprocessed_keys" in value:
        import capo_dynamodb.types.batch_get_request_map

        out["UnprocessedKeys"] = (
            capo_dynamodb.types.batch_get_request_map.serialize_aws_json_1_0(
                value["unprocessed_keys"]
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


def deserialize_aws_json_1_0(data: dict) -> BatchGetItemOutput:
    out: BatchGetItemOutput = {}  # type: ignore[typeddict-item]
    if "Responses" in data:
        import capo_dynamodb.types.batch_get_response_map

        out["responses"] = (
            capo_dynamodb.types.batch_get_response_map.deserialize_aws_json_1_0(
                data["Responses"]
            )
        )
    if "UnprocessedKeys" in data:
        import capo_dynamodb.types.batch_get_request_map

        out["unprocessed_keys"] = (
            capo_dynamodb.types.batch_get_request_map.deserialize_aws_json_1_0(
                data["UnprocessedKeys"]
            )
        )
    if "ConsumedCapacity" in data:
        import capo_dynamodb.types.consumed_capacity_multiple

        out["consumed_capacity"] = (
            capo_dynamodb.types.consumed_capacity_multiple.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    return out
