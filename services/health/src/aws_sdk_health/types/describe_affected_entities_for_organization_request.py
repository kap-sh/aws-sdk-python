"""Generated from Smithy shape ``com.amazonaws.health#DescribeAffectedEntitiesForOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_health.types.locale
    import aws_sdk_health.types.max_results_lower_range
    import aws_sdk_health.types.next_token
    import aws_sdk_health.types.organization_entity_account_filters_list
    import aws_sdk_health.types.organization_entity_filters_list


class DescribeAffectedEntitiesForOrganizationRequest(TypedDict, closed=True):
    organization_entity_filters: NotRequired[
        "aws_sdk_health.types.organization_entity_filters_list.OrganizationEntityFiltersList"
    ]
    """<p>A JSON set of elements including the <code>awsAccountId</code> and the <code>eventArn</code>.</p>"""
    locale: NotRequired["aws_sdk_health.types.locale.locale"]
    """<p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>"""
    next_token: NotRequired["aws_sdk_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""
    max_results: NotRequired[
        "aws_sdk_health.types.max_results_lower_range.maxResultsLowerRange"
    ]
    """<p>The maximum number of items to return in one batch, between 1 and 100, inclusive.</p>"""
    organization_entity_account_filters: NotRequired[
        "aws_sdk_health.types.organization_entity_account_filters_list.OrganizationEntityAccountFiltersList"
    ]
    """<p>A JSON set of elements including the <code>awsAccountId</code>, <code>eventArn</code> and a set of <code>statusCodes</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeAffectedEntitiesForOrganizationRequest,
) -> dict:
    out: dict = {}
    if "organization_entity_filters" in value:
        import aws_sdk_health.types.organization_entity_filters_list

        out["organizationEntityFilters"] = (
            aws_sdk_health.types.organization_entity_filters_list.serialize_aws_json_1_1(
                value["organization_entity_filters"]
            )
        )
    if "locale" in value:
        out["locale"] = value["locale"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "organization_entity_account_filters" in value:
        import aws_sdk_health.types.organization_entity_account_filters_list

        out["organizationEntityAccountFilters"] = (
            aws_sdk_health.types.organization_entity_account_filters_list.serialize_aws_json_1_1(
                value["organization_entity_account_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeAffectedEntitiesForOrganizationRequest:
    out: DescribeAffectedEntitiesForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if "organizationEntityFilters" in data:
        import aws_sdk_health.types.organization_entity_filters_list

        out["organization_entity_filters"] = (
            aws_sdk_health.types.organization_entity_filters_list.deserialize_aws_json_1_1(
                data["organizationEntityFilters"]
            )
        )
    if "locale" in data:
        out["locale"] = data["locale"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "organizationEntityAccountFilters" in data:
        import aws_sdk_health.types.organization_entity_account_filters_list

        out["organization_entity_account_filters"] = (
            aws_sdk_health.types.organization_entity_account_filters_list.deserialize_aws_json_1_1(
                data["organizationEntityAccountFilters"]
            )
        )
    return out
