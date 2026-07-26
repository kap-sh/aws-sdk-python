"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterOperationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.cluster_operation_info


class DescribeClusterOperationResponse(TypedDict, closed=True):
    cluster_operation_info: NotRequired[
        "capo_kafka.types.cluster_operation_info.ClusterOperationInfo"
    ]
    """<p>Cluster operation information</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterOperationResponse) -> dict:
    out: dict = {}
    if "cluster_operation_info" in value:
        import capo_kafka.types.cluster_operation_info

        out["clusterOperationInfo"] = (
            capo_kafka.types.cluster_operation_info.serialize_json(
                value["cluster_operation_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeClusterOperationResponse:
    out: DescribeClusterOperationResponse = {}  # type: ignore[typeddict-item]
    if "clusterOperationInfo" in data:
        import capo_kafka.types.cluster_operation_info

        out["cluster_operation_info"] = (
            capo_kafka.types.cluster_operation_info.deserialize_json(
                data["clusterOperationInfo"]
            )
        )
    return out
