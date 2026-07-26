"""Generated from Smithy shape ``com.amazonaws.finspace#ChangesetStatus``."""

from typing import Literal, TypeAlias, cast

ChangesetStatus: TypeAlias = Literal[
    "PENDING",
    "PROCESSING",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangesetStatus) -> str:
    return value


def deserialize_json(data: str) -> ChangesetStatus:
    return cast(ChangesetStatus, data)
