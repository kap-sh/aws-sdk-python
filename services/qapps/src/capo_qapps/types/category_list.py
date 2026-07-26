"""Generated from Smithy shape ``com.amazonaws.qapps#CategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.category

CategoryList: TypeAlias = list["capo_qapps.types.category.Category"]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryList) -> list:
    import capo_qapps.types.category

    out: list = []
    for item in value:
        out.append(capo_qapps.types.category.serialize_json(item))
    return out


def deserialize_json(data: list) -> CategoryList:
    import capo_qapps.types.category

    out: CategoryList = []
    for item in data:
        out.append(capo_qapps.types.category.deserialize_json(item))
    return out
