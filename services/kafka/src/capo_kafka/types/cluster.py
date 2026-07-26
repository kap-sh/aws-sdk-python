"""Generated from Smithy shape ``com.amazonaws.kafka#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__map_of__string
    import capo_kafka.types.__string
    import capo_kafka.types.__timestamp_iso8601
    import capo_kafka.types.cluster_state
    import capo_kafka.types.cluster_type
    import capo_kafka.types.provisioned
    import capo_kafka.types.serverless
    import capo_kafka.types.state_info


class Cluster(TypedDict, closed=True):
    active_operation_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a cluster operation.</p>"""
    cluster_type: NotRequired["capo_kafka.types.cluster_type.ClusterType"]
    """<p>Cluster Type.</p>"""
    cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    cluster_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the cluster.</p>"""
    creation_time: NotRequired[
        "capo_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the cluster was created.</p>"""
    current_version: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The current version of the MSK cluster.</p>"""
    state: NotRequired["capo_kafka.types.cluster_state.ClusterState"]
    """<p>The state of the cluster. The possible states are ACTIVE, CREATING, DELETING, FAILED, HEALING, MAINTENANCE, REBOOTING_BROKER, and UPDATING.</p>"""
    state_info: NotRequired["capo_kafka.types.state_info.StateInfo"]
    """<p>State Info for the Amazon MSK cluster.</p>"""
    tags: NotRequired["capo_kafka.types.__map_of__string.__mapOf__string"]
    """<p>Tags attached to the cluster.</p>"""
    provisioned: NotRequired["capo_kafka.types.provisioned.Provisioned"]
    """<p>Information about the provisioned cluster.</p>"""
    serverless: NotRequired["capo_kafka.types.serverless.Serverless"]
    """<p>Information about the serverless cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cluster) -> dict:
    out: dict = {}
    if "active_operation_arn" in value:
        out["activeOperationArn"] = value["active_operation_arn"]
    if "cluster_type" in value:
        import capo_kafka.types.cluster_type

        out["clusterType"] = capo_kafka.types.cluster_type.serialize_json(
            value["cluster_type"]
        )
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "creation_time" in value:
        import capo_kafka.types.__timestamp_iso8601

        out["creationTime"] = capo_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "state" in value:
        import capo_kafka.types.cluster_state

        out["state"] = capo_kafka.types.cluster_state.serialize_json(value["state"])
    if "state_info" in value:
        import capo_kafka.types.state_info

        out["stateInfo"] = capo_kafka.types.state_info.serialize_json(
            value["state_info"]
        )
    if "tags" in value:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.serialize_json(value["tags"])
    if "provisioned" in value:
        import capo_kafka.types.provisioned

        out["provisioned"] = capo_kafka.types.provisioned.serialize_json(
            value["provisioned"]
        )
    if "serverless" in value:
        import capo_kafka.types.serverless

        out["serverless"] = capo_kafka.types.serverless.serialize_json(
            value["serverless"]
        )
    return out


def deserialize_json(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if "activeOperationArn" in data:
        out["active_operation_arn"] = data["activeOperationArn"]
    if "clusterType" in data:
        import capo_kafka.types.cluster_type

        out["cluster_type"] = capo_kafka.types.cluster_type.deserialize_json(
            data["clusterType"]
        )
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "creationTime" in data:
        import capo_kafka.types.__timestamp_iso8601

        out["creation_time"] = capo_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "state" in data:
        import capo_kafka.types.cluster_state

        out["state"] = capo_kafka.types.cluster_state.deserialize_json(data["state"])
    if "stateInfo" in data:
        import capo_kafka.types.state_info

        out["state_info"] = capo_kafka.types.state_info.deserialize_json(
            data["stateInfo"]
        )
    if "tags" in data:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.deserialize_json(data["tags"])
    if "provisioned" in data:
        import capo_kafka.types.provisioned

        out["provisioned"] = capo_kafka.types.provisioned.deserialize_json(
            data["provisioned"]
        )
    if "serverless" in data:
        import capo_kafka.types.serverless

        out["serverless"] = capo_kafka.types.serverless.deserialize_json(
            data["serverless"]
        )
    return out
