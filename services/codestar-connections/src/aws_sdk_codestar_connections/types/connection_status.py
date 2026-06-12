"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_connections.errors import DeserializationError

ConnectionStatus: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "ERROR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "AVAILABLE",
        "ERROR",
    )
)


def serialize_aws_json_1_0(value: ConnectionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionStatus value: {data!r}")
    return cast(ConnectionStatus, data)
