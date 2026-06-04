"""Generated from Smithy shape ``com.amazonaws.ecs#DeviceCgroupPermission``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

DeviceCgroupPermission: TypeAlias = Literal[
    "read",
    "write",
    "mknod",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "read",
        "write",
        "mknod",
    )
)


def serialize_aws_json_1_1(value: DeviceCgroupPermission) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceCgroupPermission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceCgroupPermission value: {data!r}")
    return cast(DeviceCgroupPermission, data)
