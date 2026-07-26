"""Generated from Smithy shape ``com.amazonaws.iot#CannedAccessControlList``."""

from typing import Literal, TypeAlias, cast

CannedAccessControlList: TypeAlias = Literal[
    "private",
    "public-read",
    "public-read-write",
    "aws-exec-read",
    "authenticated-read",
    "bucket-owner-read",
    "bucket-owner-full-control",
    "log-delivery-write",
]


# --- restJson1 ser/de ---
def serialize_json(value: CannedAccessControlList) -> str:
    return value


def deserialize_json(data: str) -> CannedAccessControlList:
    return cast(CannedAccessControlList, data)
