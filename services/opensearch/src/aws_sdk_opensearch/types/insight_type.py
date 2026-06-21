"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of an insight. Possible values are <code>EVENT</code> and <code>RECOMMENDATION</code>.</p>"""
InsightType: TypeAlias = Literal[
    "EVENT",
    "RECOMMENDATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightType) -> str:
    return value


def deserialize_json(data: str) -> InsightType:
    return cast(InsightType, data)
