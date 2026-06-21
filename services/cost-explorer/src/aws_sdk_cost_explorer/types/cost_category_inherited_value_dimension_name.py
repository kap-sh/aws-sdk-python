"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryInheritedValueDimensionName``."""

from typing import Literal, TypeAlias, cast

CostCategoryInheritedValueDimensionName: TypeAlias = Literal[
    "LINKED_ACCOUNT_NAME",
    "TAG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryInheritedValueDimensionName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategoryInheritedValueDimensionName:
    return cast(CostCategoryInheritedValueDimensionName, data)
