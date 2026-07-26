"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ExclusionStatus``."""

from typing import Literal, TypeAlias, cast

ExclusionStatus: TypeAlias = Literal[
    "excluded",
    "included",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExclusionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExclusionStatus:
    return cast(ExclusionStatus, data)
