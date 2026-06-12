"""Generated from Smithy shape ``com.amazonaws.directoryservice#ClientAuthenticationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

ClientAuthenticationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: ClientAuthenticationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientAuthenticationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ClientAuthenticationStatus value: {data!r}"
        )
    return cast(ClientAuthenticationStatus, data)
