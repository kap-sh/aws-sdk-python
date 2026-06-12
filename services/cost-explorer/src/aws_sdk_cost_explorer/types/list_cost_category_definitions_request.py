"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListCostCategoryDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_max_results
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.resource_types_filter_input
    import aws_sdk_cost_explorer.types.zoned_date_time


class ListCostCategoryDefinitionsRequest(TypedDict):
    effective_on: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The date when the cost category was effective. </p>"""
    next_token: NotRequired["aws_sdk_cost_explorer.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""
    max_results: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_max_results.CostCategoryMaxResults"
    ]
    """<p>The number of entries a paginated response contains. </p>"""
    supported_resource_types: NotRequired[
        "aws_sdk_cost_explorer.types.resource_types_filter_input.ResourceTypesFilterInput"
    ]
    """<p> Filter cost category definitions that are supported by given resource types based on the latest version. If the filter is present, the result only includes Cost Categories that supports input resource type. If the filter isn't provided, no filtering is applied. The valid values are <code>billing:rispgroupsharing</code> and <code>billing:billingview</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCostCategoryDefinitionsRequest) -> dict:
    out: dict = {}
    if "effective_on" in value:
        out["EffectiveOn"] = value["effective_on"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "supported_resource_types" in value:
        import aws_sdk_cost_explorer.types.resource_types_filter_input

        out["SupportedResourceTypes"] = (
            aws_sdk_cost_explorer.types.resource_types_filter_input.serialize_aws_json_1_1(
                value["supported_resource_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCostCategoryDefinitionsRequest:
    out: ListCostCategoryDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if "EffectiveOn" in data:
        out["effective_on"] = data["EffectiveOn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "SupportedResourceTypes" in data:
        import aws_sdk_cost_explorer.types.resource_types_filter_input

        out["supported_resource_types"] = (
            aws_sdk_cost_explorer.types.resource_types_filter_input.deserialize_aws_json_1_1(
                data["SupportedResourceTypes"]
            )
        )
    return out
