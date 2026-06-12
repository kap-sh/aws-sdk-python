"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#SavingsEstimationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

SavingsEstimationMode: TypeAlias = Literal[
    "AfterDiscounts",
    "BeforeDiscounts",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AfterDiscounts",
        "BeforeDiscounts",
    )
)


def serialize_aws_json_1_0(value: SavingsEstimationMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SavingsEstimationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SavingsEstimationMode value: {data!r}")
    return cast(SavingsEstimationMode, data)
