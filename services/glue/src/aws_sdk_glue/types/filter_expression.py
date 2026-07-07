"""Generated from Smithy shape ``com.amazonaws.glue#FilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.boxed_boolean
    import aws_sdk_glue.types.filter_operation
    import aws_sdk_glue.types.filter_values


class FilterExpression(TypedDict, closed=True):
    operation: "aws_sdk_glue.types.filter_operation.FilterOperation"
    """<p>The type of operation to perform in the expression.</p>"""
    negated: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Whether the expression is to be negated.</p>"""
    values: "aws_sdk_glue.types.filter_values.FilterValues"
    """<p>A list of filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterExpression) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.filter_operation

    out["Operation"] = aws_sdk_glue.types.filter_operation.serialize_aws_json_1_1(
        value["operation"]
    )
    if "negated" in value:
        out["Negated"] = value["negated"]
    import aws_sdk_glue.types.filter_values

    out["Values"] = aws_sdk_glue.types.filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterExpression:
    out: FilterExpression = {}  # type: ignore[typeddict-item]
    if "Operation" in data:
        import aws_sdk_glue.types.filter_operation

        out["operation"] = aws_sdk_glue.types.filter_operation.deserialize_aws_json_1_1(
            data["Operation"]
        )
    else:
        raise DeserializationError("FilterExpression.operation required")
    if "Negated" in data:
        out["negated"] = data["Negated"]
    if "Values" in data:
        import aws_sdk_glue.types.filter_values

        out["values"] = aws_sdk_glue.types.filter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        raise DeserializationError("FilterExpression.values required")
    return out
