"""Generated from Smithy shape ``com.amazonaws.finspace#FederationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

FederationMode: TypeAlias = Literal[
    "FEDERATED",
    "LOCAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FEDERATED",
        "LOCAL",
    )
)


def serialize_json(value: FederationMode) -> str:
    return value


def deserialize_json(data: str) -> FederationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FederationMode value: {data!r}")
    return cast(FederationMode, data)
