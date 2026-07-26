"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateClusterKafkaVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class UpdateClusterKafkaVersionResponse(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    cluster_operation_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the cluster operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterKafkaVersionResponse) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "cluster_operation_arn" in value:
        out["clusterOperationArn"] = value["cluster_operation_arn"]
    return out


def deserialize_json(data: dict) -> UpdateClusterKafkaVersionResponse:
    out: UpdateClusterKafkaVersionResponse = {}  # type: ignore[typeddict-item]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "clusterOperationArn" in data:
        out["cluster_operation_arn"] = data["clusterOperationArn"]
    return out
