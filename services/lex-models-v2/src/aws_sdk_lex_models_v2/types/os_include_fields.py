"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OSIncludeFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.include_field

OSIncludeFields: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.include_field.IncludeField"
]


# --- restJson1 ser/de ---
def serialize_json(value: OSIncludeFields) -> list:
    return list(value)


def deserialize_json(data: list) -> OSIncludeFields:
    return list(data)
