"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.unused_action

UnusedActionList: TypeAlias = list[
    "capo_accessanalyzer.types.unused_action.UnusedAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnusedActionList) -> list:
    import capo_accessanalyzer.types.unused_action

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.unused_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> UnusedActionList:
    import capo_accessanalyzer.types.unused_action

    out: UnusedActionList = []
    for item in data:
        out.append(capo_accessanalyzer.types.unused_action.deserialize_json(item))
    return out
