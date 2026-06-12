"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterOperationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.cluster_operation_info


class DescribeClusterOperationResponse(TypedDict):
    cluster_operation_info: NotRequired[
        "aws_sdk_kafka.types.cluster_operation_info.ClusterOperationInfo"
    ]
    """<p>Cluster operation information</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterOperationResponse) -> dict:
    out: dict = {}
    if "cluster_operation_info" in value:
        import aws_sdk_kafka.types.cluster_operation_info

        out["clusterOperationInfo"] = (
            aws_sdk_kafka.types.cluster_operation_info.serialize_json(
                value["cluster_operation_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeClusterOperationResponse:
    out: DescribeClusterOperationResponse = {}  # type: ignore[typeddict-item]
    if "clusterOperationInfo" in data:
        import aws_sdk_kafka.types.cluster_operation_info

        out["cluster_operation_info"] = (
            aws_sdk_kafka.types.cluster_operation_info.deserialize_json(
                data["clusterOperationInfo"]
            )
        )
    return out
