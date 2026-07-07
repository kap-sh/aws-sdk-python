"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeMultiRegionClustersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.boolean_optional
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.string


class DescribeMultiRegionClustersRequest(TypedDict, closed=True):
    multi_region_cluster_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of a specific multi-Region cluster to describe.</p>"""
    max_results: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>A token to specify where to start paginating.</p>"""
    show_cluster_details: NotRequired[
        "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Details about the multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMultiRegionClustersRequest) -> dict:
    out: dict = {}
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "show_cluster_details" in value:
        out["ShowClusterDetails"] = value["show_cluster_details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMultiRegionClustersRequest:
    out: DescribeMultiRegionClustersRequest = {}  # type: ignore[typeddict-item]
    if "MultiRegionClusterName" in data:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ShowClusterDetails" in data:
        out["show_cluster_details"] = data["ShowClusterDetails"]
    return out
