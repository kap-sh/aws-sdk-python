"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#ChecksumType``."""

from typing import Literal, TypeAlias, cast

ChecksumType: TypeAlias = Literal["SHA1",]


# --- restJson1 ser/de ---
def serialize_json(value: ChecksumType) -> str:
    return value


def deserialize_json(data: str) -> ChecksumType:
    return cast(ChecksumType, data)
