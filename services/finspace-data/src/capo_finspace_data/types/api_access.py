"""Generated from Smithy shape ``com.amazonaws.finspacedata#ApiAccess``."""

from typing import Literal, TypeAlias, cast

ApiAccess: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiAccess) -> str:
    return value


def deserialize_json(data: str) -> ApiAccess:
    return cast(ApiAccess, data)
