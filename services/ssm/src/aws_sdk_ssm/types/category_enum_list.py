"""Generated from Smithy shape ``com.amazonaws.ssm#CategoryEnumList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.category

CategoryEnumList: TypeAlias = list["aws_sdk_ssm.types.category.Category"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoryEnumList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CategoryEnumList:
    return list(data)
