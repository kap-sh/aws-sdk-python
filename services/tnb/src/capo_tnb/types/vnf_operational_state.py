"""Generated from Smithy shape ``com.amazonaws.tnb#VnfOperationalState``."""

from typing import Literal, TypeAlias, cast

VnfOperationalState: TypeAlias = Literal[
    "STARTED",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VnfOperationalState) -> str:
    return value


def deserialize_json(data: str) -> VnfOperationalState:
    return cast(VnfOperationalState, data)
