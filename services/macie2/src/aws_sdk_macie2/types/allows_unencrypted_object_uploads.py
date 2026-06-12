"""Generated from Smithy shape ``com.amazonaws.macie2#AllowsUnencryptedObjectUploads``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

AllowsUnencryptedObjectUploads: TypeAlias = Literal[
    "TRUE",
    "FALSE",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE",
        "FALSE",
        "UNKNOWN",
    )
)


def serialize_json(value: AllowsUnencryptedObjectUploads) -> str:
    return value


def deserialize_json(data: str) -> AllowsUnencryptedObjectUploads:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AllowsUnencryptedObjectUploads value: {data!r}"
        )
    return cast(AllowsUnencryptedObjectUploads, data)
