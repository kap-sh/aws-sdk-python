"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.destination_name
    import aws_sdk_cloudwatch_logs.types.role_arn
    import aws_sdk_cloudwatch_logs.types.tags
    import aws_sdk_cloudwatch_logs.types.target_arn


class PutDestinationRequest(TypedDict):
    destination_name: "aws_sdk_cloudwatch_logs.types.destination_name.DestinationName"
    """<p>A name for the destination.</p>"""
    target_arn: "aws_sdk_cloudwatch_logs.types.target_arn.TargetArn"
    """<p>The ARN of an Amazon Kinesis stream to which to deliver matching log events.</p>"""
    role_arn: "aws_sdk_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The ARN of an IAM role that grants CloudWatch Logs permissions to call the Amazon Kinesis <code>PutRecord</code> operation on the destination stream.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch_logs.types.tags.Tags"]
    """<p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDestinationRequest) -> dict:
    out: dict = {}
    out["destinationName"] = value["destination_name"]
    out["targetArn"] = value["target_arn"]
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDestinationRequest:
    out: PutDestinationRequest = {}  # type: ignore[typeddict-item]
    if "destinationName" in data:
        out["destination_name"] = data["destinationName"]
    else:
        raise DeserializationError("PutDestinationRequest.destination_name required")
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("PutDestinationRequest.target_arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("PutDestinationRequest.role_arn required")
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
