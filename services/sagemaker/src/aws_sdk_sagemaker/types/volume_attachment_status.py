"""Generated from Smithy shape ``com.amazonaws.sagemaker#VolumeAttachmentStatus``."""

from typing import Literal, TypeAlias, cast

VolumeAttachmentStatus: TypeAlias = Literal[
    "attaching",
    "attached",
    "detaching",
    "detached",
    "busy",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeAttachmentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VolumeAttachmentStatus:
    return cast(VolumeAttachmentStatus, data)
