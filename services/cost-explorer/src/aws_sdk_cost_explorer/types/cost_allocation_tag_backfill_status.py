"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagBackfillStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

CostAllocationTagBackfillStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "PROCESSING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "PROCESSING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: CostAllocationTagBackfillStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostAllocationTagBackfillStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CostAllocationTagBackfillStatus value: {data!r}"
        )
    return cast(CostAllocationTagBackfillStatus, data)
