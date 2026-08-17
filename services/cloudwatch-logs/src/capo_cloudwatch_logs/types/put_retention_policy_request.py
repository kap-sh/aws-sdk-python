"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutRetentionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.days
    import capo_cloudwatch_logs.types.log_group_name


class PutRetentionPolicyRequest(TypedDict, closed=True):
    log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    retention_in_days: "capo_cloudwatch_logs.types.days.Days"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRetentionPolicyRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["retentionInDays"] = value["retention_in_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRetentionPolicyRequest:
    out: PutRetentionPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("PutRetentionPolicyRequest.log_group_name required")
    if data.get("retentionInDays") is not None:
        out["retention_in_days"] = data["retentionInDays"]
    else:
        raise DeserializationError(
            "PutRetentionPolicyRequest.retention_in_days required"
        )
    return out
