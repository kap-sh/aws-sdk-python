"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_task_definition_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DaemonTaskDefinitionSummary(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon task definition.</p>"""
    registered_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon task definition was registered.</p>"""
    registered_by: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The principal that registered the daemon task definition.</p>"""
    delete_requested_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon task definition delete was requested.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.daemon_task_definition_status.DaemonTaskDefinitionStatus"
    ]
    """<p>The status of the daemon task definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonTaskDefinitionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "registered_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["registeredAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["registered_at"]
        )
    if "registered_by" in value:
        out["registeredBy"] = value["registered_by"]
    if "delete_requested_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["deleteRequestedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["delete_requested_at"]
        )
    if "status" in value:
        import aws_sdk_ecs.types.daemon_task_definition_status

        out["status"] = (
            aws_sdk_ecs.types.daemon_task_definition_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonTaskDefinitionSummary:
    out: DaemonTaskDefinitionSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "registeredAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["registered_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["registeredAt"]
        )
    if "registeredBy" in data:
        out["registered_by"] = data["registeredBy"]
    if "deleteRequestedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["delete_requested_at"] = (
            aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
                data["deleteRequestedAt"]
            )
        )
    if "status" in data:
        import aws_sdk_ecs.types.daemon_task_definition_status

        out["status"] = (
            aws_sdk_ecs.types.daemon_task_definition_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
