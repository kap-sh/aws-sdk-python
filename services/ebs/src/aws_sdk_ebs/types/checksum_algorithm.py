"""Generated from Smithy shape ``com.amazonaws.ebs#ChecksumAlgorithm``."""

from typing import Literal, TypeAlias, cast

ChecksumAlgorithm: TypeAlias = Literal["SHA256",]


# --- restJson1 ser/de ---
def serialize_json(value: ChecksumAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> ChecksumAlgorithm:
    return cast(ChecksumAlgorithm, data)
