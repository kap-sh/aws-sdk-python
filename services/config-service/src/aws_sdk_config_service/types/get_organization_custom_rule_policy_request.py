"""Generated from Smithy shape ``com.amazonaws.configservice#GetOrganizationCustomRulePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_config_rule_name


class GetOrganizationCustomRulePolicyRequest(TypedDict):
    organization_config_rule_name: "aws_sdk_config_service.types.organization_config_rule_name.OrganizationConfigRuleName"
    """<p>The name of your organization Config Custom Policy rule. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOrganizationCustomRulePolicyRequest) -> dict:
    out: dict = {}
    out["OrganizationConfigRuleName"] = value["organization_config_rule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOrganizationCustomRulePolicyRequest:
    out: GetOrganizationCustomRulePolicyRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRuleName" in data:
        out["organization_config_rule_name"] = data["OrganizationConfigRuleName"]
    else:
        raise DeserializationError(
            "GetOrganizationCustomRulePolicyRequest.organization_config_rule_name required"
        )
    return out
