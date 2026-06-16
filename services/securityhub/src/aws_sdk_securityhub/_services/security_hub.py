"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityHubAPIService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_securityhub._auth._signers
import aws_sdk_securityhub._auth._sigv4
from aws_sdk_securityhub._auth._identity import Credentials
from aws_sdk_securityhub._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_securityhub._auth._zapros_handler import AuthMiddleware
from aws_sdk_securityhub._pagination import resolve_path as _resolve_path
from aws_sdk_securityhub._services._aws_config import aws_config
from aws_sdk_securityhub._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.accept_administrator_invitation_request
    import aws_sdk_securityhub.types.accept_administrator_invitation_response
    import aws_sdk_securityhub.types.accept_invitation_request
    import aws_sdk_securityhub.types.accept_invitation_response
    import aws_sdk_securityhub.types.account_details_list
    import aws_sdk_securityhub.types.account_id_list
    import aws_sdk_securityhub.types.action_list
    import aws_sdk_securityhub.types.action_target
    import aws_sdk_securityhub.types.admin_account
    import aws_sdk_securityhub.types.admins_max_results
    import aws_sdk_securityhub.types.aggregator_v2
    import aws_sdk_securityhub.types.alpha_numeric_non_empty_string
    import aws_sdk_securityhub.types.arn_list
    import aws_sdk_securityhub.types.association_filters
    import aws_sdk_securityhub.types.auto_enable_standards
    import aws_sdk_securityhub.types.automation_rules_action_list_v2
    import aws_sdk_securityhub.types.automation_rules_arns_list
    import aws_sdk_securityhub.types.automation_rules_finding_filters
    import aws_sdk_securityhub.types.aws_security_finding
    import aws_sdk_securityhub.types.aws_security_finding_filters
    import aws_sdk_securityhub.types.aws_security_finding_identifier
    import aws_sdk_securityhub.types.aws_security_finding_identifier_list
    import aws_sdk_securityhub.types.batch_delete_automation_rules_request
    import aws_sdk_securityhub.types.batch_delete_automation_rules_response
    import aws_sdk_securityhub.types.batch_disable_standards_request
    import aws_sdk_securityhub.types.batch_disable_standards_response
    import aws_sdk_securityhub.types.batch_enable_standards_request
    import aws_sdk_securityhub.types.batch_enable_standards_response
    import aws_sdk_securityhub.types.batch_get_automation_rules_request
    import aws_sdk_securityhub.types.batch_get_automation_rules_response
    import aws_sdk_securityhub.types.batch_get_configuration_policy_associations_request
    import aws_sdk_securityhub.types.batch_get_configuration_policy_associations_response
    import aws_sdk_securityhub.types.batch_get_security_controls_request
    import aws_sdk_securityhub.types.batch_get_security_controls_response
    import aws_sdk_securityhub.types.batch_get_standards_control_associations_request
    import aws_sdk_securityhub.types.batch_get_standards_control_associations_response
    import aws_sdk_securityhub.types.batch_import_findings_request
    import aws_sdk_securityhub.types.batch_import_findings_request_finding_list
    import aws_sdk_securityhub.types.batch_import_findings_response
    import aws_sdk_securityhub.types.batch_update_automation_rules_request
    import aws_sdk_securityhub.types.batch_update_automation_rules_response
    import aws_sdk_securityhub.types.batch_update_findings_request
    import aws_sdk_securityhub.types.batch_update_findings_response
    import aws_sdk_securityhub.types.batch_update_findings_v2_request
    import aws_sdk_securityhub.types.batch_update_findings_v2_response
    import aws_sdk_securityhub.types.batch_update_standards_control_associations_request
    import aws_sdk_securityhub.types.batch_update_standards_control_associations_response
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.client_token
    import aws_sdk_securityhub.types.configuration_policy_association_summary
    import aws_sdk_securityhub.types.configuration_policy_associations_list
    import aws_sdk_securityhub.types.configuration_policy_summary
    import aws_sdk_securityhub.types.connector_provider_name
    import aws_sdk_securityhub.types.connector_status
    import aws_sdk_securityhub.types.control_finding_generator
    import aws_sdk_securityhub.types.control_status
    import aws_sdk_securityhub.types.create_action_target_request
    import aws_sdk_securityhub.types.create_action_target_response
    import aws_sdk_securityhub.types.create_aggregator_v2_request
    import aws_sdk_securityhub.types.create_aggregator_v2_response
    import aws_sdk_securityhub.types.create_automation_rule_request
    import aws_sdk_securityhub.types.create_automation_rule_response
    import aws_sdk_securityhub.types.create_automation_rule_v2_request
    import aws_sdk_securityhub.types.create_automation_rule_v2_response
    import aws_sdk_securityhub.types.create_configuration_policy_request
    import aws_sdk_securityhub.types.create_configuration_policy_response
    import aws_sdk_securityhub.types.create_connector_v2_request
    import aws_sdk_securityhub.types.create_connector_v2_response
    import aws_sdk_securityhub.types.create_finding_aggregator_request
    import aws_sdk_securityhub.types.create_finding_aggregator_response
    import aws_sdk_securityhub.types.create_insight_request
    import aws_sdk_securityhub.types.create_insight_response
    import aws_sdk_securityhub.types.create_members_request
    import aws_sdk_securityhub.types.create_members_response
    import aws_sdk_securityhub.types.create_ticket_v2_request
    import aws_sdk_securityhub.types.create_ticket_v2_response
    import aws_sdk_securityhub.types.criteria
    import aws_sdk_securityhub.types.cross_account_max_results
    import aws_sdk_securityhub.types.decline_invitations_request
    import aws_sdk_securityhub.types.decline_invitations_response
    import aws_sdk_securityhub.types.delete_action_target_request
    import aws_sdk_securityhub.types.delete_action_target_response
    import aws_sdk_securityhub.types.delete_aggregator_v2_request
    import aws_sdk_securityhub.types.delete_aggregator_v2_response
    import aws_sdk_securityhub.types.delete_automation_rule_v2_request
    import aws_sdk_securityhub.types.delete_automation_rule_v2_response
    import aws_sdk_securityhub.types.delete_configuration_policy_request
    import aws_sdk_securityhub.types.delete_configuration_policy_response
    import aws_sdk_securityhub.types.delete_connector_v2_request
    import aws_sdk_securityhub.types.delete_connector_v2_response
    import aws_sdk_securityhub.types.delete_finding_aggregator_request
    import aws_sdk_securityhub.types.delete_finding_aggregator_response
    import aws_sdk_securityhub.types.delete_insight_request
    import aws_sdk_securityhub.types.delete_insight_response
    import aws_sdk_securityhub.types.delete_invitations_request
    import aws_sdk_securityhub.types.delete_invitations_response
    import aws_sdk_securityhub.types.delete_members_request
    import aws_sdk_securityhub.types.delete_members_response
    import aws_sdk_securityhub.types.describe_action_targets_request
    import aws_sdk_securityhub.types.describe_action_targets_response
    import aws_sdk_securityhub.types.describe_hub_request
    import aws_sdk_securityhub.types.describe_hub_response
    import aws_sdk_securityhub.types.describe_organization_configuration_request
    import aws_sdk_securityhub.types.describe_organization_configuration_response
    import aws_sdk_securityhub.types.describe_products_request
    import aws_sdk_securityhub.types.describe_products_response
    import aws_sdk_securityhub.types.describe_products_v2_request
    import aws_sdk_securityhub.types.describe_products_v2_response
    import aws_sdk_securityhub.types.describe_security_hub_v2_request
    import aws_sdk_securityhub.types.describe_security_hub_v2_response
    import aws_sdk_securityhub.types.describe_standards_controls_request
    import aws_sdk_securityhub.types.describe_standards_controls_response
    import aws_sdk_securityhub.types.describe_standards_request
    import aws_sdk_securityhub.types.describe_standards_response
    import aws_sdk_securityhub.types.disable_import_findings_for_product_request
    import aws_sdk_securityhub.types.disable_import_findings_for_product_response
    import aws_sdk_securityhub.types.disable_organization_admin_account_request
    import aws_sdk_securityhub.types.disable_organization_admin_account_response
    import aws_sdk_securityhub.types.disable_security_hub_request
    import aws_sdk_securityhub.types.disable_security_hub_response
    import aws_sdk_securityhub.types.disable_security_hub_v2_request
    import aws_sdk_securityhub.types.disable_security_hub_v2_response
    import aws_sdk_securityhub.types.disassociate_from_administrator_account_request
    import aws_sdk_securityhub.types.disassociate_from_administrator_account_response
    import aws_sdk_securityhub.types.disassociate_from_master_account_request
    import aws_sdk_securityhub.types.disassociate_from_master_account_response
    import aws_sdk_securityhub.types.disassociate_members_request
    import aws_sdk_securityhub.types.disassociate_members_response
    import aws_sdk_securityhub.types.enable_import_findings_for_product_request
    import aws_sdk_securityhub.types.enable_import_findings_for_product_response
    import aws_sdk_securityhub.types.enable_organization_admin_account_request
    import aws_sdk_securityhub.types.enable_organization_admin_account_response
    import aws_sdk_securityhub.types.enable_security_hub_request
    import aws_sdk_securityhub.types.enable_security_hub_response
    import aws_sdk_securityhub.types.enable_security_hub_v2_request
    import aws_sdk_securityhub.types.enable_security_hub_v2_response
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.finding_aggregator
    import aws_sdk_securityhub.types.finding_history_record
    import aws_sdk_securityhub.types.finding_scopes
    import aws_sdk_securityhub.types.findings_trends_filters
    import aws_sdk_securityhub.types.generate_recommended_policy_v2_request
    import aws_sdk_securityhub.types.generate_recommended_policy_v2_response
    import aws_sdk_securityhub.types.get_administrator_account_request
    import aws_sdk_securityhub.types.get_administrator_account_response
    import aws_sdk_securityhub.types.get_aggregator_v2_request
    import aws_sdk_securityhub.types.get_aggregator_v2_response
    import aws_sdk_securityhub.types.get_automation_rule_v2_request
    import aws_sdk_securityhub.types.get_automation_rule_v2_response
    import aws_sdk_securityhub.types.get_configuration_policy_association_request
    import aws_sdk_securityhub.types.get_configuration_policy_association_response
    import aws_sdk_securityhub.types.get_configuration_policy_request
    import aws_sdk_securityhub.types.get_configuration_policy_response
    import aws_sdk_securityhub.types.get_connector_v2_request
    import aws_sdk_securityhub.types.get_connector_v2_response
    import aws_sdk_securityhub.types.get_enabled_standards_request
    import aws_sdk_securityhub.types.get_enabled_standards_response
    import aws_sdk_securityhub.types.get_finding_aggregator_request
    import aws_sdk_securityhub.types.get_finding_aggregator_response
    import aws_sdk_securityhub.types.get_finding_history_request
    import aws_sdk_securityhub.types.get_finding_history_response
    import aws_sdk_securityhub.types.get_finding_statistics_v2_request
    import aws_sdk_securityhub.types.get_finding_statistics_v2_response
    import aws_sdk_securityhub.types.get_findings_request
    import aws_sdk_securityhub.types.get_findings_response
    import aws_sdk_securityhub.types.get_findings_trends_v2_request
    import aws_sdk_securityhub.types.get_findings_trends_v2_response
    import aws_sdk_securityhub.types.get_findings_v2_request
    import aws_sdk_securityhub.types.get_findings_v2_response
    import aws_sdk_securityhub.types.get_insight_results_request
    import aws_sdk_securityhub.types.get_insight_results_response
    import aws_sdk_securityhub.types.get_insights_request
    import aws_sdk_securityhub.types.get_insights_response
    import aws_sdk_securityhub.types.get_invitations_count_request
    import aws_sdk_securityhub.types.get_invitations_count_response
    import aws_sdk_securityhub.types.get_master_account_request
    import aws_sdk_securityhub.types.get_master_account_response
    import aws_sdk_securityhub.types.get_members_request
    import aws_sdk_securityhub.types.get_members_response
    import aws_sdk_securityhub.types.get_recommended_policy_v2_request
    import aws_sdk_securityhub.types.get_recommended_policy_v2_response
    import aws_sdk_securityhub.types.get_resources_statistics_v2_request
    import aws_sdk_securityhub.types.get_resources_statistics_v2_response
    import aws_sdk_securityhub.types.get_resources_trends_v2_request
    import aws_sdk_securityhub.types.get_resources_trends_v2_response
    import aws_sdk_securityhub.types.get_resources_v2_request
    import aws_sdk_securityhub.types.get_resources_v2_response
    import aws_sdk_securityhub.types.get_security_control_definition_request
    import aws_sdk_securityhub.types.get_security_control_definition_response
    import aws_sdk_securityhub.types.group_by_rules
    import aws_sdk_securityhub.types.insight
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.invitation
    import aws_sdk_securityhub.types.invite_members_request
    import aws_sdk_securityhub.types.invite_members_response
    import aws_sdk_securityhub.types.list_aggregators_v2_request
    import aws_sdk_securityhub.types.list_aggregators_v2_response
    import aws_sdk_securityhub.types.list_automation_rules_request
    import aws_sdk_securityhub.types.list_automation_rules_response
    import aws_sdk_securityhub.types.list_automation_rules_v2_request
    import aws_sdk_securityhub.types.list_automation_rules_v2_response
    import aws_sdk_securityhub.types.list_configuration_policies_request
    import aws_sdk_securityhub.types.list_configuration_policies_response
    import aws_sdk_securityhub.types.list_configuration_policy_associations_request
    import aws_sdk_securityhub.types.list_configuration_policy_associations_response
    import aws_sdk_securityhub.types.list_connectors_v2_request
    import aws_sdk_securityhub.types.list_connectors_v2_response
    import aws_sdk_securityhub.types.list_enabled_products_for_import_request
    import aws_sdk_securityhub.types.list_enabled_products_for_import_response
    import aws_sdk_securityhub.types.list_finding_aggregators_request
    import aws_sdk_securityhub.types.list_finding_aggregators_response
    import aws_sdk_securityhub.types.list_invitations_request
    import aws_sdk_securityhub.types.list_invitations_response
    import aws_sdk_securityhub.types.list_members_request
    import aws_sdk_securityhub.types.list_members_response
    import aws_sdk_securityhub.types.list_organization_admin_accounts_request
    import aws_sdk_securityhub.types.list_organization_admin_accounts_response
    import aws_sdk_securityhub.types.list_security_control_definitions_request
    import aws_sdk_securityhub.types.list_security_control_definitions_response
    import aws_sdk_securityhub.types.list_standards_control_associations_request
    import aws_sdk_securityhub.types.list_standards_control_associations_response
    import aws_sdk_securityhub.types.list_tags_for_resource_request
    import aws_sdk_securityhub.types.list_tags_for_resource_response
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.max_statistic_results
    import aws_sdk_securityhub.types.member
    import aws_sdk_securityhub.types.metadata_uid_list
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.note_update
    import aws_sdk_securityhub.types.ocsf_finding
    import aws_sdk_securityhub.types.ocsf_finding_filters
    import aws_sdk_securityhub.types.ocsf_finding_identifier_list
    import aws_sdk_securityhub.types.organization_configuration
    import aws_sdk_securityhub.types.parameters
    import aws_sdk_securityhub.types.policy
    import aws_sdk_securityhub.types.product
    import aws_sdk_securityhub.types.product_v2
    import aws_sdk_securityhub.types.provider_configuration
    import aws_sdk_securityhub.types.provider_update_configuration
    import aws_sdk_securityhub.types.ratio_scale
    import aws_sdk_securityhub.types.recommendation_step
    import aws_sdk_securityhub.types.record_state
    import aws_sdk_securityhub.types.register_connector_v2_request
    import aws_sdk_securityhub.types.register_connector_v2_response
    import aws_sdk_securityhub.types.related_finding_list
    import aws_sdk_securityhub.types.resource_arn
    import aws_sdk_securityhub.types.resource_group_by_rules
    import aws_sdk_securityhub.types.resource_result
    import aws_sdk_securityhub.types.resource_scopes
    import aws_sdk_securityhub.types.resources_filters
    import aws_sdk_securityhub.types.resources_trends_filters
    import aws_sdk_securityhub.types.resources_trends_metrics_result
    import aws_sdk_securityhub.types.rule_order_value
    import aws_sdk_securityhub.types.rule_order_value_v2
    import aws_sdk_securityhub.types.rule_status
    import aws_sdk_securityhub.types.rule_status_v2
    import aws_sdk_securityhub.types.security_control_definition
    import aws_sdk_securityhub.types.security_hub_feature
    import aws_sdk_securityhub.types.severity_update
    import aws_sdk_securityhub.types.sort_criteria
    import aws_sdk_securityhub.types.sort_order
    import aws_sdk_securityhub.types.standard
    import aws_sdk_securityhub.types.standards_control
    import aws_sdk_securityhub.types.standards_control_association_ids
    import aws_sdk_securityhub.types.standards_control_association_summary
    import aws_sdk_securityhub.types.standards_control_association_updates
    import aws_sdk_securityhub.types.standards_subscription
    import aws_sdk_securityhub.types.standards_subscription_arns
    import aws_sdk_securityhub.types.standards_subscription_requests
    import aws_sdk_securityhub.types.start_configuration_policy_association_request
    import aws_sdk_securityhub.types.start_configuration_policy_association_response
    import aws_sdk_securityhub.types.start_configuration_policy_disassociation_request
    import aws_sdk_securityhub.types.start_configuration_policy_disassociation_response
    import aws_sdk_securityhub.types.string_list
    import aws_sdk_securityhub.types.tag_key_list
    import aws_sdk_securityhub.types.tag_map
    import aws_sdk_securityhub.types.tag_resource_request
    import aws_sdk_securityhub.types.tag_resource_response
    import aws_sdk_securityhub.types.target
    import aws_sdk_securityhub.types.ticket_creation_mode
    import aws_sdk_securityhub.types.timestamp
    import aws_sdk_securityhub.types.trends_metrics_result
    import aws_sdk_securityhub.types.type_list
    import aws_sdk_securityhub.types.untag_resource_request
    import aws_sdk_securityhub.types.untag_resource_response
    import aws_sdk_securityhub.types.update_action_target_request
    import aws_sdk_securityhub.types.update_action_target_response
    import aws_sdk_securityhub.types.update_aggregator_v2_request
    import aws_sdk_securityhub.types.update_aggregator_v2_response
    import aws_sdk_securityhub.types.update_automation_rule_v2_request
    import aws_sdk_securityhub.types.update_automation_rule_v2_response
    import aws_sdk_securityhub.types.update_automation_rules_request_items_list
    import aws_sdk_securityhub.types.update_configuration_policy_request
    import aws_sdk_securityhub.types.update_configuration_policy_response
    import aws_sdk_securityhub.types.update_connector_v2_request
    import aws_sdk_securityhub.types.update_connector_v2_response
    import aws_sdk_securityhub.types.update_finding_aggregator_request
    import aws_sdk_securityhub.types.update_finding_aggregator_response
    import aws_sdk_securityhub.types.update_findings_request
    import aws_sdk_securityhub.types.update_findings_response
    import aws_sdk_securityhub.types.update_insight_request
    import aws_sdk_securityhub.types.update_insight_response
    import aws_sdk_securityhub.types.update_organization_configuration_request
    import aws_sdk_securityhub.types.update_organization_configuration_response
    import aws_sdk_securityhub.types.update_security_control_request
    import aws_sdk_securityhub.types.update_security_control_response
    import aws_sdk_securityhub.types.update_security_hub_configuration_request
    import aws_sdk_securityhub.types.update_security_hub_configuration_response
    import aws_sdk_securityhub.types.update_standards_control_request
    import aws_sdk_securityhub.types.update_standards_control_response
    import aws_sdk_securityhub.types.verification_state
    import aws_sdk_securityhub.types.workflow_update


class SecurityHubClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SecurityHubClient:
    """A client for the ``SecurityHub`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = SecurityHubClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[SecurityHubClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SecurityHubClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def accept_administrator_invitation(
        self,
        administrator_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        invitation_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.accept_administrator_invitation_response.AcceptAdministratorInvitationResponse":
        r"""<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html\">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Accepts the invitation to be a member account and be monitored by the Security Hub CSPM administrator account that the invitation was sent from.</p> <p>This operation is only used by member accounts that are not added through Organizations.</p> <p>When the member account accepts the invitation, permission is granted to the administrator account to view findings generated in the member account.</p>

        Args:
            administrator_id: <p>The account ID of the Security Hub CSPM administrator account that sent the invitation.</p>
            invitation_id: <p>The identifier of the invitation sent from the Security Hub CSPM administrator account.</p>

        Examples:
            To accept an invitation be a member account
            The following example demonstrates how an account can accept an invitation from the Security Hub administrator account to be a member account. This operation is applicable only to member accounts that are not added through AWS Organizations.

            >>> client.accept_administrator_invitation(administrator_id='123456789012', invitation_id='7ab938c5d52d7904ad09f9e7c20cc4eb')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.accept_administrator_invitation_request.AcceptAdministratorInvitationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.accept_administrator_invitation_response.AcceptAdministratorInvitationResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.accept_administrator_invitation

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.accept_administrator_invitation.accept_administrator_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.accept_administrator_invitation_request.AcceptAdministratorInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["administrator_id"] = administrator_id
        input_["invitation_id"] = invitation_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def accept_invitation(
        self,
        master_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        invitation_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> (
        "aws_sdk_securityhub.types.accept_invitation_response.AcceptInvitationResponse"
    ):
        """<p>This method is deprecated. Instead, use <code>AcceptAdministratorInvitation</code>.</p> <p>The Security Hub CSPM console continues to use <code>AcceptInvitation</code>. It will eventually change to use <code>AcceptAdministratorInvitation</code>. Any IAM policies that specifically control access to this function must continue to use <code>AcceptInvitation</code>. You should also add <code>AcceptAdministratorInvitation</code> to your policies to ensure that the correct permissions are in place after the console begins to use <code>AcceptAdministratorInvitation</code>.</p> <p>Accepts the invitation to be a member account and be monitored by the Security Hub CSPM administrator account that the invitation was sent from.</p> <p>This operation is only used by member accounts that are not added through Organizations.</p> <p>When the member account accepts the invitation, permission is granted to the administrator account to view findings generated in the member account.</p>

        Args:
            master_id: <p>The account ID of the Security Hub CSPM administrator account that sent the invitation.</p>
            invitation_id: <p>The identifier of the invitation sent from the Security Hub CSPM administrator account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.accept_invitation_request.AcceptInvitationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.accept_invitation_response.AcceptInvitationResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.accept_invitation

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.accept_invitation.accept_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.accept_invitation_request.AcceptInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["master_id"] = master_id
        input_["invitation_id"] = invitation_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_delete_automation_rules(
        self,
        automation_rules_arns: "aws_sdk_securityhub.types.automation_rules_arns_list.AutomationRulesArnsList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.batch_delete_automation_rules_response.BatchDeleteAutomationRulesResponse":
        """<p> Deletes one or more automation rules. </p>

        Args:
            automation_rules_arns: <p> A list of Amazon Resource Names (ARNs) for the rules that are to be deleted. </p>

        Examples:
            To delete one or more automation rules
            The following example deletes the specified automation rules.

            >>> client.batch_delete_automation_rules(automation_rules_arns=['arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_delete_automation_rules_request.BatchDeleteAutomationRulesRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_delete_automation_rules_response.BatchDeleteAutomationRulesResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_delete_automation_rules

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_delete_automation_rules.batch_delete_automation_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_delete_automation_rules_request.BatchDeleteAutomationRulesRequest = {}  # type: ignore[typeddict-item]
        input_["automation_rules_arns"] = automation_rules_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_disable_standards(
        self,
        standards_subscription_arns: "aws_sdk_securityhub.types.standards_subscription_arns.StandardsSubscriptionArns",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.batch_disable_standards_response.BatchDisableStandardsResponse":
        r"""<p>Disables the standards specified by the provided <code>StandardsSubscriptionArns</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html\">Security Standards</a> section of the <i>Security Hub CSPM User Guide</i>.</p>

        Args:
            standards_subscription_arns: <p>The ARNs of the standards subscriptions to disable.</p>

        Examples:
            To disable one or more security standards
            The following example disables a security standard in Security Hub.

            >>> client.batch_disable_standards(standards_subscription_arns=['arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_disable_standards_request.BatchDisableStandardsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_disable_standards_response.BatchDisableStandardsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_disable_standards

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_disable_standards.batch_disable_standards(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_disable_standards_request.BatchDisableStandardsRequest = {}  # type: ignore[typeddict-item]
        input_["standards_subscription_arns"] = standards_subscription_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_enable_standards(
        self,
        standards_subscription_requests: "aws_sdk_securityhub.types.standards_subscription_requests.StandardsSubscriptionRequests",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.batch_enable_standards_response.BatchEnableStandardsResponse":
        r"""<p>Enables the standards specified by the provided <code>StandardsArn</code>. To obtain the ARN for a standard, use the <code>DescribeStandards</code> operation.</p> <p>For more information, see the <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html\">Security Standards</a> section of the <i>Security Hub CSPM User Guide</i>.</p>

        Args:
            standards_subscription_requests: <p>The list of standards checks to enable.</p>

        Examples:
            To enable security standards
            The following example enables the security standard specified by the StandardArn. You can use this operation to enable one or more Security Hub standards.

            >>> client.batch_enable_standards(standards_subscription_requests=[{'StandardsArn': 'arn:aws:securityhub:us-west-1::standards/pci-dss/v/3.2.1'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_enable_standards_request.BatchEnableStandardsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_enable_standards_response.BatchEnableStandardsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_enable_standards

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_enable_standards.batch_enable_standards(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_enable_standards_request.BatchEnableStandardsRequest = {}  # type: ignore[typeddict-item]
        input_["standards_subscription_requests"] = standards_subscription_requests

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_automation_rules(
        self,
        automation_rules_arns: "aws_sdk_securityhub.types.automation_rules_arns_list.AutomationRulesArnsList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.batch_get_automation_rules_response.BatchGetAutomationRulesResponse":
        """<p> Retrieves a list of details for automation rules based on rule Amazon Resource Names (ARNs). </p>

        Args:
            automation_rules_arns: <p> A list of rule ARNs to get details for. </p>

        Examples:
            To update one ore more automation rules
            The following example updates the specified automation rules.

            >>> client.batch_get_automation_rules(automation_rules_arns=['arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_get_automation_rules_request.BatchGetAutomationRulesRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_get_automation_rules_response.BatchGetAutomationRulesResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_get_automation_rules

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_get_automation_rules.batch_get_automation_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_get_automation_rules_request.BatchGetAutomationRulesRequest = {}  # type: ignore[typeddict-item]
        input_["automation_rules_arns"] = automation_rules_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_configuration_policy_associations(
        self,
        configuration_policy_association_identifiers: "aws_sdk_securityhub.types.configuration_policy_associations_list.ConfigurationPolicyAssociationsList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.batch_get_configuration_policy_associations_response.BatchGetConfigurationPolicyAssociationsResponse":
        """<p> Returns associations between an Security Hub CSPM configuration and a batch of target accounts, organizational units, or the root. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. A configuration can refer to a configuration policy or to a self-managed configuration. </p>

        Args:
            configuration_policy_association_identifiers: <p> Specifies one or more target account IDs, organizational unit (OU) IDs, or the root ID to retrieve associations for. </p>

        Examples:
            To get configuration associations for a batch of targets
            This operation provides details about configuration associations for a batch of target accounts, organizational units, or the root.

            >>> client.batch_get_configuration_policy_associations(configuration_policy_association_identifiers=[{'Target': {'AccountId': '111122223333'}}, {'Target': {'RootId': 'r-f6g7h8i9j0example'}}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_get_configuration_policy_associations_request.BatchGetConfigurationPolicyAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_get_configuration_policy_associations_response.BatchGetConfigurationPolicyAssociationsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_get_configuration_policy_associations

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_get_configuration_policy_associations.batch_get_configuration_policy_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_get_configuration_policy_associations_request.BatchGetConfigurationPolicyAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["configuration_policy_association_identifiers"] = (
            configuration_policy_association_identifiers
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_security_controls(
        self,
        security_control_ids: "aws_sdk_securityhub.types.string_list.StringList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.batch_get_security_controls_response.BatchGetSecurityControlsResponse":
        """<p> Provides details about a batch of security controls for the current Amazon Web Services account and Amazon Web Services Region. </p>

        Args:
            security_control_ids: <p> A list of security controls (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters). The security control ID or Amazon Resource Name (ARN) is the same across standards. </p>

        Examples:
            To get security control details
            The following example gets details for the specified controls in the current AWS account and AWS Region.

            >>> client.batch_get_security_controls(security_control_ids=['ACM.1', 'APIGateway.1'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_get_security_controls_request.BatchGetSecurityControlsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_get_security_controls_response.BatchGetSecurityControlsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_get_security_controls

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_get_security_controls.batch_get_security_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_get_security_controls_request.BatchGetSecurityControlsRequest = {}  # type: ignore[typeddict-item]
        input_["security_control_ids"] = security_control_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_standards_control_associations(
        self,
        standards_control_association_ids: "aws_sdk_securityhub.types.standards_control_association_ids.StandardsControlAssociationIds",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.batch_get_standards_control_associations_response.BatchGetStandardsControlAssociationsResponse":
        """<p> For a batch of security controls and standards, identifies whether each control is currently enabled or disabled in a standard. </p> <p> Calls to this operation return a <code>RESOURCE_NOT_FOUND_EXCEPTION</code> error when the standard subscription for the association has a <code>NOT_READY_FOR_UPDATES</code> value for <code>StandardsControlsUpdatable</code>. </p>

        Args:
            standards_control_association_ids: <p> An array with one or more objects that includes a security control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) and the Amazon Resource Name (ARN) of a standard. This field is used to query the enablement status of a control in a specified standard. The security control ID or ARN is the same across standards. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_get_standards_control_associations_request.BatchGetStandardsControlAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_get_standards_control_associations_response.BatchGetStandardsControlAssociationsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_get_standards_control_associations

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_get_standards_control_associations.batch_get_standards_control_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_get_standards_control_associations_request.BatchGetStandardsControlAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["standards_control_association_ids"] = standards_control_association_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_import_findings(
        self,
        findings: "aws_sdk_securityhub.types.batch_import_findings_request_finding_list.BatchImportFindingsRequestFindingList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.batch_import_findings_response.BatchImportFindingsResponse":
        r"""<p>Imports security findings generated by a finding provider into Security Hub CSPM. This action is requested by the finding provider to import its findings into Security Hub CSPM.</p> <p> <code>BatchImportFindings</code> must be called by one of the following:</p> <ul> <li> <p>The Amazon Web Services account that is associated with a finding if you are using the <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-custom-providers.html#securityhub-custom-providers-bfi-reqs\">default product ARN</a> or are a partner sending findings from within a customer's Amazon Web Services account. In these cases, the identifier of the account that you are calling <code>BatchImportFindings</code> from needs to be the same as the <code>AwsAccountId</code> attribute for the finding.</p> </li> <li> <p>An Amazon Web Services account that Security Hub CSPM has allow-listed for an official partner integration. In this case, you can call <code>BatchImportFindings</code> from the allow-listed account and send findings from different customer accounts in the same batch.</p> </li> </ul> <p>The maximum allowed size for a finding is 240 Kb. An error is returned for any finding larger than 240 Kb.</p> <p>After a finding is created, <code>BatchImportFindings</code> cannot be used to update the following finding fields and objects, which Security Hub CSPM customers use to manage their investigation workflow.</p> <ul> <li> <p> <code>Note</code> </p> </li> <li> <p> <code>UserDefinedFields</code> </p> </li> <li> <p> <code>VerificationState</code> </p> </li> <li> <p> <code>Workflow</code> </p> </li> </ul> <p>Finding providers also should not use <code>BatchImportFindings</code> to update the following attributes.</p> <ul> <li> <p> <code>Confidence</code> </p> </li> <li> <p> <code>Criticality</code> </p> </li> <li> <p> <code>RelatedFindings</code> </p> </li> <li> <p> <code>Severity</code> </p> </li> <li> <p> <code>Types</code> </p> </li> </ul> <p>Instead, finding providers use <code>FindingProviderFields</code> to provide values for these attributes.</p>

        Args:
            findings: <p>A list of findings to import. To successfully import a finding, it must follow the <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html\">Amazon Web Services Security Finding Format</a>. Maximum of 100 findings per request.</p>

        Examples:
            To import security findings from a third party provider to Security Hub
            The following example imports findings from a third party provider to Security Hub.

            >>> client.batch_import_findings(findings=[{'AwsAccountId': '123456789012', 'CreatedAt': '2020-05-27T17:05:54.832Z', 'Description': 'Vulnerability in a CloudTrail trail', 'FindingProviderFields': {'Severity': {'Label': 'LOW', 'Original': '10'}, 'Types': ['Software and Configuration Checks/Vulnerabilities/CVE']}, 'GeneratorId': 'TestGeneratorId', 'Id': 'Id1', 'ProductArn': 'arn:aws:securityhub:us-west-1:123456789012:product/123456789012/default', 'Resources': [{'Id': 'arn:aws:cloudtrail:us-west-1:123456789012:trail/TrailName', 'Partition': 'aws', 'Region': 'us-west-1', 'Type': 'AwsCloudTrailTrail'}], 'SchemaVersion': '2018-10-08', 'Title': 'CloudTrail trail vulnerability', 'UpdatedAt': '2020-06-02T16:05:54.832Z'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_import_findings_request.BatchImportFindingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_import_findings_response.BatchImportFindingsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_import_findings

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_import_findings.batch_import_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_import_findings_request.BatchImportFindingsRequest = {}  # type: ignore[typeddict-item]
        input_["findings"] = findings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_automation_rules(
        self,
        update_automation_rules_request_items: "aws_sdk_securityhub.types.update_automation_rules_request_items_list.UpdateAutomationRulesRequestItemsList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.batch_update_automation_rules_response.BatchUpdateAutomationRulesResponse":
        """<p> Updates one or more automation rules based on rule Amazon Resource Names (ARNs) and input parameters. </p>

        Args:
            update_automation_rules_request_items: <p> An array of ARNs for the rules that are to be updated. Optionally, you can also include <code>RuleStatus</code> and <code>RuleOrder</code>. </p>

        Examples:
            To update one ore more automation rules
            The following example updates the specified automation rules.

            >>> client.batch_update_automation_rules(update_automation_rules_request_items=[{'RuleArn': 'arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'RuleStatus': 'ENABLED', 'RuleOrder': 15}, {'RuleArn': 'arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'RuleStatus': 'DISABLED'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_update_automation_rules_request.BatchUpdateAutomationRulesRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_update_automation_rules_response.BatchUpdateAutomationRulesResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_update_automation_rules

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_update_automation_rules.batch_update_automation_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_update_automation_rules_request.BatchUpdateAutomationRulesRequest = {}  # type: ignore[typeddict-item]
        input_["update_automation_rules_request_items"] = (
            update_automation_rules_request_items
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_findings(
        self,
        finding_identifiers: "aws_sdk_securityhub.types.aws_security_finding_identifier_list.AwsSecurityFindingIdentifierList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        note: Optional["aws_sdk_securityhub.types.note_update.NoteUpdate"] = None,
        severity: Optional[
            "aws_sdk_securityhub.types.severity_update.SeverityUpdate"
        ] = None,
        verification_state: Optional[
            "aws_sdk_securityhub.types.verification_state.VerificationState"
        ] = None,
        confidence: Optional["aws_sdk_securityhub.types.ratio_scale.RatioScale"] = None,
        criticality: Optional[
            "aws_sdk_securityhub.types.ratio_scale.RatioScale"
        ] = None,
        types: Optional["aws_sdk_securityhub.types.type_list.TypeList"] = None,
        user_defined_fields: Optional[
            "aws_sdk_securityhub.types.field_map.FieldMap"
        ] = None,
        workflow: Optional[
            "aws_sdk_securityhub.types.workflow_update.WorkflowUpdate"
        ] = None,
        related_findings: Optional[
            "aws_sdk_securityhub.types.related_finding_list.RelatedFindingList"
        ] = None,
    ) -> "aws_sdk_securityhub.types.batch_update_findings_response.BatchUpdateFindingsResponse":
        r"""<p> Used by Security Hub CSPM customers to update information about their investigation into one or more findings. Requested by administrator accounts or member accounts. Administrator accounts can update findings for their account and their member accounts. A member account can update findings only for their own account. Administrator and member accounts can use this operation to update the following fields and objects for one or more findings: </p> <ul> <li> <p> <code>Confidence</code> </p> </li> <li> <p> <code>Criticality</code> </p> </li> <li> <p> <code>Note</code> </p> </li> <li> <p> <code>RelatedFindings</code> </p> </li> <li> <p> <code>Severity</code> </p> </li> <li> <p> <code>Types</code> </p> </li> <li> <p> <code>UserDefinedFields</code> </p> </li> <li> <p> <code>VerificationState</code> </p> </li> <li> <p> <code>Workflow</code> </p> </li> </ul> <p> If you use this operation to update a finding, your updates don’t affect the value for the <code>UpdatedAt</code> field of the finding. Also note that it can take several minutes for Security Hub CSPM to process your request and update each finding specified in the request. </p> <p> You can configure IAM policies to restrict access to fields and field values. For example, you might not want member accounts to be able to suppress findings or change the finding severity. For more information see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/finding-update-batchupdatefindings.html#batchupdatefindings-configure-access\">Configuring access to BatchUpdateFindings</a> in the <i>Security Hub CSPM User Guide</i>. </p>

        Args:
            finding_identifiers: <p>The list of findings to update. <code>BatchUpdateFindings</code> can be used to update up to 100 findings at a time.</p> <p>For each finding, the list provides the finding identifier and the ARN of the finding provider.</p>
            severity: <p>Used to update the finding severity.</p>
            verification_state: <p>Indicates the veracity of a finding.</p> <p>The available values for <code>VerificationState</code> are as follows.</p> <ul> <li> <p> <code>UNKNOWN</code> – The default disposition of a security finding</p> </li> <li> <p> <code>TRUE_POSITIVE</code> – The security finding is confirmed</p> </li> <li> <p> <code>FALSE_POSITIVE</code> – The security finding was determined to be a false alarm</p> </li> <li> <p> <code>BENIGN_POSITIVE</code> – A special case of <code>TRUE_POSITIVE</code> where the finding doesn't pose any threat, is expected, or both</p> </li> </ul>
            confidence: <p>The updated value for the finding confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.</p> <p>Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.</p>
            criticality: <p>The updated value for the level of importance assigned to the resources associated with the findings.</p> <p>A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources. </p>
            types: <p>One or more finding types in the format of namespace/category/classifier that classify a finding.</p> <p>Valid namespace values are as follows.</p> <ul> <li> <p>Software and Configuration Checks</p> </li> <li> <p>TTPs</p> </li> <li> <p>Effects</p> </li> <li> <p>Unusual Behaviors</p> </li> <li> <p>Sensitive Data Identifications </p> </li> </ul>
            user_defined_fields: <p>A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.</p>
            workflow: <p>Used to update the workflow status of a finding.</p> <p>The workflow status indicates the progress of the investigation into the finding. </p>
            related_findings: <p>A list of findings that are related to the updated findings.</p>

        Examples:
            To update Security Hub findings
            The following example updates Security Hub findings. The finding identifier parameter specifies which findings to update. Only specific finding fields can be updated with this operation.

            >>> client.batch_update_findings(finding_identifiers=[{'Id': 'arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'ProductArn': 'arn:aws:securityhub:us-west-1::product/aws/securityhub'}, {'Id': 'arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'ProductArn': 'arn:aws:securityhub:us-west-1::product/aws/securityhub'}], note={'Text': 'Known issue that is not a risk.', 'UpdatedBy': 'user1'}, severity={'Label': 'LOW'}, verification_state='TRUE_POSITIVE', confidence=80, criticality=80, types=['Software and Configuration Checks/Vulnerabilities/CVE'], user_defined_fields={'reviewedByCio': 'true'}, workflow={'Status': 'RESOLVED'}, related_findings=[{'Id': 'arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333', 'ProductArn': 'arn:aws:securityhub:us-west-1::product/aws/securityhub'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_update_findings_request.BatchUpdateFindingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_update_findings_response.BatchUpdateFindingsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_update_findings

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_update_findings.batch_update_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_update_findings_request.BatchUpdateFindingsRequest = {}  # type: ignore[typeddict-item]
        input_["finding_identifiers"] = finding_identifiers
        if note is not None:
            input_["note"] = note
        if severity is not None:
            input_["severity"] = severity
        if verification_state is not None:
            input_["verification_state"] = verification_state
        if confidence is not None:
            input_["confidence"] = confidence
        if criticality is not None:
            input_["criticality"] = criticality
        if types is not None:
            input_["types"] = types
        if user_defined_fields is not None:
            input_["user_defined_fields"] = user_defined_fields
        if workflow is not None:
            input_["workflow"] = workflow
        if related_findings is not None:
            input_["related_findings"] = related_findings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_findings_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        metadata_uids: Optional[
            "aws_sdk_securityhub.types.metadata_uid_list.MetadataUidList"
        ] = None,
        finding_identifiers: Optional[
            "aws_sdk_securityhub.types.ocsf_finding_identifier_list.OcsfFindingIdentifierList"
        ] = None,
        comment: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        severity_id: Optional["aws_sdk_securityhub.types.integer.Integer"] = None,
        status_id: Optional["aws_sdk_securityhub.types.integer.Integer"] = None,
    ) -> "aws_sdk_securityhub.types.batch_update_findings_v2_response.BatchUpdateFindingsV2Response":
        r"""<p>Updates information about a customer's investigation into a finding. Delegated administrator accounts can update findings for their account and their member accounts. Member accounts can update findings for their own account.</p> <p> <code>BatchUpdateFindings</code> and <code>BatchUpdateFindingsV2</code> both use <code>securityhub:BatchUpdateFindings</code> in the <code>Action</code> element of an IAM policy statement. You must have permission to perform the <code>securityhub:BatchUpdateFindings</code> action. You can configure IAM policies to restrict access to specific finding fields or field values by using the <code>securityhub:OCSFSyntaxPath/<fieldName></code> condition key, where <code><fieldName></code> is one of the following supported fields: <code>SeverityId</code>, <code>StatusId</code>, or <code>Comment</code>.</p> <p>To prevent a user from updating a specific field, use a <code>Null</code> condition with <code>securityhub:OCSFSyntaxPath/<fieldName></code> set to <code>\"false\"</code>. To prevent a user from setting a field to a specific value, use a <code>StringEquals</code> condition with <code>securityhub:OCSFSyntaxPath/<fieldName></code> set to the disallowed value or list of values.</p> <p>Updates from <code>BatchUpdateFindingsV2</code> don't affect the value of <code>finding_info.modified_time</code>, <code>finding_info.modified_time_dt</code>, <code>time</code>, or <code>time_dt</code> for a finding.</p>

        Args:
            metadata_uids: <p>The list of finding <code>metadata.uid</code> to indicate findings to update. Finding <code>metadata.uid</code> is a globally unique identifier associated with the finding. Customers cannot use <code>MetadataUids</code> together with <code>FindingIdentifiers</code>.</p>
            finding_identifiers: <p>Provides information to identify a specific V2 finding.</p>
            comment: <p>The updated value for a user provided comment about the finding. Minimum character length 1. Maximum character length 512.</p>
            severity_id: <p>The updated value for the normalized severity identifier. The severity ID is an integer with the allowed enum values [0, 1, 2, 3, 4, 5, 6, 99]. When customer provides the updated severity ID, the string sibling severity will automatically be updated in the finding.</p>
            status_id: <p>The updated value for the normalized status identifier. The status ID is an integer with the allowed enum values [0, 1, 2, 3, 4, 5, 99]. When customer provides the updated status ID, the string sibling status will automatically be updated in the finding.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_update_findings_v2_request.BatchUpdateFindingsV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_update_findings_v2_response.BatchUpdateFindingsV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_update_findings_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_update_findings_v2.batch_update_findings_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_update_findings_v2_request.BatchUpdateFindingsV2Request = {}  # type: ignore[typeddict-item]
        if metadata_uids is not None:
            input_["metadata_uids"] = metadata_uids
        if finding_identifiers is not None:
            input_["finding_identifiers"] = finding_identifiers
        if comment is not None:
            input_["comment"] = comment
        if severity_id is not None:
            input_["severity_id"] = severity_id
        if status_id is not None:
            input_["status_id"] = status_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_standards_control_associations(
        self,
        standards_control_association_updates: "aws_sdk_securityhub.types.standards_control_association_updates.StandardsControlAssociationUpdates",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.batch_update_standards_control_associations_response.BatchUpdateStandardsControlAssociationsResponse":
        """<p> For a batch of security controls and standards, this operation updates the enablement status of a control in a standard. </p>

        Args:
            standards_control_association_updates: <p> Updates the enablement status of a security control in a specified standard. </p> <p> Calls to this operation return a <code>RESOURCE_NOT_FOUND_EXCEPTION</code> error when the standard subscription for the control has <code>StandardsControlsUpdatable</code> value <code>NOT_READY_FOR_UPDATES</code>. </p>

        Examples:
            To update enablement status of a batch of controls
            The following example disables CloudWatch.12 in CIS AWS Foundations Benchmark v1.2.0. The example returns an error for CloudTrail.1 because an invalid standard ARN is provided.

            >>> client.batch_update_standards_control_associations(standards_control_association_updates=[{'SecurityControlId': 'CloudTrail.1', 'StandardsArn': 'arn:aws:securityhub:::ruleset/sample-standard/v/1.1.0', 'AssociationStatus': 'DISABLED', 'UpdatedReason': 'Not relevant to environment'}, {'SecurityControlId': 'CloudWatch.12', 'StandardsArn': 'arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0', 'AssociationStatus': 'DISABLED', 'UpdatedReason': 'Not relevant to environment'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.batch_update_standards_control_associations_request.BatchUpdateStandardsControlAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.batch_update_standards_control_associations_response.BatchUpdateStandardsControlAssociationsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.batch_update_standards_control_associations

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.batch_update_standards_control_associations.batch_update_standards_control_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.batch_update_standards_control_associations_request.BatchUpdateStandardsControlAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["standards_control_association_updates"] = (
            standards_control_association_updates
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_action_target(
        self,
        name: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        description: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.create_action_target_response.CreateActionTargetResponse":
        """<p>Creates a custom action target in Security Hub CSPM.</p> <p>You can use custom actions on findings and insights in Security Hub CSPM to trigger target actions in Amazon CloudWatch Events.</p>

        Args:
            name: <p>The name of the custom action target. Can contain up to 20 characters.</p>
            description: <p>The description for the custom action target.</p>
            id: <p>The ID for the custom action target. Can contain up to 20 alphanumeric characters.</p>

        Examples:
            To create a custom action target
            The following example creates a custom action target in Security Hub. Custom actions on findings and insights automatically trigger actions in Amazon CloudWatch Events.

            >>> client.create_action_target(name='Send to remediation', description='Action to send the finding for remediation tracking', id='Remediation')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.create_action_target_request.CreateActionTargetRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.create_action_target_response.CreateActionTargetResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.create_action_target

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.create_action_target.create_action_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.create_action_target_request.CreateActionTargetRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["description"] = description
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_aggregator_v2(
        self,
        region_linking_mode: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        linked_regions: Optional[
            "aws_sdk_securityhub.types.string_list.StringList"
        ] = None,
        tags: Optional["aws_sdk_securityhub.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_securityhub.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_securityhub.types.create_aggregator_v2_response.CreateAggregatorV2Response":
        """<p>Enables aggregation across Amazon Web Services Regions.</p>

        Args:
            region_linking_mode: <p>Determines how Regions are linked to an Aggregator V2.</p>
            linked_regions: <p>The list of Regions that are linked to the aggregation Region.</p>
            tags: <p>A list of key-value pairs to be applied to the AggregatorV2.</p>
            client_token: <p>A unique identifier used to ensure idempotency.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.create_aggregator_v2_request.CreateAggregatorV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.create_aggregator_v2_response.CreateAggregatorV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.create_aggregator_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.create_aggregator_v2.create_aggregator_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.create_aggregator_v2_request.CreateAggregatorV2Request = {}  # type: ignore[typeddict-item]
        input_["region_linking_mode"] = region_linking_mode
        if linked_regions is not None:
            input_["linked_regions"] = linked_regions
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_automation_rule(
        self,
        rule_order: "aws_sdk_securityhub.types.rule_order_value.RuleOrderValue",
        rule_name: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        description: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        criteria: "aws_sdk_securityhub.types.automation_rules_finding_filters.AutomationRulesFindingFilters",
        actions: "aws_sdk_securityhub.types.action_list.ActionList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        tags: Optional["aws_sdk_securityhub.types.tag_map.TagMap"] = None,
        rule_status: Optional[
            "aws_sdk_securityhub.types.rule_status.RuleStatus"
        ] = None,
        is_terminal: Optional["aws_sdk_securityhub.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_securityhub.types.create_automation_rule_response.CreateAutomationRuleResponse":
        r"""<p> Creates an automation rule based on input parameters. </p>

        Args:
            tags: <p> User-defined tags associated with an automation rule. </p>
            rule_status: <p> Whether the rule is active after it is created. If this parameter is equal to <code>ENABLED</code>, Security Hub CSPM starts applying the rule to findings and finding updates after the rule is created. To change the value of this parameter after creating a rule, use <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateAutomationRules.html\"> <code>BatchUpdateAutomationRules</code> </a>. </p>
            rule_order: <p>An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub CSPM applies rules with lower values for this parameter first. </p>
            rule_name: <p> The name of the rule. </p>
            description: <p> A description of the rule. </p>
            is_terminal: <p>Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub CSPM applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal. </p>
            criteria: <p> A set of ASFF finding field attributes and corresponding expected values that Security Hub CSPM uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub CSPM applies the rule action to the finding. </p>
            actions: <p> One or more actions to update finding fields if a finding matches the conditions specified in <code>Criteria</code>. </p>

        Examples:
            To create an automation rule
            The following example creates an automation rule.

            >>> client.create_automation_rule(tags={'important-resources-rule': 's3-bucket'}, rule_status='ENABLED', rule_order=1, rule_name='Elevate severity for important resources', description='Elevate finding severity to Critical for important resources', is_terminal=False, criteria={'ProductName': [{'Value': 'Security Hub', 'Comparison': 'EQUALS'}], 'ComplianceStatus': [{'Value': 'FAILED', 'Comparison': 'EQUALS'}], 'RecordState': [{'Value': 'ACTIVE', 'Comparison': 'EQUALS'}], 'WorkflowStatus': [{'Value': 'NEW', 'Comparison': 'EQUALS'}], 'ResourceId': [{'Value': 'arn:aws:s3:::examplebucket/developers/design_info.doc', 'Comparison': 'EQUALS'}]}, actions=[{'Type': 'FINDING_FIELDS_UPDATE', 'FindingFieldsUpdate': {'Severity': {'Label': 'CRITICAL'}, 'Note': {'Text': 'This is a critical S3 bucket, please look into this ASAP', 'UpdatedBy': 'test-user'}}}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.create_automation_rule_request.CreateAutomationRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.create_automation_rule_response.CreateAutomationRuleResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.create_automation_rule

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.create_automation_rule.create_automation_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.create_automation_rule_request.CreateAutomationRuleRequest = {}  # type: ignore[typeddict-item]
        if tags is not None:
            input_["tags"] = tags
        if rule_status is not None:
            input_["rule_status"] = rule_status
        input_["rule_order"] = rule_order
        input_["rule_name"] = rule_name
        input_["description"] = description
        if is_terminal is not None:
            input_["is_terminal"] = is_terminal
        input_["criteria"] = criteria
        input_["actions"] = actions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_automation_rule_v2(
        self,
        rule_name: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        description: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        rule_order: "aws_sdk_securityhub.types.rule_order_value_v2.RuleOrderValueV2",
        criteria: "aws_sdk_securityhub.types.criteria.Criteria",
        actions: "aws_sdk_securityhub.types.automation_rules_action_list_v2.AutomationRulesActionListV2",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        rule_status: Optional[
            "aws_sdk_securityhub.types.rule_status_v2.RuleStatusV2"
        ] = None,
        tags: Optional["aws_sdk_securityhub.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_securityhub.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_securityhub.types.create_automation_rule_v2_response.CreateAutomationRuleV2Response":
        """<p>Creates a V2 automation rule.</p>

        Args:
            rule_name: <p>The name of the V2 automation rule.</p>
            rule_status: <p>The status of the V2 automation rule.</p>
            description: <p>A description of the V2 automation rule.</p>
            rule_order: <p>The value for the rule priority.</p>
            criteria: <p>The filtering type and configuration of the automation rule.</p>
            actions: <p>A list of actions to be performed when the rule criteria is met.</p>
            tags: <p>A list of key-value pairs associated with the V2 automation rule.</p>
            client_token: <p>A unique identifier used to ensure idempotency.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.create_automation_rule_v2_request.CreateAutomationRuleV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.create_automation_rule_v2_response.CreateAutomationRuleV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.create_automation_rule_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.create_automation_rule_v2.create_automation_rule_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.create_automation_rule_v2_request.CreateAutomationRuleV2Request = {}  # type: ignore[typeddict-item]
        input_["rule_name"] = rule_name
        if rule_status is not None:
            input_["rule_status"] = rule_status
        input_["description"] = description
        input_["rule_order"] = rule_order
        input_["criteria"] = criteria
        input_["actions"] = actions
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_configuration_policy(
        self,
        name: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        configuration_policy: "aws_sdk_securityhub.types.policy.Policy",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        description: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["aws_sdk_securityhub.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_securityhub.types.create_configuration_policy_response.CreateConfigurationPolicyResponse":
        r"""<p> Creates a configuration policy with the defined configuration. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            name: <p> The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: <code>-, ., !, *, /</code>. </p>
            description: <p> The description of the configuration policy. </p>
            configuration_policy: <p> An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls). </p>
            tags: <p> User-defined tags associated with a configuration policy. For more information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/tagging-resources.html\">Tagging Security Hub CSPM resources</a> in the <i>Security Hub CSPM user guide</i>. </p>

        Examples:
            To create a configuration policy
            This operation creates a configuration policy in Security Hub.

            >>> client.create_configuration_policy(name='TestConfigurationPolicy', description='Configuration policy for testing FSBP and CIS', configuration_policy={'SecurityHub': {'ServiceEnabled': True, 'EnabledStandardIdentifiers': ['arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0', 'arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0'], 'SecurityControlsConfiguration': {'DisabledSecurityControlIdentifiers': ['CloudWatch.1'], 'SecurityControlCustomParameters': [{'SecurityControlId': 'ACM.1', 'Parameters': {'daysToExpiration': {'ValueType': 'CUSTOM', 'Value': {'Integer': 14}}}}]}}})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.create_configuration_policy_request.CreateConfigurationPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.create_configuration_policy_response.CreateConfigurationPolicyResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.create_configuration_policy

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.create_configuration_policy.create_configuration_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.create_configuration_policy_request.CreateConfigurationPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["configuration_policy"] = configuration_policy
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_connector_v2(
        self,
        name: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        provider: "aws_sdk_securityhub.types.provider_configuration.ProviderConfiguration",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        description: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        kms_key_arn: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["aws_sdk_securityhub.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_securityhub.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_securityhub.types.create_connector_v2_response.CreateConnectorV2Response":
        """<p>Grants permission to create a connectorV2 based on input parameters.</p>

        Args:
            name: <p>The unique name of the connectorV2.</p>
            description: <p>The description of the connectorV2.</p>
            provider: <p>The third-party provider’s service configuration.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of KMS key used to encrypt secrets for the connectorV2.</p>
            tags: <p>The tags to add to the connectorV2 when you create.</p>
            client_token: <p>A unique identifier used to ensure idempotency.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.create_connector_v2_request.CreateConnectorV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.create_connector_v2_response.CreateConnectorV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.create_connector_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.create_connector_v2.create_connector_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.create_connector_v2_request.CreateConnectorV2Request = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["provider"] = provider
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_finding_aggregator(
        self,
        region_linking_mode: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        regions: Optional["aws_sdk_securityhub.types.string_list.StringList"] = None,
    ) -> "aws_sdk_securityhub.types.create_finding_aggregator_response.CreateFindingAggregatorResponse":
        r"""<note> <p>The <i>aggregation Region</i> is now called the <i>home Region</i>.</p> </note> <p>Used to enable cross-Region aggregation. This operation can be invoked from the home Region only.</p> <p>For information about how cross-Region aggregation works, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html\">Understanding cross-Region aggregation in Security Hub CSPM</a> in the <i>Security Hub CSPM User Guide</i>. </p>

        Args:
            region_linking_mode: <p>Indicates whether to aggregate findings from all of the available Regions in the current partition. Also determines whether to automatically aggregate findings from new Regions as Security Hub CSPM supports them and you opt into them.</p> <p>The selected option also determines how to use the Regions provided in the Regions list.</p> <p>The options are as follows:</p> <ul> <li> <p> <code>ALL_REGIONS</code> - Aggregates findings from all of the Regions where Security Hub CSPM is enabled. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them. </p> </li> <li> <p> <code>ALL_REGIONS_EXCEPT_SPECIFIED</code> - Aggregates findings from all of the Regions where Security Hub CSPM is enabled, except for the Regions listed in the <code>Regions</code> parameter. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them. </p> </li> <li> <p> <code>SPECIFIED_REGIONS</code> - Aggregates findings only from the Regions listed in the <code>Regions</code> parameter. Security Hub CSPM does not automatically aggregate findings from new Regions. </p> </li> <li> <p> <code>NO_REGIONS</code> - Aggregates no data because no Regions are selected as linked Regions. </p> </li> </ul>
            regions: <p>If <code>RegionLinkingMode</code> is <code>ALL_REGIONS_EXCEPT_SPECIFIED</code>, then this is a space-separated list of Regions that don't replicate and send findings to the home Region.</p> <p>If <code>RegionLinkingMode</code> is <code>SPECIFIED_REGIONS</code>, then this is a space-separated list of Regions that do replicate and send findings to the home Region. </p> <p>An <code>InvalidInputException</code> error results if you populate this field while <code>RegionLinkingMode</code> is <code>NO_REGIONS</code>.</p>

        Examples:
            To enable cross-Region aggregation
            The following example creates a finding aggregator. This is required to enable cross-Region aggregation.

            >>> client.create_finding_aggregator(region_linking_mode='SPECIFIED_REGIONS', regions=['us-west-1', 'us-west-2'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.create_finding_aggregator_request.CreateFindingAggregatorRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.create_finding_aggregator_response.CreateFindingAggregatorResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.create_finding_aggregator

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.create_finding_aggregator.create_finding_aggregator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.create_finding_aggregator_request.CreateFindingAggregatorRequest = {}  # type: ignore[typeddict-item]
        input_["region_linking_mode"] = region_linking_mode
        if regions is not None:
            input_["regions"] = regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_insight(
        self,
        name: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        filters: "aws_sdk_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters",
        group_by_attribute: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.create_insight_response.CreateInsightResponse":
        """<p>Creates a custom insight in Security Hub CSPM. An insight is a consolidation of findings that relate to a security issue that requires attention or remediation.</p> <p>To group the related findings in the insight, use the <code>GroupByAttribute</code>.</p>

        Args:
            name: <p>The name of the custom insight to create.</p>
            filters: <p>One or more attributes used to filter the findings included in the insight. The insight only includes findings that match the criteria defined in the filters.</p>
            group_by_attribute: <p>The attribute used to group the findings for the insight. The grouping attribute identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.</p>

        Examples:
            To create a custom insight
            The following example creates a custom insight in Security Hub. An insight is a collection of findings that relate to a security issue.

            >>> client.create_insight(name='Critical role findings', filters={'ResourceType': [{'Comparison': 'EQUALS', 'Value': 'AwsIamRole'}], 'SeverityLabel': [{'Comparison': 'EQUALS', 'Value': 'CRITICAL'}]}, group_by_attribute='ResourceId')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.create_insight_request.CreateInsightRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.create_insight_response.CreateInsightResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.create_insight

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.create_insight.create_insight(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.create_insight_request.CreateInsightRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["filters"] = filters
        input_["group_by_attribute"] = group_by_attribute

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_members(
        self,
        account_details: "aws_sdk_securityhub.types.account_details_list.AccountDetailsList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.create_members_response.CreateMembersResponse":
        """<p>Creates a member association in Security Hub CSPM between the specified accounts and the account used to make the request, which is the administrator account. If you are integrated with Organizations, then the administrator account is designated by the organization management account.</p> <p> <code>CreateMembers</code> is always used to add accounts that are not organization members.</p> <p>For accounts that are managed using Organizations, <code>CreateMembers</code> is only used in the following cases:</p> <ul> <li> <p>Security Hub CSPM is not configured to automatically add new organization accounts.</p> </li> <li> <p>The account was disassociated or deleted in Security Hub CSPM.</p> </li> </ul> <p>This action can only be used by an account that has Security Hub CSPM enabled. To enable Security Hub CSPM, you can use the <code>EnableSecurityHub</code> operation.</p> <p>For accounts that are not organization members, you create the account association and then send an invitation to the member account. To send the invitation, you use the <code>InviteMembers</code> operation. If the account owner accepts the invitation, the account becomes a member account in Security Hub CSPM.</p> <p>Accounts that are managed using Organizations don't receive an invitation. They automatically become a member account in Security Hub CSPM.</p> <ul> <li> <p>If the organization account does not have Security Hub CSPM enabled, then Security Hub CSPM and the default standards are automatically enabled. Note that Security Hub CSPM cannot be enabled automatically for the organization management account. The organization management account must enable Security Hub CSPM before the administrator account enables it as a member account.</p> </li> <li> <p>For organization accounts that already have Security Hub CSPM enabled, Security Hub CSPM does not make any other changes to those accounts. It does not change their enabled standards or controls.</p> </li> </ul> <p>A permissions policy is added that permits the administrator account to view the findings generated in the member account.</p> <p>To remove the association between the administrator and member accounts, use the <code>DisassociateFromMasterAccount</code> or <code>DisassociateMembers</code> operation.</p>

        Args:
            account_details: <p>The list of accounts to associate with the Security Hub CSPM administrator account. For each account, the list includes the account ID and optionally the email address.</p>

        Examples:
            To add a member account
            The following example creates a member association between the specified accounts and the administrator account (the account that makes the request). This operation is used to add accounts that aren't part of an organization.

            >>> client.create_members(account_details=[{'AccountId': '123456789012'}, {'AccountId': '111122223333'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.create_members_request.CreateMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.create_members_response.CreateMembersResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.create_members

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.create_members.create_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.create_members_request.CreateMembersRequest = {}  # type: ignore[typeddict-item]
        input_["account_details"] = account_details

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_ticket_v2(
        self,
        connector_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        finding_metadata_uid: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        client_token: Optional[
            "aws_sdk_securityhub.types.client_token.ClientToken"
        ] = None,
        mode: Optional[
            "aws_sdk_securityhub.types.ticket_creation_mode.TicketCreationMode"
        ] = None,
    ) -> "aws_sdk_securityhub.types.create_ticket_v2_response.CreateTicketV2Response":
        """<p>Grants permission to create a ticket in the chosen ITSM based on finding information for the provided finding metadata UID.</p>

        Args:
            connector_id: <p>The UUID of the connectorV2 to identify connectorV2 resource.</p>
            finding_metadata_uid: <p>The the unique ID for the finding.</p>
            client_token: <p>The client idempotency token.</p>
            mode: <p>The mode for ticket creation. When set to DRYRUN, the ticket is created using a Security Hub owned template test finding to verify the integration is working correctly.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.create_ticket_v2_request.CreateTicketV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.create_ticket_v2_response.CreateTicketV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.create_ticket_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.create_ticket_v2.create_ticket_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.create_ticket_v2_request.CreateTicketV2Request = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id
        input_["finding_metadata_uid"] = finding_metadata_uid
        if client_token is not None:
            input_["client_token"] = client_token
        if mode is not None:
            input_["mode"] = mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def decline_invitations(
        self,
        account_ids: "aws_sdk_securityhub.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.decline_invitations_response.DeclineInvitationsResponse":
        r"""<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html\">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Declines invitations to become a Security Hub CSPM member account.</p> <p>A prospective member account uses this operation to decline an invitation to become a member.</p> <p>Only member accounts that aren't part of an Amazon Web Services organization should use this operation. Organization accounts don't receive invitations.</p>

        Args:
            account_ids: <p>The list of prospective member account IDs for which to decline an invitation.</p>

        Examples:
            To decline invitation to become a member account
            The following example declines an invitation from the Security Hub administrator account to become a member account. The invited account makes the request.

            >>> client.decline_invitations(account_ids=['123456789012', '111122223333'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.decline_invitations_request.DeclineInvitationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.decline_invitations_response.DeclineInvitationsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.decline_invitations

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.decline_invitations.decline_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.decline_invitations_request.DeclineInvitationsRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_action_target(
        self,
        action_target_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.delete_action_target_response.DeleteActionTargetResponse":
        """<p>Deletes a custom action target from Security Hub CSPM.</p> <p>Deleting a custom action target does not affect any findings or insights that were already sent to Amazon CloudWatch Events using the custom action.</p>

        Args:
            action_target_arn: <p>The Amazon Resource Name (ARN) of the custom action target to delete.</p>

        Examples:
            To delete a custom action target
            The following example deletes a custom action target that triggers target actions in Amazon CloudWatch Events. Deleting a custom action target doesn't affect findings or insights that were already sent to CloudWatch Events based on the custom action.

            >>> client.delete_action_target(action_target_arn='arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.delete_action_target_request.DeleteActionTargetRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.delete_action_target_response.DeleteActionTargetResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.delete_action_target

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.delete_action_target.delete_action_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.delete_action_target_request.DeleteActionTargetRequest = {}  # type: ignore[typeddict-item]
        input_["action_target_arn"] = action_target_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_aggregator_v2(
        self,
        aggregator_v2_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.delete_aggregator_v2_response.DeleteAggregatorV2Response":
        """<p>Deletes the Aggregator V2.</p>

        Args:
            aggregator_v2_arn: <p>The ARN of the Aggregator V2.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.delete_aggregator_v2_request.DeleteAggregatorV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.delete_aggregator_v2_response.DeleteAggregatorV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.delete_aggregator_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.delete_aggregator_v2.delete_aggregator_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.delete_aggregator_v2_request.DeleteAggregatorV2Request = {}  # type: ignore[typeddict-item]
        input_["aggregator_v2_arn"] = aggregator_v2_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_automation_rule_v2(
        self,
        identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.delete_automation_rule_v2_response.DeleteAutomationRuleV2Response":
        """<p>Deletes a V2 automation rule.</p>

        Args:
            identifier: <p>The ARN of the V2 automation rule.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.delete_automation_rule_v2_request.DeleteAutomationRuleV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.delete_automation_rule_v2_response.DeleteAutomationRuleV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.delete_automation_rule_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.delete_automation_rule_v2.delete_automation_rule_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.delete_automation_rule_v2_request.DeleteAutomationRuleV2Request = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_configuration_policy(
        self,
        identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.delete_configuration_policy_response.DeleteConfigurationPolicyResponse":
        """<p> Deletes a configuration policy. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. For the deletion to succeed, you must first disassociate a configuration policy from target accounts, organizational units, or the root by invoking the <code>StartConfigurationPolicyDisassociation</code> operation. </p>

        Args:
            identifier: <p> The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy. </p>

        Examples:
            To delete a configuration policy
            This operation deletes the specified configuration policy.

            >>> client.delete_configuration_policy(identifier='arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.delete_configuration_policy_request.DeleteConfigurationPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.delete_configuration_policy_response.DeleteConfigurationPolicyResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.delete_configuration_policy

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.delete_configuration_policy.delete_configuration_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.delete_configuration_policy_request.DeleteConfigurationPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_connector_v2(
        self,
        connector_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.delete_connector_v2_response.DeleteConnectorV2Response":
        """<p>Grants permission to delete a connectorV2.</p>

        Args:
            connector_id: <p>The UUID of the connectorV2 to identify connectorV2 resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.delete_connector_v2_request.DeleteConnectorV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.delete_connector_v2_response.DeleteConnectorV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.delete_connector_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.delete_connector_v2.delete_connector_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.delete_connector_v2_request.DeleteConnectorV2Request = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_finding_aggregator(
        self,
        finding_aggregator_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.delete_finding_aggregator_response.DeleteFindingAggregatorResponse":
        """<note> <p>The <i>aggregation Region</i> is now called the <i>home Region</i>.</p> </note> <p>Deletes a finding aggregator. When you delete the finding aggregator, you stop cross-Region aggregation. Finding replication stops occurring from the linked Regions to the home Region.</p> <p>When you stop cross-Region aggregation, findings that were already replicated and sent to the home Region are still visible from the home Region. However, new findings and finding updates are no longer replicated and sent to the home Region. </p>

        Args:
            finding_aggregator_arn: <p>The ARN of the finding aggregator to delete. To obtain the ARN, use <code>ListFindingAggregators</code>.</p>

        Examples:
            To delete a finding aggregator
            The following example deletes a finding aggregator in Security Hub. Deleting the finding aggregator stops cross-Region aggregation. This operation produces no output.

            >>> client.delete_finding_aggregator(finding_aggregator_arn='arn:aws:securityhub:us-east-1:123456789012:finding-aggregator/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.delete_finding_aggregator_request.DeleteFindingAggregatorRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.delete_finding_aggregator_response.DeleteFindingAggregatorResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.delete_finding_aggregator

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.delete_finding_aggregator.delete_finding_aggregator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.delete_finding_aggregator_request.DeleteFindingAggregatorRequest = {}  # type: ignore[typeddict-item]
        input_["finding_aggregator_arn"] = finding_aggregator_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_insight(
        self,
        insight_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.delete_insight_response.DeleteInsightResponse":
        """<p>Deletes the insight specified by the <code>InsightArn</code>.</p>

        Args:
            insight_arn: <p>The ARN of the insight to delete.</p>

        Examples:
            To delete a custom insight
            The following example deletes a custom insight in Security Hub.

            >>> client.delete_insight(insight_arn='arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.delete_insight_request.DeleteInsightRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.delete_insight_response.DeleteInsightResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.delete_insight

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.delete_insight.delete_insight(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.delete_insight_request.DeleteInsightRequest = {}  # type: ignore[typeddict-item]
        input_["insight_arn"] = insight_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_invitations(
        self,
        account_ids: "aws_sdk_securityhub.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.delete_invitations_response.DeleteInvitationsResponse":
        r"""<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html\">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Deletes invitations to become a Security Hub CSPM member account.</p> <p>A Security Hub CSPM administrator account can use this operation to delete invitations sent to one or more prospective member accounts.</p> <p>This operation is only used to delete invitations that are sent to prospective member accounts that aren't part of an Amazon Web Services organization. Organization accounts don't receive invitations.</p>

        Args:
            account_ids: <p>The list of member account IDs that received the invitations you want to delete.</p>

        Examples:
            To delete a custom insight
            The following example deletes an invitation sent by the Security Hub administrator account to a prospective member account. This operation is used only for invitations sent to accounts that aren't part of an organization. Organization accounts don't receive invitations.

            >>> client.delete_invitations(account_ids=['123456789012'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.delete_invitations_request.DeleteInvitationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.delete_invitations_response.DeleteInvitationsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.delete_invitations

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.delete_invitations.delete_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.delete_invitations_request.DeleteInvitationsRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_members(
        self,
        account_ids: "aws_sdk_securityhub.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.delete_members_response.DeleteMembersResponse":
        """<p>Deletes the specified member accounts from Security Hub CSPM.</p> <p>You can invoke this API only to delete accounts that became members through invitation. You can't invoke this API to delete accounts that belong to an Organizations organization.</p>

        Args:
            account_ids: <p>The list of account IDs for the member accounts to delete.</p>

        Examples:
            To delete a member account
            The following example deletes the specified member account from Security Hub. This operation can be used to delete member accounts that are part of an organization or that were invited manually.

            >>> client.delete_members(account_ids=['123456789111', '123456789222'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.delete_members_request.DeleteMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.delete_members_response.DeleteMembersResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.delete_members

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.delete_members.delete_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.delete_members_request.DeleteMembersRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_action_targets(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        action_target_arns: Optional[
            "aws_sdk_securityhub.types.arn_list.ArnList"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.describe_action_targets_response.DescribeActionTargetsResponse":
        """<p>Returns a list of the custom action targets in Security Hub CSPM in your account.</p>

        Args:
            action_target_arns: <p>A list of custom action target ARNs for the custom action targets to retrieve.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>DescribeActionTargets</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>

        Examples:
            To return custom action targets
            The following example returns a list of custom action targets. You use custom actions on findings and insights in Security Hub to trigger target actions in Amazon CloudWatch Events.

            >>> client.describe_action_targets(action_target_arns=['arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.describe_action_targets_request.DescribeActionTargetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.describe_action_targets_response.DescribeActionTargetsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.describe_action_targets

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.describe_action_targets.describe_action_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.describe_action_targets_request.DescribeActionTargetsRequest = {}  # type: ignore[typeddict-item]
        if action_target_arns is not None:
            input_["action_target_arns"] = action_target_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_action_targets(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        action_target_arns: Optional[
            "aws_sdk_securityhub.types.arn_list.ArnList"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.action_target.ActionTarget]":
        _token = next_token
        while True:
            _response = self.describe_action_targets(
                config_overrides=config_overrides,
                action_target_arns=action_target_arns,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("action_targets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_hub(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        hub_arn: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "aws_sdk_securityhub.types.describe_hub_response.DescribeHubResponse":
        """<p>Returns details about the Hub resource in your account, including the <code>HubArn</code> and the time when you enabled Security Hub CSPM.</p>

        Args:
            hub_arn: <p>The ARN of the Hub resource to retrieve.</p>

        Examples:
            To return details about Hub resource
            The following example returns details about the Hub resource in the calling account. The Hub resource represents the implementation of  the AWS Security Hub service in the calling account.

            >>> client.describe_hub(hub_arn='arn:aws:securityhub:us-west-1:123456789012:hub/default')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.describe_hub_request.DescribeHubRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.describe_hub_response.DescribeHubResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.describe_hub

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.describe_hub.describe_hub(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.describe_hub_request.DescribeHubRequest = {}  # type: ignore[typeddict-item]
        if hub_arn is not None:
            input_["hub_arn"] = hub_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_organization_configuration(
        self, *, config_overrides: Optional[SecurityHubClientConfig] = None
    ) -> "aws_sdk_securityhub.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse":
        """<p>Returns information about the way your organization is configured in Security Hub CSPM. Only the Security Hub CSPM administrator account can invoke this operation.</p>

        Examples:
            To get information about organization configuration
            This operation provides information about the way your organization is configured in Security Hub. Only a Security Hub administrator account can invoke this operation.

            >>> client.describe_organization_configuration()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.describe_organization_configuration

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.describe_organization_configuration.describe_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_products(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
        product_arn: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> (
        "aws_sdk_securityhub.types.describe_products_response.DescribeProductsResponse"
    ):
        """<p>Returns information about product integrations in Security Hub CSPM.</p> <p>You can optionally provide an integration ARN. If you provide an integration ARN, then the results only include that integration.</p> <p>If you don't provide an integration ARN, then the results include all of the available product integrations. </p>

        Args:
            next_token: <p>The token that is required for pagination. On your first call to the <code>DescribeProducts</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>
            product_arn: <p>The ARN of the integration to return.</p>

        Examples:
            To get information about Security Hub integrations
            The following example returns details about AWS services and third-party products that Security Hub integrates with.

            >>> client.describe_products(next_token='NULL', max_results=1, product_arn='arn:aws:securityhub:us-east-1:517716713836:product/crowdstrike/crowdstrike-falcon')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.describe_products_request.DescribeProductsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.describe_products_response.DescribeProductsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.describe_products

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.describe_products.describe_products(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.describe_products_request.DescribeProductsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if product_arn is not None:
            input_["product_arn"] = product_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_products(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
        product_arn: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.product.Product]":
        _token = next_token
        while True:
            _response = self.describe_products(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                product_arn=product_arn,
            )
            _page = _resolve_path(_response, ("products",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_products_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.describe_products_v2_response.DescribeProductsV2Response":
        """<p>Gets information about the product integration.</p>

        Args:
            next_token: <p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.describe_products_v2_request.DescribeProductsV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.describe_products_v2_response.DescribeProductsV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.describe_products_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.describe_products_v2.describe_products_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.describe_products_v2_request.DescribeProductsV2Request = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_products_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.product_v2.ProductV2]":
        _token = next_token
        while True:
            _response = self.describe_products_v2(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("products_v2",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_security_hub_v2(
        self, *, config_overrides: Optional[SecurityHubClientConfig] = None
    ) -> "aws_sdk_securityhub.types.describe_security_hub_v2_response.DescribeSecurityHubV2Response":
        """<p>Returns details about the service resource in your account.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.describe_security_hub_v2_request.DescribeSecurityHubV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.describe_security_hub_v2_response.DescribeSecurityHubV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.describe_security_hub_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.describe_security_hub_v2.describe_security_hub_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.describe_security_hub_v2_request.DescribeSecurityHubV2Request = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_standards(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.describe_standards_response.DescribeStandardsResponse":
        """<p>Returns a list of the available standards in Security Hub CSPM.</p> <p>For each standard, the results include the standard ARN, the name, and a description. </p>

        Args:
            next_token: <p>The token that is required for pagination. On your first call to the <code>DescribeStandards</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of standards to return.</p>

        Examples:
            To get available Security Hub standards
            The following example returns a list of available security standards in Security Hub.

            >>> client.describe_standards()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.describe_standards_request.DescribeStandardsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.describe_standards_response.DescribeStandardsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.describe_standards

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.describe_standards.describe_standards(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.describe_standards_request.DescribeStandardsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_standards(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.standard.Standard]":
        _token = next_token
        while True:
            _response = self.describe_standards(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("standards",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_standards_controls(
        self,
        standards_subscription_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.describe_standards_controls_response.DescribeStandardsControlsResponse":
        """<p>Returns a list of security standards controls.</p> <p>For each control, the results include information about whether it is currently enabled, the severity, and a link to remediation information.</p> <p>This operation returns an empty list for standard subscriptions where <code>StandardsControlsUpdatable</code> has value <code>NOT_READY_FOR_UPDATES</code>.</p>

        Args:
            standards_subscription_arn: <p>The ARN of a resource that represents your subscription to a supported standard. To get the subscription ARNs of the standards you have enabled, use the <code>GetEnabledStandards</code> operation.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>DescribeStandardsControls</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of security standard controls to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.describe_standards_controls_request.DescribeStandardsControlsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.describe_standards_controls_response.DescribeStandardsControlsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.describe_standards_controls

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.describe_standards_controls.describe_standards_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.describe_standards_controls_request.DescribeStandardsControlsRequest = {}  # type: ignore[typeddict-item]
        input_["standards_subscription_arn"] = standards_subscription_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_standards_controls(
        self,
        standards_subscription_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.standards_control.StandardsControl]":
        _token = next_token
        while True:
            _response = self.describe_standards_controls(
                standards_subscription_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("controls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def disable_import_findings_for_product(
        self,
        product_subscription_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.disable_import_findings_for_product_response.DisableImportFindingsForProductResponse":
        """<p>Disables the integration of the specified product with Security Hub CSPM. After the integration is disabled, findings from that product are no longer sent to Security Hub CSPM.</p>

        Args:
            product_subscription_arn: <p>The ARN of the integrated product to disable the integration for.</p>

        Examples:
            To end a Security Hub integration
            The following example ends an integration between Security Hub and the specified product that sends findings to Security Hub. After the integration ends, the product no longer sends findings to Security  Hub.

            >>> client.disable_import_findings_for_product(product_subscription_arn='arn:aws:securityhub:us-east-1:517716713836:product/crowdstrike/crowdstrike-falcon')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.disable_import_findings_for_product_request.DisableImportFindingsForProductRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.disable_import_findings_for_product_response.DisableImportFindingsForProductResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.disable_import_findings_for_product

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.disable_import_findings_for_product.disable_import_findings_for_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.disable_import_findings_for_product_request.DisableImportFindingsForProductRequest = {}  # type: ignore[typeddict-item]
        input_["product_subscription_arn"] = product_subscription_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_organization_admin_account(
        self,
        admin_account_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        feature: Optional[
            "aws_sdk_securityhub.types.security_hub_feature.SecurityHubFeature"
        ] = None,
    ) -> "aws_sdk_securityhub.types.disable_organization_admin_account_response.DisableOrganizationAdminAccountResponse":
        """<p>Disables a Security Hub CSPM administrator account. Can only be called by the organization management account.</p>

        Args:
            admin_account_id: <p>The Amazon Web Services account identifier of the Security Hub CSPM administrator account.</p>
            feature: <p>The feature for which the delegated admin account is disabled. Defaults to Security Hub CSPM if not specified.</p>

        Examples:
            To remove a Security Hub administrator account
            The following example removes the Security Hub administrator account in the Region from which the operation was executed. This operation doesn't remove the delegated administrator account in AWS Organizations.

            >>> client.disable_organization_admin_account(admin_account_id='123456789012')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.disable_organization_admin_account_request.DisableOrganizationAdminAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.disable_organization_admin_account_response.DisableOrganizationAdminAccountResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.disable_organization_admin_account

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.disable_organization_admin_account.disable_organization_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.disable_organization_admin_account_request.DisableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
        input_["admin_account_id"] = admin_account_id
        if feature is not None:
            input_["feature"] = feature

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_security_hub(
        self, *, config_overrides: Optional[SecurityHubClientConfig] = None
    ) -> "aws_sdk_securityhub.types.disable_security_hub_response.DisableSecurityHubResponse":
        """<p>Disables Security Hub CSPM in your account only in the current Amazon Web Services Region. To disable Security Hub CSPM in all Regions, you must submit one request per Region where you have enabled Security Hub CSPM.</p> <p>You can't disable Security Hub CSPM in an account that is currently the Security Hub CSPM administrator.</p> <p>When you disable Security Hub CSPM, your existing findings and insights and any Security Hub CSPM configuration settings are deleted after 90 days and cannot be recovered. Any standards that were enabled are disabled, and your administrator and member account associations are removed.</p> <p>If you want to save your existing findings, you must export them before you disable Security Hub CSPM.</p>

        Examples:
            To deactivate Security Hub
            The following example deactivates Security Hub for the current account and Region.

            >>> client.disable_security_hub()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.disable_security_hub_request.DisableSecurityHubRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.disable_security_hub_response.DisableSecurityHubResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.disable_security_hub

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.disable_security_hub.disable_security_hub(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.disable_security_hub_request.DisableSecurityHubRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_security_hub_v2(
        self, *, config_overrides: Optional[SecurityHubClientConfig] = None
    ) -> "aws_sdk_securityhub.types.disable_security_hub_v2_response.DisableSecurityHubV2Response":
        """<p>Disable the service for the current Amazon Web Services Region or specified Amazon Web Services Region.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.disable_security_hub_v2_request.DisableSecurityHubV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.disable_security_hub_v2_response.DisableSecurityHubV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.disable_security_hub_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.disable_security_hub_v2.disable_security_hub_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.disable_security_hub_v2_request.DisableSecurityHubV2Request = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_from_administrator_account(
        self, *, config_overrides: Optional[SecurityHubClientConfig] = None
    ) -> "aws_sdk_securityhub.types.disassociate_from_administrator_account_response.DisassociateFromAdministratorAccountResponse":
        """<p>Disassociates the current Security Hub CSPM member account from the associated administrator account.</p> <p>This operation is only used by accounts that are not part of an organization. For organization accounts, only the administrator account can disassociate a member account.</p>

        Examples:
            To disassociate requesting account from administrator account
            The following example dissociates the requesting account from its associated administrator account.

            >>> client.disassociate_from_administrator_account()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.disassociate_from_administrator_account_request.DisassociateFromAdministratorAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.disassociate_from_administrator_account_response.DisassociateFromAdministratorAccountResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.disassociate_from_administrator_account

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.disassociate_from_administrator_account.disassociate_from_administrator_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.disassociate_from_administrator_account_request.DisassociateFromAdministratorAccountRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_from_master_account(
        self, *, config_overrides: Optional[SecurityHubClientConfig] = None
    ) -> "aws_sdk_securityhub.types.disassociate_from_master_account_response.DisassociateFromMasterAccountResponse":
        """<p>This method is deprecated. Instead, use <code>DisassociateFromAdministratorAccount</code>.</p> <p>The Security Hub CSPM console continues to use <code>DisassociateFromMasterAccount</code>. It will eventually change to use <code>DisassociateFromAdministratorAccount</code>. Any IAM policies that specifically control access to this function must continue to use <code>DisassociateFromMasterAccount</code>. You should also add <code>DisassociateFromAdministratorAccount</code> to your policies to ensure that the correct permissions are in place after the console begins to use <code>DisassociateFromAdministratorAccount</code>.</p> <p>Disassociates the current Security Hub CSPM member account from the associated administrator account.</p> <p>This operation is only used by accounts that are not part of an organization. For organization accounts, only the administrator account can disassociate a member account.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.disassociate_from_master_account_request.DisassociateFromMasterAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.disassociate_from_master_account_response.DisassociateFromMasterAccountResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.disassociate_from_master_account

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.disassociate_from_master_account.disassociate_from_master_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.disassociate_from_master_account_request.DisassociateFromMasterAccountRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_members(
        self,
        account_ids: "aws_sdk_securityhub.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.disassociate_members_response.DisassociateMembersResponse":
        """<p>Disassociates the specified member accounts from the associated administrator account.</p> <p>Can be used to disassociate both accounts that are managed using Organizations and accounts that were invited manually.</p>

        Args:
            account_ids: <p>The account IDs of the member accounts to disassociate from the administrator account.</p>

        Examples:
            To disassociate member accounts from administrator account
            The following example dissociates the specified member accounts from the associated administrator account.

            >>> client.disassociate_members(account_ids=['123456789012', '111122223333'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.disassociate_members_request.DisassociateMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.disassociate_members_response.DisassociateMembersResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.disassociate_members

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.disassociate_members.disassociate_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.disassociate_members_request.DisassociateMembersRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_import_findings_for_product(
        self,
        product_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.enable_import_findings_for_product_response.EnableImportFindingsForProductResponse":
        """<p>Enables the integration of a partner product with Security Hub CSPM. Integrated products send findings to Security Hub CSPM.</p> <p>When you enable a product integration, a permissions policy that grants permission for the product to send findings to Security Hub CSPM is applied.</p>

        Args:
            product_arn: <p>The ARN of the product to enable the integration for.</p>

        Examples:
            To activate an integration
            The following example activates an integration between Security Hub and a third party partner product that sends findings to Security Hub.

            >>> client.enable_import_findings_for_product(product_arn='arn:aws:securityhub:us-east-1:517716713836:product/crowdstrike/crowdstrike-falcon')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.enable_import_findings_for_product_request.EnableImportFindingsForProductRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.enable_import_findings_for_product_response.EnableImportFindingsForProductResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.enable_import_findings_for_product

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.enable_import_findings_for_product.enable_import_findings_for_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.enable_import_findings_for_product_request.EnableImportFindingsForProductRequest = {}  # type: ignore[typeddict-item]
        input_["product_arn"] = product_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_organization_admin_account(
        self,
        admin_account_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        feature: Optional[
            "aws_sdk_securityhub.types.security_hub_feature.SecurityHubFeature"
        ] = None,
    ) -> "aws_sdk_securityhub.types.enable_organization_admin_account_response.EnableOrganizationAdminAccountResponse":
        """<p>Designates the Security Hub CSPM administrator account for an organization. Can only be called by the organization management account.</p>

        Args:
            admin_account_id: <p>The Amazon Web Services account identifier of the account to designate as the Security Hub CSPM administrator account.</p>
            feature: <p>The feature for which the delegated admin account is enabled. Defaults to Security Hub CSPM if not specified.</p>

        Examples:
            To designate a Security Hub administrator
            The following example designates the specified account as the Security Hub administrator account. The requesting account must be the organization management account.

            >>> client.enable_organization_admin_account(admin_account_id='123456789012')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.enable_organization_admin_account_response.EnableOrganizationAdminAccountResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.enable_organization_admin_account

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.enable_organization_admin_account.enable_organization_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
        input_["admin_account_id"] = admin_account_id
        if feature is not None:
            input_["feature"] = feature

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_security_hub(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        tags: Optional["aws_sdk_securityhub.types.tag_map.TagMap"] = None,
        enable_default_standards: Optional[
            "aws_sdk_securityhub.types.boolean.Boolean"
        ] = None,
        control_finding_generator: Optional[
            "aws_sdk_securityhub.types.control_finding_generator.ControlFindingGenerator"
        ] = None,
    ) -> "aws_sdk_securityhub.types.enable_security_hub_response.EnableSecurityHubResponse":
        r"""<p>Enables Security Hub CSPM for your account in the current Region or the Region you specify in the request.</p> <p>When you enable Security Hub CSPM, you grant to Security Hub CSPM the permissions necessary to gather findings from other services that are integrated with Security Hub CSPM.</p> <p>When you use the <code>EnableSecurityHub</code> operation to enable Security Hub CSPM, you also automatically enable the following standards:</p> <ul> <li> <p>Center for Internet Security (CIS) Amazon Web Services Foundations Benchmark v1.2.0</p> </li> <li> <p>Amazon Web Services Foundational Security Best Practices</p> </li> </ul> <p>Other standards are not automatically enabled. </p> <p>To opt out of automatically enabled standards, set <code>EnableDefaultStandards</code> to <code>false</code>.</p> <p>After you enable Security Hub CSPM, to enable a standard, use the <code>BatchEnableStandards</code> operation. To disable a standard, use the <code>BatchDisableStandards</code> operation.</p> <p>To learn more, see the <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html\">setup information</a> in the <i>Security Hub CSPM User Guide</i>.</p>

        Args:
            tags: <p>The tags to add to the hub resource when you enable Security Hub CSPM.</p>
            enable_default_standards: <p>Whether to enable the security standards that Security Hub CSPM has designated as automatically enabled. If you don't provide a value for <code>EnableDefaultStandards</code>, it is set to <code>true</code>. To not enable the automatically enabled standards, set <code>EnableDefaultStandards</code> to <code>false</code>.</p>
            control_finding_generator: <p>This field, used when enabling Security Hub CSPM, specifies whether the calling account has consolidated control findings turned on. If the value for this field is set to <code>SECURITY_CONTROL</code>, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.</p> <p>If the value for this field is set to <code>STANDARD_CONTROL</code>, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.</p> <p>The value for this field in a member account matches the value in the administrator account. For accounts that aren't part of an organization, the default value of this field is <code>SECURITY_CONTROL</code> if you enabled Security Hub CSPM on or after February 23, 2023.</p>

        Examples:
            To activate Security Hub
            The following example activates the Security Hub service in the requesting AWS account. The service is activated in the current AWS Region or the Region that you specify in the request. Some standards are automatically turned on in your account unless you opt out. To determine which standards are automatically turned on, see the Security Hub documentation.

            >>> client.enable_security_hub(tags={'Department': 'Security'}, enable_default_standards=True)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.enable_security_hub_request.EnableSecurityHubRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.enable_security_hub_response.EnableSecurityHubResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.enable_security_hub

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.enable_security_hub.enable_security_hub(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.enable_security_hub_request.EnableSecurityHubRequest = {}  # type: ignore[typeddict-item]
        if tags is not None:
            input_["tags"] = tags
        if enable_default_standards is not None:
            input_["enable_default_standards"] = enable_default_standards
        if control_finding_generator is not None:
            input_["control_finding_generator"] = control_finding_generator

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_security_hub_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        tags: Optional["aws_sdk_securityhub.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_securityhub.types.enable_security_hub_v2_response.EnableSecurityHubV2Response":
        """<p>Enables the service in account for the current Amazon Web Services Region or specified Amazon Web Services Region.</p>

        Args:
            tags: <p>The tags to add to the hub V2 resource when you enable Security Hub.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.enable_security_hub_v2_request.EnableSecurityHubV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.enable_security_hub_v2_response.EnableSecurityHubV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.enable_security_hub_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.enable_security_hub_v2.enable_security_hub_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.enable_security_hub_v2_request.EnableSecurityHubV2Request = {}  # type: ignore[typeddict-item]
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def generate_recommended_policy_v2(
        self,
        metadata_uid: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.generate_recommended_policy_v2_response.GenerateRecommendedPolicyV2Response":
        """<p>Begins the recommended policy generation to remediate a Security Hub finding. <code>GenerateRecommendedPolicyV2</code> only supports findings for unused permissions.</p>

        Args:
            metadata_uid: <p>The unique identifier (ID) of Security Hub OCSF findings found under the <code>metadata.uid</code> field of the finding.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.generate_recommended_policy_v2_request.GenerateRecommendedPolicyV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.generate_recommended_policy_v2_response.GenerateRecommendedPolicyV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.generate_recommended_policy_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.generate_recommended_policy_v2.generate_recommended_policy_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.generate_recommended_policy_v2_request.GenerateRecommendedPolicyV2Request = {}  # type: ignore[typeddict-item]
        input_["metadata_uid"] = metadata_uid

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_administrator_account(
        self, *, config_overrides: Optional[SecurityHubClientConfig] = None
    ) -> "aws_sdk_securityhub.types.get_administrator_account_response.GetAdministratorAccountResponse":
        """<p>Provides the details for the Security Hub CSPM administrator account for the current member account.</p> <p>Can be used by both member accounts that are managed using Organizations and accounts that were invited manually.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_administrator_account_request.GetAdministratorAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_administrator_account_response.GetAdministratorAccountResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_administrator_account

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_administrator_account.get_administrator_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_administrator_account_request.GetAdministratorAccountRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_aggregator_v2(
        self,
        aggregator_v2_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.get_aggregator_v2_response.GetAggregatorV2Response":
        """<p>Returns the configuration of the specified Aggregator V2.</p>

        Args:
            aggregator_v2_arn: <p>The ARN of the Aggregator V2.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_aggregator_v2_request.GetAggregatorV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_aggregator_v2_response.GetAggregatorV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_aggregator_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_aggregator_v2.get_aggregator_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_aggregator_v2_request.GetAggregatorV2Request = {}  # type: ignore[typeddict-item]
        input_["aggregator_v2_arn"] = aggregator_v2_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_automation_rule_v2(
        self,
        identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.get_automation_rule_v2_response.GetAutomationRuleV2Response":
        """<p>Returns an automation rule for the V2 service.</p>

        Args:
            identifier: <p>The ARN of the V2 automation rule.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_automation_rule_v2_request.GetAutomationRuleV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_automation_rule_v2_response.GetAutomationRuleV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_automation_rule_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_automation_rule_v2.get_automation_rule_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_automation_rule_v2_request.GetAutomationRuleV2Request = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_configuration_policy(
        self,
        identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.get_configuration_policy_response.GetConfigurationPolicyResponse":
        """<p> Provides information about a configuration policy. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            identifier: <p> The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy. </p>

        Examples:
            To get details about a configuration policy
            This operation provides details about the specified configuration policy.

            >>> client.get_configuration_policy(identifier='arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_configuration_policy_request.GetConfigurationPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_configuration_policy_response.GetConfigurationPolicyResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_configuration_policy

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_configuration_policy.get_configuration_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_configuration_policy_request.GetConfigurationPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_configuration_policy_association(
        self,
        target: "aws_sdk_securityhub.types.target.Target",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.get_configuration_policy_association_response.GetConfigurationPolicyAssociationResponse":
        """<p> Returns the association between a configuration and a target account, organizational unit, or the root. The configuration can be a configuration policy or self-managed behavior. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            target: <p> The target account ID, organizational unit ID, or the root ID to retrieve the association for. </p>

        Examples:
            To get details about a configuration association
            This operation provides details about configuration associations for a specific target account, organizational unit, or the root.

            >>> client.get_configuration_policy_association(target={'AccountId': '111122223333'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_configuration_policy_association_request.GetConfigurationPolicyAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_configuration_policy_association_response.GetConfigurationPolicyAssociationResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_configuration_policy_association

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_configuration_policy_association.get_configuration_policy_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_configuration_policy_association_request.GetConfigurationPolicyAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["target"] = target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_connector_v2(
        self,
        connector_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.get_connector_v2_response.GetConnectorV2Response":
        """<p>Grants permission to retrieve details for a connectorV2 based on connector id.</p>

        Args:
            connector_id: <p>The UUID of the connectorV2 to identify connectorV2 resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_connector_v2_request.GetConnectorV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_connector_v2_response.GetConnectorV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_connector_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_connector_v2.get_connector_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_connector_v2_request.GetConnectorV2Request = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_enabled_standards(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        standards_subscription_arns: Optional[
            "aws_sdk_securityhub.types.standards_subscription_arns.StandardsSubscriptionArns"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_enabled_standards_response.GetEnabledStandardsResponse":
        """<p>Returns a list of the standards that are currently enabled.</p>

        Args:
            standards_subscription_arns: <p>The list of the standards subscription ARNs for the standards to retrieve.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>GetEnabledStandards</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of results to return in the response.</p>

        Examples:
            To return a list of enabled standards
            The following example returns a list of Security Hub standards that are currently enabled in your account.

            >>> client.get_enabled_standards(standards_subscription_arns=['arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_enabled_standards_request.GetEnabledStandardsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_enabled_standards_response.GetEnabledStandardsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_enabled_standards

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_enabled_standards.get_enabled_standards(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_enabled_standards_request.GetEnabledStandardsRequest = {}  # type: ignore[typeddict-item]
        if standards_subscription_arns is not None:
            input_["standards_subscription_arns"] = standards_subscription_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_enabled_standards(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        standards_subscription_arns: Optional[
            "aws_sdk_securityhub.types.standards_subscription_arns.StandardsSubscriptionArns"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.standards_subscription.StandardsSubscription]":
        _token = next_token
        while True:
            _response = self.get_enabled_standards(
                config_overrides=config_overrides,
                standards_subscription_arns=standards_subscription_arns,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("standards_subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_finding_aggregator(
        self,
        finding_aggregator_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.get_finding_aggregator_response.GetFindingAggregatorResponse":
        """<note> <p>The <i>aggregation Region</i> is now called the <i>home Region</i>.</p> </note> <p>Returns the current configuration in the calling account for cross-Region aggregation. A finding aggregator is a resource that establishes the home Region and any linked Regions.</p>

        Args:
            finding_aggregator_arn: <p>The ARN of the finding aggregator to return details for. To obtain the ARN, use <code>ListFindingAggregators</code>.</p>

        Examples:
            To get cross-Region aggregation details
            The following example returns cross-Region aggregation details for the requesting account.

            >>> client.get_finding_aggregator(finding_aggregator_arn='arn:aws:securityhub:us-east-1:123456789012:finding-aggregator/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_finding_aggregator_request.GetFindingAggregatorRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_finding_aggregator_response.GetFindingAggregatorResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_finding_aggregator

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_finding_aggregator.get_finding_aggregator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_finding_aggregator_request.GetFindingAggregatorRequest = {}  # type: ignore[typeddict-item]
        input_["finding_aggregator_arn"] = finding_aggregator_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_finding_history(
        self,
        finding_identifier: "aws_sdk_securityhub.types.aws_security_finding_identifier.AwsSecurityFindingIdentifier",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        start_time: Optional["aws_sdk_securityhub.types.timestamp.Timestamp"] = None,
        end_time: Optional["aws_sdk_securityhub.types.timestamp.Timestamp"] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_finding_history_response.GetFindingHistoryResponse":
        r"""<p> Returns the history of a Security Hub CSPM finding. The history includes changes made to any fields in the Amazon Web Services Security Finding Format (ASFF) except top-level timestamp fields, such as the <code>CreatedAt</code> and <code>UpdatedAt</code> fields. </p> <p>This operation might return fewer results than the maximum number of results (<code>MaxResults</code>) specified in a request, even when more results are available. If this occurs, the response includes a <code>NextToken</code> value, which you should use to retrieve the next set of results in the response. The presence of a <code>NextToken</code> value in a response doesn't necessarily indicate that the results are incomplete. However, you should continue to specify a <code>NextToken</code> value until you receive a response that doesn't include this value.</p>

        Args:
            start_time: <p>A timestamp that indicates the start time of the requested finding history.</p> <p>If you provide values for both <code>StartTime</code> and <code>EndTime</code>, Security Hub CSPM returns finding history for the specified time period. If you provide a value for <code>StartTime</code> but not for <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>StartTime</code> to the time at which the API is called. If you provide a value for <code>EndTime</code> but not for <code>StartTime</code>, Security Hub CSPM returns finding history from the <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html#securityhub-Type-AwsSecurityFindingFilters-CreatedAt\">CreatedAt</a> timestamp of the finding to the <code>EndTime</code>. If you provide neither <code>StartTime</code> nor <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>CreatedAt</code> timestamp of the finding to the time at which the API is called. In all of these scenarios, the response is limited to 100 results.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>
            end_time: <p> An ISO 8601-formatted timestamp that indicates the end time of the requested finding history.</p> <p>If you provide values for both <code>StartTime</code> and <code>EndTime</code>, Security Hub CSPM returns finding history for the specified time period. If you provide a value for <code>StartTime</code> but not for <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>StartTime</code> to the time at which the API is called. If you provide a value for <code>EndTime</code> but not for <code>StartTime</code>, Security Hub CSPM returns finding history from the <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html#securityhub-Type-AwsSecurityFindingFilters-CreatedAt\">CreatedAt</a> timestamp of the finding to the <code>EndTime</code>. If you provide neither <code>StartTime</code> nor <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>CreatedAt</code> timestamp of the finding to the time at which the API is called. In all of these scenarios, the response is limited to 100 results.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>
            next_token: <p> A token for pagination purposes. Provide <code>NULL</code> as the initial value. In subsequent requests, provide the token included in the response to get up to an additional 100 results of finding history. If you don’t provide <code>NextToken</code>, Security Hub CSPM returns up to 100 results of finding history for each request. </p>
            max_results: <p> The maximum number of results to be returned. If you don’t provide it, Security Hub CSPM returns up to 100 results of finding history. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_finding_history_request.GetFindingHistoryRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_finding_history_response.GetFindingHistoryResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_finding_history

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_finding_history.get_finding_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_finding_history_request.GetFindingHistoryRequest = {}  # type: ignore[typeddict-item]
        input_["finding_identifier"] = finding_identifier
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_finding_history(
        self,
        finding_identifier: "aws_sdk_securityhub.types.aws_security_finding_identifier.AwsSecurityFindingIdentifier",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        start_time: Optional["aws_sdk_securityhub.types.timestamp.Timestamp"] = None,
        end_time: Optional["aws_sdk_securityhub.types.timestamp.Timestamp"] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.finding_history_record.FindingHistoryRecord]":
        _token = next_token
        while True:
            _response = self.get_finding_history(
                finding_identifier,
                config_overrides=config_overrides,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_findings(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_findings_response.GetFindingsResponse":
        """<p>Returns a list of findings that match the specified criteria.</p> <p>If cross-Region aggregation is enabled, then when you call <code>GetFindings</code> from the home Region, the results include all of the matching findings from both the home Region and linked Regions.</p>

        Args:
            filters: <p>The finding attributes used to define a condition to filter the returned findings.</p> <p>You can filter by up to 10 finding attributes. For each attribute, you can provide up to 20 filter values.</p> <p>Note that in the available filter fields, <code>WorkflowState</code> is deprecated. To search for a finding based on its workflow status, use <code>WorkflowStatus</code>.</p>
            sort_criteria: <p>The finding attributes used to sort the list of returned findings.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>GetFindings</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of findings to return.</p>

        Examples:
            To get a list of findings
            The following example returns a filtered and sorted list of Security Hub findings.

            >>> client.get_findings(filters={'AwsAccountId': [{'Value': '123456789012', 'Comparison': 'PREFIX'}]}, max_results=1)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_findings_request.GetFindingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_findings_response.GetFindingsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_findings

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_findings.get_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_findings_request.GetFindingsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_findings(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.aws_security_finding.AwsSecurityFinding]":
        _token = next_token
        while True:
            _response = self.get_findings(
                config_overrides=config_overrides,
                filters=filters,
                sort_criteria=sort_criteria,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("findings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_finding_statistics_v2(
        self,
        group_by_rules: "aws_sdk_securityhub.types.group_by_rules.GroupByRules",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        scopes: Optional[
            "aws_sdk_securityhub.types.finding_scopes.FindingScopes"
        ] = None,
        sort_order: Optional["aws_sdk_securityhub.types.sort_order.SortOrder"] = None,
        max_statistic_results: Optional[
            "aws_sdk_securityhub.types.max_statistic_results.MaxStatisticResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_finding_statistics_v2_response.GetFindingStatisticsV2Response":
        """<p>Returns aggregated statistical data about findings.</p> <p>You can use the <code>Scopes</code> parameter to define the data boundary for the query. Currently, <code>Scopes</code> supports <code>AwsOrganizations</code>, which lets you aggregate findings from your entire organization or from specific organizational units. Only the delegated administrator account can use <code>Scopes</code>.</p> <p> <code>GetFindingStatisticsV2</code> uses <code>securityhub:GetAdhocInsightResults</code> in the <code>Action</code> element of an IAM policy statement. You must have permission to perform the <code>securityhub:GetAdhocInsightResults</code> action.</p>

        Args:
            group_by_rules: <p>Specifies how security findings should be aggregated and organized in the statistical analysis. It can accept up to 5 <code>groupBy</code> fields in a single call.</p>
            scopes: <p>Limits the results to findings from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees statistics from all accounts across the entire organization. Other accounts see only statistics for their own findings.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>
            sort_order: <p>Orders the aggregation count in descending or ascending order. Descending order is the default.</p>
            max_statistic_results: <p>The maximum number of results to be returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_finding_statistics_v2_request.GetFindingStatisticsV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_finding_statistics_v2_response.GetFindingStatisticsV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_finding_statistics_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_finding_statistics_v2.get_finding_statistics_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_finding_statistics_v2_request.GetFindingStatisticsV2Request = {}  # type: ignore[typeddict-item]
        input_["group_by_rules"] = group_by_rules
        if scopes is not None:
            input_["scopes"] = scopes
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_statistic_results is not None:
            input_["max_statistic_results"] = max_statistic_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_findings_trends_v2(
        self,
        start_time: "aws_sdk_securityhub.types.timestamp.Timestamp",
        end_time: "aws_sdk_securityhub.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.findings_trends_filters.FindingsTrendsFilters"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_findings_trends_v2_response.GetFindingsTrendsV2Response":
        """<p>Returns findings trend data based on the specified criteria. This operation helps you analyze patterns and changes in findings over time.</p>

        Args:
            filters: <p>The filters to apply to the findings trend data.</p>
            start_time: <p>The starting timestamp for the time period to analyze findings trends, in ISO 8601 format.</p>
            end_time: <p>The ending timestamp for the time period to analyze findings trends, in ISO 8601 format.</p>
            next_token: <p>The token to use for paginating results. This value is returned in the response if more results are available.</p>
            max_results: <p>The maximum number of trend data points to return in a single response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_findings_trends_v2_request.GetFindingsTrendsV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_findings_trends_v2_response.GetFindingsTrendsV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_findings_trends_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_findings_trends_v2.get_findings_trends_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_findings_trends_v2_request.GetFindingsTrendsV2Request = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_findings_trends_v2(
        self,
        start_time: "aws_sdk_securityhub.types.timestamp.Timestamp",
        end_time: "aws_sdk_securityhub.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.findings_trends_filters.FindingsTrendsFilters"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "Iterator[aws_sdk_securityhub.types.trends_metrics_result.TrendsMetricsResult]"
    ):
        _token = next_token
        while True:
            _response = self.get_findings_trends_v2(
                start_time,
                end_time,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("trends_metrics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_findings_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.ocsf_finding_filters.OcsfFindingFilters"
        ] = None,
        scopes: Optional[
            "aws_sdk_securityhub.types.finding_scopes.FindingScopes"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_findings_v2_response.GetFindingsV2Response":
        """<p>Returns a list of findings that match the specified criteria.</p> <p>You can use the <code>Scopes</code> parameter to define the data boundary for the query. Currently, <code>Scopes</code> supports <code>AwsOrganizations</code>, which lets you retrieve findings from your entire organization or from specific organizational units. Only the delegated administrator account can use <code>Scopes</code>.</p> <p>You can use the <code>Filters</code> parameter to refine results based on finding attributes. You can use <code>Scopes</code> and <code>Filters</code> independently or together. When both are provided, <code>Scopes</code> narrows the data set first, and then <code>Filters</code> refines results within that scoped data set.</p> <p> <code>GetFindings</code> and <code>GetFindingsV2</code> both use <code>securityhub:GetFindings</code> in the <code>Action</code> element of an IAM policy statement. You must have permission to perform the <code>securityhub:GetFindings</code> action.</p>

        Args:
            filters: <p>The finding attributes used to define a condition to filter the returned OCSF findings. You can filter up to 10 composite filters. For each filter type inside of a composite filter, you can provide up to 20 filters.</p>
            scopes: <p>Limits the results to findings from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees findings from all accounts across the entire organization. Other accounts see only their own findings.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>
            sort_criteria: <p>The finding attributes used to sort the list of returned findings.</p>
            next_token: <p> The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_findings_v2_request.GetFindingsV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_findings_v2_response.GetFindingsV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_findings_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_findings_v2.get_findings_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_findings_v2_request.GetFindingsV2Request = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if scopes is not None:
            input_["scopes"] = scopes
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_findings_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.ocsf_finding_filters.OcsfFindingFilters"
        ] = None,
        scopes: Optional[
            "aws_sdk_securityhub.types.finding_scopes.FindingScopes"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.ocsf_finding.OcsfFinding]":
        _token = next_token
        while True:
            _response = self.get_findings_v2(
                config_overrides=config_overrides,
                filters=filters,
                scopes=scopes,
                sort_criteria=sort_criteria,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("findings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_insight_results(
        self,
        insight_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.get_insight_results_response.GetInsightResultsResponse":
        """<p>Lists the results of the Security Hub CSPM insight specified by the insight ARN.</p>

        Args:
            insight_arn: <p>The ARN of the insight for which to return results.</p>

        Examples:
            To get the results of a Security Hub insight
            The following example returns the results of the Security Hub insight specified by the insight ARN.

            >>> client.get_insight_results(insight_arn='arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_insight_results_request.GetInsightResultsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_insight_results_response.GetInsightResultsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_insight_results

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_insight_results.get_insight_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_insight_results_request.GetInsightResultsRequest = {}  # type: ignore[typeddict-item]
        input_["insight_arn"] = insight_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_insights(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        insight_arns: Optional["aws_sdk_securityhub.types.arn_list.ArnList"] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_insights_response.GetInsightsResponse":
        """<p>Lists and describes insights for the specified insight ARNs.</p>

        Args:
            insight_arns: <p>The ARNs of the insights to describe. If you don't provide any insight ARNs, then <code>GetInsights</code> returns all of your custom insights. It does not return any managed insights.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>GetInsights</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of items to return in the response.</p>

        Examples:
            To get details of a Security Hub insight
            The following example returns details of the Security Hub insight with the specified ARN.

            >>> client.get_insights(insight_arns=['arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_insights_request.GetInsightsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_insights_response.GetInsightsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_insights

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_insights.get_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_insights_request.GetInsightsRequest = {}  # type: ignore[typeddict-item]
        if insight_arns is not None:
            input_["insight_arns"] = insight_arns
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_insights(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        insight_arns: Optional["aws_sdk_securityhub.types.arn_list.ArnList"] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.insight.Insight]":
        _token = next_token
        while True:
            _response = self.get_insights(
                config_overrides=config_overrides,
                insight_arns=insight_arns,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("insights",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_invitations_count(
        self, *, config_overrides: Optional[SecurityHubClientConfig] = None
    ) -> "aws_sdk_securityhub.types.get_invitations_count_response.GetInvitationsCountResponse":
        r"""<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html\">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Returns the count of all Security Hub CSPM membership invitations that were sent to the calling member account, not including the currently accepted invitation. </p>

        Examples:
            To get a count of membership invitations
            The following example returns a count of invitations that the Security Hub administrator sent to the current member account, not including the currently accepted invitation.



            >>> client.get_invitations_count()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_invitations_count_request.GetInvitationsCountRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_invitations_count_response.GetInvitationsCountResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_invitations_count

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_invitations_count.get_invitations_count(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_invitations_count_request.GetInvitationsCountRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_master_account(
        self, *, config_overrides: Optional[SecurityHubClientConfig] = None
    ) -> (
        "aws_sdk_securityhub.types.get_master_account_response.GetMasterAccountResponse"
    ):
        """<p>This method is deprecated. Instead, use <code>GetAdministratorAccount</code>.</p> <p>The Security Hub CSPM console continues to use <code>GetMasterAccount</code>. It will eventually change to use <code>GetAdministratorAccount</code>. Any IAM policies that specifically control access to this function must continue to use <code>GetMasterAccount</code>. You should also add <code>GetAdministratorAccount</code> to your policies to ensure that the correct permissions are in place after the console begins to use <code>GetAdministratorAccount</code>.</p> <p>Provides the details for the Security Hub CSPM administrator account for the current member account.</p> <p>Can be used by both member accounts that are managed using Organizations and accounts that were invited manually.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_master_account_request.GetMasterAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_master_account_response.GetMasterAccountResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_master_account

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_master_account.get_master_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_master_account_request.GetMasterAccountRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_members(
        self,
        account_ids: "aws_sdk_securityhub.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.get_members_response.GetMembersResponse":
        """<p>Returns the details for the Security Hub CSPM member accounts for the specified account IDs.</p> <p>An administrator account can be either the delegated Security Hub CSPM administrator account for an organization or an administrator account that enabled Security Hub CSPM manually.</p> <p>The results include both member accounts that are managed using Organizations and accounts that were invited manually.</p>

        Args:
            account_ids: <p>The list of account IDs for the Security Hub CSPM member accounts to return the details for. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_members_request.GetMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_members_response.GetMembersResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_members

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_members.get_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_members_request.GetMembersRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_recommended_policy_v2(
        self,
        metadata_uid: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_recommended_policy_v2_response.GetRecommendedPolicyV2Response":
        """<p>Retrieves the recommended policy to remediate a Security Hub finding. <code>GetRecommendedPolicyV2</code> only supports findings for unused permissions.</p>

        Args:
            metadata_uid: <p>The unique identifier (ID) of Security Hub OCSF findings found under the <code>metadata.uid</code> field of the finding.</p>
            next_token: <p>The token used to paginate the <code>RecommendationSteps</code> list returned. On your first call to <code>GetRecommendedPolicyV2</code>, omit this parameter or set it to <code>NULL</code>. For subsequent calls, use the <code>NextToken</code> value returned in the previous response to retrieve the next page of results.</p>
            max_results: <p>The maximum number of recommendation steps to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_recommended_policy_v2_request.GetRecommendedPolicyV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_recommended_policy_v2_response.GetRecommendedPolicyV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_recommended_policy_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_recommended_policy_v2.get_recommended_policy_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_recommended_policy_v2_request.GetRecommendedPolicyV2Request = {}  # type: ignore[typeddict-item]
        input_["metadata_uid"] = metadata_uid
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_recommended_policy_v2(
        self,
        metadata_uid: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.recommendation_step.RecommendationStep]":
        _token = next_token
        while True:
            _response = self.get_recommended_policy_v2(
                metadata_uid,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("recommendation_steps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_resources_statistics_v2(
        self,
        group_by_rules: "aws_sdk_securityhub.types.resource_group_by_rules.ResourceGroupByRules",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        scopes: Optional[
            "aws_sdk_securityhub.types.resource_scopes.ResourceScopes"
        ] = None,
        sort_order: Optional["aws_sdk_securityhub.types.sort_order.SortOrder"] = None,
        max_statistic_results: Optional[
            "aws_sdk_securityhub.types.max_statistic_results.MaxStatisticResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_resources_statistics_v2_response.GetResourcesStatisticsV2Response":
        """<p>Retrieves statistical information about Amazon Web Services resources and their associated security findings.</p> <p>You can use the <code>Scopes</code> parameter to define the data boundary for the query. Currently, <code>Scopes</code> supports <code>AwsOrganizations</code>, which lets you aggregate resources from your entire organization or from specific organizational units. Only the delegated administrator account can use <code>Scopes</code>.</p>

        Args:
            group_by_rules: <p>How resource statistics should be aggregated and organized in the response.</p>
            scopes: <p>Limits the results to resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees statistics from all accounts across the entire organization. Other accounts see only statistics for their own resources.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>
            sort_order: <p>Sorts aggregated statistics.</p>
            max_statistic_results: <p>The maximum number of results to be returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_resources_statistics_v2_request.GetResourcesStatisticsV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_resources_statistics_v2_response.GetResourcesStatisticsV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_resources_statistics_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_resources_statistics_v2.get_resources_statistics_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_resources_statistics_v2_request.GetResourcesStatisticsV2Request = {}  # type: ignore[typeddict-item]
        input_["group_by_rules"] = group_by_rules
        if scopes is not None:
            input_["scopes"] = scopes
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_statistic_results is not None:
            input_["max_statistic_results"] = max_statistic_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resources_trends_v2(
        self,
        start_time: "aws_sdk_securityhub.types.timestamp.Timestamp",
        end_time: "aws_sdk_securityhub.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.resources_trends_filters.ResourcesTrendsFilters"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_resources_trends_v2_response.GetResourcesTrendsV2Response":
        """<p>Returns resource trend data based on the specified criteria. This operation helps you analyze patterns and changes in resource compliance over time.</p>

        Args:
            filters: <p>The filters to apply to the resources trend data.</p>
            start_time: <p>The starting timestamp for the time period to analyze resources trends, in ISO 8601 format.</p>
            end_time: <p>The ending timestamp for the time period to analyze resources trends, in ISO 8601 format.</p>
            next_token: <p>The token to use for paginating results. This value is returned in the response if more results are available.</p>
            max_results: <p>The maximum number of trend data points to return in a single response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_resources_trends_v2_request.GetResourcesTrendsV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_resources_trends_v2_response.GetResourcesTrendsV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_resources_trends_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_resources_trends_v2.get_resources_trends_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_resources_trends_v2_request.GetResourcesTrendsV2Request = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_resources_trends_v2(
        self,
        start_time: "aws_sdk_securityhub.types.timestamp.Timestamp",
        end_time: "aws_sdk_securityhub.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.resources_trends_filters.ResourcesTrendsFilters"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.resources_trends_metrics_result.ResourcesTrendsMetricsResult]":
        _token = next_token
        while True:
            _response = self.get_resources_trends_v2(
                start_time,
                end_time,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("trends_metrics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_resources_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.resources_filters.ResourcesFilters"
        ] = None,
        scopes: Optional[
            "aws_sdk_securityhub.types.resource_scopes.ResourceScopes"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.get_resources_v2_response.GetResourcesV2Response":
        """<p>Returns a list of resources.</p> <p>You can use the <code>Scopes</code> parameter to define the data boundary for the query. Currently, <code>Scopes</code> supports <code>AwsOrganizations</code>, which lets you retrieve resources from your entire organization or from specific organizational units. Only the delegated administrator account can use <code>Scopes</code>.</p> <p>You can use the <code>Filters</code> parameter to refine results based on resource attributes. You can use <code>Scopes</code> and <code>Filters</code> independently or together. When both are provided, <code>Scopes</code> narrows the data set first, and then <code>Filters</code> refines results within that scoped data set.</p>

        Args:
            filters: <p>Filters resources based on a set of criteria.</p>
            scopes: <p>Limits the results to resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees resources from all accounts across the entire organization. Other accounts see only their own resources.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>
            sort_criteria: <p>The resource attributes used to sort the list of returned resources.</p>
            next_token: <p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_resources_v2_request.GetResourcesV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_resources_v2_response.GetResourcesV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_resources_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_resources_v2.get_resources_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_resources_v2_request.GetResourcesV2Request = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if scopes is not None:
            input_["scopes"] = scopes
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_resources_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.resources_filters.ResourcesFilters"
        ] = None,
        scopes: Optional[
            "aws_sdk_securityhub.types.resource_scopes.ResourceScopes"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_securityhub.types.sort_criteria.SortCriteria"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.resource_result.ResourceResult]":
        _token = next_token
        while True:
            _response = self.get_resources_v2(
                config_overrides=config_overrides,
                filters=filters,
                scopes=scopes,
                sort_criteria=sort_criteria,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_security_control_definition(
        self,
        security_control_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.get_security_control_definition_response.GetSecurityControlDefinitionResponse":
        """<p> Retrieves the definition of a security control. The definition includes the control title, description, Region availability, parameter definitions, and other details. </p>

        Args:
            security_control_id: <p> The ID of the security control to retrieve the definition for. This field doesn’t accept an Amazon Resource Name (ARN). </p>

        Examples:
            To get the definition of a security control.
            The following example retrieves definition details for the specified security control.

            >>> client.get_security_control_definition(security_control_id='EC2.4')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.get_security_control_definition_request.GetSecurityControlDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.get_security_control_definition_response.GetSecurityControlDefinitionResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.get_security_control_definition

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.get_security_control_definition.get_security_control_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.get_security_control_definition_request.GetSecurityControlDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["security_control_id"] = security_control_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def invite_members(
        self,
        account_ids: "aws_sdk_securityhub.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.invite_members_response.InviteMembersResponse":
        r"""<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html\">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Invites other Amazon Web Services accounts to become member accounts for the Security Hub CSPM administrator account that the invitation is sent from.</p> <p>This operation is only used to invite accounts that don't belong to an Amazon Web Services organization. Organization accounts don't receive invitations.</p> <p>Before you can use this action to invite a member, you must first use the <code>CreateMembers</code> action to create the member account in Security Hub CSPM.</p> <p>When the account owner enables Security Hub CSPM and accepts the invitation to become a member account, the administrator account can view the findings generated in the member account.</p>

        Args:
            account_ids: <p>The list of account IDs of the Amazon Web Services accounts to invite to Security Hub CSPM as members. </p>

        Examples:
            To invite accounts to become members
            The following example invites the specified AWS accounts to become member accounts associated with the calling Security Hub administrator account. You only use this operation to invite accounts that don't belong to an AWS Organizations organization.

            >>> client.invite_members(account_ids=['111122223333', '444455556666'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.invite_members_request.InviteMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.invite_members_response.InviteMembersResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.invite_members

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.invite_members.invite_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.invite_members_request.InviteMembersRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_aggregators_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.list_aggregators_v2_response.ListAggregatorsV2Response":
        """<p>Retrieves a list of V2 aggregators.</p>

        Args:
            next_token: <p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_aggregators_v2_request.ListAggregatorsV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_aggregators_v2_response.ListAggregatorsV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_aggregators_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_aggregators_v2.list_aggregators_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_aggregators_v2_request.ListAggregatorsV2Request = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_aggregators_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.aggregator_v2.AggregatorV2]":
        _token = next_token
        while True:
            _response = self.list_aggregators_v2(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("aggregators_v2",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_automation_rules(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.list_automation_rules_response.ListAutomationRulesResponse":
        """<p> A list of automation rules and their metadata for the calling account. </p>

        Args:
            next_token: <p> A token to specify where to start paginating the response. This is the <code>NextToken</code> from a previously truncated response. On your first call to the <code>ListAutomationRules</code> API, set the value of this parameter to <code>NULL</code>. </p>
            max_results: <p> The maximum number of rules to return in the response. This currently ranges from 1 to 100. </p>

        Examples:
            To list automation rules
            The following example lists automation rules and rule metadata in the calling account.

            >>> client.list_automation_rules(next_token='example-token', max_results=2)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_automation_rules_request.ListAutomationRulesRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_automation_rules_response.ListAutomationRulesResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_automation_rules

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_automation_rules.list_automation_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_automation_rules_request.ListAutomationRulesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_automation_rules_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.list_automation_rules_v2_response.ListAutomationRulesV2Response":
        """<p>Returns a list of automation rules and metadata for the calling account.</p>

        Args:
            next_token: <p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_automation_rules_v2_request.ListAutomationRulesV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_automation_rules_v2_response.ListAutomationRulesV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_automation_rules_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_automation_rules_v2.list_automation_rules_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_automation_rules_v2_request.ListAutomationRulesV2Request = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_configuration_policies(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.list_configuration_policies_response.ListConfigurationPoliciesResponse":
        """<p> Lists the configuration policies that the Security Hub CSPM delegated administrator has created for your organization. Only the delegated administrator can invoke this operation from the home Region. </p>

        Args:
            next_token: <p> The NextToken value that's returned from a previous paginated <code>ListConfigurationPolicies</code> request where <code>MaxResults</code> was used but the results exceeded the value of that parameter. Pagination continues from the <code>MaxResults</code> was used but the results exceeded the value of that parameter. Pagination continues from the end of the previous response that returned the <code>NextToken</code> value. This value is <code>null</code> when there are no more results to return. </p>
            max_results: <p> The maximum number of results that's returned by <code>ListConfigurationPolicies</code> in each page of the response. When this parameter is used, <code>ListConfigurationPolicies</code> returns the specified number of results in a single page and a <code>NextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListConfigurationPolicies</code> request with the returned <code>NextToken</code> value. A valid range for <code>MaxResults</code> is between 1 and 100. </p>

        Examples:
            To view a list of configuration policies
            This operation provides a list of your configuration policies, including metadata for each policy.

            >>> client.list_configuration_policies(next_token='U1FsdGVkX19nBV2zoh+Gou9NgnulLJHWpn9xnG4hqSOhvw3o2JqjI86QDxdf', max_results=1)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_configuration_policies_request.ListConfigurationPoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_configuration_policies_response.ListConfigurationPoliciesResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_configuration_policies

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_configuration_policies.list_configuration_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_configuration_policies_request.ListConfigurationPoliciesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_configuration_policies(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.configuration_policy_summary.ConfigurationPolicySummary]":
        _token = next_token
        while True:
            _response = self.list_configuration_policies(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("configuration_policy_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_configuration_policy_associations(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.association_filters.AssociationFilters"
        ] = None,
    ) -> "aws_sdk_securityhub.types.list_configuration_policy_associations_response.ListConfigurationPolicyAssociationsResponse":
        """<p> Provides information about the associations for your configuration policies and self-managed behavior. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            next_token: <p> The <code>NextToken</code> value that's returned from a previous paginated <code>ListConfigurationPolicyAssociations</code> request where <code>MaxResults</code> was used but the results exceeded the value of that parameter. Pagination continues from the end of the previous response that returned the <code>NextToken</code> value. This value is <code>null</code> when there are no more results to return. </p>
            max_results: <p> The maximum number of results that's returned by <code>ListConfigurationPolicies</code> in each page of the response. When this parameter is used, <code>ListConfigurationPolicyAssociations</code> returns the specified number of results in a single page and a <code>NextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListConfigurationPolicyAssociations</code> request with the returned <code>NextToken</code> value. A valid range for <code>MaxResults</code> is between 1 and 100. </p>
            filters: <p> Options for filtering the <code>ListConfigurationPolicyAssociations</code> response. You can filter by the Amazon Resource Name (ARN) or universally unique identifier (UUID) of a configuration, <code>AssociationType</code>, or <code>AssociationStatus</code>. </p>

        Examples:
            To list configuration associations
            This operation lists all of the associations between targets and configuration policies or self-managed behavior. Targets can include accounts, organizational units, or the root.

            >>> client.list_configuration_policy_associations(next_token='U1FsdGVkX19nBV2zoh+Gou9NgnulLJHWpn9xnG4hqSOhvw3o2JqjI86QDxdf', max_results=1, filters={'AssociationType': 'APPLIED'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_configuration_policy_associations_request.ListConfigurationPolicyAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_configuration_policy_associations_response.ListConfigurationPolicyAssociationsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_configuration_policy_associations

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_configuration_policy_associations.list_configuration_policy_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_configuration_policy_associations_request.ListConfigurationPolicyAssociationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_configuration_policy_associations(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.association_filters.AssociationFilters"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.configuration_policy_association_summary.ConfigurationPolicyAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_configuration_policy_associations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(
                _response, ("configuration_policy_association_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_connectors_v2(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
        provider_name: Optional[
            "aws_sdk_securityhub.types.connector_provider_name.ConnectorProviderName"
        ] = None,
        connector_status: Optional[
            "aws_sdk_securityhub.types.connector_status.ConnectorStatus"
        ] = None,
    ) -> (
        "aws_sdk_securityhub.types.list_connectors_v2_response.ListConnectorsV2Response"
    ):
        """<p>Grants permission to retrieve a list of connectorsV2 and their metadata for the calling account.</p>

        Args:
            next_token: <p>The pagination token per the Amazon Web Services Pagination standard</p>
            max_results: <p>The maximum number of results to be returned.</p>
            provider_name: <p>The name of the third-party provider.</p>
            connector_status: <p>The status for the connectorV2.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_connectors_v2_request.ListConnectorsV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_connectors_v2_response.ListConnectorsV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_connectors_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_connectors_v2.list_connectors_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_connectors_v2_request.ListConnectorsV2Request = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if provider_name is not None:
            input_["provider_name"] = provider_name
        if connector_status is not None:
            input_["connector_status"] = connector_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_enabled_products_for_import(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.list_enabled_products_for_import_response.ListEnabledProductsForImportResponse":
        """<p>Lists all findings-generating solutions (products) that you are subscribed to receive findings from in Security Hub CSPM.</p>

        Args:
            next_token: <p>The token that is required for pagination. On your first call to the <code>ListEnabledProductsForImport</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
            max_results: <p>The maximum number of items to return in the response.</p>

        Examples:
            To list ARNs for enabled integrations
            The following example returns a list of subscription Amazon Resource Names (ARNs) for the product integrations that you have currently enabled in Security Hub.

            >>> client.list_enabled_products_for_import()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_enabled_products_for_import_request.ListEnabledProductsForImportRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_enabled_products_for_import_response.ListEnabledProductsForImportResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_enabled_products_for_import

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_enabled_products_for_import.list_enabled_products_for_import(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_enabled_products_for_import_request.ListEnabledProductsForImportRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_enabled_products_for_import(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = self.list_enabled_products_for_import(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("product_subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_finding_aggregators(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.list_finding_aggregators_response.ListFindingAggregatorsResponse":
        """<p>If cross-Region aggregation is enabled, then <code>ListFindingAggregators</code> returns the Amazon Resource Name (ARN) of the finding aggregator. You can run this operation from any Amazon Web Services Region.</p>

        Args:
            next_token: <p>The token returned with the previous set of results. Identifies the next set of results to return.</p>
            max_results: <p>The maximum number of results to return. This operation currently only returns a single result.</p>

        Examples:
            To update the enablement status of a standard control
            The following example disables the specified control in the specified security standard.

            >>> client.list_finding_aggregators()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_finding_aggregators_request.ListFindingAggregatorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_finding_aggregators_response.ListFindingAggregatorsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_finding_aggregators

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_finding_aggregators.list_finding_aggregators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_finding_aggregators_request.ListFindingAggregatorsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_finding_aggregators(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.finding_aggregator.FindingAggregator]":
        _token = next_token
        while True:
            _response = self.list_finding_aggregators(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("finding_aggregators",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_invitations(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.cross_account_max_results.CrossAccountMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_securityhub.types.list_invitations_response.ListInvitationsResponse":
        r"""<note> <p>We recommend using Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html\">Managing Security Hub CSPM administrator and member accounts with Organizations</a> in the <i>Security Hub CSPM User Guide</i>.</p> </note> <p>Lists all Security Hub CSPM membership invitations that were sent to the calling account.</p> <p>Only accounts that are managed by invitation can use this operation. Accounts that are managed using the integration with Organizations don't receive invitations.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. </p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>ListInvitations</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_invitations_request.ListInvitationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_invitations_response.ListInvitationsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_invitations

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_invitations.list_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_invitations_request.ListInvitationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_invitations(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.cross_account_max_results.CrossAccountMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.invitation.Invitation]":
        _token = next_token
        while True:
            _response = self.list_invitations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("invitations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_members(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        only_associated: Optional["aws_sdk_securityhub.types.boolean.Boolean"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.cross_account_max_results.CrossAccountMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_securityhub.types.list_members_response.ListMembersResponse":
        """<p>Lists details about all member accounts for the current Security Hub CSPM administrator account.</p> <p>The results include both member accounts that belong to an organization and member accounts that were invited manually.</p>

        Args:
            only_associated: <p>Specifies which member accounts to include in the response based on their relationship status with the administrator account. The default value is <code>TRUE</code>.</p> <p>If <code>OnlyAssociated</code> is set to <code>TRUE</code>, the response includes member accounts whose relationship status with the administrator account is set to <code>ENABLED</code>.</p> <p>If <code>OnlyAssociated</code> is set to <code>FALSE</code>, the response includes all existing member accounts. </p>
            max_results: <p>The maximum number of items to return in the response. </p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>ListMembers</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_members_request.ListMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_members_response.ListMembersResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_members

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_members.list_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_members_request.ListMembersRequest = {}  # type: ignore[typeddict-item]
        if only_associated is not None:
            input_["only_associated"] = only_associated
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_members(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        only_associated: Optional["aws_sdk_securityhub.types.boolean.Boolean"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.cross_account_max_results.CrossAccountMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.member.Member]":
        _token = next_token
        while True:
            _response = self.list_members(
                config_overrides=config_overrides,
                only_associated=only_associated,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.admins_max_results.AdminsMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        feature: Optional[
            "aws_sdk_securityhub.types.security_hub_feature.SecurityHubFeature"
        ] = None,
    ) -> "aws_sdk_securityhub.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse":
        """<p>Lists the Security Hub CSPM administrator accounts. Can only be called by the organization management account.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response.</p>
            next_token: <p>The token that is required for pagination. On your first call to the <code>ListOrganizationAdminAccounts</code> operation, set the value of this parameter to <code>NULL</code>. For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response. </p>
            feature: <p>The feature where the delegated administrator account is listed. Defaults to Security Hub CSPM if not specified.</p>

        Examples:
            To list administrator acccounts for an organization
            The following example lists the Security  Hub administrator accounts for an organization. Only the organization management account can call this operation.

            >>> client.list_organization_admin_accounts()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_organization_admin_accounts

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_organization_admin_accounts.list_organization_admin_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if feature is not None:
            input_["feature"] = feature

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.admins_max_results.AdminsMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        feature: Optional[
            "aws_sdk_securityhub.types.security_hub_feature.SecurityHubFeature"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.admin_account.AdminAccount]":
        _token = next_token
        while True:
            _response = self.list_organization_admin_accounts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                feature=feature,
            )
            _page = _resolve_path(_response, ("admin_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_security_control_definitions(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        standards_arn: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.list_security_control_definitions_response.ListSecurityControlDefinitionsResponse":
        """<p> Lists all of the security controls that apply to a specified standard. </p>

        Args:
            standards_arn: <p> The Amazon Resource Name (ARN) of the standard that you want to view controls for. </p>
            next_token: <p> Optional pagination parameter. </p>
            max_results: <p> An optional parameter that limits the total results of the API response to the specified number. If this parameter isn't provided in the request, the results include the first 25 security controls that apply to the specified standard. The results also include a <code>NextToken</code> parameter that you can use in a subsequent API call to get the next 25 controls. This repeats until all controls for the standard are returned. </p>

        Examples:
            To list security controls that apply to a standard
            The following example lists security controls that apply to a specified Security Hub standard.

            >>> client.list_security_control_definitions(standards_arn='arn:aws:securityhub:::standards/aws-foundational-security-best-practices/v/1.0.0', next_token='NULL', max_results=3)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_security_control_definitions_request.ListSecurityControlDefinitionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_security_control_definitions_response.ListSecurityControlDefinitionsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_security_control_definitions

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_security_control_definitions.list_security_control_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_security_control_definitions_request.ListSecurityControlDefinitionsRequest = {}  # type: ignore[typeddict-item]
        if standards_arn is not None:
            input_["standards_arn"] = standards_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_security_control_definitions(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        standards_arn: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.security_control_definition.SecurityControlDefinition]":
        _token = next_token
        while True:
            _response = self.list_security_control_definitions(
                config_overrides=config_overrides,
                standards_arn=standards_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("security_control_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_standards_control_associations(
        self,
        security_control_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityhub.types.list_standards_control_associations_response.ListStandardsControlAssociationsResponse":
        """<p> Specifies whether a control is currently enabled or disabled in each enabled standard in the calling account. </p> <p>This operation omits standards control associations for standard subscriptions where <code>StandardsControlsUpdatable</code> has value <code>NOT_READY_FOR_UPDATES</code>.</p>

        Args:
            security_control_id: <p> The identifier of the control (identified with <code>SecurityControlId</code>, <code>SecurityControlArn</code>, or a mix of both parameters) that you want to determine the enablement status of in each enabled standard. </p>
            next_token: <p> Optional pagination parameter. </p>
            max_results: <p> An optional parameter that limits the total results of the API response to the specified number. If this parameter isn't provided in the request, the results include the first 25 standard and control associations. The results also include a <code>NextToken</code> parameter that you can use in a subsequent API call to get the next 25 associations. This repeats until all associations for the specified control are returned. The number of results is limited by the number of supported Security Hub CSPM standards that you've enabled in the calling account. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_standards_control_associations_request.ListStandardsControlAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_standards_control_associations_response.ListStandardsControlAssociationsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_standards_control_associations

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_standards_control_associations.list_standards_control_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_standards_control_associations_request.ListStandardsControlAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["security_control_id"] = security_control_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_standards_control_associations(
        self,
        security_control_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        next_token: Optional["aws_sdk_securityhub.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityhub.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_securityhub.types.standards_control_association_summary.StandardsControlAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_standards_control_associations(
                security_control_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("standards_control_association_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_securityhub.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags associated with a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to retrieve tags for.</p>

        Examples:
            To get a list of tags for a resource
            The following example returns a list of tags associated with the specified resource.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:securityhub:us-west-1:123456789012:hub/default')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_connector_v2(
        self,
        auth_code: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        auth_state: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.register_connector_v2_response.RegisterConnectorV2Response":
        """<p>Grants permission to complete the authorization based on input parameters.</p>

        Args:
            auth_code: <p>The authCode retrieved from authUrl to complete the OAuth 2.0 authorization code flow.</p>
            auth_state: <p>The authState retrieved from authUrl to complete the OAuth 2.0 authorization code flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.register_connector_v2_request.RegisterConnectorV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.register_connector_v2_response.RegisterConnectorV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.register_connector_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.register_connector_v2.register_connector_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.register_connector_v2_request.RegisterConnectorV2Request = {}  # type: ignore[typeddict-item]
        input_["auth_code"] = auth_code
        input_["auth_state"] = auth_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_configuration_policy_association(
        self,
        configuration_policy_identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        target: "aws_sdk_securityhub.types.target.Target",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.start_configuration_policy_association_response.StartConfigurationPolicyAssociationResponse":
        """<p> Associates a target account, organizational unit, or the root with a specified configuration. The target can be associated with a configuration policy or self-managed behavior. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            configuration_policy_identifier: <p> The Amazon Resource Name (ARN) of a configuration policy, the universally unique identifier (UUID) of a configuration policy, or a value of <code>SELF_MANAGED_SECURITY_HUB</code> for a self-managed configuration. </p>
            target: <p> The identifier of the target account, organizational unit, or the root to associate with the specified configuration. </p>

        Examples:
            To associate a configuration with a target
            This operation associates a configuration policy or self-managed behavior with the target account, organizational unit, or the root.

            >>> client.start_configuration_policy_association(configuration_policy_identifier='arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', target={'AccountId': '111122223333'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.start_configuration_policy_association_request.StartConfigurationPolicyAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.start_configuration_policy_association_response.StartConfigurationPolicyAssociationResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.start_configuration_policy_association

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.start_configuration_policy_association.start_configuration_policy_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.start_configuration_policy_association_request.StartConfigurationPolicyAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["configuration_policy_identifier"] = configuration_policy_identifier
        input_["target"] = target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_configuration_policy_disassociation(
        self,
        configuration_policy_identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        target: Optional["aws_sdk_securityhub.types.target.Target"] = None,
    ) -> "aws_sdk_securityhub.types.start_configuration_policy_disassociation_response.StartConfigurationPolicyDisassociationResponse":
        """<p> Disassociates a target account, organizational unit, or the root from a specified configuration. When you disassociate a configuration from its target, the target inherits the configuration of the closest parent. If there’s no configuration to inherit, the target retains its settings but becomes a self-managed account. A target can be disassociated from a configuration policy or self-managed behavior. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            target: <p> The identifier of the target account, organizational unit, or the root to disassociate from the specified configuration. </p>
            configuration_policy_identifier: <p> The Amazon Resource Name (ARN) of a configuration policy, the universally unique identifier (UUID) of a configuration policy, or a value of <code>SELF_MANAGED_SECURITY_HUB</code> for a self-managed configuration. </p>

        Examples:
            To disassociate a configuration from a target
            This operation disassociates a configuration policy or self-managed behavior from the target account, organizational unit, or the root.

            >>> client.start_configuration_policy_disassociation(target={'RootId': 'r-f6g7h8i9j0example'}, configuration_policy_identifier='SELF_MANAGED_SECURITY_HUB')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.start_configuration_policy_disassociation_request.StartConfigurationPolicyDisassociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.start_configuration_policy_disassociation_response.StartConfigurationPolicyDisassociationResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.start_configuration_policy_disassociation

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.start_configuration_policy_disassociation.start_configuration_policy_disassociation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.start_configuration_policy_disassociation_request.StartConfigurationPolicyDisassociationRequest = {}  # type: ignore[typeddict-item]
        if target is not None:
            input_["target"] = target
        input_["configuration_policy_identifier"] = configuration_policy_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_securityhub.types.resource_arn.ResourceArn",
        tags: "aws_sdk_securityhub.types.tag_map.TagMap",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more tags to a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to apply the tags to.</p>
            tags: <p>The tags to add to the resource. You can add up to 50 tags at a time. The tag keys can be no longer than 128 characters. The tag values can be no longer than 256 characters.</p>

        Examples:
            To tag a resource
            The following example adds the 'Department' and 'Area' tags to the specified resource.

            >>> client.tag_resource(resource_arn='arn:aws:securityhub:us-west-1:123456789012:hub/default', tags={'Department': 'Operations', 'Area': 'USMidwest'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.tag_resource

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_securityhub.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_securityhub.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
    ) -> "aws_sdk_securityhub.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to remove the tags from.</p>
            tag_keys: <p>The tag keys associated with the tags to remove from the resource. You can remove up to 50 tags at a time.</p>

        Examples:
            To remove tags from a resource
            The following example removes the 'Department' tag from the specified resource.

            >>> client.untag_resource(resource_arn='arn:aws:securityhub:us-west-1:123456789012:hub/default', tag_keys=['Department'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.untag_resource

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_action_target(
        self,
        action_target_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        name: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_action_target_response.UpdateActionTargetResponse":
        """<p>Updates the name and description of a custom action target in Security Hub CSPM.</p>

        Args:
            action_target_arn: <p>The ARN of the custom action target to update.</p>
            name: <p>The updated name of the custom action target.</p>
            description: <p>The updated description for the custom action target.</p>

        Examples:
            To update the name and description of a custom action target
            The following example updates the name and description of a custom action target in Security Hub. You can create custom actions to automatically respond to Security Hub findings using Amazon EventBridge.

            >>> client.update_action_target(action_target_arn='arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation', name='Chat custom action', description='Sends specified findings to customer service chat')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_action_target_request.UpdateActionTargetRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_action_target_response.UpdateActionTargetResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_action_target

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_action_target.update_action_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_action_target_request.UpdateActionTargetRequest = {}  # type: ignore[typeddict-item]
        input_["action_target_arn"] = action_target_arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_aggregator_v2(
        self,
        aggregator_v2_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        region_linking_mode: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        linked_regions: Optional[
            "aws_sdk_securityhub.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_aggregator_v2_response.UpdateAggregatorV2Response":
        """<p>Udpates the configuration for the Aggregator V2.</p>

        Args:
            aggregator_v2_arn: <p>The ARN of the Aggregator V2.</p>
            region_linking_mode: <p>Determines how Amazon Web Services Regions should be linked to the Aggregator V2.</p>
            linked_regions: <p>A list of Amazon Web Services Regions linked to the aggegation Region.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_aggregator_v2_request.UpdateAggregatorV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_aggregator_v2_response.UpdateAggregatorV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_aggregator_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_aggregator_v2.update_aggregator_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_aggregator_v2_request.UpdateAggregatorV2Request = {}  # type: ignore[typeddict-item]
        input_["aggregator_v2_arn"] = aggregator_v2_arn
        input_["region_linking_mode"] = region_linking_mode
        if linked_regions is not None:
            input_["linked_regions"] = linked_regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_automation_rule_v2(
        self,
        identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        rule_status: Optional[
            "aws_sdk_securityhub.types.rule_status_v2.RuleStatusV2"
        ] = None,
        rule_order: Optional[
            "aws_sdk_securityhub.types.rule_order_value_v2.RuleOrderValueV2"
        ] = None,
        description: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        rule_name: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        criteria: Optional["aws_sdk_securityhub.types.criteria.Criteria"] = None,
        actions: Optional[
            "aws_sdk_securityhub.types.automation_rules_action_list_v2.AutomationRulesActionListV2"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_automation_rule_v2_response.UpdateAutomationRuleV2Response":
        """<p>Updates a V2 automation rule.</p>

        Args:
            identifier: <p>The ARN of the automation rule.</p>
            rule_status: <p>The status of the automation rule.</p>
            rule_order: <p>Represents a value for the rule priority.</p>
            description: <p>A description of the automation rule.</p>
            rule_name: <p>The name of the automation rule.</p>
            criteria: <p>The filtering type and configuration of the automation rule.</p>
            actions: <p>A list of actions to be performed when the rule criteria is met.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_automation_rule_v2_request.UpdateAutomationRuleV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_automation_rule_v2_response.UpdateAutomationRuleV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_automation_rule_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_automation_rule_v2.update_automation_rule_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_automation_rule_v2_request.UpdateAutomationRuleV2Request = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if rule_status is not None:
            input_["rule_status"] = rule_status
        if rule_order is not None:
            input_["rule_order"] = rule_order
        if description is not None:
            input_["description"] = description
        if rule_name is not None:
            input_["rule_name"] = rule_name
        if criteria is not None:
            input_["criteria"] = criteria
        if actions is not None:
            input_["actions"] = actions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_configuration_policy(
        self,
        identifier: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        name: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        updated_reason: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        configuration_policy: Optional[
            "aws_sdk_securityhub.types.policy.Policy"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_configuration_policy_response.UpdateConfigurationPolicyResponse":
        """<p> Updates a configuration policy. Only the Security Hub CSPM delegated administrator can invoke this operation from the home Region. </p>

        Args:
            identifier: <p> The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy. </p>
            name: <p> The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: <code>-, ., !, *, /</code>. </p>
            description: <p> The description of the configuration policy. </p>
            updated_reason: <p> The reason for updating the configuration policy. </p>
            configuration_policy: <p> An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls). </p> <p>When updating a configuration policy, provide a complete list of standards that you want to enable and a complete list of controls that you want to enable or disable. The updated configuration replaces the current configuration.</p>

        Examples:
            To update a configuration policy
            This operation updates the specified configuration policy.

            >>> client.update_configuration_policy(identifier='arn:aws:securityhub:us-east-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', name='TestConfigurationPolicy', description='Updated configuration policy for testing FSBP and CIS', updated_reason='Enabling ACM.2', configuration_policy={'SecurityHub': {'ServiceEnabled': True, 'EnabledStandardIdentifiers': ['arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0', 'arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0'], 'SecurityControlsConfiguration': {'DisabledSecurityControlIdentifiers': ['CloudWatch.1', 'CloudWatch.2'], 'SecurityControlCustomParameters': [{'SecurityControlId': 'ACM.1', 'Parameters': {'daysToExpiration': {'ValueType': 'CUSTOM', 'Value': {'Integer': 21}}}}]}}})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_configuration_policy_request.UpdateConfigurationPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_configuration_policy_response.UpdateConfigurationPolicyResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_configuration_policy

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_configuration_policy.update_configuration_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_configuration_policy_request.UpdateConfigurationPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if updated_reason is not None:
            input_["updated_reason"] = updated_reason
        if configuration_policy is not None:
            input_["configuration_policy"] = configuration_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_connector_v2(
        self,
        connector_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        description: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        provider: Optional[
            "aws_sdk_securityhub.types.provider_update_configuration.ProviderUpdateConfiguration"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_connector_v2_response.UpdateConnectorV2Response":
        """<p>Grants permission to update a connectorV2 based on its id and input parameters.</p>

        Args:
            connector_id: <p>The UUID of the connectorV2 to identify connectorV2 resource.</p>
            description: <p>The description of the connectorV2.</p>
            provider: <p>The third-party provider’s service configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_connector_v2_request.UpdateConnectorV2Request]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_connector_v2_response.UpdateConnectorV2Response"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_connector_v2

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_connector_v2.update_connector_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_connector_v2_request.UpdateConnectorV2Request = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id
        if description is not None:
            input_["description"] = description
        if provider is not None:
            input_["provider"] = provider

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_finding_aggregator(
        self,
        finding_aggregator_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        region_linking_mode: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        regions: Optional["aws_sdk_securityhub.types.string_list.StringList"] = None,
    ) -> "aws_sdk_securityhub.types.update_finding_aggregator_response.UpdateFindingAggregatorResponse":
        """<note> <p>The <i>aggregation Region</i> is now called the <i>home Region</i>.</p> </note> <p>Updates cross-Region aggregation settings. You can use this operation to update the Region linking mode and the list of included or excluded Amazon Web Services Regions. However, you can't use this operation to change the home Region.</p> <p>You can invoke this operation from the current home Region only. </p>

        Args:
            finding_aggregator_arn: <p>The ARN of the finding aggregator. To obtain the ARN, use <code>ListFindingAggregators</code>.</p>
            region_linking_mode: <p>Indicates whether to aggregate findings from all of the available Regions in the current partition. Also determines whether to automatically aggregate findings from new Regions as Security Hub CSPM supports them and you opt into them.</p> <p>The selected option also determines how to use the Regions provided in the Regions list.</p> <p>The options are as follows:</p> <ul> <li> <p> <code>ALL_REGIONS</code> - Aggregates findings from all of the Regions where Security Hub CSPM is enabled. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them. </p> </li> <li> <p> <code>ALL_REGIONS_EXCEPT_SPECIFIED</code> - Aggregates findings from all of the Regions where Security Hub CSPM is enabled, except for the Regions listed in the <code>Regions</code> parameter. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them. </p> </li> <li> <p> <code>SPECIFIED_REGIONS</code> - Aggregates findings only from the Regions listed in the <code>Regions</code> parameter. Security Hub CSPM does not automatically aggregate findings from new Regions. </p> </li> <li> <p> <code>NO_REGIONS</code> - Aggregates no data because no Regions are selected as linked Regions. </p> </li> </ul>
            regions: <p>If <code>RegionLinkingMode</code> is <code>ALL_REGIONS_EXCEPT_SPECIFIED</code>, then this is a space-separated list of Regions that don't replicate and send findings to the home Region.</p> <p>If <code>RegionLinkingMode</code> is <code>SPECIFIED_REGIONS</code>, then this is a space-separated list of Regions that do replicate and send findings to the home Region.</p> <p>An <code>InvalidInputException</code> error results if you populate this field while <code>RegionLinkingMode</code> is <code>NO_REGIONS</code>.</p>

        Examples:
            To update cross-Region aggregation settings
            The following example updates the cross-Region aggregation configuration. You use this operation to change the list of linked Regions and the treatment of new Regions. However, you cannot use this operation to change the aggregation Region.

            >>> client.update_finding_aggregator(finding_aggregator_arn='arn:aws:securityhub:us-east-1:123456789012:finding-aggregator/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', region_linking_mode='SPECIFIED_REGIONS', regions=['us-west-1', 'us-west-2'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_finding_aggregator_request.UpdateFindingAggregatorRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_finding_aggregator_response.UpdateFindingAggregatorResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_finding_aggregator

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_finding_aggregator.update_finding_aggregator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_finding_aggregator_request.UpdateFindingAggregatorRequest = {}  # type: ignore[typeddict-item]
        input_["finding_aggregator_arn"] = finding_aggregator_arn
        input_["region_linking_mode"] = region_linking_mode
        if regions is not None:
            input_["regions"] = regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_findings(
        self,
        filters: "aws_sdk_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        note: Optional["aws_sdk_securityhub.types.note_update.NoteUpdate"] = None,
        record_state: Optional[
            "aws_sdk_securityhub.types.record_state.RecordState"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_findings_response.UpdateFindingsResponse":
        """<p> <code>UpdateFindings</code> is a deprecated operation. Instead of <code>UpdateFindings</code>, use the <code>BatchUpdateFindings</code> operation.</p> <p>The <code>UpdateFindings</code> operation updates the <code>Note</code> and <code>RecordState</code> of the Security Hub CSPM aggregated findings that the filter attributes specify. Any member account that can view the finding can also see the update to the finding.</p> <p>Finding updates made with <code>UpdateFindings</code> aren't persisted if the same finding is later updated by the finding provider through the <code>BatchImportFindings</code> operation. In addition, Security Hub CSPM doesn't record updates made with <code>UpdateFindings</code> in the finding history.</p>

        Args:
            filters: <p>A collection of attributes that specify which findings you want to update.</p>
            note: <p>The updated note for the finding.</p>
            record_state: <p>The updated record state for the finding.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_findings_request.UpdateFindingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_findings_response.UpdateFindingsResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_findings

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_findings.update_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_findings_request.UpdateFindingsRequest = {}  # type: ignore[typeddict-item]
        input_["filters"] = filters
        if note is not None:
            input_["note"] = note
        if record_state is not None:
            input_["record_state"] = record_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_insight(
        self,
        insight_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        name: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
        filters: Optional[
            "aws_sdk_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
        ] = None,
        group_by_attribute: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_insight_response.UpdateInsightResponse":
        """<p>Updates the Security Hub CSPM insight identified by the specified insight ARN.</p>

        Args:
            insight_arn: <p>The ARN of the insight that you want to update.</p>
            name: <p>The updated name for the insight.</p>
            filters: <p>The updated filters that define this insight.</p>
            group_by_attribute: <p>The updated <code>GroupBy</code> attribute that defines this insight.</p>

        Examples:
            To update an insight
            The following example updates the specified Security Hub insight.

            >>> client.update_insight(insight_arn='arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', name='High severity role findings', filters={'ResourceType': [{'Comparison': 'EQUALS', 'Value': 'AwsIamRole'}], 'SeverityLabel': [{'Comparison': 'EQUALS', 'Value': 'HIGH'}]})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_insight_request.UpdateInsightRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_insight_response.UpdateInsightResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_insight

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_insight.update_insight(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_insight_request.UpdateInsightRequest = {}  # type: ignore[typeddict-item]
        input_["insight_arn"] = insight_arn
        if name is not None:
            input_["name"] = name
        if filters is not None:
            input_["filters"] = filters
        if group_by_attribute is not None:
            input_["group_by_attribute"] = group_by_attribute

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_organization_configuration(
        self,
        auto_enable: "aws_sdk_securityhub.types.boolean.Boolean",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        auto_enable_standards: Optional[
            "aws_sdk_securityhub.types.auto_enable_standards.AutoEnableStandards"
        ] = None,
        organization_configuration: Optional[
            "aws_sdk_securityhub.types.organization_configuration.OrganizationConfiguration"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse":
        r"""<p>Updates the configuration of your organization in Security Hub CSPM. Only the Security Hub CSPM administrator account can invoke this operation.</p>

        Args:
            auto_enable: <p>Whether to automatically enable Security Hub CSPM in new member accounts when they join the organization.</p> <p>If set to <code>true</code>, then Security Hub CSPM is automatically enabled in new accounts. If set to <code>false</code>, then Security Hub CSPM isn't enabled in new accounts automatically. The default value is <code>false</code>.</p> <p>If the <code>ConfigurationType</code> of your organization is set to <code>CENTRAL</code>, then this field is set to <code>false</code> and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which Security Hub CSPM is enabled and associate the policy with new organization accounts.</p>
            auto_enable_standards: <p>Whether to automatically enable Security Hub CSPM <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html\">default standards</a> in new member accounts when they join the organization.</p> <p>The default value of this parameter is equal to <code>DEFAULT</code>.</p> <p>If equal to <code>DEFAULT</code>, then Security Hub CSPM default standards are automatically enabled for new member accounts. If equal to <code>NONE</code>, then default standards are not automatically enabled for new member accounts.</p> <p>If the <code>ConfigurationType</code> of your organization is set to <code>CENTRAL</code>, then this field is set to <code>NONE</code> and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which specific security standards are enabled and associate the policy with new organization accounts.</p>

        Examples:
            To update organization configuration
            This operation updates the way your organization is configured in Security Hub. Only a Security Hub administrator account can invoke this operation.

            >>> client.update_organization_configuration(auto_enable=False, auto_enable_standards='NONE', organization_configuration={'ConfigurationType': 'CENTRAL'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_organization_configuration

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_organization_configuration.update_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["auto_enable"] = auto_enable
        if auto_enable_standards is not None:
            input_["auto_enable_standards"] = auto_enable_standards
        if organization_configuration is not None:
            input_["organization_configuration"] = organization_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_security_control(
        self,
        security_control_id: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        parameters: "aws_sdk_securityhub.types.parameters.Parameters",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        last_update_reason: Optional[
            "aws_sdk_securityhub.types.alpha_numeric_non_empty_string.AlphaNumericNonEmptyString"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_security_control_response.UpdateSecurityControlResponse":
        """<p> Updates the properties of a security control. </p>

        Args:
            security_control_id: <p> The Amazon Resource Name (ARN) or ID of the control to update. </p>
            parameters: <p> An object that specifies which security control parameters to update. </p>
            last_update_reason: <p> The most recent reason for updating the properties of the security control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores. </p>

        Examples:
            To update security control properties
            The following example updates the specified security control. Specifically, this example updates control parameters.

            >>> client.update_security_control(security_control_id='ACM.1', parameters={'maxCredentialUsageAge': {'ValueType': 'CUSTOM', 'Value': {'Integer': 15}}}, last_update_reason='Comply with internal requirements')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_security_control_request.UpdateSecurityControlRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_security_control_response.UpdateSecurityControlResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_security_control

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_security_control.update_security_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_security_control_request.UpdateSecurityControlRequest = {}  # type: ignore[typeddict-item]
        input_["security_control_id"] = security_control_id
        input_["parameters"] = parameters
        if last_update_reason is not None:
            input_["last_update_reason"] = last_update_reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_security_hub_configuration(
        self,
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        auto_enable_controls: Optional[
            "aws_sdk_securityhub.types.boolean.Boolean"
        ] = None,
        control_finding_generator: Optional[
            "aws_sdk_securityhub.types.control_finding_generator.ControlFindingGenerator"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_security_hub_configuration_response.UpdateSecurityHubConfigurationResponse":
        """<p>Updates configuration options for Security Hub CSPM.</p>

        Args:
            auto_enable_controls: <p>Whether to automatically enable new controls when they are added to standards that are enabled.</p> <p>By default, this is set to <code>true</code>, and new controls are enabled automatically. To not automatically enable new controls, set this to <code>false</code>. </p> <p>When you automatically enable new controls, you can interact with the controls in the console and programmatically immediately after release. However, automatically enabled controls have a temporary default status of <code>DISABLED</code>. It can take up to several days for Security Hub CSPM to process the control release and designate the control as <code>ENABLED</code> in your account. During the processing period, you can manually enable or disable a control, and Security Hub CSPM will maintain that designation regardless of whether you have <code>AutoEnableControls</code> set to <code>true</code>.</p>
            control_finding_generator: <p>Updates whether the calling account has consolidated control findings turned on. If the value for this field is set to <code>SECURITY_CONTROL</code>, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.</p> <p>If the value for this field is set to <code>STANDARD_CONTROL</code>, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.</p> <p>For accounts that are part of an organization, this value can only be updated in the administrator account.</p>

        Examples:
            To update Security Hub settings
            The following example updates Security Hub settings to turn on consolidated control findings, and to automatically enable new controls in enabled standards.

            >>> client.update_security_hub_configuration(auto_enable_controls=True, control_finding_generator='SECURITY_CONTROL')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_security_hub_configuration_request.UpdateSecurityHubConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_security_hub_configuration_response.UpdateSecurityHubConfigurationResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_security_hub_configuration

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_security_hub_configuration.update_security_hub_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_security_hub_configuration_request.UpdateSecurityHubConfigurationRequest = {}  # type: ignore[typeddict-item]
        if auto_enable_controls is not None:
            input_["auto_enable_controls"] = auto_enable_controls
        if control_finding_generator is not None:
            input_["control_finding_generator"] = control_finding_generator

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_standards_control(
        self,
        standards_control_arn: "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[SecurityHubClientConfig] = None,
        control_status: Optional[
            "aws_sdk_securityhub.types.control_status.ControlStatus"
        ] = None,
        disabled_reason: Optional[
            "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "aws_sdk_securityhub.types.update_standards_control_response.UpdateStandardsControlResponse":
        """<p>Used to control whether an individual security standard control is enabled or disabled.</p> <p>Calls to this operation return a <code>RESOURCE_NOT_FOUND_EXCEPTION</code> error when the standard subscription for the control has <code>StandardsControlsUpdatable</code> value <code>NOT_READY_FOR_UPDATES</code>.</p>

        Args:
            standards_control_arn: <p>The ARN of the security standard control to enable or disable.</p>
            control_status: <p>The updated status of the security standard control.</p>
            disabled_reason: <p>A description of the reason why you are disabling a security standard control. If you are disabling a control, then this is required.</p>

        Examples:
            To update the enablement status of a standard control
            The following example disables the specified control in the specified security standard.

            >>> client.update_standards_control(standards_control_arn='arn:aws:securityhub:us-west-1:123456789012:control/pci-dss/v/3.2.1/PCI.AutoScaling.1', control_status='DISABLED', disabled_reason='Not applicable to my service')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityhub.types.update_standards_control_request.UpdateStandardsControlRequest]",
        ) -> OperationResponse[
            "aws_sdk_securityhub.types.update_standards_control_response.UpdateStandardsControlResponse"
        ]:
            import aws_sdk_securityhub._operations.security_hub_api_service.update_standards_control

            output, http_response = (
                aws_sdk_securityhub._operations.security_hub_api_service.update_standards_control.update_standards_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityhub.types.update_standards_control_request.UpdateStandardsControlRequest = {}  # type: ignore[typeddict-item]
        input_["standards_control_arn"] = standards_control_arn
        if control_status is not None:
            input_["control_status"] = control_status
        if disabled_reason is not None:
            input_["disabled_reason"] = disabled_reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
