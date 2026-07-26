"""Generated from Smithy shape ``com.amazonaws.iot#DetectMitigationActionsToExecuteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.mitigation_action_name

DetectMitigationActionsToExecuteList: TypeAlias = list[
    "capo_iot.types.mitigation_action_name.MitigationActionName"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectMitigationActionsToExecuteList) -> list:
    return list(value)


def deserialize_json(data: list) -> DetectMitigationActionsToExecuteList:
    return list(data)
