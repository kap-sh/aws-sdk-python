"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTagType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

CostAllocationTagType: TypeAlias = Literal[
    "AWSGenerated",
    "UserDefined",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWSGenerated",
        "UserDefined",
    )
)


def serialize_aws_json_1_1(value: CostAllocationTagType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostAllocationTagType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CostAllocationTagType value: {data!r}")
    return cast(CostAllocationTagType, data)
