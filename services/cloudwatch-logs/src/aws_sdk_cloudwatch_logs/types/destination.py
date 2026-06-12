"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Destination``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.access_policy
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.destination_name
    import aws_sdk_cloudwatch_logs.types.role_arn
    import aws_sdk_cloudwatch_logs.types.target_arn
    import aws_sdk_cloudwatch_logs.types.timestamp


class Destination(TypedDict):
    destination_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.destination_name.DestinationName"
    ]
    """<p>The name of the destination.</p>"""
    target_arn: NotRequired["aws_sdk_cloudwatch_logs.types.target_arn.TargetArn"]
    """<p>The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).</p>"""
    role_arn: NotRequired["aws_sdk_cloudwatch_logs.types.role_arn.RoleArn"]
    """<p>A role for impersonation, used when delivering log events to the target.</p>"""
    access_policy: NotRequired[
        "aws_sdk_cloudwatch_logs.types.access_policy.AccessPolicy"
    ]
    """<p>An IAM policy document that governs which Amazon Web Services accounts can create subscription filters against this destination.</p>"""
    arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of this destination.</p>"""
    creation_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The creation time of the destination, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Destination) -> dict:
    out: dict = {}
    if "destination_name" in value:
        out["destinationName"] = value["destination_name"]
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "access_policy" in value:
        out["accessPolicy"] = value["access_policy"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "destinationName" in data:
        out["destination_name"] = data["destinationName"]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "accessPolicy" in data:
        out["access_policy"] = data["accessPolicy"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
    return out
