"""Generated from Smithy shape ``com.amazonaws.iot#Policy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.policy_arn
    import capo_iot.types.policy_name


class Policy(TypedDict, closed=True):
    policy_name: NotRequired["capo_iot.types.policy_name.PolicyName"]
    """<p>The policy name.</p>"""
    policy_arn: NotRequired["capo_iot.types.policy_arn.PolicyArn"]
    """<p>The policy ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Policy) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> Policy:
    out: Policy = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    return out
