"""Generated from Smithy shape ``com.amazonaws.apprunner#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

ConnectionStatus: TypeAlias = Literal[
    "PENDING_HANDSHAKE",
    "AVAILABLE",
    "ERROR",
    "DELETED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_HANDSHAKE",
        "AVAILABLE",
        "ERROR",
        "DELETED",
    )
)


def serialize_aws_json_1_0(value: ConnectionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionStatus value: {data!r}")
    return cast(ConnectionStatus, data)
