"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.intent_filter

IntentFilters: TypeAlias = list["capo_lex_models_v2.types.intent_filter.IntentFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: IntentFilters) -> list:
    import capo_lex_models_v2.types.intent_filter

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.intent_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntentFilters:
    import capo_lex_models_v2.types.intent_filter

    out: IntentFilters = []
    for item in data:
        out.append(capo_lex_models_v2.types.intent_filter.deserialize_json(item))
    return out
