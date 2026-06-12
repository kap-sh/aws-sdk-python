"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedDataTransferType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

SupportedDataTransferType: TypeAlias = Literal[
    "RECORD",
    "FILE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RECORD",
        "FILE",
    )
)


def serialize_json(value: SupportedDataTransferType) -> str:
    return value


def deserialize_json(data: str) -> SupportedDataTransferType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SupportedDataTransferType value: {data!r}")
    return cast(SupportedDataTransferType, data)
