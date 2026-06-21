"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedDataTransferType``."""

from typing import Literal, TypeAlias, cast

SupportedDataTransferType: TypeAlias = Literal[
    "RECORD",
    "FILE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedDataTransferType) -> str:
    return value


def deserialize_json(data: str) -> SupportedDataTransferType:
    return cast(SupportedDataTransferType, data)
