"""Generated from Smithy shape ``com.amazonaws.lightsail#ContactMethodStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ContactMethodStatus: TypeAlias = Literal[
    "PendingVerification",
    "Valid",
    "Invalid",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PendingVerification",
        "Valid",
        "Invalid",
    )
)


def serialize_aws_json_1_1(value: ContactMethodStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContactMethodStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactMethodStatus value: {data!r}")
    return cast(ContactMethodStatus, data)
