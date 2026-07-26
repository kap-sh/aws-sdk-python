"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#ActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_runtime.types.predicted_action

ActionList: TypeAlias = list[
    "capo_personalize_runtime.types.predicted_action.PredictedAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionList) -> list:
    import capo_personalize_runtime.types.predicted_action

    out: list = []
    for item in value:
        out.append(capo_personalize_runtime.types.predicted_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionList:
    import capo_personalize_runtime.types.predicted_action

    out: ActionList = []
    for item in data:
        out.append(
            capo_personalize_runtime.types.predicted_action.deserialize_json(item)
        )
    return out
