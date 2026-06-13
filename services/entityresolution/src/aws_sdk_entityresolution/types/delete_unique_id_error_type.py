"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteUniqueIdErrorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

DeleteUniqueIdErrorType: TypeAlias = Literal[
    "SERVICE_ERROR",
    "VALIDATION_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE_ERROR",
        "VALIDATION_ERROR",
    )
)


def serialize_json(value: DeleteUniqueIdErrorType) -> str:
    return value


def deserialize_json(data: str) -> DeleteUniqueIdErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeleteUniqueIdErrorType value: {data!r}")
    return cast(DeleteUniqueIdErrorType, data)
