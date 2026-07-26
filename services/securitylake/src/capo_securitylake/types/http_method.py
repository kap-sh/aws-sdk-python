"""Generated from Smithy shape ``com.amazonaws.securitylake#HttpMethod``."""

from typing import Literal, TypeAlias, cast

HttpMethod: TypeAlias = Literal[
    "POST",
    "PUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: HttpMethod) -> str:
    return value


def deserialize_json(data: str) -> HttpMethod:
    return cast(HttpMethod, data)
