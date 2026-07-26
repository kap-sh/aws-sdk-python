"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SortAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.sort_attribute

SortAttributeList: TypeAlias = list[
    "capo_customer_profiles.types.sort_attribute.SortAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: SortAttributeList) -> list:
    import capo_customer_profiles.types.sort_attribute

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.sort_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> SortAttributeList:
    import capo_customer_profiles.types.sort_attribute

    out: SortAttributeList = []
    for item in data:
        out.append(capo_customer_profiles.types.sort_attribute.deserialize_json(item))
    return out
