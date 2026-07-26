"""Generated from Smithy shape ``com.amazonaws.emrcontainers#VirtualClusterState``."""

from typing import Literal, TypeAlias, cast

VirtualClusterState: TypeAlias = Literal[
    "RUNNING",
    "TERMINATING",
    "TERMINATED",
    "ARRESTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualClusterState) -> str:
    return value


def deserialize_json(data: str) -> VirtualClusterState:
    return cast(VirtualClusterState, data)
