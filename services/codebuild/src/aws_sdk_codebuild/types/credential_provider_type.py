"""Generated from Smithy shape ``com.amazonaws.codebuild#CredentialProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

CredentialProviderType: TypeAlias = Literal["SECRETS_MANAGER",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SECRETS_MANAGER",))


def serialize_aws_json_1_1(value: CredentialProviderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CredentialProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CredentialProviderType value: {data!r}")
    return cast(CredentialProviderType, data)
