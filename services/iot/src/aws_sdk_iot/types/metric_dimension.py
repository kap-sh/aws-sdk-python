"""Generated from Smithy shape ``com.amazonaws.iot#MetricDimension``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.dimension_name
    import aws_sdk_iot.types.dimension_value_operator


class MetricDimension(TypedDict):
    dimension_name: "aws_sdk_iot.types.dimension_name.DimensionName"
    """<p>A unique identifier for the dimension.</p>"""
    operator: NotRequired[
        "aws_sdk_iot.types.dimension_value_operator.DimensionValueOperator"
    ]
    """<p>Defines how the <code>dimensionValues</code> of a dimension are interpreted. For example, for dimension type TOPIC_FILTER, the <code>IN</code> operator, a message will be counted only if its topic matches one of the topic filters. With <code>NOT_IN</code> operator, a message will be counted only if it doesn't match any of the topic filters. The operator is optional: if it's not provided (is <code>null</code>), it will be interpreted as <code>IN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDimension) -> dict:
    out: dict = {}
    out["dimensionName"] = value["dimension_name"]
    if "operator" in value:
        import aws_sdk_iot.types.dimension_value_operator

        out["operator"] = aws_sdk_iot.types.dimension_value_operator.serialize_json(
            value["operator"]
        )
    return out


def deserialize_json(data: dict) -> MetricDimension:
    out: MetricDimension = {}  # type: ignore[typeddict-item]
    if "dimensionName" in data:
        out["dimension_name"] = data["dimensionName"]
    else:
        raise DeserializationError("MetricDimension.dimension_name required")
    if "operator" in data:
        import aws_sdk_iot.types.dimension_value_operator

        out["operator"] = aws_sdk_iot.types.dimension_value_operator.deserialize_json(
            data["operator"]
        )
    return out
