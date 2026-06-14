"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#AuthorizationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>The authorization type. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer. For HTTP APIs, valid values are NONE for open access, JWT for using JSON Web Tokens, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer.</p>"""
AuthorizationType: TypeAlias = Literal[
    "NONE",
    "AWS_IAM",
    "CUSTOM",
    "JWT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "AWS_IAM",
        "CUSTOM",
        "JWT",
    )
)


def serialize_json(value: AuthorizationType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizationType value: {data!r}")
    return cast(AuthorizationType, data)
