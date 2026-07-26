"""Generated from Smithy shape ``com.amazonaws.backup#ScanResourceType``."""

from typing import Literal, TypeAlias, cast

ScanResourceType: TypeAlias = Literal[
    "EBS",
    "EC2",
    "S3",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanResourceType) -> str:
    return value


def deserialize_json(data: str) -> ScanResourceType:
    return cast(ScanResourceType, data)
