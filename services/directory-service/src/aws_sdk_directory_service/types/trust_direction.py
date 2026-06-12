"""Generated from Smithy shape ``com.amazonaws.directoryservice#TrustDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

TrustDirection: TypeAlias = Literal[
    "One-Way: Outgoing",
    "One-Way: Incoming",
    "Two-Way",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "One-Way: Outgoing",
        "One-Way: Incoming",
        "Two-Way",
    )
)


def serialize_aws_json_1_1(value: TrustDirection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrustDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrustDirection value: {data!r}")
    return cast(TrustDirection, data)
