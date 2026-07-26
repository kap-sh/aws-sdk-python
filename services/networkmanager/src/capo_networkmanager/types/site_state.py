"""Generated from Smithy shape ``com.amazonaws.networkmanager#SiteState``."""

from typing import Literal, TypeAlias, cast

SiteState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SiteState) -> str:
    return value


def deserialize_json(data: str) -> SiteState:
    return cast(SiteState, data)
