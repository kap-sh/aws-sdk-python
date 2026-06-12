"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerMountPointAccessLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ContainerMountPointAccessLevel: TypeAlias = Literal[
    "READ_ONLY",
    "READ_AND_WRITE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ_ONLY",
        "READ_AND_WRITE",
    )
)


def serialize_aws_json_1_1(value: ContainerMountPointAccessLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerMountPointAccessLevel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContainerMountPointAccessLevel value: {data!r}"
        )
    return cast(ContainerMountPointAccessLevel, data)
