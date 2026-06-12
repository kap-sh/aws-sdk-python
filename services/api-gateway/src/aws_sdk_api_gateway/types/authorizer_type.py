"""Generated from Smithy shape ``com.amazonaws.apigateway#AuthorizerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

"""<p>The authorizer type. Valid values are <code>TOKEN</code> for a Lambda function using a single authorization token submitted in a custom header, <code>REQUEST</code> for a Lambda function using incoming request parameters, and <code>COGNITO_USER_POOLS</code> for using an Amazon Cognito user pool.</p>"""
AuthorizerType: TypeAlias = Literal[
    "TOKEN",
    "REQUEST",
    "COGNITO_USER_POOLS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOKEN",
        "REQUEST",
        "COGNITO_USER_POOLS",
    )
)


def serialize_json(value: AuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizerType value: {data!r}")
    return cast(AuthorizerType, data)
