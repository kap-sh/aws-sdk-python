"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ObjectTypeKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.object_type_key

ObjectTypeKeyList: TypeAlias = list[
    "capo_customer_profiles.types.object_type_key.ObjectTypeKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectTypeKeyList) -> list:
    import capo_customer_profiles.types.object_type_key

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.object_type_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> ObjectTypeKeyList:
    import capo_customer_profiles.types.object_type_key

    out: ObjectTypeKeyList = []
    for item in data:
        out.append(capo_customer_profiles.types.object_type_key.deserialize_json(item))
    return out
