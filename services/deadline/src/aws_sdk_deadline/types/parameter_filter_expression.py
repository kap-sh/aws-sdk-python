"""Generated from Smithy shape ``com.amazonaws.deadline#ParameterFilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.comparison_operator
    import aws_sdk_deadline.types.parameter_value
    import aws_sdk_deadline.types.string


class ParameterFilterExpression(TypedDict, closed=True):
    name: "aws_sdk_deadline.types.string.String"
    """<p>The name of the parameter to filter on.</p>"""
    operator: "aws_sdk_deadline.types.comparison_operator.ComparisonOperator"
    """<p>The type of comparison to use to filter results.</p>"""
    value: "aws_sdk_deadline.types.parameter_value.ParameterValue"
    """<p>The parameter's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterFilterExpression) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_deadline.types.comparison_operator

    out["operator"] = aws_sdk_deadline.types.comparison_operator.serialize_json(
        value["operator"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ParameterFilterExpression:
    out: ParameterFilterExpression = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ParameterFilterExpression.name required")
    if "operator" in data:
        import aws_sdk_deadline.types.comparison_operator

        out["operator"] = aws_sdk_deadline.types.comparison_operator.deserialize_json(
            data["operator"]
        )
    else:
        raise DeserializationError("ParameterFilterExpression.operator required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("ParameterFilterExpression.value required")
    return out
