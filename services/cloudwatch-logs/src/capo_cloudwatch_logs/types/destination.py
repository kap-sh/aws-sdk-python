"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.access_policy
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.destination_name
    import capo_cloudwatch_logs.types.role_arn
    import capo_cloudwatch_logs.types.target_arn
    import capo_cloudwatch_logs.types.timestamp


class Destination(TypedDict, closed=True):
    destination_name: NotRequired[
        "capo_cloudwatch_logs.types.destination_name.DestinationName"
    ]
    """<p>The name of the destination.</p>"""
    target_arn: NotRequired["capo_cloudwatch_logs.types.target_arn.TargetArn"]
    """<p>The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).</p>"""
    role_arn: NotRequired["capo_cloudwatch_logs.types.role_arn.RoleArn"]
    """<p>A role for impersonation, used when delivering log events to the target.</p>"""
    access_policy: NotRequired["capo_cloudwatch_logs.types.access_policy.AccessPolicy"]
    """<p>An IAM policy document that governs which Amazon Web Services accounts can create subscription filters against this destination.</p>"""
    arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of this destination.</p>"""
    creation_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
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
    if data.get("destinationName") is not None:
        out["destination_name"] = data["destinationName"]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("accessPolicy") is not None:
        out["access_policy"] = data["accessPolicy"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("creationTime") is not None:
        out["creation_time"] = data["creationTime"]
    return out
