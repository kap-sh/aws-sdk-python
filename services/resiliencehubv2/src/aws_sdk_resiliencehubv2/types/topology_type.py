"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TopologyType``."""

from typing import Literal, TypeAlias, cast

TopologyType: TypeAlias = Literal[
    "CONTAINMENT",
    "DATA_FLOW",
    "OBSERVABILITY",
    "PERMISSIONS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopologyType) -> str:
    return value


def deserialize_json(data: str) -> TopologyType:
    return cast(TopologyType, data)
