"""Generated from Smithy shape ``com.amazonaws.qapps#CategoryListInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qapps.types.category_input

CategoryListInput: TypeAlias = list["aws_sdk_qapps.types.category_input.CategoryInput"]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryListInput) -> list:
    import aws_sdk_qapps.types.category_input

    out: list = []
    for item in value:
        out.append(aws_sdk_qapps.types.category_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> CategoryListInput:
    import aws_sdk_qapps.types.category_input

    out: CategoryListInput = []
    for item in data:
        out.append(aws_sdk_qapps.types.category_input.deserialize_json(item))
    return out
