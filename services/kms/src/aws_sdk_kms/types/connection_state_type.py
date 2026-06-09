"""Generated from Smithy shape ``com.amazonaws.kms#ConnectionStateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

ConnectionStateType: TypeAlias = Literal[
    "CONNECTED",
    "CONNECTING",
    "FAILED",
    "DISCONNECTED",
    "DISCONNECTING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTED",
        "CONNECTING",
        "FAILED",
        "DISCONNECTED",
        "DISCONNECTING",
    )
)


def serialize_aws_json_1_1(value: ConnectionStateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionStateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionStateType value: {data!r}")
    return cast(ConnectionStateType, data)
