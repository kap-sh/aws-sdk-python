"""Generated from Smithy shape ``com.amazonaws.outposts#SupportedStorageEnum``."""

from typing import Literal, TypeAlias, cast

SupportedStorageEnum: TypeAlias = Literal[
    "EBS",
    "S3",
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedStorageEnum) -> str:
    return value


def deserialize_json(data: str) -> SupportedStorageEnum:
    return cast(SupportedStorageEnum, data)
