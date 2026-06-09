"""Generated from Smithy shape ``com.amazonaws.eks#ListAssociatedAccessPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.associated_access_policies_list
    import aws_sdk_eks.types.string


class ListAssociatedAccessPoliciesResponse(TypedDict):
    cluster_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of your cluster.</p>"""
    principal_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    associated_access_policies: NotRequired[
        "aws_sdk_eks.types.associated_access_policies_list.AssociatedAccessPoliciesList"
    ]
    """<p>The list of access policies associated with the access entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedAccessPoliciesResponse) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "associated_access_policies" in value:
        import aws_sdk_eks.types.associated_access_policies_list

        out["associatedAccessPolicies"] = (
            aws_sdk_eks.types.associated_access_policies_list.serialize_json(
                value["associated_access_policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListAssociatedAccessPoliciesResponse:
    out: ListAssociatedAccessPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "associatedAccessPolicies" in data:
        import aws_sdk_eks.types.associated_access_policies_list

        out["associated_access_policies"] = (
            aws_sdk_eks.types.associated_access_policies_list.deserialize_json(
                data["associatedAccessPolicies"]
            )
        )
    return out
