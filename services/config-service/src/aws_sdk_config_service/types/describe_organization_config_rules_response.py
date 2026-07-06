"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeOrganizationConfigRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_config_rules
    import aws_sdk_config_service.types.string


class DescribeOrganizationConfigRulesResponse(TypedDict, closed=True):
    organization_config_rules: NotRequired[
        "aws_sdk_config_service.types.organization_config_rules.OrganizationConfigRules"
    ]
    """<p>Returns a list of <code>OrganizationConfigRule</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOrganizationConfigRulesResponse) -> dict:
    out: dict = {}
    if "organization_config_rules" in value:
        import aws_sdk_config_service.types.organization_config_rules

        out["OrganizationConfigRules"] = (
            aws_sdk_config_service.types.organization_config_rules.serialize_aws_json_1_1(
                value["organization_config_rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeOrganizationConfigRulesResponse:
    out: DescribeOrganizationConfigRulesResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRules" in data:
        import aws_sdk_config_service.types.organization_config_rules

        out["organization_config_rules"] = (
            aws_sdk_config_service.types.organization_config_rules.deserialize_aws_json_1_1(
                data["OrganizationConfigRules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
