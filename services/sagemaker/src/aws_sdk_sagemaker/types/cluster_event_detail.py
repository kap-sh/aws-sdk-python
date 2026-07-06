"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterEventDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_arn
    import aws_sdk_sagemaker.types.cluster_event_level
    import aws_sdk_sagemaker.types.cluster_event_resource_type
    import aws_sdk_sagemaker.types.cluster_instance_group_name
    import aws_sdk_sagemaker.types.cluster_name
    import aws_sdk_sagemaker.types.event_details
    import aws_sdk_sagemaker.types.event_id
    import aws_sdk_sagemaker.types.timestamp


class ClusterEventDetail(TypedDict, closed=True):
    event_id: NotRequired["aws_sdk_sagemaker.types.event_id.EventId"]
    """<p>The unique identifier (UUID) of the event.</p>"""
    cluster_arn: NotRequired["aws_sdk_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the HyperPod cluster associated with the event.</p>"""
    cluster_name: NotRequired["aws_sdk_sagemaker.types.cluster_name.ClusterName"]
    """<p>The name of the HyperPod cluster associated with the event.</p>"""
    instance_group_name: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>The name of the instance group associated with the event, if applicable.</p>"""
    instance_id: NotRequired["str"]
    """<p>The EC2 instance ID associated with the event, if applicable.</p>"""
    resource_type: NotRequired[
        "aws_sdk_sagemaker.types.cluster_event_resource_type.ClusterEventResourceType"
    ]
    """<p>The type of resource associated with the event. Valid values are <code>Cluster</code>, <code>InstanceGroup</code>, or <code>Instance</code>.</p>"""
    event_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the event occurred.</p>"""
    event_details: NotRequired["aws_sdk_sagemaker.types.event_details.EventDetails"]
    """<p>Additional details about the event, including event-specific metadata.</p>"""
    description: NotRequired["str"]
    """<p>A human-readable description of the event.</p>"""
    event_level: NotRequired[
        "aws_sdk_sagemaker.types.cluster_event_level.ClusterEventLevel"
    ]
    """<p>The severity level of the event. Valid values are <code>Info</code>, <code>Warn</code>, and <code>Error</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterEventDetail) -> dict:
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
        import aws_sdk_sagemaker.types.cluster_event_resource_type

        out["ResourceType"] = (
            aws_sdk_sagemaker.types.cluster_event_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "event_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EventTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["event_time"]
        )
    if "event_details" in value:
        import aws_sdk_sagemaker.types.event_details

        out["EventDetails"] = (
            aws_sdk_sagemaker.types.event_details.serialize_aws_json_1_1(
                value["event_details"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "event_level" in value:
        import aws_sdk_sagemaker.types.cluster_event_level

        out["EventLevel"] = (
            aws_sdk_sagemaker.types.cluster_event_level.serialize_aws_json_1_1(
                value["event_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterEventDetail:
    out: ClusterEventDetail = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_sagemaker.types.cluster_event_resource_type

        out["resource_type"] = (
            aws_sdk_sagemaker.types.cluster_event_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if "EventTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["event_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EventTime"]
        )
    if "EventDetails" in data:
        import aws_sdk_sagemaker.types.event_details

        out["event_details"] = (
            aws_sdk_sagemaker.types.event_details.deserialize_aws_json_1_1(
                data["EventDetails"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "EventLevel" in data:
        import aws_sdk_sagemaker.types.cluster_event_level

        out["event_level"] = (
            aws_sdk_sagemaker.types.cluster_event_level.deserialize_aws_json_1_1(
                data["EventLevel"]
            )
        )
    return out
