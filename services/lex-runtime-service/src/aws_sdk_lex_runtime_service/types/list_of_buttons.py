"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#listOfButtons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.button

listOfButtons: TypeAlias = list["aws_sdk_lex_runtime_service.types.button.Button"]


# --- restJson1 ser/de ---
def serialize_json(value: listOfButtons) -> list:
    import aws_sdk_lex_runtime_service.types.button

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_runtime_service.types.button.serialize_json(item))
    return out


def deserialize_json(data: list) -> listOfButtons:
    import aws_sdk_lex_runtime_service.types.button

    out: listOfButtons = []
    for item in data:
        out.append(aws_sdk_lex_runtime_service.types.button.deserialize_json(item))
    return out
