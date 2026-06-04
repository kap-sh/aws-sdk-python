"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTaskSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.task_sets


class DescribeTaskSetsResponse(TypedDict):
    task_sets: NotRequired["aws_sdk_ecs.types.task_sets.TaskSets"]
    """<p>The list of task sets described.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTaskSetsResponse) -> dict:
    out: dict = {}
    if "task_sets" in value:
        import aws_sdk_ecs.types.task_sets

        out["taskSets"] = aws_sdk_ecs.types.task_sets.serialize_aws_json_1_1(
            value["task_sets"]
        )
    if "failures" in value:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTaskSetsResponse:
    out: DescribeTaskSetsResponse = {}  # type: ignore[typeddict-item]
    if "taskSets" in data:
        import aws_sdk_ecs.types.task_sets

        out["task_sets"] = aws_sdk_ecs.types.task_sets.deserialize_aws_json_1_1(
            data["taskSets"]
        )
    if "failures" in data:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
