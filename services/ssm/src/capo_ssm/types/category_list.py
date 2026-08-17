"""Generated from Smithy shape ``com.amazonaws.ssm#CategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.category

CategoryList: TypeAlias = list["capo_ssm.types.category.Category"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoryList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CategoryList:
    return [item for item in data if item is not None]
