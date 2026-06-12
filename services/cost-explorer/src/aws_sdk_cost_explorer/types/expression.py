"""Generated from Smithy shape ``com.amazonaws.costexplorer#Expression``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_values
    import aws_sdk_cost_explorer.types.dimension_values
    import aws_sdk_cost_explorer.types.expression
    import aws_sdk_cost_explorer.types.expressions
    import aws_sdk_cost_explorer.types.tag_values

Expression = TypedDict(
    "Expression",
    {
        "or": NotRequired["aws_sdk_cost_explorer.types.expressions.Expressions"],
        "and": NotRequired["aws_sdk_cost_explorer.types.expressions.Expressions"],
        "not": NotRequired["aws_sdk_cost_explorer.types.expression.Expression"],
        "dimensions": NotRequired[
            "aws_sdk_cost_explorer.types.dimension_values.DimensionValues"
        ],
        "tags": NotRequired["aws_sdk_cost_explorer.types.tag_values.TagValues"],
        "cost_categories": NotRequired[
            "aws_sdk_cost_explorer.types.cost_category_values.CostCategoryValues"
        ],
    },
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Expression) -> dict:
    out: dict = {}
    if "or" in value:
        import aws_sdk_cost_explorer.types.expressions

        out["Or"] = aws_sdk_cost_explorer.types.expressions.serialize_aws_json_1_1(
            value["or"]
        )
    if "and" in value:
        import aws_sdk_cost_explorer.types.expressions

        out["And"] = aws_sdk_cost_explorer.types.expressions.serialize_aws_json_1_1(
            value["and"]
        )
    if "not" in value:
        import aws_sdk_cost_explorer.types.expression

        out["Not"] = aws_sdk_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["not"]
        )
    if "dimensions" in value:
        import aws_sdk_cost_explorer.types.dimension_values

        out["Dimensions"] = (
            aws_sdk_cost_explorer.types.dimension_values.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "tags" in value:
        import aws_sdk_cost_explorer.types.tag_values

        out["Tags"] = aws_sdk_cost_explorer.types.tag_values.serialize_aws_json_1_1(
            value["tags"]
        )
    if "cost_categories" in value:
        import aws_sdk_cost_explorer.types.cost_category_values

        out["CostCategories"] = (
            aws_sdk_cost_explorer.types.cost_category_values.serialize_aws_json_1_1(
                value["cost_categories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    if "Or" in data:
        import aws_sdk_cost_explorer.types.expressions

        out["or"] = aws_sdk_cost_explorer.types.expressions.deserialize_aws_json_1_1(
            data["Or"]
        )
    if "And" in data:
        import aws_sdk_cost_explorer.types.expressions

        out["and"] = aws_sdk_cost_explorer.types.expressions.deserialize_aws_json_1_1(
            data["And"]
        )
    if "Not" in data:
        import aws_sdk_cost_explorer.types.expression

        out["not"] = aws_sdk_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Not"]
        )
    if "Dimensions" in data:
        import aws_sdk_cost_explorer.types.dimension_values

        out["dimensions"] = (
            aws_sdk_cost_explorer.types.dimension_values.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_cost_explorer.types.tag_values

        out["tags"] = aws_sdk_cost_explorer.types.tag_values.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "CostCategories" in data:
        import aws_sdk_cost_explorer.types.cost_category_values

        out["cost_categories"] = (
            aws_sdk_cost_explorer.types.cost_category_values.deserialize_aws_json_1_1(
                data["CostCategories"]
            )
        )
    return out
