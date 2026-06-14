"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#AuthorizerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>The authorizer type. Specify REQUEST for a Lambda function using incoming request parameters. Specify JWT to use JSON Web Tokens (supported only for HTTP APIs).</p>"""
AuthorizerType: TypeAlias = Literal[
    "REQUEST",
    "JWT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUEST",
        "JWT",
    )
)


def serialize_json(value: AuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizerType value: {data!r}")
    return cast(AuthorizerType, data)
