"""Generated from Smithy shape ``com.amazonaws.apigateway#DocumentationPartType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

DocumentationPartType: TypeAlias = Literal[
    "API",
    "AUTHORIZER",
    "MODEL",
    "RESOURCE",
    "METHOD",
    "PATH_PARAMETER",
    "QUERY_PARAMETER",
    "REQUEST_HEADER",
    "REQUEST_BODY",
    "RESPONSE",
    "RESPONSE_HEADER",
    "RESPONSE_BODY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "API",
        "AUTHORIZER",
        "MODEL",
        "RESOURCE",
        "METHOD",
        "PATH_PARAMETER",
        "QUERY_PARAMETER",
        "REQUEST_HEADER",
        "REQUEST_BODY",
        "RESPONSE",
        "RESPONSE_HEADER",
        "RESPONSE_BODY",
    )
)


def serialize_json(value: DocumentationPartType) -> str:
    return value


def deserialize_json(data: str) -> DocumentationPartType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentationPartType value: {data!r}")
    return cast(DocumentationPartType, data)
