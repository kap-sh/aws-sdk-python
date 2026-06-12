"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

VolumeType: TypeAlias = Literal[
    "ONTAP",
    "OPENZFS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONTAP",
        "OPENZFS",
    )
)


def serialize_aws_json_1_1(value: VolumeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VolumeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VolumeType value: {data!r}")
    return cast(VolumeType, data)
