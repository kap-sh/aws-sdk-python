"""Generated from Smithy shape ``com.amazonaws.iot#DescribeDetectMitigationActionsTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.detect_mitigation_actions_task_summary


class DescribeDetectMitigationActionsTaskResponse(TypedDict):
    task_summary: NotRequired[
        "aws_sdk_iot.types.detect_mitigation_actions_task_summary.DetectMitigationActionsTaskSummary"
    ]
    """<p> The description of a task. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDetectMitigationActionsTaskResponse) -> dict:
    out: dict = {}
    if "task_summary" in value:
        import aws_sdk_iot.types.detect_mitigation_actions_task_summary

        out["taskSummary"] = (
            aws_sdk_iot.types.detect_mitigation_actions_task_summary.serialize_json(
                value["task_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDetectMitigationActionsTaskResponse:
    out: DescribeDetectMitigationActionsTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskSummary" in data:
        import aws_sdk_iot.types.detect_mitigation_actions_task_summary

        out["task_summary"] = (
            aws_sdk_iot.types.detect_mitigation_actions_task_summary.deserialize_json(
                data["taskSummary"]
            )
        )
    return out
