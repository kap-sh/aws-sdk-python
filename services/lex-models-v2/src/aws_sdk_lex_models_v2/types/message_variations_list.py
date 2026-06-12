"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#MessageVariationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.message

MessageVariationsList: TypeAlias = list["aws_sdk_lex_models_v2.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: MessageVariationsList) -> list:
    import aws_sdk_lex_models_v2.types.message

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.message.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageVariationsList:
    import aws_sdk_lex_models_v2.types.message

    out: MessageVariationsList = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.message.deserialize_json(item))
    return out
