"""Generated from Smithy shape ``com.amazonaws.mpa#ListResourcePoliciesResponseResourcePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.policy_type
    import capo_mpa.types.string


class ListResourcePoliciesResponseResourcePolicy(TypedDict, closed=True):
    policy_arn: NotRequired["capo_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for policy.</p>"""
    policy_type: NotRequired["capo_mpa.types.policy_type.PolicyType"]
    """<p>The type of policy.</p>"""
    policy_name: NotRequired["capo_mpa.types.string.String"]
    """<p>Name of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcePoliciesResponseResourcePolicy) -> dict:
    out: dict = {}
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    if "policy_type" in value:
        import capo_mpa.types.policy_type

        out["PolicyType"] = capo_mpa.types.policy_type.serialize_json(
            value["policy_type"]
        )
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_json(data: dict) -> ListResourcePoliciesResponseResourcePolicy:
    out: ListResourcePoliciesResponseResourcePolicy = {}  # type: ignore[typeddict-item]
    if "PolicyArn" in data:
        out["policy_arn"] = data["PolicyArn"]
    if "PolicyType" in data:
        import capo_mpa.types.policy_type

        out["policy_type"] = capo_mpa.types.policy_type.deserialize_json(
            data["PolicyType"]
        )
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    return out
