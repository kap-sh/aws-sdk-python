"""Generated from Smithy shape ``com.amazonaws.autoscaling#GetPredictiveScalingForecastType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.timestamp_type
    import capo_auto_scaling.types.xml_string_max_len255


class GetPredictiveScalingForecastType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    policy_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the policy.</p>"""
    start_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The inclusive start time of the time range for the forecast data to get. At most, the date and time can be one year before the current date and time.</p>"""
    end_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is 30 days. </p> <p>Although this parameter can accept a date and time that is more than two days in the future, the availability of forecast data has limits. Amazon EC2 Auto Scaling only issues forecasts for periods of two days in advance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetPredictiveScalingForecastType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "policy_name" in value:
        pairs.append((f"{prefix}.PolicyName", str(value["policy_name"])))
    if "start_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )


def deserialize_query(el: Element) -> GetPredictiveScalingForecastType:
    out: GetPredictiveScalingForecastType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["start_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["end_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_end_time
        )
    return out
