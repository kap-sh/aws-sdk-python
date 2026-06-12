"""Generated from Smithy shape ``com.amazonaws.apigateway#GatewayResponseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: GatewayResponseType) -> str:
    return value


def deserialize_json(data: str) -> GatewayResponseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayResponseType value: {data!r}")
    return cast(GatewayResponseType, data)
