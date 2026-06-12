"""Generated from Smithy shape ``com.amazonaws.fsx#S3AccessPointAttachmentsFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.s3_access_point_attachments_filter

S3AccessPointAttachmentsFilters: TypeAlias = list[
    "aws_sdk_fsx.types.s3_access_point_attachments_filter.S3AccessPointAttachmentsFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3AccessPointAttachmentsFilters) -> list:
    import aws_sdk_fsx.types.s3_access_point_attachments_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fsx.types.s3_access_point_attachments_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> S3AccessPointAttachmentsFilters:
    import aws_sdk_fsx.types.s3_access_point_attachments_filter

    out: S3AccessPointAttachmentsFilters = []
    for item in data:
        out.append(
            aws_sdk_fsx.types.s3_access_point_attachments_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
