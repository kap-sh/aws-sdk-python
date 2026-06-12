"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Slots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.non_empty_string
    import aws_sdk_lex_runtime_v2.types.slot

Slots: TypeAlias = dict[
    "aws_sdk_lex_runtime_v2.types.non_empty_string.NonEmptyString",
    "aws_sdk_lex_runtime_v2.types.slot.Slot",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Slots) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_lex_runtime_v2.types.slot

        out[key] = aws_sdk_lex_runtime_v2.types.slot.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Slots:
    out: Slots = {}
    for key, value in data.items():
        import aws_sdk_lex_runtime_v2.types.slot

        out[key] = aws_sdk_lex_runtime_v2.types.slot.deserialize_json(value)
    return out
