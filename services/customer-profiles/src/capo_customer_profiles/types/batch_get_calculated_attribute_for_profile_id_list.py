"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetCalculatedAttributeForProfileIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.uuid

BatchGetCalculatedAttributeForProfileIdList: TypeAlias = list[
    "capo_customer_profiles.types.uuid.uuid"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCalculatedAttributeForProfileIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> BatchGetCalculatedAttributeForProfileIdList:
    return list(data)
