"""Generated from Smithy shape ``com.amazonaws.opensearch#PauseState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of the automated snapshot pause. Valid values are <code>Active</code>, <code>Completed</code>, <code>Scheduled</code>, and <code>Disabled</code>.</p>"""
PauseState: TypeAlias = Literal[
    "Active",
    "Completed",
    "Scheduled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: PauseState) -> str:
    return value


def deserialize_json(data: str) -> PauseState:
    return cast(PauseState, data)
