"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.cluster


class DescribeClusterV2Response(TypedDict):
    cluster_info: NotRequired["aws_sdk_kafka.types.cluster.Cluster"]
    """<p>The cluster information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterV2Response) -> dict:
    out: dict = {}
    if "cluster_info" in value:
        import aws_sdk_kafka.types.cluster

        out["clusterInfo"] = aws_sdk_kafka.types.cluster.serialize_json(
            value["cluster_info"]
        )
    return out


def deserialize_json(data: dict) -> DescribeClusterV2Response:
    out: DescribeClusterV2Response = {}  # type: ignore[typeddict-item]
    if "clusterInfo" in data:
        import aws_sdk_kafka.types.cluster

        out["cluster_info"] = aws_sdk_kafka.types.cluster.deserialize_json(
            data["clusterInfo"]
        )
    return out
