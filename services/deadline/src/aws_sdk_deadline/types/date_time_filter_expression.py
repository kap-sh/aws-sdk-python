"""Generated from Smithy shape ``com.amazonaws.deadline#DateTimeFilterExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.comparison_operator
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.timestamp


class DateTimeFilterExpression(TypedDict):
    name: "aws_sdk_deadline.types.string.String"
    """<p>The name of the date-time field to filter on.</p>"""
    operator: "aws_sdk_deadline.types.comparison_operator.ComparisonOperator"
    """<p>The type of comparison to use to filter the results.</p>"""
    date_time: "aws_sdk_deadline.types.timestamp.Timestamp"
    """<p>The date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeFilterExpression) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_deadline.types.comparison_operator

    out["operator"] = aws_sdk_deadline.types.comparison_operator.serialize_json(
        value["operator"]
    )
    import aws_sdk_deadline.types.timestamp

    out["dateTime"] = aws_sdk_deadline.types.timestamp.serialize_json(
        value["date_time"]
    )
    return out


def deserialize_json(data: dict) -> DateTimeFilterExpression:
    out: DateTimeFilterExpression = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DateTimeFilterExpression.name required")
    if "operator" in data:
        import aws_sdk_deadline.types.comparison_operator

        out["operator"] = aws_sdk_deadline.types.comparison_operator.deserialize_json(
            data["operator"]
        )
    else:
        raise DeserializationError("DateTimeFilterExpression.operator required")
    if "dateTime" in data:
        import aws_sdk_deadline.types.timestamp

        out["date_time"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["dateTime"]
        )
    else:
        raise DeserializationError("DateTimeFilterExpression.date_time required")
    return out
