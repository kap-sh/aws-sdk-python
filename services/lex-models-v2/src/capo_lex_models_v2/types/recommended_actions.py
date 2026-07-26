"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#RecommendedActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.recommended_action

RecommendedActions: TypeAlias = list[
    "capo_lex_models_v2.types.recommended_action.RecommendedAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendedActions) -> list:
    return list(value)


def deserialize_json(data: list) -> RecommendedActions:
    return list(data)
