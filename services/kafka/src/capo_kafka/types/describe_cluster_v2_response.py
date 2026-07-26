"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.cluster


class DescribeClusterV2Response(TypedDict, closed=True):
    cluster_info: NotRequired["capo_kafka.types.cluster.Cluster"]
    """<p>The cluster information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterV2Response) -> dict:
    out: dict = {}
    if "cluster_info" in value:
        import capo_kafka.types.cluster

        out["clusterInfo"] = capo_kafka.types.cluster.serialize_json(
            value["cluster_info"]
        )
    return out


def deserialize_json(data: dict) -> DescribeClusterV2Response:
    out: DescribeClusterV2Response = {}  # type: ignore[typeddict-item]
    if "clusterInfo" in data:
        import capo_kafka.types.cluster

        out["cluster_info"] = capo_kafka.types.cluster.deserialize_json(
            data["clusterInfo"]
        )
    return out
