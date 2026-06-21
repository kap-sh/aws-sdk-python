"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#KeySpec``."""

from typing import Literal, TypeAlias, cast

KeySpec: TypeAlias = Literal[
    "KEY_EXCHANGE",
    "SIGNATURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: KeySpec) -> str:
    return value


def deserialize_json(data: str) -> KeySpec:
    return cast(KeySpec, data)
