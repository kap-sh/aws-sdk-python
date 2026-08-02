"""Generated from Smithy shape ``com.amazonaws.ec2#MetricDataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_dimension
    import capo_ec2.types.metric_value_set
    import capo_ec2.types.millisecond_date_time


class MetricDataResult(TypedDict, closed=True):
    dimension: NotRequired[
        "capo_ec2.types.capacity_manager_dimension.CapacityManagerDimension"
    ]
    """<p> The dimension values that identify this specific data point, such as account ID, region, and instance family. </p>"""
    timestamp: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p> The timestamp for this data point, indicating when the capacity usage occurred. </p>"""
    metric_values: NotRequired["capo_ec2.types.metric_value_set.MetricValueSet"]
    """<p> The metric values and statistics for this data point, containing the actual capacity usage numbers. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MetricDataResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dimension" in value:
        import capo_ec2.types.capacity_manager_dimension

        capo_ec2.types.capacity_manager_dimension.serialize_ec2_query(
            value["dimension"], pairs, f"{key_prefix}Dimension"
        )
    if "timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )
    if "metric_values" in value:
        import capo_ec2.types.metric_value_set

        capo_ec2.types.metric_value_set.serialize_ec2_query(
            value["metric_values"], pairs, f"{key_prefix}MetricValueSet"
        )


def deserialize_ec2_query(el: Element) -> MetricDataResult:
    out: MetricDataResult = {}  # type: ignore[typeddict-item]
    child_dimension = el.find("Dimension")
    if child_dimension is not None:
        import capo_ec2.types.capacity_manager_dimension

        out["dimension"] = (
            capo_ec2.types.capacity_manager_dimension.deserialize_ec2_query(
                child_dimension
            )
        )
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["timestamp"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_timestamp
        )
    if el.find("MetricValueSet") is not None:
        import capo_ec2.types.metric_value_set

        out["metric_values"] = capo_ec2.types.metric_value_set.deserialize_ec2_query(
            el, "MetricValueSet"
        )
    return out
