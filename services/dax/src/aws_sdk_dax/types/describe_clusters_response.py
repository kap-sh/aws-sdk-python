"""Generated from Smithy shape ``com.amazonaws.dax#DescribeClustersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.cluster_list
    import aws_sdk_dax.types.string


class DescribeClustersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    clusters: NotRequired["aws_sdk_dax.types.cluster_list.ClusterList"]
    """<p>The descriptions of your DAX clusters, in response to a <i>DescribeClusters</i> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClustersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "clusters" in value:
        import aws_sdk_dax.types.cluster_list

        out["Clusters"] = aws_sdk_dax.types.cluster_list.serialize_aws_json_1_1(
            value["clusters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClustersResponse:
    out: DescribeClustersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Clusters" in data:
        import aws_sdk_dax.types.cluster_list

        out["clusters"] = aws_sdk_dax.types.cluster_list.deserialize_aws_json_1_1(
            data["Clusters"]
        )
    return out
