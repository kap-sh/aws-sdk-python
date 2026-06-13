"""Generated from Smithy shape ``com.amazonaws.s3tables#TableRecordExpirationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

TableRecordExpirationStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def serialize_json(value: TableRecordExpirationStatus) -> str:
    return value


def deserialize_json(data: str) -> TableRecordExpirationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TableRecordExpirationStatus value: {data!r}"
        )
    return cast(TableRecordExpirationStatus, data)
