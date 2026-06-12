"""Generated from Smithy shape ``com.amazonaws.transfer#SftpAuthenticationMethods``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

SftpAuthenticationMethods: TypeAlias = Literal[
    "PASSWORD",
    "PUBLIC_KEY",
    "PUBLIC_KEY_OR_PASSWORD",
    "PUBLIC_KEY_AND_PASSWORD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSWORD",
        "PUBLIC_KEY",
        "PUBLIC_KEY_OR_PASSWORD",
        "PUBLIC_KEY_AND_PASSWORD",
    )
)


def serialize_aws_json_1_1(value: SftpAuthenticationMethods) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SftpAuthenticationMethods:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SftpAuthenticationMethods value: {data!r}")
    return cast(SftpAuthenticationMethods, data)
