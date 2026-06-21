"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryStatus``."""

from typing import Literal, TypeAlias, cast

CostCategoryStatus: TypeAlias = Literal[
    "PROCESSING",
    "APPLIED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategoryStatus:
    return cast(CostCategoryStatus, data)
