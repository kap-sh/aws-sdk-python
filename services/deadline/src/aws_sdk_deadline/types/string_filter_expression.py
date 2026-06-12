"""Generated from Smithy shape ``com.amazonaws.deadline#StringFilterExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.comparison_operator
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.string_filter


class StringFilterExpression(TypedDict):
    name: "aws_sdk_deadline.types.string.String"
    """<p>The field name to search.</p>"""
    operator: "aws_sdk_deadline.types.comparison_operator.ComparisonOperator"
    """<p>The type of comparison to use for this search.</p>"""
    value: "aws_sdk_deadline.types.string_filter.StringFilter"
    """<p>The string to search for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringFilterExpression) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_deadline.types.comparison_operator

    out["operator"] = aws_sdk_deadline.types.comparison_operator.serialize_json(
        value["operator"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> StringFilterExpression:
    out: StringFilterExpression = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StringFilterExpression.name required")
    if "operator" in data:
        import aws_sdk_deadline.types.comparison_operator

        out["operator"] = aws_sdk_deadline.types.comparison_operator.deserialize_json(
            data["operator"]
        )
    else:
        raise DeserializationError("StringFilterExpression.operator required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("StringFilterExpression.value required")
    return out
