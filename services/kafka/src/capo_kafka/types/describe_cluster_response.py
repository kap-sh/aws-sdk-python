"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.cluster_info


class DescribeClusterResponse(TypedDict, closed=True):
    cluster_info: NotRequired["capo_kafka.types.cluster_info.ClusterInfo"]
    """<p>The cluster information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterResponse) -> dict:
    out: dict = {}
    if "cluster_info" in value:
        import capo_kafka.types.cluster_info

        out["clusterInfo"] = capo_kafka.types.cluster_info.serialize_json(
            value["cluster_info"]
        )
    return out


def deserialize_json(data: dict) -> DescribeClusterResponse:
    out: DescribeClusterResponse = {}  # type: ignore[typeddict-item]
    if "clusterInfo" in data:
        import capo_kafka.types.cluster_info

        out["cluster_info"] = capo_kafka.types.cluster_info.deserialize_json(
            data["clusterInfo"]
        )
    return out
