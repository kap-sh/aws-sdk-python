"""Generated from Smithy shape ``com.amazonaws.budgets#ExpressionDimensionValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.dimension
    import aws_sdk_budgets.types.match_options
    import aws_sdk_budgets.types.values


class ExpressionDimensionValues(TypedDict, closed=True):
    key: "aws_sdk_budgets.types.dimension.Dimension"
    """<p>The name of the dimension that you want to filter on.</p>"""
    values: "aws_sdk_budgets.types.values.Values"
    """<p>The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.</p>"""
    match_options: NotRequired["aws_sdk_budgets.types.match_options.MatchOptions"]
    """<p>The match options that you can use to filter your results. You can specify only one of these values in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressionDimensionValues) -> dict:
    out: dict = {}
    import aws_sdk_budgets.types.dimension

    out["Key"] = aws_sdk_budgets.types.dimension.serialize_aws_json_1_1(value["key"])
    import aws_sdk_budgets.types.values

    out["Values"] = aws_sdk_budgets.types.values.serialize_aws_json_1_1(value["values"])
    if "match_options" in value:
        import aws_sdk_budgets.types.match_options

        out["MatchOptions"] = (
            aws_sdk_budgets.types.match_options.serialize_aws_json_1_1(
                value["match_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressionDimensionValues:
    out: ExpressionDimensionValues = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_budgets.types.dimension

        out["key"] = aws_sdk_budgets.types.dimension.deserialize_aws_json_1_1(
            data["Key"]
        )
    else:
        raise DeserializationError("ExpressionDimensionValues.key required")
    if "Values" in data:
        import aws_sdk_budgets.types.values

        out["values"] = aws_sdk_budgets.types.values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        raise DeserializationError("ExpressionDimensionValues.values required")
    if "MatchOptions" in data:
        import aws_sdk_budgets.types.match_options

        out["match_options"] = (
            aws_sdk_budgets.types.match_options.deserialize_aws_json_1_1(
                data["MatchOptions"]
            )
        )
    return out
