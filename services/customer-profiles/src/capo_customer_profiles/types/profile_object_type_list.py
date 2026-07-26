"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileObjectTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.list_profile_object_type_item

ProfileObjectTypeList: TypeAlias = list[
    "capo_customer_profiles.types.list_profile_object_type_item.ListProfileObjectTypeItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileObjectTypeList) -> list:
    import capo_customer_profiles.types.list_profile_object_type_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.list_profile_object_type_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProfileObjectTypeList:
    import capo_customer_profiles.types.list_profile_object_type_item

    out: ProfileObjectTypeList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.list_profile_object_type_item.deserialize_json(
                item
            )
        )
    return out
