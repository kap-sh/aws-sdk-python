"""Generated from Smithy shape ``com.amazonaws.configservice#PutOrganizationConfigRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.string_with_char_limit256


class PutOrganizationConfigRuleResponse(TypedDict, closed=True):
    organization_config_rule_arn: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The Amazon Resource Name (ARN) of an organization Config rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutOrganizationConfigRuleResponse) -> dict:
    out: dict = {}
    if "organization_config_rule_arn" in value:
        out["OrganizationConfigRuleArn"] = value["organization_config_rule_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutOrganizationConfigRuleResponse:
    out: PutOrganizationConfigRuleResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRuleArn" in data:
        out["organization_config_rule_arn"] = data["OrganizationConfigRuleArn"]
    return out
