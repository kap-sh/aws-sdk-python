"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#LocaleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.locale

LocaleList: TypeAlias = list["capo_lex_model_building_service.types.locale.Locale"]


# --- restJson1 ser/de ---
def serialize_json(value: LocaleList) -> list:
    import capo_lex_model_building_service.types.locale

    out: list = []
    for item in value:
        out.append(capo_lex_model_building_service.types.locale.serialize_json(item))
    return out


def deserialize_json(data: list) -> LocaleList:
    import capo_lex_model_building_service.types.locale

    out: LocaleList = []
    for item in data:
        out.append(capo_lex_model_building_service.types.locale.deserialize_json(item))
    return out
