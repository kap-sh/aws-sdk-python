"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiKeySourceType``."""

from typing import Literal, TypeAlias, cast

ApiKeySourceType: TypeAlias = Literal[
    "HEADER",
    "AUTHORIZER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeySourceType) -> str:
    return value


def deserialize_json(data: str) -> ApiKeySourceType:
    return cast(ApiKeySourceType, data)
