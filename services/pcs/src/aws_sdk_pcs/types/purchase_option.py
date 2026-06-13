"""Generated from Smithy shape ``com.amazonaws.pcs#PurchaseOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pcs.errors import DeserializationError

PurchaseOption: TypeAlias = Literal[
    "ONDEMAND",
    "SPOT",
    "CAPACITY_BLOCK",
    "INTERRUPTIBLE_CAPACITY_RESERVATION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONDEMAND",
        "SPOT",
        "CAPACITY_BLOCK",
        "INTERRUPTIBLE_CAPACITY_RESERVATION",
    )
)


def serialize_aws_json_1_0(value: PurchaseOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PurchaseOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PurchaseOption value: {data!r}")
    return cast(PurchaseOption, data)
