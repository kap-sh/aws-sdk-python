"""Generated from Smithy shape ``com.amazonaws.devopsagent#NewRelicRegion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>The NewRelic region (determines API endpoint).</p>"""
NewRelicRegion: TypeAlias = Literal[
    "US",
    "EU",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "US",
        "EU",
    )
)


def serialize_json(value: NewRelicRegion) -> str:
    return value


def deserialize_json(data: str) -> NewRelicRegion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NewRelicRegion value: {data!r}")
    return cast(NewRelicRegion, data)
