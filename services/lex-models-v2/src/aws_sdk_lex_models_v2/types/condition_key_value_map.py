"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConditionKeyValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.condition_key
    import aws_sdk_lex_models_v2.types.condition_value

ConditionKeyValueMap: TypeAlias = dict[
    "aws_sdk_lex_models_v2.types.condition_key.ConditionKey",
    "aws_sdk_lex_models_v2.types.condition_value.ConditionValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConditionKeyValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ConditionKeyValueMap:
    out: ConditionKeyValueMap = {}
    for key, value in data.items():
        out[key] = value
    return out
