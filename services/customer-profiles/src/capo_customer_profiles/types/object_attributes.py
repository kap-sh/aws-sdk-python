"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ObjectAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.object_attribute

ObjectAttributes: TypeAlias = list[
    "capo_customer_profiles.types.object_attribute.ObjectAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectAttributes) -> list:
    import capo_customer_profiles.types.object_attribute

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.object_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> ObjectAttributes:
    import capo_customer_profiles.types.object_attribute

    out: ObjectAttributes = []
    for item in data:
        out.append(capo_customer_profiles.types.object_attribute.deserialize_json(item))
    return out
