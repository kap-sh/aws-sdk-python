"""Generated from Smithy shape ``com.amazonaws.securitylake#SourceCollectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securitylake.errors import DeserializationError

SourceCollectionStatus: TypeAlias = Literal[
    "COLLECTING",
    "MISCONFIGURED",
    "NOT_COLLECTING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COLLECTING",
        "MISCONFIGURED",
        "NOT_COLLECTING",
    )
)


def serialize_json(value: SourceCollectionStatus) -> str:
    return value


def deserialize_json(data: str) -> SourceCollectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceCollectionStatus value: {data!r}")
    return cast(SourceCollectionStatus, data)
