"""Generated from Smithy shape ``com.amazonaws.workspaces#LogUploadEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

LogUploadEnum: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: LogUploadEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogUploadEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogUploadEnum value: {data!r}")
    return cast(LogUploadEnum, data)
