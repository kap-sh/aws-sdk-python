"""Generated from Smithy shape ``com.amazonaws.snowball#ShipmentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

ShipmentState: TypeAlias = Literal[
    "RECEIVED",
    "RETURNED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RECEIVED",
        "RETURNED",
    )
)


def serialize_aws_json_1_1(value: ShipmentState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShipmentState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShipmentState value: {data!r}")
    return cast(ShipmentState, data)
