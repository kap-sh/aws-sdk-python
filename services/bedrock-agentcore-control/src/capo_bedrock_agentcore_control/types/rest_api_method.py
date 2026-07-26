"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RestApiMethod``."""

from typing import Literal, TypeAlias, cast

RestApiMethod: TypeAlias = Literal[
    "GET",
    "DELETE",
    "HEAD",
    "OPTIONS",
    "PATCH",
    "PUT",
    "POST",
]


# --- restJson1 ser/de ---
def serialize_json(value: RestApiMethod) -> str:
    return value


def deserialize_json(data: str) -> RestApiMethod:
    return cast(RestApiMethod, data)
