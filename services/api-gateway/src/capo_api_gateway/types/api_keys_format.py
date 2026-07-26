"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiKeysFormat``."""

from typing import Literal, TypeAlias, cast

ApiKeysFormat: TypeAlias = Literal["csv",]


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeysFormat) -> str:
    return value


def deserialize_json(data: str) -> ApiKeysFormat:
    return cast(ApiKeysFormat, data)
