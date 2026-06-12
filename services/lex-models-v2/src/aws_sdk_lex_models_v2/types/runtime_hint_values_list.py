"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#RuntimeHintValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.runtime_hint_value

RuntimeHintValuesList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.runtime_hint_value.RuntimeHintValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeHintValuesList) -> list:
    import aws_sdk_lex_models_v2.types.runtime_hint_value

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.runtime_hint_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuntimeHintValuesList:
    import aws_sdk_lex_models_v2.types.runtime_hint_value

    out: RuntimeHintValuesList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.runtime_hint_value.deserialize_json(item)
        )
    return out
