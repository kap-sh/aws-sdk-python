"""Generated from Smithy shape ``com.amazonaws.ec2#MetricValueSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric_value

MetricValueSet: TypeAlias = list["aws_sdk_ec2.types.metric_value.MetricValue"]
