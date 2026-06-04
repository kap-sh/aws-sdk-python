"""Generated from Smithy shape ``com.amazonaws.ecs#StartTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.tasks


class StartTaskResponse(TypedDict):
    tasks: NotRequired["aws_sdk_ecs.types.tasks.Tasks"]
    """<p>A full description of the tasks that were started. Each task that was successfully placed on your container instances is described.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTaskResponse) -> dict:
    out: dict = {}
    if "tasks" in value:
        import aws_sdk_ecs.types.tasks

        out["tasks"] = aws_sdk_ecs.types.tasks.serialize_aws_json_1_1(value["tasks"])
    if "failures" in value:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTaskResponse:
    out: StartTaskResponse = {}  # type: ignore[typeddict-item]
    if "tasks" in data:
        import aws_sdk_ecs.types.tasks

        out["tasks"] = aws_sdk_ecs.types.tasks.deserialize_aws_json_1_1(data["tasks"])
    if "failures" in data:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
