"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsecuretunneling.errors import DeserializationError

ConnectionStatus: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTED",
        "DISCONNECTED",
    )
)


def serialize_aws_json_1_1(value: ConnectionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionStatus value: {data!r}")
    return cast(ConnectionStatus, data)
