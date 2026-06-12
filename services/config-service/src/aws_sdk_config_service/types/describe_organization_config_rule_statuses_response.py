"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeOrganizationConfigRuleStatusesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_config_rule_statuses
    import aws_sdk_config_service.types.string


class DescribeOrganizationConfigRuleStatusesResponse(TypedDict):
    organization_config_rule_statuses: NotRequired[
        "aws_sdk_config_service.types.organization_config_rule_statuses.OrganizationConfigRuleStatuses"
    ]
    """<p>A list of <code>OrganizationConfigRuleStatus</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeOrganizationConfigRuleStatusesResponse,
) -> dict:
    out: dict = {}
    if "organization_config_rule_statuses" in value:
        import aws_sdk_config_service.types.organization_config_rule_statuses

        out["OrganizationConfigRuleStatuses"] = (
            aws_sdk_config_service.types.organization_config_rule_statuses.serialize_aws_json_1_1(
                value["organization_config_rule_statuses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeOrganizationConfigRuleStatusesResponse:
    out: DescribeOrganizationConfigRuleStatusesResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRuleStatuses" in data:
        import aws_sdk_config_service.types.organization_config_rule_statuses

        out["organization_config_rule_statuses"] = (
            aws_sdk_config_service.types.organization_config_rule_statuses.deserialize_aws_json_1_1(
                data["OrganizationConfigRuleStatuses"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
