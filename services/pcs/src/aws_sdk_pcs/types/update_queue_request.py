"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pcs.types.cluster_identifier
    import aws_sdk_pcs.types.compute_node_group_configuration_list
    import aws_sdk_pcs.types.queue_identifier
    import aws_sdk_pcs.types.sb_client_token
    import aws_sdk_pcs.types.update_queue_slurm_configuration_request


class UpdateQueueRequest(TypedDict, closed=True):
    cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster of the queue.</p>"""
    queue_identifier: "aws_sdk_pcs.types.queue_identifier.QueueIdentifier"
    """<p>The name or ID of the queue.</p>"""
    compute_node_group_configurations: NotRequired[
        "aws_sdk_pcs.types.compute_node_group_configuration_list.ComputeNodeGroupConfigurationList"
    ]
    """<p>The list of compute node group configurations to associate with the queue. Queues assign jobs to associated compute node groups.</p>"""
    slurm_configuration: NotRequired[
        "aws_sdk_pcs.types.update_queue_slurm_configuration_request.UpdateQueueSlurmConfigurationRequest"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    client_token: NotRequired["aws_sdk_pcs.types.sb_client_token.SBClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateQueueRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["queueIdentifier"] = value["queue_identifier"]
    if "compute_node_group_configurations" in value:
        import aws_sdk_pcs.types.compute_node_group_configuration_list

        out["computeNodeGroupConfigurations"] = (
            aws_sdk_pcs.types.compute_node_group_configuration_list.serialize_aws_json_1_0(
                value["compute_node_group_configurations"]
            )
        )
    if "slurm_configuration" in value:
        import aws_sdk_pcs.types.update_queue_slurm_configuration_request

        out["slurmConfiguration"] = (
            aws_sdk_pcs.types.update_queue_slurm_configuration_request.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateQueueRequest:
    out: UpdateQueueRequest = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError("UpdateQueueRequest.cluster_identifier required")
    if "queueIdentifier" in data:
        out["queue_identifier"] = data["queueIdentifier"]
    else:
        raise DeserializationError("UpdateQueueRequest.queue_identifier required")
    if "computeNodeGroupConfigurations" in data:
        import aws_sdk_pcs.types.compute_node_group_configuration_list

        out["compute_node_group_configurations"] = (
            aws_sdk_pcs.types.compute_node_group_configuration_list.deserialize_aws_json_1_0(
                data["computeNodeGroupConfigurations"]
            )
        )
    if "slurmConfiguration" in data:
        import aws_sdk_pcs.types.update_queue_slurm_configuration_request

        out["slurm_configuration"] = (
            aws_sdk_pcs.types.update_queue_slurm_configuration_request.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
