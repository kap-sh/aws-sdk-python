"""Generated from Smithy shape ``com.amazonaws.directoryservice#ClientAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

ClientAuthenticationType: TypeAlias = Literal[
    "SmartCard",
    "SmartCardOrPassword",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SmartCard",
        "SmartCardOrPassword",
    )
)


def serialize_aws_json_1_1(value: ClientAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientAuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClientAuthenticationType value: {data!r}")
    return cast(ClientAuthenticationType, data)
