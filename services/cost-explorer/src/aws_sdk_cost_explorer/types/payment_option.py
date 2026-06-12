"""Generated from Smithy shape ``com.amazonaws.costexplorer#PaymentOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

PaymentOption: TypeAlias = Literal[
    "NO_UPFRONT",
    "PARTIAL_UPFRONT",
    "ALL_UPFRONT",
    "LIGHT_UTILIZATION",
    "MEDIUM_UTILIZATION",
    "HEAVY_UTILIZATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_UPFRONT",
        "PARTIAL_UPFRONT",
        "ALL_UPFRONT",
        "LIGHT_UTILIZATION",
        "MEDIUM_UTILIZATION",
        "HEAVY_UTILIZATION",
    )
)


def serialize_aws_json_1_1(value: PaymentOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PaymentOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentOption value: {data!r}")
    return cast(PaymentOption, data)
