"""Generated from Smithy shape ``com.amazonaws.batch#AttemptEcsTaskDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.list_attempt_task_container_details
    import aws_sdk_batch.types.string


class AttemptEcsTaskDetails(TypedDict):
    container_instance_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the container instance that hosts the task.</p>"""
    task_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The ARN of the Amazon ECS task.</p>"""
    containers: NotRequired[
        "aws_sdk_batch.types.list_attempt_task_container_details.ListAttemptTaskContainerDetails"
    ]
    """<p>A list of containers that are included in the <code>taskProperties</code> list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttemptEcsTaskDetails) -> dict:
    out: dict = {}
    if "container_instance_arn" in value:
        out["containerInstanceArn"] = value["container_instance_arn"]
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    if "containers" in value:
        import aws_sdk_batch.types.list_attempt_task_container_details

        out["containers"] = (
            aws_sdk_batch.types.list_attempt_task_container_details.serialize_json(
                value["containers"]
            )
        )
    return out


def deserialize_json(data: dict) -> AttemptEcsTaskDetails:
    out: AttemptEcsTaskDetails = {}  # type: ignore[typeddict-item]
    if "containerInstanceArn" in data:
        out["container_instance_arn"] = data["containerInstanceArn"]
    if "taskArn" in data:
        out["task_arn"] = data["taskArn"]
    if "containers" in data:
        import aws_sdk_batch.types.list_attempt_task_container_details

        out["containers"] = (
            aws_sdk_batch.types.list_attempt_task_container_details.deserialize_json(
                data["containers"]
            )
        )
    return out
