"""Generated from Smithy shape ``com.amazonaws.iot#CreatePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policy_arn
    import capo_iot.types.policy_document
    import capo_iot.types.policy_name
    import capo_iot.types.policy_version_id


class CreatePolicyResponse(TypedDict, closed=True):
    policy_name: NotRequired["capo_iot.types.policy_name.PolicyName"]
    """<p>The policy name.</p>"""
    policy_arn: NotRequired["capo_iot.types.policy_arn.PolicyArn"]
    """<p>The policy ARN.</p>"""
    policy_document: NotRequired["capo_iot.types.policy_document.PolicyDocument"]
    """<p>The JSON document that describes the policy.</p>"""
    policy_version_id: NotRequired["capo_iot.types.policy_version_id.PolicyVersionId"]
    """<p>The policy version ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyResponse) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    if "policy_version_id" in value:
        out["policyVersionId"] = value["policy_version_id"]
    return out


def deserialize_json(data: dict) -> CreatePolicyResponse:
    out: CreatePolicyResponse = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    if "policyVersionId" in data:
        out["policy_version_id"] = data["policyVersionId"]
    return out
