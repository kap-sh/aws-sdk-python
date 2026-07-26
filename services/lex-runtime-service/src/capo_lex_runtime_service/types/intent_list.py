"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#IntentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.predicted_intent

IntentList: TypeAlias = list[
    "capo_lex_runtime_service.types.predicted_intent.PredictedIntent"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntentList) -> list:
    import capo_lex_runtime_service.types.predicted_intent

    out: list = []
    for item in value:
        out.append(capo_lex_runtime_service.types.predicted_intent.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntentList:
    import capo_lex_runtime_service.types.predicted_intent

    out: IntentList = []
    for item in data:
        out.append(
            capo_lex_runtime_service.types.predicted_intent.deserialize_json(item)
        )
    return out
