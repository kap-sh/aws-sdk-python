"""Generated from Smithy shape ``com.amazonaws.snowball#RemoteManagement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

RemoteManagement: TypeAlias = Literal[
    "INSTALLED_ONLY",
    "INSTALLED_AUTOSTART",
    "NOT_INSTALLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTALLED_ONLY",
        "INSTALLED_AUTOSTART",
        "NOT_INSTALLED",
    )
)


def serialize_aws_json_1_1(value: RemoteManagement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RemoteManagement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RemoteManagement value: {data!r}")
    return cast(RemoteManagement, data)
