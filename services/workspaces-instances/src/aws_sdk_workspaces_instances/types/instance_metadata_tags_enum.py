"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceMetadataTagsEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

InstanceMetadataTagsEnum: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def serialize_aws_json_1_0(value: InstanceMetadataTagsEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceMetadataTagsEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceMetadataTagsEnum value: {data!r}")
    return cast(InstanceMetadataTagsEnum, data)
