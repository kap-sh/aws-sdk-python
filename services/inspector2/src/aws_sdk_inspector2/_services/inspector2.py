"""Generated from Smithy shape ``com.amazonaws.inspector2#Inspector2``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_inspector2._auth._signers
import aws_sdk_inspector2._auth._sigv4
from aws_sdk_inspector2._auth._identity import Credentials
from aws_sdk_inspector2._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_inspector2._auth._zapros_handler import AuthMiddleware
from aws_sdk_inspector2._pagination import resolve_path as _resolve_path
from aws_sdk_inspector2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.account_id_set
    import aws_sdk_inspector2.types.aggregation_request
    import aws_sdk_inspector2.types.aggregation_response
    import aws_sdk_inspector2.types.aggregation_type
    import aws_sdk_inspector2.types.arn
    import aws_sdk_inspector2.types.associate_configuration_request_list
    import aws_sdk_inspector2.types.associate_member_request
    import aws_sdk_inspector2.types.associate_member_response
    import aws_sdk_inspector2.types.auto_enable
    import aws_sdk_inspector2.types.batch_associate_code_security_scan_configuration_request
    import aws_sdk_inspector2.types.batch_associate_code_security_scan_configuration_response
    import aws_sdk_inspector2.types.batch_disassociate_code_security_scan_configuration_request
    import aws_sdk_inspector2.types.batch_disassociate_code_security_scan_configuration_response
    import aws_sdk_inspector2.types.batch_get_account_status_request
    import aws_sdk_inspector2.types.batch_get_account_status_response
    import aws_sdk_inspector2.types.batch_get_code_snippet_request
    import aws_sdk_inspector2.types.batch_get_code_snippet_response
    import aws_sdk_inspector2.types.batch_get_finding_details_request
    import aws_sdk_inspector2.types.batch_get_finding_details_response
    import aws_sdk_inspector2.types.batch_get_free_trial_info_request
    import aws_sdk_inspector2.types.batch_get_free_trial_info_response
    import aws_sdk_inspector2.types.batch_get_member_ec2_deep_inspection_status_request
    import aws_sdk_inspector2.types.batch_get_member_ec2_deep_inspection_status_response
    import aws_sdk_inspector2.types.batch_update_member_ec2_deep_inspection_status_request
    import aws_sdk_inspector2.types.batch_update_member_ec2_deep_inspection_status_response
    import aws_sdk_inspector2.types.cancel_findings_report_request
    import aws_sdk_inspector2.types.cancel_findings_report_response
    import aws_sdk_inspector2.types.cancel_sbom_export_request
    import aws_sdk_inspector2.types.cancel_sbom_export_response
    import aws_sdk_inspector2.types.cis_check_aggregation
    import aws_sdk_inspector2.types.cis_report_format
    import aws_sdk_inspector2.types.cis_scan
    import aws_sdk_inspector2.types.cis_scan_arn
    import aws_sdk_inspector2.types.cis_scan_configuration
    import aws_sdk_inspector2.types.cis_scan_configuration_arn
    import aws_sdk_inspector2.types.cis_scan_configurations_sort_by
    import aws_sdk_inspector2.types.cis_scan_name
    import aws_sdk_inspector2.types.cis_scan_result_details
    import aws_sdk_inspector2.types.cis_scan_result_details_filter_criteria
    import aws_sdk_inspector2.types.cis_scan_result_details_sort_by
    import aws_sdk_inspector2.types.cis_scan_results_aggregated_by_checks_filter_criteria
    import aws_sdk_inspector2.types.cis_scan_results_aggregated_by_checks_sort_by
    import aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria
    import aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by
    import aws_sdk_inspector2.types.cis_scan_results_max_results
    import aws_sdk_inspector2.types.cis_security_level
    import aws_sdk_inspector2.types.cis_session_messages
    import aws_sdk_inspector2.types.cis_sort_order
    import aws_sdk_inspector2.types.cis_tag_map
    import aws_sdk_inspector2.types.cis_target_resource_aggregation
    import aws_sdk_inspector2.types.client_token
    import aws_sdk_inspector2.types.cluster_for_image_filter_criteria
    import aws_sdk_inspector2.types.cluster_information
    import aws_sdk_inspector2.types.code_security_client_token
    import aws_sdk_inspector2.types.code_security_integration_arn
    import aws_sdk_inspector2.types.code_security_resource
    import aws_sdk_inspector2.types.code_security_scan_configuration
    import aws_sdk_inspector2.types.code_security_uuid
    import aws_sdk_inspector2.types.configuration_level
    import aws_sdk_inspector2.types.counts
    import aws_sdk_inspector2.types.coverage_filter_criteria
    import aws_sdk_inspector2.types.covered_resource
    import aws_sdk_inspector2.types.create_cis_scan_configuration_request
    import aws_sdk_inspector2.types.create_cis_scan_configuration_response
    import aws_sdk_inspector2.types.create_cis_targets
    import aws_sdk_inspector2.types.create_code_security_integration_request
    import aws_sdk_inspector2.types.create_code_security_integration_response
    import aws_sdk_inspector2.types.create_code_security_scan_configuration_request
    import aws_sdk_inspector2.types.create_code_security_scan_configuration_response
    import aws_sdk_inspector2.types.create_filter_request
    import aws_sdk_inspector2.types.create_filter_response
    import aws_sdk_inspector2.types.create_findings_report_request
    import aws_sdk_inspector2.types.create_findings_report_response
    import aws_sdk_inspector2.types.create_integration_detail
    import aws_sdk_inspector2.types.create_sbom_export_request
    import aws_sdk_inspector2.types.create_sbom_export_response
    import aws_sdk_inspector2.types.delegated_admin_account
    import aws_sdk_inspector2.types.delete_cis_scan_configuration_request
    import aws_sdk_inspector2.types.delete_cis_scan_configuration_response
    import aws_sdk_inspector2.types.delete_code_security_integration_request
    import aws_sdk_inspector2.types.delete_code_security_integration_response
    import aws_sdk_inspector2.types.delete_code_security_scan_configuration_request
    import aws_sdk_inspector2.types.delete_code_security_scan_configuration_response
    import aws_sdk_inspector2.types.delete_filter_request
    import aws_sdk_inspector2.types.delete_filter_response
    import aws_sdk_inspector2.types.describe_organization_configuration_request
    import aws_sdk_inspector2.types.describe_organization_configuration_response
    import aws_sdk_inspector2.types.destination
    import aws_sdk_inspector2.types.disable_delegated_admin_account_request
    import aws_sdk_inspector2.types.disable_delegated_admin_account_response
    import aws_sdk_inspector2.types.disable_request
    import aws_sdk_inspector2.types.disable_resource_type_list
    import aws_sdk_inspector2.types.disable_response
    import aws_sdk_inspector2.types.disassociate_configuration_request_list
    import aws_sdk_inspector2.types.disassociate_member_request
    import aws_sdk_inspector2.types.disassociate_member_response
    import aws_sdk_inspector2.types.ec2_configuration
    import aws_sdk_inspector2.types.ecr_configuration
    import aws_sdk_inspector2.types.enable_delegated_admin_account_request
    import aws_sdk_inspector2.types.enable_delegated_admin_account_response
    import aws_sdk_inspector2.types.enable_request
    import aws_sdk_inspector2.types.enable_resource_type_list
    import aws_sdk_inspector2.types.enable_response
    import aws_sdk_inspector2.types.filter
    import aws_sdk_inspector2.types.filter_action
    import aws_sdk_inspector2.types.filter_arn
    import aws_sdk_inspector2.types.filter_arn_list
    import aws_sdk_inspector2.types.filter_criteria
    import aws_sdk_inspector2.types.filter_description
    import aws_sdk_inspector2.types.filter_name
    import aws_sdk_inspector2.types.filter_reason
    import aws_sdk_inspector2.types.finding
    import aws_sdk_inspector2.types.finding_arn_list
    import aws_sdk_inspector2.types.finding_arns
    import aws_sdk_inspector2.types.get_cis_scan_report_request
    import aws_sdk_inspector2.types.get_cis_scan_report_response
    import aws_sdk_inspector2.types.get_cis_scan_result_details_max_results
    import aws_sdk_inspector2.types.get_cis_scan_result_details_request
    import aws_sdk_inspector2.types.get_cis_scan_result_details_response
    import aws_sdk_inspector2.types.get_clusters_for_image_next_token
    import aws_sdk_inspector2.types.get_clusters_for_image_request
    import aws_sdk_inspector2.types.get_clusters_for_image_response
    import aws_sdk_inspector2.types.get_code_security_integration_request
    import aws_sdk_inspector2.types.get_code_security_integration_response
    import aws_sdk_inspector2.types.get_code_security_scan_configuration_request
    import aws_sdk_inspector2.types.get_code_security_scan_configuration_response
    import aws_sdk_inspector2.types.get_code_security_scan_request
    import aws_sdk_inspector2.types.get_code_security_scan_response
    import aws_sdk_inspector2.types.get_configuration_request
    import aws_sdk_inspector2.types.get_configuration_response
    import aws_sdk_inspector2.types.get_delegated_admin_account_request
    import aws_sdk_inspector2.types.get_delegated_admin_account_response
    import aws_sdk_inspector2.types.get_ec2_deep_inspection_configuration_request
    import aws_sdk_inspector2.types.get_ec2_deep_inspection_configuration_response
    import aws_sdk_inspector2.types.get_encryption_key_request
    import aws_sdk_inspector2.types.get_encryption_key_response
    import aws_sdk_inspector2.types.get_findings_report_status_request
    import aws_sdk_inspector2.types.get_findings_report_status_response
    import aws_sdk_inspector2.types.get_member_request
    import aws_sdk_inspector2.types.get_member_response
    import aws_sdk_inspector2.types.get_sbom_export_request
    import aws_sdk_inspector2.types.get_sbom_export_response
    import aws_sdk_inspector2.types.group_key
    import aws_sdk_inspector2.types.integration_name
    import aws_sdk_inspector2.types.integration_type
    import aws_sdk_inspector2.types.kms_key_arn
    import aws_sdk_inspector2.types.list_account_permissions_max_results
    import aws_sdk_inspector2.types.list_account_permissions_request
    import aws_sdk_inspector2.types.list_account_permissions_response
    import aws_sdk_inspector2.types.list_cis_scan_configurations_filter_criteria
    import aws_sdk_inspector2.types.list_cis_scan_configurations_max_results
    import aws_sdk_inspector2.types.list_cis_scan_configurations_request
    import aws_sdk_inspector2.types.list_cis_scan_configurations_response
    import aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_checks_request
    import aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_checks_response
    import aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_target_resource_request
    import aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_target_resource_response
    import aws_sdk_inspector2.types.list_cis_scans_detail_level
    import aws_sdk_inspector2.types.list_cis_scans_filter_criteria
    import aws_sdk_inspector2.types.list_cis_scans_max_results
    import aws_sdk_inspector2.types.list_cis_scans_request
    import aws_sdk_inspector2.types.list_cis_scans_response
    import aws_sdk_inspector2.types.list_cis_scans_sort_by
    import aws_sdk_inspector2.types.list_code_security_integrations_request
    import aws_sdk_inspector2.types.list_code_security_integrations_response
    import aws_sdk_inspector2.types.list_code_security_scan_configuration_associations_request
    import aws_sdk_inspector2.types.list_code_security_scan_configuration_associations_response
    import aws_sdk_inspector2.types.list_code_security_scan_configurations_request
    import aws_sdk_inspector2.types.list_code_security_scan_configurations_response
    import aws_sdk_inspector2.types.list_coverage_max_results
    import aws_sdk_inspector2.types.list_coverage_request
    import aws_sdk_inspector2.types.list_coverage_response
    import aws_sdk_inspector2.types.list_coverage_statistics_request
    import aws_sdk_inspector2.types.list_coverage_statistics_response
    import aws_sdk_inspector2.types.list_delegated_admin_accounts_request
    import aws_sdk_inspector2.types.list_delegated_admin_accounts_response
    import aws_sdk_inspector2.types.list_delegated_admin_max_results
    import aws_sdk_inspector2.types.list_filter_max_results
    import aws_sdk_inspector2.types.list_filters_request
    import aws_sdk_inspector2.types.list_filters_response
    import aws_sdk_inspector2.types.list_finding_aggregations_max_results
    import aws_sdk_inspector2.types.list_finding_aggregations_request
    import aws_sdk_inspector2.types.list_finding_aggregations_response
    import aws_sdk_inspector2.types.list_findings_max_results
    import aws_sdk_inspector2.types.list_findings_request
    import aws_sdk_inspector2.types.list_findings_response
    import aws_sdk_inspector2.types.list_members_max_results
    import aws_sdk_inspector2.types.list_members_request
    import aws_sdk_inspector2.types.list_members_response
    import aws_sdk_inspector2.types.list_tags_for_resource_request
    import aws_sdk_inspector2.types.list_tags_for_resource_response
    import aws_sdk_inspector2.types.list_usage_totals_max_results
    import aws_sdk_inspector2.types.list_usage_totals_next_token
    import aws_sdk_inspector2.types.list_usage_totals_request
    import aws_sdk_inspector2.types.list_usage_totals_response
    import aws_sdk_inspector2.types.member
    import aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_list
    import aws_sdk_inspector2.types.metering_account_id_list
    import aws_sdk_inspector2.types.next_token
    import aws_sdk_inspector2.types.path_list
    import aws_sdk_inspector2.types.permission
    import aws_sdk_inspector2.types.report_format
    import aws_sdk_inspector2.types.report_id
    import aws_sdk_inspector2.types.report_target_accounts
    import aws_sdk_inspector2.types.reset_encryption_key_request
    import aws_sdk_inspector2.types.reset_encryption_key_response
    import aws_sdk_inspector2.types.resource_filter_criteria
    import aws_sdk_inspector2.types.resource_id
    import aws_sdk_inspector2.types.resource_type
    import aws_sdk_inspector2.types.sbom_report_format
    import aws_sdk_inspector2.types.scan_configuration_arn
    import aws_sdk_inspector2.types.scan_configuration_name
    import aws_sdk_inspector2.types.scan_type
    import aws_sdk_inspector2.types.schedule
    import aws_sdk_inspector2.types.scope_settings
    import aws_sdk_inspector2.types.search_vulnerabilities_filter_criteria
    import aws_sdk_inspector2.types.search_vulnerabilities_request
    import aws_sdk_inspector2.types.search_vulnerabilities_response
    import aws_sdk_inspector2.types.send_cis_session_health_request
    import aws_sdk_inspector2.types.send_cis_session_health_response
    import aws_sdk_inspector2.types.send_cis_session_telemetry_request
    import aws_sdk_inspector2.types.send_cis_session_telemetry_response
    import aws_sdk_inspector2.types.service
    import aws_sdk_inspector2.types.sort_criteria
    import aws_sdk_inspector2.types.start_cis_session_message
    import aws_sdk_inspector2.types.start_cis_session_request
    import aws_sdk_inspector2.types.start_cis_session_response
    import aws_sdk_inspector2.types.start_code_security_scan_request
    import aws_sdk_inspector2.types.start_code_security_scan_response
    import aws_sdk_inspector2.types.stop_cis_session_message
    import aws_sdk_inspector2.types.stop_cis_session_request
    import aws_sdk_inspector2.types.stop_cis_session_response
    import aws_sdk_inspector2.types.string_filter_list
    import aws_sdk_inspector2.types.tag_key_list
    import aws_sdk_inspector2.types.tag_map
    import aws_sdk_inspector2.types.tag_resource_request
    import aws_sdk_inspector2.types.tag_resource_response
    import aws_sdk_inspector2.types.untag_resource_request
    import aws_sdk_inspector2.types.untag_resource_response
    import aws_sdk_inspector2.types.update_cis_scan_configuration_request
    import aws_sdk_inspector2.types.update_cis_scan_configuration_response
    import aws_sdk_inspector2.types.update_cis_targets
    import aws_sdk_inspector2.types.update_code_security_integration_request
    import aws_sdk_inspector2.types.update_code_security_integration_response
    import aws_sdk_inspector2.types.update_code_security_scan_configuration_request
    import aws_sdk_inspector2.types.update_code_security_scan_configuration_response
    import aws_sdk_inspector2.types.update_configuration_request
    import aws_sdk_inspector2.types.update_configuration_response
    import aws_sdk_inspector2.types.update_ec2_deep_inspection_configuration_request
    import aws_sdk_inspector2.types.update_ec2_deep_inspection_configuration_response
    import aws_sdk_inspector2.types.update_encryption_key_request
    import aws_sdk_inspector2.types.update_encryption_key_response
    import aws_sdk_inspector2.types.update_filter_request
    import aws_sdk_inspector2.types.update_filter_response
    import aws_sdk_inspector2.types.update_integration_details
    import aws_sdk_inspector2.types.update_org_ec2_deep_inspection_configuration_request
    import aws_sdk_inspector2.types.update_org_ec2_deep_inspection_configuration_response
    import aws_sdk_inspector2.types.update_organization_configuration_request
    import aws_sdk_inspector2.types.update_organization_configuration_response
    import aws_sdk_inspector2.types.usage_account_id_list
    import aws_sdk_inspector2.types.usage_total
    import aws_sdk_inspector2.types.uuid
    import aws_sdk_inspector2.types.vulnerability


class Inspector2ClientConfig(TypedDict, total=False):
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


class Inspector2Client:
    """A client for the ``Inspector2`` service.

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
        self.config = Inspector2ClientConfig(
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
        self, config_overrides: Optional[Inspector2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: Inspector2ClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def associate_member(
        self,
        account_id: "aws_sdk_inspector2.types.account_id.AccountId",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.associate_member_response.AssociateMemberResponse":
        """<p>Associates an Amazon Web Services account with an Amazon Inspector delegated administrator. An HTTP 200 response indicates the association was successfully started, but doesn’t indicate whether it was completed. You can check if the association completed by using <a href=\"https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListMembers.html\">ListMembers</a> for multiple accounts or <a href=\"https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetMember.html\">GetMembers</a> for a single account.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID of the member account to be associated.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.associate_member_request.AssociateMemberRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.associate_member_response.AssociateMemberResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.associate_member

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.associate_member.associate_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.associate_member_request.AssociateMemberRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_associate_code_security_scan_configuration(
        self,
        associate_configuration_requests: "aws_sdk_inspector2.types.associate_configuration_request_list.AssociateConfigurationRequestList",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.batch_associate_code_security_scan_configuration_response.BatchAssociateCodeSecurityScanConfigurationResponse":
        """<p>Associates multiple code repositories with an Amazon Inspector code security scan configuration.</p>

        Args:
            associate_configuration_requests: <p>A list of code repositories to associate with the specified scan configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.batch_associate_code_security_scan_configuration_request.BatchAssociateCodeSecurityScanConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.batch_associate_code_security_scan_configuration_response.BatchAssociateCodeSecurityScanConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.batch_associate_code_security_scan_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.batch_associate_code_security_scan_configuration.batch_associate_code_security_scan_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.batch_associate_code_security_scan_configuration_request.BatchAssociateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["associate_configuration_requests"] = associate_configuration_requests

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_disassociate_code_security_scan_configuration(
        self,
        disassociate_configuration_requests: "aws_sdk_inspector2.types.disassociate_configuration_request_list.DisassociateConfigurationRequestList",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.batch_disassociate_code_security_scan_configuration_response.BatchDisassociateCodeSecurityScanConfigurationResponse":
        """<p>Disassociates multiple code repositories from an Amazon Inspector code security scan configuration.</p>

        Args:
            disassociate_configuration_requests: <p>A list of code repositories to disassociate from the specified scan configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.batch_disassociate_code_security_scan_configuration_request.BatchDisassociateCodeSecurityScanConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.batch_disassociate_code_security_scan_configuration_response.BatchDisassociateCodeSecurityScanConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.batch_disassociate_code_security_scan_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.batch_disassociate_code_security_scan_configuration.batch_disassociate_code_security_scan_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.batch_disassociate_code_security_scan_configuration_request.BatchDisassociateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["disassociate_configuration_requests"] = (
            disassociate_configuration_requests
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_account_status(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        account_ids: Optional[
            "aws_sdk_inspector2.types.account_id_set.AccountIdSet"
        ] = None,
    ) -> "aws_sdk_inspector2.types.batch_get_account_status_response.BatchGetAccountStatusResponse":
        """<p>Retrieves the Amazon Inspector status of multiple Amazon Web Services accounts within your environment.</p>

        Args:
            account_ids: <p>The 12-digit Amazon Web Services account IDs of the accounts to retrieve Amazon Inspector status for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.batch_get_account_status_request.BatchGetAccountStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.batch_get_account_status_response.BatchGetAccountStatusResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.batch_get_account_status

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.batch_get_account_status.batch_get_account_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.batch_get_account_status_request.BatchGetAccountStatusRequest = {}  # type: ignore[typeddict-item]
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_code_snippet(
        self,
        finding_arns: "aws_sdk_inspector2.types.finding_arns.FindingArns",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.batch_get_code_snippet_response.BatchGetCodeSnippetResponse":
        """<p>Retrieves code snippets from findings that Amazon Inspector detected code vulnerabilities in.</p>

        Args:
            finding_arns: <p>An array of finding ARNs for the findings you want to retrieve code snippets from.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.batch_get_code_snippet_request.BatchGetCodeSnippetRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.batch_get_code_snippet_response.BatchGetCodeSnippetResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.batch_get_code_snippet

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.batch_get_code_snippet.batch_get_code_snippet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.batch_get_code_snippet_request.BatchGetCodeSnippetRequest = {}  # type: ignore[typeddict-item]
        input_["finding_arns"] = finding_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_finding_details(
        self,
        finding_arns: "aws_sdk_inspector2.types.finding_arn_list.FindingArnList",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.batch_get_finding_details_response.BatchGetFindingDetailsResponse":
        """<p>Gets vulnerability details for findings.</p>

        Args:
            finding_arns: <p>A list of finding ARNs.</p>

        Examples:
            Sample BatchGetFindingDetails Call

            >>> client.batch_get_finding_details(finding_arns=['arn:aws:inspector2:eu-west-1:123456789012:finding/78b88cc9aa1d78b6e14fde90d774dde7', 'arn:aws:inspector2:eu-west-1:111111111111:finding/78b88cc9aa1d78b6e14fde90d874dde7'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.batch_get_finding_details_request.BatchGetFindingDetailsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.batch_get_finding_details_response.BatchGetFindingDetailsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.batch_get_finding_details

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.batch_get_finding_details.batch_get_finding_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.batch_get_finding_details_request.BatchGetFindingDetailsRequest = {}  # type: ignore[typeddict-item]
        input_["finding_arns"] = finding_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_free_trial_info(
        self,
        account_ids: "aws_sdk_inspector2.types.metering_account_id_list.MeteringAccountIdList",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.batch_get_free_trial_info_response.BatchGetFreeTrialInfoResponse":
        """<p>Gets free trial status for multiple Amazon Web Services accounts.</p>

        Args:
            account_ids: <p>The account IDs to get free trial status for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.batch_get_free_trial_info_request.BatchGetFreeTrialInfoRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.batch_get_free_trial_info_response.BatchGetFreeTrialInfoResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.batch_get_free_trial_info

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.batch_get_free_trial_info.batch_get_free_trial_info(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.batch_get_free_trial_info_request.BatchGetFreeTrialInfoRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_member_ec2_deep_inspection_status(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        account_ids: Optional[
            "aws_sdk_inspector2.types.account_id_set.AccountIdSet"
        ] = None,
    ) -> "aws_sdk_inspector2.types.batch_get_member_ec2_deep_inspection_status_response.BatchGetMemberEc2DeepInspectionStatusResponse":
        """<p>Retrieves Amazon Inspector deep inspection activation status of multiple member accounts within your organization. You must be the delegated administrator of an organization in Amazon Inspector to use this API.</p>

        Args:
            account_ids: <p>The unique identifiers for the Amazon Web Services accounts to retrieve Amazon Inspector deep inspection activation status for. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.batch_get_member_ec2_deep_inspection_status_request.BatchGetMemberEc2DeepInspectionStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.batch_get_member_ec2_deep_inspection_status_response.BatchGetMemberEc2DeepInspectionStatusResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.batch_get_member_ec2_deep_inspection_status

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.batch_get_member_ec2_deep_inspection_status.batch_get_member_ec2_deep_inspection_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.batch_get_member_ec2_deep_inspection_status_request.BatchGetMemberEc2DeepInspectionStatusRequest = {}  # type: ignore[typeddict-item]
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_member_ec2_deep_inspection_status(
        self,
        account_ids: "aws_sdk_inspector2.types.member_account_ec2_deep_inspection_status_list.MemberAccountEc2DeepInspectionStatusList",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.batch_update_member_ec2_deep_inspection_status_response.BatchUpdateMemberEc2DeepInspectionStatusResponse":
        """<p>Activates or deactivates Amazon Inspector deep inspection for the provided member accounts in your organization. You must be the delegated administrator of an organization in Amazon Inspector to use this API.</p>

        Args:
            account_ids: <p>The unique identifiers for the Amazon Web Services accounts to change Amazon Inspector deep inspection status for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.batch_update_member_ec2_deep_inspection_status_request.BatchUpdateMemberEc2DeepInspectionStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.batch_update_member_ec2_deep_inspection_status_response.BatchUpdateMemberEc2DeepInspectionStatusResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.batch_update_member_ec2_deep_inspection_status

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.batch_update_member_ec2_deep_inspection_status.batch_update_member_ec2_deep_inspection_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.batch_update_member_ec2_deep_inspection_status_request.BatchUpdateMemberEc2DeepInspectionStatusRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_findings_report(
        self,
        report_id: "aws_sdk_inspector2.types.report_id.ReportId",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.cancel_findings_report_response.CancelFindingsReportResponse":
        """<p>Cancels the given findings report.</p>

        Args:
            report_id: <p>The ID of the report to be canceled.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.cancel_findings_report_request.CancelFindingsReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.cancel_findings_report_response.CancelFindingsReportResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.cancel_findings_report

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.cancel_findings_report.cancel_findings_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.cancel_findings_report_request.CancelFindingsReportRequest = {}  # type: ignore[typeddict-item]
        input_["report_id"] = report_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_sbom_export(
        self,
        report_id: "aws_sdk_inspector2.types.report_id.ReportId",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> (
        "aws_sdk_inspector2.types.cancel_sbom_export_response.CancelSbomExportResponse"
    ):
        """<p>Cancels a software bill of materials (SBOM) report.</p>

        Args:
            report_id: <p>The report ID of the SBOM export to cancel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.cancel_sbom_export_request.CancelSbomExportRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.cancel_sbom_export_response.CancelSbomExportResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.cancel_sbom_export

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.cancel_sbom_export.cancel_sbom_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.cancel_sbom_export_request.CancelSbomExportRequest = {}  # type: ignore[typeddict-item]
        input_["report_id"] = report_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_cis_scan_configuration(
        self,
        scan_name: "aws_sdk_inspector2.types.cis_scan_name.CisScanName",
        security_level: "aws_sdk_inspector2.types.cis_security_level.CisSecurityLevel",
        schedule: "aws_sdk_inspector2.types.schedule.Schedule",
        targets: "aws_sdk_inspector2.types.create_cis_targets.CreateCisTargets",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        tags: Optional["aws_sdk_inspector2.types.cis_tag_map.CisTagMap"] = None,
    ) -> "aws_sdk_inspector2.types.create_cis_scan_configuration_response.CreateCisScanConfigurationResponse":
        """<p>Creates a CIS scan configuration.</p>

        Args:
            scan_name: <p>The scan name for the CIS scan configuration.</p>
            security_level: <p> The security level for the CIS scan configuration. Security level refers to the Benchmark levels that CIS assigns to a profile. </p>
            schedule: <p>The schedule for the CIS scan configuration.</p>
            targets: <p>The targets for the CIS scan configuration.</p>
            tags: <p>The tags for the CIS scan configuration.</p>

        Examples:
            Sample CreateCisScanConfiguration Call

            >>> client.create_cis_scan_configuration(scan_name='sample', security_level='LEVEL_1', schedule={'daily': {'startTime': {'timeOfDay': '12:34', 'timezone': 'UTC'}}}, targets={'accountIds': ['SELF'], 'targetResourceTags': {'key': ['value']}})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.create_cis_scan_configuration_request.CreateCisScanConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.create_cis_scan_configuration_response.CreateCisScanConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.create_cis_scan_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.create_cis_scan_configuration.create_cis_scan_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.create_cis_scan_configuration_request.CreateCisScanConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["scan_name"] = scan_name
        input_["security_level"] = security_level
        input_["schedule"] = schedule
        input_["targets"] = targets
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_code_security_integration(
        self,
        name: "aws_sdk_inspector2.types.integration_name.IntegrationName",
        type: "aws_sdk_inspector2.types.integration_type.IntegrationType",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        details: Optional[
            "aws_sdk_inspector2.types.create_integration_detail.CreateIntegrationDetail"
        ] = None,
        tags: Optional["aws_sdk_inspector2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_inspector2.types.create_code_security_integration_response.CreateCodeSecurityIntegrationResponse":
        """<p>Creates a code security integration with a source code repository provider.</p> <p>After calling the <code>CreateCodeSecurityIntegration</code> operation, you complete authentication and authorization with your provider. Next you call the <code>UpdateCodeSecurityIntegration</code> operation to provide the <code>details</code> to complete the integration setup</p>

        Args:
            name: <p>The name of the code security integration.</p>
            type: <p>The type of repository provider for the integration.</p>
            details: <p>The integration details specific to the repository provider type.</p>
            tags: <p>The tags to apply to the code security integration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.create_code_security_integration_request.CreateCodeSecurityIntegrationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.create_code_security_integration_response.CreateCodeSecurityIntegrationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.create_code_security_integration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.create_code_security_integration.create_code_security_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.create_code_security_integration_request.CreateCodeSecurityIntegrationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["type"] = type
        if details is not None:
            input_["details"] = details
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_code_security_scan_configuration(
        self,
        name: "aws_sdk_inspector2.types.scan_configuration_name.ScanConfigurationName",
        level: "aws_sdk_inspector2.types.configuration_level.ConfigurationLevel",
        configuration: "aws_sdk_inspector2.types.code_security_scan_configuration.CodeSecurityScanConfiguration",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        scope_settings: Optional[
            "aws_sdk_inspector2.types.scope_settings.ScopeSettings"
        ] = None,
        tags: Optional["aws_sdk_inspector2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_inspector2.types.create_code_security_scan_configuration_response.CreateCodeSecurityScanConfigurationResponse":
        """<p>Creates a scan configuration for code security scanning.</p>

        Args:
            name: <p>The name of the scan configuration.</p>
            level: <p>The security level for the scan configuration.</p>
            configuration: <p>The configuration settings for the code security scan.</p>
            scope_settings: <p>The scope settings that define which repositories will be scanned. Include this parameter to create a default scan configuration. Otherwise Amazon Inspector creates a general scan configuration. </p> <p>A default scan configuration automatically applies to all existing and future projects imported into Amazon Inspector. Use the <code>BatchAssociateCodeSecurityScanConfiguration</code> operation to associate a general scan configuration with projects.</p>
            tags: <p>The tags to apply to the scan configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.create_code_security_scan_configuration_request.CreateCodeSecurityScanConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.create_code_security_scan_configuration_response.CreateCodeSecurityScanConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.create_code_security_scan_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.create_code_security_scan_configuration.create_code_security_scan_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.create_code_security_scan_configuration_request.CreateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["level"] = level
        input_["configuration"] = configuration
        if scope_settings is not None:
            input_["scope_settings"] = scope_settings
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_filter(
        self,
        action: "aws_sdk_inspector2.types.filter_action.FilterAction",
        filter_criteria: "aws_sdk_inspector2.types.filter_criteria.FilterCriteria",
        name: "aws_sdk_inspector2.types.filter_name.FilterName",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        description: Optional[
            "aws_sdk_inspector2.types.filter_description.FilterDescription"
        ] = None,
        tags: Optional["aws_sdk_inspector2.types.tag_map.TagMap"] = None,
        reason: Optional["aws_sdk_inspector2.types.filter_reason.FilterReason"] = None,
    ) -> "aws_sdk_inspector2.types.create_filter_response.CreateFilterResponse":
        """<p>Creates a filter resource using specified filter criteria. When the filter action is set to <code>SUPPRESS</code> this action creates a suppression rule.</p>

        Args:
            action: <p>Defines the action that is to be applied to the findings that match the filter.</p>
            description: <p>A description of the filter.</p>
            filter_criteria: <p>Defines the criteria to be used in the filter for querying findings.</p>
            name: <p>The name of the filter. Minimum length of 3. Maximum length of 64. Valid characters include alphanumeric characters, dot (.), underscore (_), and dash (-). Spaces are not allowed.</p>
            tags: <p>A list of tags for the filter.</p>
            reason: <p>The reason for creating the filter.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.create_filter_request.CreateFilterRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.create_filter_response.CreateFilterResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.create_filter

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.create_filter.create_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.create_filter_request.CreateFilterRequest = {}  # type: ignore[typeddict-item]
        input_["action"] = action
        if description is not None:
            input_["description"] = description
        input_["filter_criteria"] = filter_criteria
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_findings_report(
        self,
        report_format: "aws_sdk_inspector2.types.report_format.ReportFormat",
        s3_destination: "aws_sdk_inspector2.types.destination.Destination",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.filter_criteria.FilterCriteria"
        ] = None,
    ) -> "aws_sdk_inspector2.types.create_findings_report_response.CreateFindingsReportResponse":
        """<p>Creates a finding report. By default only <code>ACTIVE</code> findings are returned in the report. To see <code>SUPRESSED</code> or <code>CLOSED</code> findings you must specify a value for the <code>findingStatus</code> filter criteria. </p>

        Args:
            filter_criteria: <p>The filter criteria to apply to the results of the finding report.</p>
            report_format: <p>The format to generate the report in.</p>
            s3_destination: <p>The Amazon S3 export destination for the report.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.create_findings_report_request.CreateFindingsReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.create_findings_report_response.CreateFindingsReportResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.create_findings_report

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.create_findings_report.create_findings_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.create_findings_report_request.CreateFindingsReportRequest = {}  # type: ignore[typeddict-item]
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        input_["report_format"] = report_format
        input_["s3_destination"] = s3_destination

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_sbom_export(
        self,
        report_format: "aws_sdk_inspector2.types.sbom_report_format.SbomReportFormat",
        s3_destination: "aws_sdk_inspector2.types.destination.Destination",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        resource_filter_criteria: Optional[
            "aws_sdk_inspector2.types.resource_filter_criteria.ResourceFilterCriteria"
        ] = None,
    ) -> (
        "aws_sdk_inspector2.types.create_sbom_export_response.CreateSbomExportResponse"
    ):
        """<p>Creates a software bill of materials (SBOM) report.</p>

        Args:
            resource_filter_criteria: <p>The resource filter criteria for the software bill of materials (SBOM) report.</p>
            report_format: <p>The output format for the software bill of materials (SBOM) report.</p>
            s3_destination: <p>Contains details of the Amazon S3 bucket and KMS key used to export findings.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.create_sbom_export_request.CreateSbomExportRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.create_sbom_export_response.CreateSbomExportResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.create_sbom_export

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.create_sbom_export.create_sbom_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.create_sbom_export_request.CreateSbomExportRequest = {}  # type: ignore[typeddict-item]
        if resource_filter_criteria is not None:
            input_["resource_filter_criteria"] = resource_filter_criteria
        input_["report_format"] = report_format
        input_["s3_destination"] = s3_destination

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_cis_scan_configuration(
        self,
        scan_configuration_arn: "aws_sdk_inspector2.types.cis_scan_configuration_arn.CisScanConfigurationArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.delete_cis_scan_configuration_response.DeleteCisScanConfigurationResponse":
        """<p>Deletes a CIS scan configuration.</p>

        Args:
            scan_configuration_arn: <p>The ARN of the CIS scan configuration.</p>

        Examples:
            Sample DeleteCisScanConfiguration Call

            >>> client.delete_cis_scan_configuration(scan_configuration_arn='arn:aws:inspector2:us-east-1:123412341234:owner/123412341234/cis-configuration/624b746d-e080-44ae-8c1d-48e653365a38')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.delete_cis_scan_configuration_request.DeleteCisScanConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.delete_cis_scan_configuration_response.DeleteCisScanConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.delete_cis_scan_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.delete_cis_scan_configuration.delete_cis_scan_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.delete_cis_scan_configuration_request.DeleteCisScanConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["scan_configuration_arn"] = scan_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_code_security_integration(
        self,
        integration_arn: "aws_sdk_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.delete_code_security_integration_response.DeleteCodeSecurityIntegrationResponse":
        """<p>Deletes a code security integration.</p>

        Args:
            integration_arn: <p>The Amazon Resource Name (ARN) of the code security integration to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.delete_code_security_integration_request.DeleteCodeSecurityIntegrationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.delete_code_security_integration_response.DeleteCodeSecurityIntegrationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.delete_code_security_integration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.delete_code_security_integration.delete_code_security_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.delete_code_security_integration_request.DeleteCodeSecurityIntegrationRequest = {}  # type: ignore[typeddict-item]
        input_["integration_arn"] = integration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_code_security_scan_configuration(
        self,
        scan_configuration_arn: "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.delete_code_security_scan_configuration_response.DeleteCodeSecurityScanConfigurationResponse":
        """<p>Deletes a code security scan configuration.</p>

        Args:
            scan_configuration_arn: <p>The Amazon Resource Name (ARN) of the scan configuration to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.delete_code_security_scan_configuration_request.DeleteCodeSecurityScanConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.delete_code_security_scan_configuration_response.DeleteCodeSecurityScanConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.delete_code_security_scan_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.delete_code_security_scan_configuration.delete_code_security_scan_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.delete_code_security_scan_configuration_request.DeleteCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["scan_configuration_arn"] = scan_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_filter(
        self,
        arn: "aws_sdk_inspector2.types.filter_arn.FilterArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.delete_filter_response.DeleteFilterResponse":
        """<p>Deletes a filter resource.</p>

        Args:
            arn: <p>The Amazon Resource Number (ARN) of the filter to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.delete_filter_request.DeleteFilterRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.delete_filter_response.DeleteFilterResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.delete_filter

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.delete_filter.delete_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.delete_filter_request.DeleteFilterRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_organization_configuration(
        self, *, config_overrides: Optional[Inspector2ClientConfig] = None
    ) -> "aws_sdk_inspector2.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse":
        """<p>Describe Amazon Inspector configuration settings for an Amazon Web Services organization.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.describe_organization_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.describe_organization_configuration.describe_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        account_ids: Optional[
            "aws_sdk_inspector2.types.account_id_set.AccountIdSet"
        ] = None,
        resource_types: Optional[
            "aws_sdk_inspector2.types.disable_resource_type_list.DisableResourceTypeList"
        ] = None,
    ) -> "aws_sdk_inspector2.types.disable_response.DisableResponse":
        """<p>Disables Amazon Inspector scans for one or more Amazon Web Services accounts. Disabling all scan types in an account disables the Amazon Inspector service.</p>

        Args:
            account_ids: <p>An array of account IDs you want to disable Amazon Inspector scans for.</p>
            resource_types: <p>The resource scan types you want to disable.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.disable_request.DisableRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.disable_response.DisableResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.disable

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.disable.disable(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.disable_request.DisableRequest = {}  # type: ignore[typeddict-item]
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if resource_types is not None:
            input_["resource_types"] = resource_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_delegated_admin_account(
        self,
        delegated_admin_account_id: "aws_sdk_inspector2.types.account_id.AccountId",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.disable_delegated_admin_account_response.DisableDelegatedAdminAccountResponse":
        """<p>Disables the Amazon Inspector delegated administrator for your organization.</p>

        Args:
            delegated_admin_account_id: <p>The Amazon Web Services account ID of the current Amazon Inspector delegated administrator.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.disable_delegated_admin_account_request.DisableDelegatedAdminAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.disable_delegated_admin_account_response.DisableDelegatedAdminAccountResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.disable_delegated_admin_account

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.disable_delegated_admin_account.disable_delegated_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.disable_delegated_admin_account_request.DisableDelegatedAdminAccountRequest = {}  # type: ignore[typeddict-item]
        input_["delegated_admin_account_id"] = delegated_admin_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_member(
        self,
        account_id: "aws_sdk_inspector2.types.account_id.AccountId",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.disassociate_member_response.DisassociateMemberResponse":
        """<p>Disassociates a member account from an Amazon Inspector delegated administrator.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID of the member account to disassociate.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.disassociate_member_request.DisassociateMemberRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.disassociate_member_response.DisassociateMemberResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.disassociate_member

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.disassociate_member.disassociate_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.disassociate_member_request.DisassociateMemberRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable(
        self,
        resource_types: "aws_sdk_inspector2.types.enable_resource_type_list.EnableResourceTypeList",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        account_ids: Optional[
            "aws_sdk_inspector2.types.account_id_set.AccountIdSet"
        ] = None,
        client_token: Optional[
            "aws_sdk_inspector2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_inspector2.types.enable_response.EnableResponse":
        """<p>Enables Amazon Inspector scans for one or more Amazon Web Services accounts.</p>

        Args:
            account_ids: <p>A list of account IDs you want to enable Amazon Inspector scans for.</p>
            resource_types: <p>The resource scan types you want to enable.</p>
            client_token: <p>The idempotency token for the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.enable_request.EnableRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.enable_response.EnableResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.enable

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.enable.enable(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.enable_request.EnableRequest = {}  # type: ignore[typeddict-item]
        if account_ids is not None:
            input_["account_ids"] = account_ids
        input_["resource_types"] = resource_types
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_delegated_admin_account(
        self,
        delegated_admin_account_id: "aws_sdk_inspector2.types.account_id.AccountId",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        client_token: Optional[
            "aws_sdk_inspector2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_inspector2.types.enable_delegated_admin_account_response.EnableDelegatedAdminAccountResponse":
        """<p>Enables the Amazon Inspector delegated administrator for your Organizations organization.</p>

        Args:
            delegated_admin_account_id: <p>The Amazon Web Services account ID of the Amazon Inspector delegated administrator.</p>
            client_token: <p>The idempotency token for the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.enable_delegated_admin_account_request.EnableDelegatedAdminAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.enable_delegated_admin_account_response.EnableDelegatedAdminAccountResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.enable_delegated_admin_account

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.enable_delegated_admin_account.enable_delegated_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.enable_delegated_admin_account_request.EnableDelegatedAdminAccountRequest = {}  # type: ignore[typeddict-item]
        input_["delegated_admin_account_id"] = delegated_admin_account_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cis_scan_report(
        self,
        scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        target_accounts: Optional[
            "aws_sdk_inspector2.types.report_target_accounts.ReportTargetAccounts"
        ] = None,
        report_format: Optional[
            "aws_sdk_inspector2.types.cis_report_format.CisReportFormat"
        ] = None,
    ) -> (
        "aws_sdk_inspector2.types.get_cis_scan_report_response.GetCisScanReportResponse"
    ):
        """<p>Retrieves a CIS scan report.</p>

        Args:
            scan_arn: <p>The scan ARN.</p>
            target_accounts: <p>The target accounts.</p>
            report_format: <p> The format of the report. Valid values are <code>PDF</code> and <code>CSV</code>. If no value is specified, the report format defaults to <code>PDF</code>. </p>

        Examples:
            Sample GetCisScanReport Call

            >>> client.get_cis_scan_report(scan_arn='arn:aws:inspector2:us-east-1:123412341234:owner/123412341234/cis-scan/624b746d-e080-44ae-8c1d-48e653365a38', report_format='PDF')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_cis_scan_report_request.GetCisScanReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_cis_scan_report_response.GetCisScanReportResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_cis_scan_report

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_cis_scan_report.get_cis_scan_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_cis_scan_report_request.GetCisScanReportRequest = {}  # type: ignore[typeddict-item]
        input_["scan_arn"] = scan_arn
        if target_accounts is not None:
            input_["target_accounts"] = target_accounts
        if report_format is not None:
            input_["report_format"] = report_format

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cis_scan_result_details(
        self,
        scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn",
        target_resource_id: "aws_sdk_inspector2.types.resource_id.ResourceId",
        account_id: "aws_sdk_inspector2.types.account_id.AccountId",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.cis_scan_result_details_filter_criteria.CisScanResultDetailsFilterCriteria"
        ] = None,
        sort_by: Optional[
            "aws_sdk_inspector2.types.cis_scan_result_details_sort_by.CisScanResultDetailsSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.get_cis_scan_result_details_max_results.GetCisScanResultDetailsMaxResults"
        ] = None,
    ) -> "aws_sdk_inspector2.types.get_cis_scan_result_details_response.GetCisScanResultDetailsResponse":
        """<p>Retrieves CIS scan result details.</p>

        Args:
            scan_arn: <p>The scan ARN.</p>
            target_resource_id: <p>The target resource ID.</p>
            account_id: <p>The account ID.</p>
            filter_criteria: <p>The filter criteria.</p>
            sort_by: <p>The sort by order.</p>
            sort_order: <p>The sort order.</p>
            next_token: <p>The pagination token from a previous request that's used to retrieve the next page of results.</p>
            max_results: <p>The maximum number of CIS scan result details to be returned in a single page of results.</p>

        Examples:
            Sample GetCisScanResultDetails Call

            >>> client.get_cis_scan_result_details(scan_arn='arn:aws:inspector2:us-east-1:123412341234:owner/123412341234/cis-scan/624b746d-e080-44ae-8c1d-48e653365a38', target_resource_id='i-12341234', account_id='123412341234')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_cis_scan_result_details_request.GetCisScanResultDetailsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_cis_scan_result_details_response.GetCisScanResultDetailsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_cis_scan_result_details

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_cis_scan_result_details.get_cis_scan_result_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_cis_scan_result_details_request.GetCisScanResultDetailsRequest = {}  # type: ignore[typeddict-item]
        input_["scan_arn"] = scan_arn
        input_["target_resource_id"] = target_resource_id
        input_["account_id"] = account_id
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    def iter_get_cis_scan_result_details(
        self,
        scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn",
        target_resource_id: "aws_sdk_inspector2.types.resource_id.ResourceId",
        account_id: "aws_sdk_inspector2.types.account_id.AccountId",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.cis_scan_result_details_filter_criteria.CisScanResultDetailsFilterCriteria"
        ] = None,
        sort_by: Optional[
            "aws_sdk_inspector2.types.cis_scan_result_details_sort_by.CisScanResultDetailsSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.get_cis_scan_result_details_max_results.GetCisScanResultDetailsMaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.cis_scan_result_details.CisScanResultDetails]":
        _token = next_token
        while True:
            _response = self.get_cis_scan_result_details(
                scan_arn,
                target_resource_id,
                account_id,
                config_overrides=config_overrides,
                filter_criteria=filter_criteria,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("scan_result_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_clusters_for_image(
        self,
        filter: "aws_sdk_inspector2.types.cluster_for_image_filter_criteria.ClusterForImageFilterCriteria",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_inspector2.types.get_clusters_for_image_next_token.GetClustersForImageNextToken"
        ] = None,
    ) -> "aws_sdk_inspector2.types.get_clusters_for_image_response.GetClustersForImageResponse":
        """<p>Returns a list of clusters and metadata associated with an image.</p>

        Args:
            filter: <p>The resource Id for the Amazon ECR image.</p>
            max_results: <p>The maximum number of results to be returned in a single page of results.</p>
            next_token: <p>The pagination token from a previous request used to retrieve the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_clusters_for_image_request.GetClustersForImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_clusters_for_image_response.GetClustersForImageResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_clusters_for_image

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_clusters_for_image.get_clusters_for_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_clusters_for_image_request.GetClustersForImageRequest = {}  # type: ignore[typeddict-item]
        input_["filter"] = filter
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

    def iter_get_clusters_for_image(
        self,
        filter: "aws_sdk_inspector2.types.cluster_for_image_filter_criteria.ClusterForImageFilterCriteria",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_inspector2.types.get_clusters_for_image_next_token.GetClustersForImageNextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.cluster_information.ClusterInformation]":
        _token = next_token
        while True:
            _response = self.get_clusters_for_image(
                filter,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cluster",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_code_security_integration(
        self,
        integration_arn: "aws_sdk_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        tags: Optional["aws_sdk_inspector2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_inspector2.types.get_code_security_integration_response.GetCodeSecurityIntegrationResponse":
        """<p>Retrieves information about a code security integration.</p>

        Args:
            integration_arn: <p>The Amazon Resource Name (ARN) of the code security integration to retrieve.</p>
            tags: <p>The tags associated with the code security integration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_code_security_integration_request.GetCodeSecurityIntegrationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_code_security_integration_response.GetCodeSecurityIntegrationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_code_security_integration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_code_security_integration.get_code_security_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_code_security_integration_request.GetCodeSecurityIntegrationRequest = {}  # type: ignore[typeddict-item]
        input_["integration_arn"] = integration_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_code_security_scan(
        self,
        resource: "aws_sdk_inspector2.types.code_security_resource.CodeSecurityResource",
        scan_id: "aws_sdk_inspector2.types.code_security_uuid.CodeSecurityUuid",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.get_code_security_scan_response.GetCodeSecurityScanResponse":
        """<p>Retrieves information about a specific code security scan.</p>

        Args:
            resource: <p>The resource identifier for the code repository that was scanned.</p>
            scan_id: <p>The unique identifier of the scan to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_code_security_scan_request.GetCodeSecurityScanRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_code_security_scan_response.GetCodeSecurityScanResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_code_security_scan

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_code_security_scan.get_code_security_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_code_security_scan_request.GetCodeSecurityScanRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource
        input_["scan_id"] = scan_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_code_security_scan_configuration(
        self,
        scan_configuration_arn: "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.get_code_security_scan_configuration_response.GetCodeSecurityScanConfigurationResponse":
        """<p>Retrieves information about a code security scan configuration.</p>

        Args:
            scan_configuration_arn: <p>The Amazon Resource Name (ARN) of the scan configuration to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_code_security_scan_configuration_request.GetCodeSecurityScanConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_code_security_scan_configuration_response.GetCodeSecurityScanConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_code_security_scan_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_code_security_scan_configuration.get_code_security_scan_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_code_security_scan_configuration_request.GetCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["scan_configuration_arn"] = scan_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_configuration(
        self, *, config_overrides: Optional[Inspector2ClientConfig] = None
    ) -> "aws_sdk_inspector2.types.get_configuration_response.GetConfigurationResponse":
        """<p>Retrieves setting configurations for Inspector scans.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_configuration_request.GetConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_configuration_response.GetConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_configuration.get_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_configuration_request.GetConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_delegated_admin_account(
        self, *, config_overrides: Optional[Inspector2ClientConfig] = None
    ) -> "aws_sdk_inspector2.types.get_delegated_admin_account_response.GetDelegatedAdminAccountResponse":
        """<p>Retrieves information about the Amazon Inspector delegated administrator for your organization.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_delegated_admin_account_request.GetDelegatedAdminAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_delegated_admin_account_response.GetDelegatedAdminAccountResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_delegated_admin_account

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_delegated_admin_account.get_delegated_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_delegated_admin_account_request.GetDelegatedAdminAccountRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_ec2_deep_inspection_configuration(
        self, *, config_overrides: Optional[Inspector2ClientConfig] = None
    ) -> "aws_sdk_inspector2.types.get_ec2_deep_inspection_configuration_response.GetEc2DeepInspectionConfigurationResponse":
        """<p>Retrieves the activation status of Amazon Inspector deep inspection and custom paths associated with your account. </p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_ec2_deep_inspection_configuration_request.GetEc2DeepInspectionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_ec2_deep_inspection_configuration_response.GetEc2DeepInspectionConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_ec2_deep_inspection_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_ec2_deep_inspection_configuration.get_ec2_deep_inspection_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_ec2_deep_inspection_configuration_request.GetEc2DeepInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_encryption_key(
        self,
        scan_type: "aws_sdk_inspector2.types.scan_type.ScanType",
        resource_type: "aws_sdk_inspector2.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> (
        "aws_sdk_inspector2.types.get_encryption_key_response.GetEncryptionKeyResponse"
    ):
        """<p>Gets an encryption key.</p>

        Args:
            scan_type: <p>The scan type the key encrypts.</p>
            resource_type: <p>The resource type the key encrypts.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_encryption_key_request.GetEncryptionKeyRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_encryption_key_response.GetEncryptionKeyResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_encryption_key

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_encryption_key.get_encryption_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_encryption_key_request.GetEncryptionKeyRequest = {}  # type: ignore[typeddict-item]
        input_["scan_type"] = scan_type
        input_["resource_type"] = resource_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_findings_report_status(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        report_id: Optional["aws_sdk_inspector2.types.report_id.ReportId"] = None,
    ) -> "aws_sdk_inspector2.types.get_findings_report_status_response.GetFindingsReportStatusResponse":
        """<p>Gets the status of a findings report.</p>

        Args:
            report_id: <p>The ID of the report to retrieve the status of.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_findings_report_status_request.GetFindingsReportStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_findings_report_status_response.GetFindingsReportStatusResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_findings_report_status

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_findings_report_status.get_findings_report_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_findings_report_status_request.GetFindingsReportStatusRequest = {}  # type: ignore[typeddict-item]
        if report_id is not None:
            input_["report_id"] = report_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_member(
        self,
        account_id: "aws_sdk_inspector2.types.account_id.AccountId",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.get_member_response.GetMemberResponse":
        """<p>Gets member information for your organization.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID of the member account to retrieve information on.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_member_request.GetMemberRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_member_response.GetMemberResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_member

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_member.get_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_member_request.GetMemberRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_sbom_export(
        self,
        report_id: "aws_sdk_inspector2.types.report_id.ReportId",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.get_sbom_export_response.GetSbomExportResponse":
        """<p>Gets details of a software bill of materials (SBOM) report.</p>

        Args:
            report_id: <p>The report ID of the SBOM export to get details for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.get_sbom_export_request.GetSbomExportRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.get_sbom_export_response.GetSbomExportResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.get_sbom_export

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.get_sbom_export.get_sbom_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.get_sbom_export_request.GetSbomExportRequest = {}  # type: ignore[typeddict-item]
        input_["report_id"] = report_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_account_permissions(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        service: Optional["aws_sdk_inspector2.types.service.Service"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_account_permissions_max_results.ListAccountPermissionsMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_inspector2.types.list_account_permissions_response.ListAccountPermissionsResponse":
        """<p> Lists the permissions an account has to configure Amazon Inspector. If the account is a member account or standalone account with resources managed by an Organizations policy, the operation returns fewer permissions. </p>

        Args:
            service: <p>The service scan type to check permissions for.</p>
            max_results: <p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_account_permissions_request.ListAccountPermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_account_permissions_response.ListAccountPermissionsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_account_permissions

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_account_permissions.list_account_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_account_permissions_request.ListAccountPermissionsRequest = {}  # type: ignore[typeddict-item]
        if service is not None:
            input_["service"] = service
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

    def iter_list_account_permissions(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        service: Optional["aws_sdk_inspector2.types.service.Service"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_account_permissions_max_results.ListAccountPermissionsMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.permission.Permission]":
        _token = next_token
        while True:
            _response = self.list_account_permissions(
                config_overrides=config_overrides,
                service=service,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("permissions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cis_scan_configurations(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.list_cis_scan_configurations_filter_criteria.ListCisScanConfigurationsFilterCriteria"
        ] = None,
        sort_by: Optional[
            "aws_sdk_inspector2.types.cis_scan_configurations_sort_by.CisScanConfigurationsSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_cis_scan_configurations_max_results.ListCisScanConfigurationsMaxResults"
        ] = None,
    ) -> "aws_sdk_inspector2.types.list_cis_scan_configurations_response.ListCisScanConfigurationsResponse":
        """<p>Lists CIS scan configurations.</p>

        Args:
            filter_criteria: <p>The CIS scan configuration filter criteria.</p>
            sort_by: <p>The CIS scan configuration sort by order.</p>
            sort_order: <p>The CIS scan configuration sort order order.</p>
            next_token: <p>The pagination token from a previous request that's used to retrieve the next page of results.</p>
            max_results: <p>The maximum number of CIS scan configurations to be returned in a single page of results.</p>

        Examples:
            Sample ListCisScanConfigurations Call

            >>> client.list_cis_scan_configurations()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_cis_scan_configurations_request.ListCisScanConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_cis_scan_configurations_response.ListCisScanConfigurationsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_cis_scan_configurations

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_cis_scan_configurations.list_cis_scan_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_cis_scan_configurations_request.ListCisScanConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    def iter_list_cis_scan_configurations(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.list_cis_scan_configurations_filter_criteria.ListCisScanConfigurationsFilterCriteria"
        ] = None,
        sort_by: Optional[
            "aws_sdk_inspector2.types.cis_scan_configurations_sort_by.CisScanConfigurationsSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_cis_scan_configurations_max_results.ListCisScanConfigurationsMaxResults"
        ] = None,
    ) -> (
        "Iterator[aws_sdk_inspector2.types.cis_scan_configuration.CisScanConfiguration]"
    ):
        _token = next_token
        while True:
            _response = self.list_cis_scan_configurations(
                config_overrides=config_overrides,
                filter_criteria=filter_criteria,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("scan_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cis_scan_results_aggregated_by_checks(
        self,
        scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_aggregated_by_checks_filter_criteria.CisScanResultsAggregatedByChecksFilterCriteria"
        ] = None,
        sort_by: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_aggregated_by_checks_sort_by.CisScanResultsAggregatedByChecksSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_max_results.CisScanResultsMaxResults"
        ] = None,
    ) -> "aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_checks_response.ListCisScanResultsAggregatedByChecksResponse":
        """<p>Lists scan results aggregated by checks.</p>

        Args:
            scan_arn: <p>The scan ARN.</p>
            filter_criteria: <p>The filter criteria.</p>
            sort_by: <p>The sort by order.</p>
            sort_order: <p>The sort order.</p>
            next_token: <p>The pagination token from a previous request that's used to retrieve the next page of results.</p>
            max_results: <p>The maximum number of scan results aggregated by checks to be returned in a single page of results.</p>

        Examples:
            Sample ListCisScanResultsAggregatedByChecks Call

            >>> client.list_cis_scan_results_aggregated_by_checks(scan_arn='arn:aws:inspector2:us-east-1:123412341234:owner/123412341234/cis-scan/624b746d-e080-44ae-8c1d-48e653365a38')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_checks_request.ListCisScanResultsAggregatedByChecksRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_checks_response.ListCisScanResultsAggregatedByChecksResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_cis_scan_results_aggregated_by_checks

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_cis_scan_results_aggregated_by_checks.list_cis_scan_results_aggregated_by_checks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_checks_request.ListCisScanResultsAggregatedByChecksRequest = {}  # type: ignore[typeddict-item]
        input_["scan_arn"] = scan_arn
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    def iter_list_cis_scan_results_aggregated_by_checks(
        self,
        scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_aggregated_by_checks_filter_criteria.CisScanResultsAggregatedByChecksFilterCriteria"
        ] = None,
        sort_by: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_aggregated_by_checks_sort_by.CisScanResultsAggregatedByChecksSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_max_results.CisScanResultsMaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.cis_check_aggregation.CisCheckAggregation]":
        _token = next_token
        while True:
            _response = self.list_cis_scan_results_aggregated_by_checks(
                scan_arn,
                config_overrides=config_overrides,
                filter_criteria=filter_criteria,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("check_aggregations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cis_scan_results_aggregated_by_target_resource(
        self,
        scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria.CisScanResultsAggregatedByTargetResourceFilterCriteria"
        ] = None,
        sort_by: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by.CisScanResultsAggregatedByTargetResourceSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_max_results.CisScanResultsMaxResults"
        ] = None,
    ) -> "aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_target_resource_response.ListCisScanResultsAggregatedByTargetResourceResponse":
        """<p>Lists scan results aggregated by a target resource.</p>

        Args:
            scan_arn: <p>The scan ARN.</p>
            filter_criteria: <p>The filter criteria.</p>
            sort_by: <p>The sort by order.</p>
            sort_order: <p>The sort order.</p>
            next_token: <p>The pagination token from a previous request that's used to retrieve the next page of results.</p>
            max_results: <p>The maximum number of scan results aggregated by a target resource to be returned in a single page of results.</p>

        Examples:
            Sample ListCisScanResultsAggregatedByTargetResource Call

            >>> client.list_cis_scan_results_aggregated_by_target_resource(scan_arn='arn:aws:inspector2:us-east-1:123412341234:owner/123412341234/cis-scan/624b746d-e080-44ae-8c1d-48e653365a38')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_target_resource_request.ListCisScanResultsAggregatedByTargetResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_target_resource_response.ListCisScanResultsAggregatedByTargetResourceResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_cis_scan_results_aggregated_by_target_resource

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_cis_scan_results_aggregated_by_target_resource.list_cis_scan_results_aggregated_by_target_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_cis_scan_results_aggregated_by_target_resource_request.ListCisScanResultsAggregatedByTargetResourceRequest = {}  # type: ignore[typeddict-item]
        input_["scan_arn"] = scan_arn
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    def iter_list_cis_scan_results_aggregated_by_target_resource(
        self,
        scan_arn: "aws_sdk_inspector2.types.cis_scan_arn.CisScanArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria.CisScanResultsAggregatedByTargetResourceFilterCriteria"
        ] = None,
        sort_by: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by.CisScanResultsAggregatedByTargetResourceSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.cis_scan_results_max_results.CisScanResultsMaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.cis_target_resource_aggregation.CisTargetResourceAggregation]":
        _token = next_token
        while True:
            _response = self.list_cis_scan_results_aggregated_by_target_resource(
                scan_arn,
                config_overrides=config_overrides,
                filter_criteria=filter_criteria,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("target_resource_aggregations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cis_scans(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.list_cis_scans_filter_criteria.ListCisScansFilterCriteria"
        ] = None,
        detail_level: Optional[
            "aws_sdk_inspector2.types.list_cis_scans_detail_level.ListCisScansDetailLevel"
        ] = None,
        sort_by: Optional[
            "aws_sdk_inspector2.types.list_cis_scans_sort_by.ListCisScansSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_cis_scans_max_results.ListCisScansMaxResults"
        ] = None,
    ) -> "aws_sdk_inspector2.types.list_cis_scans_response.ListCisScansResponse":
        """<p>Returns a CIS scan list.</p>

        Args:
            filter_criteria: <p>The CIS scan filter criteria.</p>
            detail_level: <p>The detail applied to the CIS scan.</p>
            sort_by: <p>The CIS scans sort by order.</p>
            sort_order: <p>The CIS scans sort order.</p>
            next_token: <p>The pagination token from a previous request that's used to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to be returned.</p>

        Examples:
            Sample ListCisScans Call

            >>> client.list_cis_scans()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_cis_scans_request.ListCisScansRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_cis_scans_response.ListCisScansResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_cis_scans

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_cis_scans.list_cis_scans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_cis_scans_request.ListCisScansRequest = {}  # type: ignore[typeddict-item]
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if detail_level is not None:
            input_["detail_level"] = detail_level
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    def iter_list_cis_scans(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.list_cis_scans_filter_criteria.ListCisScansFilterCriteria"
        ] = None,
        detail_level: Optional[
            "aws_sdk_inspector2.types.list_cis_scans_detail_level.ListCisScansDetailLevel"
        ] = None,
        sort_by: Optional[
            "aws_sdk_inspector2.types.list_cis_scans_sort_by.ListCisScansSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_cis_scans_max_results.ListCisScansMaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.cis_scan.CisScan]":
        _token = next_token
        while True:
            _response = self.list_cis_scans(
                config_overrides=config_overrides,
                filter_criteria=filter_criteria,
                detail_level=detail_level,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("scans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_code_security_integrations(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_inspector2.types.list_code_security_integrations_response.ListCodeSecurityIntegrationsResponse":
        """<p>Lists all code security integrations in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_code_security_integrations_request.ListCodeSecurityIntegrationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_code_security_integrations_response.ListCodeSecurityIntegrationsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_code_security_integrations

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_code_security_integrations.list_code_security_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_code_security_integrations_request.ListCodeSecurityIntegrationsRequest = {}  # type: ignore[typeddict-item]
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

    def list_code_security_scan_configuration_associations(
        self,
        scan_configuration_arn: "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_inspector2.types.list_code_security_scan_configuration_associations_response.ListCodeSecurityScanConfigurationAssociationsResponse":
        """<p>Lists the associations between code repositories and Amazon Inspector code security scan configurations.</p>

        Args:
            scan_configuration_arn: <p>The Amazon Resource Name (ARN) of the scan configuration to list associations for.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>
            max_results: <p>The maximum number of results to return in the response. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_code_security_scan_configuration_associations_request.ListCodeSecurityScanConfigurationAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_code_security_scan_configuration_associations_response.ListCodeSecurityScanConfigurationAssociationsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_code_security_scan_configuration_associations

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_code_security_scan_configuration_associations.list_code_security_scan_configuration_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_code_security_scan_configuration_associations_request.ListCodeSecurityScanConfigurationAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["scan_configuration_arn"] = scan_configuration_arn
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

    def list_code_security_scan_configurations(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_inspector2.types.list_code_security_scan_configurations_response.ListCodeSecurityScanConfigurationsResponse":
        """<p>Lists all code security scan configurations in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_code_security_scan_configurations_request.ListCodeSecurityScanConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_code_security_scan_configurations_response.ListCodeSecurityScanConfigurationsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_code_security_scan_configurations

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_code_security_scan_configurations.list_code_security_scan_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_code_security_scan_configurations_request.ListCodeSecurityScanConfigurationsRequest = {}  # type: ignore[typeddict-item]
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

    def list_coverage(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_coverage_max_results.ListCoverageMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.coverage_filter_criteria.CoverageFilterCriteria"
        ] = None,
    ) -> "aws_sdk_inspector2.types.list_coverage_response.ListCoverageResponse":
        """<p>Lists coverage details for your environment.</p>

        Args:
            max_results: <p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>
            filter_criteria: <p>An object that contains details on the filters to apply to the coverage data for your environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_coverage_request.ListCoverageRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_coverage_response.ListCoverageResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_coverage

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_coverage.list_coverage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_coverage_request.ListCoverageRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_coverage(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_coverage_max_results.ListCoverageMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.coverage_filter_criteria.CoverageFilterCriteria"
        ] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.covered_resource.CoveredResource]":
        _token = next_token
        while True:
            _response = self.list_coverage(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter_criteria=filter_criteria,
            )
            _page = _resolve_path(_response, ("covered_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_coverage_statistics(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.coverage_filter_criteria.CoverageFilterCriteria"
        ] = None,
        group_by: Optional["aws_sdk_inspector2.types.group_key.GroupKey"] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_inspector2.types.list_coverage_statistics_response.ListCoverageStatisticsResponse":
        """<p>Lists Amazon Inspector coverage statistics for your environment.</p>

        Args:
            filter_criteria: <p>An object that contains details on the filters to apply to the coverage data for your environment.</p>
            group_by: <p>The value to group the results by.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_coverage_statistics_request.ListCoverageStatisticsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_coverage_statistics_response.ListCoverageStatisticsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_coverage_statistics

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_coverage_statistics.list_coverage_statistics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_coverage_statistics_request.ListCoverageStatisticsRequest = {}  # type: ignore[typeddict-item]
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if group_by is not None:
            input_["group_by"] = group_by
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_coverage_statistics(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.coverage_filter_criteria.CoverageFilterCriteria"
        ] = None,
        group_by: Optional["aws_sdk_inspector2.types.group_key.GroupKey"] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.counts.Counts]":
        _token = next_token
        while True:
            _response = self.list_coverage_statistics(
                config_overrides=config_overrides,
                filter_criteria=filter_criteria,
                group_by=group_by,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("counts_by_group",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_delegated_admin_accounts(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_delegated_admin_max_results.ListDelegatedAdminMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_inspector2.types.list_delegated_admin_accounts_response.ListDelegatedAdminAccountsResponse":
        """<p>Lists information about the Amazon Inspector delegated administrator of your organization.</p>

        Args:
            max_results: <p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_delegated_admin_accounts_request.ListDelegatedAdminAccountsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_delegated_admin_accounts_response.ListDelegatedAdminAccountsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_delegated_admin_accounts

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_delegated_admin_accounts.list_delegated_admin_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_delegated_admin_accounts_request.ListDelegatedAdminAccountsRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_delegated_admin_accounts(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_delegated_admin_max_results.ListDelegatedAdminMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.delegated_admin_account.DelegatedAdminAccount]":
        _token = next_token
        while True:
            _response = self.list_delegated_admin_accounts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("delegated_admin_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_filters(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        arns: Optional["aws_sdk_inspector2.types.filter_arn_list.FilterArnList"] = None,
        action: Optional["aws_sdk_inspector2.types.filter_action.FilterAction"] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_filter_max_results.ListFilterMaxResults"
        ] = None,
    ) -> "aws_sdk_inspector2.types.list_filters_response.ListFiltersResponse":
        """<p>Lists the filters associated with your account.</p>

        Args:
            arns: <p>The Amazon resource number (ARN) of the filter.</p>
            action: <p>The action the filter applies to matched findings.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>
            max_results: <p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_filters_request.ListFiltersRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_filters_response.ListFiltersResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_filters

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_filters.list_filters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_filters_request.ListFiltersRequest = {}  # type: ignore[typeddict-item]
        if arns is not None:
            input_["arns"] = arns
        if action is not None:
            input_["action"] = action
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

    def iter_list_filters(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        arns: Optional["aws_sdk_inspector2.types.filter_arn_list.FilterArnList"] = None,
        action: Optional["aws_sdk_inspector2.types.filter_action.FilterAction"] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_filter_max_results.ListFilterMaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.filter.Filter]":
        _token = next_token
        while True:
            _response = self.list_filters(
                config_overrides=config_overrides,
                arns=arns,
                action=action,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("filters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_finding_aggregations(
        self,
        aggregation_type: "aws_sdk_inspector2.types.aggregation_type.AggregationType",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_finding_aggregations_max_results.ListFindingAggregationsMaxResults"
        ] = None,
        account_ids: Optional[
            "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
        ] = None,
        aggregation_request: Optional[
            "aws_sdk_inspector2.types.aggregation_request.AggregationRequest"
        ] = None,
    ) -> "aws_sdk_inspector2.types.list_finding_aggregations_response.ListFindingAggregationsResponse":
        """<p>Lists aggregated finding data for your environment based on specific criteria.</p>

        Args:
            aggregation_type: <p>The type of the aggregation request.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>
            max_results: <p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>
            account_ids: <p>The Amazon Web Services account IDs to retrieve finding aggregation data for.</p>
            aggregation_request: <p>Details of the aggregation request that is used to filter your aggregation results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_finding_aggregations_request.ListFindingAggregationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_finding_aggregations_response.ListFindingAggregationsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_finding_aggregations

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_finding_aggregations.list_finding_aggregations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_finding_aggregations_request.ListFindingAggregationsRequest = {}  # type: ignore[typeddict-item]
        input_["aggregation_type"] = aggregation_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if account_ids is not None:
            input_["account_ids"] = account_ids
        if aggregation_request is not None:
            input_["aggregation_request"] = aggregation_request

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_finding_aggregations(
        self,
        aggregation_type: "aws_sdk_inspector2.types.aggregation_type.AggregationType",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_finding_aggregations_max_results.ListFindingAggregationsMaxResults"
        ] = None,
        account_ids: Optional[
            "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
        ] = None,
        aggregation_request: Optional[
            "aws_sdk_inspector2.types.aggregation_request.AggregationRequest"
        ] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.aggregation_response.AggregationResponse]":
        _token = next_token
        while True:
            _response = self.list_finding_aggregations(
                aggregation_type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                account_ids=account_ids,
                aggregation_request=aggregation_request,
            )
            _page = _resolve_path(_response, ("responses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_findings(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_findings_max_results.ListFindingsMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.filter_criteria.FilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_inspector2.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "aws_sdk_inspector2.types.list_findings_response.ListFindingsResponse":
        """<p>Lists findings for your environment.</p>

        Args:
            max_results: <p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>
            filter_criteria: <p>Details on the filters to apply to your finding results.</p>
            sort_criteria: <p>Details on the sort criteria to apply to your finding results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_findings_request.ListFindingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_findings_response.ListFindingsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_findings

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_findings.list_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_findings_request.ListFindingsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_findings(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_findings_max_results.ListFindingsMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.filter_criteria.FilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_inspector2.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.finding.Finding]":
        _token = next_token
        while True:
            _response = self.list_findings(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter_criteria=filter_criteria,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("findings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_members(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        only_associated: Optional[bool] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_members_max_results.ListMembersMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_inspector2.types.list_members_response.ListMembersResponse":
        """<p>List members associated with the Amazon Inspector delegated administrator for your organization.</p>

        Args:
            only_associated: <p>Specifies whether to list only currently associated members if <code>True</code> or to list all members within the organization if <code>False</code>.</p>
            max_results: <p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_members_request.ListMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_members_response.ListMembersResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_members

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_members.list_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_members_request.ListMembersRequest = {}  # type: ignore[typeddict-item]
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
        config_overrides: Optional[Inspector2ClientConfig] = None,
        only_associated: Optional[bool] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_members_max_results.ListMembersMaxResults"
        ] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.member.Member]":
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_inspector2.types.arn.Arn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags attached to a given resource.</p>

        Args:
            resource_arn: <p>The Amazon resource number (ARN) of the resource to list tags of.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_tags_for_resource

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_usage_totals(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_usage_totals_max_results.ListUsageTotalsMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_inspector2.types.list_usage_totals_next_token.ListUsageTotalsNextToken"
        ] = None,
        account_ids: Optional[
            "aws_sdk_inspector2.types.usage_account_id_list.UsageAccountIdList"
        ] = None,
    ) -> "aws_sdk_inspector2.types.list_usage_totals_response.ListUsageTotalsResponse":
        """<p>Lists the Amazon Inspector usage totals over the last 30 days.</p>

        Args:
            max_results: <p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>
            account_ids: <p>The Amazon Web Services account IDs to retrieve usage totals for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.list_usage_totals_request.ListUsageTotalsRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.list_usage_totals_response.ListUsageTotalsResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.list_usage_totals

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.list_usage_totals.list_usage_totals(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.list_usage_totals_request.ListUsageTotalsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_ids is not None:
            input_["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_usage_totals(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_inspector2.types.list_usage_totals_max_results.ListUsageTotalsMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_inspector2.types.list_usage_totals_next_token.ListUsageTotalsNextToken"
        ] = None,
        account_ids: Optional[
            "aws_sdk_inspector2.types.usage_account_id_list.UsageAccountIdList"
        ] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.usage_total.UsageTotal]":
        _token = next_token
        while True:
            _response = self.list_usage_totals(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                account_ids=account_ids,
            )
            _page = _resolve_path(_response, ("totals",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def reset_encryption_key(
        self,
        scan_type: "aws_sdk_inspector2.types.scan_type.ScanType",
        resource_type: "aws_sdk_inspector2.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.reset_encryption_key_response.ResetEncryptionKeyResponse":
        """<p>Resets an encryption key. After the key is reset your resources will be encrypted by an Amazon Web Services owned key.</p>

        Args:
            scan_type: <p>The scan type the key encrypts.</p>
            resource_type: <p>The resource type the key encrypts.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.reset_encryption_key_request.ResetEncryptionKeyRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.reset_encryption_key_response.ResetEncryptionKeyResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.reset_encryption_key

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.reset_encryption_key.reset_encryption_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.reset_encryption_key_request.ResetEncryptionKeyRequest = {}  # type: ignore[typeddict-item]
        input_["scan_type"] = scan_type
        input_["resource_type"] = resource_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_vulnerabilities(
        self,
        filter_criteria: "aws_sdk_inspector2.types.search_vulnerabilities_filter_criteria.SearchVulnerabilitiesFilterCriteria",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_inspector2.types.search_vulnerabilities_response.SearchVulnerabilitiesResponse":
        """<p>Lists Amazon Inspector coverage details for a specific vulnerability.</p>

        Args:
            filter_criteria: <p>The criteria used to filter the results of a vulnerability search.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.search_vulnerabilities_request.SearchVulnerabilitiesRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.search_vulnerabilities_response.SearchVulnerabilitiesResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.search_vulnerabilities

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.search_vulnerabilities.search_vulnerabilities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.search_vulnerabilities_request.SearchVulnerabilitiesRequest = {}  # type: ignore[typeddict-item]
        input_["filter_criteria"] = filter_criteria
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_search_vulnerabilities(
        self,
        filter_criteria: "aws_sdk_inspector2.types.search_vulnerabilities_filter_criteria.SearchVulnerabilitiesFilterCriteria",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        next_token: Optional["aws_sdk_inspector2.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_inspector2.types.vulnerability.Vulnerability]":
        _token = next_token
        while True:
            _response = self.search_vulnerabilities(
                filter_criteria,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("vulnerabilities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def send_cis_session_health(
        self,
        scan_job_id: "aws_sdk_inspector2.types.uuid.UUID",
        session_token: "aws_sdk_inspector2.types.uuid.UUID",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.send_cis_session_health_response.SendCisSessionHealthResponse":
        """<p> Sends a CIS session health. This API is used by the Amazon Inspector SSM plugin to communicate with the Amazon Inspector service. The Amazon Inspector SSM plugin calls this API to start a CIS scan session for the scan ID supplied by the service. </p>

        Args:
            scan_job_id: <p>A unique identifier for the scan job.</p>
            session_token: <p>The unique token that identifies the CIS session.</p>

        Examples:
            Sample SendCisSessionHealth Call

            >>> client.send_cis_session_health(scan_job_id='624b746d-e080-44ae-8c1d-48e653365a38', session_token='624b746d-e080-44ae-8c1d-48e653365a31')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.send_cis_session_health_request.SendCisSessionHealthRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.send_cis_session_health_response.SendCisSessionHealthResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.send_cis_session_health

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.send_cis_session_health.send_cis_session_health(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.send_cis_session_health_request.SendCisSessionHealthRequest = {}  # type: ignore[typeddict-item]
        input_["scan_job_id"] = scan_job_id
        input_["session_token"] = session_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_cis_session_telemetry(
        self,
        scan_job_id: "aws_sdk_inspector2.types.uuid.UUID",
        session_token: "aws_sdk_inspector2.types.uuid.UUID",
        messages: "aws_sdk_inspector2.types.cis_session_messages.CisSessionMessages",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.send_cis_session_telemetry_response.SendCisSessionTelemetryResponse":
        """<p> Sends a CIS session telemetry. This API is used by the Amazon Inspector SSM plugin to communicate with the Amazon Inspector service. The Amazon Inspector SSM plugin calls this API to start a CIS scan session for the scan ID supplied by the service. </p>

        Args:
            scan_job_id: <p>A unique identifier for the scan job.</p>
            session_token: <p>The unique token that identifies the CIS session.</p>
            messages: <p>The CIS session telemetry messages.</p>

        Examples:
            Sample SendCisSessionTelemetry Call

            >>> client.send_cis_session_telemetry(scan_job_id='624b746d-e080-44ae-8c1d-48e653365a38', session_token='624b746d-e080-44ae-8c1d-48e653365a31', messages=[{'ruleId': '1.12.1', 'status': 'FAILED', 'cisRuleDetails': 'dGVzdCBleGFtcGxlCg=='}, {'ruleId': '1.2.1', 'status': 'PASSED', 'cisRuleDetails': 'dGVzdCBleGFtcGxlCg==dGVzdCBleGFtcGxlCg'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.send_cis_session_telemetry_request.SendCisSessionTelemetryRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.send_cis_session_telemetry_response.SendCisSessionTelemetryResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.send_cis_session_telemetry

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.send_cis_session_telemetry.send_cis_session_telemetry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.send_cis_session_telemetry_request.SendCisSessionTelemetryRequest = {}  # type: ignore[typeddict-item]
        input_["scan_job_id"] = scan_job_id
        input_["session_token"] = session_token
        input_["messages"] = messages

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_cis_session(
        self,
        scan_job_id: "aws_sdk_inspector2.types.uuid.UUID",
        message: "aws_sdk_inspector2.types.start_cis_session_message.StartCisSessionMessage",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.start_cis_session_response.StartCisSessionResponse":
        """<p> Starts a CIS session. This API is used by the Amazon Inspector SSM plugin to communicate with the Amazon Inspector service. The Amazon Inspector SSM plugin calls this API to start a CIS scan session for the scan ID supplied by the service. </p>

        Args:
            scan_job_id: <p>A unique identifier for the scan job.</p>
            message: <p>The start CIS session message.</p>

        Examples:
            Sample SendCisSessionHealth Call

            >>> client.start_cis_session(scan_job_id='624b746d-e080-44ae-8c1d-48e653365a38', message={'sessionToken': '624b746d-e080-44ae-8c1d-48e653365a31'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.start_cis_session_request.StartCisSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.start_cis_session_response.StartCisSessionResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.start_cis_session

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.start_cis_session.start_cis_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.start_cis_session_request.StartCisSessionRequest = {}  # type: ignore[typeddict-item]
        input_["scan_job_id"] = scan_job_id
        input_["message"] = message

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_code_security_scan(
        self,
        resource: "aws_sdk_inspector2.types.code_security_resource.CodeSecurityResource",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        client_token: Optional[
            "aws_sdk_inspector2.types.code_security_client_token.CodeSecurityClientToken"
        ] = None,
    ) -> "aws_sdk_inspector2.types.start_code_security_scan_response.StartCodeSecurityScanResponse":
        """<p>Initiates a code security scan on a specified repository.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            resource: <p>The resource identifier for the code repository to scan.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.start_code_security_scan_request.StartCodeSecurityScanRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.start_code_security_scan_response.StartCodeSecurityScanResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.start_code_security_scan

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.start_code_security_scan.start_code_security_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.start_code_security_scan_request.StartCodeSecurityScanRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["resource"] = resource

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_cis_session(
        self,
        scan_job_id: "aws_sdk_inspector2.types.uuid.UUID",
        session_token: "aws_sdk_inspector2.types.uuid.UUID",
        message: "aws_sdk_inspector2.types.stop_cis_session_message.StopCisSessionMessage",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.stop_cis_session_response.StopCisSessionResponse":
        """<p> Stops a CIS session. This API is used by the Amazon Inspector SSM plugin to communicate with the Amazon Inspector service. The Amazon Inspector SSM plugin calls this API to stop a CIS scan session for the scan ID supplied by the service. </p>

        Args:
            scan_job_id: <p>A unique identifier for the scan job.</p>
            session_token: <p>The unique token that identifies the CIS session.</p>
            message: <p>The stop CIS session message.</p>

        Examples:
            Sample StopCisSession Call

            >>> client.stop_cis_session(scan_job_id='624b746d-e080-44ae-8c1d-48e653365a38', session_token='624b746d-e080-44ae-8c1d-48e653365a31', message={'status': 'FAILED', 'reason': 'Failure Reason', 'progress': {'informationalChecks': 1, 'errorChecks': 1, 'successfulChecks': 5, 'notApplicableChecks': 0, 'totalChecks': 10, 'unknownChecks': 0, 'notEvaluatedChecks': 2, 'failedChecks': 0}, 'computePlatform': {'vendor': 'canonical', 'product': 'ubuntu', 'version': '20.04'}, 'benchmarkVersion': '2.0.0', 'benchmarkProfile': 'xccdf_org.cisecurity.benchmarks_profile_Level_1'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.stop_cis_session_request.StopCisSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.stop_cis_session_response.StopCisSessionResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.stop_cis_session

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.stop_cis_session.stop_cis_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.stop_cis_session_request.StopCisSessionRequest = {}  # type: ignore[typeddict-item]
        input_["scan_job_id"] = scan_job_id
        input_["session_token"] = session_token
        input_["message"] = message

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_inspector2.types.arn.Arn",
        tags: "aws_sdk_inspector2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to apply a tag to.</p>
            tags: <p>The tags to be added to a resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.tag_resource

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_inspector2.types.arn.Arn",
        tag_keys: "aws_sdk_inspector2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource to remove tags from.</p>
            tag_keys: <p>The tag keys to remove from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.untag_resource

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_cis_scan_configuration(
        self,
        scan_configuration_arn: "aws_sdk_inspector2.types.cis_scan_configuration_arn.CisScanConfigurationArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        scan_name: Optional[
            "aws_sdk_inspector2.types.cis_scan_name.CisScanName"
        ] = None,
        security_level: Optional[
            "aws_sdk_inspector2.types.cis_security_level.CisSecurityLevel"
        ] = None,
        schedule: Optional["aws_sdk_inspector2.types.schedule.Schedule"] = None,
        targets: Optional[
            "aws_sdk_inspector2.types.update_cis_targets.UpdateCisTargets"
        ] = None,
    ) -> "aws_sdk_inspector2.types.update_cis_scan_configuration_response.UpdateCisScanConfigurationResponse":
        """<p>Updates a CIS scan configuration.</p>

        Args:
            scan_configuration_arn: <p>The CIS scan configuration ARN.</p>
            scan_name: <p>The scan name for the CIS scan configuration.</p>
            security_level: <p> The security level for the CIS scan configuration. Security level refers to the Benchmark levels that CIS assigns to a profile. </p>
            schedule: <p>The schedule for the CIS scan configuration.</p>
            targets: <p>The targets for the CIS scan configuration.</p>

        Examples:
            Sample UpdateCisScanConfiguration Call

            >>> client.update_cis_scan_configuration(scan_configuration_arn='arn:aws:inspector2:us-east-1:123412341234:owner/123412341234/cis-configuration/624b746d-e080-44ae-8c1d-48e653365a38', scan_name='sample_new', security_level='LEVEL_2', schedule={'daily': {'startTime': {'timeOfDay': '12:56', 'timezone': 'UTC'}}}, targets={'accountIds': ['SELF'], 'targetResourceTags': {'key2': ['value2']}})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.update_cis_scan_configuration_request.UpdateCisScanConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.update_cis_scan_configuration_response.UpdateCisScanConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.update_cis_scan_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.update_cis_scan_configuration.update_cis_scan_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.update_cis_scan_configuration_request.UpdateCisScanConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["scan_configuration_arn"] = scan_configuration_arn
        if scan_name is not None:
            input_["scan_name"] = scan_name
        if security_level is not None:
            input_["security_level"] = security_level
        if schedule is not None:
            input_["schedule"] = schedule
        if targets is not None:
            input_["targets"] = targets

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_code_security_integration(
        self,
        integration_arn: "aws_sdk_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn",
        details: "aws_sdk_inspector2.types.update_integration_details.UpdateIntegrationDetails",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.update_code_security_integration_response.UpdateCodeSecurityIntegrationResponse":
        """<p>Updates an existing code security integration.</p> <p>After calling the <code>CreateCodeSecurityIntegration</code> operation, you complete authentication and authorization with your provider. Next you call the <code>UpdateCodeSecurityIntegration</code> operation to provide the <code>details</code> to complete the integration setup</p>

        Args:
            integration_arn: <p>The Amazon Resource Name (ARN) of the code security integration to update.</p>
            details: <p>The updated integration details specific to the repository provider type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.update_code_security_integration_request.UpdateCodeSecurityIntegrationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.update_code_security_integration_response.UpdateCodeSecurityIntegrationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.update_code_security_integration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.update_code_security_integration.update_code_security_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.update_code_security_integration_request.UpdateCodeSecurityIntegrationRequest = {}  # type: ignore[typeddict-item]
        input_["integration_arn"] = integration_arn
        input_["details"] = details

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_code_security_scan_configuration(
        self,
        scan_configuration_arn: "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn",
        configuration: "aws_sdk_inspector2.types.code_security_scan_configuration.CodeSecurityScanConfiguration",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.update_code_security_scan_configuration_response.UpdateCodeSecurityScanConfigurationResponse":
        """<p>Updates an existing code security scan configuration.</p>

        Args:
            scan_configuration_arn: <p>The Amazon Resource Name (ARN) of the scan configuration to update.</p>
            configuration: <p>The updated configuration settings for the code security scan.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.update_code_security_scan_configuration_request.UpdateCodeSecurityScanConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.update_code_security_scan_configuration_response.UpdateCodeSecurityScanConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.update_code_security_scan_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.update_code_security_scan_configuration.update_code_security_scan_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.update_code_security_scan_configuration_request.UpdateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["scan_configuration_arn"] = scan_configuration_arn
        input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_configuration(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        ecr_configuration: Optional[
            "aws_sdk_inspector2.types.ecr_configuration.EcrConfiguration"
        ] = None,
        ec2_configuration: Optional[
            "aws_sdk_inspector2.types.ec2_configuration.Ec2Configuration"
        ] = None,
    ) -> "aws_sdk_inspector2.types.update_configuration_response.UpdateConfigurationResponse":
        """<p>Updates setting configurations for your Amazon Inspector account. When you use this API as an Amazon Inspector delegated administrator this updates the setting for all accounts you manage. Member accounts in an organization cannot update this setting.</p>

        Args:
            ecr_configuration: <p>Specifies how the ECR automated re-scan will be updated for your environment.</p>
            ec2_configuration: <p>Specifies how the Amazon EC2 automated scan will be updated for your environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.update_configuration_request.UpdateConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.update_configuration_response.UpdateConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.update_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.update_configuration.update_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.update_configuration_request.UpdateConfigurationRequest = {}  # type: ignore[typeddict-item]
        if ecr_configuration is not None:
            input_["ecr_configuration"] = ecr_configuration
        if ec2_configuration is not None:
            input_["ec2_configuration"] = ec2_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_ec2_deep_inspection_configuration(
        self,
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        activate_deep_inspection: Optional[bool] = None,
        package_paths: Optional["aws_sdk_inspector2.types.path_list.PathList"] = None,
    ) -> "aws_sdk_inspector2.types.update_ec2_deep_inspection_configuration_response.UpdateEc2DeepInspectionConfigurationResponse":
        """<p>Activates, deactivates Amazon Inspector deep inspection, or updates custom paths for your account. </p>

        Args:
            activate_deep_inspection: <p>Specify <code>TRUE</code> to activate Amazon Inspector deep inspection in your account, or <code>FALSE</code> to deactivate. Member accounts in an organization cannot deactivate deep inspection, instead the delegated administrator for the organization can deactivate a member account using <a href=\"https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html\">BatchUpdateMemberEc2DeepInspectionStatus</a>.</p>
            package_paths: <p>The Amazon Inspector deep inspection custom paths you are adding for your account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.update_ec2_deep_inspection_configuration_request.UpdateEc2DeepInspectionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.update_ec2_deep_inspection_configuration_response.UpdateEc2DeepInspectionConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.update_ec2_deep_inspection_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.update_ec2_deep_inspection_configuration.update_ec2_deep_inspection_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.update_ec2_deep_inspection_configuration_request.UpdateEc2DeepInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]
        if activate_deep_inspection is not None:
            input_["activate_deep_inspection"] = activate_deep_inspection
        if package_paths is not None:
            input_["package_paths"] = package_paths

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_encryption_key(
        self,
        kms_key_id: "aws_sdk_inspector2.types.kms_key_arn.KmsKeyArn",
        scan_type: "aws_sdk_inspector2.types.scan_type.ScanType",
        resource_type: "aws_sdk_inspector2.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.update_encryption_key_response.UpdateEncryptionKeyResponse":
        """<p>Updates an encryption key. A <code>ResourceNotFoundException</code> means that an Amazon Web Services owned key is being used for encryption.</p>

        Args:
            kms_key_id: <p>A KMS key ID for the encryption key.</p>
            scan_type: <p>The scan type for the encryption key.</p>
            resource_type: <p>The resource type for the encryption key.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.update_encryption_key_request.UpdateEncryptionKeyRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.update_encryption_key_response.UpdateEncryptionKeyResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.update_encryption_key

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.update_encryption_key.update_encryption_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.update_encryption_key_request.UpdateEncryptionKeyRequest = {}  # type: ignore[typeddict-item]
        input_["kms_key_id"] = kms_key_id
        input_["scan_type"] = scan_type
        input_["resource_type"] = resource_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_filter(
        self,
        filter_arn: "aws_sdk_inspector2.types.filter_arn.FilterArn",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
        action: Optional["aws_sdk_inspector2.types.filter_action.FilterAction"] = None,
        description: Optional[
            "aws_sdk_inspector2.types.filter_description.FilterDescription"
        ] = None,
        filter_criteria: Optional[
            "aws_sdk_inspector2.types.filter_criteria.FilterCriteria"
        ] = None,
        name: Optional["aws_sdk_inspector2.types.filter_name.FilterName"] = None,
        reason: Optional["aws_sdk_inspector2.types.filter_reason.FilterReason"] = None,
    ) -> "aws_sdk_inspector2.types.update_filter_response.UpdateFilterResponse":
        """<p>Specifies the action that is to be applied to the findings that match the filter.</p>

        Args:
            action: <p>Specifies the action that is to be applied to the findings that match the filter.</p>
            description: <p>A description of the filter.</p>
            filter_criteria: <p>Defines the criteria to be update in the filter.</p>
            name: <p>The name of the filter.</p>
            filter_arn: <p>The Amazon Resource Number (ARN) of the filter to update.</p>
            reason: <p>The reason the filter was updated.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.update_filter_request.UpdateFilterRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.update_filter_response.UpdateFilterResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.update_filter

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.update_filter.update_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.update_filter_request.UpdateFilterRequest = {}  # type: ignore[typeddict-item]
        if action is not None:
            input_["action"] = action
        if description is not None:
            input_["description"] = description
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if name is not None:
            input_["name"] = name
        input_["filter_arn"] = filter_arn
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_organization_configuration(
        self,
        auto_enable: "aws_sdk_inspector2.types.auto_enable.AutoEnable",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse":
        """<p>Updates the configurations for your Amazon Inspector organization.</p>

        Args:
            auto_enable: <p>Defines which scan types are enabled automatically for new members of your Amazon Inspector organization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.update_organization_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.update_organization_configuration.update_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["auto_enable"] = auto_enable

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_org_ec2_deep_inspection_configuration(
        self,
        org_package_paths: "aws_sdk_inspector2.types.path_list.PathList",
        *,
        config_overrides: Optional[Inspector2ClientConfig] = None,
    ) -> "aws_sdk_inspector2.types.update_org_ec2_deep_inspection_configuration_response.UpdateOrgEc2DeepInspectionConfigurationResponse":
        """<p>Updates the Amazon Inspector deep inspection custom paths for your organization. You must be an Amazon Inspector delegated administrator to use this API.</p>

        Args:
            org_package_paths: <p>The Amazon Inspector deep inspection custom paths you are adding for your organization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_inspector2.types.update_org_ec2_deep_inspection_configuration_request.UpdateOrgEc2DeepInspectionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_inspector2.types.update_org_ec2_deep_inspection_configuration_response.UpdateOrgEc2DeepInspectionConfigurationResponse"
        ]:
            import aws_sdk_inspector2._operations.inspector2.update_org_ec2_deep_inspection_configuration

            output, http_response = (
                aws_sdk_inspector2._operations.inspector2.update_org_ec2_deep_inspection_configuration.update_org_ec2_deep_inspection_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_inspector2.types.update_org_ec2_deep_inspection_configuration_request.UpdateOrgEc2DeepInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["org_package_paths"] = org_package_paths

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
