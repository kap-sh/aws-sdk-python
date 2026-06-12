"""Generated from Smithy shape ``com.amazonaws.workmail#IdentityProviderAuthenticationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

IdentityProviderAuthenticationMode: TypeAlias = Literal[
    "IDENTITY_PROVIDER_ONLY",
    "IDENTITY_PROVIDER_AND_DIRECTORY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDENTITY_PROVIDER_ONLY",
        "IDENTITY_PROVIDER_AND_DIRECTORY",
    )
)


def serialize_aws_json_1_1(value: IdentityProviderAuthenticationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdentityProviderAuthenticationMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IdentityProviderAuthenticationMode value: {data!r}"
        )
    return cast(IdentityProviderAuthenticationMode, data)
