"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UnAuthenticatedElement``."""

from typing import Literal, TypeAlias, cast

UnAuthenticatedElement: TypeAlias = Literal[
    "READ",
    "CREATE_AND_UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UnAuthenticatedElement) -> str:
    return value


def deserialize_json(data: str) -> UnAuthenticatedElement:
    return cast(UnAuthenticatedElement, data)
