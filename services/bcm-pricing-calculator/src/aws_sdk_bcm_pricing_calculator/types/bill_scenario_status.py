"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillScenarioStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

BillScenarioStatus: TypeAlias = Literal[
    "READY",
    "LOCKED",
    "FAILED",
    "STALE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "LOCKED",
        "FAILED",
        "STALE",
    )
)


def serialize_aws_json_1_0(value: BillScenarioStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillScenarioStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillScenarioStatus value: {data!r}")
    return cast(BillScenarioStatus, data)
