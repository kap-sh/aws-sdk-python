"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileObjectTypeTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.list_profile_object_type_template_item

ProfileObjectTypeTemplateList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.list_profile_object_type_template_item.ListProfileObjectTypeTemplateItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileObjectTypeTemplateList) -> list:
    import aws_sdk_customer_profiles.types.list_profile_object_type_template_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.list_profile_object_type_template_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProfileObjectTypeTemplateList:
    import aws_sdk_customer_profiles.types.list_profile_object_type_template_item

    out: ProfileObjectTypeTemplateList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.list_profile_object_type_template_item.deserialize_json(
                item
            )
        )
    return out
