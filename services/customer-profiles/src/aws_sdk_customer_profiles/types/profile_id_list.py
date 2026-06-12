"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.uuid

ProfileIdList: TypeAlias = list["aws_sdk_customer_profiles.types.uuid.uuid"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ProfileIdList:
    return list(data)
