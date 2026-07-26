"""Generated from Smithy shape ``com.amazonaws.iot#DescribeDetectMitigationActionsTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.detect_mitigation_actions_task_summary


class DescribeDetectMitigationActionsTaskResponse(TypedDict, closed=True):
    task_summary: NotRequired[
        "capo_iot.types.detect_mitigation_actions_task_summary.DetectMitigationActionsTaskSummary"
    ]
    """<p> The description of a task. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDetectMitigationActionsTaskResponse) -> dict:
    out: dict = {}
    if "task_summary" in value:
        import capo_iot.types.detect_mitigation_actions_task_summary

        out["taskSummary"] = (
            capo_iot.types.detect_mitigation_actions_task_summary.serialize_json(
                value["task_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDetectMitigationActionsTaskResponse:
    out: DescribeDetectMitigationActionsTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskSummary" in data:
        import capo_iot.types.detect_mitigation_actions_task_summary

        out["task_summary"] = (
            capo_iot.types.detect_mitigation_actions_task_summary.deserialize_json(
                data["taskSummary"]
            )
        )
    return out
