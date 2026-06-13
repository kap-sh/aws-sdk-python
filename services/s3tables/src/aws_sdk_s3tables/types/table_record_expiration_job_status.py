"""Generated from Smithy shape ``com.amazonaws.s3tables#TableRecordExpirationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

TableRecordExpirationJobStatus: TypeAlias = Literal[
    "NotYetRun",
    "Successful",
    "Failed",
    "Disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotYetRun",
        "Successful",
        "Failed",
        "Disabled",
    )
)


def serialize_json(value: TableRecordExpirationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> TableRecordExpirationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TableRecordExpirationJobStatus value: {data!r}"
        )
    return cast(TableRecordExpirationJobStatus, data)
