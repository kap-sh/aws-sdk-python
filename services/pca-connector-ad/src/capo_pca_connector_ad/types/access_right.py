"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#AccessRight``."""

from typing import Literal, TypeAlias, cast

AccessRight: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessRight) -> str:
    return value


def deserialize_json(data: str) -> AccessRight:
    return cast(AccessRight, data)
