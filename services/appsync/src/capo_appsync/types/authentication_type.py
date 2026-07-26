"""Generated from Smithy shape ``com.amazonaws.appsync#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

AuthenticationType: TypeAlias = Literal[
    "API_KEY",
    "AWS_IAM",
    "AMAZON_COGNITO_USER_POOLS",
    "OPENID_CONNECT",
    "AWS_LAMBDA",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    return cast(AuthenticationType, data)
