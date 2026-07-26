"""Generated from Smithy shape ``com.amazonaws.apigateway#AuthorizerType``."""

from typing import Literal, TypeAlias, cast

"""<p>The authorizer type. Valid values are <code>TOKEN</code> for a Lambda function using a single authorization token submitted in a custom header, <code>REQUEST</code> for a Lambda function using incoming request parameters, and <code>COGNITO_USER_POOLS</code> for using an Amazon Cognito user pool.</p>"""
AuthorizerType: TypeAlias = Literal[
    "TOKEN",
    "REQUEST",
    "COGNITO_USER_POOLS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizerType:
    return cast(AuthorizerType, data)
