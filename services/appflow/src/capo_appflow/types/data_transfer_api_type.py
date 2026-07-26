"""Generated from Smithy shape ``com.amazonaws.appflow#DataTransferApiType``."""

from typing import Literal, TypeAlias, cast

DataTransferApiType: TypeAlias = Literal[
    "SYNC",
    "ASYNC",
    "AUTOMATIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataTransferApiType) -> str:
    return value


def deserialize_json(data: str) -> DataTransferApiType:
    return cast(DataTransferApiType, data)
