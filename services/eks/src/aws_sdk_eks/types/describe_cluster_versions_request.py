"""Generated from Smithy shape ``com.amazonaws.eks#DescribeClusterVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boxed_boolean
    import aws_sdk_eks.types.cluster_version_status
    import aws_sdk_eks.types.describe_cluster_version_max_results
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list
    import aws_sdk_eks.types.version_status


class DescribeClusterVersionsRequest(TypedDict, closed=True):
    cluster_type: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The type of cluster to filter versions by.</p>"""
    max_results: NotRequired[
        "aws_sdk_eks.types.describe_cluster_version_max_results.DescribeClusterVersionMaxResults"
    ]
    """<p>Maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>Pagination token for the next set of results.</p>"""
    default_only: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Filter to show only default versions.</p>"""
    include_all: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Include all available versions in the response.</p>"""
    cluster_versions: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>List of specific cluster versions to describe.</p>"""
    status: NotRequired["aws_sdk_eks.types.cluster_version_status.ClusterVersionStatus"]
    """<important> <p>This field is deprecated. Use <code>versionStatus</code> instead, as that field matches for input and output of this action.</p> </important> <p>Filter versions by their current status.</p>"""
    version_status: NotRequired["aws_sdk_eks.types.version_status.VersionStatus"]
    """<p>Filter versions by their current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeClusterVersionsRequest:
    out: DescribeClusterVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
