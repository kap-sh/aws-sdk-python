"""Generated from Smithy shape ``com.amazonaws.ssm#SessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

SessionStatus: TypeAlias = Literal[
    "Connected",
    "Connecting",
    "Disconnected",
    "Terminated",
    "Terminating",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Connected",
        "Connecting",
        "Disconnected",
        "Terminated",
        "Terminating",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: SessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionStatus value: {data!r}")
    return cast(SessionStatus, data)
