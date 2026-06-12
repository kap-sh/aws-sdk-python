"""Generated from Smithy shape ``com.amazonaws.batch#DeviceCgroupPermission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

DeviceCgroupPermission: TypeAlias = Literal[
    "READ",
    "WRITE",
    "MKNOD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ",
        "WRITE",
        "MKNOD",
    )
)


def serialize_json(value: DeviceCgroupPermission) -> str:
    return value


def deserialize_json(data: str) -> DeviceCgroupPermission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceCgroupPermission value: {data!r}")
    return cast(DeviceCgroupPermission, data)
