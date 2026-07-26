"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.s3_access_point_attachment_name

S3AccessPointAttachmentNames: TypeAlias = list[
    "capo_fsx.types.s3_access_point_attachment_name.S3AccessPointAttachmentName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointAttachmentNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> S3AccessPointAttachmentNames:
    return list(data)
