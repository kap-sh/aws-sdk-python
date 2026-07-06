"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConfigRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.excluded_accounts
    import aws_sdk_config_service.types.organization_config_rule_name
    import aws_sdk_config_service.types.organization_custom_policy_rule_metadata_no_policy
    import aws_sdk_config_service.types.organization_custom_rule_metadata
    import aws_sdk_config_service.types.organization_managed_rule_metadata
    import aws_sdk_config_service.types.string_with_char_limit256


class OrganizationConfigRule(TypedDict, closed=True):
    organization_config_rule_name: "aws_sdk_config_service.types.organization_config_rule_name.OrganizationConfigRuleName"
    """<p>The name that you assign to organization Config rule.</p>"""
    organization_config_rule_arn: (
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>Amazon Resource Name (ARN) of organization Config rule.</p>"""
    organization_managed_rule_metadata: NotRequired[
        "aws_sdk_config_service.types.organization_managed_rule_metadata.OrganizationManagedRuleMetadata"
    ]
    """<p>An <code>OrganizationManagedRuleMetadata</code> object.</p>"""
    organization_custom_rule_metadata: NotRequired[
        "aws_sdk_config_service.types.organization_custom_rule_metadata.OrganizationCustomRuleMetadata"
    ]
    """<p>An <code>OrganizationCustomRuleMetadata</code> object.</p>"""
    excluded_accounts: NotRequired[
        "aws_sdk_config_service.types.excluded_accounts.ExcludedAccounts"
    ]
    """<p>A comma-separated list of accounts excluded from organization Config rule.</p>"""
    last_update_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The timestamp of the last update.</p>"""
    organization_custom_policy_rule_metadata: NotRequired[
        "aws_sdk_config_service.types.organization_custom_policy_rule_metadata_no_policy.OrganizationCustomPolicyRuleMetadataNoPolicy"
    ]
    """<p>An object that specifies metadata for your organization's Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of Amazon Web Services resource, and organization trigger types that initiate Config to evaluate Amazon Web Services resources against a rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfigRule) -> dict:
    out: dict = {}
    out["OrganizationConfigRuleName"] = value["organization_config_rule_name"]
    out["OrganizationConfigRuleArn"] = value["organization_config_rule_arn"]
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
    if "last_update_time" in value:
        import aws_sdk_config_service.types.date

        out["LastUpdateTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["last_update_time"]
            )
        )
    if "organization_custom_policy_rule_metadata" in value:
        import aws_sdk_config_service.types.organization_custom_policy_rule_metadata_no_policy

        out["OrganizationCustomPolicyRuleMetadata"] = (
            aws_sdk_config_service.types.organization_custom_policy_rule_metadata_no_policy.serialize_aws_json_1_1(
                value["organization_custom_policy_rule_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationConfigRule:
    out: OrganizationConfigRule = {}  # type: ignore[typeddict-item]
    if "OrganizationConfigRuleName" in data:
        out["organization_config_rule_name"] = data["OrganizationConfigRuleName"]
    else:
        raise DeserializationError(
            "OrganizationConfigRule.organization_config_rule_name required"
        )
    if "OrganizationConfigRuleArn" in data:
        out["organization_config_rule_arn"] = data["OrganizationConfigRuleArn"]
    else:
        raise DeserializationError(
            "OrganizationConfigRule.organization_config_rule_arn required"
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
    if "LastUpdateTime" in data:
        import aws_sdk_config_service.types.date

        out["last_update_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateTime"]
            )
        )
    if "OrganizationCustomPolicyRuleMetadata" in data:
        import aws_sdk_config_service.types.organization_custom_policy_rule_metadata_no_policy

        out["organization_custom_policy_rule_metadata"] = (
            aws_sdk_config_service.types.organization_custom_policy_rule_metadata_no_policy.deserialize_aws_json_1_1(
                data["OrganizationCustomPolicyRuleMetadata"]
            )
        )
    return out
