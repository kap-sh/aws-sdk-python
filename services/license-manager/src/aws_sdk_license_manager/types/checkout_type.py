"""Generated from Smithy shape ``com.amazonaws.licensemanager#CheckoutType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

CheckoutType: TypeAlias = Literal[
    "PROVISIONAL",
    "PERPETUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONAL",
        "PERPETUAL",
    )
)


def serialize_aws_json_1_1(value: CheckoutType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CheckoutType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CheckoutType value: {data!r}")
    return cast(CheckoutType, data)
