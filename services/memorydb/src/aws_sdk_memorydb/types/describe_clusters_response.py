"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeClustersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.cluster_list
    import aws_sdk_memorydb.types.string


class DescribeClustersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    clusters: NotRequired["aws_sdk_memorydb.types.cluster_list.ClusterList"]
    """<p>A list of clusters</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClustersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "clusters" in value:
        import aws_sdk_memorydb.types.cluster_list

        out["Clusters"] = aws_sdk_memorydb.types.cluster_list.serialize_aws_json_1_1(
            value["clusters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClustersResponse:
    out: DescribeClustersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Clusters" in data:
        import aws_sdk_memorydb.types.cluster_list

        out["clusters"] = aws_sdk_memorydb.types.cluster_list.deserialize_aws_json_1_1(
            data["Clusters"]
        )
    return out
