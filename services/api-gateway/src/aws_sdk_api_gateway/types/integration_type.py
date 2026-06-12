"""Generated from Smithy shape ``com.amazonaws.apigateway#IntegrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

"""<p>The integration type. The valid value is <code>HTTP</code> for integrating an API method with an HTTP backend; <code>AWS</code> with any Amazon Web Services service endpoints; <code>MOCK</code> for testing without actually invoking the backend; <code>HTTP_PROXY</code> for integrating with the HTTP proxy integration; <code>AWS_PROXY</code> for integrating with the Lambda proxy integration. </p>"""
IntegrationType: TypeAlias = Literal[
    "HTTP",
    "AWS",
    "MOCK",
    "HTTP_PROXY",
    "AWS_PROXY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP",
        "AWS",
        "MOCK",
        "HTTP_PROXY",
        "AWS_PROXY",
    )
)


def serialize_json(value: IntegrationType) -> str:
    return value


def deserialize_json(data: str) -> IntegrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationType value: {data!r}")
    return cast(IntegrationType, data)
