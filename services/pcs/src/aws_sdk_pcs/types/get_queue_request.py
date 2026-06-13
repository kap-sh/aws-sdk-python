"""Generated from Smithy shape ``com.amazonaws.pcs#GetQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pcs.types.cluster_identifier
    import aws_sdk_pcs.types.queue_identifier


class GetQueueRequest(TypedDict):
    cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster of the queue.</p>"""
    queue_identifier: "aws_sdk_pcs.types.queue_identifier.QueueIdentifier"
    """<p>The name or ID of the queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetQueueRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["queueIdentifier"] = value["queue_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetQueueRequest:
    out: GetQueueRequest = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError("GetQueueRequest.cluster_identifier required")
    if "queueIdentifier" in data:
        out["queue_identifier"] = data["queueIdentifier"]
    else:
        raise DeserializationError("GetQueueRequest.queue_identifier required")
    return out
