"""Generated from Smithy shape ``com.amazonaws.quicksight#NamespaceStatus``."""

from typing import Literal, TypeAlias, cast

NamespaceStatus: TypeAlias = Literal[
    "CREATED",
    "CREATING",
    "DELETING",
    "RETRYABLE_FAILURE",
    "NON_RETRYABLE_FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NamespaceStatus) -> str:
    return value


def deserialize_json(data: str) -> NamespaceStatus:
    return cast(NamespaceStatus, data)
