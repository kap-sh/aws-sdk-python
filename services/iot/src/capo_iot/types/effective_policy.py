"""Generated from Smithy shape ``com.amazonaws.iot#EffectivePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policy_arn
    import capo_iot.types.policy_document
    import capo_iot.types.policy_name


class EffectivePolicy(TypedDict, closed=True):
    policy_name: NotRequired["capo_iot.types.policy_name.PolicyName"]
    """<p>The policy name.</p>"""
    policy_arn: NotRequired["capo_iot.types.policy_arn.PolicyArn"]
    """<p>The policy ARN.</p>"""
    policy_document: NotRequired["capo_iot.types.policy_document.PolicyDocument"]
    """<p>The IAM policy document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EffectivePolicy) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "policy_document" in value:
        out["policyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> EffectivePolicy:
    out: EffectivePolicy = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    return out
