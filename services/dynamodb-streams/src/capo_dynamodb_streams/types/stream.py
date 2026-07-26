"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#Stream``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.stream_arn
    import capo_dynamodb_streams.types.string
    import capo_dynamodb_streams.types.table_name


class Stream(TypedDict, closed=True):
    stream_arn: NotRequired["capo_dynamodb_streams.types.stream_arn.StreamArn"]
    """<p>The Amazon Resource Name (ARN) for the stream.</p>"""
    table_name: NotRequired["capo_dynamodb_streams.types.table_name.TableName"]
    """<p>The DynamoDB table with which the stream is associated.</p>"""
    stream_label: NotRequired["capo_dynamodb_streams.types.string.String"]
    """<p>A timestamp, in ISO 8601 format, for this stream.</p> <p>Note that <code>LatestStreamLabel</code> is not a unique identifier for the stream, because it is possible that a stream from another table might have the same timestamp. However, the combination of the following three elements is guaranteed to be unique:</p> <ul> <li> <p>the Amazon Web Services customer ID.</p> </li> <li> <p>the table name</p> </li> <li> <p>the <code>StreamLabel</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Stream) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamArn"] = value["stream_arn"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "stream_label" in value:
        out["StreamLabel"] = value["stream_label"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Stream:
    out: Stream = {}  # type: ignore[typeddict-item]
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "StreamLabel" in data:
        out["stream_label"] = data["StreamLabel"]
    return out
