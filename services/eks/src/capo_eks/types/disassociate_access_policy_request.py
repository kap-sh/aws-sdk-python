"""Generated from Smithy shape ``com.amazonaws.eks#DisassociateAccessPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DisassociateAccessPolicyRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    principal_arn: "capo_eks.types.string.String"
    """<p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>"""
    policy_arn: "capo_eks.types.string.String"
    """<p>The ARN of the policy to disassociate from the access entry. For a list of associated policies ARNs, use <code>ListAssociatedAccessPolicies</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAccessPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateAccessPolicyRequest:
    out: DisassociateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
