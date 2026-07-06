"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#Promotion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.arn
    import aws_sdk_personalize_runtime.types.filter_values
    import aws_sdk_personalize_runtime.types.name
    import aws_sdk_personalize_runtime.types.percent_promoted_items


class Promotion(TypedDict, closed=True):
    name: NotRequired["aws_sdk_personalize_runtime.types.name.Name"]
    """<p>The name of the promotion.</p>"""
    percent_promoted_items: NotRequired[
        "aws_sdk_personalize_runtime.types.percent_promoted_items.PercentPromotedItems"
    ]
    """<p>The percentage of recommended items to apply the promotion to.</p>"""
    filter_arn: NotRequired["aws_sdk_personalize_runtime.types.arn.Arn"]
    r"""<p>The Amazon Resource Name (ARN) of the filter used by the promotion. This filter defines the criteria for promoted items. For more information, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/promoting-items.html#promotion-filters\">Promotion filters</a>.</p>"""
    filter_values: NotRequired[
        "aws_sdk_personalize_runtime.types.filter_values.FilterValues"
    ]
    r"""<p>The values to use when promoting items. For each placeholder parameter in your promotion's filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma. </p> <p>For filter expressions that use an <code>INCLUDE</code> element to include items, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an <code>EXCLUDE</code> element to exclude items, you can omit the <code>filter-values</code>. In this case, Amazon Personalize doesn't use that portion of the expression to filter recommendations.</p> <p>For more information on creating filters, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/filter.html\">Filtering recommendations and user segments</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Promotion) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "percent_promoted_items" in value:
        out["percentPromotedItems"] = value["percent_promoted_items"]
    if "filter_arn" in value:
        out["filterArn"] = value["filter_arn"]
    if "filter_values" in value:
        import aws_sdk_personalize_runtime.types.filter_values

        out["filterValues"] = (
            aws_sdk_personalize_runtime.types.filter_values.serialize_json(
                value["filter_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> Promotion:
    out: Promotion = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "percentPromotedItems" in data:
        out["percent_promoted_items"] = data["percentPromotedItems"]
    if "filterArn" in data:
        out["filter_arn"] = data["filterArn"]
    if "filterValues" in data:
        import aws_sdk_personalize_runtime.types.filter_values

        out["filter_values"] = (
            aws_sdk_personalize_runtime.types.filter_values.deserialize_json(
                data["filterValues"]
            )
        )
    return out
