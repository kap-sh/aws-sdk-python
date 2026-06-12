"""Generated from Smithy shape ``com.amazonaws.snowball#ShippingLabelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

ShippingLabelStatus: TypeAlias = Literal[
    "InProgress",
    "TimedOut",
    "Succeeded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "TimedOut",
        "Succeeded",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: ShippingLabelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShippingLabelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShippingLabelStatus value: {data!r}")
    return cast(ShippingLabelStatus, data)
