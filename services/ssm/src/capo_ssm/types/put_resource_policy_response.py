"""Generated from Smithy shape ``com.amazonaws.ssm#PutResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.policy_hash
    import capo_ssm.types.policy_id


class PutResourcePolicyResponse(TypedDict, closed=True):
    policy_id: NotRequired["capo_ssm.types.policy_id.PolicyId"]
    """<p>The policy ID. To update a policy, you must specify <code>PolicyId</code> and <code>PolicyHash</code>.</p>"""
    policy_hash: NotRequired["capo_ssm.types.policy_hash.PolicyHash"]
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
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    if data.get("PolicyHash") is not None:
        out["policy_hash"] = data["PolicyHash"]
    return out
