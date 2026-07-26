"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainHealth``."""

from typing import Literal, TypeAlias, cast

DomainHealth: TypeAlias = Literal[
    "Red",
    "Yellow",
    "Green",
    "NotAvailable",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainHealth) -> str:
    return value


def deserialize_json(data: str) -> DomainHealth:
    return cast(DomainHealth, data)
