"""Generated from Smithy shape ``com.amazonaws.fms#GetComplianceDetailRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.aws_account_id
    import aws_sdk_fms.types.policy_id


class GetComplianceDetailRequest(TypedDict):
    policy_id: "aws_sdk_fms.types.policy_id.PolicyId"
    """<p>The ID of the policy that you want to get the details for. <code>PolicyId</code> is returned by <code>PutPolicy</code> and by <code>ListPolicies</code>.</p>"""
    member_account: "aws_sdk_fms.types.aws_account_id.AWSAccountId"
    """<p>The Amazon Web Services account that owns the resources that you want to get the details for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceDetailRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    out["MemberAccount"] = value["member_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceDetailRequest:
    out: GetComplianceDetailRequest = {}  # type: ignore[typeddict-item]
    if "PolicyId" in data:
        out["policy_id"] = data["PolicyId"]
    else:
        raise DeserializationError("GetComplianceDetailRequest.policy_id required")
    if "MemberAccount" in data:
        out["member_account"] = data["MemberAccount"]
    else:
        raise DeserializationError("GetComplianceDetailRequest.member_account required")
    return out
