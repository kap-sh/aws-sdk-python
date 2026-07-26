"""Generated from Smithy shape ``com.amazonaws.appflow#TriggerTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.trigger_type

TriggerTypeList: TypeAlias = list["capo_appflow.types.trigger_type.TriggerType"]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerTypeList) -> list:
    import capo_appflow.types.trigger_type

    out: list = []
    for item in value:
        out.append(capo_appflow.types.trigger_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> TriggerTypeList:
    import capo_appflow.types.trigger_type

    out: TriggerTypeList = []
    for item in data:
        out.append(capo_appflow.types.trigger_type.deserialize_json(item))
    return out
