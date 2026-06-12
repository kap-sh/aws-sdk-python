"""Generated from Smithy shape ``com.amazonaws.appflow#DataTransferApiType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

DataTransferApiType: TypeAlias = Literal[
    "SYNC",
    "ASYNC",
    "AUTOMATIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYNC",
        "ASYNC",
        "AUTOMATIC",
    )
)


def serialize_json(value: DataTransferApiType) -> str:
    return value


def deserialize_json(data: str) -> DataTransferApiType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataTransferApiType value: {data!r}")
    return cast(DataTransferApiType, data)
