"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDataProtectionPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.data_protection_policy_document
    import aws_sdk_cloudwatch_logs.types.log_group_identifier
    import aws_sdk_cloudwatch_logs.types.timestamp


class PutDataProtectionPolicyResponse(TypedDict):
    log_group_identifier: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>The log group name or ARN that you specified in your request.</p>"""
    policy_document: NotRequired[
        "aws_sdk_cloudwatch_logs.types.data_protection_policy_document.DataProtectionPolicyDocument"
    ]
    """<p>The data protection policy used for this log group.</p>"""
    last_updated_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The date and time that this policy was most recently updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDataProtectionPolicyResponse) -> dict:
    out: dict = {}
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDataProtectionPolicyResponse:
    out: PutDataProtectionPolicyResponse = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    return out
