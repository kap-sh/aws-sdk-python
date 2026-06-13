"""Generated from Smithy shape ``com.amazonaws.pcs#CreateQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pcs.types.cluster_identifier
    import aws_sdk_pcs.types.compute_node_group_configuration_list
    import aws_sdk_pcs.types.queue_name
    import aws_sdk_pcs.types.queue_slurm_configuration_request
    import aws_sdk_pcs.types.request_tag_map
    import aws_sdk_pcs.types.sb_client_token


class CreateQueueRequest(TypedDict):
    cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster for which to create a queue.</p>"""
    queue_name: "aws_sdk_pcs.types.queue_name.QueueName"
    """<p>A name to identify the queue.</p>"""
    compute_node_group_configurations: NotRequired[
        "aws_sdk_pcs.types.compute_node_group_configuration_list.ComputeNodeGroupConfigurationList"
    ]
    """<p>The list of compute node group configurations to associate with the queue. Queues assign jobs to associated compute node groups.</p>"""
    slurm_configuration: NotRequired[
        "aws_sdk_pcs.types.queue_slurm_configuration_request.QueueSlurmConfigurationRequest"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    client_token: NotRequired["aws_sdk_pcs.types.sb_client_token.SBClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>"""
    tags: NotRequired["aws_sdk_pcs.types.request_tag_map.RequestTagMap"]
    """<p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateQueueRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["queueName"] = value["queue_name"]
    if "compute_node_group_configurations" in value:
        import aws_sdk_pcs.types.compute_node_group_configuration_list

        out["computeNodeGroupConfigurations"] = (
            aws_sdk_pcs.types.compute_node_group_configuration_list.serialize_aws_json_1_0(
                value["compute_node_group_configurations"]
            )
        )
    if "slurm_configuration" in value:
        import aws_sdk_pcs.types.queue_slurm_configuration_request

        out["slurmConfiguration"] = (
            aws_sdk_pcs.types.queue_slurm_configuration_request.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_pcs.types.request_tag_map

        out["tags"] = aws_sdk_pcs.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateQueueRequest:
    out: CreateQueueRequest = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError("CreateQueueRequest.cluster_identifier required")
    if "queueName" in data:
        out["queue_name"] = data["queueName"]
    else:
        raise DeserializationError("CreateQueueRequest.queue_name required")
    if "computeNodeGroupConfigurations" in data:
        import aws_sdk_pcs.types.compute_node_group_configuration_list

        out["compute_node_group_configurations"] = (
            aws_sdk_pcs.types.compute_node_group_configuration_list.deserialize_aws_json_1_0(
                data["computeNodeGroupConfigurations"]
            )
        )
    if "slurmConfiguration" in data:
        import aws_sdk_pcs.types.queue_slurm_configuration_request

        out["slurm_configuration"] = (
            aws_sdk_pcs.types.queue_slurm_configuration_request.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_pcs.types.request_tag_map

        out["tags"] = aws_sdk_pcs.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
