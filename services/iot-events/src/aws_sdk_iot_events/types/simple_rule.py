"""Generated from Smithy shape ``com.amazonaws.iotevents#SimpleRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.comparison_operator
    import aws_sdk_iot_events.types.input_property
    import aws_sdk_iot_events.types.threshold


class SimpleRule(TypedDict):
    input_property: "aws_sdk_iot_events.types.input_property.InputProperty"
    """<p>The value on the left side of the comparison operator. You can specify an AWS IoT Events input attribute as an input property.</p>"""
    comparison_operator: (
        "aws_sdk_iot_events.types.comparison_operator.ComparisonOperator"
    )
    """<p>The comparison operator.</p>"""
    threshold: "aws_sdk_iot_events.types.threshold.Threshold"
    """<p>The value on the right side of the comparison operator. You can enter a number or specify an AWS IoT Events input attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimpleRule) -> dict:
    out: dict = {}
    out["inputProperty"] = value["input_property"]
    import aws_sdk_iot_events.types.comparison_operator

    out["comparisonOperator"] = (
        aws_sdk_iot_events.types.comparison_operator.serialize_json(
            value["comparison_operator"]
        )
    )
    out["threshold"] = value["threshold"]
    return out


def deserialize_json(data: dict) -> SimpleRule:
    out: SimpleRule = {}  # type: ignore[typeddict-item]
    if "inputProperty" in data:
        out["input_property"] = data["inputProperty"]
    else:
        raise DeserializationError("SimpleRule.input_property required")
    if "comparisonOperator" in data:
        import aws_sdk_iot_events.types.comparison_operator

        out["comparison_operator"] = (
            aws_sdk_iot_events.types.comparison_operator.deserialize_json(
                data["comparisonOperator"]
            )
        )
    else:
        raise DeserializationError("SimpleRule.comparison_operator required")
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    else:
        raise DeserializationError("SimpleRule.threshold required")
    return out
