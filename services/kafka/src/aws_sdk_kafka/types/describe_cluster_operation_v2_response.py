"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeClusterOperationV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.cluster_operation_v2


class DescribeClusterOperationV2Response(TypedDict):
    cluster_operation_info: NotRequired[
        "aws_sdk_kafka.types.cluster_operation_v2.ClusterOperationV2"
    ]
    """<p>Cluster operation information</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterOperationV2Response) -> dict:
    out: dict = {}
    if "cluster_operation_info" in value:
        import aws_sdk_kafka.types.cluster_operation_v2

        out["clusterOperationInfo"] = (
            aws_sdk_kafka.types.cluster_operation_v2.serialize_json(
                value["cluster_operation_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeClusterOperationV2Response:
    out: DescribeClusterOperationV2Response = {}  # type: ignore[typeddict-item]
    if "clusterOperationInfo" in data:
        import aws_sdk_kafka.types.cluster_operation_v2

        out["cluster_operation_info"] = (
            aws_sdk_kafka.types.cluster_operation_v2.deserialize_json(
                data["clusterOperationInfo"]
            )
        )
    return out
