"""Generated from Smithy shape ``com.amazonaws.ec2#S3ObjectTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.s3_object_tag

S3ObjectTagList: TypeAlias = list["aws_sdk_ec2.types.s3_object_tag.S3ObjectTag"]
