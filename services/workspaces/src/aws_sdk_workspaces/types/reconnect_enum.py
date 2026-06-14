"""Generated from Smithy shape ``com.amazonaws.workspaces#ReconnectEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

ReconnectEnum: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ReconnectEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReconnectEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReconnectEnum value: {data!r}")
    return cast(ReconnectEnum, data)
