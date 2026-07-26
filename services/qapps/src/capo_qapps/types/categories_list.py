"""Generated from Smithy shape ``com.amazonaws.qapps#CategoriesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.category

CategoriesList: TypeAlias = list["capo_qapps.types.category.Category"]


# --- restJson1 ser/de ---
def serialize_json(value: CategoriesList) -> list:
    import capo_qapps.types.category

    out: list = []
    for item in value:
        out.append(capo_qapps.types.category.serialize_json(item))
    return out


def deserialize_json(data: list) -> CategoriesList:
    import capo_qapps.types.category

    out: CategoriesList = []
    for item in data:
        out.append(capo_qapps.types.category.deserialize_json(item))
    return out
