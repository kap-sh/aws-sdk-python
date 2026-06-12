"""Generated from Smithy shape ``com.amazonaws.costexplorer#DimensionValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.dimension
    import aws_sdk_cost_explorer.types.match_options
    import aws_sdk_cost_explorer.types.values


class DimensionValues(TypedDict):
    key: NotRequired["aws_sdk_cost_explorer.types.dimension.Dimension"]
    """<p>The names of the metadata types that you can use to filter and group your results. For example, <code>AZ</code> returns a list of Availability Zones.</p> <p>Not all dimensions are supported in each API. Refer to the documentation for each specific API to see what is supported.</p> <p> <code>LINKED_ACCOUNT_NAME</code> and <code>SERVICE_CODE</code> can only be used in <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html\">CostCategoryRule</a>.</p> <p> <code>ANOMALY_TOTAL_IMPACT_ABSOLUTE</code> and <code>ANOMALY_TOTAL_IMPACT_PERCENTAGE</code> can only be used in <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html\">AnomalySubscriptions</a>.</p>"""
    values: NotRequired["aws_sdk_cost_explorer.types.values.Values"]
    """<p>The metadata values that you can use to filter and group your results. You can use <code>GetDimensionValues</code> to find specific values.</p>"""
    match_options: NotRequired["aws_sdk_cost_explorer.types.match_options.MatchOptions"]
    """<p>The match options that you can use to filter your results.</p> <p> <code>MatchOptions</code> is only applicable for actions related to cost category and Anomaly Subscriptions. Refer to the documentation for each specific API to see what is supported.</p> <p>The default values for <code>MatchOptions</code> are <code>EQUALS</code> and <code>CASE_SENSITIVE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionValues) -> dict:
    out: dict = {}
    if "key" in value:
        import aws_sdk_cost_explorer.types.dimension

        out["Key"] = aws_sdk_cost_explorer.types.dimension.serialize_aws_json_1_1(
            value["key"]
        )
    if "values" in value:
        import aws_sdk_cost_explorer.types.values

        out["Values"] = aws_sdk_cost_explorer.types.values.serialize_aws_json_1_1(
            value["values"]
        )
    if "match_options" in value:
        import aws_sdk_cost_explorer.types.match_options

        out["MatchOptions"] = (
            aws_sdk_cost_explorer.types.match_options.serialize_aws_json_1_1(
                value["match_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DimensionValues:
    out: DimensionValues = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_cost_explorer.types.dimension

        out["key"] = aws_sdk_cost_explorer.types.dimension.deserialize_aws_json_1_1(
            data["Key"]
        )
    if "Values" in data:
        import aws_sdk_cost_explorer.types.values

        out["values"] = aws_sdk_cost_explorer.types.values.deserialize_aws_json_1_1(
            data["Values"]
        )
    if "MatchOptions" in data:
        import aws_sdk_cost_explorer.types.match_options

        out["match_options"] = (
            aws_sdk_cost_explorer.types.match_options.deserialize_aws_json_1_1(
                data["MatchOptions"]
            )
        )
    return out
