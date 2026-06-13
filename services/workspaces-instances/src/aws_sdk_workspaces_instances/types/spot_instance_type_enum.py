"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#SpotInstanceTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

SpotInstanceTypeEnum: TypeAlias = Literal[
    "one-time",
    "persistent",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "one-time",
        "persistent",
    )
)


def serialize_aws_json_1_0(value: SpotInstanceTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SpotInstanceTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SpotInstanceTypeEnum value: {data!r}")
    return cast(SpotInstanceTypeEnum, data)
