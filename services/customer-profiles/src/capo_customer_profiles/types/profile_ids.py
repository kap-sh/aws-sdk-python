"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.uuid

ProfileIds: TypeAlias = list["capo_customer_profiles.types.uuid.uuid"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ProfileIds:
    return list(data)
