"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteUniqueIdErrorType``."""

from typing import Literal, TypeAlias, cast

DeleteUniqueIdErrorType: TypeAlias = Literal[
    "SERVICE_ERROR",
    "VALIDATION_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUniqueIdErrorType) -> str:
    return value


def deserialize_json(data: str) -> DeleteUniqueIdErrorType:
    return cast(DeleteUniqueIdErrorType, data)
