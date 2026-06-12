"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The type of an insight field. Possible values are <code>text</code> and <code>metric</code>.</p>"""
InsightFieldType: TypeAlias = Literal[
    "text",
    "metric",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "text",
        "metric",
    )
)


def serialize_json(value: InsightFieldType) -> str:
    return value


def deserialize_json(data: str) -> InsightFieldType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightFieldType value: {data!r}")
    return cast(InsightFieldType, data)
