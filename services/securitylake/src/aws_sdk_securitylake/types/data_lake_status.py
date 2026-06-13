"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securitylake.errors import DeserializationError

DataLakeStatus: TypeAlias = Literal[
    "INITIALIZED",
    "PENDING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZED",
        "PENDING",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: DataLakeStatus) -> str:
    return value


def deserialize_json(data: str) -> DataLakeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataLakeStatus value: {data!r}")
    return cast(DataLakeStatus, data)
