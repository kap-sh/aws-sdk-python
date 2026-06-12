"""Generated from Smithy shape ``com.amazonaws.devicefarm#BillingMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

BillingMethod: TypeAlias = Literal[
    "METERED",
    "UNMETERED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "METERED",
        "UNMETERED",
    )
)


def serialize_aws_json_1_1(value: BillingMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BillingMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingMethod value: {data!r}")
    return cast(BillingMethod, data)
