"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchGetProfileIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.uuid

BatchGetProfileIdList: TypeAlias = list["capo_customer_profiles.types.uuid.uuid"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetProfileIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> BatchGetProfileIdList:
    return list(data)
