"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListOpportunitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.created_date_filter
    import aws_sdk_partnercentral_selling.types.filter_identifier
    import aws_sdk_partnercentral_selling.types.filter_life_cycle_review_status
    import aws_sdk_partnercentral_selling.types.filter_life_cycle_stage
    import aws_sdk_partnercentral_selling.types.last_modified_date
    import aws_sdk_partnercentral_selling.types.opportunity_sort
    import aws_sdk_partnercentral_selling.types.page_size
    import aws_sdk_partnercentral_selling.types.string_list
    import aws_sdk_partnercentral_selling.types.target_close_date_filter


class ListOpportunitiesRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunities are listed in. Use <code>AWS</code> for listing real opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>"""
    max_results: NotRequired["aws_sdk_partnercentral_selling.types.page_size.PageSize"]
    """<p>Specifies the maximum number of results to return in a single call. This limits the number of opportunities returned in the response to avoid providing too many results at once.</p> <p>Default: 20</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>"""
    sort: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_sort.OpportunitySort"
    ]
    """<p>An object that specifies how the response is sorted. The default <code>Sort.SortBy</code> value is <code>LastModifiedDate</code>.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.last_modified_date.LastModifiedDate"
    ]
    """<p>Filters the opportunities based on their last modified date. This filter helps retrieve opportunities that were updated after the specified date, allowing partners to track recent changes or updates.</p>"""
    identifier: NotRequired[
        "aws_sdk_partnercentral_selling.types.filter_identifier.FilterIdentifier"
    ]
    """<p>Filters the opportunities based on the opportunity identifier. This allows partners to retrieve specific opportunities by providing their unique identifiers, ensuring precise results.</p>"""
    life_cycle_stage: NotRequired[
        "aws_sdk_partnercentral_selling.types.filter_life_cycle_stage.FilterLifeCycleStage"
    ]
    """<p>Filters the opportunities based on their lifecycle stage. This filter allows partners to retrieve opportunities at various stages in the sales cycle, such as <code>Qualified</code>, <code>Technical Validation</code>, <code>Business Validation</code>, or <code>Closed Won</code>.</p>"""
    life_cycle_review_status: NotRequired[
        "aws_sdk_partnercentral_selling.types.filter_life_cycle_review_status.FilterLifeCycleReviewStatus"
    ]
    """<p>Filters the opportunities based on their current lifecycle approval status. Use this filter to retrieve opportunities with statuses such as <code>Pending Submission</code>, <code>In Review</code>, <code>Action Required</code>, or <code>Approved</code>.</p>"""
    customer_company_name: NotRequired[
        "aws_sdk_partnercentral_selling.types.string_list.StringList"
    ]
    """<p>Filters the opportunities based on the customer's company name. This allows partners to search for opportunities associated with a specific customer by matching the provided company name string.</p>"""
    created_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.created_date_filter.CreatedDateFilter"
    ]
    """<p>Filter opportunities by creation date criteria.</p>"""
    target_close_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.target_close_date_filter.TargetCloseDateFilter"
    ]
    """<p>Filters opportunities based on their target close date. This filter helps retrieve opportunities with an expected close date before or after a specified date.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOpportunitiesRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort" in value:
        import aws_sdk_partnercentral_selling.types.opportunity_sort

        out["Sort"] = (
            aws_sdk_partnercentral_selling.types.opportunity_sort.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    if "last_modified_date" in value:
        import aws_sdk_partnercentral_selling.types.last_modified_date

        out["LastModifiedDate"] = (
            aws_sdk_partnercentral_selling.types.last_modified_date.serialize_aws_json_1_0(
                value["last_modified_date"]
            )
        )
    if "identifier" in value:
        import aws_sdk_partnercentral_selling.types.filter_identifier

        out["Identifier"] = (
            aws_sdk_partnercentral_selling.types.filter_identifier.serialize_aws_json_1_0(
                value["identifier"]
            )
        )
    if "life_cycle_stage" in value:
        import aws_sdk_partnercentral_selling.types.filter_life_cycle_stage

        out["LifeCycleStage"] = (
            aws_sdk_partnercentral_selling.types.filter_life_cycle_stage.serialize_aws_json_1_0(
                value["life_cycle_stage"]
            )
        )
    if "life_cycle_review_status" in value:
        import aws_sdk_partnercentral_selling.types.filter_life_cycle_review_status

        out["LifeCycleReviewStatus"] = (
            aws_sdk_partnercentral_selling.types.filter_life_cycle_review_status.serialize_aws_json_1_0(
                value["life_cycle_review_status"]
            )
        )
    if "customer_company_name" in value:
        import aws_sdk_partnercentral_selling.types.string_list

        out["CustomerCompanyName"] = (
            aws_sdk_partnercentral_selling.types.string_list.serialize_aws_json_1_0(
                value["customer_company_name"]
            )
        )
    if "created_date" in value:
        import aws_sdk_partnercentral_selling.types.created_date_filter

        out["CreatedDate"] = (
            aws_sdk_partnercentral_selling.types.created_date_filter.serialize_aws_json_1_0(
                value["created_date"]
            )
        )
    if "target_close_date" in value:
        import aws_sdk_partnercentral_selling.types.target_close_date_filter

        out["TargetCloseDate"] = (
            aws_sdk_partnercentral_selling.types.target_close_date_filter.serialize_aws_json_1_0(
                value["target_close_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOpportunitiesRequest:
    out: ListOpportunitiesRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListOpportunitiesRequest.catalog required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Sort" in data:
        import aws_sdk_partnercentral_selling.types.opportunity_sort

        out["sort"] = (
            aws_sdk_partnercentral_selling.types.opportunity_sort.deserialize_aws_json_1_0(
                data["Sort"]
            )
        )
    if "LastModifiedDate" in data:
        import aws_sdk_partnercentral_selling.types.last_modified_date

        out["last_modified_date"] = (
            aws_sdk_partnercentral_selling.types.last_modified_date.deserialize_aws_json_1_0(
                data["LastModifiedDate"]
            )
        )
    if "Identifier" in data:
        import aws_sdk_partnercentral_selling.types.filter_identifier

        out["identifier"] = (
            aws_sdk_partnercentral_selling.types.filter_identifier.deserialize_aws_json_1_0(
                data["Identifier"]
            )
        )
    if "LifeCycleStage" in data:
        import aws_sdk_partnercentral_selling.types.filter_life_cycle_stage

        out["life_cycle_stage"] = (
            aws_sdk_partnercentral_selling.types.filter_life_cycle_stage.deserialize_aws_json_1_0(
                data["LifeCycleStage"]
            )
        )
    if "LifeCycleReviewStatus" in data:
        import aws_sdk_partnercentral_selling.types.filter_life_cycle_review_status

        out["life_cycle_review_status"] = (
            aws_sdk_partnercentral_selling.types.filter_life_cycle_review_status.deserialize_aws_json_1_0(
                data["LifeCycleReviewStatus"]
            )
        )
    if "CustomerCompanyName" in data:
        import aws_sdk_partnercentral_selling.types.string_list

        out["customer_company_name"] = (
            aws_sdk_partnercentral_selling.types.string_list.deserialize_aws_json_1_0(
                data["CustomerCompanyName"]
            )
        )
    if "CreatedDate" in data:
        import aws_sdk_partnercentral_selling.types.created_date_filter

        out["created_date"] = (
            aws_sdk_partnercentral_selling.types.created_date_filter.deserialize_aws_json_1_0(
                data["CreatedDate"]
            )
        )
    if "TargetCloseDate" in data:
        import aws_sdk_partnercentral_selling.types.target_close_date_filter

        out["target_close_date"] = (
            aws_sdk_partnercentral_selling.types.target_close_date_filter.deserialize_aws_json_1_0(
                data["TargetCloseDate"]
            )
        )
    return out
