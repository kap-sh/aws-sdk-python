"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterEventSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.cluster_event_level
    import capo_sagemaker.types.cluster_event_resource_type
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.cluster_name
    import capo_sagemaker.types.event_id
    import capo_sagemaker.types.timestamp


class ClusterEventSummary(TypedDict, closed=True):
    event_id: NotRequired["capo_sagemaker.types.event_id.EventId"]
    """<p>The unique identifier (UUID) of the event.</p>"""
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the HyperPod cluster associated with the event.</p>"""
    cluster_name: NotRequired["capo_sagemaker.types.cluster_name.ClusterName"]
    """<p>The name of the HyperPod cluster associated with the event.</p>"""
    instance_group_name: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>The name of the instance group associated with the event, if applicable.</p>"""
    instance_id: NotRequired["str"]
    """<p>The Amazon Elastic Compute Cloud (EC2) instance ID associated with the event, if applicable.</p>"""
    resource_type: NotRequired[
        "capo_sagemaker.types.cluster_event_resource_type.ClusterEventResourceType"
    ]
    """<p>The type of resource associated with the event. Valid values are <code>Cluster</code>, <code>InstanceGroup</code>, or <code>Instance</code>.</p>"""
    event_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the event occurred.</p>"""
    description: NotRequired["str"]
    """<p>A brief, human-readable description of the event.</p>"""
    event_level: NotRequired[
        "capo_sagemaker.types.cluster_event_level.ClusterEventLevel"
    ]
    """<p>The severity level of the event. Valid values are <code>Info</code>, <code>Warn</code>, and <code>Error</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterEventSummary) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["EventId"] = value["event_id"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "resource_type" in value:
        import capo_sagemaker.types.cluster_event_resource_type

        out["ResourceType"] = (
            capo_sagemaker.types.cluster_event_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "event_time" in value:
        import capo_sagemaker.types.timestamp

        out["EventTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["event_time"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "event_level" in value:
        import capo_sagemaker.types.cluster_event_level

        out["EventLevel"] = (
            capo_sagemaker.types.cluster_event_level.serialize_aws_json_1_1(
                value["event_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterEventSummary:
    out: ClusterEventSummary = {}  # type: ignore[typeddict-item]
    if "EventId" in data:
        out["event_id"] = data["EventId"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "InstanceGroupName" in data:
        out["instance_group_name"] = data["InstanceGroupName"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "ResourceType" in data:
        import capo_sagemaker.types.cluster_event_resource_type

        out["resource_type"] = (
            capo_sagemaker.types.cluster_event_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "EventTime" in data:
        import capo_sagemaker.types.timestamp

        out["event_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EventTime"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "EventLevel" in data:
        import capo_sagemaker.types.cluster_event_level

        out["event_level"] = (
            capo_sagemaker.types.cluster_event_level.deserialize_aws_json_1_1(
                data["EventLevel"]
            )
        )
    return out
