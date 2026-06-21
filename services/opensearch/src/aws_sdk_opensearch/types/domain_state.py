"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainState``."""

from typing import Literal, TypeAlias, cast

DomainState: TypeAlias = Literal[
    "Active",
    "Processing",
    "NotAvailable",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainState) -> str:
    return value


def deserialize_json(data: str) -> DomainState:
    return cast(DomainState, data)
