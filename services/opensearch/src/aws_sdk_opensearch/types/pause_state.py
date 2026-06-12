"""Generated from Smithy shape ``com.amazonaws.opensearch#PauseState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The state of the automated snapshot pause. Valid values are <code>Active</code>, <code>Completed</code>, <code>Scheduled</code>, and <code>Disabled</code>.</p>"""
PauseState: TypeAlias = Literal[
    "Active",
    "Completed",
    "Scheduled",
    "Disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Completed",
        "Scheduled",
        "Disabled",
    )
)


def serialize_json(value: PauseState) -> str:
    return value


def deserialize_json(data: str) -> PauseState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PauseState value: {data!r}")
    return cast(PauseState, data)
