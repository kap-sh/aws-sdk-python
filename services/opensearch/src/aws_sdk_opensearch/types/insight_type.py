"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The type of an insight. Possible values are <code>EVENT</code> and <code>RECOMMENDATION</code>.</p>"""
InsightType: TypeAlias = Literal[
    "EVENT",
    "RECOMMENDATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EVENT",
        "RECOMMENDATION",
    )
)


def serialize_json(value: InsightType) -> str:
    return value


def deserialize_json(data: str) -> InsightType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightType value: {data!r}")
    return cast(InsightType, data)
