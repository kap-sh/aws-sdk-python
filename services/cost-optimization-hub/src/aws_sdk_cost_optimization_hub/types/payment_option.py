"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#PaymentOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

PaymentOption: TypeAlias = Literal[
    "AllUpfront",
    "PartialUpfront",
    "NoUpfront",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AllUpfront",
        "PartialUpfront",
        "NoUpfront",
    )
)


def serialize_aws_json_1_0(value: PaymentOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PaymentOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentOption value: {data!r}")
    return cast(PaymentOption, data)
