"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightFieldType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of an insight field. Possible values are <code>text</code> and <code>metric</code>.</p>"""
InsightFieldType: TypeAlias = Literal[
    "text",
    "metric",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightFieldType) -> str:
    return value


def deserialize_json(data: str) -> InsightFieldType:
    return cast(InsightFieldType, data)
