"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

VolumeFilterName: TypeAlias = Literal[
    "file-system-id",
    "storage-virtual-machine-id",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "file-system-id",
        "storage-virtual-machine-id",
    )
)


def serialize_aws_json_1_1(value: VolumeFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VolumeFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VolumeFilterName value: {data!r}")
    return cast(VolumeFilterName, data)
