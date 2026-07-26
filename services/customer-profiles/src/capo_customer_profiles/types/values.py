"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Values``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to255

Values: TypeAlias = list["capo_customer_profiles.types.string1_to255.string1To255"]


# --- restJson1 ser/de ---
def serialize_json(value: Values) -> list:
    return list(value)


def deserialize_json(data: list) -> Values:
    return list(data)
