"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductTitleFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.machine_learning_product_title_string

MachineLearningProductTitleFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.machine_learning_product_title_string.MachineLearningProductTitleString"
]


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductTitleFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> MachineLearningProductTitleFilterValueList:
    return list(data)
