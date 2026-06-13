"""Generated from Smithy shape ``com.amazonaws.securityagent#AuthenticationProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Type of authentication provider.</p>"""
AuthenticationProviderType: TypeAlias = Literal[
    "SECRETS_MANAGER",
    "AWS_LAMBDA",
    "AWS_IAM_ROLE",
    "AWS_INTERNAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SECRETS_MANAGER",
        "AWS_LAMBDA",
        "AWS_IAM_ROLE",
        "AWS_INTERNAL",
    )
)


def serialize_json(value: AuthenticationProviderType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationProviderType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AuthenticationProviderType value: {data!r}"
        )
    return cast(AuthenticationProviderType, data)
