"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Objects``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.stringified_json

Objects: TypeAlias = list[
    "capo_customer_profiles.types.stringified_json.stringifiedJson"
]


# --- restJson1 ser/de ---
def serialize_json(value: Objects) -> list:
    return list(value)


def deserialize_json(data: list) -> Objects:
    return list(data)
