"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonRollback``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.timestamp


class DaemonRollback(TypedDict, closed=True):
    reason: NotRequired["capo_ecs.types.string.String"]
    """<p>The reason the rollback happened. For example, the circuit breaker initiated the rollback operation.</p>"""
    started_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The time that the rollback started. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    rollback_target_daemon_revision_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the daemon revision deployed as part of the rollback.</p>"""
    rollback_capacity_providers: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The capacity providers involved in the rollback.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonRollback) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "started_at" in value:
        import capo_ecs.types.timestamp

        out["startedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "rollback_target_daemon_revision_arn" in value:
        out["rollbackTargetDaemonRevisionArn"] = value[
            "rollback_target_daemon_revision_arn"
        ]
    if "rollback_capacity_providers" in value:
        import capo_ecs.types.string_list

        out["rollbackCapacityProviders"] = (
            capo_ecs.types.string_list.serialize_aws_json_1_1(
                value["rollback_capacity_providers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonRollback:
    out: DaemonRollback = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("startedAt") is not None:
        import capo_ecs.types.timestamp

        out["started_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    if data.get("rollbackTargetDaemonRevisionArn") is not None:
        out["rollback_target_daemon_revision_arn"] = data[
            "rollbackTargetDaemonRevisionArn"
        ]
    if data.get("rollbackCapacityProviders") is not None:
        import capo_ecs.types.string_list

        out["rollback_capacity_providers"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["rollbackCapacityProviders"]
            )
        )
    return out
