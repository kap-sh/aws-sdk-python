"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceVolumeDetailSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_instance_volume_detail_item

ImportInstanceVolumeDetailSet: TypeAlias = list[
    "aws_sdk_ec2.types.import_instance_volume_detail_item.ImportInstanceVolumeDetailItem"
]
