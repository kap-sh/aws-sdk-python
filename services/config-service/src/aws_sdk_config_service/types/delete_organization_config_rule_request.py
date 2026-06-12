"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteOrganizationConfigRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_config_rule_name


class DeleteOrganizationConfigRuleRequest(TypedDict):
    organization_config_rule_name: "aws_sdk_config_service.types.organization_config_rule_name.OrganizationConfigRuleName"
    """<p>The name of organization Config rule that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteOrganizationConfigRuleRequest) -> dict:
    out: dict = {}
    out["OrganizationConfigRuleName"] = value["organization_config_rule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteOrganizationConfigRuleRequest:
    out: DeleteOrganizationConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRuleName" in data:
        out["organization_config_rule_name"] = data["OrganizationConfigRuleName"]
    else:
        raise DeserializationError(
            "DeleteOrganizationConfigRuleRequest.organization_config_rule_name required"
        )
    return out
