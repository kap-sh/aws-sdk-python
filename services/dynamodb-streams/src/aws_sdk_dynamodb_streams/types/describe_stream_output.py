"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#DescribeStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.stream_description


class DescribeStreamOutput(TypedDict, closed=True):
    stream_description: NotRequired[
        "aws_sdk_dynamodb_streams.types.stream_description.StreamDescription"
    ]
    """<p>A complete description of the stream, including its creation date and time, the DynamoDB table associated with the stream, the shard IDs within the stream, and the beginning and ending sequence numbers of stream records within the shards.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeStreamOutput) -> dict:
    out: dict = {}
    if "stream_description" in value:
        import aws_sdk_dynamodb_streams.types.stream_description

        out["StreamDescription"] = (
            aws_sdk_dynamodb_streams.types.stream_description.serialize_aws_json_1_0(
                value["stream_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeStreamOutput:
    out: DescribeStreamOutput = {}  # type: ignore[typeddict-item]
    if "StreamDescription" in data:
        import aws_sdk_dynamodb_streams.types.stream_description

        out["stream_description"] = (
            aws_sdk_dynamodb_streams.types.stream_description.deserialize_aws_json_1_0(
                data["StreamDescription"]
            )
        )
    return out
