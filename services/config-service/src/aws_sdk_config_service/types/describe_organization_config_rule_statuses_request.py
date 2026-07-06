"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeOrganizationConfigRuleStatusesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.cosmos_page_limit
    import aws_sdk_config_service.types.organization_config_rule_names
    import aws_sdk_config_service.types.string


class DescribeOrganizationConfigRuleStatusesRequest(TypedDict, closed=True):
    organization_config_rule_names: NotRequired[
        "aws_sdk_config_service.types.organization_config_rule_names.OrganizationConfigRuleNames"
    ]
    """<p>The names of organization Config rules for which you want status details. If you do not specify any names, Config returns details for all your organization Config rules.</p>"""
    limit: "aws_sdk_config_service.types.cosmos_page_limit.CosmosPageLimit"
    """<p>The maximum number of <code>OrganizationConfigRuleStatuses</code> returned on each page. If you do no specify a number, Config uses the default. The default is 100.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeOrganizationConfigRuleStatusesRequest,
) -> dict:
    out: dict = {}
    if "organization_config_rule_names" in value:
        import aws_sdk_config_service.types.organization_config_rule_names

        out["OrganizationConfigRuleNames"] = (
            aws_sdk_config_service.types.organization_config_rule_names.serialize_aws_json_1_1(
                value["organization_config_rule_names"]
            )
        )
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeOrganizationConfigRuleStatusesRequest:
    out: DescribeOrganizationConfigRuleStatusesRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRuleNames" in data:
        import aws_sdk_config_service.types.organization_config_rule_names

        out["organization_config_rule_names"] = (
            aws_sdk_config_service.types.organization_config_rule_names.deserialize_aws_json_1_1(
                data["OrganizationConfigRuleNames"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
