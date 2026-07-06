"""Generated from Smithy shape ``com.amazonaws.transfer#LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.log_group_name
    import aws_sdk_transfer.types.role


class LoggingConfiguration(TypedDict, closed=True):
    logging_role: NotRequired["aws_sdk_transfer.types.role.Role"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.</p>"""
    log_group_name: NotRequired["aws_sdk_transfer.types.log_group_name.LogGroupName"]
    """<p>The name of the CloudWatch logging group for the Transfer Family server to which this workflow belongs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoggingConfiguration) -> dict:
    out: dict = {}
    if "logging_role" in value:
        out["LoggingRole"] = value["logging_role"]
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "LoggingRole" in data:
        out["logging_role"] = data["LoggingRole"]
    if "LogGroupName" in data:
        out["log_group_name"] = data["LogGroupName"]
    return out
