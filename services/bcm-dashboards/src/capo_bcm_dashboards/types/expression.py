"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.cost_category_values
    import capo_bcm_dashboards.types.dimension_values
    import capo_bcm_dashboards.types.expression
    import capo_bcm_dashboards.types.expressions
    import capo_bcm_dashboards.types.tag_values

Expression = TypedDict(
    "Expression",
    {
        "or": NotRequired["capo_bcm_dashboards.types.expressions.Expressions"],
        "and": NotRequired["capo_bcm_dashboards.types.expressions.Expressions"],
        "not": NotRequired["capo_bcm_dashboards.types.expression.Expression"],
        "dimensions": NotRequired[
            "capo_bcm_dashboards.types.dimension_values.DimensionValues"
        ],
        "tags": NotRequired["capo_bcm_dashboards.types.tag_values.TagValues"],
        "cost_categories": NotRequired[
            "capo_bcm_dashboards.types.cost_category_values.CostCategoryValues"
        ],
    },
    closed=True,
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Expression) -> dict:
    out: dict = {}
    if "or" in value:
        import capo_bcm_dashboards.types.expressions

        out["or"] = capo_bcm_dashboards.types.expressions.serialize_aws_json_1_0(
            value["or"]
        )
    if "and" in value:
        import capo_bcm_dashboards.types.expressions

        out["and"] = capo_bcm_dashboards.types.expressions.serialize_aws_json_1_0(
            value["and"]
        )
    if "not" in value:
        import capo_bcm_dashboards.types.expression

        out["not"] = capo_bcm_dashboards.types.expression.serialize_aws_json_1_0(
            value["not"]
        )
    if "dimensions" in value:
        import capo_bcm_dashboards.types.dimension_values

        out["dimensions"] = (
            capo_bcm_dashboards.types.dimension_values.serialize_aws_json_1_0(
                value["dimensions"]
            )
        )
    if "tags" in value:
        import capo_bcm_dashboards.types.tag_values

        out["tags"] = capo_bcm_dashboards.types.tag_values.serialize_aws_json_1_0(
            value["tags"]
        )
    if "cost_categories" in value:
        import capo_bcm_dashboards.types.cost_category_values

        out["costCategories"] = (
            capo_bcm_dashboards.types.cost_category_values.serialize_aws_json_1_0(
                value["cost_categories"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    if "or" in data:
        import capo_bcm_dashboards.types.expressions

        out["or"] = capo_bcm_dashboards.types.expressions.deserialize_aws_json_1_0(
            data["or"]
        )
    if "and" in data:
        import capo_bcm_dashboards.types.expressions

        out["and"] = capo_bcm_dashboards.types.expressions.deserialize_aws_json_1_0(
            data["and"]
        )
    if "not" in data:
        import capo_bcm_dashboards.types.expression

        out["not"] = capo_bcm_dashboards.types.expression.deserialize_aws_json_1_0(
            data["not"]
        )
    if "dimensions" in data:
        import capo_bcm_dashboards.types.dimension_values

        out["dimensions"] = (
            capo_bcm_dashboards.types.dimension_values.deserialize_aws_json_1_0(
                data["dimensions"]
            )
        )
    if "tags" in data:
        import capo_bcm_dashboards.types.tag_values

        out["tags"] = capo_bcm_dashboards.types.tag_values.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "costCategories" in data:
        import capo_bcm_dashboards.types.cost_category_values

        out["cost_categories"] = (
            capo_bcm_dashboards.types.cost_category_values.deserialize_aws_json_1_0(
                data["costCategories"]
            )
        )
    return out
