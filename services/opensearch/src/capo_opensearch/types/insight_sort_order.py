"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightSortOrder``."""

from typing import Literal, TypeAlias, cast

"""<p>The sort order for listing insights. Possible values are <code>ASC</code> (ascending) and <code>DESC</code> (descending).</p>"""
InsightSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightSortOrder) -> str:
    return value


def deserialize_json(data: str) -> InsightSortOrder:
    return cast(InsightSortOrder, data)
