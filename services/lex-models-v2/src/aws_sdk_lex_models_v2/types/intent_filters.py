"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.intent_filter

IntentFilters: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.intent_filter.IntentFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntentFilters) -> list:
    import aws_sdk_lex_models_v2.types.intent_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.intent_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntentFilters:
    import aws_sdk_lex_models_v2.types.intent_filter

    out: IntentFilters = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.intent_filter.deserialize_json(item))
    return out
