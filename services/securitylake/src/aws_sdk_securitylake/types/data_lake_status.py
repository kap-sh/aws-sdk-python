"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeStatus``."""

from typing import Literal, TypeAlias, cast

DataLakeStatus: TypeAlias = Literal[
    "INITIALIZED",
    "PENDING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeStatus) -> str:
    return value


def deserialize_json(data: str) -> DataLakeStatus:
    return cast(DataLakeStatus, data)
