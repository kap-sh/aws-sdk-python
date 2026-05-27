"""Generated from Smithy shape ``com.amazonaws.ec2#EbsStatusDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ebs_status_details

EbsStatusDetailsList: TypeAlias = list[
    "aws_sdk_ec2.types.ebs_status_details.EbsStatusDetails"
]
