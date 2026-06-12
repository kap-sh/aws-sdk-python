"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OutputContextsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.output_context

OutputContextsList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.output_context.OutputContext"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputContextsList) -> list:
    import aws_sdk_lex_models_v2.types.output_context

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.output_context.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputContextsList:
    import aws_sdk_lex_models_v2.types.output_context

    out: OutputContextsList = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.output_context.deserialize_json(item))
    return out
