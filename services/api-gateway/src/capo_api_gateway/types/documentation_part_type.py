"""Generated from Smithy shape ``com.amazonaws.apigateway#DocumentationPartType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: DocumentationPartType) -> str:
    return value


def deserialize_json(data: str) -> DocumentationPartType:
    return cast(DocumentationPartType, data)
