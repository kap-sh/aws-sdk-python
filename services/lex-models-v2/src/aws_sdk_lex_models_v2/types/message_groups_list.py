"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#MessageGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.message_group

MessageGroupsList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.message_group.MessageGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: MessageGroupsList) -> list:
    import aws_sdk_lex_models_v2.types.message_group

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.message_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageGroupsList:
    import aws_sdk_lex_models_v2.types.message_group

    out: MessageGroupsList = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.message_group.deserialize_json(item))
    return out
