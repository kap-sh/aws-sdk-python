"""Generated from Smithy shape ``com.amazonaws.ssm#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.policy_hash
    import aws_sdk_ssm.types.policy_id


class PutResourcePolicyResponse(TypedDict):
    policy_id: NotRequired["aws_sdk_ssm.types.policy_id.PolicyId"]
    """<p>The policy ID. To update a policy, you must specify <code>PolicyId</code> and <code>PolicyHash</code>.</p>"""
    policy_hash: NotRequired["aws_sdk_ssm.types.policy_hash.PolicyHash"]
    """<p>ID of the current policy version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyResponse) -> dict:
    out: dict = {}
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "policy_hash" in value:
        out["PolicyHash"] = value["policy_hash"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyResponse:
    out: PutResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyId" in data:
        out["policy_id"] = data["PolicyId"]
    if "PolicyHash" in data:
        out["policy_hash"] = data["PolicyHash"]
    return out
