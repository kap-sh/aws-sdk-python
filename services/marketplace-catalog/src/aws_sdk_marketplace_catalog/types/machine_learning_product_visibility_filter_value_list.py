"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductVisibilityFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_string

MachineLearningProductVisibilityFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_string.MachineLearningProductVisibilityString"
]


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductVisibilityFilterValueList) -> list:
    import aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_string

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MachineLearningProductVisibilityFilterValueList:
    import aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_string

    out: MachineLearningProductVisibilityFilterValueList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_string.deserialize_json(
                item
            )
        )
    return out
