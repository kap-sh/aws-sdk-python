"""Generated from Smithy shape ``com.amazonaws.ec2#MetricDataResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_dimension
    import aws_sdk_ec2.types.metric_value_set
    import aws_sdk_ec2.types.millisecond_date_time


class MetricDataResult(TypedDict):
    dimension: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_dimension.CapacityManagerDimension"
    ]
    """<p> The dimension values that identify this specific data point, such as account ID, region, and instance family. </p>"""
    timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp for this data point, indicating when the capacity usage occurred. </p>"""
    metric_values: NotRequired["aws_sdk_ec2.types.metric_value_set.MetricValueSet"]
    """<p> The metric values and statistics for this data point, containing the actual capacity usage numbers. </p>"""
