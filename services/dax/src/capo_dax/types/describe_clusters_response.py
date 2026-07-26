"""Generated from Smithy shape ``com.amazonaws.dax#DescribeClustersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.cluster_list
    import capo_dax.types.string


class DescribeClustersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_dax.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    clusters: NotRequired["capo_dax.types.cluster_list.ClusterList"]
    """<p>The descriptions of your DAX clusters, in response to a <i>DescribeClusters</i> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClustersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "clusters" in value:
        import capo_dax.types.cluster_list

        out["Clusters"] = capo_dax.types.cluster_list.serialize_aws_json_1_1(
            value["clusters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClustersResponse:
    out: DescribeClustersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Clusters" in data:
        import capo_dax.types.cluster_list

        out["clusters"] = capo_dax.types.cluster_list.deserialize_aws_json_1_1(
            data["Clusters"]
        )
    return out
