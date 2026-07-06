"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.expression
    import aws_sdk_bcm_pricing_calculator.types.expression_filter
    import aws_sdk_bcm_pricing_calculator.types.expression_list

Expression = TypedDict(
    "Expression",
    {
        "and": NotRequired[
            "aws_sdk_bcm_pricing_calculator.types.expression_list.ExpressionList"
        ],
        "or": NotRequired[
            "aws_sdk_bcm_pricing_calculator.types.expression_list.ExpressionList"
        ],
        "not": NotRequired[
            "aws_sdk_bcm_pricing_calculator.types.expression.Expression"
        ],
        "cost_categories": NotRequired[
            "aws_sdk_bcm_pricing_calculator.types.expression_filter.ExpressionFilter"
        ],
        "dimensions": NotRequired[
            "aws_sdk_bcm_pricing_calculator.types.expression_filter.ExpressionFilter"
        ],
        "tags": NotRequired[
            "aws_sdk_bcm_pricing_calculator.types.expression_filter.ExpressionFilter"
        ],
    },
    closed=True,
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Expression) -> dict:
    out: dict = {}
    if "and" in value:
        import aws_sdk_bcm_pricing_calculator.types.expression_list

        out["and"] = (
            aws_sdk_bcm_pricing_calculator.types.expression_list.serialize_aws_json_1_0(
                value["and"]
            )
        )
    if "or" in value:
        import aws_sdk_bcm_pricing_calculator.types.expression_list

        out["or"] = (
            aws_sdk_bcm_pricing_calculator.types.expression_list.serialize_aws_json_1_0(
                value["or"]
            )
        )
    if "not" in value:
        import aws_sdk_bcm_pricing_calculator.types.expression

        out["not"] = (
            aws_sdk_bcm_pricing_calculator.types.expression.serialize_aws_json_1_0(
                value["not"]
            )
        )
    if "cost_categories" in value:
        import aws_sdk_bcm_pricing_calculator.types.expression_filter

        out["costCategories"] = (
            aws_sdk_bcm_pricing_calculator.types.expression_filter.serialize_aws_json_1_0(
                value["cost_categories"]
            )
        )
    if "dimensions" in value:
        import aws_sdk_bcm_pricing_calculator.types.expression_filter

        out["dimensions"] = (
            aws_sdk_bcm_pricing_calculator.types.expression_filter.serialize_aws_json_1_0(
                value["dimensions"]
            )
        )
    if "tags" in value:
        import aws_sdk_bcm_pricing_calculator.types.expression_filter

        out["tags"] = (
            aws_sdk_bcm_pricing_calculator.types.expression_filter.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    if "and" in data:
        import aws_sdk_bcm_pricing_calculator.types.expression_list

        out["and"] = (
            aws_sdk_bcm_pricing_calculator.types.expression_list.deserialize_aws_json_1_0(
                data["and"]
            )
        )
    if "or" in data:
        import aws_sdk_bcm_pricing_calculator.types.expression_list

        out["or"] = (
            aws_sdk_bcm_pricing_calculator.types.expression_list.deserialize_aws_json_1_0(
                data["or"]
            )
        )
    if "not" in data:
        import aws_sdk_bcm_pricing_calculator.types.expression

        out["not"] = (
            aws_sdk_bcm_pricing_calculator.types.expression.deserialize_aws_json_1_0(
                data["not"]
            )
        )
    if "costCategories" in data:
        import aws_sdk_bcm_pricing_calculator.types.expression_filter

        out["cost_categories"] = (
            aws_sdk_bcm_pricing_calculator.types.expression_filter.deserialize_aws_json_1_0(
                data["costCategories"]
            )
        )
    if "dimensions" in data:
        import aws_sdk_bcm_pricing_calculator.types.expression_filter

        out["dimensions"] = (
            aws_sdk_bcm_pricing_calculator.types.expression_filter.deserialize_aws_json_1_0(
                data["dimensions"]
            )
        )
    if "tags" in data:
        import aws_sdk_bcm_pricing_calculator.types.expression_filter

        out["tags"] = (
            aws_sdk_bcm_pricing_calculator.types.expression_filter.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
