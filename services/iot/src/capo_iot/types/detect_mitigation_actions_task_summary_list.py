"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionsTaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.detect_mitigation_actions_task_summary

DetectMitigationActionsTaskSummaryList: TypeAlias = list[
    "capo_iot.types.detect_mitigation_actions_task_summary.DetectMitigationActionsTaskSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectMitigationActionsTaskSummaryList) -> list:
    import capo_iot.types.detect_mitigation_actions_task_summary

    out: list = []
    for item in value:
        out.append(
            capo_iot.types.detect_mitigation_actions_task_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DetectMitigationActionsTaskSummaryList:
    import capo_iot.types.detect_mitigation_actions_task_summary

    out: DetectMitigationActionsTaskSummaryList = []
    for item in data:
        out.append(
            capo_iot.types.detect_mitigation_actions_task_summary.deserialize_json(item)
        )
    return out
