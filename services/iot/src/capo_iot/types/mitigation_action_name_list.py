"""Generated from Smithy shape ``com.amazonaws.iot#MitigationActionNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.mitigation_action_name

MitigationActionNameList: TypeAlias = list[
    "capo_iot.types.mitigation_action_name.MitigationActionName"
]


# --- restJson1 ser/de ---
def serialize_json(value: MitigationActionNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> MitigationActionNameList:
    return list(data)
