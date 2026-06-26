"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WellArchitectedApiServiceLambda``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_wellarchitected._auth._signers
import aws_sdk_wellarchitected._auth._sigv4
from aws_sdk_wellarchitected._auth._identity import Credentials
from aws_sdk_wellarchitected._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_wellarchitected._auth._zapros_handler import AuthMiddleware
from aws_sdk_wellarchitected._services._aws_config import aaws_config
from aws_sdk_wellarchitected._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.account_jira_configuration_input
    import aws_sdk_wellarchitected.types.answer_reason
    import aws_sdk_wellarchitected.types.associate_lenses_input
    import aws_sdk_wellarchitected.types.associate_profiles_input
    import aws_sdk_wellarchitected.types.choice_id
    import aws_sdk_wellarchitected.types.choice_updates
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.create_lens_share_input
    import aws_sdk_wellarchitected.types.create_lens_share_output
    import aws_sdk_wellarchitected.types.create_lens_version_input
    import aws_sdk_wellarchitected.types.create_lens_version_output
    import aws_sdk_wellarchitected.types.create_milestone_input
    import aws_sdk_wellarchitected.types.create_milestone_output
    import aws_sdk_wellarchitected.types.create_profile_input
    import aws_sdk_wellarchitected.types.create_profile_output
    import aws_sdk_wellarchitected.types.create_profile_share_input
    import aws_sdk_wellarchitected.types.create_profile_share_output
    import aws_sdk_wellarchitected.types.create_review_template_input
    import aws_sdk_wellarchitected.types.create_review_template_output
    import aws_sdk_wellarchitected.types.create_template_share_input
    import aws_sdk_wellarchitected.types.create_template_share_output
    import aws_sdk_wellarchitected.types.create_workload_input
    import aws_sdk_wellarchitected.types.create_workload_output
    import aws_sdk_wellarchitected.types.create_workload_share_input
    import aws_sdk_wellarchitected.types.create_workload_share_output
    import aws_sdk_wellarchitected.types.delete_lens_input
    import aws_sdk_wellarchitected.types.delete_lens_share_input
    import aws_sdk_wellarchitected.types.delete_profile_input
    import aws_sdk_wellarchitected.types.delete_profile_share_input
    import aws_sdk_wellarchitected.types.delete_review_template_input
    import aws_sdk_wellarchitected.types.delete_template_share_input
    import aws_sdk_wellarchitected.types.delete_workload_input
    import aws_sdk_wellarchitected.types.delete_workload_share_input
    import aws_sdk_wellarchitected.types.disassociate_lenses_input
    import aws_sdk_wellarchitected.types.disassociate_profiles_input
    import aws_sdk_wellarchitected.types.discovery_integration_status
    import aws_sdk_wellarchitected.types.export_lens_input
    import aws_sdk_wellarchitected.types.export_lens_output
    import aws_sdk_wellarchitected.types.get_answer_input
    import aws_sdk_wellarchitected.types.get_answer_output
    import aws_sdk_wellarchitected.types.get_consolidated_report_input
    import aws_sdk_wellarchitected.types.get_consolidated_report_max_results
    import aws_sdk_wellarchitected.types.get_consolidated_report_output
    import aws_sdk_wellarchitected.types.get_global_settings_output
    import aws_sdk_wellarchitected.types.get_lens_input
    import aws_sdk_wellarchitected.types.get_lens_output
    import aws_sdk_wellarchitected.types.get_lens_review_input
    import aws_sdk_wellarchitected.types.get_lens_review_output
    import aws_sdk_wellarchitected.types.get_lens_review_report_input
    import aws_sdk_wellarchitected.types.get_lens_review_report_output
    import aws_sdk_wellarchitected.types.get_lens_version_difference_input
    import aws_sdk_wellarchitected.types.get_lens_version_difference_output
    import aws_sdk_wellarchitected.types.get_milestone_input
    import aws_sdk_wellarchitected.types.get_milestone_output
    import aws_sdk_wellarchitected.types.get_profile_input
    import aws_sdk_wellarchitected.types.get_profile_output
    import aws_sdk_wellarchitected.types.get_profile_template_input
    import aws_sdk_wellarchitected.types.get_profile_template_output
    import aws_sdk_wellarchitected.types.get_review_template_answer_input
    import aws_sdk_wellarchitected.types.get_review_template_answer_output
    import aws_sdk_wellarchitected.types.get_review_template_input
    import aws_sdk_wellarchitected.types.get_review_template_lens_review_input
    import aws_sdk_wellarchitected.types.get_review_template_lens_review_output
    import aws_sdk_wellarchitected.types.get_review_template_output
    import aws_sdk_wellarchitected.types.get_workload_input
    import aws_sdk_wellarchitected.types.get_workload_output
    import aws_sdk_wellarchitected.types.import_lens_input
    import aws_sdk_wellarchitected.types.import_lens_output
    import aws_sdk_wellarchitected.types.include_shared_resources
    import aws_sdk_wellarchitected.types.integrating_service
    import aws_sdk_wellarchitected.types.is_applicable
    import aws_sdk_wellarchitected.types.is_major_version
    import aws_sdk_wellarchitected.types.is_review_owner_update_acknowledged
    import aws_sdk_wellarchitected.types.jira_selected_question_configuration
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_aliases
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.lens_json
    import aws_sdk_wellarchitected.types.lens_name
    import aws_sdk_wellarchitected.types.lens_name_prefix
    import aws_sdk_wellarchitected.types.lens_status_type
    import aws_sdk_wellarchitected.types.lens_type
    import aws_sdk_wellarchitected.types.lens_version
    import aws_sdk_wellarchitected.types.list_answers_input
    import aws_sdk_wellarchitected.types.list_answers_max_results
    import aws_sdk_wellarchitected.types.list_answers_output
    import aws_sdk_wellarchitected.types.list_check_details_input
    import aws_sdk_wellarchitected.types.list_check_details_output
    import aws_sdk_wellarchitected.types.list_check_summaries_input
    import aws_sdk_wellarchitected.types.list_check_summaries_output
    import aws_sdk_wellarchitected.types.list_lens_review_improvements_input
    import aws_sdk_wellarchitected.types.list_lens_review_improvements_max_results
    import aws_sdk_wellarchitected.types.list_lens_review_improvements_output
    import aws_sdk_wellarchitected.types.list_lens_reviews_input
    import aws_sdk_wellarchitected.types.list_lens_reviews_output
    import aws_sdk_wellarchitected.types.list_lens_shares_input
    import aws_sdk_wellarchitected.types.list_lens_shares_output
    import aws_sdk_wellarchitected.types.list_lenses_input
    import aws_sdk_wellarchitected.types.list_lenses_output
    import aws_sdk_wellarchitected.types.list_milestones_input
    import aws_sdk_wellarchitected.types.list_milestones_output
    import aws_sdk_wellarchitected.types.list_notifications_input
    import aws_sdk_wellarchitected.types.list_notifications_max_results
    import aws_sdk_wellarchitected.types.list_notifications_output
    import aws_sdk_wellarchitected.types.list_profile_notifications_input
    import aws_sdk_wellarchitected.types.list_profile_notifications_output
    import aws_sdk_wellarchitected.types.list_profile_shares_input
    import aws_sdk_wellarchitected.types.list_profile_shares_max_results
    import aws_sdk_wellarchitected.types.list_profile_shares_output
    import aws_sdk_wellarchitected.types.list_profiles_input
    import aws_sdk_wellarchitected.types.list_profiles_output
    import aws_sdk_wellarchitected.types.list_review_template_answers_input
    import aws_sdk_wellarchitected.types.list_review_template_answers_max_results
    import aws_sdk_wellarchitected.types.list_review_template_answers_output
    import aws_sdk_wellarchitected.types.list_review_templates_input
    import aws_sdk_wellarchitected.types.list_review_templates_output
    import aws_sdk_wellarchitected.types.list_share_invitations_input
    import aws_sdk_wellarchitected.types.list_share_invitations_max_results
    import aws_sdk_wellarchitected.types.list_share_invitations_output
    import aws_sdk_wellarchitected.types.list_tags_for_resource_input
    import aws_sdk_wellarchitected.types.list_tags_for_resource_output
    import aws_sdk_wellarchitected.types.list_template_shares_input
    import aws_sdk_wellarchitected.types.list_template_shares_max_results
    import aws_sdk_wellarchitected.types.list_template_shares_output
    import aws_sdk_wellarchitected.types.list_workload_shares_input
    import aws_sdk_wellarchitected.types.list_workload_shares_max_results
    import aws_sdk_wellarchitected.types.list_workload_shares_output
    import aws_sdk_wellarchitected.types.list_workloads_input
    import aws_sdk_wellarchitected.types.list_workloads_max_results
    import aws_sdk_wellarchitected.types.list_workloads_output
    import aws_sdk_wellarchitected.types.max_results
    import aws_sdk_wellarchitected.types.milestone_name
    import aws_sdk_wellarchitected.types.milestone_number
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.organization_sharing_status
    import aws_sdk_wellarchitected.types.permission_type
    import aws_sdk_wellarchitected.types.pillar_id
    import aws_sdk_wellarchitected.types.pillar_notes
    import aws_sdk_wellarchitected.types.profile_arn
    import aws_sdk_wellarchitected.types.profile_arns
    import aws_sdk_wellarchitected.types.profile_description
    import aws_sdk_wellarchitected.types.profile_name
    import aws_sdk_wellarchitected.types.profile_name_prefix
    import aws_sdk_wellarchitected.types.profile_owner_type
    import aws_sdk_wellarchitected.types.profile_question_updates
    import aws_sdk_wellarchitected.types.profile_version
    import aws_sdk_wellarchitected.types.question_id
    import aws_sdk_wellarchitected.types.question_priority
    import aws_sdk_wellarchitected.types.report_format
    import aws_sdk_wellarchitected.types.resource_arn
    import aws_sdk_wellarchitected.types.review_template_arns
    import aws_sdk_wellarchitected.types.review_template_lens_aliases
    import aws_sdk_wellarchitected.types.review_template_lenses
    import aws_sdk_wellarchitected.types.selected_choices
    import aws_sdk_wellarchitected.types.share_id
    import aws_sdk_wellarchitected.types.share_invitation_action
    import aws_sdk_wellarchitected.types.share_invitation_id
    import aws_sdk_wellarchitected.types.share_resource_type
    import aws_sdk_wellarchitected.types.share_status
    import aws_sdk_wellarchitected.types.shared_with
    import aws_sdk_wellarchitected.types.shared_with_prefix
    import aws_sdk_wellarchitected.types.tag_key_list
    import aws_sdk_wellarchitected.types.tag_map
    import aws_sdk_wellarchitected.types.tag_resource_input
    import aws_sdk_wellarchitected.types.tag_resource_output
    import aws_sdk_wellarchitected.types.template_arn
    import aws_sdk_wellarchitected.types.template_description
    import aws_sdk_wellarchitected.types.template_name
    import aws_sdk_wellarchitected.types.template_name_prefix
    import aws_sdk_wellarchitected.types.untag_resource_input
    import aws_sdk_wellarchitected.types.untag_resource_output
    import aws_sdk_wellarchitected.types.update_answer_input
    import aws_sdk_wellarchitected.types.update_answer_output
    import aws_sdk_wellarchitected.types.update_global_settings_input
    import aws_sdk_wellarchitected.types.update_integration_input
    import aws_sdk_wellarchitected.types.update_lens_review_input
    import aws_sdk_wellarchitected.types.update_lens_review_output
    import aws_sdk_wellarchitected.types.update_profile_input
    import aws_sdk_wellarchitected.types.update_profile_output
    import aws_sdk_wellarchitected.types.update_review_template_answer_input
    import aws_sdk_wellarchitected.types.update_review_template_answer_output
    import aws_sdk_wellarchitected.types.update_review_template_input
    import aws_sdk_wellarchitected.types.update_review_template_lens_review_input
    import aws_sdk_wellarchitected.types.update_review_template_lens_review_output
    import aws_sdk_wellarchitected.types.update_review_template_output
    import aws_sdk_wellarchitected.types.update_share_invitation_input
    import aws_sdk_wellarchitected.types.update_share_invitation_output
    import aws_sdk_wellarchitected.types.update_workload_input
    import aws_sdk_wellarchitected.types.update_workload_output
    import aws_sdk_wellarchitected.types.update_workload_share_input
    import aws_sdk_wellarchitected.types.update_workload_share_output
    import aws_sdk_wellarchitected.types.upgrade_lens_review_input
    import aws_sdk_wellarchitected.types.upgrade_profile_version_input
    import aws_sdk_wellarchitected.types.upgrade_review_template_lens_review_input
    import aws_sdk_wellarchitected.types.workload_account_ids
    import aws_sdk_wellarchitected.types.workload_applications
    import aws_sdk_wellarchitected.types.workload_architectural_design
    import aws_sdk_wellarchitected.types.workload_arn
    import aws_sdk_wellarchitected.types.workload_aws_regions
    import aws_sdk_wellarchitected.types.workload_description
    import aws_sdk_wellarchitected.types.workload_discovery_config
    import aws_sdk_wellarchitected.types.workload_environment
    import aws_sdk_wellarchitected.types.workload_id
    import aws_sdk_wellarchitected.types.workload_improvement_status
    import aws_sdk_wellarchitected.types.workload_industry
    import aws_sdk_wellarchitected.types.workload_industry_type
    import aws_sdk_wellarchitected.types.workload_jira_configuration_input
    import aws_sdk_wellarchitected.types.workload_lenses
    import aws_sdk_wellarchitected.types.workload_name
    import aws_sdk_wellarchitected.types.workload_name_prefix
    import aws_sdk_wellarchitected.types.workload_non_aws_regions
    import aws_sdk_wellarchitected.types.workload_pillar_priorities
    import aws_sdk_wellarchitected.types.workload_profile_arns
    import aws_sdk_wellarchitected.types.workload_review_owner


class AsyncWellArchitectedClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncWellArchitectedClient:
    """A client for the ``WellArchitected`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncWellArchitectedClientConfig(
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
        self, config_overrides: Optional[AsyncWellArchitectedClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncWellArchitectedClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def associate_lenses(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_aliases: "aws_sdk_wellarchitected.types.lens_aliases.LensAliases",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Associate a lens to a workload.</p> <p>Up to 10 lenses can be associated with a workload in a single API operation. A maximum of 20 lenses can be associated with a workload.</p> <note> <p> <b>Disclaimer</b> </p> <p>By accessing and/or applying custom lenses created by another Amazon Web Services user or account, you acknowledge that custom lenses created by other users and shared with you are Third Party Content as defined in the Amazon Web Services Customer Agreement. </p> </note>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.associate_lenses_input.AssociateLensesInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.associate_lenses

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.associate_lenses.async_associate_lenses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.associate_lenses_input.AssociateLensesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_aliases"] = lens_aliases

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_profiles(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        profile_arns: "aws_sdk_wellarchitected.types.profile_arns.ProfileArns",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Associate a profile with a workload.</p>

        Args:
            profile_arns: <p>The list of profile ARNs to associate with the workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.associate_profiles_input.AssociateProfilesInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.associate_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.associate_profiles.async_associate_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.associate_profiles_input.AssociateProfilesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["profile_arns"] = profile_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_lens_share(
        self,
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        shared_with: "aws_sdk_wellarchitected.types.shared_with.SharedWith",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.create_lens_share_output.CreateLensShareOutput":
        r"""<p>Create a lens share.</p> <p>The owner of a lens can share it with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. Lenses provided by Amazon Web Services (Amazon Web Services Official Content) cannot be shared.</p> <p> Shared access to a lens is not removed until the lens invitation is deleted.</p> <p>If you share a lens with an organization or OU, all accounts in the organization or OU are granted access to the lens.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-sharing.html\">Sharing a custom lens</a> in the <i>Well-Architected Tool User Guide</i>.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.create_lens_share_input.CreateLensShareInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.create_lens_share_output.CreateLensShareOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_lens_share

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_lens_share.async_create_lens_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.create_lens_share_input.CreateLensShareInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        input_["shared_with"] = shared_with
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_lens_version(
        self,
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        lens_version: "aws_sdk_wellarchitected.types.lens_version.LensVersion",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        is_major_version: Optional[
            "aws_sdk_wellarchitected.types.is_major_version.IsMajorVersion"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.create_lens_version_output.CreateLensVersionOutput":
        """<p>Create a new lens version.</p> <p>A lens can have up to 100 versions.</p> <p>Use this operation to publish a new lens version after you have imported a lens. The <code>LensAlias</code> is used to identify the lens to be published. The owner of a lens can share the lens with other Amazon Web Services accounts and users in the same Amazon Web Services Region. Only the owner of a lens can delete it. </p>

        Args:
            lens_version: <p>The version of the lens being created.</p>
            is_major_version: <p>Set to true if this new major lens version.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.create_lens_version_input.CreateLensVersionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.create_lens_version_output.CreateLensVersionOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_lens_version

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_lens_version.async_create_lens_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.create_lens_version_input.CreateLensVersionInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        input_["lens_version"] = lens_version
        if is_major_version is not None:
            input_["is_major_version"] = is_major_version
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_milestone(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        milestone_name: "aws_sdk_wellarchitected.types.milestone_name.MilestoneName",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.create_milestone_output.CreateMilestoneOutput":
        """<p>Create a milestone for an existing workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.create_milestone_input.CreateMilestoneInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.create_milestone_output.CreateMilestoneOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_milestone

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_milestone.async_create_milestone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.create_milestone_input.CreateMilestoneInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["milestone_name"] = milestone_name
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_profile(
        self,
        profile_name: "aws_sdk_wellarchitected.types.profile_name.ProfileName",
        profile_description: "aws_sdk_wellarchitected.types.profile_description.ProfileDescription",
        profile_questions: "aws_sdk_wellarchitected.types.profile_question_updates.ProfileQuestionUpdates",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        tags: Optional["aws_sdk_wellarchitected.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_wellarchitected.types.create_profile_output.CreateProfileOutput":
        """<p>Create a profile.</p>

        Args:
            profile_name: <p>Name of the profile.</p>
            profile_description: <p>The profile description.</p>
            profile_questions: <p>The profile questions.</p>
            tags: <p>The tags assigned to the profile.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.create_profile_input.CreateProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.create_profile_output.CreateProfileOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_profile

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_profile.async_create_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.create_profile_input.CreateProfileInput = {}  # type: ignore[typeddict-item]
        input_["profile_name"] = profile_name
        input_["profile_description"] = profile_description
        input_["profile_questions"] = profile_questions
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_profile_share(
        self,
        profile_arn: "aws_sdk_wellarchitected.types.profile_arn.ProfileArn",
        shared_with: "aws_sdk_wellarchitected.types.shared_with.SharedWith",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.create_profile_share_output.CreateProfileShareOutput":
        """<p>Create a profile share.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.create_profile_share_input.CreateProfileShareInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.create_profile_share_output.CreateProfileShareOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_profile_share

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_profile_share.async_create_profile_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.create_profile_share_input.CreateProfileShareInput = {}  # type: ignore[typeddict-item]
        input_["profile_arn"] = profile_arn
        input_["shared_with"] = shared_with
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_review_template(
        self,
        template_name: "aws_sdk_wellarchitected.types.template_name.TemplateName",
        description: "aws_sdk_wellarchitected.types.template_description.TemplateDescription",
        lenses: "aws_sdk_wellarchitected.types.review_template_lenses.ReviewTemplateLenses",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        notes: Optional["aws_sdk_wellarchitected.types.notes.Notes"] = None,
        tags: Optional["aws_sdk_wellarchitected.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_wellarchitected.types.create_review_template_output.CreateReviewTemplateOutput":
        """<p>Create a review template.</p> <note> <p> <b>Disclaimer</b> </p> <p>Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your review templates. If your review template or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.</p> </note>

        Args:
            template_name: <p>Name of the review template.</p>
            description: <p>The review template description.</p>
            lenses: <p>Lenses applied to the review template.</p>
            tags: <p>The tags assigned to the review template.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.create_review_template_input.CreateReviewTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.create_review_template_output.CreateReviewTemplateOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_review_template

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_review_template.async_create_review_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.create_review_template_input.CreateReviewTemplateInput = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        input_["description"] = description
        input_["lenses"] = lenses
        if notes is not None:
            input_["notes"] = notes
        if tags is not None:
            input_["tags"] = tags
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_template_share(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        shared_with: "aws_sdk_wellarchitected.types.shared_with.SharedWith",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.create_template_share_output.CreateTemplateShareOutput":
        """<p>Create a review template share.</p> <p>The owner of a review template can share it with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. </p> <p> Shared access to a review template is not removed until the review template share invitation is deleted.</p> <p>If you share a review template with an organization or OU, all accounts in the organization or OU are granted access to the review template.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your review template with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your review template available to those other accounts.</p> </note>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.create_template_share_input.CreateTemplateShareInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.create_template_share_output.CreateTemplateShareOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_template_share

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_template_share.async_create_template_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.create_template_share_input.CreateTemplateShareInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["shared_with"] = shared_with
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_workload(
        self,
        workload_name: "aws_sdk_wellarchitected.types.workload_name.WorkloadName",
        description: "aws_sdk_wellarchitected.types.workload_description.WorkloadDescription",
        environment: "aws_sdk_wellarchitected.types.workload_environment.WorkloadEnvironment",
        lenses: "aws_sdk_wellarchitected.types.workload_lenses.WorkloadLenses",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        account_ids: Optional[
            "aws_sdk_wellarchitected.types.workload_account_ids.WorkloadAccountIds"
        ] = None,
        aws_regions: Optional[
            "aws_sdk_wellarchitected.types.workload_aws_regions.WorkloadAwsRegions"
        ] = None,
        non_aws_regions: Optional[
            "aws_sdk_wellarchitected.types.workload_non_aws_regions.WorkloadNonAwsRegions"
        ] = None,
        pillar_priorities: Optional[
            "aws_sdk_wellarchitected.types.workload_pillar_priorities.WorkloadPillarPriorities"
        ] = None,
        architectural_design: Optional[
            "aws_sdk_wellarchitected.types.workload_architectural_design.WorkloadArchitecturalDesign"
        ] = None,
        review_owner: Optional[
            "aws_sdk_wellarchitected.types.workload_review_owner.WorkloadReviewOwner"
        ] = None,
        industry_type: Optional[
            "aws_sdk_wellarchitected.types.workload_industry_type.WorkloadIndustryType"
        ] = None,
        industry: Optional[
            "aws_sdk_wellarchitected.types.workload_industry.WorkloadIndustry"
        ] = None,
        notes: Optional["aws_sdk_wellarchitected.types.notes.Notes"] = None,
        tags: Optional["aws_sdk_wellarchitected.types.tag_map.TagMap"] = None,
        discovery_config: Optional[
            "aws_sdk_wellarchitected.types.workload_discovery_config.WorkloadDiscoveryConfig"
        ] = None,
        applications: Optional[
            "aws_sdk_wellarchitected.types.workload_applications.WorkloadApplications"
        ] = None,
        profile_arns: Optional[
            "aws_sdk_wellarchitected.types.workload_profile_arns.WorkloadProfileArns"
        ] = None,
        review_template_arns: Optional[
            "aws_sdk_wellarchitected.types.review_template_arns.ReviewTemplateArns"
        ] = None,
        jira_configuration: Optional[
            "aws_sdk_wellarchitected.types.workload_jira_configuration_input.WorkloadJiraConfigurationInput"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.create_workload_output.CreateWorkloadOutput":
        r"""<p>Create a new workload.</p> <p>The owner of a workload can share the workload with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. Only the owner of a workload can delete it.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/wellarchitected/latest/userguide/define-workload.html\">Defining a Workload</a> in the <i>Well-Architected Tool User Guide</i>.</p> <important> <p>Either <code>AwsRegions</code>, <code>NonAwsRegions</code>, or both must be specified when creating a workload.</p> <p>You also must specify <code>ReviewOwner</code>, even though the parameter is listed as not being required in the following section. </p> </important> <p>When creating a workload using a review template, you must have the following IAM permissions:</p> <ul> <li> <p> <code>wellarchitected:GetReviewTemplate</code> </p> </li> <li> <p> <code>wellarchitected:GetReviewTemplateAnswer</code> </p> </li> <li> <p> <code>wellarchitected:ListReviewTemplateAnswers</code> </p> </li> <li> <p> <code>wellarchitected:GetReviewTemplateLensReview</code> </p> </li> </ul>

        Args:
            tags: <p>The tags to be associated with the workload.</p>
            discovery_config: <p>Well-Architected discovery configuration settings associated to the workload.</p>
            applications: <p>List of AppRegistry application ARNs associated to the workload.</p>
            profile_arns: <p>The list of profile ARNs associated with the workload.</p>
            review_template_arns: <p>The list of review template ARNs to associate with the workload.</p>
            jira_configuration: <p>Jira configuration settings when creating a workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.create_workload_input.CreateWorkloadInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.create_workload_output.CreateWorkloadOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_workload

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_workload.async_create_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.create_workload_input.CreateWorkloadInput = {}  # type: ignore[typeddict-item]
        input_["workload_name"] = workload_name
        input_["description"] = description
        input_["environment"] = environment
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if aws_regions is not None:
            input_["aws_regions"] = aws_regions
        if non_aws_regions is not None:
            input_["non_aws_regions"] = non_aws_regions
        if pillar_priorities is not None:
            input_["pillar_priorities"] = pillar_priorities
        if architectural_design is not None:
            input_["architectural_design"] = architectural_design
        if review_owner is not None:
            input_["review_owner"] = review_owner
        if industry_type is not None:
            input_["industry_type"] = industry_type
        if industry is not None:
            input_["industry"] = industry
        input_["lenses"] = lenses
        if notes is not None:
            input_["notes"] = notes
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if discovery_config is not None:
            input_["discovery_config"] = discovery_config
        if applications is not None:
            input_["applications"] = applications
        if profile_arns is not None:
            input_["profile_arns"] = profile_arns
        if review_template_arns is not None:
            input_["review_template_arns"] = review_template_arns
        if jira_configuration is not None:
            input_["jira_configuration"] = jira_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_workload_share(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        shared_with: "aws_sdk_wellarchitected.types.shared_with.SharedWith",
        permission_type: "aws_sdk_wellarchitected.types.permission_type.PermissionType",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.create_workload_share_output.CreateWorkloadShareOutput":
        r"""<p>Create a workload share.</p> <p>The owner of a workload can share it with other Amazon Web Services accounts and users in the same Amazon Web Services Region. Shared access to a workload is not removed until the workload invitation is deleted.</p> <p>If you share a workload with an organization or OU, all accounts in the organization or OU are granted access to the workload.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-sharing.html\">Sharing a workload</a> in the <i>Well-Architected Tool User Guide</i>.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.create_workload_share_input.CreateWorkloadShareInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.create_workload_share_output.CreateWorkloadShareOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_workload_share

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.create_workload_share.async_create_workload_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.create_workload_share_input.CreateWorkloadShareInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["shared_with"] = shared_with
        input_["permission_type"] = permission_type
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_lens(
        self,
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        lens_status: "aws_sdk_wellarchitected.types.lens_status_type.LensStatusType",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete an existing lens.</p> <p>Only the owner of a lens can delete it. After the lens is deleted, Amazon Web Services accounts and users that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads. </p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Args:
            lens_status: <p>The status of the lens to be deleted.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.delete_lens_input.DeleteLensInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_lens

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_lens.async_delete_lens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.delete_lens_input.DeleteLensInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        input_["client_request_token"] = client_request_token
        input_["lens_status"] = lens_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_lens_share(
        self,
        share_id: "aws_sdk_wellarchitected.types.share_id.ShareId",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a lens share.</p> <p>After the lens share is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.delete_lens_share_input.DeleteLensShareInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_lens_share

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_lens_share.async_delete_lens_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.delete_lens_share_input.DeleteLensShareInput = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id
        input_["lens_alias"] = lens_alias
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_profile(
        self,
        profile_arn: "aws_sdk_wellarchitected.types.profile_arn.ProfileArn",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a profile.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your profile with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your profile available to those other accounts. Those other accounts may continue to access and use your shared profile even if you delete the profile from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.delete_profile_input.DeleteProfileInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_profile

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_profile.async_delete_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.delete_profile_input.DeleteProfileInput = {}  # type: ignore[typeddict-item]
        input_["profile_arn"] = profile_arn
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_profile_share(
        self,
        share_id: "aws_sdk_wellarchitected.types.share_id.ShareId",
        profile_arn: "aws_sdk_wellarchitected.types.profile_arn.ProfileArn",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a profile share.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.delete_profile_share_input.DeleteProfileShareInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_profile_share

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_profile_share.async_delete_profile_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.delete_profile_share_input.DeleteProfileShareInput = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id
        input_["profile_arn"] = profile_arn
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_review_template(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a review template.</p> <p>Only the owner of a review template can delete it.</p> <p>After the review template is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the review template with will no longer be able to apply it to new workloads.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.delete_review_template_input.DeleteReviewTemplateInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_review_template

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_review_template.async_delete_review_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.delete_review_template_input.DeleteReviewTemplateInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_template_share(
        self,
        share_id: "aws_sdk_wellarchitected.types.share_id.ShareId",
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a review template share.</p> <p>After the review template share is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the review template with will no longer be able to apply it to new workloads.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.delete_template_share_input.DeleteTemplateShareInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_template_share

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_template_share.async_delete_template_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.delete_template_share_input.DeleteTemplateShareInput = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id
        input_["template_arn"] = template_arn
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_workload(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete an existing workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.delete_workload_input.DeleteWorkloadInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_workload

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_workload.async_delete_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.delete_workload_input.DeleteWorkloadInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_workload_share(
        self,
        share_id: "aws_sdk_wellarchitected.types.share_id.ShareId",
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a workload share.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.delete_workload_share_input.DeleteWorkloadShareInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_workload_share

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.delete_workload_share.async_delete_workload_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.delete_workload_share_input.DeleteWorkloadShareInput = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id
        input_["workload_id"] = workload_id
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_lenses(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_aliases: "aws_sdk_wellarchitected.types.lens_aliases.LensAliases",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Disassociate a lens from a workload.</p> <p>Up to 10 lenses can be disassociated from a workload in a single API operation.</p> <note> <p>The Amazon Web Services Well-Architected Framework lens (<code>wellarchitected</code>) cannot be removed from a workload.</p> </note>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.disassociate_lenses_input.DisassociateLensesInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.disassociate_lenses

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.disassociate_lenses.async_disassociate_lenses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.disassociate_lenses_input.DisassociateLensesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_aliases"] = lens_aliases

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_profiles(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        profile_arns: "aws_sdk_wellarchitected.types.profile_arns.ProfileArns",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Disassociate a profile from a workload.</p>

        Args:
            profile_arns: <p>The list of profile ARNs to disassociate from the workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.disassociate_profiles_input.DisassociateProfilesInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.disassociate_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.disassociate_profiles.async_disassociate_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.disassociate_profiles_input.DisassociateProfilesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["profile_arns"] = profile_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def export_lens(
        self,
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_version: Optional[
            "aws_sdk_wellarchitected.types.lens_version.LensVersion"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.export_lens_output.ExportLensOutput":
        r"""<p>Export an existing lens.</p> <p>Only the owner of a lens can export it. Lenses provided by Amazon Web Services (Amazon Web Services Official Content) cannot be exported.</p> <p>Lenses are defined in JSON. For more information, see <a href=\"https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html\">JSON format specification</a> in the <i>Well-Architected Tool User Guide</i>.</p> <note> <p> <b>Disclaimer</b> </p> <p>Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.</p> </note>

        Args:
            lens_version: <p>The lens version to be exported.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.export_lens_input.ExportLensInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.export_lens_output.ExportLensOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.export_lens

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.export_lens.async_export_lens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.export_lens_input.ExportLensInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        if lens_version is not None:
            input_["lens_version"] = lens_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_answer(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        question_id: "aws_sdk_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.get_answer_output.GetAnswerOutput":
        """<p>Get the answer to a specific question in a workload review.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_answer_input.GetAnswerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_answer_output.GetAnswerOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_answer

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_answer.async_get_answer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_answer_input.GetAnswerInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        input_["question_id"] = question_id
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_consolidated_report(
        self,
        format: "aws_sdk_wellarchitected.types.report_format.ReportFormat",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        include_shared_resources: Optional[
            "aws_sdk_wellarchitected.types.include_shared_resources.IncludeSharedResources"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.get_consolidated_report_max_results.GetConsolidatedReportMaxResults"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.get_consolidated_report_output.GetConsolidatedReportOutput":
        """<p>Get a consolidated report of your workloads.</p> <p>You can optionally choose to include workloads that have been shared with you.</p>

        Args:
            format: <p>The format of the consolidated report.</p> <p>For <code>PDF</code>, <code>Base64String</code> is returned. For <code>JSON</code>, <code>Metrics</code> is returned.</p>
            include_shared_resources: <p>Set to <code>true</code> to have shared resources included in the report.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_consolidated_report_input.GetConsolidatedReportInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_consolidated_report_output.GetConsolidatedReportOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_consolidated_report

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_consolidated_report.async_get_consolidated_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_consolidated_report_input.GetConsolidatedReportInput = {}  # type: ignore[typeddict-item]
        input_["format"] = format
        if include_shared_resources is not None:
            input_["include_shared_resources"] = include_shared_resources
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_global_settings(
        self, *, config_overrides: Optional[AsyncWellArchitectedClientConfig] = None
    ) -> "aws_sdk_wellarchitected.types.get_global_settings_output.GetGlobalSettingsOutput":
        """<p>Global settings for all workloads.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_global_settings_output.GetGlobalSettingsOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_global_settings

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_global_settings.async_get_global_settings(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_lens(
        self,
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_version: Optional[
            "aws_sdk_wellarchitected.types.lens_version.LensVersion"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.get_lens_output.GetLensOutput":
        """<p>Get an existing lens.</p>

        Args:
            lens_version: <p>The lens version to be retrieved.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_lens_input.GetLensInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_lens_output.GetLensOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_lens

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_lens.async_get_lens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_lens_input.GetLensInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        if lens_version is not None:
            input_["lens_version"] = lens_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_lens_review(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.get_lens_review_output.GetLensReviewOutput":
        """<p>Get lens review.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_lens_review_input.GetLensReviewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_lens_review_output.GetLensReviewOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review.async_get_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_lens_review_input.GetLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_lens_review_report(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.get_lens_review_report_output.GetLensReviewReportOutput":
        """<p>Get lens review report.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_lens_review_report_input.GetLensReviewReportInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_lens_review_report_output.GetLensReviewReportOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review_report

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review_report.async_get_lens_review_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_lens_review_report_input.GetLensReviewReportInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_lens_version_difference(
        self,
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        base_lens_version: Optional[
            "aws_sdk_wellarchitected.types.lens_version.LensVersion"
        ] = None,
        target_lens_version: Optional[
            "aws_sdk_wellarchitected.types.lens_version.LensVersion"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.get_lens_version_difference_output.GetLensVersionDifferenceOutput":
        """<p>Get lens version differences.</p>

        Args:
            base_lens_version: <p>The base version of the lens.</p>
            target_lens_version: <p>The lens version to target a difference for.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_lens_version_difference_input.GetLensVersionDifferenceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_lens_version_difference_output.GetLensVersionDifferenceOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_lens_version_difference

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_lens_version_difference.async_get_lens_version_difference(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_lens_version_difference_input.GetLensVersionDifferenceInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        if base_lens_version is not None:
            input_["base_lens_version"] = base_lens_version
        if target_lens_version is not None:
            input_["target_lens_version"] = target_lens_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_milestone(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        milestone_number: "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.get_milestone_output.GetMilestoneOutput":
        """<p>Get a milestone for an existing workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_milestone_input.GetMilestoneInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_milestone_output.GetMilestoneOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_milestone

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_milestone.async_get_milestone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_milestone_input.GetMilestoneInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["milestone_number"] = milestone_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_profile(
        self,
        profile_arn: "aws_sdk_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        profile_version: Optional[
            "aws_sdk_wellarchitected.types.profile_version.ProfileVersion"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.get_profile_output.GetProfileOutput":
        """<p>Get profile information.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>
            profile_version: <p>The profile version.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_profile_input.GetProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_profile_output.GetProfileOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_profile

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_profile.async_get_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_profile_input.GetProfileInput = {}  # type: ignore[typeddict-item]
        input_["profile_arn"] = profile_arn
        if profile_version is not None:
            input_["profile_version"] = profile_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_profile_template(
        self, *, config_overrides: Optional[AsyncWellArchitectedClientConfig] = None
    ) -> "aws_sdk_wellarchitected.types.get_profile_template_output.GetProfileTemplateOutput":
        """<p>Get profile template.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_profile_template_input.GetProfileTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_profile_template_output.GetProfileTemplateOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_profile_template

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_profile_template.async_get_profile_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_profile_template_input.GetProfileTemplateInput = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_review_template(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.get_review_template_output.GetReviewTemplateOutput":
        """<p>Get review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_review_template_input.GetReviewTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_review_template_output.GetReviewTemplateOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_review_template

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_review_template.async_get_review_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_review_template_input.GetReviewTemplateInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_review_template_answer(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        question_id: "aws_sdk_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.get_review_template_answer_output.GetReviewTemplateAnswerOutput":
        """<p>Get review template answer.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_review_template_answer_input.GetReviewTemplateAnswerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_review_template_answer_output.GetReviewTemplateAnswerOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_answer

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_answer.async_get_review_template_answer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_review_template_answer_input.GetReviewTemplateAnswerInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias
        input_["question_id"] = question_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_review_template_lens_review(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.get_review_template_lens_review_output.GetReviewTemplateLensReviewOutput":
        """<p>Get a lens review associated with a review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_review_template_lens_review_input.GetReviewTemplateLensReviewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_review_template_lens_review_output.GetReviewTemplateLensReviewOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_lens_review

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_lens_review.async_get_review_template_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_review_template_lens_review_input.GetReviewTemplateLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_workload(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.get_workload_output.GetWorkloadOutput":
        """<p>Get an existing workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.get_workload_input.GetWorkloadInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.get_workload_output.GetWorkloadOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_workload

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.get_workload.async_get_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.get_workload_input.GetWorkloadInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_lens(
        self,
        json_string: "aws_sdk_wellarchitected.types.lens_json.LensJSON",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_alias: Optional[
            "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
        ] = None,
        tags: Optional["aws_sdk_wellarchitected.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_wellarchitected.types.import_lens_output.ImportLensOutput":
        r"""<p>Import a new custom lens or update an existing custom lens.</p> <p>To update an existing custom lens, specify its ARN as the <code>LensAlias</code>. If no ARN is specified, a new custom lens is created.</p> <p>The new or updated lens will have a status of <code>DRAFT</code>. The lens cannot be applied to workloads or shared with other Amazon Web Services accounts until it's published with <a>CreateLensVersion</a>.</p> <p>Lenses are defined in JSON. For more information, see <a href=\"https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html\">JSON format specification</a> in the <i>Well-Architected Tool User Guide</i>.</p> <p>A custom lens cannot exceed 500 KB in size.</p> <note> <p> <b>Disclaimer</b> </p> <p>Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.</p> </note>

        Args:
            json_string: <p>The JSON representation of a lens.</p>
            tags: <p>Tags to associate to a lens.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.import_lens_input.ImportLensInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.import_lens_output.ImportLensOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.import_lens

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.import_lens.async_import_lens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.import_lens_input.ImportLensInput = {}  # type: ignore[typeddict-item]
        if lens_alias is not None:
            input_["lens_alias"] = lens_alias
        input_["json_string"] = json_string
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_answers(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        pillar_id: Optional["aws_sdk_wellarchitected.types.pillar_id.PillarId"] = None,
        milestone_number: Optional[
            "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.list_answers_max_results.ListAnswersMaxResults"
        ] = None,
        question_priority: Optional[
            "aws_sdk_wellarchitected.types.question_priority.QuestionPriority"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_answers_output.ListAnswersOutput":
        """<p>List of answers for a particular workload and lens.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>
            question_priority: <p>The priority of the question.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_answers_input.ListAnswersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_answers_output.ListAnswersOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_answers

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_answers.async_list_answers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_answers_input.ListAnswersInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        if pillar_id is not None:
            input_["pillar_id"] = pillar_id
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if question_priority is not None:
            input_["question_priority"] = question_priority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_check_details(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_arn: "aws_sdk_wellarchitected.types.lens_arn.LensArn",
        pillar_id: "aws_sdk_wellarchitected.types.pillar_id.PillarId",
        question_id: "aws_sdk_wellarchitected.types.question_id.QuestionId",
        choice_id: "aws_sdk_wellarchitected.types.choice_id.ChoiceId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "aws_sdk_wellarchitected.types.list_check_details_output.ListCheckDetailsOutput"
    ):
        """<p>List of Trusted Advisor check details by account related to the workload.</p>

        Args:
            lens_arn: <p>Well-Architected Lens ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_check_details_input.ListCheckDetailsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_check_details_output.ListCheckDetailsOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_check_details

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_check_details.async_list_check_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_check_details_input.ListCheckDetailsInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["lens_arn"] = lens_arn
        input_["pillar_id"] = pillar_id
        input_["question_id"] = question_id
        input_["choice_id"] = choice_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_check_summaries(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_arn: "aws_sdk_wellarchitected.types.lens_arn.LensArn",
        pillar_id: "aws_sdk_wellarchitected.types.pillar_id.PillarId",
        question_id: "aws_sdk_wellarchitected.types.question_id.QuestionId",
        choice_id: "aws_sdk_wellarchitected.types.choice_id.ChoiceId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_check_summaries_output.ListCheckSummariesOutput":
        """<p>List of Trusted Advisor checks summarized for all accounts related to the workload.</p>

        Args:
            lens_arn: <p>Well-Architected Lens ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_check_summaries_input.ListCheckSummariesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_check_summaries_output.ListCheckSummariesOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_check_summaries

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_check_summaries.async_list_check_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_check_summaries_input.ListCheckSummariesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["lens_arn"] = lens_arn
        input_["pillar_id"] = pillar_id
        input_["question_id"] = question_id
        input_["choice_id"] = choice_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_lenses(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.max_results.MaxResults"
        ] = None,
        lens_type: Optional["aws_sdk_wellarchitected.types.lens_type.LensType"] = None,
        lens_status: Optional[
            "aws_sdk_wellarchitected.types.lens_status_type.LensStatusType"
        ] = None,
        lens_name: Optional["aws_sdk_wellarchitected.types.lens_name.LensName"] = None,
    ) -> "aws_sdk_wellarchitected.types.list_lenses_output.ListLensesOutput":
        """<p>List the available lenses.</p>

        Args:
            lens_type: <p>The type of lenses to be returned.</p>
            lens_status: <p>The status of lenses to be returned.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_lenses_input.ListLensesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_lenses_output.ListLensesOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_lenses

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_lenses.async_list_lenses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_lenses_input.ListLensesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if lens_type is not None:
            input_["lens_type"] = lens_type
        if lens_status is not None:
            input_["lens_status"] = lens_status
        if lens_name is not None:
            input_["lens_name"] = lens_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_lens_review_improvements(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        pillar_id: Optional["aws_sdk_wellarchitected.types.pillar_id.PillarId"] = None,
        milestone_number: Optional[
            "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.list_lens_review_improvements_max_results.ListLensReviewImprovementsMaxResults"
        ] = None,
        question_priority: Optional[
            "aws_sdk_wellarchitected.types.question_priority.QuestionPriority"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_lens_review_improvements_output.ListLensReviewImprovementsOutput":
        """<p>List the improvements of a particular lens review.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>
            question_priority: <p>The priority of the question.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_lens_review_improvements_input.ListLensReviewImprovementsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_lens_review_improvements_output.ListLensReviewImprovementsOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_lens_review_improvements

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_lens_review_improvements.async_list_lens_review_improvements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_lens_review_improvements_input.ListLensReviewImprovementsInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        if pillar_id is not None:
            input_["pillar_id"] = pillar_id
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if question_priority is not None:
            input_["question_priority"] = question_priority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_lens_reviews(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_lens_reviews_output.ListLensReviewsOutput":
        """<p>List lens reviews for a particular workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_lens_reviews_input.ListLensReviewsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_lens_reviews_output.ListLensReviewsOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_lens_reviews

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_lens_reviews.async_list_lens_reviews(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_lens_reviews_input.ListLensReviewsInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_lens_shares(
        self,
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "aws_sdk_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.list_workload_shares_max_results.ListWorkloadSharesMaxResults"
        ] = None,
        status: Optional[
            "aws_sdk_wellarchitected.types.share_status.ShareStatus"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_lens_shares_output.ListLensSharesOutput":
        """<p>List the lens shares associated with the lens.</p>

        Args:
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the lens is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_lens_shares_input.ListLensSharesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_lens_shares_output.ListLensSharesOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_lens_shares

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_lens_shares.async_list_lens_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_lens_shares_input.ListLensSharesInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_milestones(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_milestones_output.ListMilestonesOutput":
        """<p>List all milestones for an existing workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_milestones_input.ListMilestonesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_milestones_output.ListMilestonesOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_milestones

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_milestones.async_list_milestones(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_milestones_input.ListMilestonesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_notifications(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_id: Optional[
            "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.list_notifications_max_results.ListNotificationsMaxResults"
        ] = None,
        resource_arn: Optional[
            "aws_sdk_wellarchitected.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_notifications_output.ListNotificationsOutput":
        """<p>List lens notifications.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>
            resource_arn: <p>The ARN for the related resource for the notification.</p> <note> <p>Only one of <code>WorkloadID</code> or <code>ResourceARN</code> should be specified.</p> </note>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_notifications_input.ListNotificationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_notifications_output.ListNotificationsOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_notifications

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_notifications.async_list_notifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_notifications_input.ListNotificationsInput = {}  # type: ignore[typeddict-item]
        if workload_id is not None:
            input_["workload_id"] = workload_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_profile_notifications(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_id: Optional[
            "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_profile_notifications_output.ListProfileNotificationsOutput":
        """<p>List profile notifications.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_profile_notifications_input.ListProfileNotificationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_profile_notifications_output.ListProfileNotificationsOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_profile_notifications

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_profile_notifications.async_list_profile_notifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_profile_notifications_input.ListProfileNotificationsInput = {}  # type: ignore[typeddict-item]
        if workload_id is not None:
            input_["workload_id"] = workload_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_profiles(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        profile_name_prefix: Optional[
            "aws_sdk_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
        ] = None,
        profile_owner_type: Optional[
            "aws_sdk_wellarchitected.types.profile_owner_type.ProfileOwnerType"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_profiles_output.ListProfilesOutput":
        """<p>List profiles.</p>

        Args:
            profile_name_prefix: <p>An optional string added to the beginning of each profile name returned in the results.</p>
            profile_owner_type: <p>Profile owner type.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_profiles_input.ListProfilesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_profiles_output.ListProfilesOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_profiles

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_profiles.async_list_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_profiles_input.ListProfilesInput = {}  # type: ignore[typeddict-item]
        if profile_name_prefix is not None:
            input_["profile_name_prefix"] = profile_name_prefix
        if profile_owner_type is not None:
            input_["profile_owner_type"] = profile_owner_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_profile_shares(
        self,
        profile_arn: "aws_sdk_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "aws_sdk_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.list_profile_shares_max_results.ListProfileSharesMaxResults"
        ] = None,
        status: Optional[
            "aws_sdk_wellarchitected.types.share_status.ShareStatus"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_profile_shares_output.ListProfileSharesOutput":
        """<p>List profile shares.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the profile is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_profile_shares_input.ListProfileSharesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_profile_shares_output.ListProfileSharesOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_profile_shares

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_profile_shares.async_list_profile_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_profile_shares_input.ListProfileSharesInput = {}  # type: ignore[typeddict-item]
        input_["profile_arn"] = profile_arn
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_review_template_answers(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        pillar_id: Optional["aws_sdk_wellarchitected.types.pillar_id.PillarId"] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.list_review_template_answers_max_results.ListReviewTemplateAnswersMaxResults"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_review_template_answers_output.ListReviewTemplateAnswersOutput":
        """<p>List the answers of a review template.</p>

        Args:
            template_arn: <p>The ARN of the review template.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_review_template_answers_input.ListReviewTemplateAnswersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_review_template_answers_output.ListReviewTemplateAnswersOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_review_template_answers

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_review_template_answers.async_list_review_template_answers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_review_template_answers_input.ListReviewTemplateAnswersInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias
        if pillar_id is not None:
            input_["pillar_id"] = pillar_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_review_templates(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_review_templates_output.ListReviewTemplatesOutput":
        """<p>List review templates.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_review_templates_input.ListReviewTemplatesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_review_templates_output.ListReviewTemplatesOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_review_templates

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_review_templates.async_list_review_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_review_templates_input.ListReviewTemplatesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_share_invitations(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_name_prefix: Optional[
            "aws_sdk_wellarchitected.types.workload_name_prefix.WorkloadNamePrefix"
        ] = None,
        lens_name_prefix: Optional[
            "aws_sdk_wellarchitected.types.lens_name_prefix.LensNamePrefix"
        ] = None,
        share_resource_type: Optional[
            "aws_sdk_wellarchitected.types.share_resource_type.ShareResourceType"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.list_share_invitations_max_results.ListShareInvitationsMaxResults"
        ] = None,
        profile_name_prefix: Optional[
            "aws_sdk_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
        ] = None,
        template_name_prefix: Optional[
            "aws_sdk_wellarchitected.types.template_name_prefix.TemplateNamePrefix"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_share_invitations_output.ListShareInvitationsOutput":
        """<p>List the share invitations.</p> <p> <code>WorkloadNamePrefix</code>, <code>LensNamePrefix</code>, <code>ProfileNamePrefix</code>, and <code>TemplateNamePrefix</code> are mutually exclusive. Use the parameter that matches your <code>ShareResourceType</code>.</p>

        Args:
            lens_name_prefix: <p>An optional string added to the beginning of each lens name returned in the results.</p>
            share_resource_type: <p>The type of share invitations to be returned.</p>
            max_results: <p>The maximum number of results to return for this request.</p>
            profile_name_prefix: <p>An optional string added to the beginning of each profile name returned in the results.</p>
            template_name_prefix: <p>An optional string added to the beginning of each review template name returned in the results.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_share_invitations_input.ListShareInvitationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_share_invitations_output.ListShareInvitationsOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_share_invitations

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_share_invitations.async_list_share_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_share_invitations_input.ListShareInvitationsInput = {}  # type: ignore[typeddict-item]
        if workload_name_prefix is not None:
            input_["workload_name_prefix"] = workload_name_prefix
        if lens_name_prefix is not None:
            input_["lens_name_prefix"] = lens_name_prefix
        if share_resource_type is not None:
            input_["share_resource_type"] = share_resource_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if profile_name_prefix is not None:
            input_["profile_name_prefix"] = profile_name_prefix
        if template_name_prefix is not None:
            input_["template_name_prefix"] = template_name_prefix

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        workload_arn: "aws_sdk_wellarchitected.types.workload_arn.WorkloadArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List the tags for a resource.</p> <note> <p>The WorkloadArn parameter can be a workload ARN, a custom lens ARN, a profile ARN, or review template ARN.</p> </note>

        Raises:
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["workload_arn"] = workload_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_template_shares(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "aws_sdk_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.list_template_shares_max_results.ListTemplateSharesMaxResults"
        ] = None,
        status: Optional[
            "aws_sdk_wellarchitected.types.share_status.ShareStatus"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_template_shares_output.ListTemplateSharesOutput":
        """<p>List review template shares.</p>

        Args:
            template_arn: <p>The review template ARN.</p>
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the profile is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_template_shares_input.ListTemplateSharesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_template_shares_output.ListTemplateSharesOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_template_shares

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_template_shares.async_list_template_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_template_shares_input.ListTemplateSharesInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_workloads(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_name_prefix: Optional[
            "aws_sdk_wellarchitected.types.workload_name_prefix.WorkloadNamePrefix"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.list_workloads_max_results.ListWorkloadsMaxResults"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_workloads_output.ListWorkloadsOutput":
        """<p>Paginated list of workloads.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_workloads_input.ListWorkloadsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_workloads_output.ListWorkloadsOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_workloads

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_workloads.async_list_workloads(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_workloads_input.ListWorkloadsInput = {}  # type: ignore[typeddict-item]
        if workload_name_prefix is not None:
            input_["workload_name_prefix"] = workload_name_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_workload_shares(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "aws_sdk_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional[
            "aws_sdk_wellarchitected.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_wellarchitected.types.list_workload_shares_max_results.ListWorkloadSharesMaxResults"
        ] = None,
        status: Optional[
            "aws_sdk_wellarchitected.types.share_status.ShareStatus"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.list_workload_shares_output.ListWorkloadSharesOutput":
        """<p>List the workload shares associated with the workload.</p>

        Args:
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the workload is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.list_workload_shares_input.ListWorkloadSharesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.list_workload_shares_output.ListWorkloadSharesOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_workload_shares

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.list_workload_shares.async_list_workload_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.list_workload_shares_input.ListWorkloadSharesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        workload_arn: "aws_sdk_wellarchitected.types.workload_arn.WorkloadArn",
        tags: "aws_sdk_wellarchitected.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.tag_resource_output.TagResourceOutput":
        """<p>Adds one or more tags to the specified resource.</p> <note> <p>The WorkloadArn parameter can be a workload ARN, a custom lens ARN, a profile ARN, or review template ARN.</p> </note>

        Args:
            tags: <p>The tags for the resource.</p>

        Raises:
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["workload_arn"] = workload_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        workload_arn: "aws_sdk_wellarchitected.types.workload_arn.WorkloadArn",
        tag_keys: "aws_sdk_wellarchitected.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.untag_resource_output.UntagResourceOutput":
        """<p>Deletes specified tags from a resource.</p> <note> <p>The WorkloadArn parameter can be a workload ARN, a custom lens ARN, a profile ARN, or review template ARN.</p> </note> <p>To specify multiple tags, use separate <b>tagKeys</b> parameters, for example:</p> <p> <code>DELETE /tags/WorkloadArn?tagKeys=key1&tagKeys=key2</code> </p>

        Args:
            tag_keys: <p>A list of tag keys. Existing tags of the resource whose keys are members of this list are removed from the resource.</p>

        Raises:
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["workload_arn"] = workload_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_answer(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        question_id: "aws_sdk_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        selected_choices: Optional[
            "aws_sdk_wellarchitected.types.selected_choices.SelectedChoices"
        ] = None,
        choice_updates: Optional[
            "aws_sdk_wellarchitected.types.choice_updates.ChoiceUpdates"
        ] = None,
        notes: Optional["aws_sdk_wellarchitected.types.notes.Notes"] = None,
        is_applicable: Optional[
            "aws_sdk_wellarchitected.types.is_applicable.IsApplicable"
        ] = None,
        reason: Optional[
            "aws_sdk_wellarchitected.types.answer_reason.AnswerReason"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.update_answer_output.UpdateAnswerOutput":
        """<p>Update the answer to a specific question in a workload review.</p>

        Args:
            choice_updates: <p>A list of choices to update on a question in your workload. The String key corresponds to the choice ID to be updated.</p>
            reason: <p>The reason why a question is not applicable to your workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_answer_input.UpdateAnswerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.update_answer_output.UpdateAnswerOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_answer

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_answer.async_update_answer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_answer_input.UpdateAnswerInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        input_["question_id"] = question_id
        if selected_choices is not None:
            input_["selected_choices"] = selected_choices
        if choice_updates is not None:
            input_["choice_updates"] = choice_updates
        if notes is not None:
            input_["notes"] = notes
        if is_applicable is not None:
            input_["is_applicable"] = is_applicable
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_global_settings(
        self,
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        organization_sharing_status: Optional[
            "aws_sdk_wellarchitected.types.organization_sharing_status.OrganizationSharingStatus"
        ] = None,
        discovery_integration_status: Optional[
            "aws_sdk_wellarchitected.types.discovery_integration_status.DiscoveryIntegrationStatus"
        ] = None,
        jira_configuration: Optional[
            "aws_sdk_wellarchitected.types.account_jira_configuration_input.AccountJiraConfigurationInput"
        ] = None,
    ) -> None:
        """<p>Update whether the Amazon Web Services account is opted into organization sharing and discovery integration features.</p>

        Args:
            organization_sharing_status: <p>The status of organization sharing settings.</p>
            discovery_integration_status: <p>The status of discovery support settings.</p>
            jira_configuration: <p>The status of Jira integration settings.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_global_settings_input.UpdateGlobalSettingsInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_global_settings

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_global_settings.async_update_global_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_global_settings_input.UpdateGlobalSettingsInput = {}  # type: ignore[typeddict-item]
        if organization_sharing_status is not None:
            input_["organization_sharing_status"] = organization_sharing_status
        if discovery_integration_status is not None:
            input_["discovery_integration_status"] = discovery_integration_status
        if jira_configuration is not None:
            input_["jira_configuration"] = jira_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_integration(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        client_request_token: "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken",
        integrating_service: "aws_sdk_wellarchitected.types.integrating_service.IntegratingService",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Update integration features.</p>

        Args:
            integrating_service: <p>Which integrated service to update.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_integration_input.UpdateIntegrationInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_integration

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_integration.async_update_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_integration_input.UpdateIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["client_request_token"] = client_request_token
        input_["integrating_service"] = integrating_service

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_lens_review(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_notes: Optional["aws_sdk_wellarchitected.types.notes.Notes"] = None,
        pillar_notes: Optional[
            "aws_sdk_wellarchitected.types.pillar_notes.PillarNotes"
        ] = None,
        jira_configuration: Optional[
            "aws_sdk_wellarchitected.types.jira_selected_question_configuration.JiraSelectedQuestionConfiguration"
        ] = None,
    ) -> (
        "aws_sdk_wellarchitected.types.update_lens_review_output.UpdateLensReviewOutput"
    ):
        """<p>Update lens review for a particular workload.</p>

        Args:
            jira_configuration: <p>Configuration of the Jira integration.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_lens_review_input.UpdateLensReviewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.update_lens_review_output.UpdateLensReviewOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_lens_review

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_lens_review.async_update_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_lens_review_input.UpdateLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        if lens_notes is not None:
            input_["lens_notes"] = lens_notes
        if pillar_notes is not None:
            input_["pillar_notes"] = pillar_notes
        if jira_configuration is not None:
            input_["jira_configuration"] = jira_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_profile(
        self,
        profile_arn: "aws_sdk_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        profile_description: Optional[
            "aws_sdk_wellarchitected.types.profile_description.ProfileDescription"
        ] = None,
        profile_questions: Optional[
            "aws_sdk_wellarchitected.types.profile_question_updates.ProfileQuestionUpdates"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.update_profile_output.UpdateProfileOutput":
        """<p>Update a profile.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>
            profile_description: <p>The profile description.</p>
            profile_questions: <p>Profile questions.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_profile_input.UpdateProfileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.update_profile_output.UpdateProfileOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_profile

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_profile.async_update_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_profile_input.UpdateProfileInput = {}  # type: ignore[typeddict-item]
        input_["profile_arn"] = profile_arn
        if profile_description is not None:
            input_["profile_description"] = profile_description
        if profile_questions is not None:
            input_["profile_questions"] = profile_questions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_review_template(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        template_name: Optional[
            "aws_sdk_wellarchitected.types.template_name.TemplateName"
        ] = None,
        description: Optional[
            "aws_sdk_wellarchitected.types.template_description.TemplateDescription"
        ] = None,
        notes: Optional["aws_sdk_wellarchitected.types.notes.Notes"] = None,
        lenses_to_associate: Optional[
            "aws_sdk_wellarchitected.types.review_template_lens_aliases.ReviewTemplateLensAliases"
        ] = None,
        lenses_to_disassociate: Optional[
            "aws_sdk_wellarchitected.types.review_template_lens_aliases.ReviewTemplateLensAliases"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.update_review_template_output.UpdateReviewTemplateOutput":
        """<p>Update a review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>
            template_name: <p>The review template name.</p>
            description: <p>The review template description.</p>
            lenses_to_associate: <p>A list of lens aliases or ARNs to apply to the review template.</p>
            lenses_to_disassociate: <p>A list of lens aliases or ARNs to unapply to the review template. The <code>wellarchitected</code> lens cannot be unapplied.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_review_template_input.UpdateReviewTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.update_review_template_output.UpdateReviewTemplateOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_review_template

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_review_template.async_update_review_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_review_template_input.UpdateReviewTemplateInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        if template_name is not None:
            input_["template_name"] = template_name
        if description is not None:
            input_["description"] = description
        if notes is not None:
            input_["notes"] = notes
        if lenses_to_associate is not None:
            input_["lenses_to_associate"] = lenses_to_associate
        if lenses_to_disassociate is not None:
            input_["lenses_to_disassociate"] = lenses_to_disassociate

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_review_template_answer(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        question_id: "aws_sdk_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        selected_choices: Optional[
            "aws_sdk_wellarchitected.types.selected_choices.SelectedChoices"
        ] = None,
        choice_updates: Optional[
            "aws_sdk_wellarchitected.types.choice_updates.ChoiceUpdates"
        ] = None,
        notes: Optional["aws_sdk_wellarchitected.types.notes.Notes"] = None,
        is_applicable: Optional[
            "aws_sdk_wellarchitected.types.is_applicable.IsApplicable"
        ] = None,
        reason: Optional[
            "aws_sdk_wellarchitected.types.answer_reason.AnswerReason"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.update_review_template_answer_output.UpdateReviewTemplateAnswerOutput":
        """<p>Update a review template answer.</p>

        Args:
            template_arn: <p>The review template ARN.</p>
            choice_updates: <p>A list of choices to be updated.</p>
            reason: <p>The update reason.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_review_template_answer_input.UpdateReviewTemplateAnswerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.update_review_template_answer_output.UpdateReviewTemplateAnswerOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_answer

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_answer.async_update_review_template_answer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_review_template_answer_input.UpdateReviewTemplateAnswerInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias
        input_["question_id"] = question_id
        if selected_choices is not None:
            input_["selected_choices"] = selected_choices
        if choice_updates is not None:
            input_["choice_updates"] = choice_updates
        if notes is not None:
            input_["notes"] = notes
        if is_applicable is not None:
            input_["is_applicable"] = is_applicable
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_review_template_lens_review(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        lens_notes: Optional["aws_sdk_wellarchitected.types.notes.Notes"] = None,
        pillar_notes: Optional[
            "aws_sdk_wellarchitected.types.pillar_notes.PillarNotes"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.update_review_template_lens_review_output.UpdateReviewTemplateLensReviewOutput":
        """<p>Update a lens review associated with a review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_review_template_lens_review_input.UpdateReviewTemplateLensReviewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.update_review_template_lens_review_output.UpdateReviewTemplateLensReviewOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_lens_review

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_lens_review.async_update_review_template_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_review_template_lens_review_input.UpdateReviewTemplateLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias
        if lens_notes is not None:
            input_["lens_notes"] = lens_notes
        if pillar_notes is not None:
            input_["pillar_notes"] = pillar_notes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_share_invitation(
        self,
        share_invitation_id: "aws_sdk_wellarchitected.types.share_invitation_id.ShareInvitationId",
        share_invitation_action: "aws_sdk_wellarchitected.types.share_invitation_action.ShareInvitationAction",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.update_share_invitation_output.UpdateShareInvitationOutput":
        """<p>Update a workload or custom lens share invitation.</p> <note> <p>This API operation can be called independently of any resource. Previous documentation implied that a workload ARN must be specified.</p> </note>

        Args:
            share_invitation_id: <p>The ID assigned to the share invitation.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_share_invitation_input.UpdateShareInvitationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.update_share_invitation_output.UpdateShareInvitationOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_share_invitation

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_share_invitation.async_update_share_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_share_invitation_input.UpdateShareInvitationInput = {}  # type: ignore[typeddict-item]
        input_["share_invitation_id"] = share_invitation_id
        input_["share_invitation_action"] = share_invitation_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_workload(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        workload_name: Optional[
            "aws_sdk_wellarchitected.types.workload_name.WorkloadName"
        ] = None,
        description: Optional[
            "aws_sdk_wellarchitected.types.workload_description.WorkloadDescription"
        ] = None,
        environment: Optional[
            "aws_sdk_wellarchitected.types.workload_environment.WorkloadEnvironment"
        ] = None,
        account_ids: Optional[
            "aws_sdk_wellarchitected.types.workload_account_ids.WorkloadAccountIds"
        ] = None,
        aws_regions: Optional[
            "aws_sdk_wellarchitected.types.workload_aws_regions.WorkloadAwsRegions"
        ] = None,
        non_aws_regions: Optional[
            "aws_sdk_wellarchitected.types.workload_non_aws_regions.WorkloadNonAwsRegions"
        ] = None,
        pillar_priorities: Optional[
            "aws_sdk_wellarchitected.types.workload_pillar_priorities.WorkloadPillarPriorities"
        ] = None,
        architectural_design: Optional[
            "aws_sdk_wellarchitected.types.workload_architectural_design.WorkloadArchitecturalDesign"
        ] = None,
        review_owner: Optional[
            "aws_sdk_wellarchitected.types.workload_review_owner.WorkloadReviewOwner"
        ] = None,
        is_review_owner_update_acknowledged: Optional[
            "aws_sdk_wellarchitected.types.is_review_owner_update_acknowledged.IsReviewOwnerUpdateAcknowledged"
        ] = None,
        industry_type: Optional[
            "aws_sdk_wellarchitected.types.workload_industry_type.WorkloadIndustryType"
        ] = None,
        industry: Optional[
            "aws_sdk_wellarchitected.types.workload_industry.WorkloadIndustry"
        ] = None,
        notes: Optional["aws_sdk_wellarchitected.types.notes.Notes"] = None,
        improvement_status: Optional[
            "aws_sdk_wellarchitected.types.workload_improvement_status.WorkloadImprovementStatus"
        ] = None,
        discovery_config: Optional[
            "aws_sdk_wellarchitected.types.workload_discovery_config.WorkloadDiscoveryConfig"
        ] = None,
        applications: Optional[
            "aws_sdk_wellarchitected.types.workload_applications.WorkloadApplications"
        ] = None,
        jira_configuration: Optional[
            "aws_sdk_wellarchitected.types.workload_jira_configuration_input.WorkloadJiraConfigurationInput"
        ] = None,
    ) -> "aws_sdk_wellarchitected.types.update_workload_output.UpdateWorkloadOutput":
        """<p>Update an existing workload.</p>

        Args:
            is_review_owner_update_acknowledged: <p>Flag indicating whether the workload owner has acknowledged that the <i>Review owner</i> field is required.</p> <p>If a <b>Review owner</b> is not added to the workload within 60 days of acknowledgement, access to the workload is restricted until an owner is added.</p>
            discovery_config: <p>Well-Architected discovery configuration settings to associate to the workload.</p>
            applications: <p>List of AppRegistry application ARNs to associate to the workload.</p>
            jira_configuration: <p>Configuration of the Jira integration.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_workload_input.UpdateWorkloadInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.update_workload_output.UpdateWorkloadOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_workload

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_workload.async_update_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_workload_input.UpdateWorkloadInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        if workload_name is not None:
            input_["workload_name"] = workload_name
        if description is not None:
            input_["description"] = description
        if environment is not None:
            input_["environment"] = environment
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if aws_regions is not None:
            input_["aws_regions"] = aws_regions
        if non_aws_regions is not None:
            input_["non_aws_regions"] = non_aws_regions
        if pillar_priorities is not None:
            input_["pillar_priorities"] = pillar_priorities
        if architectural_design is not None:
            input_["architectural_design"] = architectural_design
        if review_owner is not None:
            input_["review_owner"] = review_owner
        if is_review_owner_update_acknowledged is not None:
            input_["is_review_owner_update_acknowledged"] = (
                is_review_owner_update_acknowledged
            )
        if industry_type is not None:
            input_["industry_type"] = industry_type
        if industry is not None:
            input_["industry"] = industry
        if notes is not None:
            input_["notes"] = notes
        if improvement_status is not None:
            input_["improvement_status"] = improvement_status
        if discovery_config is not None:
            input_["discovery_config"] = discovery_config
        if applications is not None:
            input_["applications"] = applications
        if jira_configuration is not None:
            input_["jira_configuration"] = jira_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_workload_share(
        self,
        share_id: "aws_sdk_wellarchitected.types.share_id.ShareId",
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        permission_type: "aws_sdk_wellarchitected.types.permission_type.PermissionType",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
    ) -> "aws_sdk_wellarchitected.types.update_workload_share_output.UpdateWorkloadShareOutput":
        """<p>Update a workload share.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.update_workload_share_input.UpdateWorkloadShareInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wellarchitected.types.update_workload_share_output.UpdateWorkloadShareOutput"
        ]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_workload_share

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.update_workload_share.async_update_workload_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.update_workload_share_input.UpdateWorkloadShareInput = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id
        input_["workload_id"] = workload_id
        input_["permission_type"] = permission_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def upgrade_lens_review(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        milestone_name: "aws_sdk_wellarchitected.types.milestone_name.MilestoneName",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Upgrade lens review for a particular workload.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.upgrade_lens_review_input.UpgradeLensReviewInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.upgrade_lens_review

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.upgrade_lens_review.async_upgrade_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.upgrade_lens_review_input.UpgradeLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        input_["milestone_name"] = milestone_name
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def upgrade_profile_version(
        self,
        workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId",
        profile_arn: "aws_sdk_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        milestone_name: Optional[
            "aws_sdk_wellarchitected.types.milestone_name.MilestoneName"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Upgrade a profile.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.upgrade_profile_version_input.UpgradeProfileVersionInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.upgrade_profile_version

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.upgrade_profile_version.async_upgrade_profile_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.upgrade_profile_version_input.UpgradeProfileVersionInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["profile_arn"] = profile_arn
        if milestone_name is not None:
            input_["milestone_name"] = milestone_name
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def upgrade_review_template_lens_review(
        self,
        template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[AsyncWellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Upgrade the lens review of a review template.</p>

        Args:
            template_arn: <p>The ARN of the review template.</p>

        Raises:
            aws_sdk_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            aws_sdk_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            aws_sdk_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            aws_sdk_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            aws_sdk_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            aws_sdk_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wellarchitected.types.upgrade_review_template_lens_review_input.UpgradeReviewTemplateLensReviewInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.upgrade_review_template_lens_review

            (
                output,
                http_response,
            ) = await aws_sdk_wellarchitected._operations.well_architected_api_service_lambda.upgrade_review_template_lens_review.async_upgrade_review_template_lens_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_wellarchitected.types.upgrade_review_template_lens_review_input.UpgradeReviewTemplateLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

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
