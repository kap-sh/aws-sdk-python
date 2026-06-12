"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#SimpleRuleEvaluation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.comparison_operator
    import aws_sdk_iot_events_data.types.input_property_value
    import aws_sdk_iot_events_data.types.threshold_value


class SimpleRuleEvaluation(TypedDict):
    input_property_value: NotRequired[
        "aws_sdk_iot_events_data.types.input_property_value.InputPropertyValue"
    ]
    """<p>The value of the input property, on the left side of the comparison operator.</p>"""
    operator: NotRequired[
        "aws_sdk_iot_events_data.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The comparison operator.</p>"""
    threshold_value: NotRequired[
        "aws_sdk_iot_events_data.types.threshold_value.ThresholdValue"
    ]
    """<p>The threshold value, on the right side of the comparison operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimpleRuleEvaluation) -> dict:
    out: dict = {}
    if "input_property_value" in value:
        out["inputPropertyValue"] = value["input_property_value"]
    if "operator" in value:
        import aws_sdk_iot_events_data.types.comparison_operator

        out["operator"] = (
            aws_sdk_iot_events_data.types.comparison_operator.serialize_json(
                value["operator"]
            )
        )
    if "threshold_value" in value:
        out["thresholdValue"] = value["threshold_value"]
    return out


def deserialize_json(data: dict) -> SimpleRuleEvaluation:
    out: SimpleRuleEvaluation = {}  # type: ignore[typeddict-item]
    if "inputPropertyValue" in data:
        out["input_property_value"] = data["inputPropertyValue"]
    if "operator" in data:
        import aws_sdk_iot_events_data.types.comparison_operator

        out["operator"] = (
            aws_sdk_iot_events_data.types.comparison_operator.deserialize_json(
                data["operator"]
            )
        )
    if "thresholdValue" in data:
        out["threshold_value"] = data["thresholdValue"]
    return out
