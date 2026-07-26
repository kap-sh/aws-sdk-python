"""Generated from Smithy shape ``com.amazonaws.billing#Expression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.cost_category_values
    import capo_billing.types.dimension_values
    import capo_billing.types.tag_values
    import capo_billing.types.time_range


class Expression(TypedDict, closed=True):
    dimensions: NotRequired["capo_billing.types.dimension_values.DimensionValues"]
    """<p> The specific <code>Dimension</code> to use for <code>Expression</code>. </p>"""
    tags: NotRequired["capo_billing.types.tag_values.TagValues"]
    """<p> The specific <code>Tag</code> to use for <code>Expression</code>. </p>"""
    cost_categories: NotRequired[
        "capo_billing.types.cost_category_values.CostCategoryValues"
    ]
    """<p> The filter that's based on <code>CostCategory</code> values. </p>"""
    time_range: NotRequired["capo_billing.types.time_range.TimeRange"]
    """<p> Specifies a time range filter for the billing view data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Expression) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_billing.types.dimension_values

        out["dimensions"] = capo_billing.types.dimension_values.serialize_aws_json_1_0(
            value["dimensions"]
        )
    if "tags" in value:
        import capo_billing.types.tag_values

        out["tags"] = capo_billing.types.tag_values.serialize_aws_json_1_0(
            value["tags"]
        )
    if "cost_categories" in value:
        import capo_billing.types.cost_category_values

        out["costCategories"] = (
            capo_billing.types.cost_category_values.serialize_aws_json_1_0(
                value["cost_categories"]
            )
        )
    if "time_range" in value:
        import capo_billing.types.time_range

        out["timeRange"] = capo_billing.types.time_range.serialize_aws_json_1_0(
            value["time_range"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Expression:
    out: Expression = {}  # type: ignore[typeddict-item]
    if "dimensions" in data:
        import capo_billing.types.dimension_values

        out["dimensions"] = (
            capo_billing.types.dimension_values.deserialize_aws_json_1_0(
                data["dimensions"]
            )
        )
    if "tags" in data:
        import capo_billing.types.tag_values

        out["tags"] = capo_billing.types.tag_values.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "costCategories" in data:
        import capo_billing.types.cost_category_values

        out["cost_categories"] = (
            capo_billing.types.cost_category_values.deserialize_aws_json_1_0(
                data["costCategories"]
            )
        )
    if "timeRange" in data:
        import capo_billing.types.time_range

        out["time_range"] = capo_billing.types.time_range.deserialize_aws_json_1_0(
            data["timeRange"]
        )
    return out
