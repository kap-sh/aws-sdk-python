"""Generated from Smithy shape ``com.amazonaws.ecs#Rollback``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class Rollback(TypedDict, closed=True):
    reason: NotRequired["capo_ecs.types.string.String"]
    """<p>The reason the rollback happened. For example, the circuit breaker initiated the rollback operation.</p>"""
    started_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>Time time that the rollback started. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    service_revision_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the service revision deployed as part of the rollback.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rollback) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "started_at" in value:
        import capo_ecs.types.timestamp

        out["startedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "service_revision_arn" in value:
        out["serviceRevisionArn"] = value["service_revision_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Rollback:
    out: Rollback = {}  # type: ignore[typeddict-item]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("startedAt") is not None:
        import capo_ecs.types.timestamp

        out["started_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["startedAt"]
        )
    if data.get("serviceRevisionArn") is not None:
        out["service_revision_arn"] = data["serviceRevisionArn"]
    return out
