"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

CostCategorySplitChargeMethod: TypeAlias = Literal[
    "FIXED",
    "PROPORTIONAL",
    "EVEN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIXED",
        "PROPORTIONAL",
        "EVEN",
    )
)


def serialize_aws_json_1_1(value: CostCategorySplitChargeMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategorySplitChargeMethod:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CostCategorySplitChargeMethod value: {data!r}"
        )
    return cast(CostCategorySplitChargeMethod, data)
