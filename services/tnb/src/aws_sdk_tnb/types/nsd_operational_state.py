"""Generated from Smithy shape ``com.amazonaws.tnb#NsdOperationalState``."""

from typing import Literal, TypeAlias, cast

NsdOperationalState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NsdOperationalState) -> str:
    return value


def deserialize_json(data: str) -> NsdOperationalState:
    return cast(NsdOperationalState, data)
