"""Generated from Smithy shape ``com.amazonaws.emr#ListClustersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cluster_summary_list
    import capo_emr.types.marker


class ListClustersOutput(TypedDict, closed=True):
    clusters: NotRequired["capo_emr.types.cluster_summary_list.ClusterSummaryList"]
    """<p>The list of clusters for the account based on the given filters.</p>"""
    marker: NotRequired["capo_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClustersOutput) -> dict:
    out: dict = {}
    if "clusters" in value:
        import capo_emr.types.cluster_summary_list

        out["Clusters"] = capo_emr.types.cluster_summary_list.serialize_aws_json_1_1(
            value["clusters"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClustersOutput:
    out: ListClustersOutput = {}  # type: ignore[typeddict-item]
    if "Clusters" in data:
        import capo_emr.types.cluster_summary_list

        out["clusters"] = capo_emr.types.cluster_summary_list.deserialize_aws_json_1_1(
            data["Clusters"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
