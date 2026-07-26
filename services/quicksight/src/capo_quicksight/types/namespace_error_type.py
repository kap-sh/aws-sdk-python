"""Generated from Smithy shape ``com.amazonaws.quicksight#NamespaceErrorType``."""

from typing import Literal, TypeAlias, cast

NamespaceErrorType: TypeAlias = Literal[
    "PERMISSION_DENIED",
    "INTERNAL_SERVICE_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceErrorType) -> str:
    return value


def deserialize_json(data: str) -> NamespaceErrorType:
    return cast(NamespaceErrorType, data)
