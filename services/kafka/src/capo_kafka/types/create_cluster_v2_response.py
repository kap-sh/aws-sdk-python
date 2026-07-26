"""Generated from Smithy shape ``com.amazonaws.kafka#CreateClusterV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.cluster_state
    import capo_kafka.types.cluster_type


class CreateClusterV2Response(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    cluster_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the MSK cluster.</p>"""
    state: NotRequired["capo_kafka.types.cluster_state.ClusterState"]
    """<p>The state of the cluster. The possible states are ACTIVE, CREATING, DELETING, FAILED, HEALING, MAINTENANCE, REBOOTING_BROKER, and UPDATING.</p>"""
    cluster_type: NotRequired["capo_kafka.types.cluster_type.ClusterType"]
    """<p>The type of the cluster. The possible states are PROVISIONED or SERVERLESS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterV2Response) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "state" in value:
        import capo_kafka.types.cluster_state

        out["state"] = capo_kafka.types.cluster_state.serialize_json(value["state"])
    if "cluster_type" in value:
        import capo_kafka.types.cluster_type

        out["clusterType"] = capo_kafka.types.cluster_type.serialize_json(
            value["cluster_type"]
        )
    return out


def deserialize_json(data: dict) -> CreateClusterV2Response:
    out: CreateClusterV2Response = {}  # type: ignore[typeddict-item]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "state" in data:
        import capo_kafka.types.cluster_state

        out["state"] = capo_kafka.types.cluster_state.deserialize_json(data["state"])
    if "clusterType" in data:
        import capo_kafka.types.cluster_type

        out["cluster_type"] = capo_kafka.types.cluster_type.deserialize_json(
            data["clusterType"]
        )
    return out
