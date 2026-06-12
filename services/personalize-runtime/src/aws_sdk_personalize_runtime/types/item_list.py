"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#ItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.predicted_item

ItemList: TypeAlias = list[
    "aws_sdk_personalize_runtime.types.predicted_item.PredictedItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ItemList) -> list:
    import aws_sdk_personalize_runtime.types.predicted_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize_runtime.types.predicted_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ItemList:
    import aws_sdk_personalize_runtime.types.predicted_item

    out: ItemList = []
    for item in data:
        out.append(
            aws_sdk_personalize_runtime.types.predicted_item.deserialize_json(item)
        )
    return out
