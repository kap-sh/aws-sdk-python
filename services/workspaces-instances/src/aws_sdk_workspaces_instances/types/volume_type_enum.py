"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#VolumeTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

VolumeTypeEnum: TypeAlias = Literal[
    "standard",
    "io1",
    "io2",
    "gp2",
    "sc1",
    "st1",
    "gp3",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "io1",
        "io2",
        "gp2",
        "sc1",
        "st1",
        "gp3",
    )
)


def serialize_aws_json_1_0(value: VolumeTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VolumeTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VolumeTypeEnum value: {data!r}")
    return cast(VolumeTypeEnum, data)
