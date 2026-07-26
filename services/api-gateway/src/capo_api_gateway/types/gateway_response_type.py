"""Generated from Smithy shape ``com.amazonaws.apigateway#GatewayResponseType``."""

from typing import Literal, TypeAlias, cast

GatewayResponseType: TypeAlias = Literal[
    "DEFAULT_4XX",
    "DEFAULT_5XX",
    "RESOURCE_NOT_FOUND",
    "UNAUTHORIZED",
    "INVALID_API_KEY",
    "ACCESS_DENIED",
    "AUTHORIZER_FAILURE",
    "AUTHORIZER_CONFIGURATION_ERROR",
    "INVALID_SIGNATURE",
    "EXPIRED_TOKEN",
    "MISSING_AUTHENTICATION_TOKEN",
    "INTEGRATION_FAILURE",
    "INTEGRATION_TIMEOUT",
    "API_CONFIGURATION_ERROR",
    "UNSUPPORTED_MEDIA_TYPE",
    "BAD_REQUEST_PARAMETERS",
    "BAD_REQUEST_BODY",
    "REQUEST_TOO_LARGE",
    "THROTTLED",
    "QUOTA_EXCEEDED",
    "WAF_FILTERED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayResponseType) -> str:
    return value


def deserialize_json(data: str) -> GatewayResponseType:
    return cast(GatewayResponseType, data)
