"""Generated from Smithy shape ``com.amazonaws.macie2#Macie2``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_macie2._auth._signers
import aws_sdk_macie2._auth._sigv4
from aws_sdk_macie2._auth._identity import Credentials
from aws_sdk_macie2._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_macie2._auth._zapros_handler import AuthMiddleware
from aws_sdk_macie2._pagination import resolve_path as _resolve_path
from aws_sdk_macie2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__list_of__string
    import aws_sdk_macie2.types.__list_of_automated_discovery_account_update
    import aws_sdk_macie2.types.__list_of_finding_type
    import aws_sdk_macie2.types.__list_of_suppress_data_identifier
    import aws_sdk_macie2.types.__list_of_usage_statistics_filter
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__string_min1_max128_pattern
    import aws_sdk_macie2.types.__string_min1_max512_pattern_ss
    import aws_sdk_macie2.types.accept_invitation_request
    import aws_sdk_macie2.types.accept_invitation_response
    import aws_sdk_macie2.types.account_detail
    import aws_sdk_macie2.types.admin_account
    import aws_sdk_macie2.types.allow_list_criteria
    import aws_sdk_macie2.types.allow_list_summary
    import aws_sdk_macie2.types.auto_enable_mode
    import aws_sdk_macie2.types.automated_discovery_account
    import aws_sdk_macie2.types.automated_discovery_status
    import aws_sdk_macie2.types.batch_get_custom_data_identifiers_request
    import aws_sdk_macie2.types.batch_get_custom_data_identifiers_response
    import aws_sdk_macie2.types.batch_update_automated_discovery_accounts_request
    import aws_sdk_macie2.types.batch_update_automated_discovery_accounts_response
    import aws_sdk_macie2.types.bucket_criteria
    import aws_sdk_macie2.types.bucket_metadata
    import aws_sdk_macie2.types.bucket_sort_criteria
    import aws_sdk_macie2.types.classification_export_configuration
    import aws_sdk_macie2.types.classification_scope_summary
    import aws_sdk_macie2.types.create_allow_list_request
    import aws_sdk_macie2.types.create_allow_list_response
    import aws_sdk_macie2.types.create_classification_job_request
    import aws_sdk_macie2.types.create_classification_job_response
    import aws_sdk_macie2.types.create_custom_data_identifier_request
    import aws_sdk_macie2.types.create_custom_data_identifier_response
    import aws_sdk_macie2.types.create_findings_filter_request
    import aws_sdk_macie2.types.create_findings_filter_response
    import aws_sdk_macie2.types.create_invitations_request
    import aws_sdk_macie2.types.create_invitations_response
    import aws_sdk_macie2.types.create_member_request
    import aws_sdk_macie2.types.create_member_response
    import aws_sdk_macie2.types.create_sample_findings_request
    import aws_sdk_macie2.types.create_sample_findings_response
    import aws_sdk_macie2.types.custom_data_identifier_summary
    import aws_sdk_macie2.types.decline_invitations_request
    import aws_sdk_macie2.types.decline_invitations_response
    import aws_sdk_macie2.types.delete_allow_list_request
    import aws_sdk_macie2.types.delete_allow_list_response
    import aws_sdk_macie2.types.delete_custom_data_identifier_request
    import aws_sdk_macie2.types.delete_custom_data_identifier_response
    import aws_sdk_macie2.types.delete_findings_filter_request
    import aws_sdk_macie2.types.delete_findings_filter_response
    import aws_sdk_macie2.types.delete_invitations_request
    import aws_sdk_macie2.types.delete_invitations_response
    import aws_sdk_macie2.types.delete_member_request
    import aws_sdk_macie2.types.delete_member_response
    import aws_sdk_macie2.types.describe_buckets_request
    import aws_sdk_macie2.types.describe_buckets_response
    import aws_sdk_macie2.types.describe_classification_job_request
    import aws_sdk_macie2.types.describe_classification_job_response
    import aws_sdk_macie2.types.describe_organization_configuration_request
    import aws_sdk_macie2.types.describe_organization_configuration_response
    import aws_sdk_macie2.types.detection
    import aws_sdk_macie2.types.disable_macie_request
    import aws_sdk_macie2.types.disable_macie_response
    import aws_sdk_macie2.types.disable_organization_admin_account_request
    import aws_sdk_macie2.types.disable_organization_admin_account_response
    import aws_sdk_macie2.types.disassociate_from_administrator_account_request
    import aws_sdk_macie2.types.disassociate_from_administrator_account_response
    import aws_sdk_macie2.types.disassociate_from_master_account_request
    import aws_sdk_macie2.types.disassociate_from_master_account_response
    import aws_sdk_macie2.types.disassociate_member_request
    import aws_sdk_macie2.types.disassociate_member_response
    import aws_sdk_macie2.types.enable_macie_request
    import aws_sdk_macie2.types.enable_macie_response
    import aws_sdk_macie2.types.enable_organization_admin_account_request
    import aws_sdk_macie2.types.enable_organization_admin_account_response
    import aws_sdk_macie2.types.finding_criteria
    import aws_sdk_macie2.types.finding_publishing_frequency
    import aws_sdk_macie2.types.finding_statistics_sort_criteria
    import aws_sdk_macie2.types.findings_filter_action
    import aws_sdk_macie2.types.findings_filter_list_item
    import aws_sdk_macie2.types.get_administrator_account_request
    import aws_sdk_macie2.types.get_administrator_account_response
    import aws_sdk_macie2.types.get_allow_list_request
    import aws_sdk_macie2.types.get_allow_list_response
    import aws_sdk_macie2.types.get_automated_discovery_configuration_request
    import aws_sdk_macie2.types.get_automated_discovery_configuration_response
    import aws_sdk_macie2.types.get_bucket_statistics_request
    import aws_sdk_macie2.types.get_bucket_statistics_response
    import aws_sdk_macie2.types.get_classification_export_configuration_request
    import aws_sdk_macie2.types.get_classification_export_configuration_response
    import aws_sdk_macie2.types.get_classification_scope_request
    import aws_sdk_macie2.types.get_classification_scope_response
    import aws_sdk_macie2.types.get_custom_data_identifier_request
    import aws_sdk_macie2.types.get_custom_data_identifier_response
    import aws_sdk_macie2.types.get_finding_statistics_request
    import aws_sdk_macie2.types.get_finding_statistics_response
    import aws_sdk_macie2.types.get_findings_filter_request
    import aws_sdk_macie2.types.get_findings_filter_response
    import aws_sdk_macie2.types.get_findings_publication_configuration_request
    import aws_sdk_macie2.types.get_findings_publication_configuration_response
    import aws_sdk_macie2.types.get_findings_request
    import aws_sdk_macie2.types.get_findings_response
    import aws_sdk_macie2.types.get_invitations_count_request
    import aws_sdk_macie2.types.get_invitations_count_response
    import aws_sdk_macie2.types.get_macie_session_request
    import aws_sdk_macie2.types.get_macie_session_response
    import aws_sdk_macie2.types.get_master_account_request
    import aws_sdk_macie2.types.get_master_account_response
    import aws_sdk_macie2.types.get_member_request
    import aws_sdk_macie2.types.get_member_response
    import aws_sdk_macie2.types.get_resource_profile_request
    import aws_sdk_macie2.types.get_resource_profile_response
    import aws_sdk_macie2.types.get_reveal_configuration_request
    import aws_sdk_macie2.types.get_reveal_configuration_response
    import aws_sdk_macie2.types.get_sensitive_data_occurrences_availability_request
    import aws_sdk_macie2.types.get_sensitive_data_occurrences_availability_response
    import aws_sdk_macie2.types.get_sensitive_data_occurrences_request
    import aws_sdk_macie2.types.get_sensitive_data_occurrences_response
    import aws_sdk_macie2.types.get_sensitivity_inspection_template_request
    import aws_sdk_macie2.types.get_sensitivity_inspection_template_response
    import aws_sdk_macie2.types.get_usage_statistics_request
    import aws_sdk_macie2.types.get_usage_statistics_response
    import aws_sdk_macie2.types.get_usage_totals_request
    import aws_sdk_macie2.types.get_usage_totals_response
    import aws_sdk_macie2.types.group_by
    import aws_sdk_macie2.types.invitation
    import aws_sdk_macie2.types.job_schedule_frequency
    import aws_sdk_macie2.types.job_status
    import aws_sdk_macie2.types.job_summary
    import aws_sdk_macie2.types.job_type
    import aws_sdk_macie2.types.list_allow_lists_request
    import aws_sdk_macie2.types.list_allow_lists_response
    import aws_sdk_macie2.types.list_automated_discovery_accounts_request
    import aws_sdk_macie2.types.list_automated_discovery_accounts_response
    import aws_sdk_macie2.types.list_classification_jobs_request
    import aws_sdk_macie2.types.list_classification_jobs_response
    import aws_sdk_macie2.types.list_classification_scopes_request
    import aws_sdk_macie2.types.list_classification_scopes_response
    import aws_sdk_macie2.types.list_custom_data_identifiers_request
    import aws_sdk_macie2.types.list_custom_data_identifiers_response
    import aws_sdk_macie2.types.list_findings_filters_request
    import aws_sdk_macie2.types.list_findings_filters_response
    import aws_sdk_macie2.types.list_findings_request
    import aws_sdk_macie2.types.list_findings_response
    import aws_sdk_macie2.types.list_invitations_request
    import aws_sdk_macie2.types.list_invitations_response
    import aws_sdk_macie2.types.list_jobs_filter_criteria
    import aws_sdk_macie2.types.list_jobs_sort_criteria
    import aws_sdk_macie2.types.list_managed_data_identifiers_request
    import aws_sdk_macie2.types.list_managed_data_identifiers_response
    import aws_sdk_macie2.types.list_members_request
    import aws_sdk_macie2.types.list_members_response
    import aws_sdk_macie2.types.list_organization_admin_accounts_request
    import aws_sdk_macie2.types.list_organization_admin_accounts_response
    import aws_sdk_macie2.types.list_resource_profile_artifacts_request
    import aws_sdk_macie2.types.list_resource_profile_artifacts_response
    import aws_sdk_macie2.types.list_resource_profile_detections_request
    import aws_sdk_macie2.types.list_resource_profile_detections_response
    import aws_sdk_macie2.types.list_sensitivity_inspection_templates_request
    import aws_sdk_macie2.types.list_sensitivity_inspection_templates_response
    import aws_sdk_macie2.types.list_tags_for_resource_request
    import aws_sdk_macie2.types.list_tags_for_resource_response
    import aws_sdk_macie2.types.macie_status
    import aws_sdk_macie2.types.managed_data_identifier_selector
    import aws_sdk_macie2.types.managed_data_identifier_summary
    import aws_sdk_macie2.types.matching_resource
    import aws_sdk_macie2.types.max_results
    import aws_sdk_macie2.types.member
    import aws_sdk_macie2.types.put_classification_export_configuration_request
    import aws_sdk_macie2.types.put_classification_export_configuration_response
    import aws_sdk_macie2.types.put_findings_publication_configuration_request
    import aws_sdk_macie2.types.put_findings_publication_configuration_response
    import aws_sdk_macie2.types.resource_profile_artifact
    import aws_sdk_macie2.types.reveal_configuration
    import aws_sdk_macie2.types.s3_classification_scope_update
    import aws_sdk_macie2.types.s3_job_definition
    import aws_sdk_macie2.types.search_resources_bucket_criteria
    import aws_sdk_macie2.types.search_resources_request
    import aws_sdk_macie2.types.search_resources_response
    import aws_sdk_macie2.types.search_resources_sort_criteria
    import aws_sdk_macie2.types.security_hub_configuration
    import aws_sdk_macie2.types.sensitivity_inspection_template_excludes
    import aws_sdk_macie2.types.sensitivity_inspection_template_includes
    import aws_sdk_macie2.types.sensitivity_inspection_templates_entry
    import aws_sdk_macie2.types.severity_level_list
    import aws_sdk_macie2.types.sort_criteria
    import aws_sdk_macie2.types.tag_map
    import aws_sdk_macie2.types.tag_resource_request
    import aws_sdk_macie2.types.tag_resource_response
    import aws_sdk_macie2.types.test_custom_data_identifier_request
    import aws_sdk_macie2.types.test_custom_data_identifier_response
    import aws_sdk_macie2.types.time_range
    import aws_sdk_macie2.types.untag_resource_request
    import aws_sdk_macie2.types.untag_resource_response
    import aws_sdk_macie2.types.update_allow_list_request
    import aws_sdk_macie2.types.update_allow_list_response
    import aws_sdk_macie2.types.update_automated_discovery_configuration_request
    import aws_sdk_macie2.types.update_automated_discovery_configuration_response
    import aws_sdk_macie2.types.update_classification_job_request
    import aws_sdk_macie2.types.update_classification_job_response
    import aws_sdk_macie2.types.update_classification_scope_request
    import aws_sdk_macie2.types.update_classification_scope_response
    import aws_sdk_macie2.types.update_findings_filter_request
    import aws_sdk_macie2.types.update_findings_filter_response
    import aws_sdk_macie2.types.update_macie_session_request
    import aws_sdk_macie2.types.update_macie_session_response
    import aws_sdk_macie2.types.update_member_session_request
    import aws_sdk_macie2.types.update_member_session_response
    import aws_sdk_macie2.types.update_organization_configuration_request
    import aws_sdk_macie2.types.update_organization_configuration_response
    import aws_sdk_macie2.types.update_resource_profile_detections_request
    import aws_sdk_macie2.types.update_resource_profile_detections_response
    import aws_sdk_macie2.types.update_resource_profile_request
    import aws_sdk_macie2.types.update_resource_profile_response
    import aws_sdk_macie2.types.update_retrieval_configuration
    import aws_sdk_macie2.types.update_reveal_configuration_request
    import aws_sdk_macie2.types.update_reveal_configuration_response
    import aws_sdk_macie2.types.update_sensitivity_inspection_template_request
    import aws_sdk_macie2.types.update_sensitivity_inspection_template_response
    import aws_sdk_macie2.types.usage_record
    import aws_sdk_macie2.types.usage_statistics_sort_by


class AsyncMacie2ClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncMacie2Client:
    """A client for the ``Macie2`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncMacie2ClientConfig(
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
        self, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMacie2ClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def accept_invitation(
        self,
        invitation_id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        administrator_account_id: Optional[
            "aws_sdk_macie2.types.__string.__string"
        ] = None,
        master_account: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.accept_invitation_response.AcceptInvitationResponse":
        """<p>Accepts an Amazon Macie membership invitation that was received from a specific account.</p>

        Args:
            administrator_account_id: <p>The Amazon Web Services account ID for the account that sent the invitation.</p>
            invitation_id: <p>The unique identifier for the invitation to accept.</p>
            master_account: <p>(Deprecated) The Amazon Web Services account ID for the account that sent the invitation. This property has been replaced by the administratorAccountId property and is retained only for backward compatibility.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.accept_invitation_request.AcceptInvitationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.accept_invitation_response.AcceptInvitationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.accept_invitation

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.accept_invitation.async_accept_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.accept_invitation_request.AcceptInvitationRequest = {}  # type: ignore[typeddict-item]
        if administrator_account_id is not None:
            input_["administrator_account_id"] = administrator_account_id
        input_["invitation_id"] = invitation_id
        if master_account is not None:
            input_["master_account"] = master_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_custom_data_identifiers(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        ids: Optional["aws_sdk_macie2.types.__list_of__string.__listOf__string"] = None,
    ) -> "aws_sdk_macie2.types.batch_get_custom_data_identifiers_response.BatchGetCustomDataIdentifiersResponse":
        """<p>Retrieves information about one or more custom data identifiers.</p>

        Args:
            ids: <p>An array of custom data identifier IDs, one for each custom data identifier to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.batch_get_custom_data_identifiers_request.BatchGetCustomDataIdentifiersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.batch_get_custom_data_identifiers_response.BatchGetCustomDataIdentifiersResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.batch_get_custom_data_identifiers

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.batch_get_custom_data_identifiers.async_batch_get_custom_data_identifiers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.batch_get_custom_data_identifiers_request.BatchGetCustomDataIdentifiersRequest = {}  # type: ignore[typeddict-item]
        if ids is not None:
            input_["ids"] = ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_update_automated_discovery_accounts(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        accounts: Optional[
            "aws_sdk_macie2.types.__list_of_automated_discovery_account_update.__listOfAutomatedDiscoveryAccountUpdate"
        ] = None,
    ) -> "aws_sdk_macie2.types.batch_update_automated_discovery_accounts_response.BatchUpdateAutomatedDiscoveryAccountsResponse":
        """<p>Changes the status of automated sensitive data discovery for one or more accounts.</p>

        Args:
            accounts: <p>An array of objects, one for each account to change the status of automated sensitive data discovery for. Each object specifies the Amazon Web Services account ID for an account and a new status for that account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.batch_update_automated_discovery_accounts_request.BatchUpdateAutomatedDiscoveryAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.batch_update_automated_discovery_accounts_response.BatchUpdateAutomatedDiscoveryAccountsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.batch_update_automated_discovery_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.batch_update_automated_discovery_accounts.async_batch_update_automated_discovery_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.batch_update_automated_discovery_accounts_request.BatchUpdateAutomatedDiscoveryAccountsRequest = {}  # type: ignore[typeddict-item]
        if accounts is not None:
            input_["accounts"] = accounts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_allow_list(
        self,
        client_token: "aws_sdk_macie2.types.__string.__string",
        criteria: "aws_sdk_macie2.types.allow_list_criteria.AllowListCriteria",
        name: "aws_sdk_macie2.types.__string_min1_max128_pattern.__stringMin1Max128Pattern",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        description: Optional[
            "aws_sdk_macie2.types.__string_min1_max512_pattern_ss.__stringMin1Max512PatternSS"
        ] = None,
        tags: Optional["aws_sdk_macie2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_macie2.types.create_allow_list_response.CreateAllowListResponse":
        """<p>Creates and defines the settings for an allow list.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
            criteria: <p>The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an S3 object that lists specific text to ignore (s3WordsList), or a regular expression (regex) that defines a text pattern to ignore.</p>
            description: <p>A custom description of the allow list. The description can contain as many as 512 characters.</p>
            name: <p>A custom name for the allow list. The name can contain as many as 128 characters.</p>
            tags: <p>A map of key-value pairs that specifies the tags to associate with the allow list.</p> <p>An allow list can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.create_allow_list_request.CreateAllowListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.create_allow_list_response.CreateAllowListResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.create_allow_list

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.create_allow_list.async_create_allow_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.create_allow_list_request.CreateAllowListRequest = {}  # type: ignore[typeddict-item]
        input_["client_token"] = client_token
        input_["criteria"] = criteria
        if description is not None:
            input_["description"] = description
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_classification_job(
        self,
        client_token: "aws_sdk_macie2.types.__string.__string",
        job_type: "aws_sdk_macie2.types.job_type.JobType",
        name: "aws_sdk_macie2.types.__string.__string",
        s3_job_definition: "aws_sdk_macie2.types.s3_job_definition.S3JobDefinition",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        allow_list_ids: Optional[
            "aws_sdk_macie2.types.__list_of__string.__listOf__string"
        ] = None,
        custom_data_identifier_ids: Optional[
            "aws_sdk_macie2.types.__list_of__string.__listOf__string"
        ] = None,
        description: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        initial_run: Optional["aws_sdk_macie2.types.__boolean.__boolean"] = None,
        managed_data_identifier_ids: Optional[
            "aws_sdk_macie2.types.__list_of__string.__listOf__string"
        ] = None,
        managed_data_identifier_selector: Optional[
            "aws_sdk_macie2.types.managed_data_identifier_selector.ManagedDataIdentifierSelector"
        ] = None,
        sampling_percentage: Optional[
            "aws_sdk_macie2.types.__integer.__integer"
        ] = None,
        schedule_frequency: Optional[
            "aws_sdk_macie2.types.job_schedule_frequency.JobScheduleFrequency"
        ] = None,
        tags: Optional["aws_sdk_macie2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_macie2.types.create_classification_job_response.CreateClassificationJobResponse":
        """<p>Creates and defines the settings for a classification job.</p>

        Args:
            allow_list_ids: <p>An array of unique identifiers, one for each allow list for the job to use when it analyzes data.</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
            custom_data_identifier_ids: <p>An array of unique identifiers, one for each custom data identifier for the job to use when it analyzes data. To use only managed data identifiers, don't specify a value for this property and specify a value other than NONE for the managedDataIdentifierSelector property.</p>
            description: <p>A custom description of the job. The description can contain as many as 200 characters.</p>
            initial_run: <p>For a recurring job, specifies whether to analyze all existing, eligible objects immediately after the job is created (true). To analyze only those objects that are created or changed after you create the job and before the job's first scheduled run, set this value to false.</p> <p>If you configure the job to run only once, don't specify a value for this property.</p>
            job_type: <p>The schedule for running the job. Valid values are:</p> <ul><li><p>ONE_TIME - Run the job only once. If you specify this value, don't specify a value for the scheduleFrequency property.</p></li> <li><p>SCHEDULED - Run the job on a daily, weekly, or monthly basis. If you specify this value, use the scheduleFrequency property to specify the recurrence pattern for the job.</p></li></ul>
            managed_data_identifier_ids: <p>An array of unique identifiers, one for each managed data identifier for the job to include (use) or exclude (not use) when it analyzes data. Inclusion or exclusion depends on the managed data identifier selection type that you specify for the job (managedDataIdentifierSelector).</p> <p>To retrieve a list of valid values for this property, use the ListManagedDataIdentifiers operation.</p>
            managed_data_identifier_selector: <p>The selection type to apply when determining which managed data identifiers the job uses to analyze data. Valid values are:</p> <ul><li><p>ALL - Use all managed data identifiers. If you specify this value, don't specify any values for the managedDataIdentifierIds property.</p></li> <li><p>EXCLUDE - Use all managed data identifiers except the ones specified by the managedDataIdentifierIds property.</p></li> <li><p>INCLUDE - Use only the managed data identifiers specified by the managedDataIdentifierIds property.</p></li> <li><p>NONE - Don't use any managed data identifiers. If you specify this value, specify at least one value for the customDataIdentifierIds property and don't specify any values for the managedDataIdentifierIds property.</p></li> <li><p>RECOMMENDED (default) - Use the recommended set of managed data identifiers. If you specify this value, don't specify any values for the managedDataIdentifierIds property.</p></li></ul> <p>If you don't specify a value for this property, the job uses the recommended set of managed data identifiers.</p> <p>If the job is a recurring job and you specify ALL or EXCLUDE, each job run automatically uses new managed data identifiers that are released. If you don't specify a value for this property or you specify RECOMMENDED for a recurring job, each job run automatically uses all the managed data identifiers that are in the recommended set when the run starts.</p> <p>To learn about individual managed data identifiers or determine which ones are in the recommended set, see <a href=\"https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html\">Using managed data identifiers</a> or <a href=\"https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-mdis-recommended.html\">Recommended managed data identifiers</a> in the <i>Amazon Macie User Guide</i>.</p>
            name: <p>A custom name for the job. The name can contain as many as 500 characters.</p>
            s3_job_definition: <p>The S3 buckets that contain the objects to analyze, and the scope of that analysis.</p>
            sampling_percentage: <p>The sampling depth, as a percentage, for the job to apply when processing objects. This value determines the percentage of eligible objects that the job analyzes. If this value is less than 100, Amazon Macie selects the objects to analyze at random, up to the specified percentage, and analyzes all the data in those objects.</p>
            schedule_frequency: <p>The recurrence pattern for running the job. To run the job only once, don't specify a value for this property and set the value for the jobType property to ONE_TIME.</p>
            tags: <p>A map of key-value pairs that specifies the tags to associate with the job.</p> <p>A job can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.create_classification_job_request.CreateClassificationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.create_classification_job_response.CreateClassificationJobResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.create_classification_job

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.create_classification_job.async_create_classification_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.create_classification_job_request.CreateClassificationJobRequest = {}  # type: ignore[typeddict-item]
        if allow_list_ids is not None:
            input_["allow_list_ids"] = allow_list_ids
        input_["client_token"] = client_token
        if custom_data_identifier_ids is not None:
            input_["custom_data_identifier_ids"] = custom_data_identifier_ids
        if description is not None:
            input_["description"] = description
        if initial_run is not None:
            input_["initial_run"] = initial_run
        input_["job_type"] = job_type
        if managed_data_identifier_ids is not None:
            input_["managed_data_identifier_ids"] = managed_data_identifier_ids
        if managed_data_identifier_selector is not None:
            input_["managed_data_identifier_selector"] = (
                managed_data_identifier_selector
            )
        input_["name"] = name
        input_["s3_job_definition"] = s3_job_definition
        if sampling_percentage is not None:
            input_["sampling_percentage"] = sampling_percentage
        if schedule_frequency is not None:
            input_["schedule_frequency"] = schedule_frequency
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_custom_data_identifier(
        self,
        name: "aws_sdk_macie2.types.__string.__string",
        regex: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        client_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        description: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        ignore_words: Optional[
            "aws_sdk_macie2.types.__list_of__string.__listOf__string"
        ] = None,
        keywords: Optional[
            "aws_sdk_macie2.types.__list_of__string.__listOf__string"
        ] = None,
        maximum_match_distance: Optional[
            "aws_sdk_macie2.types.__integer.__integer"
        ] = None,
        severity_levels: Optional[
            "aws_sdk_macie2.types.severity_level_list.SeverityLevelList"
        ] = None,
        tags: Optional["aws_sdk_macie2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_macie2.types.create_custom_data_identifier_response.CreateCustomDataIdentifierResponse":
        """<p>Creates and defines the criteria and other settings for a custom data identifier.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
            description: <p>A custom description of the custom data identifier. The description can contain as many as 512 characters.</p> <p>We strongly recommend that you avoid including any sensitive data in the description of a custom data identifier. Other users of your account might be able to see this description, depending on the actions that they're allowed to perform in Amazon Macie.</p>
            ignore_words: <p>An array that lists specific character sequences (<i>ignore words</i>) to exclude from the results. If the text matched by the regular expression contains any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive.</p>
            keywords: <p>An array that lists specific character sequences (<i>keywords</i>), one of which must precede and be within proximity (maximumMatchDistance) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren't case sensitive.</p>
            maximum_match_distance: <p>The maximum number of characters that can exist between the end of at least one complete character sequence specified by the keywords array and the end of the text that matches the regex pattern. If a complete keyword precedes all the text that matches the pattern and the keyword is within the specified distance, Amazon Macie includes the result. The distance can be 1-300 characters. The default value is 50.</p>
            name: <p>A custom name for the custom data identifier. The name can contain as many as 128 characters.</p> <p>We strongly recommend that you avoid including any sensitive data in the name of a custom data identifier. Other users of your account might be able to see this name, depending on the actions that they're allowed to perform in Amazon Macie.</p>
            regex: <p>The regular expression (<i>regex</i>) that defines the pattern to match. The expression can contain as many as 512 characters.</p>
            severity_levels: <p>The severity to assign to findings that the custom data identifier produces, based on the number of occurrences of text that match the custom data identifier's detection criteria. You can specify as many as three SeverityLevel objects in this array, one for each severity: LOW, MEDIUM, or HIGH. If you specify more than one, the occurrences thresholds must be in ascending order by severity, moving from LOW to HIGH. For example, 1 for LOW, 50 for MEDIUM, and 100 for HIGH. If an S3 object contains fewer occurrences than the lowest specified threshold, Amazon Macie doesn't create a finding.</p> <p>If you don't specify any values for this array, Macie creates findings for S3 objects that contain at least one occurrence of text that matches the detection criteria, and Macie assigns the MEDIUM severity to those findings.</p>
            tags: <p>A map of key-value pairs that specifies the tags to associate with the custom data identifier.</p> <p>A custom data identifier can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.create_custom_data_identifier_request.CreateCustomDataIdentifierRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.create_custom_data_identifier_response.CreateCustomDataIdentifierResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.create_custom_data_identifier

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.create_custom_data_identifier.async_create_custom_data_identifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.create_custom_data_identifier_request.CreateCustomDataIdentifierRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if ignore_words is not None:
            input_["ignore_words"] = ignore_words
        if keywords is not None:
            input_["keywords"] = keywords
        if maximum_match_distance is not None:
            input_["maximum_match_distance"] = maximum_match_distance
        input_["name"] = name
        input_["regex"] = regex
        if severity_levels is not None:
            input_["severity_levels"] = severity_levels
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_findings_filter(
        self,
        action: "aws_sdk_macie2.types.findings_filter_action.FindingsFilterAction",
        finding_criteria: "aws_sdk_macie2.types.finding_criteria.FindingCriteria",
        name: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        client_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        description: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        position: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        tags: Optional["aws_sdk_macie2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_macie2.types.create_findings_filter_response.CreateFindingsFilterResponse":
        """<p>Creates and defines the criteria and other settings for a findings filter.</p>

        Args:
            action: <p>The action to perform on findings that match the filter criteria (findingCriteria). Valid values are: ARCHIVE, suppress (automatically archive) the findings; and, NOOP, don't perform any action on the findings.</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
            description: <p>A custom description of the filter. The description can contain as many as 512 characters.</p> <p>We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users of your account might be able to see this description, depending on the actions that they're allowed to perform in Amazon Macie.</p>
            finding_criteria: <p>The criteria to use to filter findings.</p>
            name: <p>A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters.</p> <p>We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users of your account might be able to see this name, depending on the actions that they're allowed to perform in Amazon Macie.</p>
            position: <p>The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.</p>
            tags: <p>A map of key-value pairs that specifies the tags to associate with the filter.</p> <p>A findings filter can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.create_findings_filter_request.CreateFindingsFilterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.create_findings_filter_response.CreateFindingsFilterResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.create_findings_filter

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.create_findings_filter.async_create_findings_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.create_findings_filter_request.CreateFindingsFilterRequest = {}  # type: ignore[typeddict-item]
        input_["action"] = action
        if client_token is not None:
            input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        input_["finding_criteria"] = finding_criteria
        input_["name"] = name
        if position is not None:
            input_["position"] = position
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_invitations(
        self,
        account_ids: "aws_sdk_macie2.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        disable_email_notification: Optional[
            "aws_sdk_macie2.types.__boolean.__boolean"
        ] = None,
        message: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.create_invitations_response.CreateInvitationsResponse":
        """<p>Sends an Amazon Macie membership invitation to one or more accounts.</p>

        Args:
            account_ids: <p>An array that lists Amazon Web Services account IDs, one for each account to send the invitation to.</p>
            disable_email_notification: <p>Specifies whether to send the invitation as an email message. If this value is false, Amazon Macie sends the invitation (as an email message) to the email address that you specified for the recipient's account when you associated the account with your account. The default value is false.</p>
            message: <p>Custom text to include in the email message that contains the invitation. The text can contain as many as 80 alphanumeric characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.create_invitations_request.CreateInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.create_invitations_response.CreateInvitationsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.create_invitations

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.create_invitations.async_create_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.create_invitations_request.CreateInvitationsRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids
        if disable_email_notification is not None:
            input_["disable_email_notification"] = disable_email_notification
        if message is not None:
            input_["message"] = message

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_member(
        self,
        account: "aws_sdk_macie2.types.account_detail.AccountDetail",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        tags: Optional["aws_sdk_macie2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_macie2.types.create_member_response.CreateMemberResponse":
        """<p>Associates an account with an Amazon Macie administrator account.</p>

        Args:
            account: <p>The details of the account to associate with the administrator account.</p>
            tags: <p>A map of key-value pairs that specifies the tags to associate with the account in Amazon Macie.</p> <p>An account can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.create_member_request.CreateMemberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.create_member_response.CreateMemberResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.create_member

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.create_member.async_create_member(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.create_member_request.CreateMemberRequest = {}  # type: ignore[typeddict-item]
        input_["account"] = account
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_sample_findings(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        finding_types: Optional[
            "aws_sdk_macie2.types.__list_of_finding_type.__listOfFindingType"
        ] = None,
    ) -> "aws_sdk_macie2.types.create_sample_findings_response.CreateSampleFindingsResponse":
        """<p>Creates sample findings.</p>

        Args:
            finding_types: <p>An array of finding types, one for each type of sample finding to create. To create a sample of every type of finding that Amazon Macie supports, don't include this array in your request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.create_sample_findings_request.CreateSampleFindingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.create_sample_findings_response.CreateSampleFindingsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.create_sample_findings

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.create_sample_findings.async_create_sample_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.create_sample_findings_request.CreateSampleFindingsRequest = {}  # type: ignore[typeddict-item]
        if finding_types is not None:
            input_["finding_types"] = finding_types

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def decline_invitations(
        self,
        account_ids: "aws_sdk_macie2.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.decline_invitations_response.DeclineInvitationsResponse":
        """<p>Declines Amazon Macie membership invitations that were received from specific accounts.</p>

        Args:
            account_ids: <p>An array that lists Amazon Web Services account IDs, one for each account that sent an invitation to decline.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.decline_invitations_request.DeclineInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.decline_invitations_response.DeclineInvitationsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.decline_invitations

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.decline_invitations.async_decline_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.decline_invitations_request.DeclineInvitationsRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_allow_list(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        ignore_job_checks: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.delete_allow_list_response.DeleteAllowListResponse":
        """<p>Deletes an allow list.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
            ignore_job_checks: <p>Specifies whether to force deletion of the allow list, even if active classification jobs are configured to use the list.</p> <p>When you try to delete an allow list, Amazon Macie checks for classification jobs that use the list and have a status other than COMPLETE or CANCELLED. By default, Macie rejects your request if any jobs meet these criteria. To skip these checks and delete the list, set this value to true. To delete the list only if no active jobs are configured to use it, set this value to false.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.delete_allow_list_request.DeleteAllowListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.delete_allow_list_response.DeleteAllowListResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.delete_allow_list

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.delete_allow_list.async_delete_allow_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.delete_allow_list_request.DeleteAllowListRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if ignore_job_checks is not None:
            input_["ignore_job_checks"] = ignore_job_checks

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_custom_data_identifier(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.delete_custom_data_identifier_response.DeleteCustomDataIdentifierResponse":
        """<p>Soft deletes a custom data identifier.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.delete_custom_data_identifier_request.DeleteCustomDataIdentifierRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.delete_custom_data_identifier_response.DeleteCustomDataIdentifierResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.delete_custom_data_identifier

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.delete_custom_data_identifier.async_delete_custom_data_identifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.delete_custom_data_identifier_request.DeleteCustomDataIdentifierRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_findings_filter(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.delete_findings_filter_response.DeleteFindingsFilterResponse":
        """<p>Deletes a findings filter.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.delete_findings_filter_request.DeleteFindingsFilterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.delete_findings_filter_response.DeleteFindingsFilterResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.delete_findings_filter

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.delete_findings_filter.async_delete_findings_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.delete_findings_filter_request.DeleteFindingsFilterRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_invitations(
        self,
        account_ids: "aws_sdk_macie2.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.delete_invitations_response.DeleteInvitationsResponse":
        """<p>Deletes Amazon Macie membership invitations that were received from specific accounts.</p>

        Args:
            account_ids: <p>An array that lists Amazon Web Services account IDs, one for each account that sent an invitation to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.delete_invitations_request.DeleteInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.delete_invitations_response.DeleteInvitationsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.delete_invitations

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.delete_invitations.async_delete_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.delete_invitations_request.DeleteInvitationsRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_member(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.delete_member_response.DeleteMemberResponse":
        """<p>Deletes the association between an Amazon Macie administrator account and an account.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.delete_member_request.DeleteMemberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.delete_member_response.DeleteMemberResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.delete_member

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.delete_member.async_delete_member(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.delete_member_request.DeleteMemberRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_buckets(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        criteria: Optional[
            "aws_sdk_macie2.types.bucket_criteria.BucketCriteria"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        sort_criteria: Optional[
            "aws_sdk_macie2.types.bucket_sort_criteria.BucketSortCriteria"
        ] = None,
    ) -> "aws_sdk_macie2.types.describe_buckets_response.DescribeBucketsResponse":
        """<p>Retrieves (queries) statistical data and other information about one or more S3 buckets that Amazon Macie monitors and analyzes for an account.</p>

        Args:
            criteria: <p>The criteria to use to filter the query results.</p>
            max_results: <p>The maximum number of items to include in each page of the response. The default value is 50.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
            sort_criteria: <p>The criteria to use to sort the query results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.describe_buckets_request.DescribeBucketsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.describe_buckets_response.DescribeBucketsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.describe_buckets

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.describe_buckets.async_describe_buckets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.describe_buckets_request.DescribeBucketsRequest = {}  # type: ignore[typeddict-item]
        if criteria is not None:
            input_["criteria"] = criteria
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_buckets(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        criteria: Optional[
            "aws_sdk_macie2.types.bucket_criteria.BucketCriteria"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        sort_criteria: Optional[
            "aws_sdk_macie2.types.bucket_sort_criteria.BucketSortCriteria"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.bucket_metadata.BucketMetadata]":
        _token = next_token
        while True:
            _response = await self.describe_buckets(
                config_overrides=config_overrides,
                criteria=criteria,
                max_results=max_results,
                next_token=_token,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("buckets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_classification_job(
        self,
        job_id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.describe_classification_job_response.DescribeClassificationJobResponse":
        """<p>Retrieves the status and settings for a classification job.</p>

        Args:
            job_id: <p>The unique identifier for the classification job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.describe_classification_job_request.DescribeClassificationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.describe_classification_job_response.DescribeClassificationJobResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.describe_classification_job

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.describe_classification_job.async_describe_classification_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.describe_classification_job_request.DescribeClassificationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_organization_configuration(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse":
        """<p>Retrieves the Amazon Macie configuration settings for an organization in Organizations.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.describe_organization_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.describe_organization_configuration.async_describe_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_macie(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.disable_macie_response.DisableMacieResponse":
        """<p>Disables Amazon Macie and deletes all settings and resources for a Macie account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.disable_macie_request.DisableMacieRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.disable_macie_response.DisableMacieResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.disable_macie

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.disable_macie.async_disable_macie(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.disable_macie_request.DisableMacieRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_organization_admin_account(
        self,
        admin_account_id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.disable_organization_admin_account_response.DisableOrganizationAdminAccountResponse":
        """<p>Disables an account as the delegated Amazon Macie administrator account for an organization in Organizations.</p>

        Args:
            admin_account_id: <p>The Amazon Web Services account ID of the delegated Amazon Macie administrator account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.disable_organization_admin_account_request.DisableOrganizationAdminAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.disable_organization_admin_account_response.DisableOrganizationAdminAccountResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.disable_organization_admin_account

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.disable_organization_admin_account.async_disable_organization_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.disable_organization_admin_account_request.DisableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
        input_["admin_account_id"] = admin_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_from_administrator_account(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.disassociate_from_administrator_account_response.DisassociateFromAdministratorAccountResponse":
        """<p>Disassociates a member account from its Amazon Macie administrator account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.disassociate_from_administrator_account_request.DisassociateFromAdministratorAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.disassociate_from_administrator_account_response.DisassociateFromAdministratorAccountResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.disassociate_from_administrator_account

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.disassociate_from_administrator_account.async_disassociate_from_administrator_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.disassociate_from_administrator_account_request.DisassociateFromAdministratorAccountRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_from_master_account(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.disassociate_from_master_account_response.DisassociateFromMasterAccountResponse":
        """<p>(Deprecated) Disassociates a member account from its Amazon Macie administrator account. This operation has been replaced by the <link linkend=\"DisassociateFromAdministratorAccount\">DisassociateFromAdministratorAccount</link> operation.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.disassociate_from_master_account_request.DisassociateFromMasterAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.disassociate_from_master_account_response.DisassociateFromMasterAccountResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.disassociate_from_master_account

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.disassociate_from_master_account.async_disassociate_from_master_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.disassociate_from_master_account_request.DisassociateFromMasterAccountRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_member(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.disassociate_member_response.DisassociateMemberResponse":
        """<p>Disassociates an Amazon Macie administrator account from a member account.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.disassociate_member_request.DisassociateMemberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.disassociate_member_response.DisassociateMemberResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.disassociate_member

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.disassociate_member.async_disassociate_member(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.disassociate_member_request.DisassociateMemberRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_macie(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        client_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        finding_publishing_frequency: Optional[
            "aws_sdk_macie2.types.finding_publishing_frequency.FindingPublishingFrequency"
        ] = None,
        status: Optional["aws_sdk_macie2.types.macie_status.MacieStatus"] = None,
    ) -> "aws_sdk_macie2.types.enable_macie_response.EnableMacieResponse":
        """<p>Enables Amazon Macie and specifies the configuration settings for a Macie account.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
            finding_publishing_frequency: <p>Specifies how often to publish updates to policy findings for the account. This includes publishing updates to Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events).</p>
            status: <p>Specifies the new status for the account. To enable Amazon Macie and start all Macie activities for the account, set this value to ENABLED.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.enable_macie_request.EnableMacieRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.enable_macie_response.EnableMacieResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.enable_macie

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.enable_macie.async_enable_macie(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.enable_macie_request.EnableMacieRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if finding_publishing_frequency is not None:
            input_["finding_publishing_frequency"] = finding_publishing_frequency
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_organization_admin_account(
        self,
        admin_account_id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        client_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.enable_organization_admin_account_response.EnableOrganizationAdminAccountResponse":
        """<p>Designates an account as the delegated Amazon Macie administrator account for an organization in Organizations.</p>

        Args:
            admin_account_id: <p>The Amazon Web Services account ID for the account to designate as the delegated Amazon Macie administrator account for the organization.</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.enable_organization_admin_account_response.EnableOrganizationAdminAccountResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.enable_organization_admin_account

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.enable_organization_admin_account.async_enable_organization_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
        input_["admin_account_id"] = admin_account_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_administrator_account(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.get_administrator_account_response.GetAdministratorAccountResponse":
        """<p>Retrieves information about the Amazon Macie administrator account for an account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_administrator_account_request.GetAdministratorAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_administrator_account_response.GetAdministratorAccountResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_administrator_account

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_administrator_account.async_get_administrator_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_administrator_account_request.GetAdministratorAccountRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_allow_list(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.get_allow_list_response.GetAllowListResponse":
        """<p>Retrieves the settings and status of an allow list.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_allow_list_request.GetAllowListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_allow_list_response.GetAllowListResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_allow_list

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_allow_list.async_get_allow_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_allow_list_request.GetAllowListRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_automated_discovery_configuration(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.get_automated_discovery_configuration_response.GetAutomatedDiscoveryConfigurationResponse":
        """<p>Retrieves the configuration settings and status of automated sensitive data discovery for an organization or standalone account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_automated_discovery_configuration_request.GetAutomatedDiscoveryConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_automated_discovery_configuration_response.GetAutomatedDiscoveryConfigurationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_automated_discovery_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_automated_discovery_configuration.async_get_automated_discovery_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_automated_discovery_configuration_request.GetAutomatedDiscoveryConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_bucket_statistics(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        account_id: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.get_bucket_statistics_response.GetBucketStatisticsResponse":
        """<p>Retrieves (queries) aggregated statistical data about all the S3 buckets that Amazon Macie monitors and analyzes for an account.</p>

        Args:
            account_id: <p>The unique identifier for the Amazon Web Services account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_bucket_statistics_request.GetBucketStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_bucket_statistics_response.GetBucketStatisticsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_bucket_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_bucket_statistics.async_get_bucket_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_bucket_statistics_request.GetBucketStatisticsRequest = {}  # type: ignore[typeddict-item]
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_classification_export_configuration(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.get_classification_export_configuration_response.GetClassificationExportConfigurationResponse":
        """<p>Retrieves the configuration settings for storing data classification results.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_classification_export_configuration_request.GetClassificationExportConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_classification_export_configuration_response.GetClassificationExportConfigurationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_classification_export_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_classification_export_configuration.async_get_classification_export_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_classification_export_configuration_request.GetClassificationExportConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_classification_scope(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.get_classification_scope_response.GetClassificationScopeResponse":
        """<p>Retrieves the classification scope settings for an account.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_classification_scope_request.GetClassificationScopeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_classification_scope_response.GetClassificationScopeResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_classification_scope

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_classification_scope.async_get_classification_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_classification_scope_request.GetClassificationScopeRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_custom_data_identifier(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.get_custom_data_identifier_response.GetCustomDataIdentifierResponse":
        """<p>Retrieves the criteria and other settings for a custom data identifier.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_custom_data_identifier_request.GetCustomDataIdentifierRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_custom_data_identifier_response.GetCustomDataIdentifierResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_custom_data_identifier

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_custom_data_identifier.async_get_custom_data_identifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_custom_data_identifier_request.GetCustomDataIdentifierRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_findings(
        self,
        finding_ids: "aws_sdk_macie2.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        sort_criteria: Optional[
            "aws_sdk_macie2.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "aws_sdk_macie2.types.get_findings_response.GetFindingsResponse":
        """<p>Retrieves the details of one or more findings.</p>

        Args:
            finding_ids: <p>An array of strings that lists the unique identifiers for the findings to retrieve. You can specify as many as 50 unique identifiers in this array.</p>
            sort_criteria: <p>The criteria for sorting the results of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_findings_request.GetFindingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_findings_response.GetFindingsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_findings

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_findings.async_get_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_findings_request.GetFindingsRequest = {}  # type: ignore[typeddict-item]
        input_["finding_ids"] = finding_ids
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_findings_filter(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.get_findings_filter_response.GetFindingsFilterResponse":
        """<p>Retrieves the criteria and other settings for a findings filter.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_findings_filter_request.GetFindingsFilterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_findings_filter_response.GetFindingsFilterResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_findings_filter

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_findings_filter.async_get_findings_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_findings_filter_request.GetFindingsFilterRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_findings_publication_configuration(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.get_findings_publication_configuration_response.GetFindingsPublicationConfigurationResponse":
        """<p>Retrieves the configuration settings for publishing findings to Security Hub.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_findings_publication_configuration_request.GetFindingsPublicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_findings_publication_configuration_response.GetFindingsPublicationConfigurationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_findings_publication_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_findings_publication_configuration.async_get_findings_publication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_findings_publication_configuration_request.GetFindingsPublicationConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_finding_statistics(
        self,
        group_by: "aws_sdk_macie2.types.group_by.GroupBy",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        finding_criteria: Optional[
            "aws_sdk_macie2.types.finding_criteria.FindingCriteria"
        ] = None,
        size: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        sort_criteria: Optional[
            "aws_sdk_macie2.types.finding_statistics_sort_criteria.FindingStatisticsSortCriteria"
        ] = None,
    ) -> "aws_sdk_macie2.types.get_finding_statistics_response.GetFindingStatisticsResponse":
        """<p>Retrieves (queries) aggregated statistical data about findings.</p>

        Args:
            finding_criteria: <p>The criteria to use to filter the query results.</p>
            group_by: <p>The finding property to use to group the query results. Valid values are:</p> <ul><li><p>classificationDetails.jobId - The unique identifier for the classification job that produced the finding.</p></li> <li><p>resourcesAffected.s3Bucket.name - The name of the S3 bucket that the finding applies to.</p></li> <li><p>severity.description - The severity level of the finding, such as High or Medium.</p></li> <li><p>type - The type of finding, such as Policy:IAMUser/S3BucketPublic and SensitiveData:S3Object/Personal.</p></li></ul>
            size: <p>The maximum number of items to include in each page of the response.</p>
            sort_criteria: <p>The criteria to use to sort the query results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_finding_statistics_request.GetFindingStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_finding_statistics_response.GetFindingStatisticsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_finding_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_finding_statistics.async_get_finding_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_finding_statistics_request.GetFindingStatisticsRequest = {}  # type: ignore[typeddict-item]
        if finding_criteria is not None:
            input_["finding_criteria"] = finding_criteria
        input_["group_by"] = group_by
        if size is not None:
            input_["size"] = size
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_invitations_count(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.get_invitations_count_response.GetInvitationsCountResponse":
        """<p>Retrieves the count of Amazon Macie membership invitations that were received by an account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_invitations_count_request.GetInvitationsCountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_invitations_count_response.GetInvitationsCountResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_invitations_count

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_invitations_count.async_get_invitations_count(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_invitations_count_request.GetInvitationsCountRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_macie_session(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.get_macie_session_response.GetMacieSessionResponse":
        """<p>Retrieves the status and configuration settings for an Amazon Macie account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_macie_session_request.GetMacieSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_macie_session_response.GetMacieSessionResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_macie_session

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_macie_session.async_get_macie_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_macie_session_request.GetMacieSessionRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_master_account(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.get_master_account_response.GetMasterAccountResponse":
        """<p>(Deprecated) Retrieves information about the Amazon Macie administrator account for an account. This operation has been replaced by the <link linkend=\"GetAdministratorAccount\">GetAdministratorAccount</link> operation.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_master_account_request.GetMasterAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_master_account_response.GetMasterAccountResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_master_account

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_master_account.async_get_master_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_master_account_request.GetMasterAccountRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_member(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.get_member_response.GetMemberResponse":
        """<p>Retrieves information about an account that's associated with an Amazon Macie administrator account.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_member_request.GetMemberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_member_response.GetMemberResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_member

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_member.async_get_member(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_member_request.GetMemberRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_profile(
        self,
        resource_arn: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> (
        "aws_sdk_macie2.types.get_resource_profile_response.GetResourceProfileResponse"
    ):
        """<p>Retrieves (queries) sensitive data discovery statistics and the sensitivity score for an S3 bucket.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the S3 bucket that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_resource_profile_request.GetResourceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_resource_profile_response.GetResourceProfileResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_resource_profile

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_resource_profile.async_get_resource_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_resource_profile_request.GetResourceProfileRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_reveal_configuration(
        self, *, config_overrides: Optional[AsyncMacie2ClientConfig] = None
    ) -> "aws_sdk_macie2.types.get_reveal_configuration_response.GetRevealConfigurationResponse":
        """<p>Retrieves the status and configuration settings for retrieving occurrences of sensitive data reported by findings.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_reveal_configuration_request.GetRevealConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_reveal_configuration_response.GetRevealConfigurationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_reveal_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_reveal_configuration.async_get_reveal_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_reveal_configuration_request.GetRevealConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_sensitive_data_occurrences(
        self,
        finding_id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.get_sensitive_data_occurrences_response.GetSensitiveDataOccurrencesResponse":
        """<p>Retrieves occurrences of sensitive data reported by a finding.</p>

        Args:
            finding_id: <p>The unique identifier for the finding.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_sensitive_data_occurrences_request.GetSensitiveDataOccurrencesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_sensitive_data_occurrences_response.GetSensitiveDataOccurrencesResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_sensitive_data_occurrences

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_sensitive_data_occurrences.async_get_sensitive_data_occurrences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_sensitive_data_occurrences_request.GetSensitiveDataOccurrencesRequest = {}  # type: ignore[typeddict-item]
        input_["finding_id"] = finding_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_sensitive_data_occurrences_availability(
        self,
        finding_id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.get_sensitive_data_occurrences_availability_response.GetSensitiveDataOccurrencesAvailabilityResponse":
        """<p>Checks whether occurrences of sensitive data can be retrieved for a finding.</p>

        Args:
            finding_id: <p>The unique identifier for the finding.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_sensitive_data_occurrences_availability_request.GetSensitiveDataOccurrencesAvailabilityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_sensitive_data_occurrences_availability_response.GetSensitiveDataOccurrencesAvailabilityResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_sensitive_data_occurrences_availability

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_sensitive_data_occurrences_availability.async_get_sensitive_data_occurrences_availability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_sensitive_data_occurrences_availability_request.GetSensitiveDataOccurrencesAvailabilityRequest = {}  # type: ignore[typeddict-item]
        input_["finding_id"] = finding_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_sensitivity_inspection_template(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.get_sensitivity_inspection_template_response.GetSensitivityInspectionTemplateResponse":
        """<p>Retrieves the settings for the sensitivity inspection template for an account.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_sensitivity_inspection_template_request.GetSensitivityInspectionTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_sensitivity_inspection_template_response.GetSensitivityInspectionTemplateResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_sensitivity_inspection_template

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_sensitivity_inspection_template.async_get_sensitivity_inspection_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_sensitivity_inspection_template_request.GetSensitivityInspectionTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_usage_statistics(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        filter_by: Optional[
            "aws_sdk_macie2.types.__list_of_usage_statistics_filter.__listOfUsageStatisticsFilter"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        sort_by: Optional[
            "aws_sdk_macie2.types.usage_statistics_sort_by.UsageStatisticsSortBy"
        ] = None,
        time_range: Optional["aws_sdk_macie2.types.time_range.TimeRange"] = None,
    ) -> (
        "aws_sdk_macie2.types.get_usage_statistics_response.GetUsageStatisticsResponse"
    ):
        """<p>Retrieves (queries) quotas and aggregated usage data for one or more accounts.</p>

        Args:
            filter_by: <p>An array of objects, one for each condition to use to filter the query results. If you specify more than one condition, Amazon Macie uses an AND operator to join the conditions.</p>
            max_results: <p>The maximum number of items to include in each page of the response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
            sort_by: <p>The criteria to use to sort the query results.</p>
            time_range: <p>The inclusive time period to query usage data for. Valid values are: MONTH_TO_DATE, for the current calendar month to date; and, PAST_30_DAYS, for the preceding 30 days. If you don't specify a value, Amazon Macie provides usage data for the preceding 30 days.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_usage_statistics_request.GetUsageStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_usage_statistics_response.GetUsageStatisticsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_usage_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_usage_statistics.async_get_usage_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_usage_statistics_request.GetUsageStatisticsRequest = {}  # type: ignore[typeddict-item]
        if filter_by is not None:
            input_["filter_by"] = filter_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if time_range is not None:
            input_["time_range"] = time_range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_get_usage_statistics(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        filter_by: Optional[
            "aws_sdk_macie2.types.__list_of_usage_statistics_filter.__listOfUsageStatisticsFilter"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        sort_by: Optional[
            "aws_sdk_macie2.types.usage_statistics_sort_by.UsageStatisticsSortBy"
        ] = None,
        time_range: Optional["aws_sdk_macie2.types.time_range.TimeRange"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.usage_record.UsageRecord]":
        _token = next_token
        while True:
            _response = await self.get_usage_statistics(
                config_overrides=config_overrides,
                filter_by=filter_by,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                time_range=time_range,
            )
            _page = _resolve_path(_response, ("records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_usage_totals(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        time_range: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.get_usage_totals_response.GetUsageTotalsResponse":
        """<p>Retrieves (queries) aggregated usage data for an account.</p>

        Args:
            time_range: <p>The inclusive time period to retrieve the data for. Valid values are: MONTH_TO_DATE, for the current calendar month to date; and, PAST_30_DAYS, for the preceding 30 days. If you don't specify a value for this parameter, Amazon Macie provides aggregated usage data for the preceding 30 days.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.get_usage_totals_request.GetUsageTotalsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.get_usage_totals_response.GetUsageTotalsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.get_usage_totals

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.get_usage_totals.async_get_usage_totals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.get_usage_totals_request.GetUsageTotalsRequest = {}  # type: ignore[typeddict-item]
        if time_range is not None:
            input_["time_range"] = time_range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_allow_lists(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_allow_lists_response.ListAllowListsResponse":
        """<p>Retrieves a subset of information about all the allow lists for an account.</p>

        Args:
            max_results: <p>The maximum number of items to include in each page of a paginated response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_allow_lists_request.ListAllowListsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_allow_lists_response.ListAllowListsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_allow_lists

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_allow_lists.async_list_allow_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_allow_lists_request.ListAllowListsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_allow_lists(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.allow_list_summary.AllowListSummary]":
        _token = next_token
        while True:
            _response = await self.list_allow_lists(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("allow_lists",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_automated_discovery_accounts(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        account_ids: Optional[
            "aws_sdk_macie2.types.__list_of__string.__listOf__string"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_automated_discovery_accounts_response.ListAutomatedDiscoveryAccountsResponse":
        """<p>Retrieves the status of automated sensitive data discovery for one or more accounts.</p>

        Args:
            account_ids: <p>The Amazon Web Services account ID for each account, for as many as 50 accounts. To retrieve the status for multiple accounts, append the accountIds parameter and argument for each account, separated by an ampersand (&amp;). To retrieve the status for all the accounts in an organization, omit this parameter.</p>
            max_results: <p>The maximum number of items to include in each page of a paginated response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_automated_discovery_accounts_request.ListAutomatedDiscoveryAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_automated_discovery_accounts_response.ListAutomatedDiscoveryAccountsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_automated_discovery_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_automated_discovery_accounts.async_list_automated_discovery_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_automated_discovery_accounts_request.ListAutomatedDiscoveryAccountsRequest = {}  # type: ignore[typeddict-item]
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_automated_discovery_accounts(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        account_ids: Optional[
            "aws_sdk_macie2.types.__list_of__string.__listOf__string"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.automated_discovery_account.AutomatedDiscoveryAccount]":
        _token = next_token
        while True:
            _response = await self.list_automated_discovery_accounts(
                config_overrides=config_overrides,
                account_ids=account_ids,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_classification_jobs(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_macie2.types.list_jobs_filter_criteria.ListJobsFilterCriteria"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        sort_criteria: Optional[
            "aws_sdk_macie2.types.list_jobs_sort_criteria.ListJobsSortCriteria"
        ] = None,
    ) -> "aws_sdk_macie2.types.list_classification_jobs_response.ListClassificationJobsResponse":
        """<p>Retrieves a subset of information about one or more classification jobs.</p>

        Args:
            filter_criteria: <p>The criteria to use to filter the results.</p>
            max_results: <p>The maximum number of items to include in each page of the response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
            sort_criteria: <p>The criteria to use to sort the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_classification_jobs_request.ListClassificationJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_classification_jobs_response.ListClassificationJobsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_classification_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_classification_jobs.async_list_classification_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_classification_jobs_request.ListClassificationJobsRequest = {}  # type: ignore[typeddict-item]
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_classification_jobs(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_macie2.types.list_jobs_filter_criteria.ListJobsFilterCriteria"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        sort_criteria: Optional[
            "aws_sdk_macie2.types.list_jobs_sort_criteria.ListJobsSortCriteria"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.job_summary.JobSummary]":
        _token = next_token
        while True:
            _response = await self.list_classification_jobs(
                config_overrides=config_overrides,
                filter_criteria=filter_criteria,
                max_results=max_results,
                next_token=_token,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_classification_scopes(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        name: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_classification_scopes_response.ListClassificationScopesResponse":
        """<p>Retrieves a subset of information about the classification scope for an account.</p>

        Args:
            name: <p>The name of the classification scope to retrieve the unique identifier for.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_classification_scopes_request.ListClassificationScopesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_classification_scopes_response.ListClassificationScopesResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_classification_scopes

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_classification_scopes.async_list_classification_scopes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_classification_scopes_request.ListClassificationScopesRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_classification_scopes(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        name: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.classification_scope_summary.ClassificationScopeSummary]":
        _token = next_token
        while True:
            _response = await self.list_classification_scopes(
                config_overrides=config_overrides,
                name=name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("classification_scopes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_custom_data_identifiers(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_custom_data_identifiers_response.ListCustomDataIdentifiersResponse":
        """<p>Retrieves a subset of information about the custom data identifiers for an account.</p>

        Args:
            max_results: <p>The maximum number of items to include in each page of the response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_custom_data_identifiers_request.ListCustomDataIdentifiersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_custom_data_identifiers_response.ListCustomDataIdentifiersResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_custom_data_identifiers

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_custom_data_identifiers.async_list_custom_data_identifiers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_custom_data_identifiers_request.ListCustomDataIdentifiersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_custom_data_identifiers(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.custom_data_identifier_summary.CustomDataIdentifierSummary]":
        _token = next_token
        while True:
            _response = await self.list_custom_data_identifiers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_findings(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        finding_criteria: Optional[
            "aws_sdk_macie2.types.finding_criteria.FindingCriteria"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        sort_criteria: Optional[
            "aws_sdk_macie2.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "aws_sdk_macie2.types.list_findings_response.ListFindingsResponse":
        """<p>Retrieves a subset of information about one or more findings.</p>

        Args:
            finding_criteria: <p>The criteria to use to filter the results.</p>
            max_results: <p>The maximum number of items to include in each page of the response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
            sort_criteria: <p>The criteria to use to sort the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_findings_request.ListFindingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_findings_response.ListFindingsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_findings

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_findings.async_list_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_findings_request.ListFindingsRequest = {}  # type: ignore[typeddict-item]
        if finding_criteria is not None:
            input_["finding_criteria"] = finding_criteria
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_findings(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        finding_criteria: Optional[
            "aws_sdk_macie2.types.finding_criteria.FindingCriteria"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        sort_criteria: Optional[
            "aws_sdk_macie2.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.__string.__string]":
        _token = next_token
        while True:
            _response = await self.list_findings(
                config_overrides=config_overrides,
                finding_criteria=finding_criteria,
                max_results=max_results,
                next_token=_token,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("finding_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_findings_filters(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_findings_filters_response.ListFindingsFiltersResponse":
        """<p>Retrieves a subset of information about all the findings filters for an account.</p>

        Args:
            max_results: <p>The maximum number of items to include in each page of a paginated response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_findings_filters_request.ListFindingsFiltersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_findings_filters_response.ListFindingsFiltersResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_findings_filters

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_findings_filters.async_list_findings_filters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_findings_filters_request.ListFindingsFiltersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_findings_filters(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.findings_filter_list_item.FindingsFilterListItem]":
        _token = next_token
        while True:
            _response = await self.list_findings_filters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("findings_filter_list_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_invitations(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_invitations_response.ListInvitationsResponse":
        """<p>Retrieves information about Amazon Macie membership invitations that were received by an account.</p>

        Args:
            max_results: <p>The maximum number of items to include in each page of a paginated response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_invitations_request.ListInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_invitations_response.ListInvitationsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_invitations

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_invitations.async_list_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_invitations_request.ListInvitationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_invitations(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.invitation.Invitation]":
        _token = next_token
        while True:
            _response = await self.list_invitations(
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

    async def list_managed_data_identifiers(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_managed_data_identifiers_response.ListManagedDataIdentifiersResponse":
        """<p>Retrieves information about all the managed data identifiers that Amazon Macie currently provides.</p>

        Args:
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_managed_data_identifiers_request.ListManagedDataIdentifiersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_managed_data_identifiers_response.ListManagedDataIdentifiersResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_managed_data_identifiers

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_managed_data_identifiers.async_list_managed_data_identifiers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_managed_data_identifiers_request.ListManagedDataIdentifiersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_managed_data_identifiers(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.managed_data_identifier_summary.ManagedDataIdentifierSummary]":
        _token = next_token
        while True:
            _response = await self.list_managed_data_identifiers(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_members(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        only_associated: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_members_response.ListMembersResponse":
        """<p>Retrieves information about the accounts that are associated with an Amazon Macie administrator account.</p>

        Args:
            max_results: <p>The maximum number of items to include in each page of a paginated response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
            only_associated: <p>Specifies which accounts to include in the response, based on the status of an account's relationship with the administrator account. By default, the response includes only current member accounts. To include all accounts, set this value to false.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_members_request.ListMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_members_response.ListMembersResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_members

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_members.async_list_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_members_request.ListMembersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if only_associated is not None:
            input_["only_associated"] = only_associated

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_members(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        only_associated: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.member.Member]":
        _token = next_token
        while True:
            _response = await self.list_members(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                only_associated=only_associated,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse":
        """<p>Retrieves information about the delegated Amazon Macie administrator account for an organization in Organizations.</p>

        Args:
            max_results: <p>The maximum number of items to include in each page of a paginated response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_organization_admin_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_organization_admin_accounts.async_list_organization_admin_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.admin_account.AdminAccount]":
        _token = next_token
        while True:
            _response = await self.list_organization_admin_accounts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("admin_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_profile_artifacts(
        self,
        resource_arn: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_resource_profile_artifacts_response.ListResourceProfileArtifactsResponse":
        """<p>Retrieves information about objects that Amazon Macie selected from an S3 bucket for automated sensitive data discovery.</p>

        Args:
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the S3 bucket that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_resource_profile_artifacts_request.ListResourceProfileArtifactsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_resource_profile_artifacts_response.ListResourceProfileArtifactsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_resource_profile_artifacts

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_resource_profile_artifacts.async_list_resource_profile_artifacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_resource_profile_artifacts_request.ListResourceProfileArtifactsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_resource_profile_artifacts(
        self,
        resource_arn: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.resource_profile_artifact.ResourceProfileArtifact]":
        _token = next_token
        while True:
            _response = await self.list_resource_profile_artifacts(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("artifacts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_profile_detections(
        self,
        resource_arn: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_resource_profile_detections_response.ListResourceProfileDetectionsResponse":
        """<p>Retrieves information about the types and amount of sensitive data that Amazon Macie found in an S3 bucket.</p>

        Args:
            max_results: <p>The maximum number of items to include in each page of a paginated response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the S3 bucket that the request applies to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_resource_profile_detections_request.ListResourceProfileDetectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_resource_profile_detections_response.ListResourceProfileDetectionsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_resource_profile_detections

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_resource_profile_detections.async_list_resource_profile_detections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_resource_profile_detections_request.ListResourceProfileDetectionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_resource_profile_detections(
        self,
        resource_arn: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.detection.Detection]":
        _token = next_token
        while True:
            _response = await self.list_resource_profile_detections(
                resource_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("detections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_sensitivity_inspection_templates(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "aws_sdk_macie2.types.list_sensitivity_inspection_templates_response.ListSensitivityInspectionTemplatesResponse":
        """<p>Retrieves a subset of information about the sensitivity inspection template for an account.</p>

        Args:
            max_results: <p>The maximum number of items to include in each page of a paginated response.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_sensitivity_inspection_templates_request.ListSensitivityInspectionTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_sensitivity_inspection_templates_response.ListSensitivityInspectionTemplatesResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_sensitivity_inspection_templates

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_sensitivity_inspection_templates.async_list_sensitivity_inspection_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_sensitivity_inspection_templates_request.ListSensitivityInspectionTemplatesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_sensitivity_inspection_templates(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        max_results: Optional["aws_sdk_macie2.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.sensitivity_inspection_templates_entry.SensitivityInspectionTemplatesEntry]":
        _token = next_token
        while True:
            _response = await self.list_sensitivity_inspection_templates(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sensitivity_inspection_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the tags (keys and values) that are associated with an Amazon Macie resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_classification_export_configuration(
        self,
        configuration: "aws_sdk_macie2.types.classification_export_configuration.ClassificationExportConfiguration",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.put_classification_export_configuration_response.PutClassificationExportConfigurationResponse":
        """<p>Adds or updates the configuration settings for storing data classification results.</p>

        Args:
            configuration: <p>The location to store data classification results in, and the encryption settings to use when storing results in that location.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.put_classification_export_configuration_request.PutClassificationExportConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.put_classification_export_configuration_response.PutClassificationExportConfigurationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.put_classification_export_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.put_classification_export_configuration.async_put_classification_export_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.put_classification_export_configuration_request.PutClassificationExportConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_findings_publication_configuration(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        client_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        security_hub_configuration: Optional[
            "aws_sdk_macie2.types.security_hub_configuration.SecurityHubConfiguration"
        ] = None,
    ) -> "aws_sdk_macie2.types.put_findings_publication_configuration_response.PutFindingsPublicationConfigurationResponse":
        """<p>Updates the configuration settings for publishing findings to Security Hub.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
            security_hub_configuration: <p>The configuration settings that determine which findings to publish to Security Hub.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.put_findings_publication_configuration_request.PutFindingsPublicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.put_findings_publication_configuration_response.PutFindingsPublicationConfigurationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.put_findings_publication_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.put_findings_publication_configuration.async_put_findings_publication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.put_findings_publication_configuration_request.PutFindingsPublicationConfigurationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if security_hub_configuration is not None:
            input_["security_hub_configuration"] = security_hub_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def search_resources(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        bucket_criteria: Optional[
            "aws_sdk_macie2.types.search_resources_bucket_criteria.SearchResourcesBucketCriteria"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        sort_criteria: Optional[
            "aws_sdk_macie2.types.search_resources_sort_criteria.SearchResourcesSortCriteria"
        ] = None,
    ) -> "aws_sdk_macie2.types.search_resources_response.SearchResourcesResponse":
        """<p>Retrieves (queries) statistical data and other information about Amazon Web Services resources that Amazon Macie monitors and analyzes for an account.</p>

        Args:
            bucket_criteria: <p>The filter conditions that determine which S3 buckets to include or exclude from the query results.</p>
            max_results: <p>The maximum number of items to include in each page of the response. The default value is 50.</p>
            next_token: <p>The nextToken string that specifies which page of results to return in a paginated response.</p>
            sort_criteria: <p>The criteria to use to sort the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.search_resources_request.SearchResourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.search_resources_response.SearchResourcesResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.search_resources

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.search_resources.async_search_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.search_resources_request.SearchResourcesRequest = {}  # type: ignore[typeddict-item]
        if bucket_criteria is not None:
            input_["bucket_criteria"] = bucket_criteria
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_search_resources(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        bucket_criteria: Optional[
            "aws_sdk_macie2.types.search_resources_bucket_criteria.SearchResourcesBucketCriteria"
        ] = None,
        max_results: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
        next_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        sort_criteria: Optional[
            "aws_sdk_macie2.types.search_resources_sort_criteria.SearchResourcesSortCriteria"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_macie2.types.matching_resource.MatchingResource]":
        _token = next_token
        while True:
            _response = await self.search_resources(
                config_overrides=config_overrides,
                bucket_criteria=bucket_criteria,
                max_results=max_results,
                next_token=_token,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("matching_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_macie2.types.__string.__string",
        tags: "aws_sdk_macie2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates one or more tags (keys and values) that are associated with an Amazon Macie resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>A map of key-value pairs that specifies the tags to associate with the resource.</p> <p>A resource can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_custom_data_identifier(
        self,
        regex: "aws_sdk_macie2.types.__string.__string",
        sample_text: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        ignore_words: Optional[
            "aws_sdk_macie2.types.__list_of__string.__listOf__string"
        ] = None,
        keywords: Optional[
            "aws_sdk_macie2.types.__list_of__string.__listOf__string"
        ] = None,
        maximum_match_distance: Optional[
            "aws_sdk_macie2.types.__integer.__integer"
        ] = None,
    ) -> "aws_sdk_macie2.types.test_custom_data_identifier_response.TestCustomDataIdentifierResponse":
        """<p>Tests criteria for a custom data identifier.</p>

        Args:
            ignore_words: <p>An array that lists specific character sequences (<i>ignore words</i>) to exclude from the results. If the text matched by the regular expression contains any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive.</p>
            keywords: <p>An array that lists specific character sequences (<i>keywords</i>), one of which must precede and be within proximity (maximumMatchDistance) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren't case sensitive.</p>
            maximum_match_distance: <p>The maximum number of characters that can exist between the end of at least one complete character sequence specified by the keywords array and the end of the text that matches the regex pattern. If a complete keyword precedes all the text that matches the pattern and the keyword is within the specified distance, Amazon Macie includes the result. The distance can be 1-300 characters. The default value is 50.</p>
            regex: <p>The regular expression (<i>regex</i>) that defines the pattern to match. The expression can contain as many as 512 characters.</p>
            sample_text: <p>The sample text to inspect by using the custom data identifier. The text can contain as many as 1,000 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.test_custom_data_identifier_request.TestCustomDataIdentifierRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.test_custom_data_identifier_response.TestCustomDataIdentifierResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.test_custom_data_identifier

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.test_custom_data_identifier.async_test_custom_data_identifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.test_custom_data_identifier_request.TestCustomDataIdentifierRequest = {}  # type: ignore[typeddict-item]
        if ignore_words is not None:
            input_["ignore_words"] = ignore_words
        if keywords is not None:
            input_["keywords"] = keywords
        if maximum_match_distance is not None:
            input_["maximum_match_distance"] = maximum_match_distance
        input_["regex"] = regex
        input_["sample_text"] = sample_text

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_macie2.types.__string.__string",
        tag_keys: "aws_sdk_macie2.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags (keys and values) from an Amazon Macie resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>One or more tags (keys) to remove from the resource. In an HTTP request to remove multiple tags, append the tagKeys parameter and argument for each tag to remove, separated by an ampersand (&amp;).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_allow_list(
        self,
        criteria: "aws_sdk_macie2.types.allow_list_criteria.AllowListCriteria",
        id: "aws_sdk_macie2.types.__string.__string",
        name: "aws_sdk_macie2.types.__string_min1_max128_pattern.__stringMin1Max128Pattern",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        description: Optional[
            "aws_sdk_macie2.types.__string_min1_max512_pattern_ss.__stringMin1Max512PatternSS"
        ] = None,
    ) -> "aws_sdk_macie2.types.update_allow_list_response.UpdateAllowListResponse":
        """<p>Updates the settings for an allow list.</p>

        Args:
            criteria: <p>The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an S3 object that lists specific text to ignore (s3WordsList), or a regular expression that defines a text pattern to ignore (regex).</p> <p>You can change a list's underlying criteria, such as the name of the S3 object or the regular expression to use. However, you can't change the type from s3WordsList to regex or the other way around.</p>
            description: <p>A custom description of the allow list. The description can contain as many as 512 characters.</p>
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
            name: <p>A custom name for the allow list. The name can contain as many as 128 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_allow_list_request.UpdateAllowListRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_allow_list_response.UpdateAllowListResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_allow_list

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_allow_list.async_update_allow_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_allow_list_request.UpdateAllowListRequest = {}  # type: ignore[typeddict-item]
        input_["criteria"] = criteria
        if description is not None:
            input_["description"] = description
        input_["id"] = id
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_automated_discovery_configuration(
        self,
        status: "aws_sdk_macie2.types.automated_discovery_status.AutomatedDiscoveryStatus",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        auto_enable_organization_members: Optional[
            "aws_sdk_macie2.types.auto_enable_mode.AutoEnableMode"
        ] = None,
    ) -> "aws_sdk_macie2.types.update_automated_discovery_configuration_response.UpdateAutomatedDiscoveryConfigurationResponse":
        """<p>Changes the configuration settings and status of automated sensitive data discovery for an organization or standalone account.</p>

        Args:
            auto_enable_organization_members: <p>Specifies whether to automatically enable automated sensitive data discovery for accounts in the organization. Valid values are: ALL (default), enable it for all existing accounts and new member accounts; NEW, enable it only for new member accounts; and, NONE, don't enable it for any accounts.</p> <p>If you specify NEW or NONE, automated sensitive data discovery continues to be enabled for any existing accounts that it's currently enabled for. To enable or disable it for individual member accounts, specify NEW or NONE, and then enable or disable it for each account by using the BatchUpdateAutomatedDiscoveryAccounts operation.</p>
            status: <p>The new status of automated sensitive data discovery for the organization or account. Valid values are: ENABLED, start or resume all automated sensitive data discovery activities; and, DISABLED, stop performing all automated sensitive data discovery activities.</p> <p>If you specify DISABLED for an administrator account, you also disable automated sensitive data discovery for all member accounts in the organization.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_automated_discovery_configuration_request.UpdateAutomatedDiscoveryConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_automated_discovery_configuration_response.UpdateAutomatedDiscoveryConfigurationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_automated_discovery_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_automated_discovery_configuration.async_update_automated_discovery_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_automated_discovery_configuration_request.UpdateAutomatedDiscoveryConfigurationRequest = {}  # type: ignore[typeddict-item]
        if auto_enable_organization_members is not None:
            input_["auto_enable_organization_members"] = (
                auto_enable_organization_members
            )
        input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_classification_job(
        self,
        job_id: "aws_sdk_macie2.types.__string.__string",
        job_status: "aws_sdk_macie2.types.job_status.JobStatus",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.update_classification_job_response.UpdateClassificationJobResponse":
        """<p>Changes the status of a classification job.</p>

        Args:
            job_id: <p>The unique identifier for the classification job.</p>
            job_status: <p>The new status for the job. Valid values are:</p> <ul><li><p>CANCELLED - Stops the job permanently and cancels it. This value is valid only if the job's current status is IDLE, PAUSED, RUNNING, or USER_PAUSED.</p> <p>If you specify this value and the job's current status is RUNNING, Amazon Macie immediately begins to stop all processing tasks for the job. You can't resume or restart a job after you cancel it.</p></li> <li><p>RUNNING - Resumes the job. This value is valid only if the job's current status is USER_PAUSED.</p> <p>If you paused the job while it was actively running and you specify this value less than 30 days after you paused the job, Macie immediately resumes processing from the point where you paused the job. Otherwise, Macie resumes the job according to the schedule and other settings for the job.</p></li> <li><p>USER_PAUSED - Pauses the job temporarily. This value is valid only if the job's current status is IDLE, PAUSED, or RUNNING. If you specify this value and the job's current status is RUNNING, Macie immediately begins to pause all processing tasks for the job.</p> <p>If you pause a one-time job and you don't resume it within 30 days, the job expires and Macie cancels the job. If you pause a recurring job when its status is RUNNING and you don't resume it within 30 days, the job run expires and Macie cancels the run. To check the expiration date, refer to the UserPausedDetails.jobExpiresAt property.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_classification_job_request.UpdateClassificationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_classification_job_response.UpdateClassificationJobResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_classification_job

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_classification_job.async_update_classification_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_classification_job_request.UpdateClassificationJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
        input_["job_status"] = job_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_classification_scope(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        s3: Optional[
            "aws_sdk_macie2.types.s3_classification_scope_update.S3ClassificationScopeUpdate"
        ] = None,
    ) -> "aws_sdk_macie2.types.update_classification_scope_response.UpdateClassificationScopeResponse":
        """<p>Updates the classification scope settings for an account.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
            s3: <p>The S3 buckets to add or remove from the exclusion list defined by the classification scope.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_classification_scope_request.UpdateClassificationScopeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_classification_scope_response.UpdateClassificationScopeResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_classification_scope

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_classification_scope.async_update_classification_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_classification_scope_request.UpdateClassificationScopeRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if s3 is not None:
            input_["s3"] = s3

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_findings_filter(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        action: Optional[
            "aws_sdk_macie2.types.findings_filter_action.FindingsFilterAction"
        ] = None,
        client_token: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        description: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        finding_criteria: Optional[
            "aws_sdk_macie2.types.finding_criteria.FindingCriteria"
        ] = None,
        name: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        position: Optional["aws_sdk_macie2.types.__integer.__integer"] = None,
    ) -> "aws_sdk_macie2.types.update_findings_filter_response.UpdateFindingsFilterResponse":
        """<p>Updates the criteria and other settings for a findings filter.</p>

        Args:
            action: <p>The action to perform on findings that match the filter criteria (findingCriteria). Valid values are: ARCHIVE, suppress (automatically archive) the findings; and, NOOP, don't perform any action on the findings.</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>
            description: <p>A custom description of the filter. The description can contain as many as 512 characters.</p> <p>We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users of your account might be able to see this description, depending on the actions that they're allowed to perform in Amazon Macie.</p>
            finding_criteria: <p>The criteria to use to filter findings.</p>
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
            name: <p>A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters.</p> <p>We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users of your account might be able to see this name, depending on the actions that they're allowed to perform in Amazon Macie.</p>
            position: <p>The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_findings_filter_request.UpdateFindingsFilterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_findings_filter_response.UpdateFindingsFilterResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_findings_filter

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_findings_filter.async_update_findings_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_findings_filter_request.UpdateFindingsFilterRequest = {}  # type: ignore[typeddict-item]
        if action is not None:
            input_["action"] = action
        if client_token is not None:
            input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if finding_criteria is not None:
            input_["finding_criteria"] = finding_criteria
        input_["id"] = id
        if name is not None:
            input_["name"] = name
        if position is not None:
            input_["position"] = position

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_macie_session(
        self,
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        finding_publishing_frequency: Optional[
            "aws_sdk_macie2.types.finding_publishing_frequency.FindingPublishingFrequency"
        ] = None,
        status: Optional["aws_sdk_macie2.types.macie_status.MacieStatus"] = None,
    ) -> (
        "aws_sdk_macie2.types.update_macie_session_response.UpdateMacieSessionResponse"
    ):
        """<p>Suspends or re-enables Amazon Macie, or updates the configuration settings for a Macie account.</p>

        Args:
            finding_publishing_frequency: <p>Specifies how often to publish updates to policy findings for the account. This includes publishing updates to Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events).</p>
            status: <p>Specifies a new status for the account. Valid values are: ENABLED, resume all Amazon Macie activities for the account; and, PAUSED, suspend all Macie activities for the account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_macie_session_request.UpdateMacieSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_macie_session_response.UpdateMacieSessionResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_macie_session

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_macie_session.async_update_macie_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_macie_session_request.UpdateMacieSessionRequest = {}  # type: ignore[typeddict-item]
        if finding_publishing_frequency is not None:
            input_["finding_publishing_frequency"] = finding_publishing_frequency
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_member_session(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        status: "aws_sdk_macie2.types.macie_status.MacieStatus",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.update_member_session_response.UpdateMemberSessionResponse":
        """<p>Enables an Amazon Macie administrator to suspend or re-enable Macie for a member account.</p>

        Args:
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
            status: <p>Specifies the new status for the account. Valid values are: ENABLED, resume all Amazon Macie activities for the account; and, PAUSED, suspend all Macie activities for the account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_member_session_request.UpdateMemberSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_member_session_response.UpdateMemberSessionResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_member_session

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_member_session.async_update_member_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_member_session_request.UpdateMemberSessionRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_organization_configuration(
        self,
        auto_enable: "aws_sdk_macie2.types.__boolean.__boolean",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
    ) -> "aws_sdk_macie2.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse":
        """<p>Updates the Amazon Macie configuration settings for an organization in Organizations.</p>

        Args:
            auto_enable: <p>Specifies whether to enable Amazon Macie automatically for accounts that are added to the organization in Organizations.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_organization_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_organization_configuration.async_update_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["auto_enable"] = auto_enable

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_resource_profile(
        self,
        resource_arn: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        sensitivity_score_override: Optional[
            "aws_sdk_macie2.types.__integer.__integer"
        ] = None,
    ) -> "aws_sdk_macie2.types.update_resource_profile_response.UpdateResourceProfileResponse":
        """<p>Updates the sensitivity score for an S3 bucket.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the S3 bucket that the request applies to.</p>
            sensitivity_score_override: <p>The new sensitivity score for the bucket. Valid values are: 100, assign the maximum score and apply the <i>Sensitive</i> label to the bucket; and, null (empty), assign a score that Amazon Macie calculates automatically after you submit the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_resource_profile_request.UpdateResourceProfileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_resource_profile_response.UpdateResourceProfileResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_resource_profile

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_resource_profile.async_update_resource_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_resource_profile_request.UpdateResourceProfileRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if sensitivity_score_override is not None:
            input_["sensitivity_score_override"] = sensitivity_score_override

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_resource_profile_detections(
        self,
        resource_arn: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        suppress_data_identifiers: Optional[
            "aws_sdk_macie2.types.__list_of_suppress_data_identifier.__listOfSuppressDataIdentifier"
        ] = None,
    ) -> "aws_sdk_macie2.types.update_resource_profile_detections_response.UpdateResourceProfileDetectionsResponse":
        """<p>Updates the sensitivity scoring settings for an S3 bucket.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the S3 bucket that the request applies to.</p>
            suppress_data_identifiers: <p>An array of objects, one for each custom data identifier or managed data identifier that detected a type of sensitive data to exclude from the bucket's score. To include all sensitive data types in the score, don't specify any values for this array.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_resource_profile_detections_request.UpdateResourceProfileDetectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_resource_profile_detections_response.UpdateResourceProfileDetectionsResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_resource_profile_detections

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_resource_profile_detections.async_update_resource_profile_detections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_resource_profile_detections_request.UpdateResourceProfileDetectionsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if suppress_data_identifiers is not None:
            input_["suppress_data_identifiers"] = suppress_data_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_reveal_configuration(
        self,
        configuration: "aws_sdk_macie2.types.reveal_configuration.RevealConfiguration",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        retrieval_configuration: Optional[
            "aws_sdk_macie2.types.update_retrieval_configuration.UpdateRetrievalConfiguration"
        ] = None,
    ) -> "aws_sdk_macie2.types.update_reveal_configuration_response.UpdateRevealConfigurationResponse":
        """<p>Updates the status and configuration settings for retrieving occurrences of sensitive data reported by findings.</p>

        Args:
            configuration: <p>The KMS key to use to encrypt the sensitive data, and the status of the configuration for the Amazon Macie account.</p>
            retrieval_configuration: <p>The access method and settings to use when retrieving the sensitive data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_reveal_configuration_request.UpdateRevealConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_reveal_configuration_response.UpdateRevealConfigurationResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_reveal_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_reveal_configuration.async_update_reveal_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_reveal_configuration_request.UpdateRevealConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["configuration"] = configuration
        if retrieval_configuration is not None:
            input_["retrieval_configuration"] = retrieval_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_sensitivity_inspection_template(
        self,
        id: "aws_sdk_macie2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMacie2ClientConfig] = None,
        description: Optional["aws_sdk_macie2.types.__string.__string"] = None,
        excludes: Optional[
            "aws_sdk_macie2.types.sensitivity_inspection_template_excludes.SensitivityInspectionTemplateExcludes"
        ] = None,
        includes: Optional[
            "aws_sdk_macie2.types.sensitivity_inspection_template_includes.SensitivityInspectionTemplateIncludes"
        ] = None,
    ) -> "aws_sdk_macie2.types.update_sensitivity_inspection_template_response.UpdateSensitivityInspectionTemplateResponse":
        """<p>Updates the settings for the sensitivity inspection template for an account.</p>

        Args:
            description: <p>A custom description of the template. The description can contain as many as 200 characters.</p>
            excludes: <p>The managed data identifiers to explicitly exclude (not use) when performing automated sensitive data discovery.</p> <p>To exclude an allow list or custom data identifier that's currently included by the template, update the values for the SensitivityInspectionTemplateIncludes.allowListIds and SensitivityInspectionTemplateIncludes.customDataIdentifierIds properties, respectively.</p>
            id: <p>The unique identifier for the Amazon Macie resource that the request applies to.</p>
            includes: <p>The allow lists, custom data identifiers, and managed data identifiers to explicitly include (use) when performing automated sensitive data discovery.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_macie2.types.update_sensitivity_inspection_template_request.UpdateSensitivityInspectionTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_macie2.types.update_sensitivity_inspection_template_response.UpdateSensitivityInspectionTemplateResponse"
        ]:
            import aws_sdk_macie2._operations.macie2.update_sensitivity_inspection_template

            (
                output,
                http_response,
            ) = await aws_sdk_macie2._operations.macie2.update_sensitivity_inspection_template.async_update_sensitivity_inspection_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_macie2.types.update_sensitivity_inspection_template_request.UpdateSensitivityInspectionTemplateRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        if excludes is not None:
            input_["excludes"] = excludes
        input_["id"] = id
        if includes is not None:
            input_["includes"] = includes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
