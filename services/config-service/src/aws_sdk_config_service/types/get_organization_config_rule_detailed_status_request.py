"""Generated from Smithy shape ``com.amazonaws.configservice#GetOrganizationConfigRuleDetailedStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.cosmos_page_limit
    import aws_sdk_config_service.types.organization_config_rule_name
    import aws_sdk_config_service.types.status_detail_filters
    import aws_sdk_config_service.types.string


class GetOrganizationConfigRuleDetailedStatusRequest(TypedDict, closed=True):
    organization_config_rule_name: "aws_sdk_config_service.types.organization_config_rule_name.OrganizationConfigRuleName"
    """<p>The name of your organization Config rule for which you want status details for member accounts.</p>"""
    filters: NotRequired[
        "aws_sdk_config_service.types.status_detail_filters.StatusDetailFilters"
    ]
    """<p>A <code>StatusDetailFilters</code> object.</p>"""
    limit: "aws_sdk_config_service.types.cosmos_page_limit.CosmosPageLimit"
    """<p>The maximum number of <code>OrganizationConfigRuleDetailedStatus</code> returned on each page. If you do not specify a number, Config uses the default. The default is 100.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetOrganizationConfigRuleDetailedStatusRequest,
) -> dict:
    out: dict = {}
    out["OrganizationConfigRuleName"] = value["organization_config_rule_name"]
    if "filters" in value:
        import aws_sdk_config_service.types.status_detail_filters

        out["Filters"] = (
            aws_sdk_config_service.types.status_detail_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetOrganizationConfigRuleDetailedStatusRequest:
    out: GetOrganizationConfigRuleDetailedStatusRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRuleName" in data:
        out["organization_config_rule_name"] = data["OrganizationConfigRuleName"]
    else:
        raise DeserializationError(
            "GetOrganizationConfigRuleDetailedStatusRequest.organization_config_rule_name required"
        )
    if "Filters" in data:
        import aws_sdk_config_service.types.status_detail_filters

        out["filters"] = (
            aws_sdk_config_service.types.status_detail_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
