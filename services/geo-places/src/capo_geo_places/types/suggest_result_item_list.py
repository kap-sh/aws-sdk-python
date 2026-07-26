"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.suggest_result_item

SuggestResultItemList: TypeAlias = list[
    "capo_geo_places.types.suggest_result_item.SuggestResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestResultItemList) -> list:
    import capo_geo_places.types.suggest_result_item

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.suggest_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SuggestResultItemList:
    import capo_geo_places.types.suggest_result_item

    out: SuggestResultItemList = []
    for item in data:
        out.append(capo_geo_places.types.suggest_result_item.deserialize_json(item))
    return out
