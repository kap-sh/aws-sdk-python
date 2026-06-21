"""Generated from Smithy shape ``com.amazonaws.macie2#AllowsUnencryptedObjectUploads``."""

from typing import Literal, TypeAlias, cast

AllowsUnencryptedObjectUploads: TypeAlias = Literal[
    "TRUE",
    "FALSE",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowsUnencryptedObjectUploads) -> str:
    return value


def deserialize_json(data: str) -> AllowsUnencryptedObjectUploads:
    return cast(AllowsUnencryptedObjectUploads, data)
