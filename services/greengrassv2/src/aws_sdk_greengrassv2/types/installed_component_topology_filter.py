"""Generated from Smithy shape ``com.amazonaws.greengrassv2#InstalledComponentTopologyFilter``."""

from typing import Literal, TypeAlias, cast

InstalledComponentTopologyFilter: TypeAlias = Literal[
    "ALL",
    "ROOT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InstalledComponentTopologyFilter) -> str:
    return value


def deserialize_json(data: str) -> InstalledComponentTopologyFilter:
    return cast(InstalledComponentTopologyFilter, data)
