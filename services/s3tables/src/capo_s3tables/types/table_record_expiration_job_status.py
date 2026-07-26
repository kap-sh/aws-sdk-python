"""Generated from Smithy shape ``com.amazonaws.s3tables#TableRecordExpirationJobStatus``."""

from typing import Literal, TypeAlias, cast

TableRecordExpirationJobStatus: TypeAlias = Literal[
    "NotYetRun",
    "Successful",
    "Failed",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableRecordExpirationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> TableRecordExpirationJobStatus:
    return cast(TableRecordExpirationJobStatus, data)
