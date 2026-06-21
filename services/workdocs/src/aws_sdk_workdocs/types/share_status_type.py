"""Generated from Smithy shape ``com.amazonaws.workdocs#ShareStatusType``."""

from typing import Literal, TypeAlias, cast

ShareStatusType: TypeAlias = Literal[
    "SUCCESS",
    "FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareStatusType) -> str:
    return value


def deserialize_json(data: str) -> ShareStatusType:
    return cast(ShareStatusType, data)
