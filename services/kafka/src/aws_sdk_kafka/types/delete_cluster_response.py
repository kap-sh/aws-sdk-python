"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.cluster_state


class DeleteClusterResponse(TypedDict, closed=True):
    cluster_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    state: NotRequired["aws_sdk_kafka.types.cluster_state.ClusterState"]
    """<p>The state of the cluster. The possible states are ACTIVE, CREATING, DELETING, FAILED, HEALING, MAINTENANCE, REBOOTING_BROKER, and UPDATING.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterResponse) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "state" in value:
        import aws_sdk_kafka.types.cluster_state

        out["state"] = aws_sdk_kafka.types.cluster_state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> DeleteClusterResponse:
    out: DeleteClusterResponse = {}  # type: ignore[typeddict-item]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "state" in data:
        import aws_sdk_kafka.types.cluster_state

        out["state"] = aws_sdk_kafka.types.cluster_state.deserialize_json(data["state"])
    return out
