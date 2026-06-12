"""Generated from Smithy shape ``com.amazonaws.configservice#GetOrganizationConfigRuleDetailedStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_config_rule_detailed_status
    import aws_sdk_config_service.types.string


class GetOrganizationConfigRuleDetailedStatusResponse(TypedDict):
    organization_config_rule_detailed_status: NotRequired[
        "aws_sdk_config_service.types.organization_config_rule_detailed_status.OrganizationConfigRuleDetailedStatus"
    ]
    """<p>A list of <code>MemberAccountStatus</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetOrganizationConfigRuleDetailedStatusResponse,
) -> dict:
    out: dict = {}
    if "organization_config_rule_detailed_status" in value:
        import aws_sdk_config_service.types.organization_config_rule_detailed_status

        out["OrganizationConfigRuleDetailedStatus"] = (
            aws_sdk_config_service.types.organization_config_rule_detailed_status.serialize_aws_json_1_1(
                value["organization_config_rule_detailed_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetOrganizationConfigRuleDetailedStatusResponse:
    out: GetOrganizationConfigRuleDetailedStatusResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRuleDetailedStatus" in data:
        import aws_sdk_config_service.types.organization_config_rule_detailed_status

        out["organization_config_rule_detailed_status"] = (
            aws_sdk_config_service.types.organization_config_rule_detailed_status.deserialize_aws_json_1_1(
                data["OrganizationConfigRuleDetailedStatus"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
