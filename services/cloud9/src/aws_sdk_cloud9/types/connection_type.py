"""Generated from Smithy shape ``com.amazonaws.cloud9#ConnectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloud9.errors import DeserializationError

ConnectionType: TypeAlias = Literal[
    "CONNECT_SSH",
    "CONNECT_SSM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECT_SSH",
        "CONNECT_SSM",
    )
)


def serialize_aws_json_1_1(value: ConnectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionType value: {data!r}")
    return cast(ConnectionType, data)
