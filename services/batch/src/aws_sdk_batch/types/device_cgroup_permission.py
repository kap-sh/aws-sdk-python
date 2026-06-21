"""Generated from Smithy shape ``com.amazonaws.batch#DeviceCgroupPermission``."""

from typing import Literal, TypeAlias, cast

DeviceCgroupPermission: TypeAlias = Literal[
    "READ",
    "WRITE",
    "MKNOD",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceCgroupPermission) -> str:
    return value


def deserialize_json(data: str) -> DeviceCgroupPermission:
    return cast(DeviceCgroupPermission, data)
