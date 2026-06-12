"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ActiveContextsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.active_context

ActiveContextsList: TypeAlias = list[
    "aws_sdk_lex_runtime_v2.types.active_context.ActiveContext"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActiveContextsList) -> list:
    import aws_sdk_lex_runtime_v2.types.active_context

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_runtime_v2.types.active_context.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActiveContextsList:
    import aws_sdk_lex_runtime_v2.types.active_context

    out: ActiveContextsList = []
    for item in data:
        out.append(aws_sdk_lex_runtime_v2.types.active_context.deserialize_json(item))
    return out
