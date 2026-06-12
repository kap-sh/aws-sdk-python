"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.slot_type_value

SlotTypeValues: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.slot_type_value.SlotTypeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeValues) -> list:
    import aws_sdk_lex_models_v2.types.slot_type_value

    out: list = []
    for item in value:
        out.append(aws_sdk_lex_models_v2.types.slot_type_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> SlotTypeValues:
    import aws_sdk_lex_models_v2.types.slot_type_value

    out: SlotTypeValues = []
    for item in data:
        out.append(aws_sdk_lex_models_v2.types.slot_type_value.deserialize_json(item))
    return out
