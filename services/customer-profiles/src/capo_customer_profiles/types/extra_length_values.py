"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ExtraLengthValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to1000

ExtraLengthValues: TypeAlias = list[
    "capo_customer_profiles.types.string1_to1000.string1To1000"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtraLengthValues) -> list:
    return list(value)


def deserialize_json(data: list) -> ExtraLengthValues:
    return list(data)
