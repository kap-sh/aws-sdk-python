"""Generated from Smithy shape ``com.amazonaws.macie2#Type``."""

from typing import Literal, TypeAlias, cast

Type: TypeAlias = Literal[
    "NONE",
    "AES256",
    "aws:kms",
    "aws:kms:dsse",
]


# --- restJson1 ser/de ---
def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    return cast(Type, data)
