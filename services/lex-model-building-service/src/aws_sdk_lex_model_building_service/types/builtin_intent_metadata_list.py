"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BuiltinIntentMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.builtin_intent_metadata

BuiltinIntentMetadataList: TypeAlias = list[
    "aws_sdk_lex_model_building_service.types.builtin_intent_metadata.BuiltinIntentMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: BuiltinIntentMetadataList) -> list:
    import aws_sdk_lex_model_building_service.types.builtin_intent_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_model_building_service.types.builtin_intent_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BuiltinIntentMetadataList:
    import aws_sdk_lex_model_building_service.types.builtin_intent_metadata

    out: BuiltinIntentMetadataList = []
    for item in data:
        out.append(
            aws_sdk_lex_model_building_service.types.builtin_intent_metadata.deserialize_json(
                item
            )
        )
    return out
