"""Generated from Smithy shape ``com.amazonaws.s3tables#TableRecordExpirationStatus``."""

from typing import Literal, TypeAlias, cast

TableRecordExpirationStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableRecordExpirationStatus) -> str:
    return value


def deserialize_json(data: str) -> TableRecordExpirationStatus:
    return cast(TableRecordExpirationStatus, data)
