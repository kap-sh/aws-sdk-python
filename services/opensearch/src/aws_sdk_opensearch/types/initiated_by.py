"""Generated from Smithy shape ``com.amazonaws.opensearch#InitiatedBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

InitiatedBy: TypeAlias = Literal[
    "CUSTOMER",
    "SERVICE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER",
        "SERVICE",
    )
)


def serialize_json(value: InitiatedBy) -> str:
    return value


def deserialize_json(data: str) -> InitiatedBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InitiatedBy value: {data!r}")
    return cast(InitiatedBy, data)
