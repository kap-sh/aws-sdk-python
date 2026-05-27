"""Generated from Smithy shape ``com.amazonaws.ec2#MetricSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric

MetricSet: TypeAlias = list["aws_sdk_ec2.types.metric.Metric"]
