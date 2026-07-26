"""Generated from Smithy shape ``com.amazonaws.qapps#BatchCreateCategoryInputCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.batch_create_category_input_category

BatchCreateCategoryInputCategoryList: TypeAlias = list[
    "capo_qapps.types.batch_create_category_input_category.BatchCreateCategoryInputCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateCategoryInputCategoryList) -> list:
    import capo_qapps.types.batch_create_category_input_category

    out: list = []
    for item in value:
        out.append(
            capo_qapps.types.batch_create_category_input_category.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchCreateCategoryInputCategoryList:
    import capo_qapps.types.batch_create_category_input_category

    out: BatchCreateCategoryInputCategoryList = []
    for item in data:
        out.append(
            capo_qapps.types.batch_create_category_input_category.deserialize_json(item)
        )
    return out
