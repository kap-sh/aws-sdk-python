"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterOperationV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.cluster_operation_v2


class DescribeClusterOperationV2Response(TypedDict, closed=True):
    cluster_operation_info: NotRequired[
        "capo_kafka.types.cluster_operation_v2.ClusterOperationV2"
    ]
    """<p>Cluster operation information</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterOperationV2Response) -> dict:
    out: dict = {}
    if "cluster_operation_info" in value:
        import capo_kafka.types.cluster_operation_v2

        out["clusterOperationInfo"] = (
            capo_kafka.types.cluster_operation_v2.serialize_json(
                value["cluster_operation_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeClusterOperationV2Response:
    out: DescribeClusterOperationV2Response = {}  # type: ignore[typeddict-item]
    if "clusterOperationInfo" in data:
        import capo_kafka.types.cluster_operation_v2

        out["cluster_operation_info"] = (
            capo_kafka.types.cluster_operation_v2.deserialize_json(
                data["clusterOperationInfo"]
            )
        )
    return out
