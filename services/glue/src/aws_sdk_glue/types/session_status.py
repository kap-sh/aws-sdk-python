"""Generated from Smithy shape ``com.amazonaws.glue#SessionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

SessionStatus: TypeAlias = Literal[
    "PROVISIONING",
    "READY",
    "FAILED",
    "TIMEOUT",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONING",
        "READY",
        "FAILED",
        "TIMEOUT",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: SessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionStatus value: {data!r}")
    return cast(SessionStatus, data)
