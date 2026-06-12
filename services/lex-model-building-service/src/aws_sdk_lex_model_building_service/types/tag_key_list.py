"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.tag_key

TagKeyList: TypeAlias = list["aws_sdk_lex_model_building_service.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeyList:
    return list(data)
