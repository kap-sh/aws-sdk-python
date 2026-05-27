"""Generated from Smithy shape ``com.amazonaws.ec2#ReasonCodesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.report_instance_reason_codes

ReasonCodesList: TypeAlias = list[
    "aws_sdk_ec2.types.report_instance_reason_codes.ReportInstanceReasonCodes"
]
