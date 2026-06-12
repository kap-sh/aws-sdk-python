"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentsFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.s3_access_point_attachments_filter_value

S3AccessPointAttachmentsFilterValues: TypeAlias = list[
    "aws_sdk_fsx.types.s3_access_point_attachments_filter_value.S3AccessPointAttachmentsFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointAttachmentsFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> S3AccessPointAttachmentsFilterValues:
    return list(data)
