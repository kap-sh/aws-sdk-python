"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#AccessDeniedReason``."""

from typing import Literal, TypeAlias, cast

AccessDeniedReason: TypeAlias = Literal[
    "IAM_AUTH",
    "DIRECTORY_AUTH",
    "DATA_DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedReason) -> str:
    return value


def deserialize_json(data: str) -> AccessDeniedReason:
    return cast(AccessDeniedReason, data)
