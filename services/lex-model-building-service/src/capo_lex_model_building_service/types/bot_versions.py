"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BotVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.version

BotVersions: TypeAlias = list["capo_lex_model_building_service.types.version.Version"]


# --- restJson1 ser/de ---
def serialize_json(value: BotVersions) -> list:
    return list(value)


def deserialize_json(data: list) -> BotVersions:
    return list(data)
