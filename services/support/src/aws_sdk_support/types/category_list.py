"""Generated from Smithy shape ``com.amazonaws.support#CategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.category

CategoryList: TypeAlias = list["aws_sdk_support.types.category.Category"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoryList) -> list:
    import aws_sdk_support.types.category

    out: list = []
    for item in value:
        out.append(aws_sdk_support.types.category.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CategoryList:
    import aws_sdk_support.types.category

    out: CategoryList = []
    for item in data:
        out.append(aws_sdk_support.types.category.deserialize_aws_json_1_1(item))
    return out
