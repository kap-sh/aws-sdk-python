"""Generated from Smithy shape ``com.amazonaws.athena#CapacityReservationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

CapacityReservationStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "CANCELLING",
    "CANCELLED",
    "FAILED",
    "UPDATE_PENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
        "CANCELLING",
        "CANCELLED",
        "FAILED",
        "UPDATE_PENDING",
    )
)


def serialize_aws_json_1_1(value: CapacityReservationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityReservationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityReservationStatus value: {data!r}")
    return cast(CapacityReservationStatus, data)
