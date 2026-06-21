"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#AuthorizerType``."""

from typing import Literal, TypeAlias, cast

"""<p>The authorizer type. Specify REQUEST for a Lambda function using incoming request parameters. Specify JWT to use JSON Web Tokens (supported only for HTTP APIs).</p>"""
AuthorizerType: TypeAlias = Literal[
    "REQUEST",
    "JWT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizerType:
    return cast(AuthorizerType, data)
