"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#BandwidthWeightingEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

BandwidthWeightingEnum: TypeAlias = Literal[
    "default",
    "vpc-1",
    "ebs-1",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "vpc-1",
        "ebs-1",
    )
)


def serialize_aws_json_1_0(value: BandwidthWeightingEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BandwidthWeightingEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BandwidthWeightingEnum value: {data!r}")
    return cast(BandwidthWeightingEnum, data)
