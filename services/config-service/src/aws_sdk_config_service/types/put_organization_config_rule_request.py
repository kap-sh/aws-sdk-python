"""Generated from Smithy shape ``com.amazonaws.configservice#PutOrganizationConfigRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.excluded_accounts
    import aws_sdk_config_service.types.organization_config_rule_name
    import aws_sdk_config_service.types.organization_custom_policy_rule_metadata
    import aws_sdk_config_service.types.organization_custom_rule_metadata
    import aws_sdk_config_service.types.organization_managed_rule_metadata


class PutOrganizationConfigRuleRequest(TypedDict, closed=True):
    organization_config_rule_name: "aws_sdk_config_service.types.organization_config_rule_name.OrganizationConfigRuleName"
    """<p>The name that you assign to an organization Config rule.</p>"""
    organization_managed_rule_metadata: NotRequired[
        "aws_sdk_config_service.types.organization_managed_rule_metadata.OrganizationManagedRuleMetadata"
    ]
    """<p>An <code>OrganizationManagedRuleMetadata</code> object. This object specifies organization managed rule metadata such as resource type and ID of Amazon Web Services resource along with the rule identifier. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.</p>"""
    organization_custom_rule_metadata: NotRequired[
        "aws_sdk_config_service.types.organization_custom_rule_metadata.OrganizationCustomRuleMetadata"
    ]
    """<p>An <code>OrganizationCustomRuleMetadata</code> object. This object specifies organization custom rule metadata such as resource type, resource ID of Amazon Web Services resource, Lambda function ARN, and organization trigger types that trigger Config to evaluate your Amazon Web Services resources against a rule. It also provides the frequency with which you want Config to run evaluations for the rule if the trigger type is periodic.</p>"""
    excluded_accounts: NotRequired[
        "aws_sdk_config_service.types.excluded_accounts.ExcludedAccounts"
    ]
    """<p>A comma-separated list of accounts that you want to exclude from an organization Config rule.</p>"""
    organization_custom_policy_rule_metadata: NotRequired[
        "aws_sdk_config_service.types.organization_custom_policy_rule_metadata.OrganizationCustomPolicyRuleMetadata"
    ]
    """<p>An <code>OrganizationCustomPolicyRuleMetadata</code> object. This object specifies metadata for your organization's Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of Amazon Web Services resource, and organization trigger types that initiate Config to evaluate Amazon Web Services resources against a rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutOrganizationConfigRuleRequest) -> dict:
    out: dict = {}
    out["OrganizationConfigRuleName"] = value["organization_config_rule_name"]
    if "organization_managed_rule_metadata" in value:
        import aws_sdk_config_service.types.organization_managed_rule_metadata

        out["OrganizationManagedRuleMetadata"] = (
            aws_sdk_config_service.types.organization_managed_rule_metadata.serialize_aws_json_1_1(
                value["organization_managed_rule_metadata"]
            )
        )
    if "organization_custom_rule_metadata" in value:
        import aws_sdk_config_service.types.organization_custom_rule_metadata

        out["OrganizationCustomRuleMetadata"] = (
            aws_sdk_config_service.types.organization_custom_rule_metadata.serialize_aws_json_1_1(
                value["organization_custom_rule_metadata"]
            )
        )
    if "excluded_accounts" in value:
        import aws_sdk_config_service.types.excluded_accounts

        out["ExcludedAccounts"] = (
            aws_sdk_config_service.types.excluded_accounts.serialize_aws_json_1_1(
                value["excluded_accounts"]
            )
        )
    if "organization_custom_policy_rule_metadata" in value:
        import aws_sdk_config_service.types.organization_custom_policy_rule_metadata

        out["OrganizationCustomPolicyRuleMetadata"] = (
            aws_sdk_config_service.types.organization_custom_policy_rule_metadata.serialize_aws_json_1_1(
                value["organization_custom_policy_rule_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutOrganizationConfigRuleRequest:
    out: PutOrganizationConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRuleName" in data:
        out["organization_config_rule_name"] = data["OrganizationConfigRuleName"]
    else:
        raise DeserializationError(
            "PutOrganizationConfigRuleRequest.organization_config_rule_name required"
        )
    if "OrganizationManagedRuleMetadata" in data:
        import aws_sdk_config_service.types.organization_managed_rule_metadata

        out["organization_managed_rule_metadata"] = (
            aws_sdk_config_service.types.organization_managed_rule_metadata.deserialize_aws_json_1_1(
                data["OrganizationManagedRuleMetadata"]
            )
        )
    if "OrganizationCustomRuleMetadata" in data:
        import aws_sdk_config_service.types.organization_custom_rule_metadata

        out["organization_custom_rule_metadata"] = (
            aws_sdk_config_service.types.organization_custom_rule_metadata.deserialize_aws_json_1_1(
                data["OrganizationCustomRuleMetadata"]
            )
        )
    if "ExcludedAccounts" in data:
        import aws_sdk_config_service.types.excluded_accounts

        out["excluded_accounts"] = (
            aws_sdk_config_service.types.excluded_accounts.deserialize_aws_json_1_1(
                data["ExcludedAccounts"]
            )
        )
    if "OrganizationCustomPolicyRuleMetadata" in data:
        import aws_sdk_config_service.types.organization_custom_policy_rule_metadata

        out["organization_custom_policy_rule_metadata"] = (
            aws_sdk_config_service.types.organization_custom_policy_rule_metadata.deserialize_aws_json_1_1(
                data["OrganizationCustomPolicyRuleMetadata"]
            )
        )
    return out
