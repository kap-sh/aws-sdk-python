"""Generated from Smithy shape ``com.amazonaws.datazone#FilterExpression``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.filter_expression_type


class FilterExpression(TypedDict):
    type: "aws_sdk_datazone.types.filter_expression_type.FilterExpressionType"
    """<p>The search filter explresison type.</p>"""
    expression: "str"
    """<p>The search filter expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterExpression) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.filter_expression_type

    out["type"] = aws_sdk_datazone.types.filter_expression_type.serialize_json(
        value["type"]
    )
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> FilterExpression:
    out: FilterExpression = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_datazone.types.filter_expression_type

        out["type"] = aws_sdk_datazone.types.filter_expression_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("FilterExpression.type required")
    if "expression" in data:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("FilterExpression.expression required")
    return out
