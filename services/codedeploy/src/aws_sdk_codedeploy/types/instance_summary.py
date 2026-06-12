"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_id
    import aws_sdk_codedeploy.types.instance_id
    import aws_sdk_codedeploy.types.instance_status
    import aws_sdk_codedeploy.types.instance_type
    import aws_sdk_codedeploy.types.lifecycle_event_list
    import aws_sdk_codedeploy.types.timestamp


class InstanceSummary(TypedDict):
    deployment_id: NotRequired["aws_sdk_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a deployment. </p>"""
    instance_id: NotRequired["aws_sdk_codedeploy.types.instance_id.InstanceId"]
    """<p>The instance ID.</p>"""
    status: NotRequired["aws_sdk_codedeploy.types.instance_status.InstanceStatus"]
    """<p>The deployment status for this instance:</p> <ul> <li> <p> <code>Pending</code>: The deployment is pending for this instance.</p> </li> <li> <p> <code>In Progress</code>: The deployment is in progress for this instance.</p> </li> <li> <p> <code>Succeeded</code>: The deployment has succeeded for this instance.</p> </li> <li> <p> <code>Failed</code>: The deployment has failed for this instance.</p> </li> <li> <p> <code>Skipped</code>: The deployment has been skipped for this instance.</p> </li> <li> <p> <code>Unknown</code>: The deployment status is unknown for this instance.</p> </li> </ul>"""
    last_updated_at: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the instance information was last updated.</p>"""
    lifecycle_events: NotRequired[
        "aws_sdk_codedeploy.types.lifecycle_event_list.LifecycleEventList"
    ]
    """<p>A list of lifecycle events for this instance.</p>"""
    instance_type: NotRequired["aws_sdk_codedeploy.types.instance_type.InstanceType"]
    """<p>Information about which environment an instance belongs to in a blue/green deployment.</p> <ul> <li> <p>BLUE: The instance is part of the original environment.</p> </li> <li> <p>GREEN: The instance is part of the replacement environment.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceSummary) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "status" in value:
        import aws_sdk_codedeploy.types.instance_status

        out["status"] = aws_sdk_codedeploy.types.instance_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "last_updated_at" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
                value["last_updated_at"]
            )
        )
    if "lifecycle_events" in value:
        import aws_sdk_codedeploy.types.lifecycle_event_list

        out["lifecycleEvents"] = (
            aws_sdk_codedeploy.types.lifecycle_event_list.serialize_aws_json_1_1(
                value["lifecycle_events"]
            )
        )
    if "instance_type" in value:
        import aws_sdk_codedeploy.types.instance_type

        out["instanceType"] = (
            aws_sdk_codedeploy.types.instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceSummary:
    out: InstanceSummary = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    if "status" in data:
        import aws_sdk_codedeploy.types.instance_status

        out["status"] = (
            aws_sdk_codedeploy.types.instance_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["lastUpdatedAt"]
            )
        )
    if "lifecycleEvents" in data:
        import aws_sdk_codedeploy.types.lifecycle_event_list

        out["lifecycle_events"] = (
            aws_sdk_codedeploy.types.lifecycle_event_list.deserialize_aws_json_1_1(
                data["lifecycleEvents"]
            )
        )
    if "instanceType" in data:
        import aws_sdk_codedeploy.types.instance_type

        out["instance_type"] = (
            aws_sdk_codedeploy.types.instance_type.deserialize_aws_json_1_1(
                data["instanceType"]
            )
        )
    return out
