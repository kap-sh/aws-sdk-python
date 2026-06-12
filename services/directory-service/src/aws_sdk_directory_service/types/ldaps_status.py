"""Generated from Smithy shape ``com.amazonaws.directoryservice#LDAPSStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

LDAPSStatus: TypeAlias = Literal[
    "Enabling",
    "Enabled",
    "EnableFailed",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabling",
        "Enabled",
        "EnableFailed",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: LDAPSStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LDAPSStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LDAPSStatus value: {data!r}")
    return cast(LDAPSStatus, data)
