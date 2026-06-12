"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

DomainState: TypeAlias = Literal[
    "Active",
    "Processing",
    "NotAvailable",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Processing",
        "NotAvailable",
    )
)


def serialize_json(value: DomainState) -> str:
    return value


def deserialize_json(data: str) -> DomainState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainState value: {data!r}")
    return cast(DomainState, data)
