"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightPriorityLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>The priority level of an insight. Possible values are <code>CRITICAL</code>, <code>HIGH</code>, <code>MEDIUM</code>, and <code>LOW</code>.</p>"""
InsightPriorityLevel: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightPriorityLevel) -> str:
    return value


def deserialize_json(data: str) -> InsightPriorityLevel:
    return cast(InsightPriorityLevel, data)
