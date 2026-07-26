"""Generated from Smithy shape ``com.amazonaws.kafka#VpcConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.__timestamp_iso8601
    import capo_kafka.types.vpc_connection_state


class VpcConnection(TypedDict, closed=True):
    vpc_connection_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ARN that identifies the Vpc Connection.</p>"""
    target_cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ARN that identifies the Cluster which the Vpc Connection belongs to.</p>"""
    creation_time: NotRequired[
        "capo_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>Creation time of the Vpc Connection.</p>"""
    authentication: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Information about the auth scheme of Vpc Connection.</p>"""
    vpc_id: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The vpcId that belongs to the Vpc Connection.</p>"""
    state: NotRequired["capo_kafka.types.vpc_connection_state.VpcConnectionState"]
    """<p>State of the Vpc Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConnection) -> dict:
    out: dict = {}
    if "vpc_connection_arn" in value:
        out["vpcConnectionArn"] = value["vpc_connection_arn"]
    if "target_cluster_arn" in value:
        out["targetClusterArn"] = value["target_cluster_arn"]
    if "creation_time" in value:
        import capo_kafka.types.__timestamp_iso8601

        out["creationTime"] = capo_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "authentication" in value:
        out["authentication"] = value["authentication"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "state" in value:
        import capo_kafka.types.vpc_connection_state

        out["state"] = capo_kafka.types.vpc_connection_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> VpcConnection:
    out: VpcConnection = {}  # type: ignore[typeddict-item]
    if "vpcConnectionArn" in data:
        out["vpc_connection_arn"] = data["vpcConnectionArn"]
    if "targetClusterArn" in data:
        out["target_cluster_arn"] = data["targetClusterArn"]
    if "creationTime" in data:
        import capo_kafka.types.__timestamp_iso8601

        out["creation_time"] = capo_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "authentication" in data:
        out["authentication"] = data["authentication"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "state" in data:
        import capo_kafka.types.vpc_connection_state

        out["state"] = capo_kafka.types.vpc_connection_state.deserialize_json(
            data["state"]
        )
    return out
