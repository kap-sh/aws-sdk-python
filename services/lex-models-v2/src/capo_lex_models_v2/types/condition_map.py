"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConditionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.condition_key_value_map
    import capo_lex_models_v2.types.condition_operator

ConditionMap: TypeAlias = dict[
    "capo_lex_models_v2.types.condition_operator.ConditionOperator",
    "capo_lex_models_v2.types.condition_key_value_map.ConditionKeyValueMap",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConditionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lex_models_v2.types.condition_key_value_map

        out[key] = capo_lex_models_v2.types.condition_key_value_map.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ConditionMap:
    out: ConditionMap = {}
    for key, value in data.items():
        import capo_lex_models_v2.types.condition_key_value_map

        out[key] = capo_lex_models_v2.types.condition_key_value_map.deserialize_json(
            value
        )
    return out
