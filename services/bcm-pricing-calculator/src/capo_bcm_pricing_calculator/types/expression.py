"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.expression
    import capo_bcm_pricing_calculator.types.expression_filter
    import capo_bcm_pricing_calculator.types.expression_list

Expression = TypedDict(
    "Expression",
    {
        "and": NotRequired[
            "capo_bcm_pricing_calculator.types.expression_list.ExpressionList"
        ],
        "or": NotRequired[
            "capo_bcm_pricing_calculator.types.expression_list.ExpressionList"
        ],
        "not": NotRequired["capo_bcm_pricing_calculator.types.expression.Expression"],
        "cost_categories": NotRequired[
            "capo_bcm_pricing_calculator.types.expression_filter.ExpressionFilter"
        ],
        "dimensions": NotRequired[
            "capo_bcm_pricing_calculator.types.expression_filter.ExpressionFilter"
        ],
        "tags": NotRequired[
            "capo_bcm_pricing_calculator.types.expression_filter.ExpressionFilter"
        ],
    },
    closed=True,
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Expression) -> dict:
    out: dict = {}
    if "and" in value:
        import capo_bcm_pricing_calculator.types.expression_list

        out["and"] = (
            capo_bcm_pricing_calculator.types.expression_list.serialize_aws_json_1_0(
                value["and"]
            )
        )
    if "or" in value:
        import capo_bcm_pricing_calculator.types.expression_list

        out["or"] = (
            capo_bcm_pricing_calculator.types.expression_list.serialize_aws_json_1_0(
                value["or"]
            )
        )
    if "not" in value:
        import capo_bcm_pricing_calculator.types.expression

        out["not"] = (
            capo_bcm_pricing_calculator.types.expression.serialize_aws_json_1_0(
                value["not"]
            )
        )
    if "cost_categories" in value:
        import capo_bcm_pricing_calculator.types.expression_filter

        out["costCategories"] = (
            capo_bcm_pricing_calculator.types.expression_filter.serialize_aws_json_1_0(
                value["cost_categories"]
            )
        )
    if "dimensions" in value:
        import capo_bcm_pricing_calculator.types.expression_filter

        out["dimensions"] = (
            capo_bcm_pricing_calculator.types.expression_filter.serialize_aws_json_1_0(
                value["dimensions"]
            )
        )
    if "tags" in value:
        import capo_bcm_pricing_calculator.types.expression_filter

        out["tags"] = (
            capo_bcm_pricing_calculator.types.expression_filter.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    if "and" in data:
        import capo_bcm_pricing_calculator.types.expression_list

        out["and"] = (
            capo_bcm_pricing_calculator.types.expression_list.deserialize_aws_json_1_0(
                data["and"]
            )
        )
    if "or" in data:
        import capo_bcm_pricing_calculator.types.expression_list

        out["or"] = (
            capo_bcm_pricing_calculator.types.expression_list.deserialize_aws_json_1_0(
                data["or"]
            )
        )
    if "not" in data:
        import capo_bcm_pricing_calculator.types.expression

        out["not"] = (
            capo_bcm_pricing_calculator.types.expression.deserialize_aws_json_1_0(
                data["not"]
            )
        )
    if "costCategories" in data:
        import capo_bcm_pricing_calculator.types.expression_filter

        out["cost_categories"] = (
            capo_bcm_pricing_calculator.types.expression_filter.deserialize_aws_json_1_0(
                data["costCategories"]
            )
        )
    if "dimensions" in data:
        import capo_bcm_pricing_calculator.types.expression_filter

        out["dimensions"] = (
            capo_bcm_pricing_calculator.types.expression_filter.deserialize_aws_json_1_0(
                data["dimensions"]
            )
        )
    if "tags" in data:
        import capo_bcm_pricing_calculator.types.expression_filter

        out["tags"] = (
            capo_bcm_pricing_calculator.types.expression_filter.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
