"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The type of entity for which to retrieve insights. Possible values are <code>Account</code> and <code>DomainName</code>.</p>"""
InsightEntityType: TypeAlias = Literal[
    "Account",
    "DomainName",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Account",
        "DomainName",
    )
)


def serialize_json(value: InsightEntityType) -> str:
    return value


def deserialize_json(data: str) -> InsightEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightEntityType value: {data!r}")
    return cast(InsightEntityType, data)
