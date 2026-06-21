"""Generated from Smithy shape ``com.amazonaws.arczonalshift#AppliedStatus``."""

from typing import Literal, TypeAlias, cast

AppliedStatus: TypeAlias = Literal[
    "APPLIED",
    "NOT_APPLIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppliedStatus) -> str:
    return value


def deserialize_json(data: str) -> AppliedStatus:
    return cast(AppliedStatus, data)
