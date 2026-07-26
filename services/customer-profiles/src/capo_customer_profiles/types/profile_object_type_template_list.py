"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileObjectTypeTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.list_profile_object_type_template_item

ProfileObjectTypeTemplateList: TypeAlias = list[
    "capo_customer_profiles.types.list_profile_object_type_template_item.ListProfileObjectTypeTemplateItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileObjectTypeTemplateList) -> list:
    import capo_customer_profiles.types.list_profile_object_type_template_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.list_profile_object_type_template_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProfileObjectTypeTemplateList:
    import capo_customer_profiles.types.list_profile_object_type_template_item

    out: ProfileObjectTypeTemplateList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.list_profile_object_type_template_item.deserialize_json(
                item
            )
        )
    return out
