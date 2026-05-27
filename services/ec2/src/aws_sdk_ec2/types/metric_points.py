"""Generated from Smithy shape ``com.amazonaws.ec2#MetricPoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric_point

MetricPoints: TypeAlias = list["aws_sdk_ec2.types.metric_point.MetricPoint"]
