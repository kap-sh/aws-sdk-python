"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ButtonsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.button

ButtonsList: TypeAlias = list["aws_sdk_lex_runtime_v2.types.button.Button"]


# --- restJson1 ser/de ---
def serialize_json(value: ButtonsList) -> list:
    import aws_sdk_lex_runtime_v2.types.button

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_runtime_v2.types.button.serialize_json(item))
    return out


def deserialize_json(data: list) -> ButtonsList:
    import aws_sdk_lex_runtime_v2.types.button

    out: ButtonsList = []
    for item in data:
        out.append(aws_sdk_lex_runtime_v2.types.button.deserialize_json(item))
    return out
