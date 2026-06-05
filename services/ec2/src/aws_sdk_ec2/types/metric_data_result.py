"""Generated from Smithy shape ``com.amazonaws.ec2#MetricDataResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MetricDataResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dimension" in value:
        import aws_sdk_ec2.types.capacity_manager_dimension

        aws_sdk_ec2.types.capacity_manager_dimension.serialize_ec2_query(
            value["dimension"], pairs, f"{prefix}.Dimension"
        )
    if "timestamp" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["timestamp"], pairs, f"{prefix}.Timestamp"
        )
    if "metric_values" in value:
        import aws_sdk_ec2.types.metric_value_set

        aws_sdk_ec2.types.metric_value_set.serialize_ec2_query(
            value["metric_values"], pairs, f"{prefix}.MetricValueSet"
        )


def deserialize_ec2_query(el: Element) -> MetricDataResult:
    out: MetricDataResult = {}  # type: ignore[typeddict-item]
    child_dimension = el.find("Dimension")
    if child_dimension is not None:
        import aws_sdk_ec2.types.capacity_manager_dimension

        out["dimension"] = (
            aws_sdk_ec2.types.capacity_manager_dimension.deserialize_ec2_query(
                child_dimension
            )
        )
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["timestamp"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_timestamp
            )
        )
    if el.find("MetricValueSet") is not None:
        import aws_sdk_ec2.types.metric_value_set

        out["metric_values"] = aws_sdk_ec2.types.metric_value_set.deserialize_ec2_query(
            el, "MetricValueSet"
        )
    return out
