"""Generated from Smithy shape ``com.amazonaws.codedeploy#ECSTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_id
    import aws_sdk_codedeploy.types.ecs_task_set_list
    import aws_sdk_codedeploy.types.lifecycle_event_list
    import aws_sdk_codedeploy.types.target_arn
    import aws_sdk_codedeploy.types.target_id
    import aws_sdk_codedeploy.types.target_status
    import aws_sdk_codedeploy.types.time


class ECSTarget(TypedDict, closed=True):
    deployment_id: NotRequired["aws_sdk_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a deployment. </p>"""
    target_id: NotRequired["aws_sdk_codedeploy.types.target_id.TargetId"]
    """<p> The unique ID of a deployment target that has a type of <code>ecsTarget</code>. </p>"""
    target_arn: NotRequired["aws_sdk_codedeploy.types.target_arn.TargetArn"]
    """<p> The Amazon Resource Name (ARN) of the target. </p>"""
    last_updated_at: NotRequired["aws_sdk_codedeploy.types.time.Time"]
    """<p> The date and time when the target Amazon ECS application was updated by a deployment. </p>"""
    lifecycle_events: NotRequired[
        "aws_sdk_codedeploy.types.lifecycle_event_list.LifecycleEventList"
    ]
    """<p> The lifecycle events of the deployment to this target Amazon ECS application. </p>"""
    status: NotRequired["aws_sdk_codedeploy.types.target_status.TargetStatus"]
    """<p> The status an Amazon ECS deployment's target ECS application. </p>"""
    task_sets_info: NotRequired[
        "aws_sdk_codedeploy.types.ecs_task_set_list.ECSTaskSetList"
    ]
    """<p> The <code>ECSTaskSet</code> objects associated with the ECS target. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ECSTarget) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "last_updated_at" in value:
        import aws_sdk_codedeploy.types.time

        out["lastUpdatedAt"] = aws_sdk_codedeploy.types.time.serialize_aws_json_1_1(
            value["last_updated_at"]
        )
    if "lifecycle_events" in value:
        import aws_sdk_codedeploy.types.lifecycle_event_list

        out["lifecycleEvents"] = (
            aws_sdk_codedeploy.types.lifecycle_event_list.serialize_aws_json_1_1(
                value["lifecycle_events"]
            )
        )
    if "status" in value:
        import aws_sdk_codedeploy.types.target_status

        out["status"] = aws_sdk_codedeploy.types.target_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "task_sets_info" in value:
        import aws_sdk_codedeploy.types.ecs_task_set_list

        out["taskSetsInfo"] = (
            aws_sdk_codedeploy.types.ecs_task_set_list.serialize_aws_json_1_1(
                value["task_sets_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ECSTarget:
    out: ECSTarget = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    if "lastUpdatedAt" in data:
        import aws_sdk_codedeploy.types.time

        out["last_updated_at"] = aws_sdk_codedeploy.types.time.deserialize_aws_json_1_1(
            data["lastUpdatedAt"]
        )
    if "lifecycleEvents" in data:
        import aws_sdk_codedeploy.types.lifecycle_event_list

        out["lifecycle_events"] = (
            aws_sdk_codedeploy.types.lifecycle_event_list.deserialize_aws_json_1_1(
                data["lifecycleEvents"]
            )
        )
    if "status" in data:
        import aws_sdk_codedeploy.types.target_status

        out["status"] = aws_sdk_codedeploy.types.target_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if "taskSetsInfo" in data:
        import aws_sdk_codedeploy.types.ecs_task_set_list

        out["task_sets_info"] = (
            aws_sdk_codedeploy.types.ecs_task_set_list.deserialize_aws_json_1_1(
                data["taskSetsInfo"]
            )
        )
    return out
