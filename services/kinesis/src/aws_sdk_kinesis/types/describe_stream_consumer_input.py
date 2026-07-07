"""Generated from Smithy shape ``com.amazonaws.kinesis#DescribeStreamConsumerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.consumer_arn
    import aws_sdk_kinesis.types.consumer_name
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_id


class DescribeStreamConsumerInput(TypedDict, closed=True):
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    r"""<p>The ARN of the Kinesis data stream that the consumer is registered with. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    consumer_name: NotRequired["aws_sdk_kinesis.types.consumer_name.ConsumerName"]
    """<p>The name that you gave to the consumer.</p>"""
    consumer_arn: NotRequired["aws_sdk_kinesis.types.consumer_arn.ConsumerARN"]
    """<p>The ARN returned by Kinesis Data Streams when you registered the consumer.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStreamConsumerInput) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "consumer_name" in value:
        out["ConsumerName"] = value["consumer_name"]
    if "consumer_arn" in value:
        out["ConsumerARN"] = value["consumer_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStreamConsumerInput:
    out: DescribeStreamConsumerInput = {}  # type: ignore[typeddict-item]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "ConsumerName" in data:
        out["consumer_name"] = data["ConsumerName"]
    if "ConsumerARN" in data:
        out["consumer_arn"] = data["ConsumerARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
