"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#TokenStatus``."""

from typing import Literal, TypeAlias, cast

TokenStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: TokenStatus) -> str:
    return value


def deserialize_json(data: str) -> TokenStatus:
    return cast(TokenStatus, data)
