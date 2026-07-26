"""Generated from Smithy shape ``com.amazonaws.georoutes#LanguageTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.language_tag

LanguageTagList: TypeAlias = list["capo_geo_routes.types.language_tag.LanguageTag"]


# --- restJson1 ser/de ---
def serialize_json(value: LanguageTagList) -> list:
    return list(value)


def deserialize_json(data: list) -> LanguageTagList:
    return list(data)
