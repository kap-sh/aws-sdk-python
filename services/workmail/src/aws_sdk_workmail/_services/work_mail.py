"""Generated from Smithy shape ``com.amazonaws.workmail#WorkMailService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_workmail._auth._signers
import aws_sdk_workmail._auth._sigv4
from aws_sdk_workmail._auth._identity import Credentials
from aws_sdk_workmail._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_workmail._auth._zapros_handler import AuthMiddleware
from aws_sdk_workmail._pagination import resolve_path as _resolve_path
from aws_sdk_workmail._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_workmail.types.access_control_rule_action
    import aws_sdk_workmail.types.access_control_rule_description
    import aws_sdk_workmail.types.access_control_rule_effect
    import aws_sdk_workmail.types.access_control_rule_name
    import aws_sdk_workmail.types.actions_list
    import aws_sdk_workmail.types.amazon_resource_name
    import aws_sdk_workmail.types.application_arn
    import aws_sdk_workmail.types.associate_delegate_to_resource_request
    import aws_sdk_workmail.types.associate_delegate_to_resource_response
    import aws_sdk_workmail.types.associate_member_to_group_request
    import aws_sdk_workmail.types.associate_member_to_group_response
    import aws_sdk_workmail.types.assume_impersonation_role_request
    import aws_sdk_workmail.types.assume_impersonation_role_response
    import aws_sdk_workmail.types.availability_configuration
    import aws_sdk_workmail.types.booking_options
    import aws_sdk_workmail.types.boolean
    import aws_sdk_workmail.types.boolean_object
    import aws_sdk_workmail.types.cancel_mailbox_export_job_request
    import aws_sdk_workmail.types.cancel_mailbox_export_job_response
    import aws_sdk_workmail.types.create_alias_request
    import aws_sdk_workmail.types.create_alias_response
    import aws_sdk_workmail.types.create_availability_configuration_request
    import aws_sdk_workmail.types.create_availability_configuration_response
    import aws_sdk_workmail.types.create_group_request
    import aws_sdk_workmail.types.create_group_response
    import aws_sdk_workmail.types.create_identity_center_application_request
    import aws_sdk_workmail.types.create_identity_center_application_response
    import aws_sdk_workmail.types.create_impersonation_role_request
    import aws_sdk_workmail.types.create_impersonation_role_response
    import aws_sdk_workmail.types.create_mobile_device_access_rule_request
    import aws_sdk_workmail.types.create_mobile_device_access_rule_response
    import aws_sdk_workmail.types.create_organization_request
    import aws_sdk_workmail.types.create_organization_response
    import aws_sdk_workmail.types.create_resource_request
    import aws_sdk_workmail.types.create_resource_response
    import aws_sdk_workmail.types.create_user_request
    import aws_sdk_workmail.types.create_user_response
    import aws_sdk_workmail.types.delete_access_control_rule_request
    import aws_sdk_workmail.types.delete_access_control_rule_response
    import aws_sdk_workmail.types.delete_alias_request
    import aws_sdk_workmail.types.delete_alias_response
    import aws_sdk_workmail.types.delete_availability_configuration_request
    import aws_sdk_workmail.types.delete_availability_configuration_response
    import aws_sdk_workmail.types.delete_email_monitoring_configuration_request
    import aws_sdk_workmail.types.delete_email_monitoring_configuration_response
    import aws_sdk_workmail.types.delete_group_request
    import aws_sdk_workmail.types.delete_group_response
    import aws_sdk_workmail.types.delete_identity_center_application_request
    import aws_sdk_workmail.types.delete_identity_center_application_response
    import aws_sdk_workmail.types.delete_identity_provider_configuration_request
    import aws_sdk_workmail.types.delete_identity_provider_configuration_response
    import aws_sdk_workmail.types.delete_impersonation_role_request
    import aws_sdk_workmail.types.delete_impersonation_role_response
    import aws_sdk_workmail.types.delete_mailbox_permissions_request
    import aws_sdk_workmail.types.delete_mailbox_permissions_response
    import aws_sdk_workmail.types.delete_mobile_device_access_override_request
    import aws_sdk_workmail.types.delete_mobile_device_access_override_response
    import aws_sdk_workmail.types.delete_mobile_device_access_rule_request
    import aws_sdk_workmail.types.delete_mobile_device_access_rule_response
    import aws_sdk_workmail.types.delete_organization_request
    import aws_sdk_workmail.types.delete_organization_response
    import aws_sdk_workmail.types.delete_personal_access_token_request
    import aws_sdk_workmail.types.delete_personal_access_token_response
    import aws_sdk_workmail.types.delete_resource_request
    import aws_sdk_workmail.types.delete_resource_response
    import aws_sdk_workmail.types.delete_retention_policy_request
    import aws_sdk_workmail.types.delete_retention_policy_response
    import aws_sdk_workmail.types.delete_user_request
    import aws_sdk_workmail.types.delete_user_response
    import aws_sdk_workmail.types.deregister_from_work_mail_request
    import aws_sdk_workmail.types.deregister_from_work_mail_response
    import aws_sdk_workmail.types.deregister_mail_domain_request
    import aws_sdk_workmail.types.deregister_mail_domain_response
    import aws_sdk_workmail.types.describe_email_monitoring_configuration_request
    import aws_sdk_workmail.types.describe_email_monitoring_configuration_response
    import aws_sdk_workmail.types.describe_entity_request
    import aws_sdk_workmail.types.describe_entity_response
    import aws_sdk_workmail.types.describe_group_request
    import aws_sdk_workmail.types.describe_group_response
    import aws_sdk_workmail.types.describe_identity_provider_configuration_request
    import aws_sdk_workmail.types.describe_identity_provider_configuration_response
    import aws_sdk_workmail.types.describe_inbound_dmarc_settings_request
    import aws_sdk_workmail.types.describe_inbound_dmarc_settings_response
    import aws_sdk_workmail.types.describe_mailbox_export_job_request
    import aws_sdk_workmail.types.describe_mailbox_export_job_response
    import aws_sdk_workmail.types.describe_organization_request
    import aws_sdk_workmail.types.describe_organization_response
    import aws_sdk_workmail.types.describe_resource_request
    import aws_sdk_workmail.types.describe_resource_response
    import aws_sdk_workmail.types.describe_user_request
    import aws_sdk_workmail.types.describe_user_response
    import aws_sdk_workmail.types.description
    import aws_sdk_workmail.types.device_id
    import aws_sdk_workmail.types.device_model
    import aws_sdk_workmail.types.device_model_list
    import aws_sdk_workmail.types.device_operating_system
    import aws_sdk_workmail.types.device_operating_system_list
    import aws_sdk_workmail.types.device_type
    import aws_sdk_workmail.types.device_type_list
    import aws_sdk_workmail.types.device_user_agent
    import aws_sdk_workmail.types.device_user_agent_list
    import aws_sdk_workmail.types.directory_id
    import aws_sdk_workmail.types.disassociate_delegate_from_resource_request
    import aws_sdk_workmail.types.disassociate_delegate_from_resource_response
    import aws_sdk_workmail.types.disassociate_member_from_group_request
    import aws_sdk_workmail.types.disassociate_member_from_group_response
    import aws_sdk_workmail.types.domain_name
    import aws_sdk_workmail.types.domains
    import aws_sdk_workmail.types.email_address
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.ews_availability_provider
    import aws_sdk_workmail.types.folder_configurations
    import aws_sdk_workmail.types.get_access_control_effect_request
    import aws_sdk_workmail.types.get_access_control_effect_response
    import aws_sdk_workmail.types.get_default_retention_policy_request
    import aws_sdk_workmail.types.get_default_retention_policy_response
    import aws_sdk_workmail.types.get_impersonation_role_effect_request
    import aws_sdk_workmail.types.get_impersonation_role_effect_response
    import aws_sdk_workmail.types.get_impersonation_role_request
    import aws_sdk_workmail.types.get_impersonation_role_response
    import aws_sdk_workmail.types.get_mail_domain_request
    import aws_sdk_workmail.types.get_mail_domain_response
    import aws_sdk_workmail.types.get_mailbox_details_request
    import aws_sdk_workmail.types.get_mailbox_details_response
    import aws_sdk_workmail.types.get_mobile_device_access_effect_request
    import aws_sdk_workmail.types.get_mobile_device_access_effect_response
    import aws_sdk_workmail.types.get_mobile_device_access_override_request
    import aws_sdk_workmail.types.get_mobile_device_access_override_response
    import aws_sdk_workmail.types.get_personal_access_token_metadata_request
    import aws_sdk_workmail.types.get_personal_access_token_metadata_response
    import aws_sdk_workmail.types.group_name
    import aws_sdk_workmail.types.idempotency_client_token
    import aws_sdk_workmail.types.identity_center_application_name
    import aws_sdk_workmail.types.identity_center_configuration
    import aws_sdk_workmail.types.identity_provider_authentication_mode
    import aws_sdk_workmail.types.identity_provider_user_id
    import aws_sdk_workmail.types.identity_provider_user_id_for_update
    import aws_sdk_workmail.types.impersonation_role_description
    import aws_sdk_workmail.types.impersonation_role_id
    import aws_sdk_workmail.types.impersonation_role_id_list
    import aws_sdk_workmail.types.impersonation_role_name
    import aws_sdk_workmail.types.impersonation_role_type
    import aws_sdk_workmail.types.impersonation_rule_list
    import aws_sdk_workmail.types.instance_arn
    import aws_sdk_workmail.types.ip_address
    import aws_sdk_workmail.types.ip_range_list
    import aws_sdk_workmail.types.kms_key_arn
    import aws_sdk_workmail.types.lambda_availability_provider
    import aws_sdk_workmail.types.list_access_control_rules_request
    import aws_sdk_workmail.types.list_access_control_rules_response
    import aws_sdk_workmail.types.list_aliases_request
    import aws_sdk_workmail.types.list_aliases_response
    import aws_sdk_workmail.types.list_availability_configurations_request
    import aws_sdk_workmail.types.list_availability_configurations_response
    import aws_sdk_workmail.types.list_group_members_request
    import aws_sdk_workmail.types.list_group_members_response
    import aws_sdk_workmail.types.list_groups_filters
    import aws_sdk_workmail.types.list_groups_for_entity_filters
    import aws_sdk_workmail.types.list_groups_for_entity_request
    import aws_sdk_workmail.types.list_groups_for_entity_response
    import aws_sdk_workmail.types.list_groups_request
    import aws_sdk_workmail.types.list_groups_response
    import aws_sdk_workmail.types.list_impersonation_roles_request
    import aws_sdk_workmail.types.list_impersonation_roles_response
    import aws_sdk_workmail.types.list_mail_domains_request
    import aws_sdk_workmail.types.list_mail_domains_response
    import aws_sdk_workmail.types.list_mailbox_export_jobs_request
    import aws_sdk_workmail.types.list_mailbox_export_jobs_response
    import aws_sdk_workmail.types.list_mailbox_permissions_request
    import aws_sdk_workmail.types.list_mailbox_permissions_response
    import aws_sdk_workmail.types.list_mobile_device_access_overrides_request
    import aws_sdk_workmail.types.list_mobile_device_access_overrides_response
    import aws_sdk_workmail.types.list_mobile_device_access_rules_request
    import aws_sdk_workmail.types.list_mobile_device_access_rules_response
    import aws_sdk_workmail.types.list_organizations_request
    import aws_sdk_workmail.types.list_organizations_response
    import aws_sdk_workmail.types.list_personal_access_tokens_request
    import aws_sdk_workmail.types.list_personal_access_tokens_response
    import aws_sdk_workmail.types.list_resource_delegates_request
    import aws_sdk_workmail.types.list_resource_delegates_response
    import aws_sdk_workmail.types.list_resources_filters
    import aws_sdk_workmail.types.list_resources_request
    import aws_sdk_workmail.types.list_resources_response
    import aws_sdk_workmail.types.list_tags_for_resource_request
    import aws_sdk_workmail.types.list_tags_for_resource_response
    import aws_sdk_workmail.types.list_users_filters
    import aws_sdk_workmail.types.list_users_request
    import aws_sdk_workmail.types.list_users_response
    import aws_sdk_workmail.types.log_group_arn
    import aws_sdk_workmail.types.mailbox_export_job_id
    import aws_sdk_workmail.types.mailbox_quota
    import aws_sdk_workmail.types.max_results
    import aws_sdk_workmail.types.mobile_device_access_rule_description
    import aws_sdk_workmail.types.mobile_device_access_rule_effect
    import aws_sdk_workmail.types.mobile_device_access_rule_id
    import aws_sdk_workmail.types.mobile_device_access_rule_name
    import aws_sdk_workmail.types.new_resource_description
    import aws_sdk_workmail.types.next_token
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.organization_name
    import aws_sdk_workmail.types.password
    import aws_sdk_workmail.types.permission_values
    import aws_sdk_workmail.types.personal_access_token_configuration
    import aws_sdk_workmail.types.personal_access_token_id
    import aws_sdk_workmail.types.personal_access_token_summary
    import aws_sdk_workmail.types.policy_description
    import aws_sdk_workmail.types.put_access_control_rule_request
    import aws_sdk_workmail.types.put_access_control_rule_response
    import aws_sdk_workmail.types.put_email_monitoring_configuration_request
    import aws_sdk_workmail.types.put_email_monitoring_configuration_response
    import aws_sdk_workmail.types.put_identity_provider_configuration_request
    import aws_sdk_workmail.types.put_identity_provider_configuration_response
    import aws_sdk_workmail.types.put_inbound_dmarc_settings_request
    import aws_sdk_workmail.types.put_inbound_dmarc_settings_response
    import aws_sdk_workmail.types.put_mailbox_permissions_request
    import aws_sdk_workmail.types.put_mailbox_permissions_response
    import aws_sdk_workmail.types.put_mobile_device_access_override_request
    import aws_sdk_workmail.types.put_mobile_device_access_override_response
    import aws_sdk_workmail.types.put_retention_policy_request
    import aws_sdk_workmail.types.put_retention_policy_response
    import aws_sdk_workmail.types.register_mail_domain_request
    import aws_sdk_workmail.types.register_mail_domain_response
    import aws_sdk_workmail.types.register_to_work_mail_request
    import aws_sdk_workmail.types.register_to_work_mail_response
    import aws_sdk_workmail.types.reset_password_request
    import aws_sdk_workmail.types.reset_password_response
    import aws_sdk_workmail.types.resource_description
    import aws_sdk_workmail.types.resource_name
    import aws_sdk_workmail.types.resource_type
    import aws_sdk_workmail.types.role_arn
    import aws_sdk_workmail.types.s3_bucket_name
    import aws_sdk_workmail.types.s3_object_key
    import aws_sdk_workmail.types.short_string
    import aws_sdk_workmail.types.start_mailbox_export_job_request
    import aws_sdk_workmail.types.start_mailbox_export_job_response
    import aws_sdk_workmail.types.tag_key_list
    import aws_sdk_workmail.types.tag_list
    import aws_sdk_workmail.types.tag_resource_request
    import aws_sdk_workmail.types.tag_resource_response
    import aws_sdk_workmail.types.test_availability_configuration_request
    import aws_sdk_workmail.types.test_availability_configuration_response
    import aws_sdk_workmail.types.untag_resource_request
    import aws_sdk_workmail.types.untag_resource_response
    import aws_sdk_workmail.types.update_availability_configuration_request
    import aws_sdk_workmail.types.update_availability_configuration_response
    import aws_sdk_workmail.types.update_default_mail_domain_request
    import aws_sdk_workmail.types.update_default_mail_domain_response
    import aws_sdk_workmail.types.update_group_request
    import aws_sdk_workmail.types.update_group_response
    import aws_sdk_workmail.types.update_impersonation_role_request
    import aws_sdk_workmail.types.update_impersonation_role_response
    import aws_sdk_workmail.types.update_mailbox_quota_request
    import aws_sdk_workmail.types.update_mailbox_quota_response
    import aws_sdk_workmail.types.update_mobile_device_access_rule_request
    import aws_sdk_workmail.types.update_mobile_device_access_rule_response
    import aws_sdk_workmail.types.update_primary_email_address_request
    import aws_sdk_workmail.types.update_primary_email_address_response
    import aws_sdk_workmail.types.update_resource_request
    import aws_sdk_workmail.types.update_resource_response
    import aws_sdk_workmail.types.update_user_request
    import aws_sdk_workmail.types.update_user_response
    import aws_sdk_workmail.types.user_attribute
    import aws_sdk_workmail.types.user_id_list
    import aws_sdk_workmail.types.user_name
    import aws_sdk_workmail.types.user_role
    import aws_sdk_workmail.types.work_mail_domain_name
    import aws_sdk_workmail.types.work_mail_identifier


class WorkMailClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class WorkMailClient:
    """A client for the ``WorkMail`` service.

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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = WorkMailClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[WorkMailClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WorkMailClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    def associate_delegate_to_resource(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        resource_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.associate_delegate_to_resource_response.AssociateDelegateToResourceResponse":
        """<p>Adds a member (user or group) to the resource's set of delegates.</p>

        Args:
            organization_id: <p>The organization under which the resource exists.</p>
            resource_id: <p>The resource for which members (users or groups) are associated.</p> <p>The identifier can accept <i>ResourceId</i>, <i>Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Email address: resource@domain.tld</p> </li> <li> <p>Resource name: resource</p> </li> </ul>
            entity_id: <p>The member (user or group) to associate to the resource.</p> <p>The entity ID can accept <i>UserId or GroupID</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Entity: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity: entity</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.associate_delegate_to_resource_request.AssociateDelegateToResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.associate_delegate_to_resource_response.AssociateDelegateToResourceResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.associate_delegate_to_resource

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.associate_delegate_to_resource.associate_delegate_to_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.associate_delegate_to_resource_request.AssociateDelegateToResourceRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["resource_id"] = resource_id
        input_["entity_id"] = entity_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_member_to_group(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        group_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        member_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.associate_member_to_group_response.AssociateMemberToGroupResponse":
        """<p>Adds a member (user or group) to the group's set.</p>

        Args:
            organization_id: <p>The organization under which the group exists.</p>
            group_id: <p>The group to which the member (user or group) is associated.</p> <p>The identifier can accept <i>GroupId</i>, <i>Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: group@domain.tld</p> </li> <li> <p>Group name: group</p> </li> </ul>
            member_id: <p>The member (user or group) to associate to the group.</p> <p>The member ID can accept <i>UserID or GroupId</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Member: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: member@domain.tld</p> </li> <li> <p>Member name: member</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.associate_member_to_group_request.AssociateMemberToGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.associate_member_to_group_response.AssociateMemberToGroupResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.associate_member_to_group

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.associate_member_to_group.associate_member_to_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.associate_member_to_group_request.AssociateMemberToGroupRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["group_id"] = group_id
        input_["member_id"] = member_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def assume_impersonation_role(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        impersonation_role_id: "aws_sdk_workmail.types.impersonation_role_id.ImpersonationRoleId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.assume_impersonation_role_response.AssumeImpersonationRoleResponse":
        """<p>Assumes an impersonation role for the given WorkMail organization. This method returns an authentication token you can use to make impersonated calls.</p>

        Args:
            organization_id: <p>The WorkMail organization under which the impersonation role will be assumed.</p>
            impersonation_role_id: <p>The impersonation role ID to assume.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.assume_impersonation_role_request.AssumeImpersonationRoleRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.assume_impersonation_role_response.AssumeImpersonationRoleResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.assume_impersonation_role

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.assume_impersonation_role.assume_impersonation_role(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.assume_impersonation_role_request.AssumeImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["impersonation_role_id"] = impersonation_role_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_mailbox_export_job(
        self,
        client_token: "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken",
        job_id: "aws_sdk_workmail.types.mailbox_export_job_id.MailboxExportJobId",
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.cancel_mailbox_export_job_response.CancelMailboxExportJobResponse":
        """<p>Cancels a mailbox export job.</p> <note> <p>If the mailbox export job is near completion, it might not be possible to cancel it.</p> </note>

        Args:
            client_token: <p>The idempotency token for the client request.</p>
            job_id: <p>The job ID.</p>
            organization_id: <p>The organization ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.cancel_mailbox_export_job_request.CancelMailboxExportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.cancel_mailbox_export_job_response.CancelMailboxExportJobResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.cancel_mailbox_export_job

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.cancel_mailbox_export_job.cancel_mailbox_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.cancel_mailbox_export_job_request.CancelMailboxExportJobRequest = {}  # type: ignore[typeddict-item]
        input_["client_token"] = client_token
        input_["job_id"] = job_id
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_alias(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier",
        alias: "aws_sdk_workmail.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.create_alias_response.CreateAliasResponse":
        """<p>Adds an alias to the set of a given member (user or group) of WorkMail.</p>

        Args:
            organization_id: <p>The organization under which the member (user or group) exists.</p>
            entity_id: <p>The member (user or group) to which this alias is added.</p>
            alias: <p>The alias to add to the member set.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.create_alias_request.CreateAliasRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.create_alias_response.CreateAliasResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.create_alias

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.create_alias.create_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.create_alias_request.CreateAliasRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id
        input_["alias"] = alias

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_availability_configuration(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        domain_name: "aws_sdk_workmail.types.domain_name.DomainName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        client_token: Optional[
            "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
        ] = None,
        ews_provider: Optional[
            "aws_sdk_workmail.types.ews_availability_provider.EwsAvailabilityProvider"
        ] = None,
        lambda_provider: Optional[
            "aws_sdk_workmail.types.lambda_availability_provider.LambdaAvailabilityProvider"
        ] = None,
    ) -> "aws_sdk_workmail.types.create_availability_configuration_response.CreateAvailabilityConfigurationResponse":
        """<p>Creates an <code>AvailabilityConfiguration</code> for the given WorkMail organization and domain.</p>

        Args:
            client_token: <p>An idempotent token that ensures that an API request is executed only once.</p>
            organization_id: <p>The WorkMail organization for which the <code>AvailabilityConfiguration</code> will be created.</p>
            domain_name: <p>The domain to which the provider applies.</p>
            ews_provider: <p>Exchange Web Services (EWS) availability provider definition. The request must contain exactly one provider definition, either <code>EwsProvider</code> or <code>LambdaProvider</code>.</p>
            lambda_provider: <p>Lambda availability provider definition. The request must contain exactly one provider definition, either <code>EwsProvider</code> or <code>LambdaProvider</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.create_availability_configuration_request.CreateAvailabilityConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.create_availability_configuration_response.CreateAvailabilityConfigurationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.create_availability_configuration

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.create_availability_configuration.create_availability_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.create_availability_configuration_request.CreateAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["organization_id"] = organization_id
        input_["domain_name"] = domain_name
        if ews_provider is not None:
            input_["ews_provider"] = ews_provider
        if lambda_provider is not None:
            input_["lambda_provider"] = lambda_provider

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_group(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        name: "aws_sdk_workmail.types.group_name.GroupName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        hidden_from_global_address_list: Optional[
            "aws_sdk_workmail.types.boolean.Boolean"
        ] = None,
    ) -> "aws_sdk_workmail.types.create_group_response.CreateGroupResponse":
        """<p>Creates a group that can be used in WorkMail by calling the <a>RegisterToWorkMail</a> operation.</p>

        Args:
            organization_id: <p>The organization under which the group is to be created.</p>
            name: <p>The name of the group.</p>
            hidden_from_global_address_list: <p>If this parameter is enabled, the group will be hidden from the address book.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.create_group_request.CreateGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.create_group_response.CreateGroupResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.create_group

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.create_group.create_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.create_group_request.CreateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["name"] = name
        if hidden_from_global_address_list is not None:
            input_["hidden_from_global_address_list"] = hidden_from_global_address_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_identity_center_application(
        self,
        name: "aws_sdk_workmail.types.identity_center_application_name.IdentityCenterApplicationName",
        instance_arn: "aws_sdk_workmail.types.instance_arn.InstanceArn",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        client_token: Optional[
            "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
        ] = None,
    ) -> "aws_sdk_workmail.types.create_identity_center_application_response.CreateIdentityCenterApplicationResponse":
        """<p> Creates the WorkMail application in IAM Identity Center that can be used later in the WorkMail - IdC integration. For more information, see PutIdentityProviderConfiguration. This action does not affect the authentication settings for any WorkMail organizations. </p>

        Args:
            name: <p> The name of the IAM Identity Center application. </p>
            instance_arn: <p> The Amazon Resource Name (ARN) of the instance. </p>
            client_token: <p> The idempotency token associated with the request. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.create_identity_center_application_request.CreateIdentityCenterApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.create_identity_center_application_response.CreateIdentityCenterApplicationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.create_identity_center_application

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.create_identity_center_application.create_identity_center_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.create_identity_center_application_request.CreateIdentityCenterApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["instance_arn"] = instance_arn
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_impersonation_role(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        name: "aws_sdk_workmail.types.impersonation_role_name.ImpersonationRoleName",
        type: "aws_sdk_workmail.types.impersonation_role_type.ImpersonationRoleType",
        rules: "aws_sdk_workmail.types.impersonation_rule_list.ImpersonationRuleList",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        client_token: Optional[
            "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_workmail.types.impersonation_role_description.ImpersonationRoleDescription"
        ] = None,
    ) -> "aws_sdk_workmail.types.create_impersonation_role_response.CreateImpersonationRoleResponse":
        """<p>Creates an impersonation role for the given WorkMail organization.</p> <p> <i>Idempotency</i> ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries also complete successfully without performing any further actions.</p>

        Args:
            client_token: <p>The idempotency token for the client request.</p>
            organization_id: <p>The WorkMail organization to create the new impersonation role within.</p>
            name: <p>The name of the new impersonation role.</p>
            type: <p>The impersonation role's type. The available impersonation role types are <code>READ_ONLY</code> or <code>FULL_ACCESS</code>.</p>
            description: <p>The description of the new impersonation role.</p>
            rules: <p>The list of rules for the impersonation role.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.create_impersonation_role_request.CreateImpersonationRoleRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.create_impersonation_role_response.CreateImpersonationRoleResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.create_impersonation_role

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.create_impersonation_role.create_impersonation_role(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.create_impersonation_role_request.CreateImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["organization_id"] = organization_id
        input_["name"] = name
        input_["type"] = type
        if description is not None:
            input_["description"] = description
        input_["rules"] = rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_mobile_device_access_rule(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        name: "aws_sdk_workmail.types.mobile_device_access_rule_name.MobileDeviceAccessRuleName",
        effect: "aws_sdk_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        client_token: Optional[
            "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
        ] = None,
        device_types: Optional[
            "aws_sdk_workmail.types.device_type_list.DeviceTypeList"
        ] = None,
        not_device_types: Optional[
            "aws_sdk_workmail.types.device_type_list.DeviceTypeList"
        ] = None,
        device_models: Optional[
            "aws_sdk_workmail.types.device_model_list.DeviceModelList"
        ] = None,
        not_device_models: Optional[
            "aws_sdk_workmail.types.device_model_list.DeviceModelList"
        ] = None,
        device_operating_systems: Optional[
            "aws_sdk_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
        ] = None,
        not_device_operating_systems: Optional[
            "aws_sdk_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
        ] = None,
        device_user_agents: Optional[
            "aws_sdk_workmail.types.device_user_agent_list.DeviceUserAgentList"
        ] = None,
        not_device_user_agents: Optional[
            "aws_sdk_workmail.types.device_user_agent_list.DeviceUserAgentList"
        ] = None,
    ) -> "aws_sdk_workmail.types.create_mobile_device_access_rule_response.CreateMobileDeviceAccessRuleResponse":
        """<p>Creates a new mobile device access rule for the specified WorkMail organization.</p>

        Args:
            organization_id: <p>The WorkMail organization under which the rule will be created.</p>
            client_token: <p>The idempotency token for the client request.</p>
            name: <p>The rule name.</p>
            description: <p>The rule description.</p>
            effect: <p>The effect of the rule when it matches. Allowed values are <code>ALLOW</code> or <code>DENY</code>.</p>
            device_types: <p>Device types that the rule will match.</p>
            not_device_types: <p>Device types that the rule <b>will not</b> match. All other device types will match.</p>
            device_models: <p>Device models that the rule will match.</p>
            not_device_models: <p>Device models that the rule <b>will not</b> match. All other device models will match.</p>
            device_operating_systems: <p>Device operating systems that the rule will match.</p>
            not_device_operating_systems: <p>Device operating systems that the rule <b>will not</b> match. All other device operating systems will match.</p>
            device_user_agents: <p>Device user agents that the rule will match.</p>
            not_device_user_agents: <p>Device user agents that the rule <b>will not</b> match. All other device user agents will match.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.create_mobile_device_access_rule_request.CreateMobileDeviceAccessRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.create_mobile_device_access_rule_response.CreateMobileDeviceAccessRuleResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.create_mobile_device_access_rule

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.create_mobile_device_access_rule.create_mobile_device_access_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.create_mobile_device_access_rule_request.CreateMobileDeviceAccessRuleRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["effect"] = effect
        if device_types is not None:
            input_["device_types"] = device_types
        if not_device_types is not None:
            input_["not_device_types"] = not_device_types
        if device_models is not None:
            input_["device_models"] = device_models
        if not_device_models is not None:
            input_["not_device_models"] = not_device_models
        if device_operating_systems is not None:
            input_["device_operating_systems"] = device_operating_systems
        if not_device_operating_systems is not None:
            input_["not_device_operating_systems"] = not_device_operating_systems
        if device_user_agents is not None:
            input_["device_user_agents"] = device_user_agents
        if not_device_user_agents is not None:
            input_["not_device_user_agents"] = not_device_user_agents

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_organization(
        self,
        alias: "aws_sdk_workmail.types.organization_name.OrganizationName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        directory_id: Optional[
            "aws_sdk_workmail.types.directory_id.DirectoryId"
        ] = None,
        client_token: Optional[
            "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
        ] = None,
        domains: Optional["aws_sdk_workmail.types.domains.Domains"] = None,
        kms_key_arn: Optional["aws_sdk_workmail.types.kms_key_arn.KmsKeyArn"] = None,
        enable_interoperability: Optional[
            "aws_sdk_workmail.types.boolean.Boolean"
        ] = None,
    ) -> (
        "aws_sdk_workmail.types.create_organization_response.CreateOrganizationResponse"
    ):
        r"""<p>Creates a new WorkMail organization. Optionally, you can choose to associate an existing AWS Directory Service directory with your organization. If an AWS Directory Service directory ID is specified, the organization alias must match the directory alias. If you choose not to associate an existing directory with your organization, then we create a new WorkMail directory for you. For more information, see <a href=\"https://docs.aws.amazon.com/workmail/latest/adminguide/add_new_organization.html\">Adding an organization</a> in the <i>WorkMail Administrator Guide</i>.</p> <p>You can associate multiple email domains with an organization, then choose your default email domain from the WorkMail console. You can also associate a domain that is managed in an Amazon Route 53 public hosted zone. For more information, see <a href=\"https://docs.aws.amazon.com/workmail/latest/adminguide/add_domain.html\">Adding a domain</a> and <a href=\"https://docs.aws.amazon.com/workmail/latest/adminguide/default_domain.html\">Choosing the default domain</a> in the <i>WorkMail Administrator Guide</i>.</p> <p>Optionally, you can use a customer managed key from AWS Key Management Service (AWS KMS) to encrypt email for your organization. If you don't associate an AWS KMS key, WorkMail creates a default, AWS managed key for you.</p>

        Args:
            directory_id: <p>The AWS Directory Service directory ID.</p>
            alias: <p>The organization alias.</p>
            client_token: <p>The idempotency token associated with the request.</p>
            domains: <p>The email domains to associate with the organization.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of a customer managed key from AWS KMS.</p>
            enable_interoperability: <p>When <code>true</code>, allows organization interoperability between WorkMail and Microsoft Exchange. If <code>true</code>, you must include a AD Connector directory ID in the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.create_organization_request.CreateOrganizationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.create_organization_response.CreateOrganizationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.create_organization

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.create_organization.create_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.create_organization_request.CreateOrganizationRequest = {}  # type: ignore[typeddict-item]
        if directory_id is not None:
            input_["directory_id"] = directory_id
        input_["alias"] = alias
        if client_token is not None:
            input_["client_token"] = client_token
        if domains is not None:
            input_["domains"] = domains
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if enable_interoperability is not None:
            input_["enable_interoperability"] = enable_interoperability

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_resource(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        name: "aws_sdk_workmail.types.resource_name.ResourceName",
        type: "aws_sdk_workmail.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        description: Optional[
            "aws_sdk_workmail.types.resource_description.ResourceDescription"
        ] = None,
        hidden_from_global_address_list: Optional[
            "aws_sdk_workmail.types.boolean.Boolean"
        ] = None,
    ) -> "aws_sdk_workmail.types.create_resource_response.CreateResourceResponse":
        """<p>Creates a new WorkMail resource.</p>

        Args:
            organization_id: <p>The identifier associated with the organization for which the resource is created.</p>
            name: <p>The name of the new resource.</p>
            type: <p>The type of the new resource. The available types are <code>equipment</code> and <code>room</code>.</p>
            description: <p>Resource description.</p>
            hidden_from_global_address_list: <p>If this parameter is enabled, the resource will be hidden from the address book.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.create_resource_request.CreateResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.create_resource_response.CreateResourceResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.create_resource

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.create_resource.create_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.create_resource_request.CreateResourceRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["name"] = name
        input_["type"] = type
        if description is not None:
            input_["description"] = description
        if hidden_from_global_address_list is not None:
            input_["hidden_from_global_address_list"] = hidden_from_global_address_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_user(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        name: "aws_sdk_workmail.types.user_name.UserName",
        display_name: "aws_sdk_workmail.types.user_attribute.UserAttribute",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        password: Optional["aws_sdk_workmail.types.password.Password"] = None,
        role: Optional["aws_sdk_workmail.types.user_role.UserRole"] = None,
        first_name: Optional[
            "aws_sdk_workmail.types.user_attribute.UserAttribute"
        ] = None,
        last_name: Optional[
            "aws_sdk_workmail.types.user_attribute.UserAttribute"
        ] = None,
        hidden_from_global_address_list: Optional[
            "aws_sdk_workmail.types.boolean.Boolean"
        ] = None,
        identity_provider_user_id: Optional[
            "aws_sdk_workmail.types.identity_provider_user_id.IdentityProviderUserId"
        ] = None,
    ) -> "aws_sdk_workmail.types.create_user_response.CreateUserResponse":
        """<p>Creates a user who can be used in WorkMail by calling the <a>RegisterToWorkMail</a> operation.</p>

        Args:
            organization_id: <p>The identifier of the organization for which the user is created.</p>
            name: <p>The name for the new user. WorkMail directory user names have a maximum length of 64. All others have a maximum length of 20.</p>
            display_name: <p>The display name for the new user.</p>
            password: <p>The password for the new user.</p>
            role: <p>The role of the new user.</p> <p>You cannot pass <i>SYSTEM_USER</i> or <i>RESOURCE</i> role in a single request. When a user role is not selected, the default role of <i>USER</i> is selected.</p>
            first_name: <p>The first name of the new user.</p>
            last_name: <p>The last name of the new user. </p>
            hidden_from_global_address_list: <p>If this parameter is enabled, the user will be hidden from the address book.</p>
            identity_provider_user_id: <p>User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.create_user_response.CreateUserResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.create_user

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.create_user_request.CreateUserRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["name"] = name
        input_["display_name"] = display_name
        if password is not None:
            input_["password"] = password
        if role is not None:
            input_["role"] = role
        if first_name is not None:
            input_["first_name"] = first_name
        if last_name is not None:
            input_["last_name"] = last_name
        if hidden_from_global_address_list is not None:
            input_["hidden_from_global_address_list"] = hidden_from_global_address_list
        if identity_provider_user_id is not None:
            input_["identity_provider_user_id"] = identity_provider_user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_access_control_rule(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        name: "aws_sdk_workmail.types.access_control_rule_name.AccessControlRuleName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_access_control_rule_response.DeleteAccessControlRuleResponse":
        """<p>Deletes an access control rule for the specified WorkMail organization.</p> <note> <p>Deleting already deleted and non-existing rules does not produce an error. In those cases, the service sends back an HTTP 200 response with an empty HTTP body.</p> </note>

        Args:
            organization_id: <p>The identifier for the organization.</p>
            name: <p>The name of the access control rule.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_access_control_rule_request.DeleteAccessControlRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_access_control_rule_response.DeleteAccessControlRuleResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_access_control_rule

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_access_control_rule.delete_access_control_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_access_control_rule_request.DeleteAccessControlRuleRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_alias(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier",
        alias: "aws_sdk_workmail.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_alias_response.DeleteAliasResponse":
        """<p>Remove one or more specified aliases from a set of aliases for a given user.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the user exists.</p>
            entity_id: <p>The identifier for the member (user or group) from which to have the aliases removed.</p>
            alias: <p>The aliases to be removed from the user's set of aliases. Duplicate entries in the list are collapsed into single entries (the list is transformed into a set).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_alias_request.DeleteAliasRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_alias_response.DeleteAliasResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_alias

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_alias.delete_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_alias_request.DeleteAliasRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id
        input_["alias"] = alias

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_availability_configuration(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        domain_name: "aws_sdk_workmail.types.domain_name.DomainName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_availability_configuration_response.DeleteAvailabilityConfigurationResponse":
        """<p>Deletes the <code>AvailabilityConfiguration</code> for the given WorkMail organization and domain.</p>

        Args:
            organization_id: <p>The WorkMail organization for which the <code>AvailabilityConfiguration</code> will be deleted.</p>
            domain_name: <p>The domain for which the <code>AvailabilityConfiguration</code> will be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_availability_configuration_request.DeleteAvailabilityConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_availability_configuration_response.DeleteAvailabilityConfigurationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_availability_configuration

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_availability_configuration.delete_availability_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_availability_configuration_request.DeleteAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["domain_name"] = domain_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_email_monitoring_configuration(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_email_monitoring_configuration_response.DeleteEmailMonitoringConfigurationResponse":
        """<p>Deletes the email monitoring configuration for a specified organization.</p>

        Args:
            organization_id: <p>The ID of the organization from which the email monitoring configuration is deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_email_monitoring_configuration_request.DeleteEmailMonitoringConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_email_monitoring_configuration_response.DeleteEmailMonitoringConfigurationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_email_monitoring_configuration

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_email_monitoring_configuration.delete_email_monitoring_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_email_monitoring_configuration_request.DeleteEmailMonitoringConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_group(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        group_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_group_response.DeleteGroupResponse":
        """<p>Deletes a group from WorkMail.</p>

        Args:
            organization_id: <p>The organization that contains the group.</p>
            group_id: <p>The identifier of the group to be deleted.</p> <p>The identifier can be the <i>GroupId</i>, or <i>Groupname</i>. The following identity formats are available:</p> <ul> <li> <p>Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Group name: group</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_group_request.DeleteGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_group_response.DeleteGroupResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_group

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_group.delete_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_group_request.DeleteGroupRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["group_id"] = group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_identity_center_application(
        self,
        application_arn: "aws_sdk_workmail.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_identity_center_application_response.DeleteIdentityCenterApplicationResponse":
        """<p> Deletes the IAM Identity Center application from WorkMail. This action does not affect the authentication settings for any WorkMail organizations. </p>

        Args:
            application_arn: <p> The Amazon Resource Name (ARN) of the application. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_identity_center_application_request.DeleteIdentityCenterApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_identity_center_application_response.DeleteIdentityCenterApplicationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_identity_center_application

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_identity_center_application.delete_identity_center_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_identity_center_application_request.DeleteIdentityCenterApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_identity_provider_configuration(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_identity_provider_configuration_response.DeleteIdentityProviderConfigurationResponse":
        """<p> Disables the integration between IdC and WorkMail. Authentication will continue with the directory as it was before the IdC integration. You might have to reset your directory passwords and reconfigure your desktop and mobile email clients. </p>

        Args:
            organization_id: <p> The Organization ID. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_identity_provider_configuration_request.DeleteIdentityProviderConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_identity_provider_configuration_response.DeleteIdentityProviderConfigurationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_identity_provider_configuration

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_identity_provider_configuration.delete_identity_provider_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_identity_provider_configuration_request.DeleteIdentityProviderConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_impersonation_role(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        impersonation_role_id: "aws_sdk_workmail.types.impersonation_role_id.ImpersonationRoleId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_impersonation_role_response.DeleteImpersonationRoleResponse":
        """<p>Deletes an impersonation role for the given WorkMail organization.</p>

        Args:
            organization_id: <p>The WorkMail organization from which to delete the impersonation role.</p>
            impersonation_role_id: <p>The ID of the impersonation role to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_impersonation_role_request.DeleteImpersonationRoleRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_impersonation_role_response.DeleteImpersonationRoleResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_impersonation_role

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_impersonation_role.delete_impersonation_role(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_impersonation_role_request.DeleteImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["impersonation_role_id"] = impersonation_role_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_mailbox_permissions(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        grantee_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_mailbox_permissions_response.DeleteMailboxPermissionsResponse":
        """<p>Deletes permissions granted to a member (user or group).</p>

        Args:
            organization_id: <p>The identifier of the organization under which the member (user or group) exists.</p>
            entity_id: <p>The identifier of the entity that owns the mailbox.</p> <p>The identifier can be <i>UserId or Group Id</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>
            grantee_id: <p>The identifier of the entity for which to delete granted permissions.</p> <p>The identifier can be <i>UserId, ResourceID, or Group Id</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Grantee ID: 12345678-1234-1234-1234-123456789012,r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: grantee@domain.tld</p> </li> <li> <p>Grantee name: grantee</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_mailbox_permissions_request.DeleteMailboxPermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_mailbox_permissions_response.DeleteMailboxPermissionsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_mailbox_permissions

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_mailbox_permissions.delete_mailbox_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_mailbox_permissions_request.DeleteMailboxPermissionsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id
        input_["grantee_id"] = grantee_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_mobile_device_access_override(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        device_id: "aws_sdk_workmail.types.device_id.DeviceId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_mobile_device_access_override_response.DeleteMobileDeviceAccessOverrideResponse":
        """<p>Deletes the mobile device access override for the given WorkMail organization, user, and device.</p> <note> <p>Deleting already deleted and non-existing overrides does not produce an error. In those cases, the service sends back an HTTP 200 response with an empty HTTP body.</p> </note>

        Args:
            organization_id: <p>The WorkMail organization for which the access override will be deleted.</p>
            user_id: <p>The WorkMail user for which you want to delete the override. Accepts the following types of user identities:</p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>
            device_id: <p>The mobile device for which you delete the override. <code>DeviceId</code> is case insensitive.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_mobile_device_access_override_request.DeleteMobileDeviceAccessOverrideRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_mobile_device_access_override_response.DeleteMobileDeviceAccessOverrideResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_mobile_device_access_override

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_mobile_device_access_override.delete_mobile_device_access_override(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_mobile_device_access_override_request.DeleteMobileDeviceAccessOverrideRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["user_id"] = user_id
        input_["device_id"] = device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_mobile_device_access_rule(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        mobile_device_access_rule_id: "aws_sdk_workmail.types.mobile_device_access_rule_id.MobileDeviceAccessRuleId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_mobile_device_access_rule_response.DeleteMobileDeviceAccessRuleResponse":
        """<p>Deletes a mobile device access rule for the specified WorkMail organization.</p> <note> <p>Deleting already deleted and non-existing rules does not produce an error. In those cases, the service sends back an HTTP 200 response with an empty HTTP body.</p> </note>

        Args:
            organization_id: <p>The WorkMail organization under which the rule will be deleted.</p>
            mobile_device_access_rule_id: <p>The identifier of the rule to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_mobile_device_access_rule_request.DeleteMobileDeviceAccessRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_mobile_device_access_rule_response.DeleteMobileDeviceAccessRuleResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_mobile_device_access_rule

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_mobile_device_access_rule.delete_mobile_device_access_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_mobile_device_access_rule_request.DeleteMobileDeviceAccessRuleRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["mobile_device_access_rule_id"] = mobile_device_access_rule_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_organization(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        delete_directory: "aws_sdk_workmail.types.boolean.Boolean",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        client_token: Optional[
            "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
        ] = None,
        force_delete: Optional["aws_sdk_workmail.types.boolean.Boolean"] = None,
        delete_identity_center_application: Optional[
            "aws_sdk_workmail.types.boolean.Boolean"
        ] = None,
    ) -> (
        "aws_sdk_workmail.types.delete_organization_response.DeleteOrganizationResponse"
    ):
        r"""<p>Deletes an WorkMail organization and all underlying AWS resources managed by WorkMail as part of the organization. You can choose whether to delete the associated directory. For more information, see <a href=\"https://docs.aws.amazon.com/workmail/latest/adminguide/remove_organization.html\">Removing an organization</a> in the <i>WorkMail Administrator Guide</i>.</p>

        Args:
            client_token: <p>The idempotency token associated with the request.</p>
            organization_id: <p>The organization ID.</p>
            delete_directory: <p>If true, deletes the AWS Directory Service directory associated with the organization.</p>
            force_delete: <p>Deletes a WorkMail organization even if the organization has enabled users.</p>
            delete_identity_center_application: <p>Deletes IAM Identity Center application for WorkMail. This action does not affect authentication settings for any organization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_organization_request.DeleteOrganizationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_organization_response.DeleteOrganizationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_organization

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_organization.delete_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_organization_request.DeleteOrganizationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["organization_id"] = organization_id
        input_["delete_directory"] = delete_directory
        if force_delete is not None:
            input_["force_delete"] = force_delete
        if delete_identity_center_application is not None:
            input_["delete_identity_center_application"] = (
                delete_identity_center_application
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_personal_access_token(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        personal_access_token_id: "aws_sdk_workmail.types.personal_access_token_id.PersonalAccessTokenId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_personal_access_token_response.DeletePersonalAccessTokenResponse":
        """<p> Deletes the Personal Access Token from the provided WorkMail Organization. </p>

        Args:
            organization_id: <p> The Organization ID. </p>
            personal_access_token_id: <p> The Personal Access Token ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_personal_access_token_request.DeletePersonalAccessTokenRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_personal_access_token_response.DeletePersonalAccessTokenResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_personal_access_token

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_personal_access_token.delete_personal_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_personal_access_token_request.DeletePersonalAccessTokenRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["personal_access_token_id"] = personal_access_token_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_resource(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        resource_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_resource_response.DeleteResourceResponse":
        """<p>Deletes the specified resource.</p>

        Args:
            organization_id: <p>The identifier associated with the organization from which the resource is deleted.</p>
            resource_id: <p>The identifier of the resource to be deleted.</p> <p>The identifier can accept <i>ResourceId</i>, or <i>Resourcename</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Resource name: resource</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_resource_request.DeleteResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_resource_response.DeleteResourceResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_resource

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_resource.delete_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_resource_request.DeleteResourceRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["resource_id"] = resource_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_retention_policy(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        id: "aws_sdk_workmail.types.short_string.ShortString",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_retention_policy_response.DeleteRetentionPolicyResponse":
        """<p>Deletes the specified retention policy from the specified organization.</p>

        Args:
            organization_id: <p>The organization ID.</p>
            id: <p>The retention policy ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_retention_policy_request.DeleteRetentionPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_retention_policy_response.DeleteRetentionPolicyResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_retention_policy

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_retention_policy.delete_retention_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_retention_policy_request.DeleteRetentionPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_user(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.delete_user_response.DeleteUserResponse":
        """<p>Deletes a user from WorkMail and all subsequent systems. Before you can delete a user, the user state must be <code>DISABLED</code>. Use the <a>DescribeUser</a> action to confirm the user state.</p> <p>Deleting a user is permanent and cannot be undone. WorkMail archives user mailboxes for 30 days before they are permanently removed.</p>

        Args:
            organization_id: <p>The organization that contains the user to be deleted.</p>
            user_id: <p>The identifier of the user to be deleted.</p> <p>The identifier can be the <i>UserId</i> or <i>Username</i>. The following identity formats are available:</p> <ul> <li> <p>User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>User name: user</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.delete_user_response.DeleteUserResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.delete_user

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.delete_user.delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.delete_user_request.DeleteUserRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_from_work_mail(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.deregister_from_work_mail_response.DeregisterFromWorkMailResponse":
        """<p>Mark a user, group, or resource as no longer used in WorkMail. This action disassociates the mailbox and schedules it for clean-up. WorkMail keeps mailboxes for 30 days before they are permanently removed. The functionality in the console is <i>Disable</i>.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the WorkMail entity exists.</p>
            entity_id: <p>The identifier for the member to be updated.</p> <p>The identifier can be <i>UserId, ResourceId, or Group Id</i>, <i>Username, Resourcename, or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.deregister_from_work_mail_request.DeregisterFromWorkMailRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.deregister_from_work_mail_response.DeregisterFromWorkMailResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.deregister_from_work_mail

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.deregister_from_work_mail.deregister_from_work_mail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.deregister_from_work_mail_request.DeregisterFromWorkMailRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_mail_domain(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        domain_name: "aws_sdk_workmail.types.work_mail_domain_name.WorkMailDomainName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.deregister_mail_domain_response.DeregisterMailDomainResponse":
        """<p>Removes a domain from WorkMail, stops email routing to WorkMail, and removes the authorization allowing WorkMail use. SES keeps the domain because other applications may use it. You must first remove any email address used by WorkMail entities before you remove the domain.</p>

        Args:
            organization_id: <p>The WorkMail organization for which the domain will be deregistered.</p>
            domain_name: <p>The domain to deregister in WorkMail and SES.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.deregister_mail_domain_request.DeregisterMailDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.deregister_mail_domain_response.DeregisterMailDomainResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.deregister_mail_domain

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.deregister_mail_domain.deregister_mail_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.deregister_mail_domain_request.DeregisterMailDomainRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["domain_name"] = domain_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_email_monitoring_configuration(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.describe_email_monitoring_configuration_response.DescribeEmailMonitoringConfigurationResponse":
        """<p>Describes the current email monitoring configuration for a specified organization.</p>

        Args:
            organization_id: <p>The ID of the organization for which the email monitoring configuration is described.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.describe_email_monitoring_configuration_request.DescribeEmailMonitoringConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.describe_email_monitoring_configuration_response.DescribeEmailMonitoringConfigurationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.describe_email_monitoring_configuration

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.describe_email_monitoring_configuration.describe_email_monitoring_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.describe_email_monitoring_configuration_request.DescribeEmailMonitoringConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_entity(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        email: "aws_sdk_workmail.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.describe_entity_response.DescribeEntityResponse":
        """<p>Returns basic details about an entity in WorkMail. </p>

        Args:
            organization_id: <p>The identifier for the organization under which the entity exists.</p>
            email: <p>The email under which the entity exists.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.describe_entity_request.DescribeEntityRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.describe_entity_response.DescribeEntityResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.describe_entity

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.describe_entity.describe_entity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.describe_entity_request.DescribeEntityRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["email"] = email

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_group(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        group_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.describe_group_response.DescribeGroupResponse":
        """<p>Returns the data available for the group.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the group exists.</p>
            group_id: <p>The identifier for the group to be described.</p> <p>The identifier can accept <i>GroupId</i>, <i>Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: group@domain.tld</p> </li> <li> <p>Group name: group</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.describe_group_request.DescribeGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.describe_group_response.DescribeGroupResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.describe_group

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.describe_group.describe_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.describe_group_request.DescribeGroupRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["group_id"] = group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_identity_provider_configuration(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.describe_identity_provider_configuration_response.DescribeIdentityProviderConfigurationResponse":
        """<p> Returns detailed information on the current IdC setup for the WorkMail organization. </p>

        Args:
            organization_id: <p> The Organization ID. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.describe_identity_provider_configuration_request.DescribeIdentityProviderConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.describe_identity_provider_configuration_response.DescribeIdentityProviderConfigurationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.describe_identity_provider_configuration

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.describe_identity_provider_configuration.describe_identity_provider_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.describe_identity_provider_configuration_request.DescribeIdentityProviderConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_inbound_dmarc_settings(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.describe_inbound_dmarc_settings_response.DescribeInboundDmarcSettingsResponse":
        """<p>Lists the settings in a DMARC policy for a specified organization.</p>

        Args:
            organization_id: <p>Lists the ID of the given organization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.describe_inbound_dmarc_settings_request.DescribeInboundDmarcSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.describe_inbound_dmarc_settings_response.DescribeInboundDmarcSettingsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.describe_inbound_dmarc_settings

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.describe_inbound_dmarc_settings.describe_inbound_dmarc_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.describe_inbound_dmarc_settings_request.DescribeInboundDmarcSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_mailbox_export_job(
        self,
        job_id: "aws_sdk_workmail.types.mailbox_export_job_id.MailboxExportJobId",
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.describe_mailbox_export_job_response.DescribeMailboxExportJobResponse":
        """<p>Describes the current status of a mailbox export job.</p>

        Args:
            job_id: <p>The mailbox export job ID.</p>
            organization_id: <p>The organization ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.describe_mailbox_export_job_request.DescribeMailboxExportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.describe_mailbox_export_job_response.DescribeMailboxExportJobResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.describe_mailbox_export_job

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.describe_mailbox_export_job.describe_mailbox_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.describe_mailbox_export_job_request.DescribeMailboxExportJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_organization(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.describe_organization_response.DescribeOrganizationResponse":
        """<p>Provides more information regarding a given organization based on its identifier.</p>

        Args:
            organization_id: <p>The identifier for the organization to be described.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.describe_organization_request.DescribeOrganizationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.describe_organization_response.DescribeOrganizationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.describe_organization

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.describe_organization.describe_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.describe_organization_request.DescribeOrganizationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_resource(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        resource_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.describe_resource_response.DescribeResourceResponse":
        """<p>Returns the data available for the resource.</p>

        Args:
            organization_id: <p>The identifier associated with the organization for which the resource is described.</p>
            resource_id: <p>The identifier of the resource to be described.</p> <p>The identifier can accept <i>ResourceId</i>, <i>Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Email address: resource@domain.tld</p> </li> <li> <p>Resource name: resource</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.describe_resource_request.DescribeResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.describe_resource_response.DescribeResourceResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.describe_resource

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.describe_resource.describe_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.describe_resource_request.DescribeResourceRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["resource_id"] = resource_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_user(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.describe_user_response.DescribeUserResponse":
        """<p>Provides information regarding the user.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the user exists.</p>
            user_id: <p>The identifier for the user to be described.</p> <p>The identifier can be the <i>UserId</i>, <i>Username</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: user@domain.tld</p> </li> <li> <p>User name: user</p> </li> </ul> <p></p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.describe_user_request.DescribeUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.describe_user_response.DescribeUserResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.describe_user

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.describe_user.describe_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.describe_user_request.DescribeUserRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_delegate_from_resource(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        resource_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.disassociate_delegate_from_resource_response.DisassociateDelegateFromResourceResponse":
        """<p>Removes a member from the resource's set of delegates.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the resource exists.</p>
            resource_id: <p>The identifier of the resource from which delegates' set members are removed. </p> <p>The identifier can accept <i>ResourceId</i>, <i>Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Email address: resource@domain.tld</p> </li> <li> <p>Resource name: resource</p> </li> </ul>
            entity_id: <p>The identifier for the member (user, group) to be removed from the resource's delegates.</p> <p>The entity ID can accept <i>UserId or GroupID</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Entity: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity: entity</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.disassociate_delegate_from_resource_request.DisassociateDelegateFromResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.disassociate_delegate_from_resource_response.DisassociateDelegateFromResourceResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.disassociate_delegate_from_resource

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.disassociate_delegate_from_resource.disassociate_delegate_from_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.disassociate_delegate_from_resource_request.DisassociateDelegateFromResourceRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["resource_id"] = resource_id
        input_["entity_id"] = entity_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_member_from_group(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        group_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        member_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.disassociate_member_from_group_response.DisassociateMemberFromGroupResponse":
        """<p>Removes a member from a group.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the group exists.</p>
            group_id: <p>The identifier for the group from which members are removed.</p> <p>The identifier can accept <i>GroupId</i>, <i>Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: group@domain.tld</p> </li> <li> <p>Group name: group</p> </li> </ul>
            member_id: <p>The identifier for the member to be removed from the group.</p> <p>The member ID can accept <i>UserID or GroupId</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Member ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: member@domain.tld</p> </li> <li> <p>Member name: member</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.disassociate_member_from_group_request.DisassociateMemberFromGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.disassociate_member_from_group_response.DisassociateMemberFromGroupResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.disassociate_member_from_group

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.disassociate_member_from_group.disassociate_member_from_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.disassociate_member_from_group_request.DisassociateMemberFromGroupRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["group_id"] = group_id
        input_["member_id"] = member_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_access_control_effect(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        ip_address: "aws_sdk_workmail.types.ip_address.IpAddress",
        action: "aws_sdk_workmail.types.access_control_rule_action.AccessControlRuleAction",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        user_id: Optional[
            "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier"
        ] = None,
        impersonation_role_id: Optional[
            "aws_sdk_workmail.types.impersonation_role_id.ImpersonationRoleId"
        ] = None,
    ) -> "aws_sdk_workmail.types.get_access_control_effect_response.GetAccessControlEffectResponse":
        """<p>Gets the effects of an organization's access control rules as they apply to a specified IPv4 address, access protocol action, and user ID or impersonation role ID. You must provide either the user ID or impersonation role ID. Impersonation role ID can only be used with Action EWS.</p>

        Args:
            organization_id: <p>The identifier for the organization.</p>
            ip_address: <p>The IPv4 address.</p>
            action: <p>The access protocol action. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>
            user_id: <p>The user ID.</p>
            impersonation_role_id: <p>The impersonation role ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.get_access_control_effect_request.GetAccessControlEffectRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.get_access_control_effect_response.GetAccessControlEffectResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.get_access_control_effect

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.get_access_control_effect.get_access_control_effect(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.get_access_control_effect_request.GetAccessControlEffectRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["ip_address"] = ip_address
        input_["action"] = action
        if user_id is not None:
            input_["user_id"] = user_id
        if impersonation_role_id is not None:
            input_["impersonation_role_id"] = impersonation_role_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_default_retention_policy(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.get_default_retention_policy_response.GetDefaultRetentionPolicyResponse":
        """<p>Gets the default retention policy details for the specified organization.</p>

        Args:
            organization_id: <p>The organization ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.get_default_retention_policy_request.GetDefaultRetentionPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.get_default_retention_policy_response.GetDefaultRetentionPolicyResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.get_default_retention_policy

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.get_default_retention_policy.get_default_retention_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.get_default_retention_policy_request.GetDefaultRetentionPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_impersonation_role(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        impersonation_role_id: "aws_sdk_workmail.types.impersonation_role_id.ImpersonationRoleId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.get_impersonation_role_response.GetImpersonationRoleResponse":
        """<p>Gets the impersonation role details for the given WorkMail organization.</p>

        Args:
            organization_id: <p>The WorkMail organization from which to retrieve the impersonation role.</p>
            impersonation_role_id: <p>The impersonation role ID to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.get_impersonation_role_request.GetImpersonationRoleRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.get_impersonation_role_response.GetImpersonationRoleResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.get_impersonation_role

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.get_impersonation_role.get_impersonation_role(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.get_impersonation_role_request.GetImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["impersonation_role_id"] = impersonation_role_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_impersonation_role_effect(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        impersonation_role_id: "aws_sdk_workmail.types.impersonation_role_id.ImpersonationRoleId",
        target_user: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.get_impersonation_role_effect_response.GetImpersonationRoleEffectResponse":
        """<p>Tests whether the given impersonation role can impersonate a target user.</p>

        Args:
            organization_id: <p>The WorkMail organization where the impersonation role is defined.</p>
            impersonation_role_id: <p>The impersonation role ID to test.</p>
            target_user: <p>The WorkMail organization user chosen to test the impersonation role. The following identity formats are available:</p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.get_impersonation_role_effect_request.GetImpersonationRoleEffectRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.get_impersonation_role_effect_response.GetImpersonationRoleEffectResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.get_impersonation_role_effect

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.get_impersonation_role_effect.get_impersonation_role_effect(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.get_impersonation_role_effect_request.GetImpersonationRoleEffectRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["impersonation_role_id"] = impersonation_role_id
        input_["target_user"] = target_user

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_mailbox_details(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> (
        "aws_sdk_workmail.types.get_mailbox_details_response.GetMailboxDetailsResponse"
    ):
        """<p>Requests a user's mailbox details for a specified organization and user.</p>

        Args:
            organization_id: <p>The identifier for the organization that contains the user whose mailbox details are being requested.</p>
            user_id: <p>The identifier for the user whose mailbox details are being requested.</p> <p>The identifier can be the <i>UserId</i>, <i>Username</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: user@domain.tld</p> </li> <li> <p>User name: user</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.get_mailbox_details_request.GetMailboxDetailsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.get_mailbox_details_response.GetMailboxDetailsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.get_mailbox_details

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.get_mailbox_details.get_mailbox_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.get_mailbox_details_request.GetMailboxDetailsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_mail_domain(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        domain_name: "aws_sdk_workmail.types.work_mail_domain_name.WorkMailDomainName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.get_mail_domain_response.GetMailDomainResponse":
        """<p>Gets details for a mail domain, including domain records required to configure your domain with recommended security.</p>

        Args:
            organization_id: <p>The WorkMail organization for which the domain is retrieved.</p>
            domain_name: <p>The domain from which you want to retrieve details.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.get_mail_domain_request.GetMailDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.get_mail_domain_response.GetMailDomainResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.get_mail_domain

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.get_mail_domain.get_mail_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.get_mail_domain_request.GetMailDomainRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["domain_name"] = domain_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_mobile_device_access_effect(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        device_type: Optional["aws_sdk_workmail.types.device_type.DeviceType"] = None,
        device_model: Optional[
            "aws_sdk_workmail.types.device_model.DeviceModel"
        ] = None,
        device_operating_system: Optional[
            "aws_sdk_workmail.types.device_operating_system.DeviceOperatingSystem"
        ] = None,
        device_user_agent: Optional[
            "aws_sdk_workmail.types.device_user_agent.DeviceUserAgent"
        ] = None,
    ) -> "aws_sdk_workmail.types.get_mobile_device_access_effect_response.GetMobileDeviceAccessEffectResponse":
        """<p>Simulates the effect of the mobile device access rules for the given attributes of a sample access event. Use this method to test the effects of the current set of mobile device access rules for the WorkMail organization for a particular user's attributes.</p>

        Args:
            organization_id: <p>The WorkMail organization to simulate the access effect for.</p>
            device_type: <p>Device type the simulated user will report.</p>
            device_model: <p>Device model the simulated user will report.</p>
            device_operating_system: <p>Device operating system the simulated user will report.</p>
            device_user_agent: <p>Device user agent the simulated user will report.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.get_mobile_device_access_effect_request.GetMobileDeviceAccessEffectRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.get_mobile_device_access_effect_response.GetMobileDeviceAccessEffectResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.get_mobile_device_access_effect

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.get_mobile_device_access_effect.get_mobile_device_access_effect(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.get_mobile_device_access_effect_request.GetMobileDeviceAccessEffectRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        if device_type is not None:
            input_["device_type"] = device_type
        if device_model is not None:
            input_["device_model"] = device_model
        if device_operating_system is not None:
            input_["device_operating_system"] = device_operating_system
        if device_user_agent is not None:
            input_["device_user_agent"] = device_user_agent

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_mobile_device_access_override(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        device_id: "aws_sdk_workmail.types.device_id.DeviceId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.get_mobile_device_access_override_response.GetMobileDeviceAccessOverrideResponse":
        """<p>Gets the mobile device access override for the given WorkMail organization, user, and device.</p>

        Args:
            organization_id: <p>The WorkMail organization to which you want to apply the override.</p>
            user_id: <p>Identifies the WorkMail user for the override. Accepts the following types of user identities: </p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>
            device_id: <p>The mobile device to which the override applies. <code>DeviceId</code> is case insensitive.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.get_mobile_device_access_override_request.GetMobileDeviceAccessOverrideRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.get_mobile_device_access_override_response.GetMobileDeviceAccessOverrideResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.get_mobile_device_access_override

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.get_mobile_device_access_override.get_mobile_device_access_override(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.get_mobile_device_access_override_request.GetMobileDeviceAccessOverrideRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["user_id"] = user_id
        input_["device_id"] = device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_personal_access_token_metadata(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        personal_access_token_id: "aws_sdk_workmail.types.personal_access_token_id.PersonalAccessTokenId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.get_personal_access_token_metadata_response.GetPersonalAccessTokenMetadataResponse":
        """<p> Requests details of a specific Personal Access Token within the WorkMail organization. </p>

        Args:
            organization_id: <p> The Organization ID. </p>
            personal_access_token_id: <p> The Personal Access Token ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.get_personal_access_token_metadata_request.GetPersonalAccessTokenMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.get_personal_access_token_metadata_response.GetPersonalAccessTokenMetadataResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.get_personal_access_token_metadata

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.get_personal_access_token_metadata.get_personal_access_token_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.get_personal_access_token_metadata_request.GetPersonalAccessTokenMetadataRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["personal_access_token_id"] = personal_access_token_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_access_control_rules(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.list_access_control_rules_response.ListAccessControlRulesResponse":
        """<p>Lists the access control rules for the specified organization.</p>

        Args:
            organization_id: <p>The identifier for the organization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_access_control_rules_request.ListAccessControlRulesRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_access_control_rules_response.ListAccessControlRulesResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_access_control_rules

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_access_control_rules.list_access_control_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_access_control_rules_request.ListAccessControlRulesRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_aliases(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_workmail.types.list_aliases_response.ListAliasesResponse":
        """<p>Creates a paginated call to list the aliases associated with a given entity.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the entity exists.</p>
            entity_id: <p>The identifier for the entity for which to list the aliases.</p>
            next_token: <p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_aliases_request.ListAliasesRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_aliases_response.ListAliasesResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_aliases

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_aliases.list_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_aliases_request.ListAliasesRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id
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

    def list_availability_configurations(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_workmail.types.list_availability_configurations_response.ListAvailabilityConfigurationsResponse":
        """<p>List all the <code>AvailabilityConfiguration</code>'s for the given WorkMail organization.</p>

        Args:
            organization_id: <p>The WorkMail organization for which the <code>AvailabilityConfiguration</code>'s will be listed.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token to use to retrieve the next page of results. The first call does not require a token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_availability_configurations_request.ListAvailabilityConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_availability_configurations_response.ListAvailabilityConfigurationsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_availability_configurations

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_availability_configurations.list_availability_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_availability_configurations_request.ListAvailabilityConfigurationsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
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

    def iter_list_availability_configurations(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_workmail.types.availability_configuration.AvailabilityConfiguration]":
        _token = next_token
        while True:
            _response = self.list_availability_configurations(
                organization_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("availability_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_group_members(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        group_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_workmail.types.list_group_members_response.ListGroupMembersResponse":
        """<p>Returns an overview of the members of a group. Users and groups can be members of a group.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the group exists.</p>
            group_id: <p>The identifier for the group to which the members (users or groups) are associated.</p> <p>The identifier can accept <i>GroupId</i>, <i>Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: group@domain.tld</p> </li> <li> <p>Group name: group</p> </li> </ul>
            next_token: <p> The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_group_members_request.ListGroupMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_group_members_response.ListGroupMembersResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_group_members

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_group_members.list_group_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_group_members_request.ListGroupMembersRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["group_id"] = group_id
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

    def list_groups(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
        filters: Optional[
            "aws_sdk_workmail.types.list_groups_filters.ListGroupsFilters"
        ] = None,
    ) -> "aws_sdk_workmail.types.list_groups_response.ListGroupsResponse":
        """<p>Returns summaries of the organization's groups.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the groups exist.</p>
            next_token: <p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            filters: <p>Limit the search results based on the filter criteria. Only one filter per request is supported.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_groups_request.ListGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_groups_response.ListGroupsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_groups

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_groups.list_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_groups_request.ListGroupsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
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

    def list_groups_for_entity(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        filters: Optional[
            "aws_sdk_workmail.types.list_groups_for_entity_filters.ListGroupsForEntityFilters"
        ] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_workmail.types.list_groups_for_entity_response.ListGroupsForEntityResponse":
        """<p>Returns all the groups to which an entity belongs.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the entity exists.</p>
            entity_id: <p>The identifier for the entity.</p> <p>The entity ID can accept <i>UserId or GroupID</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>
            filters: <p>Limit the search results based on the filter criteria.</p>
            next_token: <p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_groups_for_entity_request.ListGroupsForEntityRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_groups_for_entity_response.ListGroupsForEntityResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_groups_for_entity

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_groups_for_entity.list_groups_for_entity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_groups_for_entity_request.ListGroupsForEntityRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id
        if filters is not None:
            input_["filters"] = filters
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

    def list_impersonation_roles(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_workmail.types.list_impersonation_roles_response.ListImpersonationRolesResponse":
        """<p>Lists all the impersonation roles for the given WorkMail organization.</p>

        Args:
            organization_id: <p>The WorkMail organization to which the listed impersonation roles belong.</p>
            next_token: <p>The token used to retrieve the next page of results. The first call doesn't require a token.</p>
            max_results: <p>The maximum number of results returned in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_impersonation_roles_request.ListImpersonationRolesRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_impersonation_roles_response.ListImpersonationRolesResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_impersonation_roles

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_impersonation_roles.list_impersonation_roles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_impersonation_roles_request.ListImpersonationRolesRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
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

    def list_mailbox_export_jobs(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_workmail.types.list_mailbox_export_jobs_response.ListMailboxExportJobsResponse":
        """<p>Lists the mailbox export jobs started for the specified organization within the last seven days.</p>

        Args:
            organization_id: <p>The organization ID.</p>
            next_token: <p>The token to use to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_mailbox_export_jobs_request.ListMailboxExportJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_mailbox_export_jobs_response.ListMailboxExportJobsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_mailbox_export_jobs

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_mailbox_export_jobs.list_mailbox_export_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_mailbox_export_jobs_request.ListMailboxExportJobsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
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

    def list_mailbox_permissions(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_workmail.types.list_mailbox_permissions_response.ListMailboxPermissionsResponse":
        """<p>Lists the mailbox permissions associated with a user, group, or resource mailbox.</p>

        Args:
            organization_id: <p>The identifier of the organization under which the user, group, or resource exists.</p>
            entity_id: <p>The identifier of the user, or resource for which to list mailbox permissions.</p> <p>The entity ID can accept <i>UserId or ResourceId</i>, <i>Username or Resourcename</i>, or <i>email</i>.</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, or r-0123456789a0123456789b0123456789</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>
            next_token: <p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_mailbox_permissions_request.ListMailboxPermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_mailbox_permissions_response.ListMailboxPermissionsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_mailbox_permissions

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_mailbox_permissions.list_mailbox_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_mailbox_permissions_request.ListMailboxPermissionsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id
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

    def list_mail_domains(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_workmail.types.list_mail_domains_response.ListMailDomainsResponse":
        """<p>Lists the mail domains in a given WorkMail organization.</p>

        Args:
            organization_id: <p>The WorkMail organization for which to list domains.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token to use to retrieve the next page of results. The first call does not require a token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_mail_domains_request.ListMailDomainsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_mail_domains_response.ListMailDomainsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_mail_domains

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_mail_domains.list_mail_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_mail_domains_request.ListMailDomainsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
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

    def list_mobile_device_access_overrides(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        user_id: Optional[
            "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
        ] = None,
        device_id: Optional["aws_sdk_workmail.types.device_id.DeviceId"] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_workmail.types.list_mobile_device_access_overrides_response.ListMobileDeviceAccessOverridesResponse":
        """<p>Lists all the mobile device access overrides for any given combination of WorkMail organization, user, or device.</p>

        Args:
            organization_id: <p>The WorkMail organization under which to list mobile device access overrides.</p>
            user_id: <p>The WorkMail user under which you list the mobile device access overrides. Accepts the following types of user identities:</p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>
            device_id: <p>The mobile device to which the access override applies.</p>
            next_token: <p>The token to use to retrieve the next page of results. The first call does not require a token.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_mobile_device_access_overrides_request.ListMobileDeviceAccessOverridesRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_mobile_device_access_overrides_response.ListMobileDeviceAccessOverridesResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_mobile_device_access_overrides

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_mobile_device_access_overrides.list_mobile_device_access_overrides(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_mobile_device_access_overrides_request.ListMobileDeviceAccessOverridesRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        if user_id is not None:
            input_["user_id"] = user_id
        if device_id is not None:
            input_["device_id"] = device_id
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

    def list_mobile_device_access_rules(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.list_mobile_device_access_rules_response.ListMobileDeviceAccessRulesResponse":
        """<p>Lists the mobile device access rules for the specified WorkMail organization.</p>

        Args:
            organization_id: <p>The WorkMail organization for which to list the rules.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_mobile_device_access_rules_request.ListMobileDeviceAccessRulesRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_mobile_device_access_rules_response.ListMobileDeviceAccessRulesResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_mobile_device_access_rules

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_mobile_device_access_rules.list_mobile_device_access_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_mobile_device_access_rules_request.ListMobileDeviceAccessRulesRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_organizations(
        self,
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_workmail.types.list_organizations_response.ListOrganizationsResponse":
        """<p>Returns summaries of the customer's organizations.</p>

        Args:
            next_token: <p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_organizations_request.ListOrganizationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_organizations_response.ListOrganizationsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_organizations

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_organizations.list_organizations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_organizations_request.ListOrganizationsRequest = {}  # type: ignore[typeddict-item]
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

    def list_personal_access_tokens(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        user_id: Optional[
            "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
        ] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_workmail.types.list_personal_access_tokens_response.ListPersonalAccessTokensResponse":
        """<p> Returns a summary of your Personal Access Tokens. </p>

        Args:
            organization_id: <p> The Organization ID. </p>
            user_id: <p> The WorkMail User ID. </p>
            next_token: <p> The token from the previous response to query the next page.</p>
            max_results: <p> The maximum amount of items that should be returned in a response. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_personal_access_tokens_request.ListPersonalAccessTokensRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_personal_access_tokens_response.ListPersonalAccessTokensResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_personal_access_tokens

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_personal_access_tokens.list_personal_access_tokens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_personal_access_tokens_request.ListPersonalAccessTokensRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        if user_id is not None:
            input_["user_id"] = user_id
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

    def iter_list_personal_access_tokens(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        user_id: Optional[
            "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
        ] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "Iterator[aws_sdk_workmail.types.personal_access_token_summary.PersonalAccessTokenSummary]":
        _token = next_token
        while True:
            _response = self.list_personal_access_tokens(
                organization_id,
                config_overrides=config_overrides,
                user_id=user_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("personal_access_token_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_delegates(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        resource_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_workmail.types.list_resource_delegates_response.ListResourceDelegatesResponse":
        """<p>Lists the delegates associated with a resource. Users and groups can be resource delegates and answer requests on behalf of the resource.</p>

        Args:
            organization_id: <p>The identifier for the organization that contains the resource for which delegates are listed.</p>
            resource_id: <p>The identifier for the resource whose delegates are listed.</p> <p>The identifier can accept <i>ResourceId</i>, <i>Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Email address: resource@domain.tld</p> </li> <li> <p>Resource name: resource</p> </li> </ul>
            next_token: <p>The token used to paginate through the delegates associated with a resource.</p>
            max_results: <p>The number of maximum results in a page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_resource_delegates_request.ListResourceDelegatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_resource_delegates_response.ListResourceDelegatesResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_resource_delegates

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_resource_delegates.list_resource_delegates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_resource_delegates_request.ListResourceDelegatesRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["resource_id"] = resource_id
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

    def list_resources(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
        filters: Optional[
            "aws_sdk_workmail.types.list_resources_filters.ListResourcesFilters"
        ] = None,
    ) -> "aws_sdk_workmail.types.list_resources_response.ListResourcesResponse":
        """<p>Returns summaries of the organization's resources.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the resources exist.</p>
            next_token: <p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            filters: <p>Limit the resource search results based on the filter criteria. You can only use one filter per request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_resources_request.ListResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_resources_response.ListResourcesResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_resources

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_resources.list_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_resources_request.ListResourcesRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_workmail.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags applied to an WorkMail organization resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_users(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        next_token: Optional["aws_sdk_workmail.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_workmail.types.max_results.MaxResults"] = None,
        filters: Optional[
            "aws_sdk_workmail.types.list_users_filters.ListUsersFilters"
        ] = None,
    ) -> "aws_sdk_workmail.types.list_users_response.ListUsersResponse":
        """<p>Returns summaries of the organization's users.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the users exist.</p>
            next_token: <p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            filters: <p>Limit the user search results based on the filter criteria. You can only use one filter per request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.list_users_request.ListUsersRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.list_users_response.ListUsersResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.list_users

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.list_users.list_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.list_users_request.ListUsersRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
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

    def put_access_control_rule(
        self,
        name: "aws_sdk_workmail.types.access_control_rule_name.AccessControlRuleName",
        effect: "aws_sdk_workmail.types.access_control_rule_effect.AccessControlRuleEffect",
        description: "aws_sdk_workmail.types.access_control_rule_description.AccessControlRuleDescription",
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        ip_ranges: Optional["aws_sdk_workmail.types.ip_range_list.IpRangeList"] = None,
        not_ip_ranges: Optional[
            "aws_sdk_workmail.types.ip_range_list.IpRangeList"
        ] = None,
        actions: Optional["aws_sdk_workmail.types.actions_list.ActionsList"] = None,
        not_actions: Optional["aws_sdk_workmail.types.actions_list.ActionsList"] = None,
        user_ids: Optional["aws_sdk_workmail.types.user_id_list.UserIdList"] = None,
        not_user_ids: Optional["aws_sdk_workmail.types.user_id_list.UserIdList"] = None,
        impersonation_role_ids: Optional[
            "aws_sdk_workmail.types.impersonation_role_id_list.ImpersonationRoleIdList"
        ] = None,
        not_impersonation_role_ids: Optional[
            "aws_sdk_workmail.types.impersonation_role_id_list.ImpersonationRoleIdList"
        ] = None,
    ) -> "aws_sdk_workmail.types.put_access_control_rule_response.PutAccessControlRuleResponse":
        """<p>Adds a new access control rule for the specified organization. The rule allows or denies access to the organization for the specified IPv4 addresses, access protocol actions, user IDs and impersonation IDs. Adding a new rule with the same name as an existing rule replaces the older rule.</p>

        Args:
            name: <p>The rule name.</p>
            effect: <p>The rule effect.</p>
            description: <p>The rule description.</p>
            ip_ranges: <p>IPv4 CIDR ranges to include in the rule.</p>
            not_ip_ranges: <p>IPv4 CIDR ranges to exclude from the rule.</p>
            actions: <p>Access protocol actions to include in the rule. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>
            not_actions: <p>Access protocol actions to exclude from the rule. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>
            user_ids: <p>User IDs to include in the rule.</p>
            not_user_ids: <p>User IDs to exclude from the rule.</p>
            organization_id: <p>The identifier of the organization.</p>
            impersonation_role_ids: <p>Impersonation role IDs to include in the rule.</p>
            not_impersonation_role_ids: <p>Impersonation role IDs to exclude from the rule.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.put_access_control_rule_request.PutAccessControlRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.put_access_control_rule_response.PutAccessControlRuleResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.put_access_control_rule

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.put_access_control_rule.put_access_control_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.put_access_control_rule_request.PutAccessControlRuleRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["effect"] = effect
        input_["description"] = description
        if ip_ranges is not None:
            input_["ip_ranges"] = ip_ranges
        if not_ip_ranges is not None:
            input_["not_ip_ranges"] = not_ip_ranges
        if actions is not None:
            input_["actions"] = actions
        if not_actions is not None:
            input_["not_actions"] = not_actions
        if user_ids is not None:
            input_["user_ids"] = user_ids
        if not_user_ids is not None:
            input_["not_user_ids"] = not_user_ids
        input_["organization_id"] = organization_id
        if impersonation_role_ids is not None:
            input_["impersonation_role_ids"] = impersonation_role_ids
        if not_impersonation_role_ids is not None:
            input_["not_impersonation_role_ids"] = not_impersonation_role_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_email_monitoring_configuration(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        log_group_arn: "aws_sdk_workmail.types.log_group_arn.LogGroupArn",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        role_arn: Optional["aws_sdk_workmail.types.role_arn.RoleArn"] = None,
    ) -> "aws_sdk_workmail.types.put_email_monitoring_configuration_response.PutEmailMonitoringConfigurationResponse":
        """<p>Creates or updates the email monitoring configuration for a specified organization.</p>

        Args:
            organization_id: <p>The ID of the organization for which the email monitoring configuration is set.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM Role associated with the email monitoring configuration. If absent, the IAM Role Arn of AWSServiceRoleForAmazonWorkMailEvents will be used.</p>
            log_group_arn: <p>The Amazon Resource Name (ARN) of the CloudWatch Log group associated with the email monitoring configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.put_email_monitoring_configuration_request.PutEmailMonitoringConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.put_email_monitoring_configuration_response.PutEmailMonitoringConfigurationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.put_email_monitoring_configuration

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.put_email_monitoring_configuration.put_email_monitoring_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.put_email_monitoring_configuration_request.PutEmailMonitoringConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
        input_["log_group_arn"] = log_group_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_identity_provider_configuration(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        authentication_mode: "aws_sdk_workmail.types.identity_provider_authentication_mode.IdentityProviderAuthenticationMode",
        identity_center_configuration: "aws_sdk_workmail.types.identity_center_configuration.IdentityCenterConfiguration",
        personal_access_token_configuration: "aws_sdk_workmail.types.personal_access_token_configuration.PersonalAccessTokenConfiguration",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.put_identity_provider_configuration_response.PutIdentityProviderConfigurationResponse":
        """<p> Enables integration between IAM Identity Center (IdC) and WorkMail to proxy authentication requests for mailbox users. You can connect your IdC directory or your external directory to WorkMail through IdC and manage access to WorkMail mailboxes in a single place. For enhanced protection, you could enable Multifactor Authentication (MFA) and Personal Access Tokens. </p>

        Args:
            organization_id: <p> The ID of the WorkMail Organization. </p>
            authentication_mode: <p> The authentication mode used in WorkMail.</p>
            identity_center_configuration: <p> The details of the IAM Identity Center configuration.</p>
            personal_access_token_configuration: <p> The details of the Personal Access Token configuration. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.put_identity_provider_configuration_request.PutIdentityProviderConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.put_identity_provider_configuration_response.PutIdentityProviderConfigurationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.put_identity_provider_configuration

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.put_identity_provider_configuration.put_identity_provider_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.put_identity_provider_configuration_request.PutIdentityProviderConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["authentication_mode"] = authentication_mode
        input_["identity_center_configuration"] = identity_center_configuration
        input_["personal_access_token_configuration"] = (
            personal_access_token_configuration
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_inbound_dmarc_settings(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        enforced: "aws_sdk_workmail.types.boolean_object.BooleanObject",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.put_inbound_dmarc_settings_response.PutInboundDmarcSettingsResponse":
        """<p>Enables or disables a DMARC policy for a given organization.</p>

        Args:
            organization_id: <p>The ID of the organization that you are applying the DMARC policy to.</p>
            enforced: <p>Enforces or suspends a policy after it's applied.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.put_inbound_dmarc_settings_request.PutInboundDmarcSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.put_inbound_dmarc_settings_response.PutInboundDmarcSettingsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.put_inbound_dmarc_settings

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.put_inbound_dmarc_settings.put_inbound_dmarc_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.put_inbound_dmarc_settings_request.PutInboundDmarcSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["enforced"] = enforced

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_mailbox_permissions(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        grantee_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        permission_values: "aws_sdk_workmail.types.permission_values.PermissionValues",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.put_mailbox_permissions_response.PutMailboxPermissionsResponse":
        """<p>Sets permissions for a user, group, or resource. This replaces any pre-existing permissions.</p>

        Args:
            organization_id: <p>The identifier of the organization under which the user, group, or resource exists.</p>
            entity_id: <p>The identifier of the user or resource for which to update mailbox permissions.</p> <p>The identifier can be <i>UserId, ResourceID, or Group Id</i>, <i>Username, Resourcename, or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>
            grantee_id: <p>The identifier of the user, group, or resource to which to grant the permissions.</p> <p>The identifier can be <i>UserId, ResourceID, or Group Id</i>, <i>Username, Resourcename, or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Grantee ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: grantee@domain.tld</p> </li> <li> <p>Grantee name: grantee</p> </li> </ul>
            permission_values: <p>The permissions granted to the grantee. SEND_AS allows the grantee to send email as the owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF allows the grantee to send email on behalf of the owner of the mailbox (the grantee is not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee full access to the mailbox, irrespective of other folder-level permissions set on the mailbox.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.put_mailbox_permissions_request.PutMailboxPermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.put_mailbox_permissions_response.PutMailboxPermissionsResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.put_mailbox_permissions

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.put_mailbox_permissions.put_mailbox_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.put_mailbox_permissions_request.PutMailboxPermissionsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id
        input_["grantee_id"] = grantee_id
        input_["permission_values"] = permission_values

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_mobile_device_access_override(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        device_id: "aws_sdk_workmail.types.device_id.DeviceId",
        effect: "aws_sdk_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        description: Optional[
            "aws_sdk_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
        ] = None,
    ) -> "aws_sdk_workmail.types.put_mobile_device_access_override_response.PutMobileDeviceAccessOverrideResponse":
        """<p>Creates or updates a mobile device access override for the given WorkMail organization, user, and device.</p>

        Args:
            organization_id: <p>Identifies the WorkMail organization for which you create the override.</p>
            user_id: <p>The WorkMail user for which you create the override. Accepts the following types of user identities:</p> <ul> <li> <p>User ID: <code>12345678-1234-1234-1234-123456789012</code> or <code>S-1-1-12-1234567890-123456789-123456789-1234</code> </p> </li> <li> <p>Email address: <code>user@domain.tld</code> </p> </li> <li> <p>User name: <code>user</code> </p> </li> </ul>
            device_id: <p>The mobile device for which you create the override. <code>DeviceId</code> is case insensitive.</p>
            effect: <p>The effect of the override, <code>ALLOW</code> or <code>DENY</code>.</p>
            description: <p>A description of the override.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.put_mobile_device_access_override_request.PutMobileDeviceAccessOverrideRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.put_mobile_device_access_override_response.PutMobileDeviceAccessOverrideResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.put_mobile_device_access_override

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.put_mobile_device_access_override.put_mobile_device_access_override(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.put_mobile_device_access_override_request.PutMobileDeviceAccessOverrideRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["user_id"] = user_id
        input_["device_id"] = device_id
        input_["effect"] = effect
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_retention_policy(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        name: "aws_sdk_workmail.types.short_string.ShortString",
        folder_configurations: "aws_sdk_workmail.types.folder_configurations.FolderConfigurations",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        id: Optional["aws_sdk_workmail.types.short_string.ShortString"] = None,
        description: Optional[
            "aws_sdk_workmail.types.policy_description.PolicyDescription"
        ] = None,
    ) -> "aws_sdk_workmail.types.put_retention_policy_response.PutRetentionPolicyResponse":
        """<p>Puts a retention policy to the specified organization.</p>

        Args:
            organization_id: <p>The organization ID.</p>
            id: <p>The retention policy ID.</p>
            name: <p>The retention policy name.</p>
            description: <p>The retention policy description.</p>
            folder_configurations: <p>The retention policy folder configurations.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.put_retention_policy_request.PutRetentionPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.put_retention_policy_response.PutRetentionPolicyResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.put_retention_policy

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.put_retention_policy.put_retention_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.put_retention_policy_request.PutRetentionPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        if id is not None:
            input_["id"] = id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["folder_configurations"] = folder_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_mail_domain(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        domain_name: "aws_sdk_workmail.types.work_mail_domain_name.WorkMailDomainName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        client_token: Optional[
            "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
        ] = None,
    ) -> "aws_sdk_workmail.types.register_mail_domain_response.RegisterMailDomainResponse":
        """<p>Registers a new domain in WorkMail and SES, and configures it for use by WorkMail. Emails received by SES for this domain are routed to the specified WorkMail organization, and WorkMail has permanent permission to use the specified domain for sending your users' emails.</p>

        Args:
            client_token: <p>Idempotency token used when retrying requests.</p>
            organization_id: <p>The WorkMail organization under which you're creating the domain.</p>
            domain_name: <p>The name of the mail domain to create in WorkMail and SES.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.register_mail_domain_request.RegisterMailDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.register_mail_domain_response.RegisterMailDomainResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.register_mail_domain

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.register_mail_domain.register_mail_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.register_mail_domain_request.RegisterMailDomainRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["organization_id"] = organization_id
        input_["domain_name"] = domain_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_to_work_mail(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        email: "aws_sdk_workmail.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.register_to_work_mail_response.RegisterToWorkMailResponse":
        r"""<p>Registers an existing and disabled user, group, or resource for WorkMail use by associating a mailbox and calendaring capabilities. It performs no change if the user, group, or resource is enabled and fails if the user, group, or resource is deleted. This operation results in the accumulation of costs. For more information, see <a href=\"https://aws.amazon.com/workmail/pricing\">Pricing</a>. The equivalent console functionality for this operation is <i>Enable</i>.</p> <p>Users can either be created by calling the <a>CreateUser</a> API operation or they can be synchronized from your directory. For more information, see <a>DeregisterFromWorkMail</a>.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the user, group, or resource exists.</p>
            entity_id: <p>The identifier for the user, group, or resource to be updated.</p> <p>The identifier can accept <i>UserId, ResourceId, or GroupId</i>, or <i>Username, Resourcename, or Groupname</i>. The following identity formats are available:</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Entity name: entity</p> </li> </ul>
            email: <p>The email for the user, group, or resource to be updated.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.register_to_work_mail_request.RegisterToWorkMailRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.register_to_work_mail_response.RegisterToWorkMailResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.register_to_work_mail

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.register_to_work_mail.register_to_work_mail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.register_to_work_mail_request.RegisterToWorkMailRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id
        input_["email"] = email

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reset_password(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        user_id: "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier",
        password: "aws_sdk_workmail.types.password.Password",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.reset_password_response.ResetPasswordResponse":
        """<p>Allows the administrator to reset the password for a user.</p>

        Args:
            organization_id: <p>The identifier of the organization that contains the user for which the password is reset.</p>
            user_id: <p>The identifier of the user for whom the password is reset.</p>
            password: <p>The new password for the user.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.reset_password_request.ResetPasswordRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.reset_password_response.ResetPasswordResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.reset_password

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.reset_password.reset_password(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.reset_password_request.ResetPasswordRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["user_id"] = user_id
        input_["password"] = password

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_mailbox_export_job(
        self,
        client_token: "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken",
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        role_arn: "aws_sdk_workmail.types.role_arn.RoleArn",
        kms_key_arn: "aws_sdk_workmail.types.kms_key_arn.KmsKeyArn",
        s3_bucket_name: "aws_sdk_workmail.types.s3_bucket_name.S3BucketName",
        s3_prefix: "aws_sdk_workmail.types.s3_object_key.S3ObjectKey",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        description: Optional["aws_sdk_workmail.types.description.Description"] = None,
    ) -> "aws_sdk_workmail.types.start_mailbox_export_job_response.StartMailboxExportJobResponse":
        r"""<p>Starts a mailbox export job to export MIME-format email messages and calendar items from the specified mailbox to the specified Amazon Simple Storage Service (Amazon S3) bucket. For more information, see <a href=\"https://docs.aws.amazon.com/workmail/latest/adminguide/mail-export.html\">Exporting mailbox content</a> in the <i>WorkMail Administrator Guide</i>.</p>

        Args:
            client_token: <p>The idempotency token for the client request.</p>
            organization_id: <p>The identifier associated with the organization.</p>
            entity_id: <p>The identifier of the user or resource associated with the mailbox.</p> <p>The identifier can accept <i>UserId or ResourceId</i>, <i>Username or Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789 , or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>
            description: <p>The mailbox export job description.</p>
            role_arn: <p>The ARN of the AWS Identity and Access Management (IAM) role that grants write permission to the S3 bucket.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the symmetric AWS Key Management Service (AWS KMS) key that encrypts the exported mailbox content.</p>
            s3_bucket_name: <p>The name of the S3 bucket.</p>
            s3_prefix: <p>The S3 bucket prefix.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.start_mailbox_export_job_request.StartMailboxExportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.start_mailbox_export_job_response.StartMailboxExportJobResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.start_mailbox_export_job

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.start_mailbox_export_job.start_mailbox_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.start_mailbox_export_job_request.StartMailboxExportJobRequest = {}  # type: ignore[typeddict-item]
        input_["client_token"] = client_token
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id
        if description is not None:
            input_["description"] = description
        input_["role_arn"] = role_arn
        input_["kms_key_arn"] = kms_key_arn
        input_["s3_bucket_name"] = s3_bucket_name
        input_["s3_prefix"] = s3_prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_workmail.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_workmail.types.tag_list.TagList",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.tag_resource_response.TagResourceResponse":
        """<p>Applies the specified tags to the specified WorkMailorganization resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tags: <p>The tag key-value pairs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.tag_resource

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def test_availability_configuration(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        domain_name: Optional["aws_sdk_workmail.types.domain_name.DomainName"] = None,
        ews_provider: Optional[
            "aws_sdk_workmail.types.ews_availability_provider.EwsAvailabilityProvider"
        ] = None,
        lambda_provider: Optional[
            "aws_sdk_workmail.types.lambda_availability_provider.LambdaAvailabilityProvider"
        ] = None,
    ) -> "aws_sdk_workmail.types.test_availability_configuration_response.TestAvailabilityConfigurationResponse":
        """<p>Performs a test on an availability provider to ensure that access is allowed. For EWS, it verifies the provided credentials can be used to successfully log in. For Lambda, it verifies that the Lambda function can be invoked and that the resource access policy was configured to deny anonymous access. An anonymous invocation is one done without providing either a <code>SourceArn</code> or <code>SourceAccount</code> header.</p> <note> <p>The request must contain either one provider definition (<code>EwsProvider</code> or <code>LambdaProvider</code>) or the <code>DomainName</code> parameter. If the <code>DomainName</code> parameter is provided, the configuration stored under the <code>DomainName</code> will be tested.</p> </note>

        Args:
            organization_id: <p>The WorkMail organization where the availability provider will be tested.</p>
            domain_name: <p>The domain to which the provider applies. If this field is provided, a stored availability provider associated to this domain name will be tested.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.test_availability_configuration_request.TestAvailabilityConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.test_availability_configuration_response.TestAvailabilityConfigurationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.test_availability_configuration

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.test_availability_configuration.test_availability_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.test_availability_configuration_request.TestAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if ews_provider is not None:
            input_["ews_provider"] = ews_provider
        if lambda_provider is not None:
            input_["lambda_provider"] = lambda_provider

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_workmail.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_workmail.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.untag_resource_response.UntagResourceResponse":
        """<p>Untags the specified tags from the specified WorkMail organization resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tag_keys: <p>The tag keys.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.untag_resource

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_availability_configuration(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        domain_name: "aws_sdk_workmail.types.domain_name.DomainName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        ews_provider: Optional[
            "aws_sdk_workmail.types.ews_availability_provider.EwsAvailabilityProvider"
        ] = None,
        lambda_provider: Optional[
            "aws_sdk_workmail.types.lambda_availability_provider.LambdaAvailabilityProvider"
        ] = None,
    ) -> "aws_sdk_workmail.types.update_availability_configuration_response.UpdateAvailabilityConfigurationResponse":
        """<p>Updates an existing <code>AvailabilityConfiguration</code> for the given WorkMail organization and domain.</p>

        Args:
            organization_id: <p>The WorkMail organization for which the <code>AvailabilityConfiguration</code> will be updated.</p>
            domain_name: <p>The domain to which the provider applies the availability configuration.</p>
            ews_provider: <p>The EWS availability provider definition. The request must contain exactly one provider definition, either <code>EwsProvider</code> or <code>LambdaProvider</code>. The previously stored provider will be overridden by the one provided.</p>
            lambda_provider: <p>The Lambda availability provider definition. The request must contain exactly one provider definition, either <code>EwsProvider</code> or <code>LambdaProvider</code>. The previously stored provider will be overridden by the one provided.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.update_availability_configuration_request.UpdateAvailabilityConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.update_availability_configuration_response.UpdateAvailabilityConfigurationResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.update_availability_configuration

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.update_availability_configuration.update_availability_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.update_availability_configuration_request.UpdateAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["domain_name"] = domain_name
        if ews_provider is not None:
            input_["ews_provider"] = ews_provider
        if lambda_provider is not None:
            input_["lambda_provider"] = lambda_provider

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_default_mail_domain(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        domain_name: "aws_sdk_workmail.types.work_mail_domain_name.WorkMailDomainName",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.update_default_mail_domain_response.UpdateDefaultMailDomainResponse":
        """<p>Updates the default mail domain for an organization. The default mail domain is used by the WorkMail AWS Console to suggest an email address when enabling a mail user. You can only have one default domain.</p>

        Args:
            organization_id: <p>The WorkMail organization for which to list domains.</p>
            domain_name: <p>The domain name that will become the default domain.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.update_default_mail_domain_request.UpdateDefaultMailDomainRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.update_default_mail_domain_response.UpdateDefaultMailDomainResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.update_default_mail_domain

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.update_default_mail_domain.update_default_mail_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.update_default_mail_domain_request.UpdateDefaultMailDomainRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["domain_name"] = domain_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_group(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        group_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        hidden_from_global_address_list: Optional[
            "aws_sdk_workmail.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "aws_sdk_workmail.types.update_group_response.UpdateGroupResponse":
        """<p>Updates attributes in a group.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the group exists.</p>
            group_id: <p>The identifier for the group to be updated.</p> <p>The identifier can accept <i>GroupId</i>, <i>Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: group@domain.tld</p> </li> <li> <p>Group name: group</p> </li> </ul>
            hidden_from_global_address_list: <p>If enabled, the group is hidden from the global address list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.update_group_request.UpdateGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.update_group_response.UpdateGroupResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.update_group

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.update_group.update_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.update_group_request.UpdateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["group_id"] = group_id
        if hidden_from_global_address_list is not None:
            input_["hidden_from_global_address_list"] = hidden_from_global_address_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_impersonation_role(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        impersonation_role_id: "aws_sdk_workmail.types.impersonation_role_id.ImpersonationRoleId",
        name: "aws_sdk_workmail.types.impersonation_role_name.ImpersonationRoleName",
        type: "aws_sdk_workmail.types.impersonation_role_type.ImpersonationRoleType",
        rules: "aws_sdk_workmail.types.impersonation_rule_list.ImpersonationRuleList",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        description: Optional[
            "aws_sdk_workmail.types.impersonation_role_description.ImpersonationRoleDescription"
        ] = None,
    ) -> "aws_sdk_workmail.types.update_impersonation_role_response.UpdateImpersonationRoleResponse":
        """<p>Updates an impersonation role for the given WorkMail organization.</p>

        Args:
            organization_id: <p>The WorkMail organization that contains the impersonation role to update.</p>
            impersonation_role_id: <p>The ID of the impersonation role to update.</p>
            name: <p>The updated impersonation role name.</p>
            type: <p>The updated impersonation role type.</p>
            description: <p>The updated impersonation role description.</p>
            rules: <p>The updated list of rules.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.update_impersonation_role_request.UpdateImpersonationRoleRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.update_impersonation_role_response.UpdateImpersonationRoleResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.update_impersonation_role

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.update_impersonation_role.update_impersonation_role(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.update_impersonation_role_request.UpdateImpersonationRoleRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["impersonation_role_id"] = impersonation_role_id
        input_["name"] = name
        input_["type"] = type
        if description is not None:
            input_["description"] = description
        input_["rules"] = rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_mailbox_quota(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        mailbox_quota: "aws_sdk_workmail.types.mailbox_quota.MailboxQuota",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.update_mailbox_quota_response.UpdateMailboxQuotaResponse":
        """<p>Updates a user's current mailbox quota for a specified organization and user.</p>

        Args:
            organization_id: <p>The identifier for the organization that contains the user for whom to update the mailbox quota.</p>
            user_id: <p>The identifer for the user for whom to update the mailbox quota.</p> <p>The identifier can be the <i>UserId</i>, <i>Username</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: user@domain.tld</p> </li> <li> <p>User name: user</p> </li> </ul>
            mailbox_quota: <p>The updated mailbox quota, in MB, for the specified user.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.update_mailbox_quota_request.UpdateMailboxQuotaRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.update_mailbox_quota_response.UpdateMailboxQuotaResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.update_mailbox_quota

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.update_mailbox_quota.update_mailbox_quota(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.update_mailbox_quota_request.UpdateMailboxQuotaRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["user_id"] = user_id
        input_["mailbox_quota"] = mailbox_quota

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_mobile_device_access_rule(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        mobile_device_access_rule_id: "aws_sdk_workmail.types.mobile_device_access_rule_id.MobileDeviceAccessRuleId",
        name: "aws_sdk_workmail.types.mobile_device_access_rule_name.MobileDeviceAccessRuleName",
        effect: "aws_sdk_workmail.types.mobile_device_access_rule_effect.MobileDeviceAccessRuleEffect",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        description: Optional[
            "aws_sdk_workmail.types.mobile_device_access_rule_description.MobileDeviceAccessRuleDescription"
        ] = None,
        device_types: Optional[
            "aws_sdk_workmail.types.device_type_list.DeviceTypeList"
        ] = None,
        not_device_types: Optional[
            "aws_sdk_workmail.types.device_type_list.DeviceTypeList"
        ] = None,
        device_models: Optional[
            "aws_sdk_workmail.types.device_model_list.DeviceModelList"
        ] = None,
        not_device_models: Optional[
            "aws_sdk_workmail.types.device_model_list.DeviceModelList"
        ] = None,
        device_operating_systems: Optional[
            "aws_sdk_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
        ] = None,
        not_device_operating_systems: Optional[
            "aws_sdk_workmail.types.device_operating_system_list.DeviceOperatingSystemList"
        ] = None,
        device_user_agents: Optional[
            "aws_sdk_workmail.types.device_user_agent_list.DeviceUserAgentList"
        ] = None,
        not_device_user_agents: Optional[
            "aws_sdk_workmail.types.device_user_agent_list.DeviceUserAgentList"
        ] = None,
    ) -> "aws_sdk_workmail.types.update_mobile_device_access_rule_response.UpdateMobileDeviceAccessRuleResponse":
        """<p>Updates a mobile device access rule for the specified WorkMail organization.</p>

        Args:
            organization_id: <p>The WorkMail organization under which the rule will be updated.</p>
            mobile_device_access_rule_id: <p>The identifier of the rule to be updated.</p>
            name: <p>The updated rule name.</p>
            description: <p>The updated rule description.</p>
            effect: <p>The effect of the rule when it matches. Allowed values are <code>ALLOW</code> or <code>DENY</code>.</p>
            device_types: <p>Device types that the updated rule will match.</p>
            not_device_types: <p>Device types that the updated rule <b>will not</b> match. All other device types will match.</p>
            device_models: <p>Device models that the updated rule will match.</p>
            not_device_models: <p>Device models that the updated rule <b>will not</b> match. All other device models will match.</p>
            device_operating_systems: <p>Device operating systems that the updated rule will match.</p>
            not_device_operating_systems: <p>Device operating systems that the updated rule <b>will not</b> match. All other device operating systems will match.</p>
            device_user_agents: <p>User agents that the updated rule will match.</p>
            not_device_user_agents: <p>User agents that the updated rule <b>will not</b> match. All other user agents will match.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.update_mobile_device_access_rule_request.UpdateMobileDeviceAccessRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.update_mobile_device_access_rule_response.UpdateMobileDeviceAccessRuleResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.update_mobile_device_access_rule

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.update_mobile_device_access_rule.update_mobile_device_access_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.update_mobile_device_access_rule_request.UpdateMobileDeviceAccessRuleRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["mobile_device_access_rule_id"] = mobile_device_access_rule_id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["effect"] = effect
        if device_types is not None:
            input_["device_types"] = device_types
        if not_device_types is not None:
            input_["not_device_types"] = not_device_types
        if device_models is not None:
            input_["device_models"] = device_models
        if not_device_models is not None:
            input_["not_device_models"] = not_device_models
        if device_operating_systems is not None:
            input_["device_operating_systems"] = device_operating_systems
        if not_device_operating_systems is not None:
            input_["not_device_operating_systems"] = not_device_operating_systems
        if device_user_agents is not None:
            input_["device_user_agents"] = device_user_agents
        if not_device_user_agents is not None:
            input_["not_device_user_agents"] = not_device_user_agents

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_primary_email_address(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        email: "aws_sdk_workmail.types.email_address.EmailAddress",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
    ) -> "aws_sdk_workmail.types.update_primary_email_address_response.UpdatePrimaryEmailAddressResponse":
        """<p>Updates the primary email for a user, group, or resource. The current email is moved into the list of aliases (or swapped between an existing alias and the current primary email), and the email provided in the input is promoted as the primary.</p>

        Args:
            organization_id: <p>The organization that contains the user, group, or resource to update.</p>
            entity_id: <p>The user, group, or resource to update.</p> <p>The identifier can accept <i>UseriD, ResourceId, or GroupId</i>, <i>Username, Resourcename, or Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>
            email: <p>The value of the email to be updated as primary.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.update_primary_email_address_request.UpdatePrimaryEmailAddressRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.update_primary_email_address_response.UpdatePrimaryEmailAddressResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.update_primary_email_address

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.update_primary_email_address.update_primary_email_address(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.update_primary_email_address_request.UpdatePrimaryEmailAddressRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["entity_id"] = entity_id
        input_["email"] = email

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_resource(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        resource_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        name: Optional["aws_sdk_workmail.types.resource_name.ResourceName"] = None,
        booking_options: Optional[
            "aws_sdk_workmail.types.booking_options.BookingOptions"
        ] = None,
        description: Optional[
            "aws_sdk_workmail.types.new_resource_description.NewResourceDescription"
        ] = None,
        type: Optional["aws_sdk_workmail.types.resource_type.ResourceType"] = None,
        hidden_from_global_address_list: Optional[
            "aws_sdk_workmail.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "aws_sdk_workmail.types.update_resource_response.UpdateResourceResponse":
        """<p>Updates data for the resource. To have the latest information, it must be preceded by a <a>DescribeResource</a> call. The dataset in the request should be the one expected when performing another <code>DescribeResource</code> call.</p>

        Args:
            organization_id: <p>The identifier associated with the organization for which the resource is updated.</p>
            resource_id: <p>The identifier of the resource to be updated.</p> <p>The identifier can accept <i>ResourceId</i>, <i>Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Email address: resource@domain.tld</p> </li> <li> <p>Resource name: resource</p> </li> </ul>
            name: <p>The name of the resource to be updated.</p>
            booking_options: <p>The resource's booking options to be updated.</p>
            description: <p>Updates the resource description.</p>
            type: <p>Updates the resource type.</p>
            hidden_from_global_address_list: <p>If enabled, the resource is hidden from the global address list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.update_resource_request.UpdateResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.update_resource_response.UpdateResourceResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.update_resource

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.update_resource.update_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.update_resource_request.UpdateResourceRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["resource_id"] = resource_id
        if name is not None:
            input_["name"] = name
        if booking_options is not None:
            input_["booking_options"] = booking_options
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if hidden_from_global_address_list is not None:
            input_["hidden_from_global_address_list"] = hidden_from_global_address_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_user(
        self,
        organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId",
        user_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier",
        *,
        config_overrides: Optional[WorkMailClientConfig] = None,
        role: Optional["aws_sdk_workmail.types.user_role.UserRole"] = None,
        display_name: Optional[
            "aws_sdk_workmail.types.user_attribute.UserAttribute"
        ] = None,
        first_name: Optional[
            "aws_sdk_workmail.types.user_attribute.UserAttribute"
        ] = None,
        last_name: Optional[
            "aws_sdk_workmail.types.user_attribute.UserAttribute"
        ] = None,
        hidden_from_global_address_list: Optional[
            "aws_sdk_workmail.types.boolean_object.BooleanObject"
        ] = None,
        initials: Optional[
            "aws_sdk_workmail.types.user_attribute.UserAttribute"
        ] = None,
        telephone: Optional[
            "aws_sdk_workmail.types.user_attribute.UserAttribute"
        ] = None,
        street: Optional["aws_sdk_workmail.types.user_attribute.UserAttribute"] = None,
        job_title: Optional[
            "aws_sdk_workmail.types.user_attribute.UserAttribute"
        ] = None,
        city: Optional["aws_sdk_workmail.types.user_attribute.UserAttribute"] = None,
        company: Optional["aws_sdk_workmail.types.user_attribute.UserAttribute"] = None,
        zip_code: Optional[
            "aws_sdk_workmail.types.user_attribute.UserAttribute"
        ] = None,
        department: Optional[
            "aws_sdk_workmail.types.user_attribute.UserAttribute"
        ] = None,
        country: Optional["aws_sdk_workmail.types.user_attribute.UserAttribute"] = None,
        office: Optional["aws_sdk_workmail.types.user_attribute.UserAttribute"] = None,
        identity_provider_user_id: Optional[
            "aws_sdk_workmail.types.identity_provider_user_id_for_update.IdentityProviderUserIdForUpdate"
        ] = None,
    ) -> "aws_sdk_workmail.types.update_user_response.UpdateUserResponse":
        """<p>Updates data for the user. To have the latest information, it must be preceded by a <a>DescribeUser</a> call. The dataset in the request should be the one expected when performing another <code>DescribeUser</code> call.</p>

        Args:
            organization_id: <p>The identifier for the organization under which the user exists.</p>
            user_id: <p>The identifier for the user to be updated.</p> <p>The identifier can be the <i>UserId</i>, <i>Username</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: user@domain.tld</p> </li> <li> <p>User name: user</p> </li> </ul>
            role: <p>Updates the user role.</p> <p>You cannot pass <i>SYSTEM_USER</i> or <i>RESOURCE</i>.</p>
            display_name: <p>Updates the display name of the user.</p>
            first_name: <p>Updates the user's first name.</p>
            last_name: <p>Updates the user's last name.</p>
            hidden_from_global_address_list: <p>If enabled, the user is hidden from the global address list.</p>
            initials: <p>Updates the user's initials.</p>
            telephone: <p>Updates the user's contact details.</p>
            street: <p>Updates the user's street address.</p>
            job_title: <p>Updates the user's job title.</p>
            city: <p>Updates the user's city.</p>
            company: <p>Updates the user's company.</p>
            zip_code: <p>Updates the user's zip code.</p>
            department: <p>Updates the user's department.</p>
            country: <p>Updates the user's country.</p>
            office: <p>Updates the user's office.</p>
            identity_provider_user_id: <p>User ID from the IAM Identity Center. If this parameter is empty it will be updated automatically when the user logs in for the first time to the mailbox associated with WorkMail.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workmail.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_workmail.types.update_user_response.UpdateUserResponse"
        ]:
            import aws_sdk_workmail._operations.work_mail_service.update_user

            output, http_response = (
                aws_sdk_workmail._operations.work_mail_service.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmail.types.update_user_request.UpdateUserRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["user_id"] = user_id
        if role is not None:
            input_["role"] = role
        if display_name is not None:
            input_["display_name"] = display_name
        if first_name is not None:
            input_["first_name"] = first_name
        if last_name is not None:
            input_["last_name"] = last_name
        if hidden_from_global_address_list is not None:
            input_["hidden_from_global_address_list"] = hidden_from_global_address_list
        if initials is not None:
            input_["initials"] = initials
        if telephone is not None:
            input_["telephone"] = telephone
        if street is not None:
            input_["street"] = street
        if job_title is not None:
            input_["job_title"] = job_title
        if city is not None:
            input_["city"] = city
        if company is not None:
            input_["company"] = company
        if zip_code is not None:
            input_["zip_code"] = zip_code
        if department is not None:
            input_["department"] = department
        if country is not None:
            input_["country"] = country
        if office is not None:
            input_["office"] = office
        if identity_provider_user_id is not None:
            input_["identity_provider_user_id"] = identity_provider_user_id

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
