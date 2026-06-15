"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cross_account_filter_option
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.resource_property_name
    import aws_sdk_sagemaker.types.resource_type
    import aws_sdk_sagemaker.types.search_expression
    import aws_sdk_sagemaker.types.search_sort_order
    import aws_sdk_sagemaker.types.visibility_conditions_list


class SearchRequest(TypedDict):
    resource: NotRequired["aws_sdk_sagemaker.types.resource_type.ResourceType"]
    """<p>The name of the SageMaker resource to search for.</p>"""
    search_expression: NotRequired[
        "aws_sdk_sagemaker.types.search_expression.SearchExpression"
    ]
    """<p>A Boolean conditional statement. Resources must satisfy this condition to be included in search results. You must provide at least one subexpression, filter, or nested filter. The maximum number of recursive <code>SubExpressions</code>, <code>NestedFilters</code>, and <code>Filters</code> that can be included in a <code>SearchExpression</code> object is 50.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.resource_property_name.ResourcePropertyName"
    ]
    """<p>The name of the resource property used to sort the <code>SearchResults</code>. The default is <code>LastModifiedTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.search_sort_order.SearchSortOrder"]
    """<p>How <code>SearchResults</code> are ordered. Valid values are <code>Ascending</code> or <code>Descending</code>. The default is <code>Descending</code>.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If more than <code>MaxResults</code> resources match the specified <code>SearchExpression</code>, the response includes a <code>NextToken</code>. The <code>NextToken</code> can be passed to the next <code>SearchRequest</code> to continue retrieving results.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    cross_account_filter_option: NotRequired[
        "aws_sdk_sagemaker.types.cross_account_filter_option.CrossAccountFilterOption"
    ]
    r"""<p> A cross account filter option. When the value is <code>\"CrossAccount\"</code> the search results will only include resources made discoverable to you from other accounts. When the value is <code>\"SameAccount\"</code> or <code>null</code> the search results will only include resources from your account. Default is <code>null</code>. For more information on searching for resources made discoverable to your account, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-discoverability-use.html\"> Search discoverable resources</a> in the SageMaker Developer Guide. The maximum number of <code>ResourceCatalog</code>s viewable is 1000. </p>"""
    visibility_conditions: NotRequired[
        "aws_sdk_sagemaker.types.visibility_conditions_list.VisibilityConditionsList"
    ]
    """<p> Limits the results of your search request to the resources that you can access. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchRequest) -> dict:
    out: dict = {}
    if "resource" in value:
        import aws_sdk_sagemaker.types.resource_type

        out["Resource"] = aws_sdk_sagemaker.types.resource_type.serialize_aws_json_1_1(
            value["resource"]
        )
    if "search_expression" in value:
        import aws_sdk_sagemaker.types.search_expression

        out["SearchExpression"] = (
            aws_sdk_sagemaker.types.search_expression.serialize_aws_json_1_1(
                value["search_expression"]
            )
        )
    if "sort_by" in value:
        out["SortBy"] = value["sort_by"]
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.search_sort_order

        out["SortOrder"] = (
            aws_sdk_sagemaker.types.search_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "cross_account_filter_option" in value:
        import aws_sdk_sagemaker.types.cross_account_filter_option

        out["CrossAccountFilterOption"] = (
            aws_sdk_sagemaker.types.cross_account_filter_option.serialize_aws_json_1_1(
                value["cross_account_filter_option"]
            )
        )
    if "visibility_conditions" in value:
        import aws_sdk_sagemaker.types.visibility_conditions_list

        out["VisibilityConditions"] = (
            aws_sdk_sagemaker.types.visibility_conditions_list.serialize_aws_json_1_1(
                value["visibility_conditions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchRequest:
    out: SearchRequest = {}  # type: ignore[typeddict-item]
    if "Resource" in data:
        import aws_sdk_sagemaker.types.resource_type

        out["resource"] = (
            aws_sdk_sagemaker.types.resource_type.deserialize_aws_json_1_1(
                data["Resource"]
            )
        )
    if "SearchExpression" in data:
        import aws_sdk_sagemaker.types.search_expression

        out["search_expression"] = (
            aws_sdk_sagemaker.types.search_expression.deserialize_aws_json_1_1(
                data["SearchExpression"]
            )
        )
    if "SortBy" in data:
        out["sort_by"] = data["SortBy"]
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.search_sort_order

        out["sort_order"] = (
            aws_sdk_sagemaker.types.search_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "CrossAccountFilterOption" in data:
        import aws_sdk_sagemaker.types.cross_account_filter_option

        out["cross_account_filter_option"] = (
            aws_sdk_sagemaker.types.cross_account_filter_option.deserialize_aws_json_1_1(
                data["CrossAccountFilterOption"]
            )
        )
    if "VisibilityConditions" in data:
        import aws_sdk_sagemaker.types.visibility_conditions_list

        out["visibility_conditions"] = (
            aws_sdk_sagemaker.types.visibility_conditions_list.deserialize_aws_json_1_1(
                data["VisibilityConditions"]
            )
        )
    return out
