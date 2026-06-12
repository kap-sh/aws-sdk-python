"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#MetricDimension``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.metric_dimension_name
    import aws_sdk_application_auto_scaling.types.metric_dimension_value


class MetricDimension(TypedDict):
    name: "aws_sdk_application_auto_scaling.types.metric_dimension_name.MetricDimensionName"
    """<p>The name of the dimension.</p>"""
    value: "aws_sdk_application_auto_scaling.types.metric_dimension_value.MetricDimensionValue"
    """<p>The value of the dimension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDimension) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDimension:
    out: MetricDimension = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("MetricDimension.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("MetricDimension.value required")
    return out
