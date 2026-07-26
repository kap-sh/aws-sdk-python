"""Generated from Smithy shape ``com.amazonaws.bedrockagent#WebScopeType``."""

from typing import Literal, TypeAlias, cast

WebScopeType: TypeAlias = Literal[
    "HOST_ONLY",
    "SUBDOMAINS",
]


# --- restJson1 ser/de ---
def serialize_json(value: WebScopeType) -> str:
    return value


def deserialize_json(data: str) -> WebScopeType:
    return cast(WebScopeType, data)
