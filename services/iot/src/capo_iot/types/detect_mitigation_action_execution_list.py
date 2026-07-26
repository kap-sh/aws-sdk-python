"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.detect_mitigation_action_execution

DetectMitigationActionExecutionList: TypeAlias = list[
    "capo_iot.types.detect_mitigation_action_execution.DetectMitigationActionExecution"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectMitigationActionExecutionList) -> list:
    import capo_iot.types.detect_mitigation_action_execution

    out: list = []
    for item in value:
        out.append(
            capo_iot.types.detect_mitigation_action_execution.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DetectMitigationActionExecutionList:
    import capo_iot.types.detect_mitigation_action_execution

    out: DetectMitigationActionExecutionList = []
    for item in data:
        out.append(
            capo_iot.types.detect_mitigation_action_execution.deserialize_json(item)
        )
    return out
