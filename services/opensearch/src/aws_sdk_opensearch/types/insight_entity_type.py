"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightEntityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of entity for which to retrieve insights. Possible values are <code>Account</code> and <code>DomainName</code>.</p>"""
InsightEntityType: TypeAlias = Literal[
    "Account",
    "DomainName",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightEntityType) -> str:
    return value


def deserialize_json(data: str) -> InsightEntityType:
    return cast(InsightEntityType, data)
