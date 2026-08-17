"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_task_definition_status
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class DaemonTaskDefinitionSummary(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon task definition.</p>"""
    registered_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon task definition was registered.</p>"""
    registered_by: NotRequired["capo_ecs.types.string.String"]
    """<p>The principal that registered the daemon task definition.</p>"""
    delete_requested_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon task definition delete was requested.</p>"""
    status: NotRequired[
        "capo_ecs.types.daemon_task_definition_status.DaemonTaskDefinitionStatus"
    ]
    """<p>The status of the daemon task definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonTaskDefinitionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "registered_at" in value:
        import capo_ecs.types.timestamp

        out["registeredAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["registered_at"]
        )
    if "registered_by" in value:
        out["registeredBy"] = value["registered_by"]
    if "delete_requested_at" in value:
        import capo_ecs.types.timestamp

        out["deleteRequestedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["delete_requested_at"]
        )
    if "status" in value:
        import capo_ecs.types.daemon_task_definition_status

        out["status"] = (
            capo_ecs.types.daemon_task_definition_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonTaskDefinitionSummary:
    out: DaemonTaskDefinitionSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("registeredAt") is not None:
        import capo_ecs.types.timestamp

        out["registered_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["registeredAt"]
        )
    if data.get("registeredBy") is not None:
        out["registered_by"] = data["registeredBy"]
    if data.get("deleteRequestedAt") is not None:
        import capo_ecs.types.timestamp

        out["delete_requested_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["deleteRequestedAt"]
        )
    if data.get("status") is not None:
        import capo_ecs.types.daemon_task_definition_status

        out["status"] = (
            capo_ecs.types.daemon_task_definition_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
