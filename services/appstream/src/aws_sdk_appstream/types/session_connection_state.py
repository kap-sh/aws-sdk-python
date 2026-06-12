"""Generated from Smithy shape ``com.amazonaws.appstream#SessionConnectionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

SessionConnectionState: TypeAlias = Literal[
    "CONNECTED",
    "NOT_CONNECTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTED",
        "NOT_CONNECTED",
    )
)


def serialize_aws_json_1_1(value: SessionConnectionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionConnectionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionConnectionState value: {data!r}")
    return cast(SessionConnectionState, data)
