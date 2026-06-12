"""Generated from Smithy shape ``com.amazonaws.qapps#DeleteCategoryInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qapps.types.uuid

DeleteCategoryInputList: TypeAlias = list["aws_sdk_qapps.types.uuid.UUID"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCategoryInputList) -> list:
    return list(value)


def deserialize_json(data: list) -> DeleteCategoryInputList:
    return list(data)
