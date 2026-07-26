"""Generated from Smithy shape ``com.amazonaws.codedeploy#CloudFormationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.cloud_formation_resource_type
    import capo_codedeploy.types.deployment_id
    import capo_codedeploy.types.lifecycle_event_list
    import capo_codedeploy.types.target_id
    import capo_codedeploy.types.target_status
    import capo_codedeploy.types.time
    import capo_codedeploy.types.traffic_weight


class CloudFormationTarget(TypedDict, closed=True):
    deployment_id: NotRequired["capo_codedeploy.types.deployment_id.DeploymentId"]
    """<p>The unique ID of an CloudFormation blue/green deployment.</p>"""
    target_id: NotRequired["capo_codedeploy.types.target_id.TargetId"]
    """<p> The unique ID of a deployment target that has a type of <code>CloudFormationTarget</code>. </p>"""
    last_updated_at: NotRequired["capo_codedeploy.types.time.Time"]
    """<p> The date and time when the target application was updated by an CloudFormation blue/green deployment. </p>"""
    lifecycle_events: NotRequired[
        "capo_codedeploy.types.lifecycle_event_list.LifecycleEventList"
    ]
    """<p> The lifecycle events of the CloudFormation blue/green deployment to this target application. </p>"""
    status: NotRequired["capo_codedeploy.types.target_status.TargetStatus"]
    """<p> The status of an CloudFormation blue/green deployment's target application. </p>"""
    resource_type: NotRequired[
        "capo_codedeploy.types.cloud_formation_resource_type.CloudFormationResourceType"
    ]
    """<p>The resource type for the CloudFormation blue/green deployment.</p>"""
    target_version_weight: "capo_codedeploy.types.traffic_weight.TrafficWeight"
    """<p>The percentage of production traffic that the target version of an CloudFormation blue/green deployment receives.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudFormationTarget) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    if "last_updated_at" in value:
        import capo_codedeploy.types.time

        out["lastUpdatedAt"] = capo_codedeploy.types.time.serialize_aws_json_1_1(
            value["last_updated_at"]
        )
    if "lifecycle_events" in value:
        import capo_codedeploy.types.lifecycle_event_list

        out["lifecycleEvents"] = (
            capo_codedeploy.types.lifecycle_event_list.serialize_aws_json_1_1(
                value["lifecycle_events"]
            )
        )
    if "status" in value:
        import capo_codedeploy.types.target_status

        out["status"] = capo_codedeploy.types.target_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    out["targetVersionWeight"] = value.get("target_version_weight", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudFormationTarget:
    out: CloudFormationTarget = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    if "lastUpdatedAt" in data:
        import capo_codedeploy.types.time

        out["last_updated_at"] = capo_codedeploy.types.time.deserialize_aws_json_1_1(
            data["lastUpdatedAt"]
        )
    if "lifecycleEvents" in data:
        import capo_codedeploy.types.lifecycle_event_list

        out["lifecycle_events"] = (
            capo_codedeploy.types.lifecycle_event_list.deserialize_aws_json_1_1(
                data["lifecycleEvents"]
            )
        )
    if "status" in data:
        import capo_codedeploy.types.target_status

        out["status"] = capo_codedeploy.types.target_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "targetVersionWeight" in data:
        out["target_version_weight"] = data["targetVersionWeight"]
    else:
        out["target_version_weight"] = 0
    return out
