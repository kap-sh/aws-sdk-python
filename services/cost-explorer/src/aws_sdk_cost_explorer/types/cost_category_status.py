"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

CostCategoryStatus: TypeAlias = Literal[
    "PROCESSING",
    "APPLIED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROCESSING",
        "APPLIED",
    )
)


def serialize_aws_json_1_1(value: CostCategoryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategoryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CostCategoryStatus value: {data!r}")
    return cast(CostCategoryStatus, data)
