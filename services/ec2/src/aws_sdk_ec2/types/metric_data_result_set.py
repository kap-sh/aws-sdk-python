"""Generated from Smithy shape ``com.amazonaws.ec2#MetricDataResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric_data_result

MetricDataResultSet: TypeAlias = list[
    "aws_sdk_ec2.types.metric_data_result.MetricDataResult"
]
