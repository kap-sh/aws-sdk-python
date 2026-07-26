"""Generated from Smithy shape ``com.amazonaws.greengrassv2#InstalledComponentLifecycleState``."""

from typing import Literal, TypeAlias, cast

InstalledComponentLifecycleState: TypeAlias = Literal[
    "NEW",
    "INSTALLED",
    "STARTING",
    "RUNNING",
    "STOPPING",
    "ERRORED",
    "BROKEN",
    "FINISHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InstalledComponentLifecycleState) -> str:
    return value


def deserialize_json(data: str) -> InstalledComponentLifecycleState:
    return cast(InstalledComponentLifecycleState, data)
