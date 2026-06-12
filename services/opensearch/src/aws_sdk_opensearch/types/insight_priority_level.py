"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightPriorityLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The priority level of an insight. Possible values are <code>CRITICAL</code>, <code>HIGH</code>, <code>MEDIUM</code>, and <code>LOW</code>.</p>"""
InsightPriorityLevel: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRITICAL",
        "HIGH",
        "MEDIUM",
        "LOW",
    )
)


def serialize_json(value: InsightPriorityLevel) -> str:
    return value


def deserialize_json(data: str) -> InsightPriorityLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightPriorityLevel value: {data!r}")
    return cast(InsightPriorityLevel, data)
