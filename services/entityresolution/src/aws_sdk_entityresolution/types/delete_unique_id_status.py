"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteUniqueIdStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

DeleteUniqueIdStatus: TypeAlias = Literal[
    "COMPLETED",
    "ACCEPTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "ACCEPTED",
    )
)


def serialize_json(value: DeleteUniqueIdStatus) -> str:
    return value


def deserialize_json(data: str) -> DeleteUniqueIdStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeleteUniqueIdStatus value: {data!r}")
    return cast(DeleteUniqueIdStatus, data)
