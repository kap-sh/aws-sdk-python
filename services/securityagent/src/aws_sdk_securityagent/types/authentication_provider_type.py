"""Generated from Smithy shape ``com.amazonaws.securityagent#AuthenticationProviderType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of authentication provider.</p>"""
AuthenticationProviderType: TypeAlias = Literal[
    "SECRETS_MANAGER",
    "AWS_LAMBDA",
    "AWS_IAM_ROLE",
    "AWS_INTERNAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationProviderType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationProviderType:
    return cast(AuthenticationProviderType, data)
