"""Generated from Smithy shape ``com.amazonaws.iot#AuthorizerStatus``."""

from typing import Literal, TypeAlias, cast

AuthorizerStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizerStatus) -> str:
    return value


def deserialize_json(data: str) -> AuthorizerStatus:
    return cast(AuthorizerStatus, data)
