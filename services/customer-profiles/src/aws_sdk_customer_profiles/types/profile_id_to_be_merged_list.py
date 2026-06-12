"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileIdToBeMergedList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.uuid

ProfileIdToBeMergedList: TypeAlias = list["aws_sdk_customer_profiles.types.uuid.uuid"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileIdToBeMergedList) -> list:
    return list(value)


def deserialize_json(data: list) -> ProfileIdToBeMergedList:
    return list(data)
