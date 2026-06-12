"""Generated from Smithy shape ``com.amazonaws.ssm#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ConnectionStatus: TypeAlias = Literal[
    "connected",
    "notconnected",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "connected",
        "notconnected",
    )
)


def serialize_aws_json_1_1(value: ConnectionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionStatus value: {data!r}")
    return cast(ConnectionStatus, data)
