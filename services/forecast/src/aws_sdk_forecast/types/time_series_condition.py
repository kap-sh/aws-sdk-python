"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesCondition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.attribute_value
    import aws_sdk_forecast.types.condition
    import aws_sdk_forecast.types.name


class TimeSeriesCondition(TypedDict):
    attribute_name: "aws_sdk_forecast.types.name.Name"
    """<p>The item_id, dimension name, IM name, or timestamp that you are modifying.</p>"""
    attribute_value: "aws_sdk_forecast.types.attribute_value.AttributeValue"
    """<p>The value that is applied for the chosen <code>Condition</code>.</p>"""
    condition: "aws_sdk_forecast.types.condition.Condition"
    """<p>The condition to apply. Valid values are <code>EQUALS</code>, <code>NOT_EQUALS</code>, <code>LESS_THAN</code> and <code>GREATER_THAN</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesCondition) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    out["AttributeValue"] = value["attribute_value"]
    import aws_sdk_forecast.types.condition

    out["Condition"] = aws_sdk_forecast.types.condition.serialize_aws_json_1_1(
        value["condition"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeSeriesCondition:
    out: TimeSeriesCondition = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("TimeSeriesCondition.attribute_name required")
    if "AttributeValue" in data:
        out["attribute_value"] = data["AttributeValue"]
    else:
        raise DeserializationError("TimeSeriesCondition.attribute_value required")
    if "Condition" in data:
        import aws_sdk_forecast.types.condition

        out["condition"] = aws_sdk_forecast.types.condition.deserialize_aws_json_1_1(
            data["Condition"]
        )
    else:
        raise DeserializationError("TimeSeriesCondition.condition required")
    return out
