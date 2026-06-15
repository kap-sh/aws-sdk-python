"""Generated from Smithy shape ``com.amazonaws.eks#DescribeAddonVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.describe_addon_versions_request_max_results
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class DescribeAddonVersionsRequest(TypedDict):
    kubernetes_version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Kubernetes versions that you can use the add-on with.</p>"""
    max_results: NotRequired[
        "aws_sdk_eks.types.describe_addon_versions_request_max_results.DescribeAddonVersionsRequestMaxResults"
    ]
    """<p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    addon_name: NotRequired["aws_sdk_eks.types.string.String"]
    r"""<p>The name of the add-on. The name must match one of the names returned by <a href=\"https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html\"> <code>ListAddons</code> </a>.</p>"""
    types: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The type of the add-on. For valid <code>types</code>, don't specify a value for this property.</p>"""
    publishers: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The publisher of the add-on. For valid <code>publishers</code>, don't specify a value for this property.</p>"""
    owners: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The owner of the add-on. For valid <code>owners</code>, don't specify a value for this property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAddonVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAddonVersionsRequest:
    out: DescribeAddonVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
