"""Generated from Smithy shape ``com.amazonaws.qapps#BatchCreateCategoryInputCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qapps.types.batch_create_category_input_category

BatchCreateCategoryInputCategoryList: TypeAlias = list[
    "aws_sdk_qapps.types.batch_create_category_input_category.BatchCreateCategoryInputCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateCategoryInputCategoryList) -> list:
    import aws_sdk_qapps.types.batch_create_category_input_category

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qapps.types.batch_create_category_input_category.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateCategoryInputCategoryList:
    import aws_sdk_qapps.types.batch_create_category_input_category

    out: BatchCreateCategoryInputCategoryList = []
    for item in data:
        out.append(
            aws_sdk_qapps.types.batch_create_category_input_category.deserialize_json(
                item
            )
        )
    return out
