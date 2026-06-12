"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#Expression``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.cost_category_values
    import aws_sdk_bcm_dashboards.types.dimension_values
    import aws_sdk_bcm_dashboards.types.expression
    import aws_sdk_bcm_dashboards.types.expressions
    import aws_sdk_bcm_dashboards.types.tag_values

Expression = TypedDict(
    "Expression",
    {
        "or": NotRequired["aws_sdk_bcm_dashboards.types.expressions.Expressions"],
        "and": NotRequired["aws_sdk_bcm_dashboards.types.expressions.Expressions"],
        "not": NotRequired["aws_sdk_bcm_dashboards.types.expression.Expression"],
        "dimensions": NotRequired[
            "aws_sdk_bcm_dashboards.types.dimension_values.DimensionValues"
        ],
        "tags": NotRequired["aws_sdk_bcm_dashboards.types.tag_values.TagValues"],
        "cost_categories": NotRequired[
            "aws_sdk_bcm_dashboards.types.cost_category_values.CostCategoryValues"
        ],
    },
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Expression) -> dict:
    out: dict = {}
    if "or" in value:
        import aws_sdk_bcm_dashboards.types.expressions

        out["or"] = aws_sdk_bcm_dashboards.types.expressions.serialize_aws_json_1_0(
            value["or"]
        )
    if "and" in value:
        import aws_sdk_bcm_dashboards.types.expressions

        out["and"] = aws_sdk_bcm_dashboards.types.expressions.serialize_aws_json_1_0(
            value["and"]
        )
    if "not" in value:
        import aws_sdk_bcm_dashboards.types.expression

        out["not"] = aws_sdk_bcm_dashboards.types.expression.serialize_aws_json_1_0(
            value["not"]
        )
    if "dimensions" in value:
        import aws_sdk_bcm_dashboards.types.dimension_values

        out["dimensions"] = (
            aws_sdk_bcm_dashboards.types.dimension_values.serialize_aws_json_1_0(
                value["dimensions"]
            )
        )
    if "tags" in value:
        import aws_sdk_bcm_dashboards.types.tag_values

        out["tags"] = aws_sdk_bcm_dashboards.types.tag_values.serialize_aws_json_1_0(
            value["tags"]
        )
    if "cost_categories" in value:
        import aws_sdk_bcm_dashboards.types.cost_category_values

        out["costCategories"] = (
            aws_sdk_bcm_dashboards.types.cost_category_values.serialize_aws_json_1_0(
                value["cost_categories"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    if "or" in data:
        import aws_sdk_bcm_dashboards.types.expressions

        out["or"] = aws_sdk_bcm_dashboards.types.expressions.deserialize_aws_json_1_0(
            data["or"]
        )
    if "and" in data:
        import aws_sdk_bcm_dashboards.types.expressions

        out["and"] = aws_sdk_bcm_dashboards.types.expressions.deserialize_aws_json_1_0(
            data["and"]
        )
    if "not" in data:
        import aws_sdk_bcm_dashboards.types.expression

        out["not"] = aws_sdk_bcm_dashboards.types.expression.deserialize_aws_json_1_0(
            data["not"]
        )
    if "dimensions" in data:
        import aws_sdk_bcm_dashboards.types.dimension_values

        out["dimensions"] = (
            aws_sdk_bcm_dashboards.types.dimension_values.deserialize_aws_json_1_0(
                data["dimensions"]
            )
        )
    if "tags" in data:
        import aws_sdk_bcm_dashboards.types.tag_values

        out["tags"] = aws_sdk_bcm_dashboards.types.tag_values.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "costCategories" in data:
        import aws_sdk_bcm_dashboards.types.cost_category_values

        out["cost_categories"] = (
            aws_sdk_bcm_dashboards.types.cost_category_values.deserialize_aws_json_1_0(
                data["costCategories"]
            )
        )
    return out
