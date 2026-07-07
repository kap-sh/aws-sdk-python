"""Generated from Smithy shape ``com.amazonaws.ecs#GetTaskProtectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.protected_tasks


class GetTaskProtectionResponse(TypedDict, closed=True):
    protected_tasks: NotRequired["aws_sdk_ecs.types.protected_tasks.ProtectedTasks"]
    """<p>A list of tasks with the following information.</p> <ul> <li> <p> <code>taskArn</code>: The task ARN.</p> </li> <li> <p> <code>protectionEnabled</code>: The protection status of the task. If scale-in protection is turned on for a task, the value is <code>true</code>. Otherwise, it is <code>false</code>.</p> </li> <li> <p> <code>expirationDate</code>: The epoch time when protection for the task will expire.</p> </li> </ul>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTaskProtectionResponse) -> dict:
    out: dict = {}
    if "protected_tasks" in value:
        import aws_sdk_ecs.types.protected_tasks

        out["protectedTasks"] = (
            aws_sdk_ecs.types.protected_tasks.serialize_aws_json_1_1(
                value["protected_tasks"]
            )
        )
    if "failures" in value:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTaskProtectionResponse:
    out: GetTaskProtectionResponse = {}  # type: ignore[typeddict-item]
    if "protectedTasks" in data:
        import aws_sdk_ecs.types.protected_tasks

        out["protected_tasks"] = (
            aws_sdk_ecs.types.protected_tasks.deserialize_aws_json_1_1(
                data["protectedTasks"]
            )
        )
    if "failures" in data:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
