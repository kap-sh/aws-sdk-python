"""Generated from Smithy shape ``com.amazonaws.devopsagent#Priority``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Priority levels for tasks, from highest to lowest urgency</p>"""
Priority: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "MINIMAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRITICAL",
        "HIGH",
        "MEDIUM",
        "LOW",
        "MINIMAL",
    )
)


def serialize_json(value: Priority) -> str:
    return value


def deserialize_json(data: str) -> Priority:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Priority value: {data!r}")
    return cast(Priority, data)
