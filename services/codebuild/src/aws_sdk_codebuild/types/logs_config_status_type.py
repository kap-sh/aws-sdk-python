"""Generated from Smithy shape ``com.amazonaws.codebuild#LogsConfigStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

LogsConfigStatusType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: LogsConfigStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogsConfigStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogsConfigStatusType value: {data!r}")
    return cast(LogsConfigStatusType, data)
