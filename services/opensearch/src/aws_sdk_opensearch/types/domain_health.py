"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainHealth``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

DomainHealth: TypeAlias = Literal[
    "Red",
    "Yellow",
    "Green",
    "NotAvailable",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Red",
        "Yellow",
        "Green",
        "NotAvailable",
    )
)


def serialize_json(value: DomainHealth) -> str:
    return value


def deserialize_json(data: str) -> DomainHealth:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainHealth value: {data!r}")
    return cast(DomainHealth, data)
