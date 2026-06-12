"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#AuthorizationScopes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and64

AuthorizationScopes: TypeAlias = list[
    "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationScopes) -> list:
    return list(value)


def deserialize_json(data: list) -> AuthorizationScopes:
    return list(data)
