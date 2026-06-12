"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ActiveContextList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.active_context

ActiveContextList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.active_context.ActiveContext"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActiveContextList) -> list:
    import aws_sdk_lex_models_v2.types.active_context

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.active_context.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActiveContextList:
    import aws_sdk_lex_models_v2.types.active_context

    out: ActiveContextList = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.active_context.deserialize_json(item))
    return out
