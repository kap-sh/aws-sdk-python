"""Generated from Smithy shape ``com.amazonaws.securitylake#AccessType``."""

from typing import Literal, TypeAlias, cast

AccessType: TypeAlias = Literal[
    "LAKEFORMATION",
    "S3",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessType) -> str:
    return value


def deserialize_json(data: str) -> AccessType:
    return cast(AccessType, data)
