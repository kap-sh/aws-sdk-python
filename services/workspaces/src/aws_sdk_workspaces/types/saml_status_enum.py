"""Generated from Smithy shape ``com.amazonaws.workspaces#SamlStatusEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

SamlStatusEnum: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK",
    )
)


def serialize_aws_json_1_1(value: SamlStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SamlStatusEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SamlStatusEnum value: {data!r}")
    return cast(SamlStatusEnum, data)
