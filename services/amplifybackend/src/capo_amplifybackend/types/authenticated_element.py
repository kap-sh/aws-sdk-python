"""Generated from Smithy shape ``com.amazonaws.amplifybackend#AuthenticatedElement``."""

from typing import Literal, TypeAlias, cast

AuthenticatedElement: TypeAlias = Literal[
    "READ",
    "CREATE_AND_UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticatedElement) -> str:
    return value


def deserialize_json(data: str) -> AuthenticatedElement:
    return cast(AuthenticatedElement, data)
