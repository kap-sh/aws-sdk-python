"""Generated from Smithy shape ``com.amazonaws.sagemaker#VolumeAttachmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

VolumeAttachmentStatus: TypeAlias = Literal[
    "attaching",
    "attached",
    "detaching",
    "detached",
    "busy",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "attaching",
        "attached",
        "detaching",
        "detached",
        "busy",
    )
)


def serialize_aws_json_1_1(value: VolumeAttachmentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VolumeAttachmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VolumeAttachmentStatus value: {data!r}")
    return cast(VolumeAttachmentStatus, data)
