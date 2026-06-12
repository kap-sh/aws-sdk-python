"""Generated from Smithy shape ``com.amazonaws.appstream#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

AuthenticationType: TypeAlias = Literal[
    "API",
    "SAML",
    "USERPOOL",
    "AWS_AD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "API",
        "SAML",
        "USERPOOL",
        "AWS_AD",
    )
)


def serialize_aws_json_1_1(value: AuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationType value: {data!r}")
    return cast(AuthenticationType, data)
