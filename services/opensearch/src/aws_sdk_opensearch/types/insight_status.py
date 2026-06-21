"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of an insight. Possible values are <code>ACTIVE</code>, <code>RESOLVED</code>, and <code>DISMISSED</code>.</p>"""
InsightStatus: TypeAlias = Literal[
    "ACTIVE",
    "RESOLVED",
    "DISMISSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightStatus) -> str:
    return value


def deserialize_json(data: str) -> InsightStatus:
    return cast(InsightStatus, data)
