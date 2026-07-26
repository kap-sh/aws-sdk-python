"""Generated from Smithy shape ``com.amazonaws.wellarchitected#WellArchitectedApiServiceLambda``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_wellarchitected._auth._signers
import capo_wellarchitected._auth._sigv4
from capo_wellarchitected._auth._identity import Credentials
from capo_wellarchitected._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_wellarchitected._auth._zapros_handler import AuthMiddleware
from capo_wellarchitected._services._aws_config import aws_config
from capo_wellarchitected._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_wellarchitected.types.account_jira_configuration_input
    import capo_wellarchitected.types.answer_reason
    import capo_wellarchitected.types.associate_lenses_input
    import capo_wellarchitected.types.associate_profiles_input
    import capo_wellarchitected.types.choice_id
    import capo_wellarchitected.types.choice_updates
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.create_lens_share_input
    import capo_wellarchitected.types.create_lens_share_output
    import capo_wellarchitected.types.create_lens_version_input
    import capo_wellarchitected.types.create_lens_version_output
    import capo_wellarchitected.types.create_milestone_input
    import capo_wellarchitected.types.create_milestone_output
    import capo_wellarchitected.types.create_profile_input
    import capo_wellarchitected.types.create_profile_output
    import capo_wellarchitected.types.create_profile_share_input
    import capo_wellarchitected.types.create_profile_share_output
    import capo_wellarchitected.types.create_review_template_input
    import capo_wellarchitected.types.create_review_template_output
    import capo_wellarchitected.types.create_template_share_input
    import capo_wellarchitected.types.create_template_share_output
    import capo_wellarchitected.types.create_workload_input
    import capo_wellarchitected.types.create_workload_output
    import capo_wellarchitected.types.create_workload_share_input
    import capo_wellarchitected.types.create_workload_share_output
    import capo_wellarchitected.types.delete_lens_input
    import capo_wellarchitected.types.delete_lens_share_input
    import capo_wellarchitected.types.delete_profile_input
    import capo_wellarchitected.types.delete_profile_share_input
    import capo_wellarchitected.types.delete_review_template_input
    import capo_wellarchitected.types.delete_template_share_input
    import capo_wellarchitected.types.delete_workload_input
    import capo_wellarchitected.types.delete_workload_share_input
    import capo_wellarchitected.types.disassociate_lenses_input
    import capo_wellarchitected.types.disassociate_profiles_input
    import capo_wellarchitected.types.discovery_integration_status
    import capo_wellarchitected.types.export_lens_input
    import capo_wellarchitected.types.export_lens_output
    import capo_wellarchitected.types.get_answer_input
    import capo_wellarchitected.types.get_answer_output
    import capo_wellarchitected.types.get_consolidated_report_input
    import capo_wellarchitected.types.get_consolidated_report_max_results
    import capo_wellarchitected.types.get_consolidated_report_output
    import capo_wellarchitected.types.get_global_settings_output
    import capo_wellarchitected.types.get_lens_input
    import capo_wellarchitected.types.get_lens_output
    import capo_wellarchitected.types.get_lens_review_input
    import capo_wellarchitected.types.get_lens_review_output
    import capo_wellarchitected.types.get_lens_review_report_input
    import capo_wellarchitected.types.get_lens_review_report_output
    import capo_wellarchitected.types.get_lens_version_difference_input
    import capo_wellarchitected.types.get_lens_version_difference_output
    import capo_wellarchitected.types.get_milestone_input
    import capo_wellarchitected.types.get_milestone_output
    import capo_wellarchitected.types.get_profile_input
    import capo_wellarchitected.types.get_profile_output
    import capo_wellarchitected.types.get_profile_template_input
    import capo_wellarchitected.types.get_profile_template_output
    import capo_wellarchitected.types.get_review_template_answer_input
    import capo_wellarchitected.types.get_review_template_answer_output
    import capo_wellarchitected.types.get_review_template_input
    import capo_wellarchitected.types.get_review_template_lens_review_input
    import capo_wellarchitected.types.get_review_template_lens_review_output
    import capo_wellarchitected.types.get_review_template_output
    import capo_wellarchitected.types.get_workload_input
    import capo_wellarchitected.types.get_workload_output
    import capo_wellarchitected.types.import_lens_input
    import capo_wellarchitected.types.import_lens_output
    import capo_wellarchitected.types.include_shared_resources
    import capo_wellarchitected.types.integrating_service
    import capo_wellarchitected.types.is_applicable
    import capo_wellarchitected.types.is_major_version
    import capo_wellarchitected.types.is_review_owner_update_acknowledged
    import capo_wellarchitected.types.jira_selected_question_configuration
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.lens_aliases
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.lens_json
    import capo_wellarchitected.types.lens_name
    import capo_wellarchitected.types.lens_name_prefix
    import capo_wellarchitected.types.lens_status_type
    import capo_wellarchitected.types.lens_type
    import capo_wellarchitected.types.lens_version
    import capo_wellarchitected.types.list_answers_input
    import capo_wellarchitected.types.list_answers_max_results
    import capo_wellarchitected.types.list_answers_output
    import capo_wellarchitected.types.list_check_details_input
    import capo_wellarchitected.types.list_check_details_output
    import capo_wellarchitected.types.list_check_summaries_input
    import capo_wellarchitected.types.list_check_summaries_output
    import capo_wellarchitected.types.list_lens_review_improvements_input
    import capo_wellarchitected.types.list_lens_review_improvements_max_results
    import capo_wellarchitected.types.list_lens_review_improvements_output
    import capo_wellarchitected.types.list_lens_reviews_input
    import capo_wellarchitected.types.list_lens_reviews_output
    import capo_wellarchitected.types.list_lens_shares_input
    import capo_wellarchitected.types.list_lens_shares_output
    import capo_wellarchitected.types.list_lenses_input
    import capo_wellarchitected.types.list_lenses_output
    import capo_wellarchitected.types.list_milestones_input
    import capo_wellarchitected.types.list_milestones_output
    import capo_wellarchitected.types.list_notifications_input
    import capo_wellarchitected.types.list_notifications_max_results
    import capo_wellarchitected.types.list_notifications_output
    import capo_wellarchitected.types.list_profile_notifications_input
    import capo_wellarchitected.types.list_profile_notifications_output
    import capo_wellarchitected.types.list_profile_shares_input
    import capo_wellarchitected.types.list_profile_shares_max_results
    import capo_wellarchitected.types.list_profile_shares_output
    import capo_wellarchitected.types.list_profiles_input
    import capo_wellarchitected.types.list_profiles_output
    import capo_wellarchitected.types.list_review_template_answers_input
    import capo_wellarchitected.types.list_review_template_answers_max_results
    import capo_wellarchitected.types.list_review_template_answers_output
    import capo_wellarchitected.types.list_review_templates_input
    import capo_wellarchitected.types.list_review_templates_output
    import capo_wellarchitected.types.list_share_invitations_input
    import capo_wellarchitected.types.list_share_invitations_max_results
    import capo_wellarchitected.types.list_share_invitations_output
    import capo_wellarchitected.types.list_tags_for_resource_input
    import capo_wellarchitected.types.list_tags_for_resource_output
    import capo_wellarchitected.types.list_template_shares_input
    import capo_wellarchitected.types.list_template_shares_max_results
    import capo_wellarchitected.types.list_template_shares_output
    import capo_wellarchitected.types.list_workload_shares_input
    import capo_wellarchitected.types.list_workload_shares_max_results
    import capo_wellarchitected.types.list_workload_shares_output
    import capo_wellarchitected.types.list_workloads_input
    import capo_wellarchitected.types.list_workloads_max_results
    import capo_wellarchitected.types.list_workloads_output
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.milestone_name
    import capo_wellarchitected.types.milestone_number
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.organization_sharing_status
    import capo_wellarchitected.types.permission_type
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.pillar_notes
    import capo_wellarchitected.types.profile_arn
    import capo_wellarchitected.types.profile_arns
    import capo_wellarchitected.types.profile_description
    import capo_wellarchitected.types.profile_name
    import capo_wellarchitected.types.profile_name_prefix
    import capo_wellarchitected.types.profile_owner_type
    import capo_wellarchitected.types.profile_question_updates
    import capo_wellarchitected.types.profile_version
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.question_priority
    import capo_wellarchitected.types.report_format
    import capo_wellarchitected.types.resource_arn
    import capo_wellarchitected.types.review_template_arns
    import capo_wellarchitected.types.review_template_lens_aliases
    import capo_wellarchitected.types.review_template_lenses
    import capo_wellarchitected.types.selected_choices
    import capo_wellarchitected.types.share_id
    import capo_wellarchitected.types.share_invitation_action
    import capo_wellarchitected.types.share_invitation_id
    import capo_wellarchitected.types.share_resource_type
    import capo_wellarchitected.types.share_status
    import capo_wellarchitected.types.shared_with
    import capo_wellarchitected.types.shared_with_prefix
    import capo_wellarchitected.types.tag_key_list
    import capo_wellarchitected.types.tag_map
    import capo_wellarchitected.types.tag_resource_input
    import capo_wellarchitected.types.tag_resource_output
    import capo_wellarchitected.types.template_arn
    import capo_wellarchitected.types.template_description
    import capo_wellarchitected.types.template_name
    import capo_wellarchitected.types.template_name_prefix
    import capo_wellarchitected.types.untag_resource_input
    import capo_wellarchitected.types.untag_resource_output
    import capo_wellarchitected.types.update_answer_input
    import capo_wellarchitected.types.update_answer_output
    import capo_wellarchitected.types.update_global_settings_input
    import capo_wellarchitected.types.update_integration_input
    import capo_wellarchitected.types.update_lens_review_input
    import capo_wellarchitected.types.update_lens_review_output
    import capo_wellarchitected.types.update_profile_input
    import capo_wellarchitected.types.update_profile_output
    import capo_wellarchitected.types.update_review_template_answer_input
    import capo_wellarchitected.types.update_review_template_answer_output
    import capo_wellarchitected.types.update_review_template_input
    import capo_wellarchitected.types.update_review_template_lens_review_input
    import capo_wellarchitected.types.update_review_template_lens_review_output
    import capo_wellarchitected.types.update_review_template_output
    import capo_wellarchitected.types.update_share_invitation_input
    import capo_wellarchitected.types.update_share_invitation_output
    import capo_wellarchitected.types.update_workload_input
    import capo_wellarchitected.types.update_workload_output
    import capo_wellarchitected.types.update_workload_share_input
    import capo_wellarchitected.types.update_workload_share_output
    import capo_wellarchitected.types.upgrade_lens_review_input
    import capo_wellarchitected.types.upgrade_profile_version_input
    import capo_wellarchitected.types.upgrade_review_template_lens_review_input
    import capo_wellarchitected.types.workload_account_ids
    import capo_wellarchitected.types.workload_applications
    import capo_wellarchitected.types.workload_architectural_design
    import capo_wellarchitected.types.workload_arn
    import capo_wellarchitected.types.workload_aws_regions
    import capo_wellarchitected.types.workload_description
    import capo_wellarchitected.types.workload_discovery_config
    import capo_wellarchitected.types.workload_environment
    import capo_wellarchitected.types.workload_id
    import capo_wellarchitected.types.workload_improvement_status
    import capo_wellarchitected.types.workload_industry
    import capo_wellarchitected.types.workload_industry_type
    import capo_wellarchitected.types.workload_jira_configuration_input
    import capo_wellarchitected.types.workload_lenses
    import capo_wellarchitected.types.workload_name
    import capo_wellarchitected.types.workload_name_prefix
    import capo_wellarchitected.types.workload_non_aws_regions
    import capo_wellarchitected.types.workload_pillar_priorities
    import capo_wellarchitected.types.workload_profile_arns
    import capo_wellarchitected.types.workload_review_owner


class WellArchitectedClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class WellArchitectedClient:
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
        self._config = WellArchitectedClientConfig(
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
        self, config_overrides: Optional[WellArchitectedClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WellArchitectedClientConfig = config_overrides or {}
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

    def associate_lenses(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_aliases: "capo_wellarchitected.types.lens_aliases.LensAliases",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Associate a lens to a workload.</p> <p>Up to 10 lenses can be associated with a workload in a single API operation. A maximum of 20 lenses can be associated with a workload.</p> <note> <p> <b>Disclaimer</b> </p> <p>By accessing and/or applying custom lenses created by another Amazon Web Services user or account, you acknowledge that custom lenses created by other users and shared with you are Third Party Content as defined in the Amazon Web Services Customer Agreement. </p> </note>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.associate_lenses_input.AssociateLensesInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.associate_lenses

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.associate_lenses.associate_lenses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.associate_lenses_input.AssociateLensesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_aliases"] = lens_aliases

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_profiles(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        profile_arns: "capo_wellarchitected.types.profile_arns.ProfileArns",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Associate a profile with a workload.</p>

        Args:
            profile_arns: <p>The list of profile ARNs to associate with the workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.associate_profiles_input.AssociateProfilesInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.associate_profiles

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.associate_profiles.associate_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.associate_profiles_input.AssociateProfilesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["profile_arns"] = profile_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_lens_share(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        shared_with: "capo_wellarchitected.types.shared_with.SharedWith",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.create_lens_share_output.CreateLensShareOutput":
        r"""<p>Create a lens share.</p> <p>The owner of a lens can share it with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. Lenses provided by Amazon Web Services (Amazon Web Services Official Content) cannot be shared.</p> <p> Shared access to a lens is not removed until the lens invitation is deleted.</p> <p>If you share a lens with an organization or OU, all accounts in the organization or OU are granted access to the lens.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-sharing.html\">Sharing a custom lens</a> in the <i>Well-Architected Tool User Guide</i>.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.create_lens_share_input.CreateLensShareInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.create_lens_share_output.CreateLensShareOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_lens_share

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.create_lens_share.create_lens_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_lens_share_input.CreateLensShareInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        input_["shared_with"] = shared_with
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_lens_version(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        lens_version: "capo_wellarchitected.types.lens_version.LensVersion",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        is_major_version: Optional[
            "capo_wellarchitected.types.is_major_version.IsMajorVersion"
        ] = None,
    ) -> (
        "capo_wellarchitected.types.create_lens_version_output.CreateLensVersionOutput"
    ):
        """<p>Create a new lens version.</p> <p>A lens can have up to 100 versions.</p> <p>Use this operation to publish a new lens version after you have imported a lens. The <code>LensAlias</code> is used to identify the lens to be published. The owner of a lens can share the lens with other Amazon Web Services accounts and users in the same Amazon Web Services Region. Only the owner of a lens can delete it. </p>

        Args:
            lens_version: <p>The version of the lens being created.</p>
            is_major_version: <p>Set to true if this new major lens version.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.create_lens_version_input.CreateLensVersionInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.create_lens_version_output.CreateLensVersionOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_lens_version

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.create_lens_version.create_lens_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_lens_version_input.CreateLensVersionInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        input_["lens_version"] = lens_version
        if is_major_version is not None:
            input_["is_major_version"] = is_major_version
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_milestone(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        milestone_name: "capo_wellarchitected.types.milestone_name.MilestoneName",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.create_milestone_output.CreateMilestoneOutput":
        """<p>Create a milestone for an existing workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.create_milestone_input.CreateMilestoneInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.create_milestone_output.CreateMilestoneOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_milestone

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.create_milestone.create_milestone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_milestone_input.CreateMilestoneInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["milestone_name"] = milestone_name
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_profile(
        self,
        profile_name: "capo_wellarchitected.types.profile_name.ProfileName",
        profile_description: "capo_wellarchitected.types.profile_description.ProfileDescription",
        profile_questions: "capo_wellarchitected.types.profile_question_updates.ProfileQuestionUpdates",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        tags: Optional["capo_wellarchitected.types.tag_map.TagMap"] = None,
    ) -> "capo_wellarchitected.types.create_profile_output.CreateProfileOutput":
        """<p>Create a profile.</p>

        Args:
            profile_name: <p>Name of the profile.</p>
            profile_description: <p>The profile description.</p>
            profile_questions: <p>The profile questions.</p>
            tags: <p>The tags assigned to the profile.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.create_profile_input.CreateProfileInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.create_profile_output.CreateProfileOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_profile

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.create_profile.create_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_profile_input.CreateProfileInput = {}  # type: ignore[typeddict-item]
        input_["profile_name"] = profile_name
        input_["profile_description"] = profile_description
        input_["profile_questions"] = profile_questions
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_profile_share(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        shared_with: "capo_wellarchitected.types.shared_with.SharedWith",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.create_profile_share_output.CreateProfileShareOutput":
        """<p>Create a profile share.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.create_profile_share_input.CreateProfileShareInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.create_profile_share_output.CreateProfileShareOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_profile_share

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.create_profile_share.create_profile_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_profile_share_input.CreateProfileShareInput = {}  # type: ignore[typeddict-item]
        input_["profile_arn"] = profile_arn
        input_["shared_with"] = shared_with
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_review_template(
        self,
        template_name: "capo_wellarchitected.types.template_name.TemplateName",
        description: "capo_wellarchitected.types.template_description.TemplateDescription",
        lenses: "capo_wellarchitected.types.review_template_lenses.ReviewTemplateLenses",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        tags: Optional["capo_wellarchitected.types.tag_map.TagMap"] = None,
    ) -> "capo_wellarchitected.types.create_review_template_output.CreateReviewTemplateOutput":
        """<p>Create a review template.</p> <note> <p> <b>Disclaimer</b> </p> <p>Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your review templates. If your review template or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.</p> </note>

        Args:
            template_name: <p>Name of the review template.</p>
            description: <p>The review template description.</p>
            lenses: <p>Lenses applied to the review template.</p>
            tags: <p>The tags assigned to the review template.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.create_review_template_input.CreateReviewTemplateInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.create_review_template_output.CreateReviewTemplateOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_review_template

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.create_review_template.create_review_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_review_template_input.CreateReviewTemplateInput = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        input_["description"] = description
        input_["lenses"] = lenses
        if notes is not None:
            input_["notes"] = notes
        if tags is not None:
            input_["tags"] = tags
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_template_share(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        shared_with: "capo_wellarchitected.types.shared_with.SharedWith",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.create_template_share_output.CreateTemplateShareOutput":
        """<p>Create a review template share.</p> <p>The owner of a review template can share it with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. </p> <p> Shared access to a review template is not removed until the review template share invitation is deleted.</p> <p>If you share a review template with an organization or OU, all accounts in the organization or OU are granted access to the review template.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your review template with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your review template available to those other accounts.</p> </note>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.create_template_share_input.CreateTemplateShareInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.create_template_share_output.CreateTemplateShareOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_template_share

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.create_template_share.create_template_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_template_share_input.CreateTemplateShareInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["shared_with"] = shared_with
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_workload(
        self,
        workload_name: "capo_wellarchitected.types.workload_name.WorkloadName",
        description: "capo_wellarchitected.types.workload_description.WorkloadDescription",
        environment: "capo_wellarchitected.types.workload_environment.WorkloadEnvironment",
        lenses: "capo_wellarchitected.types.workload_lenses.WorkloadLenses",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        account_ids: Optional[
            "capo_wellarchitected.types.workload_account_ids.WorkloadAccountIds"
        ] = None,
        aws_regions: Optional[
            "capo_wellarchitected.types.workload_aws_regions.WorkloadAwsRegions"
        ] = None,
        non_aws_regions: Optional[
            "capo_wellarchitected.types.workload_non_aws_regions.WorkloadNonAwsRegions"
        ] = None,
        pillar_priorities: Optional[
            "capo_wellarchitected.types.workload_pillar_priorities.WorkloadPillarPriorities"
        ] = None,
        architectural_design: Optional[
            "capo_wellarchitected.types.workload_architectural_design.WorkloadArchitecturalDesign"
        ] = None,
        review_owner: Optional[
            "capo_wellarchitected.types.workload_review_owner.WorkloadReviewOwner"
        ] = None,
        industry_type: Optional[
            "capo_wellarchitected.types.workload_industry_type.WorkloadIndustryType"
        ] = None,
        industry: Optional[
            "capo_wellarchitected.types.workload_industry.WorkloadIndustry"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        tags: Optional["capo_wellarchitected.types.tag_map.TagMap"] = None,
        discovery_config: Optional[
            "capo_wellarchitected.types.workload_discovery_config.WorkloadDiscoveryConfig"
        ] = None,
        applications: Optional[
            "capo_wellarchitected.types.workload_applications.WorkloadApplications"
        ] = None,
        profile_arns: Optional[
            "capo_wellarchitected.types.workload_profile_arns.WorkloadProfileArns"
        ] = None,
        review_template_arns: Optional[
            "capo_wellarchitected.types.review_template_arns.ReviewTemplateArns"
        ] = None,
        jira_configuration: Optional[
            "capo_wellarchitected.types.workload_jira_configuration_input.WorkloadJiraConfigurationInput"
        ] = None,
    ) -> "capo_wellarchitected.types.create_workload_output.CreateWorkloadOutput":
        r"""<p>Create a new workload.</p> <p>The owner of a workload can share the workload with other Amazon Web Services accounts, users, an organization, and organizational units (OUs) in the same Amazon Web Services Region. Only the owner of a workload can delete it.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/wellarchitected/latest/userguide/define-workload.html\">Defining a Workload</a> in the <i>Well-Architected Tool User Guide</i>.</p> <important> <p>Either <code>AwsRegions</code>, <code>NonAwsRegions</code>, or both must be specified when creating a workload.</p> <p>You also must specify <code>ReviewOwner</code>, even though the parameter is listed as not being required in the following section. </p> </important> <p>When creating a workload using a review template, you must have the following IAM permissions:</p> <ul> <li> <p> <code>wellarchitected:GetReviewTemplate</code> </p> </li> <li> <p> <code>wellarchitected:GetReviewTemplateAnswer</code> </p> </li> <li> <p> <code>wellarchitected:ListReviewTemplateAnswers</code> </p> </li> <li> <p> <code>wellarchitected:GetReviewTemplateLensReview</code> </p> </li> </ul>

        Args:
            tags: <p>The tags to be associated with the workload.</p>
            discovery_config: <p>Well-Architected discovery configuration settings associated to the workload.</p>
            applications: <p>List of AppRegistry application ARNs associated to the workload.</p>
            profile_arns: <p>The list of profile ARNs associated with the workload.</p>
            review_template_arns: <p>The list of review template ARNs to associate with the workload.</p>
            jira_configuration: <p>Jira configuration settings when creating a workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.create_workload_input.CreateWorkloadInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.create_workload_output.CreateWorkloadOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_workload

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.create_workload.create_workload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_workload_input.CreateWorkloadInput = {}  # type: ignore[typeddict-item]
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_workload_share(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        shared_with: "capo_wellarchitected.types.shared_with.SharedWith",
        permission_type: "capo_wellarchitected.types.permission_type.PermissionType",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.create_workload_share_output.CreateWorkloadShareOutput":
        r"""<p>Create a workload share.</p> <p>The owner of a workload can share it with other Amazon Web Services accounts and users in the same Amazon Web Services Region. Shared access to a workload is not removed until the workload invitation is deleted.</p> <p>If you share a workload with an organization or OU, all accounts in the organization or OU are granted access to the workload.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-sharing.html\">Sharing a workload</a> in the <i>Well-Architected Tool User Guide</i>.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.create_workload_share_input.CreateWorkloadShareInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.create_workload_share_output.CreateWorkloadShareOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.create_workload_share

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.create_workload_share.create_workload_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.create_workload_share_input.CreateWorkloadShareInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["shared_with"] = shared_with
        input_["permission_type"] = permission_type
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_lens(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        lens_status: "capo_wellarchitected.types.lens_status_type.LensStatusType",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete an existing lens.</p> <p>Only the owner of a lens can delete it. After the lens is deleted, Amazon Web Services accounts and users that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads. </p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Args:
            lens_status: <p>The status of the lens to be deleted.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.delete_lens_input.DeleteLensInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_lens

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.delete_lens.delete_lens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_lens_input.DeleteLensInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        input_["client_request_token"] = client_request_token
        input_["lens_status"] = lens_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_lens_share(
        self,
        share_id: "capo_wellarchitected.types.share_id.ShareId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a lens share.</p> <p>After the lens share is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the lens with can continue to use it, but they will no longer be able to apply it to new workloads.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your custom lenses with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your custom lenses available to those other accounts. Those other accounts may continue to access and use your shared custom lenses even if you delete the custom lenses from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.delete_lens_share_input.DeleteLensShareInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_lens_share

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.delete_lens_share.delete_lens_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_lens_share_input.DeleteLensShareInput = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id
        input_["lens_alias"] = lens_alias
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_profile(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a profile.</p> <note> <p> <b>Disclaimer</b> </p> <p>By sharing your profile with other Amazon Web Services accounts, you acknowledge that Amazon Web Services will make your profile available to those other accounts. Those other accounts may continue to access and use your shared profile even if you delete the profile from your own Amazon Web Services account or terminate your Amazon Web Services account.</p> </note>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.delete_profile_input.DeleteProfileInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_profile

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.delete_profile.delete_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_profile_input.DeleteProfileInput = {}  # type: ignore[typeddict-item]
        input_["profile_arn"] = profile_arn
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_profile_share(
        self,
        share_id: "capo_wellarchitected.types.share_id.ShareId",
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a profile share.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.delete_profile_share_input.DeleteProfileShareInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_profile_share

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.delete_profile_share.delete_profile_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_profile_share_input.DeleteProfileShareInput = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id
        input_["profile_arn"] = profile_arn
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_review_template(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a review template.</p> <p>Only the owner of a review template can delete it.</p> <p>After the review template is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the review template with will no longer be able to apply it to new workloads.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.delete_review_template_input.DeleteReviewTemplateInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_review_template

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.delete_review_template.delete_review_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_review_template_input.DeleteReviewTemplateInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_template_share(
        self,
        share_id: "capo_wellarchitected.types.share_id.ShareId",
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a review template share.</p> <p>After the review template share is deleted, Amazon Web Services accounts, users, organizations, and organizational units (OUs) that you shared the review template with will no longer be able to apply it to new workloads.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.delete_template_share_input.DeleteTemplateShareInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_template_share

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.delete_template_share.delete_template_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_template_share_input.DeleteTemplateShareInput = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id
        input_["template_arn"] = template_arn
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_workload(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete an existing workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.delete_workload_input.DeleteWorkloadInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_workload

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.delete_workload.delete_workload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_workload_input.DeleteWorkloadInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_workload_share(
        self,
        share_id: "capo_wellarchitected.types.share_id.ShareId",
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Delete a workload share.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.delete_workload_share_input.DeleteWorkloadShareInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.delete_workload_share

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.delete_workload_share.delete_workload_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.delete_workload_share_input.DeleteWorkloadShareInput = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id
        input_["workload_id"] = workload_id
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_lenses(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_aliases: "capo_wellarchitected.types.lens_aliases.LensAliases",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Disassociate a lens from a workload.</p> <p>Up to 10 lenses can be disassociated from a workload in a single API operation.</p> <note> <p>The Amazon Web Services Well-Architected Framework lens (<code>wellarchitected</code>) cannot be removed from a workload.</p> </note>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.disassociate_lenses_input.DisassociateLensesInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.disassociate_lenses

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.disassociate_lenses.disassociate_lenses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.disassociate_lenses_input.DisassociateLensesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_aliases"] = lens_aliases

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_profiles(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        profile_arns: "capo_wellarchitected.types.profile_arns.ProfileArns",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Disassociate a profile from a workload.</p>

        Args:
            profile_arns: <p>The list of profile ARNs to disassociate from the workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.disassociate_profiles_input.DisassociateProfilesInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.disassociate_profiles

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.disassociate_profiles.disassociate_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.disassociate_profiles_input.DisassociateProfilesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["profile_arns"] = profile_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def export_lens(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        lens_version: Optional[
            "capo_wellarchitected.types.lens_version.LensVersion"
        ] = None,
    ) -> "capo_wellarchitected.types.export_lens_output.ExportLensOutput":
        r"""<p>Export an existing lens.</p> <p>Only the owner of a lens can export it. Lenses provided by Amazon Web Services (Amazon Web Services Official Content) cannot be exported.</p> <p>Lenses are defined in JSON. For more information, see <a href=\"https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html\">JSON format specification</a> in the <i>Well-Architected Tool User Guide</i>.</p> <note> <p> <b>Disclaimer</b> </p> <p>Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.</p> </note>

        Args:
            lens_version: <p>The lens version to be exported.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.export_lens_input.ExportLensInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.export_lens_output.ExportLensOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.export_lens

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.export_lens.export_lens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.export_lens_input.ExportLensInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        if lens_version is not None:
            input_["lens_version"] = lens_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_answer(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        question_id: "capo_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
    ) -> "capo_wellarchitected.types.get_answer_output.GetAnswerOutput":
        """<p>Get the answer to a specific question in a workload review.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_answer_input.GetAnswerInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_answer_output.GetAnswerOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_answer

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_answer.get_answer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_answer_input.GetAnswerInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        input_["question_id"] = question_id
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_consolidated_report(
        self,
        format: "capo_wellarchitected.types.report_format.ReportFormat",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        include_shared_resources: Optional[
            "capo_wellarchitected.types.include_shared_resources.IncludeSharedResources"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.get_consolidated_report_max_results.GetConsolidatedReportMaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.get_consolidated_report_output.GetConsolidatedReportOutput":
        """<p>Get a consolidated report of your workloads.</p> <p>You can optionally choose to include workloads that have been shared with you.</p>

        Args:
            format: <p>The format of the consolidated report.</p> <p>For <code>PDF</code>, <code>Base64String</code> is returned. For <code>JSON</code>, <code>Metrics</code> is returned.</p>
            include_shared_resources: <p>Set to <code>true</code> to have shared resources included in the report.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_consolidated_report_input.GetConsolidatedReportInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_consolidated_report_output.GetConsolidatedReportOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_consolidated_report

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_consolidated_report.get_consolidated_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_consolidated_report_input.GetConsolidatedReportInput = {}  # type: ignore[typeddict-item]
        input_["format"] = format
        if include_shared_resources is not None:
            input_["include_shared_resources"] = include_shared_resources
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

    def get_global_settings(
        self, *, config_overrides: Optional[WellArchitectedClientConfig] = None
    ) -> (
        "capo_wellarchitected.types.get_global_settings_output.GetGlobalSettingsOutput"
    ):
        """<p>Global settings for all workloads.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_global_settings_output.GetGlobalSettingsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_global_settings

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_global_settings.get_global_settings(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_lens(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        lens_version: Optional[
            "capo_wellarchitected.types.lens_version.LensVersion"
        ] = None,
    ) -> "capo_wellarchitected.types.get_lens_output.GetLensOutput":
        """<p>Get an existing lens.</p>

        Args:
            lens_version: <p>The lens version to be retrieved.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_lens_input.GetLensInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_lens_output.GetLensOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens.get_lens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_lens_input.GetLensInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        if lens_version is not None:
            input_["lens_version"] = lens_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_lens_review(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
    ) -> "capo_wellarchitected.types.get_lens_review_output.GetLensReviewOutput":
        """<p>Get lens review.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_lens_review_input.GetLensReviewInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_lens_review_output.GetLensReviewOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review.get_lens_review(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_lens_review_input.GetLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_lens_review_report(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
    ) -> "capo_wellarchitected.types.get_lens_review_report_output.GetLensReviewReportOutput":
        """<p>Get lens review report.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_lens_review_report_input.GetLensReviewReportInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_lens_review_report_output.GetLensReviewReportOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review_report

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_review_report.get_lens_review_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_lens_review_report_input.GetLensReviewReportInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_lens_version_difference(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        base_lens_version: Optional[
            "capo_wellarchitected.types.lens_version.LensVersion"
        ] = None,
        target_lens_version: Optional[
            "capo_wellarchitected.types.lens_version.LensVersion"
        ] = None,
    ) -> "capo_wellarchitected.types.get_lens_version_difference_output.GetLensVersionDifferenceOutput":
        """<p>Get lens version differences.</p>

        Args:
            base_lens_version: <p>The base version of the lens.</p>
            target_lens_version: <p>The lens version to target a difference for.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_lens_version_difference_input.GetLensVersionDifferenceInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_lens_version_difference_output.GetLensVersionDifferenceOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_version_difference

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_lens_version_difference.get_lens_version_difference(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_lens_version_difference_input.GetLensVersionDifferenceInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        if base_lens_version is not None:
            input_["base_lens_version"] = base_lens_version
        if target_lens_version is not None:
            input_["target_lens_version"] = target_lens_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_milestone(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        milestone_number: "capo_wellarchitected.types.milestone_number.MilestoneNumber",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.get_milestone_output.GetMilestoneOutput":
        """<p>Get a milestone for an existing workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_milestone_input.GetMilestoneInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_milestone_output.GetMilestoneOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_milestone

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_milestone.get_milestone(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_milestone_input.GetMilestoneInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["milestone_number"] = milestone_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_profile(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        profile_version: Optional[
            "capo_wellarchitected.types.profile_version.ProfileVersion"
        ] = None,
    ) -> "capo_wellarchitected.types.get_profile_output.GetProfileOutput":
        """<p>Get profile information.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>
            profile_version: <p>The profile version.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_profile_input.GetProfileInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_profile_output.GetProfileOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_profile

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_profile.get_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_profile_input.GetProfileInput = {}  # type: ignore[typeddict-item]
        input_["profile_arn"] = profile_arn
        if profile_version is not None:
            input_["profile_version"] = profile_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_profile_template(
        self, *, config_overrides: Optional[WellArchitectedClientConfig] = None
    ) -> "capo_wellarchitected.types.get_profile_template_output.GetProfileTemplateOutput":
        """<p>Get profile template.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_profile_template_input.GetProfileTemplateInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_profile_template_output.GetProfileTemplateOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_profile_template

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_profile_template.get_profile_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_profile_template_input.GetProfileTemplateInput = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_review_template(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> (
        "capo_wellarchitected.types.get_review_template_output.GetReviewTemplateOutput"
    ):
        """<p>Get review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_review_template_input.GetReviewTemplateInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_review_template_output.GetReviewTemplateOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template.get_review_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_review_template_input.GetReviewTemplateInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_review_template_answer(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        question_id: "capo_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.get_review_template_answer_output.GetReviewTemplateAnswerOutput":
        """<p>Get review template answer.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_review_template_answer_input.GetReviewTemplateAnswerInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_review_template_answer_output.GetReviewTemplateAnswerOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_answer

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_answer.get_review_template_answer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_review_template_answer_input.GetReviewTemplateAnswerInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias
        input_["question_id"] = question_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_review_template_lens_review(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.get_review_template_lens_review_output.GetReviewTemplateLensReviewOutput":
        """<p>Get a lens review associated with a review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_review_template_lens_review_input.GetReviewTemplateLensReviewInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_review_template_lens_review_output.GetReviewTemplateLensReviewOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_lens_review

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_review_template_lens_review.get_review_template_lens_review(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_review_template_lens_review_input.GetReviewTemplateLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_workload(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.get_workload_output.GetWorkloadOutput":
        """<p>Get an existing workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.get_workload_input.GetWorkloadInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.get_workload_output.GetWorkloadOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.get_workload

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.get_workload.get_workload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.get_workload_input.GetWorkloadInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_lens(
        self,
        json_string: "capo_wellarchitected.types.lens_json.LensJSON",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        lens_alias: Optional["capo_wellarchitected.types.lens_alias.LensAlias"] = None,
        tags: Optional["capo_wellarchitected.types.tag_map.TagMap"] = None,
    ) -> "capo_wellarchitected.types.import_lens_output.ImportLensOutput":
        r"""<p>Import a new custom lens or update an existing custom lens.</p> <p>To update an existing custom lens, specify its ARN as the <code>LensAlias</code>. If no ARN is specified, a new custom lens is created.</p> <p>The new or updated lens will have a status of <code>DRAFT</code>. The lens cannot be applied to workloads or shared with other Amazon Web Services accounts until it's published with <a>CreateLensVersion</a>.</p> <p>Lenses are defined in JSON. For more information, see <a href=\"https://docs.aws.amazon.com/wellarchitected/latest/userguide/lenses-format-specification.html\">JSON format specification</a> in the <i>Well-Architected Tool User Guide</i>.</p> <p>A custom lens cannot exceed 500 KB in size.</p> <note> <p> <b>Disclaimer</b> </p> <p>Do not include or gather personal identifiable information (PII) of end users or other identifiable individuals in or via your custom lenses. If your custom lens or those shared with you and used in your account do include or collect PII you are responsible for: ensuring that the included PII is processed in accordance with applicable law, providing adequate privacy notices, and obtaining necessary consents for processing such data.</p> </note>

        Args:
            json_string: <p>The JSON representation of a lens.</p>
            tags: <p>Tags to associate to a lens.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.import_lens_input.ImportLensInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.import_lens_output.ImportLensOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.import_lens

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.import_lens.import_lens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.import_lens_input.ImportLensInput = {}  # type: ignore[typeddict-item]
        if lens_alias is not None:
            input_["lens_alias"] = lens_alias
        input_["json_string"] = json_string
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_answers(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.list_answers_max_results.ListAnswersMaxResults"
        ] = None,
        question_priority: Optional[
            "capo_wellarchitected.types.question_priority.QuestionPriority"
        ] = None,
    ) -> "capo_wellarchitected.types.list_answers_output.ListAnswersOutput":
        """<p>List of answers for a particular workload and lens.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>
            question_priority: <p>The priority of the question.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_answers_input.ListAnswersInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_answers_output.ListAnswersOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_answers

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_answers.list_answers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_answers_input.ListAnswersInput = {}  # type: ignore[typeddict-item]
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_check_details(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_arn: "capo_wellarchitected.types.lens_arn.LensArn",
        pillar_id: "capo_wellarchitected.types.pillar_id.PillarId",
        question_id: "capo_wellarchitected.types.question_id.QuestionId",
        choice_id: "capo_wellarchitected.types.choice_id.ChoiceId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_check_details_output.ListCheckDetailsOutput":
        """<p>List of Trusted Advisor check details by account related to the workload.</p>

        Args:
            lens_arn: <p>Well-Architected Lens ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_check_details_input.ListCheckDetailsInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_check_details_output.ListCheckDetailsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_check_details

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_check_details.list_check_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_check_details_input.ListCheckDetailsInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["lens_arn"] = lens_arn
        input_["pillar_id"] = pillar_id
        input_["question_id"] = question_id
        input_["choice_id"] = choice_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_check_summaries(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_arn: "capo_wellarchitected.types.lens_arn.LensArn",
        pillar_id: "capo_wellarchitected.types.pillar_id.PillarId",
        question_id: "capo_wellarchitected.types.question_id.QuestionId",
        choice_id: "capo_wellarchitected.types.choice_id.ChoiceId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_check_summaries_output.ListCheckSummariesOutput":
        """<p>List of Trusted Advisor checks summarized for all accounts related to the workload.</p>

        Args:
            lens_arn: <p>Well-Architected Lens ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_check_summaries_input.ListCheckSummariesInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_check_summaries_output.ListCheckSummariesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_check_summaries

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_check_summaries.list_check_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_check_summaries_input.ListCheckSummariesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["lens_arn"] = lens_arn
        input_["pillar_id"] = pillar_id
        input_["question_id"] = question_id
        input_["choice_id"] = choice_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_lenses(
        self,
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
        lens_type: Optional["capo_wellarchitected.types.lens_type.LensType"] = None,
        lens_status: Optional[
            "capo_wellarchitected.types.lens_status_type.LensStatusType"
        ] = None,
        lens_name: Optional["capo_wellarchitected.types.lens_name.LensName"] = None,
    ) -> "capo_wellarchitected.types.list_lenses_output.ListLensesOutput":
        """<p>List the available lenses.</p>

        Args:
            lens_type: <p>The type of lenses to be returned.</p>
            lens_status: <p>The status of lenses to be returned.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_lenses_input.ListLensesInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_lenses_output.ListLensesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_lenses

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_lenses.list_lenses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_lenses_input.ListLensesInput = {}  # type: ignore[typeddict-item]
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_lens_review_improvements(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.list_lens_review_improvements_max_results.ListLensReviewImprovementsMaxResults"
        ] = None,
        question_priority: Optional[
            "capo_wellarchitected.types.question_priority.QuestionPriority"
        ] = None,
    ) -> "capo_wellarchitected.types.list_lens_review_improvements_output.ListLensReviewImprovementsOutput":
        """<p>List the improvements of a particular lens review.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>
            question_priority: <p>The priority of the question.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_lens_review_improvements_input.ListLensReviewImprovementsInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_lens_review_improvements_output.ListLensReviewImprovementsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_review_improvements

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_review_improvements.list_lens_review_improvements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_lens_review_improvements_input.ListLensReviewImprovementsInput = {}  # type: ignore[typeddict-item]
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_lens_reviews(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        milestone_number: Optional[
            "capo_wellarchitected.types.milestone_number.MilestoneNumber"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_lens_reviews_output.ListLensReviewsOutput":
        """<p>List lens reviews for a particular workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_lens_reviews_input.ListLensReviewsInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_lens_reviews_output.ListLensReviewsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_reviews

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_reviews.list_lens_reviews(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_lens_reviews_input.ListLensReviewsInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        if milestone_number is not None:
            input_["milestone_number"] = milestone_number
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

    def list_lens_shares(
        self,
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.list_workload_shares_max_results.ListWorkloadSharesMaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> "capo_wellarchitected.types.list_lens_shares_output.ListLensSharesOutput":
        """<p>List the lens shares associated with the lens.</p>

        Args:
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the lens is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_lens_shares_input.ListLensSharesInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_lens_shares_output.ListLensSharesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_shares

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_lens_shares.list_lens_shares(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_lens_shares_input.ListLensSharesInput = {}  # type: ignore[typeddict-item]
        input_["lens_alias"] = lens_alias
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_milestones(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_milestones_output.ListMilestonesOutput":
        """<p>List all milestones for an existing workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_milestones_input.ListMilestonesInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_milestones_output.ListMilestonesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_milestones

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_milestones.list_milestones(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_milestones_input.ListMilestonesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
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

    def list_notifications(
        self,
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        workload_id: Optional[
            "capo_wellarchitected.types.workload_id.WorkloadId"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.list_notifications_max_results.ListNotificationsMaxResults"
        ] = None,
        resource_arn: Optional[
            "capo_wellarchitected.types.resource_arn.ResourceArn"
        ] = None,
    ) -> "capo_wellarchitected.types.list_notifications_output.ListNotificationsOutput":
        """<p>List lens notifications.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>
            resource_arn: <p>The ARN for the related resource for the notification.</p> <note> <p>Only one of <code>WorkloadID</code> or <code>ResourceARN</code> should be specified.</p> </note>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_notifications_input.ListNotificationsInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_notifications_output.ListNotificationsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_notifications

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_notifications.list_notifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_notifications_input.ListNotificationsInput = {}  # type: ignore[typeddict-item]
        if workload_id is not None:
            input_["workload_id"] = workload_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_profile_notifications(
        self,
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        workload_id: Optional[
            "capo_wellarchitected.types.workload_id.WorkloadId"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_profile_notifications_output.ListProfileNotificationsOutput":
        """<p>List profile notifications.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_profile_notifications_input.ListProfileNotificationsInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_profile_notifications_output.ListProfileNotificationsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_profile_notifications

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_profile_notifications.list_profile_notifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_profile_notifications_input.ListProfileNotificationsInput = {}  # type: ignore[typeddict-item]
        if workload_id is not None:
            input_["workload_id"] = workload_id
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

    def list_profiles(
        self,
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        profile_name_prefix: Optional[
            "capo_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
        ] = None,
        profile_owner_type: Optional[
            "capo_wellarchitected.types.profile_owner_type.ProfileOwnerType"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_profiles_output.ListProfilesOutput":
        """<p>List profiles.</p>

        Args:
            profile_name_prefix: <p>An optional string added to the beginning of each profile name returned in the results.</p>
            profile_owner_type: <p>Profile owner type.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_profiles_input.ListProfilesInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_profiles_output.ListProfilesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_profiles

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_profiles.list_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_profiles_input.ListProfilesInput = {}  # type: ignore[typeddict-item]
        if profile_name_prefix is not None:
            input_["profile_name_prefix"] = profile_name_prefix
        if profile_owner_type is not None:
            input_["profile_owner_type"] = profile_owner_type
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

    def list_profile_shares(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.list_profile_shares_max_results.ListProfileSharesMaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> (
        "capo_wellarchitected.types.list_profile_shares_output.ListProfileSharesOutput"
    ):
        """<p>List profile shares.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the profile is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_profile_shares_input.ListProfileSharesInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_profile_shares_output.ListProfileSharesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_profile_shares

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_profile_shares.list_profile_shares(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_profile_shares_input.ListProfileSharesInput = {}  # type: ignore[typeddict-item]
        input_["profile_arn"] = profile_arn
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_review_template_answers(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        pillar_id: Optional["capo_wellarchitected.types.pillar_id.PillarId"] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.list_review_template_answers_max_results.ListReviewTemplateAnswersMaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_review_template_answers_output.ListReviewTemplateAnswersOutput":
        """<p>List the answers of a review template.</p>

        Args:
            template_arn: <p>The ARN of the review template.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_review_template_answers_input.ListReviewTemplateAnswersInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_review_template_answers_output.ListReviewTemplateAnswersOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_review_template_answers

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_review_template_answers.list_review_template_answers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_review_template_answers_input.ListReviewTemplateAnswersInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias
        if pillar_id is not None:
            input_["pillar_id"] = pillar_id
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

    def list_review_templates(
        self,
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_review_templates_output.ListReviewTemplatesOutput":
        """<p>List review templates.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_review_templates_input.ListReviewTemplatesInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_review_templates_output.ListReviewTemplatesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_review_templates

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_review_templates.list_review_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_review_templates_input.ListReviewTemplatesInput = {}  # type: ignore[typeddict-item]
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

    def list_share_invitations(
        self,
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        workload_name_prefix: Optional[
            "capo_wellarchitected.types.workload_name_prefix.WorkloadNamePrefix"
        ] = None,
        lens_name_prefix: Optional[
            "capo_wellarchitected.types.lens_name_prefix.LensNamePrefix"
        ] = None,
        share_resource_type: Optional[
            "capo_wellarchitected.types.share_resource_type.ShareResourceType"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.list_share_invitations_max_results.ListShareInvitationsMaxResults"
        ] = None,
        profile_name_prefix: Optional[
            "capo_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
        ] = None,
        template_name_prefix: Optional[
            "capo_wellarchitected.types.template_name_prefix.TemplateNamePrefix"
        ] = None,
    ) -> "capo_wellarchitected.types.list_share_invitations_output.ListShareInvitationsOutput":
        """<p>List the share invitations.</p> <p> <code>WorkloadNamePrefix</code>, <code>LensNamePrefix</code>, <code>ProfileNamePrefix</code>, and <code>TemplateNamePrefix</code> are mutually exclusive. Use the parameter that matches your <code>ShareResourceType</code>.</p>

        Args:
            lens_name_prefix: <p>An optional string added to the beginning of each lens name returned in the results.</p>
            share_resource_type: <p>The type of share invitations to be returned.</p>
            max_results: <p>The maximum number of results to return for this request.</p>
            profile_name_prefix: <p>An optional string added to the beginning of each profile name returned in the results.</p>
            template_name_prefix: <p>An optional string added to the beginning of each review template name returned in the results.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_share_invitations_input.ListShareInvitationsInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_share_invitations_output.ListShareInvitationsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_share_invitations

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_share_invitations.list_share_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_share_invitations_input.ListShareInvitationsInput = {}  # type: ignore[typeddict-item]
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        workload_arn: "capo_wellarchitected.types.workload_arn.WorkloadArn",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List the tags for a resource.</p> <note> <p>The WorkloadArn parameter can be a workload ARN, a custom lens ARN, a profile ARN, or review template ARN.</p> </note>

        Raises:
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_tags_for_resource

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["workload_arn"] = workload_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_template_shares(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.list_template_shares_max_results.ListTemplateSharesMaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> "capo_wellarchitected.types.list_template_shares_output.ListTemplateSharesOutput":
        """<p>List review template shares.</p>

        Args:
            template_arn: <p>The review template ARN.</p>
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the profile is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_template_shares_input.ListTemplateSharesInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_template_shares_output.ListTemplateSharesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_template_shares

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_template_shares.list_template_shares(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_template_shares_input.ListTemplateSharesInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_workloads(
        self,
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        workload_name_prefix: Optional[
            "capo_wellarchitected.types.workload_name_prefix.WorkloadNamePrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.list_workloads_max_results.ListWorkloadsMaxResults"
        ] = None,
    ) -> "capo_wellarchitected.types.list_workloads_output.ListWorkloadsOutput":
        """<p>Paginated list of workloads.</p>

        Args:
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_workloads_input.ListWorkloadsInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_workloads_output.ListWorkloadsOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_workloads

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_workloads.list_workloads(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_workloads_input.ListWorkloadsInput = {}  # type: ignore[typeddict-item]
        if workload_name_prefix is not None:
            input_["workload_name_prefix"] = workload_name_prefix
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

    def list_workload_shares(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        shared_with_prefix: Optional[
            "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
        ] = None,
        next_token: Optional["capo_wellarchitected.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_wellarchitected.types.list_workload_shares_max_results.ListWorkloadSharesMaxResults"
        ] = None,
        status: Optional["capo_wellarchitected.types.share_status.ShareStatus"] = None,
    ) -> "capo_wellarchitected.types.list_workload_shares_output.ListWorkloadSharesOutput":
        """<p>List the workload shares associated with the workload.</p>

        Args:
            shared_with_prefix: <p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the workload is shared.</p>
            max_results: <p>The maximum number of results to return for this request.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.list_workload_shares_input.ListWorkloadSharesInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.list_workload_shares_output.ListWorkloadSharesOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.list_workload_shares

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.list_workload_shares.list_workload_shares(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.list_workload_shares_input.ListWorkloadSharesInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        if shared_with_prefix is not None:
            input_["shared_with_prefix"] = shared_with_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        workload_arn: "capo_wellarchitected.types.workload_arn.WorkloadArn",
        tags: "capo_wellarchitected.types.tag_map.TagMap",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.tag_resource_output.TagResourceOutput":
        """<p>Adds one or more tags to the specified resource.</p> <note> <p>The WorkloadArn parameter can be a workload ARN, a custom lens ARN, a profile ARN, or review template ARN.</p> </note>

        Args:
            tags: <p>The tags for the resource.</p>

        Raises:
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.tag_resource

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["workload_arn"] = workload_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        workload_arn: "capo_wellarchitected.types.workload_arn.WorkloadArn",
        tag_keys: "capo_wellarchitected.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.untag_resource_output.UntagResourceOutput":
        """<p>Deletes specified tags from a resource.</p> <note> <p>The WorkloadArn parameter can be a workload ARN, a custom lens ARN, a profile ARN, or review template ARN.</p> </note> <p>To specify multiple tags, use separate <b>tagKeys</b> parameters, for example:</p> <p> <code>DELETE /tags/WorkloadArn?tagKeys=key1&tagKeys=key2</code> </p>

        Args:
            tag_keys: <p>A list of tag keys. Existing tags of the resource whose keys are members of this list are removed from the resource.</p>

        Raises:
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.untag_resource

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["workload_arn"] = workload_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_answer(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        question_id: "capo_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        selected_choices: Optional[
            "capo_wellarchitected.types.selected_choices.SelectedChoices"
        ] = None,
        choice_updates: Optional[
            "capo_wellarchitected.types.choice_updates.ChoiceUpdates"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        is_applicable: Optional[
            "capo_wellarchitected.types.is_applicable.IsApplicable"
        ] = None,
        reason: Optional[
            "capo_wellarchitected.types.answer_reason.AnswerReason"
        ] = None,
    ) -> "capo_wellarchitected.types.update_answer_output.UpdateAnswerOutput":
        """<p>Update the answer to a specific question in a workload review.</p>

        Args:
            choice_updates: <p>A list of choices to update on a question in your workload. The String key corresponds to the choice ID to be updated.</p>
            reason: <p>The reason why a question is not applicable to your workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_answer_input.UpdateAnswerInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.update_answer_output.UpdateAnswerOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_answer

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_answer.update_answer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_answer_input.UpdateAnswerInput = {}  # type: ignore[typeddict-item]
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_global_settings(
        self,
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        organization_sharing_status: Optional[
            "capo_wellarchitected.types.organization_sharing_status.OrganizationSharingStatus"
        ] = None,
        discovery_integration_status: Optional[
            "capo_wellarchitected.types.discovery_integration_status.DiscoveryIntegrationStatus"
        ] = None,
        jira_configuration: Optional[
            "capo_wellarchitected.types.account_jira_configuration_input.AccountJiraConfigurationInput"
        ] = None,
    ) -> None:
        """<p>Update whether the Amazon Web Services account is opted into organization sharing and discovery integration features.</p>

        Args:
            organization_sharing_status: <p>The status of organization sharing settings.</p>
            discovery_integration_status: <p>The status of discovery support settings.</p>
            jira_configuration: <p>The status of Jira integration settings.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_global_settings_input.UpdateGlobalSettingsInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_global_settings

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_global_settings.update_global_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_global_settings_input.UpdateGlobalSettingsInput = {}  # type: ignore[typeddict-item]
        if organization_sharing_status is not None:
            input_["organization_sharing_status"] = organization_sharing_status
        if discovery_integration_status is not None:
            input_["discovery_integration_status"] = discovery_integration_status
        if jira_configuration is not None:
            input_["jira_configuration"] = jira_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_integration(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        client_request_token: "capo_wellarchitected.types.client_request_token.ClientRequestToken",
        integrating_service: "capo_wellarchitected.types.integrating_service.IntegratingService",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> None:
        """<p>Update integration features.</p>

        Args:
            integrating_service: <p>Which integrated service to update.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_integration_input.UpdateIntegrationInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_integration

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_integration.update_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_integration_input.UpdateIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["client_request_token"] = client_request_token
        input_["integrating_service"] = integrating_service

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_lens_review(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        lens_notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        pillar_notes: Optional[
            "capo_wellarchitected.types.pillar_notes.PillarNotes"
        ] = None,
        jira_configuration: Optional[
            "capo_wellarchitected.types.jira_selected_question_configuration.JiraSelectedQuestionConfiguration"
        ] = None,
    ) -> "capo_wellarchitected.types.update_lens_review_output.UpdateLensReviewOutput":
        """<p>Update lens review for a particular workload.</p>

        Args:
            jira_configuration: <p>Configuration of the Jira integration.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_lens_review_input.UpdateLensReviewInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.update_lens_review_output.UpdateLensReviewOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_lens_review

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_lens_review.update_lens_review(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_lens_review_input.UpdateLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        if lens_notes is not None:
            input_["lens_notes"] = lens_notes
        if pillar_notes is not None:
            input_["pillar_notes"] = pillar_notes
        if jira_configuration is not None:
            input_["jira_configuration"] = jira_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_profile(
        self,
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        profile_description: Optional[
            "capo_wellarchitected.types.profile_description.ProfileDescription"
        ] = None,
        profile_questions: Optional[
            "capo_wellarchitected.types.profile_question_updates.ProfileQuestionUpdates"
        ] = None,
    ) -> "capo_wellarchitected.types.update_profile_output.UpdateProfileOutput":
        """<p>Update a profile.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>
            profile_description: <p>The profile description.</p>
            profile_questions: <p>Profile questions.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_profile_input.UpdateProfileInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.update_profile_output.UpdateProfileOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_profile

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_profile.update_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_profile_input.UpdateProfileInput = {}  # type: ignore[typeddict-item]
        input_["profile_arn"] = profile_arn
        if profile_description is not None:
            input_["profile_description"] = profile_description
        if profile_questions is not None:
            input_["profile_questions"] = profile_questions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_review_template(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        template_name: Optional[
            "capo_wellarchitected.types.template_name.TemplateName"
        ] = None,
        description: Optional[
            "capo_wellarchitected.types.template_description.TemplateDescription"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        lenses_to_associate: Optional[
            "capo_wellarchitected.types.review_template_lens_aliases.ReviewTemplateLensAliases"
        ] = None,
        lenses_to_disassociate: Optional[
            "capo_wellarchitected.types.review_template_lens_aliases.ReviewTemplateLensAliases"
        ] = None,
    ) -> "capo_wellarchitected.types.update_review_template_output.UpdateReviewTemplateOutput":
        """<p>Update a review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>
            template_name: <p>The review template name.</p>
            description: <p>The review template description.</p>
            lenses_to_associate: <p>A list of lens aliases or ARNs to apply to the review template.</p>
            lenses_to_disassociate: <p>A list of lens aliases or ARNs to unapply to the review template. The <code>wellarchitected</code> lens cannot be unapplied.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_review_template_input.UpdateReviewTemplateInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.update_review_template_output.UpdateReviewTemplateOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template.update_review_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_review_template_input.UpdateReviewTemplateInput = {}  # type: ignore[typeddict-item]
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_review_template_answer(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        question_id: "capo_wellarchitected.types.question_id.QuestionId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        selected_choices: Optional[
            "capo_wellarchitected.types.selected_choices.SelectedChoices"
        ] = None,
        choice_updates: Optional[
            "capo_wellarchitected.types.choice_updates.ChoiceUpdates"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        is_applicable: Optional[
            "capo_wellarchitected.types.is_applicable.IsApplicable"
        ] = None,
        reason: Optional[
            "capo_wellarchitected.types.answer_reason.AnswerReason"
        ] = None,
    ) -> "capo_wellarchitected.types.update_review_template_answer_output.UpdateReviewTemplateAnswerOutput":
        """<p>Update a review template answer.</p>

        Args:
            template_arn: <p>The review template ARN.</p>
            choice_updates: <p>A list of choices to be updated.</p>
            reason: <p>The update reason.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_review_template_answer_input.UpdateReviewTemplateAnswerInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.update_review_template_answer_output.UpdateReviewTemplateAnswerOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_answer

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_answer.update_review_template_answer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_review_template_answer_input.UpdateReviewTemplateAnswerInput = {}  # type: ignore[typeddict-item]
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_review_template_lens_review(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        lens_notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        pillar_notes: Optional[
            "capo_wellarchitected.types.pillar_notes.PillarNotes"
        ] = None,
    ) -> "capo_wellarchitected.types.update_review_template_lens_review_output.UpdateReviewTemplateLensReviewOutput":
        """<p>Update a lens review associated with a review template.</p>

        Args:
            template_arn: <p>The review template ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_review_template_lens_review_input.UpdateReviewTemplateLensReviewInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.update_review_template_lens_review_output.UpdateReviewTemplateLensReviewOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_lens_review

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_review_template_lens_review.update_review_template_lens_review(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_review_template_lens_review_input.UpdateReviewTemplateLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias
        if lens_notes is not None:
            input_["lens_notes"] = lens_notes
        if pillar_notes is not None:
            input_["pillar_notes"] = pillar_notes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_share_invitation(
        self,
        share_invitation_id: "capo_wellarchitected.types.share_invitation_id.ShareInvitationId",
        share_invitation_action: "capo_wellarchitected.types.share_invitation_action.ShareInvitationAction",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.update_share_invitation_output.UpdateShareInvitationOutput":
        """<p>Update a workload or custom lens share invitation.</p> <note> <p>This API operation can be called independently of any resource. Previous documentation implied that a workload ARN must be specified.</p> </note>

        Args:
            share_invitation_id: <p>The ID assigned to the share invitation.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_share_invitation_input.UpdateShareInvitationInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.update_share_invitation_output.UpdateShareInvitationOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_share_invitation

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_share_invitation.update_share_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_share_invitation_input.UpdateShareInvitationInput = {}  # type: ignore[typeddict-item]
        input_["share_invitation_id"] = share_invitation_id
        input_["share_invitation_action"] = share_invitation_action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_workload(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        workload_name: Optional[
            "capo_wellarchitected.types.workload_name.WorkloadName"
        ] = None,
        description: Optional[
            "capo_wellarchitected.types.workload_description.WorkloadDescription"
        ] = None,
        environment: Optional[
            "capo_wellarchitected.types.workload_environment.WorkloadEnvironment"
        ] = None,
        account_ids: Optional[
            "capo_wellarchitected.types.workload_account_ids.WorkloadAccountIds"
        ] = None,
        aws_regions: Optional[
            "capo_wellarchitected.types.workload_aws_regions.WorkloadAwsRegions"
        ] = None,
        non_aws_regions: Optional[
            "capo_wellarchitected.types.workload_non_aws_regions.WorkloadNonAwsRegions"
        ] = None,
        pillar_priorities: Optional[
            "capo_wellarchitected.types.workload_pillar_priorities.WorkloadPillarPriorities"
        ] = None,
        architectural_design: Optional[
            "capo_wellarchitected.types.workload_architectural_design.WorkloadArchitecturalDesign"
        ] = None,
        review_owner: Optional[
            "capo_wellarchitected.types.workload_review_owner.WorkloadReviewOwner"
        ] = None,
        is_review_owner_update_acknowledged: Optional[
            "capo_wellarchitected.types.is_review_owner_update_acknowledged.IsReviewOwnerUpdateAcknowledged"
        ] = None,
        industry_type: Optional[
            "capo_wellarchitected.types.workload_industry_type.WorkloadIndustryType"
        ] = None,
        industry: Optional[
            "capo_wellarchitected.types.workload_industry.WorkloadIndustry"
        ] = None,
        notes: Optional["capo_wellarchitected.types.notes.Notes"] = None,
        improvement_status: Optional[
            "capo_wellarchitected.types.workload_improvement_status.WorkloadImprovementStatus"
        ] = None,
        discovery_config: Optional[
            "capo_wellarchitected.types.workload_discovery_config.WorkloadDiscoveryConfig"
        ] = None,
        applications: Optional[
            "capo_wellarchitected.types.workload_applications.WorkloadApplications"
        ] = None,
        jira_configuration: Optional[
            "capo_wellarchitected.types.workload_jira_configuration_input.WorkloadJiraConfigurationInput"
        ] = None,
    ) -> "capo_wellarchitected.types.update_workload_output.UpdateWorkloadOutput":
        """<p>Update an existing workload.</p>

        Args:
            is_review_owner_update_acknowledged: <p>Flag indicating whether the workload owner has acknowledged that the <i>Review owner</i> field is required.</p> <p>If a <b>Review owner</b> is not added to the workload within 60 days of acknowledgement, access to the workload is restricted until an owner is added.</p>
            discovery_config: <p>Well-Architected discovery configuration settings to associate to the workload.</p>
            applications: <p>List of AppRegistry application ARNs to associate to the workload.</p>
            jira_configuration: <p>Configuration of the Jira integration.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_workload_input.UpdateWorkloadInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.update_workload_output.UpdateWorkloadOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_workload

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_workload.update_workload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_workload_input.UpdateWorkloadInput = {}  # type: ignore[typeddict-item]
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_workload_share(
        self,
        share_id: "capo_wellarchitected.types.share_id.ShareId",
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        permission_type: "capo_wellarchitected.types.permission_type.PermissionType",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
    ) -> "capo_wellarchitected.types.update_workload_share_output.UpdateWorkloadShareOutput":
        """<p>Update a workload share.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.update_workload_share_input.UpdateWorkloadShareInput]",
        ) -> OperationResponse[
            "capo_wellarchitected.types.update_workload_share_output.UpdateWorkloadShareOutput"
        ]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.update_workload_share

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.update_workload_share.update_workload_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.update_workload_share_input.UpdateWorkloadShareInput = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id
        input_["workload_id"] = workload_id
        input_["permission_type"] = permission_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def upgrade_lens_review(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        milestone_name: "capo_wellarchitected.types.milestone_name.MilestoneName",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Upgrade lens review for a particular workload.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.upgrade_lens_review_input.UpgradeLensReviewInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_lens_review

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_lens_review.upgrade_lens_review(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.upgrade_lens_review_input.UpgradeLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["lens_alias"] = lens_alias
        input_["milestone_name"] = milestone_name
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def upgrade_profile_version(
        self,
        workload_id: "capo_wellarchitected.types.workload_id.WorkloadId",
        profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        milestone_name: Optional[
            "capo_wellarchitected.types.milestone_name.MilestoneName"
        ] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Upgrade a profile.</p>

        Args:
            profile_arn: <p>The profile ARN.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The user has reached their resource quota.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.upgrade_profile_version_input.UpgradeProfileVersionInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_profile_version

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_profile_version.upgrade_profile_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.upgrade_profile_version_input.UpgradeProfileVersionInput = {}  # type: ignore[typeddict-item]
        input_["workload_id"] = workload_id
        input_["profile_arn"] = profile_arn
        if milestone_name is not None:
            input_["milestone_name"] = milestone_name
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def upgrade_review_template_lens_review(
        self,
        template_arn: "capo_wellarchitected.types.template_arn.TemplateArn",
        lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias",
        *,
        config_overrides: Optional[WellArchitectedClientConfig] = None,
        client_request_token: Optional[
            "capo_wellarchitected.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Upgrade the lens review of a review template.</p>

        Args:
            template_arn: <p>The ARN of the review template.</p>

        Raises:
            capo_wellarchitected.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_wellarchitected.errors.conflict_exception.ConflictException: <p>The resource has already been processed, was deleted, or is too large.</p>
            capo_wellarchitected.errors.internal_server_exception.InternalServerException: <p>There is a problem with the Well-Architected Tool API service.</p>
            capo_wellarchitected.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_wellarchitected.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_wellarchitected.errors.validation_exception.ValidationException: <p>The user input is not valid.</p>
            capo_wellarchitected.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wellarchitected.types.upgrade_review_template_lens_review_input.UpgradeReviewTemplateLensReviewInput]",
        ) -> OperationResponse[None]:
            import capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_review_template_lens_review

            output, http_response = (
                capo_wellarchitected._operations.well_architected_api_service_lambda.upgrade_review_template_lens_review.upgrade_review_template_lens_review(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wellarchitected.types.upgrade_review_template_lens_review_input.UpgradeReviewTemplateLensReviewInput = {}  # type: ignore[typeddict-item]
        input_["template_arn"] = template_arn
        input_["lens_alias"] = lens_alias
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

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
