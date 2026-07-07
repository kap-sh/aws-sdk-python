"""Generated from Smithy shape ``com.amazonaws.batch#AttemptDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.attempt_container_detail
    import aws_sdk_batch.types.list_attempt_ecs_task_details
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.string


class AttemptDetail(TypedDict, closed=True):
    container: NotRequired[
        "aws_sdk_batch.types.attempt_container_detail.AttemptContainerDetail"
    ]
    """<p>The details for the container in this job attempt.</p>"""
    started_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the attempt was started (when the attempt transitioned from the <code>STARTING</code> state to the <code>RUNNING</code> state).</p>"""
    stopped_at: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The Unix timestamp (in milliseconds) for when the attempt was stopped (when the attempt transitioned from the <code>RUNNING</code> state to a terminal state, such as <code>SUCCEEDED</code> or <code>FAILED</code>).</p>"""
    status_reason: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A short, human-readable string to provide additional details for the current status of the job attempt.</p>"""
    task_properties: NotRequired[
        "aws_sdk_batch.types.list_attempt_ecs_task_details.ListAttemptEcsTaskDetails"
    ]
    """<p>The properties for a task definition that describes the container and volume definitions of an Amazon ECS task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttemptDetail) -> dict:
    out: dict = {}
    if "container" in value:
        import aws_sdk_batch.types.attempt_container_detail

        out["container"] = aws_sdk_batch.types.attempt_container_detail.serialize_json(
            value["container"]
        )
    if "started_at" in value:
        out["startedAt"] = value["started_at"]
    if "stopped_at" in value:
        out["stoppedAt"] = value["stopped_at"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "task_properties" in value:
        import aws_sdk_batch.types.list_attempt_ecs_task_details

        out["taskProperties"] = (
            aws_sdk_batch.types.list_attempt_ecs_task_details.serialize_json(
                value["task_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> AttemptDetail:
    out: AttemptDetail = {}  # type: ignore[typeddict-item]
    if "container" in data:
        import aws_sdk_batch.types.attempt_container_detail

        out["container"] = (
            aws_sdk_batch.types.attempt_container_detail.deserialize_json(
                data["container"]
            )
        )
    if "startedAt" in data:
        out["started_at"] = data["startedAt"]
    if "stoppedAt" in data:
        out["stopped_at"] = data["stoppedAt"]
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "taskProperties" in data:
        import aws_sdk_batch.types.list_attempt_ecs_task_details

        out["task_properties"] = (
            aws_sdk_batch.types.list_attempt_ecs_task_details.deserialize_json(
                data["taskProperties"]
            )
        )
    return out
