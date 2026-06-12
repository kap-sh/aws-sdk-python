"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#InputContextList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.input_context

InputContextList: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.input_context.InputContext"
]


# --- restJson1 ser/de ---
def serialize_json(value: InputContextList) -> list:
    import aws_sdk_lex_model_building_service.types.input_context

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.input_context.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InputContextList:
    import aws_sdk_lex_model_building_service.types.input_context

    out: InputContextList = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.input_context.deserialize_json(
                item
            )
        )
    return out
