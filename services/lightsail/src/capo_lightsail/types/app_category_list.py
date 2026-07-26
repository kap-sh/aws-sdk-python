"""Generated from Smithy shape ``com.amazonaws.lightsail#AppCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.app_category

AppCategoryList: TypeAlias = list["capo_lightsail.types.app_category.AppCategory"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppCategoryList) -> list:
    import capo_lightsail.types.app_category

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.app_category.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AppCategoryList:
    import capo_lightsail.types.app_category

    out: AppCategoryList = []
    for item in data:
        out.append(capo_lightsail.types.app_category.deserialize_aws_json_1_1(item))
    return out
