"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PauseState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

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
