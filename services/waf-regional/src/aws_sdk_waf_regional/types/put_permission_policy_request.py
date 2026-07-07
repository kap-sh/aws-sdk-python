"""Generated from Smithy shape ``com.amazonaws.wafregional#PutPermissionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.policy_string
    import aws_sdk_waf_regional.types.resource_arn


class PutPermissionPolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_waf_regional.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.</p>"""
    policy: "aws_sdk_waf_regional.types.policy_string.PolicyString"
    """<p>The policy to attach to the specified RuleGroup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPermissionPolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPermissionPolicyRequest:
    out: PutPermissionPolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutPermissionPolicyRequest.resource_arn required")
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutPermissionPolicyRequest.policy required")
    return out
