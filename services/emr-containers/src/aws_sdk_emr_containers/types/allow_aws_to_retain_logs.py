"""Generated from Smithy shape ``com.amazonaws.emrcontainers#AllowAWSToRetainLogs``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr_containers.errors import DeserializationError

AllowAWSToRetainLogs: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AllowAWSToRetainLogs) -> str:
    return value


def deserialize_json(data: str) -> AllowAWSToRetainLogs:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllowAWSToRetainLogs value: {data!r}")
    return cast(AllowAWSToRetainLogs, data)
