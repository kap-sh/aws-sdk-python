"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The sort order for listing insights. Possible values are <code>ASC</code> (ascending) and <code>DESC</code> (descending).</p>"""
InsightSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_json(value: InsightSortOrder) -> str:
    return value


def deserialize_json(data: str) -> InsightSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightSortOrder value: {data!r}")
    return cast(InsightSortOrder, data)
