"""Generated from Smithy shape ``com.amazonaws.ecs#ProtectedTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class ProtectedTask(TypedDict, closed=True):
    task_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The task ARN.</p>"""
    protection_enabled: "capo_ecs.types.boolean.Boolean"
    """<p>The protection status of the task. If scale-in protection is on for a task, the value is <code>true</code>. Otherwise, it is <code>false</code>.</p>"""
    expiration_date: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The epoch time when protection for the task will expire.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectedTask) -> dict:
    out: dict = {}
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
    out["protectionEnabled"] = value.get("protection_enabled", False)
    if "expiration_date" in value:
        import capo_ecs.types.timestamp

        out["expirationDate"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["expiration_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectedTask:
    out: ProtectedTask = {}  # type: ignore[typeddict-item]
    if "taskArn" in data:
        out["task_arn"] = data["taskArn"]
    if "protectionEnabled" in data:
        out["protection_enabled"] = data["protectionEnabled"]
    else:
        out["protection_enabled"] = False
    if "expirationDate" in data:
        import capo_ecs.types.timestamp

        out["expiration_date"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["expirationDate"]
        )
    return out
