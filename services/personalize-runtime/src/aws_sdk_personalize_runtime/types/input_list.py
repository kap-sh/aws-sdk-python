"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#InputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.item_id

InputList: TypeAlias = list["aws_sdk_personalize_runtime.types.item_id.ItemID"]


# --- restJson1 ser/de ---
def serialize_json(value: InputList) -> list:
    return list(value)


def deserialize_json(data: list) -> InputList:
    return list(data)
