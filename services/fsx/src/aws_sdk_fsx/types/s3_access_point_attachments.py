"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.s3_access_point_attachment

S3AccessPointAttachments: TypeAlias = list[
    "aws_sdk_fsx.types.s3_access_point_attachment.S3AccessPointAttachment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointAttachments) -> list:
    import aws_sdk_fsx.types.s3_access_point_attachment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fsx.types.s3_access_point_attachment.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> S3AccessPointAttachments:
    import aws_sdk_fsx.types.s3_access_point_attachment

    out: S3AccessPointAttachments = []
    for item in data:
        out.append(
            aws_sdk_fsx.types.s3_access_point_attachment.deserialize_aws_json_1_1(item)
        )
    return out
