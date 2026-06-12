"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

SavingsPlansDataType: TypeAlias = Literal[
    "ATTRIBUTES",
    "UTILIZATION",
    "AMORTIZED_COMMITMENT",
    "SAVINGS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATTRIBUTES",
        "UTILIZATION",
        "AMORTIZED_COMMITMENT",
        "SAVINGS",
    )
)


def serialize_aws_json_1_1(value: SavingsPlansDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SavingsPlansDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SavingsPlansDataType value: {data!r}")
    return cast(SavingsPlansDataType, data)
