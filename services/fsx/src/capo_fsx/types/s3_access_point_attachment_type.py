"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentType``."""

from typing import Literal, TypeAlias, cast

S3AccessPointAttachmentType: TypeAlias = Literal[
    "OPENZFS",
    "ONTAP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointAttachmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3AccessPointAttachmentType:
    return cast(S3AccessPointAttachmentType, data)
