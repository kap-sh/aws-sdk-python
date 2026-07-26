"""Generated from Smithy shape ``com.amazonaws.qapps#CategoryIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.uuid

CategoryIdList: TypeAlias = list["capo_qapps.types.uuid.UUID"]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> CategoryIdList:
    return list(data)
