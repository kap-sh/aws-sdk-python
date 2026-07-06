"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#Datapoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.metric_scale
    import aws_sdk_auto_scaling_plans.types.timestamp_type


class Datapoint(TypedDict, closed=True):
    timestamp: NotRequired[
        "aws_sdk_auto_scaling_plans.types.timestamp_type.TimestampType"
    ]
    """<p>The time stamp for the data point in UTC format.</p>"""
    value: NotRequired["aws_sdk_auto_scaling_plans.types.metric_scale.MetricScale"]
    """<p>The value of the data point.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Datapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_auto_scaling_plans.types.timestamp_type

        out["Timestamp"] = (
            aws_sdk_auto_scaling_plans.types.timestamp_type.serialize_aws_json_1_1(
                value["timestamp"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Datapoint:
    out: Datapoint = {}  # type: ignore[typeddict-item]
    if "Timestamp" in data:
        import aws_sdk_auto_scaling_plans.types.timestamp_type

        out["timestamp"] = (
            aws_sdk_auto_scaling_plans.types.timestamp_type.deserialize_aws_json_1_1(
                data["Timestamp"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
