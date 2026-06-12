"""Generated from Smithy shape ``com.amazonaws.lightsail#AppCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.app_category

AppCategoryList: TypeAlias = list["aws_sdk_lightsail.types.app_category.AppCategory"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppCategoryList) -> list:
    import aws_sdk_lightsail.types.app_category

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.app_category.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AppCategoryList:
    import aws_sdk_lightsail.types.app_category

    out: AppCategoryList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.app_category.deserialize_aws_json_1_1(item))
    return out
