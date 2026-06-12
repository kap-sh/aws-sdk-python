"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#ListStreamsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.positive_integer_object
    import aws_sdk_dynamodb_streams.types.stream_arn
    import aws_sdk_dynamodb_streams.types.table_name


class ListStreamsInput(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb_streams.types.table_name.TableName"]
    """<p>If this parameter is provided, then only the streams associated with this table name are returned.</p>"""
    limit: NotRequired[
        "aws_sdk_dynamodb_streams.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The maximum number of streams to return. The upper limit is 100.</p>"""
    exclusive_start_stream_arn: NotRequired[
        "aws_sdk_dynamodb_streams.types.stream_arn.StreamArn"
    ]
    """<p>The ARN (Amazon Resource Name) of the first item that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedStreamArn</code> in the previous operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListStreamsInput) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "exclusive_start_stream_arn" in value:
        out["ExclusiveStartStreamArn"] = value["exclusive_start_stream_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListStreamsInput:
    out: ListStreamsInput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "ExclusiveStartStreamArn" in data:
        out["exclusive_start_stream_arn"] = data["ExclusiveStartStreamArn"]
    return out
