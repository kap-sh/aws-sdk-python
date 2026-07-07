"""Generated from Smithy shape ``com.amazonaws.iot#AggregationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aggregation_type_name
    import aws_sdk_iot.types.aggregation_type_values


class AggregationType(TypedDict, closed=True):
    name: "aws_sdk_iot.types.aggregation_type_name.AggregationTypeName"
    """<p>The name of the aggregation type.</p>"""
    values: NotRequired[
        "aws_sdk_iot.types.aggregation_type_values.AggregationTypeValues"
    ]
    """<p>A list of the values of aggregation types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationType) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.aggregation_type_name

    out["name"] = aws_sdk_iot.types.aggregation_type_name.serialize_json(value["name"])
    if "values" in value:
        import aws_sdk_iot.types.aggregation_type_values

        out["values"] = aws_sdk_iot.types.aggregation_type_values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> AggregationType:
    out: AggregationType = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_iot.types.aggregation_type_name

        out["name"] = aws_sdk_iot.types.aggregation_type_name.deserialize_json(
            data["name"]
        )
    else:
        raise DeserializationError("AggregationType.name required")
    if "values" in data:
        import aws_sdk_iot.types.aggregation_type_values

        out["values"] = aws_sdk_iot.types.aggregation_type_values.deserialize_json(
            data["values"]
        )
    return out
