"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

CostAllocationTagStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
    )
)


def serialize_aws_json_1_1(value: CostAllocationTagStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostAllocationTagStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CostAllocationTagStatus value: {data!r}")
    return cast(CostAllocationTagStatus, data)
