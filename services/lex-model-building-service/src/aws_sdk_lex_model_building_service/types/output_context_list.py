"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#OutputContextList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.output_context

OutputContextList: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.output_context.OutputContext"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputContextList) -> list:
    import aws_sdk_lex_model_building_service.types.output_context

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.output_context.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OutputContextList:
    import aws_sdk_lex_model_building_service.types.output_context

    out: OutputContextList = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.output_context.deserialize_json(
                item
            )
        )
    return out
