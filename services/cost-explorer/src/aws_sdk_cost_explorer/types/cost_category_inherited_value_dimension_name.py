"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryInheritedValueDimensionName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

CostCategoryInheritedValueDimensionName: TypeAlias = Literal[
    "LINKED_ACCOUNT_NAME",
    "TAG",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINKED_ACCOUNT_NAME",
        "TAG",
    )
)


def serialize_aws_json_1_1(value: CostCategoryInheritedValueDimensionName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategoryInheritedValueDimensionName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CostCategoryInheritedValueDimensionName value: {data!r}"
        )
    return cast(CostCategoryInheritedValueDimensionName, data)
