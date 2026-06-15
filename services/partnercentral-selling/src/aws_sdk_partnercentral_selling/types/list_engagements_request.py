"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_account_list
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.engagement_context_type_list
    import aws_sdk_partnercentral_selling.types.engagement_identifiers
    import aws_sdk_partnercentral_selling.types.engagement_page_size
    import aws_sdk_partnercentral_selling.types.engagement_sort


class ListEngagementsRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog related to the request. </p>"""
    created_by: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account_list.AwsAccountList"
    ]
    """<p> A list of AWS account IDs. When specified, the response includes engagements created by these accounts. This filter is useful for finding engagements created by specific team members. </p>"""
    exclude_created_by: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account_list.AwsAccountList"
    ]
    """<p>An array of strings representing AWS Account IDs. Use this to exclude engagements created by specific users. </p>"""
    context_types: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
    ]
    r"""<p>Filters engagements to include only those containing the specified context types, such as \"CustomerProject\" or \"Lead\". Use this to find engagements that have specific types of contextual information associated with them.</p>"""
    exclude_context_types: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
    ]
    """<p>Filters engagements to exclude those containing the specified context types. Use this to find engagements that do not have certain types of contextual information, helping to narrow results based on context exclusion criteria.</p>"""
    sort: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_sort.EngagementSort"
    ]
    max_results: (
        "aws_sdk_partnercentral_selling.types.engagement_page_size.EngagementPageSize"
    )
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. This value is returned from a previous call.</p>"""
    engagement_identifier: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
    ]
    """<p>An array of strings representing engagement identifiers to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "created_by" in value:
        import aws_sdk_partnercentral_selling.types.aws_account_list

        out["CreatedBy"] = (
            aws_sdk_partnercentral_selling.types.aws_account_list.serialize_aws_json_1_0(
                value["created_by"]
            )
        )
    if "exclude_created_by" in value:
        import aws_sdk_partnercentral_selling.types.aws_account_list

        out["ExcludeCreatedBy"] = (
            aws_sdk_partnercentral_selling.types.aws_account_list.serialize_aws_json_1_0(
                value["exclude_created_by"]
            )
        )
    if "context_types" in value:
        import aws_sdk_partnercentral_selling.types.engagement_context_type_list

        out["ContextTypes"] = (
            aws_sdk_partnercentral_selling.types.engagement_context_type_list.serialize_aws_json_1_0(
                value["context_types"]
            )
        )
    if "exclude_context_types" in value:
        import aws_sdk_partnercentral_selling.types.engagement_context_type_list

        out["ExcludeContextTypes"] = (
            aws_sdk_partnercentral_selling.types.engagement_context_type_list.serialize_aws_json_1_0(
                value["exclude_context_types"]
            )
        )
    if "sort" in value:
        import aws_sdk_partnercentral_selling.types.engagement_sort

        out["Sort"] = (
            aws_sdk_partnercentral_selling.types.engagement_sort.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    out["MaxResults"] = value.get("max_results", 20)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "engagement_identifier" in value:
        import aws_sdk_partnercentral_selling.types.engagement_identifiers

        out["EngagementIdentifier"] = (
            aws_sdk_partnercentral_selling.types.engagement_identifiers.serialize_aws_json_1_0(
                value["engagement_identifier"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementsRequest:
    out: ListEngagementsRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListEngagementsRequest.catalog required")
    if "CreatedBy" in data:
        import aws_sdk_partnercentral_selling.types.aws_account_list

        out["created_by"] = (
            aws_sdk_partnercentral_selling.types.aws_account_list.deserialize_aws_json_1_0(
                data["CreatedBy"]
            )
        )
    if "ExcludeCreatedBy" in data:
        import aws_sdk_partnercentral_selling.types.aws_account_list

        out["exclude_created_by"] = (
            aws_sdk_partnercentral_selling.types.aws_account_list.deserialize_aws_json_1_0(
                data["ExcludeCreatedBy"]
            )
        )
    if "ContextTypes" in data:
        import aws_sdk_partnercentral_selling.types.engagement_context_type_list

        out["context_types"] = (
            aws_sdk_partnercentral_selling.types.engagement_context_type_list.deserialize_aws_json_1_0(
                data["ContextTypes"]
            )
        )
    if "ExcludeContextTypes" in data:
        import aws_sdk_partnercentral_selling.types.engagement_context_type_list

        out["exclude_context_types"] = (
            aws_sdk_partnercentral_selling.types.engagement_context_type_list.deserialize_aws_json_1_0(
                data["ExcludeContextTypes"]
            )
        )
    if "Sort" in data:
        import aws_sdk_partnercentral_selling.types.engagement_sort

        out["sort"] = (
            aws_sdk_partnercentral_selling.types.engagement_sort.deserialize_aws_json_1_0(
                data["Sort"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 20
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "EngagementIdentifier" in data:
        import aws_sdk_partnercentral_selling.types.engagement_identifiers

        out["engagement_identifier"] = (
            aws_sdk_partnercentral_selling.types.engagement_identifiers.deserialize_aws_json_1_0(
                data["EngagementIdentifier"]
            )
        )
    return out
