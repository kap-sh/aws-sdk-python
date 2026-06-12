"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetDataProtectionPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_identifier


class GetDataProtectionPolicyRequest(TypedDict):
    log_group_identifier: (
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    """<p>The name or ARN of the log group that contains the data protection policy that you want to see.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataProtectionPolicyRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataProtectionPolicyRequest:
    out: GetDataProtectionPolicyRequest = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        raise DeserializationError(
            "GetDataProtectionPolicyRequest.log_group_identifier required"
        )
    return out
