"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostAndUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.dimension_values_with_attributes_list
    import capo_cost_explorer.types.group_definitions
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.results_by_time


class GetCostAndUsageResponse(TypedDict, closed=True):
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token for the next set of retrievable results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""
    group_definitions: NotRequired[
        "capo_cost_explorer.types.group_definitions.GroupDefinitions"
    ]
    """<p>The groups that are specified by the <code>Filter</code> or <code>GroupBy</code> parameters in the request.</p>"""
    results_by_time: NotRequired[
        "capo_cost_explorer.types.results_by_time.ResultsByTime"
    ]
    """<p>The time period that's covered by the results in the response.</p>"""
    dimension_value_attributes: NotRequired[
        "capo_cost_explorer.types.dimension_values_with_attributes_list.DimensionValuesWithAttributesList"
    ]
    """<p>The attributes that apply to a specific dimension value. For example, if the value is a linked account, the attribute is that account name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostAndUsageResponse) -> dict:
    out: dict = {}
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "group_definitions" in value:
        import capo_cost_explorer.types.group_definitions

        out["GroupDefinitions"] = (
            capo_cost_explorer.types.group_definitions.serialize_aws_json_1_1(
                value["group_definitions"]
            )
        )
    if "results_by_time" in value:
        import capo_cost_explorer.types.results_by_time

        out["ResultsByTime"] = (
            capo_cost_explorer.types.results_by_time.serialize_aws_json_1_1(
                value["results_by_time"]
            )
        )
    if "dimension_value_attributes" in value:
        import capo_cost_explorer.types.dimension_values_with_attributes_list

        out["DimensionValueAttributes"] = (
            capo_cost_explorer.types.dimension_values_with_attributes_list.serialize_aws_json_1_1(
                value["dimension_value_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostAndUsageResponse:
    out: GetCostAndUsageResponse = {}  # type: ignore[typeddict-item]
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    if "GroupDefinitions" in data:
        import capo_cost_explorer.types.group_definitions

        out["group_definitions"] = (
            capo_cost_explorer.types.group_definitions.deserialize_aws_json_1_1(
                data["GroupDefinitions"]
            )
        )
    if "ResultsByTime" in data:
        import capo_cost_explorer.types.results_by_time

        out["results_by_time"] = (
            capo_cost_explorer.types.results_by_time.deserialize_aws_json_1_1(
                data["ResultsByTime"]
            )
        )
    if "DimensionValueAttributes" in data:
        import capo_cost_explorer.types.dimension_values_with_attributes_list

        out["dimension_value_attributes"] = (
            capo_cost_explorer.types.dimension_values_with_attributes_list.deserialize_aws_json_1_1(
                data["DimensionValueAttributes"]
            )
        )
    return out
