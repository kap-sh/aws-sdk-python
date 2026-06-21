"""Generated from Smithy shape ``com.amazonaws.mediatailor#AccessType``."""

from typing import Literal, TypeAlias, cast

AccessType: TypeAlias = Literal[
    "S3_SIGV4",
    "SECRETS_MANAGER_ACCESS_TOKEN",
    "AUTODETECT_SIGV4",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessType) -> str:
    return value


def deserialize_json(data: str) -> AccessType:
    return cast(AccessType, data)
