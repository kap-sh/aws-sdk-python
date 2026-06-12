"""Generated from Smithy shape ``com.amazonaws.guardduty#EcsClusterDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.ecs_task_details
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tags


class EcsClusterDetails(TypedDict):
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the ECS Cluster.</p>"""
    arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the cluster.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The status of the ECS cluster.</p>"""
    active_services_count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The number of services that are running on the cluster in an ACTIVE state.</p>"""
    registered_container_instances_count: NotRequired[
        "aws_sdk_guardduty.types.integer.Integer"
    ]
    """<p>The number of container instances registered into the cluster.</p>"""
    running_tasks_count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The number of tasks in the cluster that are in the RUNNING state.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tags.Tags"]
    """<p>The tags of the ECS Cluster.</p>"""
    task_details: NotRequired["aws_sdk_guardduty.types.ecs_task_details.EcsTaskDetails"]
    """<p>Contains information about the details of the ECS Task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsClusterDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "active_services_count" in value:
        out["activeServicesCount"] = value["active_services_count"]
    if "registered_container_instances_count" in value:
        out["registeredContainerInstancesCount"] = value[
            "registered_container_instances_count"
        ]
    if "running_tasks_count" in value:
        out["runningTasksCount"] = value["running_tasks_count"]
    if "tags" in value:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.serialize_json(value["tags"])
    if "task_details" in value:
        import aws_sdk_guardduty.types.ecs_task_details

        out["taskDetails"] = aws_sdk_guardduty.types.ecs_task_details.serialize_json(
            value["task_details"]
        )
    return out


def deserialize_json(data: dict) -> EcsClusterDetails:
    out: EcsClusterDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        out["status"] = data["status"]
    if "activeServicesCount" in data:
        out["active_services_count"] = data["activeServicesCount"]
    if "registeredContainerInstancesCount" in data:
        out["registered_container_instances_count"] = data[
            "registeredContainerInstancesCount"
        ]
    if "runningTasksCount" in data:
        out["running_tasks_count"] = data["runningTasksCount"]
    if "tags" in data:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.deserialize_json(data["tags"])
    if "taskDetails" in data:
        import aws_sdk_guardduty.types.ecs_task_details

        out["task_details"] = aws_sdk_guardduty.types.ecs_task_details.deserialize_json(
            data["taskDetails"]
        )
    return out
