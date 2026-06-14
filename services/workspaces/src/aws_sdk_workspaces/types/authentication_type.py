"""Generated from Smithy shape ``com.amazonaws.workspaces#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

AuthenticationType: TypeAlias = Literal["SAML",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SAML",))


def serialize_aws_json_1_1(value: AuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationType value: {data!r}")
    return cast(AuthenticationType, data)
