"""Generated from Smithy shape ``com.amazonaws.billing#ListBillingViewsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billing.types.account_id
    import aws_sdk_billing.types.active_time_range
    import aws_sdk_billing.types.billing_view_arn_list
    import aws_sdk_billing.types.billing_view_type_list
    import aws_sdk_billing.types.billing_views_max_results
    import aws_sdk_billing.types.page_token
    import aws_sdk_billing.types.string_searches


class ListBillingViewsRequest(TypedDict, closed=True):
    active_time_range: NotRequired[
        "aws_sdk_billing.types.active_time_range.ActiveTimeRange"
    ]
    """<p> The time range for the billing views listed. <code>PRIMARY</code> billing view is always listed. <code>BILLING_GROUP</code> billing views are listed for time ranges when the associated billing group resource in Billing Conductor is active. The time range must be within one calendar month. </p>"""
    arns: NotRequired["aws_sdk_billing.types.billing_view_arn_list.BillingViewArnList"]
    """<p>The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""
    billing_view_types: NotRequired[
        "aws_sdk_billing.types.billing_view_type_list.BillingViewTypeList"
    ]
    """<p>The type of billing view.</p>"""
    names: NotRequired["aws_sdk_billing.types.string_searches.StringSearches"]
    """<p> Filters the list of billing views by name. You can specify search criteria to match billing view names based on the search option provided. </p>"""
    owner_account_id: NotRequired["aws_sdk_billing.types.account_id.AccountId"]
    """<p> The list of owners of the billing view. </p>"""
    source_account_id: NotRequired["aws_sdk_billing.types.account_id.AccountId"]
    """<p> Filters the results to include only billing views that use the specified account as a source. </p>"""
    max_results: NotRequired[
        "aws_sdk_billing.types.billing_views_max_results.BillingViewsMaxResults"
    ]
    """<p>The maximum number of billing views to retrieve. Default is 100. </p>"""
    next_token: NotRequired["aws_sdk_billing.types.page_token.PageToken"]
    """<p>The pagination token that is used on subsequent calls to list billing views.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillingViewsRequest) -> dict:
    out: dict = {}
    if "active_time_range" in value:
        import aws_sdk_billing.types.active_time_range

        out["activeTimeRange"] = (
            aws_sdk_billing.types.active_time_range.serialize_aws_json_1_0(
                value["active_time_range"]
            )
        )
    if "arns" in value:
        import aws_sdk_billing.types.billing_view_arn_list

        out["arns"] = (
            aws_sdk_billing.types.billing_view_arn_list.serialize_aws_json_1_0(
                value["arns"]
            )
        )
    if "billing_view_types" in value:
        import aws_sdk_billing.types.billing_view_type_list

        out["billingViewTypes"] = (
            aws_sdk_billing.types.billing_view_type_list.serialize_aws_json_1_0(
                value["billing_view_types"]
            )
        )
    if "names" in value:
        import aws_sdk_billing.types.string_searches

        out["names"] = aws_sdk_billing.types.string_searches.serialize_aws_json_1_0(
            value["names"]
        )
    if "owner_account_id" in value:
        out["ownerAccountId"] = value["owner_account_id"]
    if "source_account_id" in value:
        out["sourceAccountId"] = value["source_account_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillingViewsRequest:
    out: ListBillingViewsRequest = {}  # type: ignore[typeddict-item]
    if "activeTimeRange" in data:
        import aws_sdk_billing.types.active_time_range

        out["active_time_range"] = (
            aws_sdk_billing.types.active_time_range.deserialize_aws_json_1_0(
                data["activeTimeRange"]
            )
        )
    if "arns" in data:
        import aws_sdk_billing.types.billing_view_arn_list

        out["arns"] = (
            aws_sdk_billing.types.billing_view_arn_list.deserialize_aws_json_1_0(
                data["arns"]
            )
        )
    if "billingViewTypes" in data:
        import aws_sdk_billing.types.billing_view_type_list

        out["billing_view_types"] = (
            aws_sdk_billing.types.billing_view_type_list.deserialize_aws_json_1_0(
                data["billingViewTypes"]
            )
        )
    if "names" in data:
        import aws_sdk_billing.types.string_searches

        out["names"] = aws_sdk_billing.types.string_searches.deserialize_aws_json_1_0(
            data["names"]
        )
    if "ownerAccountId" in data:
        out["owner_account_id"] = data["ownerAccountId"]
    if "sourceAccountId" in data:
        out["source_account_id"] = data["sourceAccountId"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
