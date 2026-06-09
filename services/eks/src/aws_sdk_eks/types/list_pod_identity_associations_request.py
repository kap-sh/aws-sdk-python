"""Generated from Smithy shape ``com.amazonaws.eks#ListPodIdentityAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.list_pod_identity_associations_max_results
    import aws_sdk_eks.types.string


class ListPodIdentityAssociationsRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the cluster that the associations are in.</p>"""
    namespace: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the Kubernetes namespace inside the cluster that the associations are in.</p>"""
    service_account: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the Kubernetes service account that the associations use.</p>"""
    max_results: NotRequired[
        "aws_sdk_eks.types.list_pod_identity_associations_max_results.ListPodIdentityAssociationsMaxResults"
    ]
    """<p>The maximum number of EKS Pod Identity association results returned by <code>ListPodIdentityAssociations</code> in paginated output. When you use this parameter, <code>ListPodIdentityAssociations</code> returns only <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListPodIdentityAssociations</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListPodIdentityAssociations</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListUpdates</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPodIdentityAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPodIdentityAssociationsRequest:
    out: ListPodIdentityAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
