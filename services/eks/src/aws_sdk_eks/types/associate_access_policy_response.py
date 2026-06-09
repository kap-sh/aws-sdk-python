"""Generated from Smithy shape ``com.amazonaws.eks#AssociateAccessPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.associated_access_policy
    import aws_sdk_eks.types.string


class AssociateAccessPolicyResponse(TypedDict):
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of your cluster.</p>"""
    principal_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>"""
    associated_access_policy: NotRequired[
        "aws_sdk_eks.types.associated_access_policy.AssociatedAccessPolicy"
    ]
    """<p>The <code>AccessPolicy</code> and scope associated to the <code>AccessEntry</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAccessPolicyResponse) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    if "associated_access_policy" in value:
        import aws_sdk_eks.types.associated_access_policy

        out["associatedAccessPolicy"] = (
            aws_sdk_eks.types.associated_access_policy.serialize_json(
                value["associated_access_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateAccessPolicyResponse:
    out: AssociateAccessPolicyResponse = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    if "associatedAccessPolicy" in data:
        import aws_sdk_eks.types.associated_access_policy

        out["associated_access_policy"] = (
            aws_sdk_eks.types.associated_access_policy.deserialize_json(
                data["associatedAccessPolicy"]
            )
        )
    return out
