"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.tasks


class DescribeTasksResponse(TypedDict):
    tasks: NotRequired["aws_sdk_ecs.types.tasks.Tasks"]
    """<p>The list of tasks.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTasksResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> DescribeTasksResponse:
    out: DescribeTasksResponse = {}  # type: ignore[typeddict-item]
    if "tasks" in data:
        import aws_sdk_ecs.types.tasks

        out["tasks"] = aws_sdk_ecs.types.tasks.deserialize_aws_json_1_1(data["tasks"])
    if "failures" in data:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
