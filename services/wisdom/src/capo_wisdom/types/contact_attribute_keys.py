"""Generated from Smithy shape ``com.amazonaws.wisdom#ContactAttributeKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.contact_attribute_key

ContactAttributeKeys: TypeAlias = list[
    "capo_wisdom.types.contact_attribute_key.ContactAttributeKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactAttributeKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> ContactAttributeKeys:
    return list(data)
