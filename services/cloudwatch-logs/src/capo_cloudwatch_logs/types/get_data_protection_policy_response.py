"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDataProtectionPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.data_protection_policy_document
    import capo_cloudwatch_logs.types.log_group_identifier
    import capo_cloudwatch_logs.types.timestamp


class GetDataProtectionPolicyResponse(TypedDict, closed=True):
    log_group_identifier: NotRequired[
        "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>The log group name or ARN that you specified in your request.</p>"""
    policy_document: NotRequired[
        "capo_cloudwatch_logs.types.data_protection_policy_document.DataProtectionPolicyDocument"
    ]
    """<p>The data protection policy document for this log group.</p>"""
    last_updated_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The date and time that this policy was most recently updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataProtectionPolicyResponse) -> dict:
    out: dict = {}
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataProtectionPolicyResponse:
    out: GetDataProtectionPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifier") is not None:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    if data.get("lastUpdatedTime") is not None:
        out["last_updated_time"] = data["lastUpdatedTime"]
    return out
