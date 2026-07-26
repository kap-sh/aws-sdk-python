"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#OutputContextList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.output_context

OutputContextList: TypeAlias = list[
    "capo_lex_model_building_service.types.output_context.OutputContext"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutputContextList) -> list:
    import capo_lex_model_building_service.types.output_context

    out: list = []
    for item in value:
        out.append(
            capo_lex_model_building_service.types.output_context.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OutputContextList:
    import capo_lex_model_building_service.types.output_context

    out: OutputContextList = []
    for item in data:
        out.append(
            capo_lex_model_building_service.types.output_context.deserialize_json(item)
        )
    return out
