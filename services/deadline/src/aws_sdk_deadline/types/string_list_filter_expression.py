"""Generated from Smithy shape ``com.amazonaws.deadline#StringListFilterExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.comparison_operator
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.string_filter_list


class StringListFilterExpression(TypedDict):
    name: "aws_sdk_deadline.types.string.String"
    """<p>The field name to search.</p>"""
    operator: "aws_sdk_deadline.types.comparison_operator.ComparisonOperator"
    """<p>The type of comparison to use for this search.</p>"""
    values: "aws_sdk_deadline.types.string_filter_list.StringFilterList"
    """<p>The list of string values to search for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringListFilterExpression) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_deadline.types.comparison_operator

    out["operator"] = aws_sdk_deadline.types.comparison_operator.serialize_json(
        value["operator"]
    )
    import aws_sdk_deadline.types.string_filter_list

    out["values"] = aws_sdk_deadline.types.string_filter_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> StringListFilterExpression:
    out: StringListFilterExpression = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StringListFilterExpression.name required")
    if "operator" in data:
        import aws_sdk_deadline.types.comparison_operator

        out["operator"] = aws_sdk_deadline.types.comparison_operator.deserialize_json(
            data["operator"]
        )
    else:
        raise DeserializationError("StringListFilterExpression.operator required")
    if "values" in data:
        import aws_sdk_deadline.types.string_filter_list

        out["values"] = aws_sdk_deadline.types.string_filter_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("StringListFilterExpression.values required")
    return out
