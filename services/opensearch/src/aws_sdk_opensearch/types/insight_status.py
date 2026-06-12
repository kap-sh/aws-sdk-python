"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The status of an insight. Possible values are <code>ACTIVE</code>, <code>RESOLVED</code>, and <code>DISMISSED</code>.</p>"""
InsightStatus: TypeAlias = Literal[
    "ACTIVE",
    "RESOLVED",
    "DISMISSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "RESOLVED",
        "DISMISSED",
    )
)


def serialize_json(value: InsightStatus) -> str:
    return value


def deserialize_json(data: str) -> InsightStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightStatus value: {data!r}")
    return cast(InsightStatus, data)
