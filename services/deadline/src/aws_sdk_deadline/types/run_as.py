"""Generated from Smithy shape ``com.amazonaws.deadline#RunAs``."""

from typing import Literal, TypeAlias, cast

RunAs: TypeAlias = Literal[
    "QUEUE_CONFIGURED_USER",
    "WORKER_AGENT_USER",
]


# --- restJson1 ser/de ---
def serialize_json(value: RunAs) -> str:
    return value


def deserialize_json(data: str) -> RunAs:
    return cast(RunAs, data)
