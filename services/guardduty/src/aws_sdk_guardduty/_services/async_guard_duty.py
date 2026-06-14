"""Generated from Smithy shape ``com.amazonaws.guardduty#GuardDutyAPIService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_guardduty._auth._signers
import aws_sdk_guardduty._auth._sigv4
from aws_sdk_guardduty._auth._identity import Credentials
from aws_sdk_guardduty._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_guardduty._auth._zapros_handler import AuthMiddleware
from aws_sdk_guardduty._pagination import resolve_path as _resolve_path
from aws_sdk_guardduty._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.accept_administrator_invitation_request
    import aws_sdk_guardduty.types.accept_administrator_invitation_response
    import aws_sdk_guardduty.types.accept_invitation_request
    import aws_sdk_guardduty.types.accept_invitation_response
    import aws_sdk_guardduty.types.account_details
    import aws_sdk_guardduty.types.account_id
    import aws_sdk_guardduty.types.account_ids
    import aws_sdk_guardduty.types.admin_account
    import aws_sdk_guardduty.types.archive_findings_request
    import aws_sdk_guardduty.types.archive_findings_response
    import aws_sdk_guardduty.types.auto_enable_members
    import aws_sdk_guardduty.types.boolean
    import aws_sdk_guardduty.types.client_token
    import aws_sdk_guardduty.types.coverage_filter_criteria
    import aws_sdk_guardduty.types.coverage_resource
    import aws_sdk_guardduty.types.coverage_sort_criteria
    import aws_sdk_guardduty.types.coverage_statistics_type_list
    import aws_sdk_guardduty.types.create_detector_request
    import aws_sdk_guardduty.types.create_detector_response
    import aws_sdk_guardduty.types.create_filter_request
    import aws_sdk_guardduty.types.create_filter_response
    import aws_sdk_guardduty.types.create_ip_set_request
    import aws_sdk_guardduty.types.create_ip_set_response
    import aws_sdk_guardduty.types.create_malware_protection_plan_request
    import aws_sdk_guardduty.types.create_malware_protection_plan_response
    import aws_sdk_guardduty.types.create_members_request
    import aws_sdk_guardduty.types.create_members_response
    import aws_sdk_guardduty.types.create_protected_resource
    import aws_sdk_guardduty.types.create_publishing_destination_request
    import aws_sdk_guardduty.types.create_publishing_destination_response
    import aws_sdk_guardduty.types.create_sample_findings_request
    import aws_sdk_guardduty.types.create_sample_findings_response
    import aws_sdk_guardduty.types.create_threat_entity_set_request
    import aws_sdk_guardduty.types.create_threat_entity_set_response
    import aws_sdk_guardduty.types.create_threat_intel_set_request
    import aws_sdk_guardduty.types.create_threat_intel_set_response
    import aws_sdk_guardduty.types.create_trusted_entity_set_request
    import aws_sdk_guardduty.types.create_trusted_entity_set_response
    import aws_sdk_guardduty.types.data_source_configurations
    import aws_sdk_guardduty.types.decline_invitations_request
    import aws_sdk_guardduty.types.decline_invitations_response
    import aws_sdk_guardduty.types.delete_detector_request
    import aws_sdk_guardduty.types.delete_detector_response
    import aws_sdk_guardduty.types.delete_filter_request
    import aws_sdk_guardduty.types.delete_filter_response
    import aws_sdk_guardduty.types.delete_invitations_request
    import aws_sdk_guardduty.types.delete_invitations_response
    import aws_sdk_guardduty.types.delete_ip_set_request
    import aws_sdk_guardduty.types.delete_ip_set_response
    import aws_sdk_guardduty.types.delete_malware_protection_plan_request
    import aws_sdk_guardduty.types.delete_members_request
    import aws_sdk_guardduty.types.delete_members_response
    import aws_sdk_guardduty.types.delete_publishing_destination_request
    import aws_sdk_guardduty.types.delete_publishing_destination_response
    import aws_sdk_guardduty.types.delete_threat_entity_set_request
    import aws_sdk_guardduty.types.delete_threat_entity_set_response
    import aws_sdk_guardduty.types.delete_threat_intel_set_request
    import aws_sdk_guardduty.types.delete_threat_intel_set_response
    import aws_sdk_guardduty.types.delete_trusted_entity_set_request
    import aws_sdk_guardduty.types.delete_trusted_entity_set_response
    import aws_sdk_guardduty.types.describe_malware_scans_request
    import aws_sdk_guardduty.types.describe_malware_scans_response
    import aws_sdk_guardduty.types.describe_organization_configuration_request
    import aws_sdk_guardduty.types.describe_organization_configuration_response
    import aws_sdk_guardduty.types.describe_publishing_destination_request
    import aws_sdk_guardduty.types.describe_publishing_destination_response
    import aws_sdk_guardduty.types.destination_properties
    import aws_sdk_guardduty.types.destination_type
    import aws_sdk_guardduty.types.detector_feature_configurations
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.disable_organization_admin_account_request
    import aws_sdk_guardduty.types.disable_organization_admin_account_response
    import aws_sdk_guardduty.types.disassociate_from_administrator_account_request
    import aws_sdk_guardduty.types.disassociate_from_administrator_account_response
    import aws_sdk_guardduty.types.disassociate_from_master_account_request
    import aws_sdk_guardduty.types.disassociate_from_master_account_response
    import aws_sdk_guardduty.types.disassociate_members_request
    import aws_sdk_guardduty.types.disassociate_members_response
    import aws_sdk_guardduty.types.ebs_snapshot_preservation
    import aws_sdk_guardduty.types.enable_organization_admin_account_request
    import aws_sdk_guardduty.types.enable_organization_admin_account_response
    import aws_sdk_guardduty.types.expected_bucket_owner
    import aws_sdk_guardduty.types.feedback
    import aws_sdk_guardduty.types.filter_action
    import aws_sdk_guardduty.types.filter_criteria
    import aws_sdk_guardduty.types.filter_description
    import aws_sdk_guardduty.types.filter_name
    import aws_sdk_guardduty.types.filter_rank
    import aws_sdk_guardduty.types.finding_criteria
    import aws_sdk_guardduty.types.finding_id
    import aws_sdk_guardduty.types.finding_ids
    import aws_sdk_guardduty.types.finding_publishing_frequency
    import aws_sdk_guardduty.types.finding_statistic_types
    import aws_sdk_guardduty.types.finding_types
    import aws_sdk_guardduty.types.get_administrator_account_request
    import aws_sdk_guardduty.types.get_administrator_account_response
    import aws_sdk_guardduty.types.get_coverage_statistics_request
    import aws_sdk_guardduty.types.get_coverage_statistics_response
    import aws_sdk_guardduty.types.get_detector_request
    import aws_sdk_guardduty.types.get_detector_response
    import aws_sdk_guardduty.types.get_filter_request
    import aws_sdk_guardduty.types.get_filter_response
    import aws_sdk_guardduty.types.get_findings_request
    import aws_sdk_guardduty.types.get_findings_response
    import aws_sdk_guardduty.types.get_findings_statistics_request
    import aws_sdk_guardduty.types.get_findings_statistics_response
    import aws_sdk_guardduty.types.get_invitations_count_request
    import aws_sdk_guardduty.types.get_invitations_count_response
    import aws_sdk_guardduty.types.get_ip_set_request
    import aws_sdk_guardduty.types.get_ip_set_response
    import aws_sdk_guardduty.types.get_malware_protection_plan_request
    import aws_sdk_guardduty.types.get_malware_protection_plan_response
    import aws_sdk_guardduty.types.get_malware_scan_request
    import aws_sdk_guardduty.types.get_malware_scan_response
    import aws_sdk_guardduty.types.get_malware_scan_settings_request
    import aws_sdk_guardduty.types.get_malware_scan_settings_response
    import aws_sdk_guardduty.types.get_master_account_request
    import aws_sdk_guardduty.types.get_master_account_response
    import aws_sdk_guardduty.types.get_member_detectors_request
    import aws_sdk_guardduty.types.get_member_detectors_response
    import aws_sdk_guardduty.types.get_members_request
    import aws_sdk_guardduty.types.get_members_response
    import aws_sdk_guardduty.types.get_organization_statistics_response
    import aws_sdk_guardduty.types.get_remaining_free_trial_days_request
    import aws_sdk_guardduty.types.get_remaining_free_trial_days_response
    import aws_sdk_guardduty.types.get_threat_entity_set_request
    import aws_sdk_guardduty.types.get_threat_entity_set_response
    import aws_sdk_guardduty.types.get_threat_intel_set_request
    import aws_sdk_guardduty.types.get_threat_intel_set_response
    import aws_sdk_guardduty.types.get_trusted_entity_set_request
    import aws_sdk_guardduty.types.get_trusted_entity_set_response
    import aws_sdk_guardduty.types.get_usage_statistics_request
    import aws_sdk_guardduty.types.get_usage_statistics_response
    import aws_sdk_guardduty.types.group_by_type
    import aws_sdk_guardduty.types.guard_duty_arn
    import aws_sdk_guardduty.types.integer_value_with_max
    import aws_sdk_guardduty.types.invitation
    import aws_sdk_guardduty.types.invite_members_request
    import aws_sdk_guardduty.types.invite_members_response
    import aws_sdk_guardduty.types.ip_set_format
    import aws_sdk_guardduty.types.list_coverage_request
    import aws_sdk_guardduty.types.list_coverage_response
    import aws_sdk_guardduty.types.list_detectors_request
    import aws_sdk_guardduty.types.list_detectors_response
    import aws_sdk_guardduty.types.list_filters_request
    import aws_sdk_guardduty.types.list_filters_response
    import aws_sdk_guardduty.types.list_findings_request
    import aws_sdk_guardduty.types.list_findings_response
    import aws_sdk_guardduty.types.list_invitations_request
    import aws_sdk_guardduty.types.list_invitations_response
    import aws_sdk_guardduty.types.list_ip_sets_request
    import aws_sdk_guardduty.types.list_ip_sets_response
    import aws_sdk_guardduty.types.list_malware_protection_plans_request
    import aws_sdk_guardduty.types.list_malware_protection_plans_response
    import aws_sdk_guardduty.types.list_malware_scans_filter_criteria
    import aws_sdk_guardduty.types.list_malware_scans_request
    import aws_sdk_guardduty.types.list_malware_scans_response
    import aws_sdk_guardduty.types.list_members_request
    import aws_sdk_guardduty.types.list_members_response
    import aws_sdk_guardduty.types.list_organization_admin_accounts_request
    import aws_sdk_guardduty.types.list_organization_admin_accounts_response
    import aws_sdk_guardduty.types.list_publishing_destinations_request
    import aws_sdk_guardduty.types.list_publishing_destinations_response
    import aws_sdk_guardduty.types.list_tags_for_resource_request
    import aws_sdk_guardduty.types.list_tags_for_resource_response
    import aws_sdk_guardduty.types.list_threat_entity_sets_request
    import aws_sdk_guardduty.types.list_threat_entity_sets_response
    import aws_sdk_guardduty.types.list_threat_intel_sets_request
    import aws_sdk_guardduty.types.list_threat_intel_sets_response
    import aws_sdk_guardduty.types.list_trusted_entity_sets_request
    import aws_sdk_guardduty.types.list_trusted_entity_sets_response
    import aws_sdk_guardduty.types.location
    import aws_sdk_guardduty.types.malware_protection_plan_actions
    import aws_sdk_guardduty.types.malware_scan
    import aws_sdk_guardduty.types.max_results
    import aws_sdk_guardduty.types.max_results100
    import aws_sdk_guardduty.types.member
    import aws_sdk_guardduty.types.member_features_configurations
    import aws_sdk_guardduty.types.name
    import aws_sdk_guardduty.types.order_by
    import aws_sdk_guardduty.types.organization_data_source_configurations
    import aws_sdk_guardduty.types.organization_features_configurations
    import aws_sdk_guardduty.types.resource_arn
    import aws_sdk_guardduty.types.s3_object_for_send_object_malware_scan
    import aws_sdk_guardduty.types.scan
    import aws_sdk_guardduty.types.scan_resource_criteria
    import aws_sdk_guardduty.types.send_object_malware_scan_request
    import aws_sdk_guardduty.types.send_object_malware_scan_response
    import aws_sdk_guardduty.types.sensitive_string
    import aws_sdk_guardduty.types.sort_criteria
    import aws_sdk_guardduty.types.start_malware_scan_configuration
    import aws_sdk_guardduty.types.start_malware_scan_request
    import aws_sdk_guardduty.types.start_malware_scan_response
    import aws_sdk_guardduty.types.start_monitoring_members_request
    import aws_sdk_guardduty.types.start_monitoring_members_response
    import aws_sdk_guardduty.types.stop_monitoring_members_request
    import aws_sdk_guardduty.types.stop_monitoring_members_response
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tag_key_list
    import aws_sdk_guardduty.types.tag_map
    import aws_sdk_guardduty.types.tag_resource_request
    import aws_sdk_guardduty.types.tag_resource_response
    import aws_sdk_guardduty.types.threat_entity_set_format
    import aws_sdk_guardduty.types.threat_intel_set_format
    import aws_sdk_guardduty.types.trusted_entity_set_format
    import aws_sdk_guardduty.types.unarchive_findings_request
    import aws_sdk_guardduty.types.unarchive_findings_response
    import aws_sdk_guardduty.types.untag_resource_request
    import aws_sdk_guardduty.types.untag_resource_response
    import aws_sdk_guardduty.types.update_detector_request
    import aws_sdk_guardduty.types.update_detector_response
    import aws_sdk_guardduty.types.update_filter_request
    import aws_sdk_guardduty.types.update_filter_response
    import aws_sdk_guardduty.types.update_findings_feedback_request
    import aws_sdk_guardduty.types.update_findings_feedback_response
    import aws_sdk_guardduty.types.update_ip_set_request
    import aws_sdk_guardduty.types.update_ip_set_response
    import aws_sdk_guardduty.types.update_malware_protection_plan_request
    import aws_sdk_guardduty.types.update_malware_scan_settings_request
    import aws_sdk_guardduty.types.update_malware_scan_settings_response
    import aws_sdk_guardduty.types.update_member_detectors_request
    import aws_sdk_guardduty.types.update_member_detectors_response
    import aws_sdk_guardduty.types.update_organization_configuration_request
    import aws_sdk_guardduty.types.update_organization_configuration_response
    import aws_sdk_guardduty.types.update_protected_resource
    import aws_sdk_guardduty.types.update_publishing_destination_request
    import aws_sdk_guardduty.types.update_publishing_destination_response
    import aws_sdk_guardduty.types.update_threat_entity_set_request
    import aws_sdk_guardduty.types.update_threat_entity_set_response
    import aws_sdk_guardduty.types.update_threat_intel_set_request
    import aws_sdk_guardduty.types.update_threat_intel_set_response
    import aws_sdk_guardduty.types.update_trusted_entity_set_request
    import aws_sdk_guardduty.types.update_trusted_entity_set_response
    import aws_sdk_guardduty.types.usage_criteria
    import aws_sdk_guardduty.types.usage_statistic_type


class AsyncGuardDutyClientConfig(TypedDict, total=False):
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


class AsyncGuardDutyClient:
    """A client for the ``GuardDuty`` service.

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
        self._config = AsyncGuardDutyClientConfig(
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
        self, config_overrides: Optional[AsyncGuardDutyClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncGuardDutyClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def accept_administrator_invitation(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        administrator_id: "aws_sdk_guardduty.types.string.String",
        invitation_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.accept_administrator_invitation_response.AcceptAdministratorInvitationResponse":
        """<p>Accepts the invitation to be a member account and get monitored by a GuardDuty administrator account that sent the invitation.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p>
            administrator_id: <p>The account ID of the GuardDuty administrator account whose invitation you're accepting.</p>
            invitation_id: <p>The value that is used to validate the administrator account to the member account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.accept_administrator_invitation_request.AcceptAdministratorInvitationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.accept_administrator_invitation_response.AcceptAdministratorInvitationResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.accept_administrator_invitation

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.accept_administrator_invitation.async_accept_administrator_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.accept_administrator_invitation_request.AcceptAdministratorInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["administrator_id"] = administrator_id
        input_["invitation_id"] = invitation_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def accept_invitation(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        master_id: "aws_sdk_guardduty.types.string.String",
        invitation_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.accept_invitation_response.AcceptInvitationResponse":
        r"""<p>Accepts the invitation to be monitored by a GuardDuty administrator account.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            master_id: <p>The account ID of the GuardDuty administrator account whose invitation you're accepting.</p>
            invitation_id: <p>The value that is used to validate the administrator account to the member account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.accept_invitation_request.AcceptInvitationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.accept_invitation_response.AcceptInvitationResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.accept_invitation

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.accept_invitation.async_accept_invitation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.accept_invitation_request.AcceptInvitationRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["master_id"] = master_id
        input_["invitation_id"] = invitation_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def archive_findings(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        finding_ids: "aws_sdk_guardduty.types.finding_ids.FindingIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.archive_findings_response.ArchiveFindingsResponse":
        r"""<p>Archives GuardDuty findings that are specified by the list of finding IDs.</p> <note> <p>Only the administrator account can archive findings. Member accounts don't have permission to archive findings from their accounts.</p> </note>

        Args:
            detector_id: <p>The ID of the detector that specifies the GuardDuty service whose findings you want to archive.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            finding_ids: <p>The IDs of the findings that you want to archive.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.archive_findings_request.ArchiveFindingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.archive_findings_response.ArchiveFindingsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.archive_findings

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.archive_findings.async_archive_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.archive_findings_request.ArchiveFindingsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["finding_ids"] = finding_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_detector(
        self,
        enable: "aws_sdk_guardduty.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        client_token: Optional[
            "aws_sdk_guardduty.types.client_token.ClientToken"
        ] = None,
        finding_publishing_frequency: Optional[
            "aws_sdk_guardduty.types.finding_publishing_frequency.FindingPublishingFrequency"
        ] = None,
        data_sources: Optional[
            "aws_sdk_guardduty.types.data_source_configurations.DataSourceConfigurations"
        ] = None,
        tags: Optional["aws_sdk_guardduty.types.tag_map.TagMap"] = None,
        features: Optional[
            "aws_sdk_guardduty.types.detector_feature_configurations.DetectorFeatureConfigurations"
        ] = None,
    ) -> "aws_sdk_guardduty.types.create_detector_response.CreateDetectorResponse":
        r"""<p>Creates a single GuardDuty detector. A detector is a resource that represents the GuardDuty service. To start using GuardDuty, you must create a detector in each Region where you enable the service. You can have only one detector per account per Region. All data sources are enabled in a new detector by default.</p> <ul> <li> <p>When you don't specify any <code>features</code>, with an exception to <code>RUNTIME_MONITORING</code>, all the optional features are enabled by default.</p> </li> <li> <p>When you specify some of the <code>features</code>, any feature that is not specified in the API call gets enabled by default, with an exception to <code>RUNTIME_MONITORING</code>. </p> </li> </ul> <p>Specifying both EKS Runtime Monitoring (<code>EKS_RUNTIME_MONITORING</code>) and Runtime Monitoring (<code>RUNTIME_MONITORING</code>) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html\">Runtime Monitoring</a>.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            enable: <p>A Boolean value that specifies whether the detector is to be enabled.</p>
            client_token: <p>The idempotency token for the create request.</p>
            finding_publishing_frequency: <p>A value that specifies how frequently updated findings are exported.</p>
            data_sources: <p>Describes which data sources will be enabled for the detector.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>
            tags: <p>The tags to be added to a new detector resource.</p>
            features: <p>A list of features that will be configured for the detector.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.create_detector_request.CreateDetectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.create_detector_response.CreateDetectorResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.create_detector

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.create_detector.async_create_detector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.create_detector_request.CreateDetectorRequest = {}  # type: ignore[typeddict-item]
        input_["enable"] = enable
        if client_token is not None:
            input_["client_token"] = client_token
        if finding_publishing_frequency is not None:
            input_["finding_publishing_frequency"] = finding_publishing_frequency
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if tags is not None:
            input_["tags"] = tags
        if features is not None:
            input_["features"] = features

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_filter(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        name: "aws_sdk_guardduty.types.filter_name.FilterName",
        finding_criteria: "aws_sdk_guardduty.types.finding_criteria.FindingCriteria",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        description: Optional[
            "aws_sdk_guardduty.types.filter_description.FilterDescription"
        ] = None,
        action: Optional["aws_sdk_guardduty.types.filter_action.FilterAction"] = None,
        rank: Optional["aws_sdk_guardduty.types.filter_rank.FilterRank"] = None,
        client_token: Optional[
            "aws_sdk_guardduty.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_guardduty.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_guardduty.types.create_filter_response.CreateFilterResponse":
        r"""<p>Creates a filter using the specified finding criteria. The maximum number of saved filters per Amazon Web Services account per Region is 100. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_limits.html\">Quotas for GuardDuty</a>.</p>

        Args:
            detector_id: <p>The detector ID associated with the GuardDuty account for which you want to create a filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            name: <p>The name of the filter. Valid characters include period (.), underscore (_), dash (-), and alphanumeric characters. A whitespace is considered to be an invalid character.</p>
            description: <p>The description of the filter. Valid characters include alphanumeric characters, and special characters such as hyphen, period, colon, underscore, parentheses (<code>{ }</code>, <code>[ ]</code>, and <code>( )</code>), forward slash, horizontal tab, vertical tab, newline, form feed, return, and whitespace.</p>
            action: <p>Specifies the action that is to be applied to the findings that match the filter.</p> <p>Default: NOOP</p>
            rank: <p>Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.</p>
            finding_criteria: <p>Represents the criteria to be used in the filter for querying findings. The following fields are available for filtering:</p> <ul> <li> <p>accountId</p> </li> <li> <p>arn</p> </li> <li> <p>associatedAttackSequenceArn</p> </li> <li> <p>confidence</p> </li> <li> <p>createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>id</p> </li> <li> <p>partition</p> </li> <li> <p>region</p> </li> <li> <p>resource.accessKeyDetails.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.accountId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.arn</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.attributes.mfaAuthenticated</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.ec2RoleDelivery</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.invokedBy</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.accountId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.arn</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.type</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.userName</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sourceIdentity</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.webIdFederationData.attributes</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.webIdFederationData.federatedProvider</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.type</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.userName</p> </li> <li> <p>resource.accessKeyDetails.userName</p> </li> <li> <p>resource.accessKeyDetails.userType</p> </li> <li> <p>resource.bedrockGuardrailDetails.guardrailArn</p> </li> <li> <p>resource.bedrockGuardrailDetails.guardrailVersion</p> </li> <li> <p>resource.containerDetails.containerRuntime</p> </li> <li> <p>resource.containerDetails.id</p> </li> <li> <p>resource.containerDetails.image</p> </li> <li> <p>resource.containerDetails.imagePrefix</p> </li> <li> <p>resource.containerDetails.name</p> </li> <li> <p>resource.containerDetails.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.containerDetails.securityContext.privileged</p> </li> <li> <p>resource.containerDetails.volumeMounts.mountPath</p> </li> <li> <p>resource.containerDetails.volumeMounts.name</p> </li> <li> <p>resource.ebsSnapshotDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.deviceName</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.encryptionType</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.kmsKeyArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeSizeInGB</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeType</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.deviceName</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.encryptionType</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.kmsKeyArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeSizeInGB</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeType</p> </li> <li> <p>resource.ec2ImageDetails.imageArn</p> </li> <li> <p>resource.ecsClusterDetails.activeServicesCount</p> </li> <li> <p>resource.ecsClusterDetails.arn</p> </li> <li> <p>resource.ecsClusterDetails.name</p> </li> <li> <p>resource.ecsClusterDetails.registeredContainerInstancesCount</p> </li> <li> <p>resource.ecsClusterDetails.runningTasksCount</p> </li> <li> <p>resource.ecsClusterDetails.status</p> </li> <li> <p>resource.ecsClusterDetails.tags.key</p> </li> <li> <p>resource.ecsClusterDetails.tags.value</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.arn</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.containerRuntime</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.id</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.image</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.imagePrefix</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.name</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.securityContext.privileged</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.volumeMounts.mountPath</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.volumeMounts.name</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.definitionArn</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.group</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.launchType</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.startedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.startedBy</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.tags.key</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.tags.value</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.version</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.volumes.hostPath.path</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.volumes.name</p> </li> <li> <p>resource.eksClusterDetails.arn</p> </li> <li> <p>resource.eksClusterDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.eksClusterDetails.name</p> </li> <li> <p>resource.eksClusterDetails.status</p> </li> <li> <p>resource.eksClusterDetails.tags.key</p> </li> <li> <p>resource.eksClusterDetails.tags.value</p> </li> <li> <p>resource.eksClusterDetails.vpcId</p> </li> <li> <p>resource.instanceDetails.availabilityZone</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.arn</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.id</p> </li> <li> <p>resource.instanceDetails.imageDescription</p> </li> <li> <p>resource.instanceDetails.imageId</p> </li> <li> <p>resource.instanceDetails.instanceId</p> </li> <li> <p>resource.instanceDetails.instanceState</p> </li> <li> <p>resource.instanceDetails.instanceType</p> </li> <li> <p>resource.instanceDetails.launchTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.ipv6Addresses</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.networkInterfaceId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicIp</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.subnetId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.vpcId</p> </li> <li> <p>resource.instanceDetails.outpostArn</p> </li> <li> <p>resource.instanceDetails.platform</p> </li> <li> <p>resource.instanceDetails.productCodes.productCodeId</p> </li> <li> <p>resource.instanceDetails.productCodes.productCodeType</p> </li> <li> <p>resource.instanceDetails.tags.key</p> </li> <li> <p>resource.instanceDetails.tags.value</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.groups</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser.groups</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser.username</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.sessionName</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.uid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.username</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.containerRuntime</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.id</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.image</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.imagePrefix</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.privileged</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.volumeMounts.mountPath</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.volumeMounts.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostIpc</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostNetwork</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostPid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.namespace</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.serviceAccountName</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.type</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.uid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.volumes.hostPath.path</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.volumes.name</p> </li> <li> <p>resource.lambdaDetails.description</p> </li> <li> <p>resource.lambdaDetails.functionArn</p> </li> <li> <p>resource.lambdaDetails.functionName</p> </li> <li> <p>resource.lambdaDetails.functionVersion</p> </li> <li> <p>resource.lambdaDetails.lastModifiedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.lambdaDetails.revisionId</p> </li> <li> <p>resource.lambdaDetails.role</p> </li> <li> <p>resource.lambdaDetails.tags.key</p> </li> <li> <p>resource.lambdaDetails.tags.value</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.securityGroups.groupId</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.securityGroups.groupName</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.subnetIds</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.vpcId</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbClusterIdentifier</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbInstanceArn</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbInstanceIdentifier</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbSecurityGroups.name</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbSecurityGroups.status</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbiResourceId</p> </li> <li> <p>resource.rdsDbInstanceDetails.engine</p> </li> <li> <p>resource.rdsDbInstanceDetails.engineVersion</p> </li> <li> <p>resource.rdsDbInstanceDetails.iamDatabaseAuthenticationEnabled</p> </li> <li> <p>resource.rdsDbInstanceDetails.publiclyAccessible</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcId</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcSecurityGroups.status</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcSecurityGroups.vpcSecurityGroupId</p> </li> <li> <p>resource.rdsDbUserDetails.application</p> </li> <li> <p>resource.rdsDbUserDetails.authMethod</p> </li> <li> <p>resource.rdsDbUserDetails.database</p> </li> <li> <p>resource.rdsDbUserDetails.ssl</p> </li> <li> <p>resource.rdsDbUserDetails.user</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbClusterIdentifier</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupArn</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupIdentifier</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupResourceId</p> </li> <li> <p>resource.rdsLimitlessDbDetails.engine</p> </li> <li> <p>resource.rdsLimitlessDbDetails.engineVersion</p> </li> <li> <p>resource.rdsLimitlessDbDetails.tags.key</p> </li> <li> <p>resource.rdsLimitlessDbDetails.tags.value</p> </li> <li> <p>resource.recoveryPointDetails.backupVaultName</p> </li> <li> <p>resource.recoveryPointDetails.recoveryPointArn</p> </li> <li> <p>resource.resourceType</p> </li> <li> <p>resource.s3BucketDetails.arn</p> </li> <li> <p>resource.s3BucketDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.s3BucketDetails.defaultServerSideEncryption.encryptionType</p> </li> <li> <p>resource.s3BucketDetails.defaultServerSideEncryption.kmsMasterKeyArn</p> </li> <li> <p>resource.s3BucketDetails.name</p> </li> <li> <p>resource.s3BucketDetails.owner.id</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.effectivePermission</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicPolicy</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.ignorePublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.restrictPublicBuckets</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicReadAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicWriteAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicPolicy</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.ignorePublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.restrictPublicBuckets</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicReadAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicWriteAccess</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.eTag</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.hash</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.key</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.objectArn</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.versionId</p> </li> <li> <p>resource.s3BucketDetails.tags.key</p> </li> <li> <p>resource.s3BucketDetails.tags.value</p> </li> <li> <p>resource.s3BucketDetails.type</p> </li> <li> <p>schemaVersion</p> </li> <li> <p>service.action.actionType</p> </li> <li> <p>service.action.awsApiCallAction.api</p> </li> <li> <p>service.action.awsApiCallAction.callerType</p> </li> <li> <p>service.action.awsApiCallAction.domainDetails.domain</p> </li> <li> <p>service.action.awsApiCallAction.errorCode</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.accountId</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.affiliated</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.awsServiceName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.awsApiCallAction.serviceName</p> </li> <li> <p>service.action.awsApiCallAction.userAgent</p> </li> <li> <p>service.action.dnsRequestAction.blocked</p> </li> <li> <p>service.action.dnsRequestAction.domain</p> </li> <li> <p>service.action.dnsRequestAction.domainWithSuffix</p> </li> <li> <p>service.action.dnsRequestAction.protocol</p> </li> <li> <p>service.action.dnsRequestAction.vpcOwnerAccountId</p> </li> <li> <p>service.action.kubernetesApiCallAction.namespace</p> </li> <li> <p>service.action.kubernetesApiCallAction.parameters</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.kubernetesApiCallAction.requestUri</p> </li> <li> <p>service.action.kubernetesApiCallAction.resource</p> </li> <li> <p>service.action.kubernetesApiCallAction.resourceName</p> </li> <li> <p>service.action.kubernetesApiCallAction.sourceIPs</p> </li> <li> <p>service.action.kubernetesApiCallAction.statusCode</p> </li> <li> <p>service.action.kubernetesApiCallAction.subresource</p> </li> <li> <p>service.action.kubernetesApiCallAction.userAgent</p> </li> <li> <p>service.action.kubernetesApiCallAction.verb</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.allowed</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.namespace</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.resource</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.verb</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.kind</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.name</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.roleRefKind</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.roleRefName</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.uid</p> </li> <li> <p>service.action.kubernetesRoleDetails.kind</p> </li> <li> <p>service.action.kubernetesRoleDetails.name</p> </li> <li> <p>service.action.kubernetesRoleDetails.uid</p> </li> <li> <p>service.action.networkConnectionAction.blocked</p> </li> <li> <p>service.action.networkConnectionAction.connectionDirection</p> </li> <li> <p>service.action.networkConnectionAction.localIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.localIpDetails.ipAddressV6</p> </li> <li> <p>service.action.networkConnectionAction.localNetworkInterface</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.portName</p> </li> <li> <p>service.action.networkConnectionAction.protocol</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.portName</p> </li> <li> <p>service.action.portProbeAction.blocked</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localIpDetails.ipAddressV4</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localIpDetails.ipAddressV6</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localPortDetails.port</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localPortDetails.portName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.application</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.failedLoginAttempts</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.successfulLoginAttempts</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.user</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.additionalInfo.agentDetails.agentId</p> </li> <li> <p>service.additionalInfo.agentDetails.agentVersion</p> </li> <li> <p>service.additionalInfo.anomalies.anomalousAPIs</p> </li> <li> <p>service.additionalInfo.authenticationMethod</p> </li> <li> <p>service.additionalInfo.averagePacketSizeIn</p> </li> <li> <p>service.additionalInfo.averagePacketSizeOut</p> </li> <li> <p>service.additionalInfo.context</p> </li> <li> <p>service.additionalInfo.domain</p> </li> <li> <p>service.additionalInfo.inBytes</p> </li> <li> <p>service.additionalInfo.localNetworkInterfaceOwner</p> </li> <li> <p>service.additionalInfo.localPort</p> </li> <li> <p>service.additionalInfo.outBytes</p> </li> <li> <p>service.additionalInfo.packetsIn</p> </li> <li> <p>service.additionalInfo.packetsOut</p> </li> <li> <p>service.additionalInfo.policyArn</p> </li> <li> <p>service.additionalInfo.policyName</p> </li> <li> <p>service.additionalInfo.remotePort</p> </li> <li> <p>service.additionalInfo.sample</p> </li> <li> <p>service.additionalInfo.scannedPort</p> </li> <li> <p>service.additionalInfo.threatFileSha256</p> </li> <li> <p>service.additionalInfo.threatListName</p> </li> <li> <p>service.additionalInfo.threatName</p> </li> <li> <p>service.additionalInfo.totalBytesIn</p> </li> <li> <p>service.additionalInfo.totalBytesOut</p> </li> <li> <p>service.additionalInfo.type</p> </li> <li> <p>service.additionalInfo.unusual.asnOrg</p> </li> <li> <p>service.additionalInfo.unusual.port</p> </li> <li> <p>service.additionalInfo.unusualProtocol</p> </li> <li> <p>service.additionalInfo.userAgent.fullUserAgent</p> </li> <li> <p>service.additionalInfo.userAgent.userAgentCategory</p> </li> <li> <p>service.additionalInfo.value</p> </li> <li> <p>service.additionalInfo.vpcOwnerAccountId</p> </li> <li> <p>service.archived</p> </li> <li> <p>service.count</p> </li> <li> <p>service.detection.sequence.actors.id</p> </li> <li> <p>service.detection.sequence.actors.process.name</p> </li> <li> <p>service.detection.sequence.actors.process.path</p> </li> <li> <p>service.detection.sequence.actors.process.sha256</p> </li> <li> <p>service.detection.sequence.actors.session.createdTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.actors.session.issuer</p> </li> <li> <p>service.detection.sequence.actors.session.mfaStatus</p> </li> <li> <p>service.detection.sequence.actors.session.uid</p> </li> <li> <p>service.detection.sequence.actors.user.account.account</p> </li> <li> <p>service.detection.sequence.actors.user.account.uid</p> </li> <li> <p>service.detection.sequence.actors.user.credentialUid</p> </li> <li> <p>service.detection.sequence.actors.user.name</p> </li> <li> <p>service.detection.sequence.actors.user.type</p> </li> <li> <p>service.detection.sequence.actors.user.uid</p> </li> <li> <p>service.detection.sequence.additionalSequenceTypes</p> </li> <li> <p>service.detection.sequence.description</p> </li> <li> <p>service.detection.sequence.endpoints.autonomousSystem.name</p> </li> <li> <p>service.detection.sequence.endpoints.autonomousSystem.number</p> </li> <li> <p>service.detection.sequence.endpoints.connection.direction</p> </li> <li> <p>service.detection.sequence.endpoints.domain</p> </li> <li> <p>service.detection.sequence.endpoints.id</p> </li> <li> <p>service.detection.sequence.endpoints.ip</p> </li> <li> <p>service.detection.sequence.endpoints.location.city</p> </li> <li> <p>service.detection.sequence.endpoints.location.country</p> </li> <li> <p>service.detection.sequence.endpoints.location.lat</p> </li> <li> <p>service.detection.sequence.endpoints.location.lon</p> </li> <li> <p>service.detection.sequence.endpoints.port</p> </li> <li> <p>service.detection.sequence.resources.accountId</p> </li> <li> <p>service.detection.sequence.resources.cloudPartition</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.principalId</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.userName</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.userType</p> </li> <li> <p>service.detection.sequence.resources.data.autoscalingAutoScalingGroup.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.cloudformationStack.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.container.image</p> </li> <li> <p>service.detection.sequence.resources.data.container.imageUid</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Image.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.availabilityZone</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.ec2NetworkInterfaceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.iamInstanceProfile.arn</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.iamInstanceProfile.id</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.imageDescription</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.instanceState</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.instanceType</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.outpostArn</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.platform</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.productCodes.productCodeId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.productCodes.productCodeType</p> </li> <li> <p>service.detection.sequence.resources.data.ec2LaunchTemplate.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2LaunchTemplate.version</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.ipv6Addresses</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.privateIpAddresses.privateDnsName</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.privateIpAddresses.privateIpAddress</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.publicIp</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.securityGroups.groupId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.securityGroups.groupName</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.subNetId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.vpcId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Vpc.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsCluster.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsCluster.status</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.containerUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.launchType</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.taskDefinitionArn</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.arn</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.status</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.vpcId</p> </li> <li> <p>service.detection.sequence.resources.data.iamInstanceProfile.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.iamInstanceProfile.id</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.containerUids</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.namespace</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.type</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicAclAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicAclIgnoreBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicBucketRestrictBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicPolicyAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicAclAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicAclIgnoreBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicBucketRestrictBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicPolicyAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.effectivePermission</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.encryptionKeyArn</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.encryptionType</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.ownerId</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.publicReadAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.publicWriteAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.s3ObjectUids</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.eTag</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.key</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.versionId</p> </li> <li> <p>service.detection.sequence.resources.name</p> </li> <li> <p>service.detection.sequence.resources.region</p> </li> <li> <p>service.detection.sequence.resources.resourceType</p> </li> <li> <p>service.detection.sequence.resources.service</p> </li> <li> <p>service.detection.sequence.resources.tags.key</p> </li> <li> <p>service.detection.sequence.resources.tags.value</p> </li> <li> <p>service.detection.sequence.resources.uid</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.key</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.title</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.values</p> </li> <li> <p>service.detection.sequence.signals.actorIds</p> </li> <li> <p>service.detection.sequence.signals.count</p> </li> <li> <p>service.detection.sequence.signals.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.description</p> </li> <li> <p>service.detection.sequence.signals.endpointIds</p> </li> <li> <p>service.detection.sequence.signals.firstSeenAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.lastSeenAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.name</p> </li> <li> <p>service.detection.sequence.signals.resourceUids</p> </li> <li> <p>service.detection.sequence.signals.severity</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.key</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.title</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.values</p> </li> <li> <p>service.detection.sequence.signals.type</p> </li> <li> <p>service.detection.sequence.signals.uid</p> </li> <li> <p>service.detection.sequence.signals.updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.uid</p> </li> <li> <p>service.detectorId</p> </li> <li> <p>service.ebsVolumeScanDetails.scanCompletedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.count</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.severity</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.threatName</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.files</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.totalGb</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.volumes</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.itemCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.shortened</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.fileName</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.filePath</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.hash</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.volumeArn</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.itemCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.name</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.severity</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.uniqueThreatNameCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatsDetectedItemCount.files</p> </li> <li> <p>service.ebsVolumeScanDetails.scanId</p> </li> <li> <p>service.ebsVolumeScanDetails.scanStartedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.ebsVolumeScanDetails.scanType</p> </li> <li> <p>service.ebsVolumeScanDetails.sources</p> </li> <li> <p>service.ebsVolumeScanDetails.triggerFindingId</p> </li> <li> <p>service.eventFirstSeen</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.eventLastSeen</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatFileSha256</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatListName</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatNames</p> </li> <li> <p>service.featureName</p> </li> <li> <p>service.malwareScanDetails.scanCategory</p> </li> <li> <p>service.malwareScanDetails.scanConfiguration.incrementalScanDetails.baselineResourceArn</p> </li> <li> <p>service.malwareScanDetails.scanConfiguration.triggerType</p> </li> <li> <p>service.malwareScanDetails.scanId</p> </li> <li> <p>service.malwareScanDetails.scanType</p> </li> <li> <p>service.malwareScanDetails.threats.count</p> </li> <li> <p>service.malwareScanDetails.threats.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.additionalInfo.deviceName</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.additionalInfo.versionId</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.itemPath</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.resourceArn</p> </li> <li> <p>service.malwareScanDetails.threats.itemPaths.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemPaths.nestedItemPath</p> </li> <li> <p>service.malwareScanDetails.threats.name</p> </li> <li> <p>service.malwareScanDetails.threats.source</p> </li> <li> <p>service.malwareScanDetails.uniqueThreatCount</p> </li> <li> <p>service.resourceRole</p> </li> <li> <p>service.runtimeDetails.context.addressFamily</p> </li> <li> <p>service.runtimeDetails.context.commandLineExample</p> </li> <li> <p>service.runtimeDetails.context.fileOperation</p> </li> <li> <p>service.runtimeDetails.context.filePath</p> </li> <li> <p>service.runtimeDetails.context.fileSystemType</p> </li> <li> <p>service.runtimeDetails.context.flags</p> </li> <li> <p>service.runtimeDetails.context.ianaProtocolNumber</p> </li> <li> <p>service.runtimeDetails.context.ldPreloadValue</p> </li> <li> <p>service.runtimeDetails.context.libraryPath</p> </li> <li> <p>service.runtimeDetails.context.memoryRegions</p> </li> <li> <p>service.runtimeDetails.context.modifiedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.euid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.executablePath</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.executableSha256</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.euid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.name</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.pid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.userId</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.name</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.pid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.pwd</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.user</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.userId</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.uuid</p> </li> <li> <p>service.runtimeDetails.context.moduleFilePath</p> </li> <li> <p>service.runtimeDetails.context.moduleName</p> </li> <li> <p>service.runtimeDetails.context.moduleSha256</p> </li> <li> <p>service.runtimeDetails.context.mountSource</p> </li> <li> <p>service.runtimeDetails.context.mountTarget</p> </li> <li> <p>service.runtimeDetails.context.relatedFilePaths</p> </li> <li> <p>service.runtimeDetails.context.releaseAgentPath</p> </li> <li> <p>service.runtimeDetails.context.runcBinaryPath</p> </li> <li> <p>service.runtimeDetails.context.scriptPath</p> </li> <li> <p>service.runtimeDetails.context.serviceName</p> </li> <li> <p>service.runtimeDetails.context.shellHistoryFilePath</p> </li> <li> <p>service.runtimeDetails.context.socketPath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.euid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.executablePath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.executableSha256</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.euid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.name</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.pid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.userId</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.name</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.pid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.pwd</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.user</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.userId</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.uuid</p> </li> <li> <p>service.runtimeDetails.context.threatFilePath</p> </li> <li> <p>service.runtimeDetails.context.toolCategory</p> </li> <li> <p>service.runtimeDetails.context.toolName</p> </li> <li> <p>service.runtimeDetails.process.euid</p> </li> <li> <p>service.runtimeDetails.process.executablePath</p> </li> <li> <p>service.runtimeDetails.process.executableSha256</p> </li> <li> <p>service.runtimeDetails.process.lineage.euid</p> </li> <li> <p>service.runtimeDetails.process.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.process.lineage.name</p> </li> <li> <p>service.runtimeDetails.process.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.process.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.process.lineage.pid</p> </li> <li> <p>service.runtimeDetails.process.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.process.lineage.userId</p> </li> <li> <p>service.runtimeDetails.process.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.process.name</p> </li> <li> <p>service.runtimeDetails.process.namespacePid</p> </li> <li> <p>service.runtimeDetails.process.parentUuid</p> </li> <li> <p>service.runtimeDetails.process.pid</p> </li> <li> <p>service.runtimeDetails.process.pwd</p> </li> <li> <p>service.runtimeDetails.process.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.process.user</p> </li> <li> <p>service.runtimeDetails.process.userId</p> </li> <li> <p>service.runtimeDetails.process.uuid</p> </li> <li> <p>service.serviceName</p> </li> <li> <p>service.userFeedback</p> </li> <li> <p>severity</p> <p>To configure severity based filters, use the following for the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingCriteria.html\">FindingCriteria</a> condition:</p> <ul> <li> <p> <b>Low</b>: <code>[\"1\", \"2\", \"3\"]</code> </p> </li> <li> <p> <b>Medium</b>: <code>[\"4\", \"5\", \"6\"]</code> </p> </li> <li> <p> <b>High</b>: <code>[\"7\", \"8\"]</code> </p> </li> <li> <p> <b>Critical</b>: <code>[\"9\", \"10\"]</code> </p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html\">Findings severity levels</a> in the <i>Amazon GuardDuty User Guide</i>.</p> </li> <li> <p>type</p> </li> <li> <p>updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> </ul>
            client_token: <p>The idempotency token for the create request.</p>
            tags: <p>The tags to be added to a new filter resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.create_filter_request.CreateFilterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.create_filter_response.CreateFilterResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.create_filter

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.create_filter.async_create_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.create_filter_request.CreateFilterRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if action is not None:
            input_["action"] = action
        if rank is not None:
            input_["rank"] = rank
        input_["finding_criteria"] = finding_criteria
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_ip_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        name: "aws_sdk_guardduty.types.name.Name",
        format: "aws_sdk_guardduty.types.ip_set_format.IpSetFormat",
        location: "aws_sdk_guardduty.types.location.Location",
        activate: "aws_sdk_guardduty.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        client_token: Optional[
            "aws_sdk_guardduty.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_guardduty.types.tag_map.TagMap"] = None,
        expected_bucket_owner: Optional[
            "aws_sdk_guardduty.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_guardduty.types.create_ip_set_response.CreateIPSetResponse":
        r"""<p>Creates a new IPSet, which is called a trusted IP list in the console user interface. An IPSet is a list of IP addresses that are trusted for secure communication with Amazon Web Services infrastructure and applications. GuardDuty doesn't generate findings for IP addresses that are included in IPSets. Only users from the administrator account can use this operation.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account for which you want to create an IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            name: <p>The user-friendly name to identify the IPSet.</p> <p> Allowed characters are alphanumeric, whitespace, dash (-), and underscores (_).</p>
            format: <p>The format of the file that contains the IPSet.</p>
            location: <p>The URI of the file that contains the IPSet. </p>
            activate: <p>A Boolean value that indicates whether GuardDuty is to start using the uploaded IPSet.</p>
            client_token: <p>The idempotency token for the create request.</p>
            tags: <p>The tags to be added to a new IP set resource.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.create_ip_set_request.CreateIPSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.create_ip_set_response.CreateIPSetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.create_ip_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.create_ip_set.async_create_ip_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.create_ip_set_request.CreateIPSetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["name"] = name
        input_["format"] = format
        input_["location"] = location
        input_["activate"] = activate
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_malware_protection_plan(
        self,
        role: "aws_sdk_guardduty.types.string.String",
        protected_resource: "aws_sdk_guardduty.types.create_protected_resource.CreateProtectedResource",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        client_token: Optional[
            "aws_sdk_guardduty.types.client_token.ClientToken"
        ] = None,
        actions: Optional[
            "aws_sdk_guardduty.types.malware_protection_plan_actions.MalwareProtectionPlanActions"
        ] = None,
        tags: Optional["aws_sdk_guardduty.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_guardduty.types.create_malware_protection_plan_response.CreateMalwareProtectionPlanResponse":
        r"""<p>Creates a new Malware Protection plan for the protected resource.</p> <p>When you create a Malware Protection plan, the Amazon Web Services service terms for GuardDuty Malware Protection apply. For more information, see <a href=\"http://aws.amazon.com/service-terms/#87._Amazon_GuardDuty\">Amazon Web Services service terms for GuardDuty Malware Protection</a>.</p>

        Args:
            client_token: <p>The idempotency token for the create request.</p>
            role: <p>Amazon Resource Name (ARN) of the IAM role that has the permissions to scan and add tags to the associated protected resource.</p>
            protected_resource: <p>Information about the protected resource that is associated with the created Malware Protection plan. Presently, <code>S3Bucket</code> is the only supported protected resource.</p>
            actions: <p>Information about whether the tags will be added to the S3 object after scanning.</p>
            tags: <p>Tags added to the Malware Protection plan resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.create_malware_protection_plan_request.CreateMalwareProtectionPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.create_malware_protection_plan_response.CreateMalwareProtectionPlanResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.create_malware_protection_plan

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.create_malware_protection_plan.async_create_malware_protection_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.create_malware_protection_plan_request.CreateMalwareProtectionPlanRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["role"] = role
        input_["protected_resource"] = protected_resource
        if actions is not None:
            input_["actions"] = actions
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_members(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        account_details: "aws_sdk_guardduty.types.account_details.AccountDetails",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.create_members_response.CreateMembersResponse":
        r"""<p>Creates member accounts of the current Amazon Web Services account by specifying a list of Amazon Web Services account IDs. This step is a prerequisite for managing the associated member accounts either by invitation or through an organization.</p> <p>As a delegated administrator, using <code>CreateMembers</code> will enable GuardDuty in the added member accounts, with the exception of the organization delegated administrator account. A delegated administrator must enable GuardDuty prior to being added as a member.</p> <p>When you use CreateMembers as an Organizations delegated administrator, GuardDuty applies your organization's auto-enable settings to the member accounts in this request, irrespective of the accounts being new or existing members. For more information about the existing auto-enable settings for your organization, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribeOrganizationConfiguration.html\">DescribeOrganizationConfiguration</a>.</p> <p>If you disassociate a member account that was added by invitation, the member account details obtained from this API, including the associated email addresses, will be retained. This is done so that the delegated administrator can invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html\">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html\">DeleteMembers</a> API. </p> <p>When the member accounts added through Organizations are later disassociated, you (administrator) can't invite them by calling the InviteMembers API. You can create an association with these member accounts again only by calling the CreateMembers API.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account for which you want to associate member accounts.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            account_details: <p>A list of account ID and email address pairs of the accounts that you want to associate with the GuardDuty administrator account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.create_members_request.CreateMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.create_members_response.CreateMembersResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.create_members

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.create_members.async_create_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.create_members_request.CreateMembersRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["account_details"] = account_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_publishing_destination(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        destination_type: "aws_sdk_guardduty.types.destination_type.DestinationType",
        destination_properties: "aws_sdk_guardduty.types.destination_properties.DestinationProperties",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        client_token: Optional[
            "aws_sdk_guardduty.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_guardduty.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_guardduty.types.create_publishing_destination_response.CreatePublishingDestinationResponse":
        r"""<p>Creates a publishing destination where you can export your GuardDuty findings. Before you start exporting the findings, the destination resource must exist.</p>

        Args:
            detector_id: <p>The ID of the GuardDuty detector associated with the publishing destination.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            destination_type: <p>The type of resource for the publishing destination. Currently only Amazon S3 buckets are supported.</p>
            destination_properties: <p>The properties of the publishing destination, including the ARNs for the destination and the KMS key used for encryption.</p>
            client_token: <p>The idempotency token for the request.</p>
            tags: <p>The tags to be added to a new publishing destination resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.create_publishing_destination_request.CreatePublishingDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.create_publishing_destination_response.CreatePublishingDestinationResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.create_publishing_destination

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.create_publishing_destination.async_create_publishing_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.create_publishing_destination_request.CreatePublishingDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["destination_type"] = destination_type
        input_["destination_properties"] = destination_properties
        if client_token is not None:
            input_["client_token"] = client_token
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
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        finding_types: Optional[
            "aws_sdk_guardduty.types.finding_types.FindingTypes"
        ] = None,
    ) -> "aws_sdk_guardduty.types.create_sample_findings_response.CreateSampleFindingsResponse":
        r"""<p>Generates sample findings of types specified by the list of finding types. If 'NULL' is specified for <code>findingTypes</code>, the API generates sample findings of all supported finding types.</p>

        Args:
            detector_id: <p>The ID of the detector for which you need to create sample findings.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            finding_types: <p>The types of sample findings to generate.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.create_sample_findings_request.CreateSampleFindingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.create_sample_findings_response.CreateSampleFindingsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.create_sample_findings

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.create_sample_findings.async_create_sample_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.create_sample_findings_request.CreateSampleFindingsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        if finding_types is not None:
            input_["finding_types"] = finding_types

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_threat_entity_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        name: "aws_sdk_guardduty.types.name.Name",
        format: "aws_sdk_guardduty.types.threat_entity_set_format.ThreatEntitySetFormat",
        location: "aws_sdk_guardduty.types.location.Location",
        activate: "aws_sdk_guardduty.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        expected_bucket_owner: Optional[
            "aws_sdk_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
        ] = None,
        client_token: Optional[
            "aws_sdk_guardduty.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_guardduty.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_guardduty.types.create_threat_entity_set_response.CreateThreatEntitySetResponse":
        r"""<p>Creates a new threat entity set. In a threat entity set, you can provide known malicious threat entities for your Amazon Web Services environment. GuardDuty generates findings based on the entries in the threat entity sets. Only users of the administrator account can manage entity sets, which automatically apply to member accounts.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account for which you want to create a threat entity set.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            name: <p>A user-friendly name to identify the threat entity set.</p> <p>The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (_).</p>
            format: <p>The format of the file that contains the threat entity set.</p>
            location: <p>The URI of the file that contains the threat entity set. The format of the <code>Location</code> URL must be a valid Amazon S3 URL format. Invalid URL formats will result in an error, regardless of whether you activate the entity set or not. For more information about format of the location URLs, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-create-activate.html\">Format of location URL under Step 2: Adding trusted or threat intelligence data</a> in the <i>Amazon GuardDuty User Guide</i>.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
            activate: <p>A boolean value that indicates whether GuardDuty should start using the uploaded threat entity set to generate findings.</p>
            client_token: <p>The idempotency token for the create request.</p>
            tags: <p>The tags to be added to a new threat entity set resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.create_threat_entity_set_request.CreateThreatEntitySetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.create_threat_entity_set_response.CreateThreatEntitySetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.create_threat_entity_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.create_threat_entity_set.async_create_threat_entity_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.create_threat_entity_set_request.CreateThreatEntitySetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["name"] = name
        input_["format"] = format
        input_["location"] = location
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner
        input_["activate"] = activate
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_threat_intel_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        name: "aws_sdk_guardduty.types.name.Name",
        format: "aws_sdk_guardduty.types.threat_intel_set_format.ThreatIntelSetFormat",
        location: "aws_sdk_guardduty.types.location.Location",
        activate: "aws_sdk_guardduty.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        client_token: Optional[
            "aws_sdk_guardduty.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_guardduty.types.tag_map.TagMap"] = None,
        expected_bucket_owner: Optional[
            "aws_sdk_guardduty.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_guardduty.types.create_threat_intel_set_response.CreateThreatIntelSetResponse":
        r"""<p>Creates a new ThreatIntelSet. ThreatIntelSets consist of known malicious IP addresses. GuardDuty generates findings based on ThreatIntelSets. Only users of the administrator account can use this operation.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account for which you want to create a <code>threatIntelSet</code>.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            name: <p>A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.</p>
            format: <p>The format of the file that contains the ThreatIntelSet.</p>
            location: <p>The URI of the file that contains the ThreatIntelSet. </p>
            activate: <p>A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.</p>
            client_token: <p>The idempotency token for the create request.</p>
            tags: <p>The tags to be added to a new threat list resource.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.create_threat_intel_set_request.CreateThreatIntelSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.create_threat_intel_set_response.CreateThreatIntelSetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.create_threat_intel_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.create_threat_intel_set.async_create_threat_intel_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.create_threat_intel_set_request.CreateThreatIntelSetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["name"] = name
        input_["format"] = format
        input_["location"] = location
        input_["activate"] = activate
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_trusted_entity_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        name: "aws_sdk_guardduty.types.name.Name",
        format: "aws_sdk_guardduty.types.trusted_entity_set_format.TrustedEntitySetFormat",
        location: "aws_sdk_guardduty.types.location.Location",
        activate: "aws_sdk_guardduty.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        expected_bucket_owner: Optional[
            "aws_sdk_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
        ] = None,
        client_token: Optional[
            "aws_sdk_guardduty.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_guardduty.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_guardduty.types.create_trusted_entity_set_response.CreateTrustedEntitySetResponse":
        r"""<p>Creates a new trusted entity set. In the trusted entity set, you can provide IP addresses and domains that you believe are secure for communication in your Amazon Web Services environment. GuardDuty will not generate findings for the entries that are specified in a trusted entity set. At any given time, you can have only one trusted entity set. </p> <p>Only users of the administrator account can manage the entity sets, which automatically apply to member accounts.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account for which you want to create a trusted entity set.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            name: <p>A user-friendly name to identify the trusted entity set.</p> <p>The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (_).</p>
            format: <p>The format of the file that contains the trusted entity set.</p>
            location: <p>The URI of the file that contains the threat entity set. The format of the <code>Location</code> URL must be a valid Amazon S3 URL format. Invalid URL formats will result in an error, regardless of whether you activate the entity set or not. For more information about format of the location URLs, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-create-activate.html\">Format of location URL under Step 2: Adding trusted or threat intelligence data</a> in the <i>Amazon GuardDuty User Guide</i>.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
            activate: <p>A boolean value that indicates whether GuardDuty is to start using the uploaded trusted entity set.</p>
            client_token: <p>The idempotency token for the create request.</p>
            tags: <p>The tags to be added to a new trusted entity set resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.create_trusted_entity_set_request.CreateTrustedEntitySetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.create_trusted_entity_set_response.CreateTrustedEntitySetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.create_trusted_entity_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.create_trusted_entity_set.async_create_trusted_entity_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.create_trusted_entity_set_request.CreateTrustedEntitySetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["name"] = name
        input_["format"] = format
        input_["location"] = location
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner
        input_["activate"] = activate
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def decline_invitations(
        self,
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.decline_invitations_response.DeclineInvitationsResponse":
        """<p>Declines invitations sent to the current member account by Amazon Web Services accounts specified by their account IDs.</p>

        Args:
            account_ids: <p>A list of account IDs of the Amazon Web Services accounts that sent invitations to the current member account that you want to decline invitations from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.decline_invitations_request.DeclineInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.decline_invitations_response.DeclineInvitationsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.decline_invitations

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.decline_invitations.async_decline_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.decline_invitations_request.DeclineInvitationsRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_detector(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.delete_detector_response.DeleteDetectorResponse":
        r"""<p>Deletes an Amazon GuardDuty detector that is specified by the detector ID.</p>

        Args:
            detector_id: <p>The unique ID of the detector that you want to delete.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.delete_detector_request.DeleteDetectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.delete_detector_response.DeleteDetectorResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.delete_detector

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.delete_detector.async_delete_detector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.delete_detector_request.DeleteDetectorRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_filter(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        filter_name: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.delete_filter_response.DeleteFilterResponse":
        r"""<p>Deletes the filter specified by the filter name.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            filter_name: <p>The name of the filter that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.delete_filter_request.DeleteFilterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.delete_filter_response.DeleteFilterResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.delete_filter

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.delete_filter.async_delete_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.delete_filter_request.DeleteFilterRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["filter_name"] = filter_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_invitations(
        self,
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> (
        "aws_sdk_guardduty.types.delete_invitations_response.DeleteInvitationsResponse"
    ):
        """<p>Deletes invitations sent to the current member account by Amazon Web Services accounts specified by their account IDs.</p>

        Args:
            account_ids: <p>A list of account IDs of the Amazon Web Services accounts that sent invitations to the current member account that you want to delete invitations from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.delete_invitations_request.DeleteInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.delete_invitations_response.DeleteInvitationsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.delete_invitations

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.delete_invitations.async_delete_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.delete_invitations_request.DeleteInvitationsRequest = {}  # type: ignore[typeddict-item]
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_ip_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        ip_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.delete_ip_set_response.DeleteIPSetResponse":
        r"""<p>Deletes the IPSet specified by the <code>ipSetId</code>. IPSets are called trusted IP lists in the console user interface.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            ip_set_id: <p>The unique ID of the IPSet to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.delete_ip_set_request.DeleteIPSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.delete_ip_set_response.DeleteIPSetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.delete_ip_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.delete_ip_set.async_delete_ip_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.delete_ip_set_request.DeleteIPSetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["ip_set_id"] = ip_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_malware_protection_plan(
        self,
        malware_protection_plan_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> None:
        """<p>Deletes the Malware Protection plan ID associated with the Malware Protection plan resource. Use this API only when you no longer want to protect the resource associated with this Malware Protection plan ID.</p>

        Args:
            malware_protection_plan_id: <p>A unique identifier associated with Malware Protection plan resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.delete_malware_protection_plan_request.DeleteMalwareProtectionPlanRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.delete_malware_protection_plan

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.delete_malware_protection_plan.async_delete_malware_protection_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.delete_malware_protection_plan_request.DeleteMalwareProtectionPlanRequest = {}  # type: ignore[typeddict-item]
        input_["malware_protection_plan_id"] = malware_protection_plan_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_members(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.delete_members_response.DeleteMembersResponse":
        r"""<p>Deletes GuardDuty member accounts (to the current GuardDuty administrator account) specified by the account IDs.</p> <p>With <code>autoEnableOrganizationMembers</code> configuration for your organization set to <code>ALL</code>, you'll receive an error if you attempt to disable GuardDuty for a member account in your organization.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account whose members you want to delete.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            account_ids: <p>A list of account IDs of the GuardDuty member accounts that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.delete_members_request.DeleteMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.delete_members_response.DeleteMembersResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.delete_members

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.delete_members.async_delete_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.delete_members_request.DeleteMembersRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_publishing_destination(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        destination_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.delete_publishing_destination_response.DeletePublishingDestinationResponse":
        r"""<p>Deletes the publishing definition with the specified <code>destinationId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the publishing destination to delete.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            destination_id: <p>The ID of the publishing destination to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.delete_publishing_destination_request.DeletePublishingDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.delete_publishing_destination_response.DeletePublishingDestinationResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.delete_publishing_destination

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.delete_publishing_destination.async_delete_publishing_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.delete_publishing_destination_request.DeletePublishingDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["destination_id"] = destination_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_threat_entity_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        threat_entity_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.delete_threat_entity_set_response.DeleteThreatEntitySetResponse":
        r"""<p>Deletes the threat entity set that is associated with the specified <code>threatEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the threat entity set resource.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            threat_entity_set_id: <p>The unique ID that helps GuardDuty identify which threat entity set needs to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.delete_threat_entity_set_request.DeleteThreatEntitySetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.delete_threat_entity_set_response.DeleteThreatEntitySetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.delete_threat_entity_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.delete_threat_entity_set.async_delete_threat_entity_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.delete_threat_entity_set_request.DeleteThreatEntitySetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["threat_entity_set_id"] = threat_entity_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_threat_intel_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        threat_intel_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.delete_threat_intel_set_response.DeleteThreatIntelSetResponse":
        r"""<p>Deletes the ThreatIntelSet specified by the ThreatIntelSet ID.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the threatIntelSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            threat_intel_set_id: <p>The unique ID of the threatIntelSet that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.delete_threat_intel_set_request.DeleteThreatIntelSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.delete_threat_intel_set_response.DeleteThreatIntelSetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.delete_threat_intel_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.delete_threat_intel_set.async_delete_threat_intel_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.delete_threat_intel_set_request.DeleteThreatIntelSetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["threat_intel_set_id"] = threat_intel_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_trusted_entity_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        trusted_entity_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.delete_trusted_entity_set_response.DeleteTrustedEntitySetResponse":
        r"""<p>Deletes the trusted entity set that is associated with the specified <code>trustedEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the trusted entity set resource.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            trusted_entity_set_id: <p>The unique ID that helps GuardDuty identify which trusted entity set needs to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.delete_trusted_entity_set_request.DeleteTrustedEntitySetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.delete_trusted_entity_set_response.DeleteTrustedEntitySetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.delete_trusted_entity_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.delete_trusted_entity_set.async_delete_trusted_entity_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.delete_trusted_entity_set_request.DeleteTrustedEntitySetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["trusted_entity_set_id"] = trusted_entity_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_malware_scans(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_guardduty.types.integer_value_with_max.IntegerValueWithMax"
        ] = None,
        filter_criteria: Optional[
            "aws_sdk_guardduty.types.filter_criteria.FilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "aws_sdk_guardduty.types.describe_malware_scans_response.DescribeMalwareScansResponse":
        r"""<p>Returns a list of malware scans. Each member account can view the malware scans for their own accounts. An administrator can view the malware scans for all the member accounts.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The unique ID of the detector that the request is associated with.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            filter_criteria: <p>Represents the criteria to be used in the filter for describing scan entries.</p>
            sort_criteria: <p>Represents the criteria used for sorting scan entries. The <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_SortCriteria.html#guardduty-Type-SortCriteria-attributeName\"> <code>attributeName</code> </a> is required and it must be <code>scanStartTime</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.describe_malware_scans_request.DescribeMalwareScansRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.describe_malware_scans_response.DescribeMalwareScansResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.describe_malware_scans

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.describe_malware_scans.async_describe_malware_scans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.describe_malware_scans_request.DescribeMalwareScansRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_malware_scans(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_guardduty.types.integer_value_with_max.IntegerValueWithMax"
        ] = None,
        filter_criteria: Optional[
            "aws_sdk_guardduty.types.filter_criteria.FilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.scan.Scan]":
        _token = next_token
        while True:
            _response = await self.describe_malware_scans(
                detector_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter_criteria=filter_criteria,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("scans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_organization_configuration(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse":
        r"""<p>Returns information about the account selected as the delegated administrator for GuardDuty.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The detector ID of the delegated administrator for which you need to retrieve the information.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill <code>nextToken</code> in the request with the value of <code>NextToken</code> from the previous response to continue listing data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.describe_organization_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.describe_organization_configuration.async_describe_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
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

    async def describe_publishing_destination(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        destination_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.describe_publishing_destination_response.DescribePublishingDestinationResponse":
        r"""<p>Returns information about the publishing destination specified by the provided <code>destinationId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the publishing destination to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            destination_id: <p>The ID of the publishing destination to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.describe_publishing_destination_request.DescribePublishingDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.describe_publishing_destination_response.DescribePublishingDestinationResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.describe_publishing_destination

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.describe_publishing_destination.async_describe_publishing_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.describe_publishing_destination_request.DescribePublishingDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["destination_id"] = destination_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_organization_admin_account(
        self,
        admin_account_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.disable_organization_admin_account_response.DisableOrganizationAdminAccountResponse":
        """<p>Removes the existing GuardDuty delegated administrator of the organization. Only the organization's management account can run this API operation.</p>

        Args:
            admin_account_id: <p>The Amazon Web Services Account ID for the organizations account to be disabled as a GuardDuty delegated administrator.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.disable_organization_admin_account_request.DisableOrganizationAdminAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.disable_organization_admin_account_response.DisableOrganizationAdminAccountResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.disable_organization_admin_account

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.disable_organization_admin_account.async_disable_organization_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.disable_organization_admin_account_request.DisableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
        input_["admin_account_id"] = admin_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_from_administrator_account(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.disassociate_from_administrator_account_response.DisassociateFromAdministratorAccountResponse":
        r"""<p>Disassociates the current GuardDuty member account from its administrator account.</p> <p>When you disassociate an invited member from a GuardDuty delegated administrator, the member account details obtained from the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html\">CreateMembers</a> API, including the associated email addresses, are retained. This is done so that the delegated administrator can invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html\">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html\">DeleteMembers</a> API. </p> <p>With <code>autoEnableOrganizationMembers</code> configuration for your organization set to <code>ALL</code>, you'll receive an error if you attempt to disable GuardDuty in a member account.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.disassociate_from_administrator_account_request.DisassociateFromAdministratorAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.disassociate_from_administrator_account_response.DisassociateFromAdministratorAccountResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.disassociate_from_administrator_account

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.disassociate_from_administrator_account.async_disassociate_from_administrator_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.disassociate_from_administrator_account_request.DisassociateFromAdministratorAccountRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_from_master_account(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.disassociate_from_master_account_response.DisassociateFromMasterAccountResponse":
        r"""<p>Disassociates the current GuardDuty member account from its administrator account.</p> <p>When you disassociate an invited member from a GuardDuty delegated administrator, the member account details obtained from the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html\">CreateMembers</a> API, including the associated email addresses, are retained. This is done so that the delegated administrator can invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html\">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html\">DeleteMembers</a> API.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.disassociate_from_master_account_request.DisassociateFromMasterAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.disassociate_from_master_account_response.DisassociateFromMasterAccountResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.disassociate_from_master_account

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.disassociate_from_master_account.async_disassociate_from_master_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.disassociate_from_master_account_request.DisassociateFromMasterAccountRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_members(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.disassociate_members_response.DisassociateMembersResponse":
        r"""<p>Disassociates GuardDuty member accounts (from the current administrator account) specified by the account IDs.</p> <p>When you disassociate an invited member from a GuardDuty delegated administrator, the member account details obtained from the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html\">CreateMembers</a> API, including the associated email addresses, are retained. This is done so that the delegated administrator can invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html\">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html\">DeleteMembers</a> API. </p> <p>With <code>autoEnableOrganizationMembers</code> configuration for your organization set to <code>ALL</code>, you'll receive an error if you attempt to disassociate a member account before removing them from your organization.</p> <p>If you disassociate a member account that was added by invitation, the member account details obtained from this API, including the associated email addresses, will be retained. This is done so that the delegated administrator can invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html\">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html\">DeleteMembers</a> API. </p> <p>When the member accounts added through Organizations are later disassociated, you (administrator) can't invite them by calling the InviteMembers API. You can create an association with these member accounts again only by calling the CreateMembers API.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account whose members you want to disassociate from the administrator account.</p>
            account_ids: <p>A list of account IDs of the GuardDuty member accounts that you want to disassociate from the administrator account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.disassociate_members_request.DisassociateMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.disassociate_members_response.DisassociateMembersResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.disassociate_members

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.disassociate_members.async_disassociate_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.disassociate_members_request.DisassociateMembersRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_organization_admin_account(
        self,
        admin_account_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.enable_organization_admin_account_response.EnableOrganizationAdminAccountResponse":
        """<p>Designates an Amazon Web Services account within the organization as your GuardDuty delegated administrator. Only the organization's management account can run this API operation.</p>

        Args:
            admin_account_id: <p>The Amazon Web Services account ID for the organization account to be enabled as a GuardDuty delegated administrator.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.enable_organization_admin_account_response.EnableOrganizationAdminAccountResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.enable_organization_admin_account

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.enable_organization_admin_account.async_enable_organization_admin_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
        input_["admin_account_id"] = admin_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_administrator_account(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_administrator_account_response.GetAdministratorAccountResponse":
        """<p>Provides the details of the GuardDuty administrator account associated with the current GuardDuty member account.</p> <p>Based on the type of account that runs this API, the following list shows how the API behavior varies:</p> <ul> <li> <p>When the GuardDuty administrator account runs this API, it will return success (<code>HTTP 200</code>) but no content.</p> </li> <li> <p>When a member account runs this API, it will return the details of the GuardDuty administrator account that is associated with this calling member account.</p> </li> <li> <p>When an individual account (not associated with an organization) runs this API, it will return success (<code>HTTP 200</code>) but no content.</p> </li> </ul>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_administrator_account_request.GetAdministratorAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_administrator_account_response.GetAdministratorAccountResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_administrator_account

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_administrator_account.async_get_administrator_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_administrator_account_request.GetAdministratorAccountRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_coverage_statistics(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        statistics_type: "aws_sdk_guardduty.types.coverage_statistics_type_list.CoverageStatisticsTypeList",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        filter_criteria: Optional[
            "aws_sdk_guardduty.types.coverage_filter_criteria.CoverageFilterCriteria"
        ] = None,
    ) -> "aws_sdk_guardduty.types.get_coverage_statistics_response.GetCoverageStatisticsResponse":
        r"""<p>Retrieves aggregated statistics for your account. If you are a GuardDuty administrator, you can retrieve the statistics for all the resources associated with the active member accounts in your organization who have enabled Runtime Monitoring and have the GuardDuty security agent running on their resources.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            filter_criteria: <p>Represents the criteria used to filter the coverage statistics.</p>
            statistics_type: <p>Represents the statistics type used to aggregate the coverage details.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_coverage_statistics_request.GetCoverageStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_coverage_statistics_response.GetCoverageStatisticsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_coverage_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_coverage_statistics.async_get_coverage_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_coverage_statistics_request.GetCoverageStatisticsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        input_["statistics_type"] = statistics_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_detector(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_detector_response.GetDetectorResponse":
        r"""<p>Retrieves a GuardDuty detector specified by the detectorId.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The unique ID of the detector that you want to get.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_detector_request.GetDetectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_detector_response.GetDetectorResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_detector

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_detector.async_get_detector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_detector_request.GetDetectorRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_filter(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        filter_name: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_filter_response.GetFilterResponse":
        r"""<p>Returns the details of the filter specified by the filter name.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with this filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            filter_name: <p>The name of the filter you want to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_filter_request.GetFilterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_filter_response.GetFilterResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_filter

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_filter.async_get_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_filter_request.GetFilterRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["filter_name"] = filter_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_findings(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        finding_ids: "aws_sdk_guardduty.types.finding_ids.FindingIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        sort_criteria: Optional[
            "aws_sdk_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "aws_sdk_guardduty.types.get_findings_response.GetFindingsResponse":
        r"""<p>Describes Amazon GuardDuty findings specified by finding IDs.</p>

        Args:
            detector_id: <p>The ID of the detector that specifies the GuardDuty service whose findings you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            finding_ids: <p>The IDs of the findings that you want to retrieve.</p>
            sort_criteria: <p>Represents the criteria used for sorting findings.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_findings_request.GetFindingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_findings_response.GetFindingsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_findings

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_findings.async_get_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_findings_request.GetFindingsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["finding_ids"] = finding_ids
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_findings_statistics(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        finding_statistic_types: Optional[
            "aws_sdk_guardduty.types.finding_statistic_types.FindingStatisticTypes"
        ] = None,
        finding_criteria: Optional[
            "aws_sdk_guardduty.types.finding_criteria.FindingCriteria"
        ] = None,
        group_by: Optional["aws_sdk_guardduty.types.group_by_type.GroupByType"] = None,
        order_by: Optional["aws_sdk_guardduty.types.order_by.OrderBy"] = None,
        max_results: Optional[
            "aws_sdk_guardduty.types.max_results100.MaxResults100"
        ] = None,
    ) -> "aws_sdk_guardduty.types.get_findings_statistics_response.GetFindingsStatisticsResponse":
        r"""<p>Lists GuardDuty findings statistics for the specified detector ID.</p> <p>You must provide either <code>findingStatisticTypes</code> or <code>groupBy</code> parameter, and not both. You can use the <code>maxResults</code> and <code>orderBy</code> parameters only when using <code>groupBy</code>.</p> <p>There might be regional differences because some flags might not be available in all the Regions where GuardDuty is currently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The ID of the detector whose findings statistics you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            finding_statistic_types: <p>The types of finding statistics to retrieve.</p>
            finding_criteria: <p>Represents the criteria that is used for querying findings.</p>
            group_by: <p>Displays the findings statistics grouped by one of the listed valid values.</p>
            order_by: <p>Displays the sorted findings in the requested order. The default value of <code>orderBy</code> is <code>DESC</code>.</p> <p>You can use this parameter only with the <code>groupBy</code> parameter.</p>
            max_results: <p>The maximum number of results to be returned in the response. The default value is 25.</p> <p>You can use this parameter only with the <code>groupBy</code> parameter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_findings_statistics_request.GetFindingsStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_findings_statistics_response.GetFindingsStatisticsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_findings_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_findings_statistics.async_get_findings_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_findings_statistics_request.GetFindingsStatisticsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        if finding_statistic_types is not None:
            input_["finding_statistic_types"] = finding_statistic_types
        if finding_criteria is not None:
            input_["finding_criteria"] = finding_criteria
        if group_by is not None:
            input_["group_by"] = group_by
        if order_by is not None:
            input_["order_by"] = order_by
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_invitations_count(
        self, *, config_overrides: Optional[AsyncGuardDutyClientConfig] = None
    ) -> "aws_sdk_guardduty.types.get_invitations_count_response.GetInvitationsCountResponse":
        """<p>Returns the count of all GuardDuty membership invitations that were sent to the current member account except the currently accepted invitation.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_invitations_count_request.GetInvitationsCountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_invitations_count_response.GetInvitationsCountResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_invitations_count

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_invitations_count.async_get_invitations_count(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_invitations_count_request.GetInvitationsCountRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_ip_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        ip_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_ip_set_response.GetIPSetResponse":
        r"""<p>Retrieves the IPSet specified by the <code>ipSetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            ip_set_id: <p>The unique ID of the IPSet to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_ip_set_request.GetIPSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_ip_set_response.GetIPSetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_ip_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_ip_set.async_get_ip_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_ip_set_request.GetIPSetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["ip_set_id"] = ip_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_malware_protection_plan(
        self,
        malware_protection_plan_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_malware_protection_plan_response.GetMalwareProtectionPlanResponse":
        """<p>Retrieves the Malware Protection plan details associated with a Malware Protection plan ID.</p>

        Args:
            malware_protection_plan_id: <p>A unique identifier associated with Malware Protection plan resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_malware_protection_plan_request.GetMalwareProtectionPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_malware_protection_plan_response.GetMalwareProtectionPlanResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_malware_protection_plan

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_malware_protection_plan.async_get_malware_protection_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_malware_protection_plan_request.GetMalwareProtectionPlanRequest = {}  # type: ignore[typeddict-item]
        input_["malware_protection_plan_id"] = malware_protection_plan_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_malware_scan(
        self,
        scan_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_malware_scan_response.GetMalwareScanResponse":
        r"""<p>Retrieves the detailed information for a specific malware scan. Each member account can view the malware scan details for their own account. An administrator can view malware scan details for all accounts in the organization.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            scan_id: <p>A unique identifier that gets generated when you invoke the API without any error. Each malware scan has a corresponding scan ID. Using this scan ID, you can monitor the status of your malware scan.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_malware_scan_request.GetMalwareScanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_malware_scan_response.GetMalwareScanResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_malware_scan

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_malware_scan.async_get_malware_scan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_malware_scan_request.GetMalwareScanRequest = {}  # type: ignore[typeddict-item]
        input_["scan_id"] = scan_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_malware_scan_settings(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_malware_scan_settings_response.GetMalwareScanSettingsResponse":
        r"""<p>Returns the details of the malware scan settings.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with this scan.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_malware_scan_settings_request.GetMalwareScanSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_malware_scan_settings_response.GetMalwareScanSettingsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_malware_scan_settings

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_malware_scan_settings.async_get_malware_scan_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_malware_scan_settings_request.GetMalwareScanSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_master_account(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_master_account_response.GetMasterAccountResponse":
        r"""<p>Provides the details for the GuardDuty administrator account associated with the current GuardDuty member account.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_master_account_request.GetMasterAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_master_account_response.GetMasterAccountResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_master_account

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_master_account.async_get_master_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_master_account_request.GetMasterAccountRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_member_detectors(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_member_detectors_response.GetMemberDetectorsResponse":
        r"""<p>Describes which data sources are enabled for the member account's detector.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The detector ID for the administrator account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            account_ids: <p>A list of member account IDs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_member_detectors_request.GetMemberDetectorsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_member_detectors_response.GetMemberDetectorsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_member_detectors

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_member_detectors.async_get_member_detectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_member_detectors_request.GetMemberDetectorsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_members(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_members_response.GetMembersResponse":
        r"""<p>Retrieves GuardDuty member accounts (of the current GuardDuty administrator account) specified by the account IDs.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account whose members you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            account_ids: <p>A list of account IDs of the GuardDuty member accounts that you want to describe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_members_request.GetMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_members_response.GetMembersResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_members

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_members.async_get_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_members_request.GetMembersRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_organization_statistics(
        self, *, config_overrides: Optional[AsyncGuardDutyClientConfig] = None
    ) -> "aws_sdk_guardduty.types.get_organization_statistics_response.GetOrganizationStatisticsResponse":
        """<p>Retrieves how many active member accounts have each feature enabled within GuardDuty. Only a delegated GuardDuty administrator of an organization can run this API.</p> <p>When you create a new organization, it might take up to 24 hours to generate the statistics for the entire organization.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_organization_statistics_response.GetOrganizationStatisticsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_organization_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_organization_statistics.async_get_organization_statistics(
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

    async def get_remaining_free_trial_days(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_remaining_free_trial_days_response.GetRemainingFreeTrialDaysResponse":
        r"""<p>Provides the number of days left for each data source used in the free trial period.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty member account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            account_ids: <p>A list of account identifiers of the GuardDuty member account.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_remaining_free_trial_days_request.GetRemainingFreeTrialDaysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_remaining_free_trial_days_response.GetRemainingFreeTrialDaysResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_remaining_free_trial_days

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_remaining_free_trial_days.async_get_remaining_free_trial_days(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_remaining_free_trial_days_request.GetRemainingFreeTrialDaysRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_threat_entity_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        threat_entity_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_threat_entity_set_response.GetThreatEntitySetResponse":
        r"""<p>Retrieves the threat entity set associated with the specified <code>threatEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the threat entity set resource.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            threat_entity_set_id: <p>The unique ID that helps GuardDuty identify the threat entity set.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_threat_entity_set_request.GetThreatEntitySetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_threat_entity_set_response.GetThreatEntitySetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_threat_entity_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_threat_entity_set.async_get_threat_entity_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_threat_entity_set_request.GetThreatEntitySetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["threat_entity_set_id"] = threat_entity_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_threat_intel_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        threat_intel_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_threat_intel_set_response.GetThreatIntelSetResponse":
        r"""<p>Retrieves the ThreatIntelSet that is specified by the ThreatIntelSet ID.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the threatIntelSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            threat_intel_set_id: <p>The unique ID of the threatIntelSet that you want to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_threat_intel_set_request.GetThreatIntelSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_threat_intel_set_response.GetThreatIntelSetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_threat_intel_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_threat_intel_set.async_get_threat_intel_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_threat_intel_set_request.GetThreatIntelSetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["threat_intel_set_id"] = threat_intel_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_trusted_entity_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        trusted_entity_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.get_trusted_entity_set_response.GetTrustedEntitySetResponse":
        """<p>Retrieves the trusted entity set associated with the specified <code>trustedEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector associated with this trusted entity set.</p>
            trusted_entity_set_id: <p>The unique ID that helps GuardDuty identify the trusted entity set.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_trusted_entity_set_request.GetTrustedEntitySetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_trusted_entity_set_response.GetTrustedEntitySetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_trusted_entity_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_trusted_entity_set.async_get_trusted_entity_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_trusted_entity_set_request.GetTrustedEntitySetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["trusted_entity_set_id"] = trusted_entity_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_usage_statistics(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        usage_statistic_type: "aws_sdk_guardduty.types.usage_statistic_type.UsageStatisticType",
        usage_criteria: "aws_sdk_guardduty.types.usage_criteria.UsageCriteria",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        unit: Optional["aws_sdk_guardduty.types.string.String"] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.get_usage_statistics_response.GetUsageStatisticsResponse":
        r"""<p>Lists Amazon GuardDuty usage statistics over the last 30 days for the specified detector ID. For newly enabled detectors or data sources, the cost returned will include only the usage so far under 30 days. This may differ from the cost metrics in the console, which project usage over 30 days to provide a monthly cost estimate. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/monitoring_costs.html#usage-calculations\">Understanding How Usage Costs are Calculated</a>.</p>

        Args:
            detector_id: <p>The ID of the detector that specifies the GuardDuty service whose usage statistics you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            usage_statistic_type: <p>The type of usage statistics to retrieve.</p>
            usage_criteria: <p>Represents the criteria used for querying usage.</p>
            unit: <p>The currency unit you would like to view your usage statistics in. Current valid values are USD.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.get_usage_statistics_request.GetUsageStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.get_usage_statistics_response.GetUsageStatisticsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.get_usage_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.get_usage_statistics.async_get_usage_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.get_usage_statistics_request.GetUsageStatisticsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["usage_statistic_type"] = usage_statistic_type
        input_["usage_criteria"] = usage_criteria
        if unit is not None:
            input_["unit"] = unit
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

    async def invite_members(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        disable_email_notification: Optional[
            "aws_sdk_guardduty.types.boolean.Boolean"
        ] = None,
        message: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.invite_members_response.InviteMembersResponse":
        r"""<p>Invites Amazon Web Services accounts to become members of an organization administered by the Amazon Web Services account that invokes this API. If you are using Amazon Web Services Organizations to manage your GuardDuty environment, this step is not needed. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html\">Managing accounts with organizations</a>.</p> <p>To invite Amazon Web Services accounts, the first step is to ensure that GuardDuty has been enabled in the potential member accounts. You can now invoke this API to add accounts by invitation. The invited accounts can either accept or decline the invitation from their GuardDuty accounts. Each invited Amazon Web Services account can choose to accept the invitation from only one Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_invitations.html\">Managing GuardDuty accounts by invitation</a>.</p> <p>After the invite has been accepted and you choose to disassociate a member account (by using <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisassociateMembers.html\">DisassociateMembers</a>) from your account, the details of the member account obtained by invoking <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html\">CreateMembers</a>, including the associated email addresses, will be retained. This is done so that you can invoke InviteMembers without the need to invoke <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html\">CreateMembers</a> again. To remove the details associated with a member account, you must also invoke <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html\">DeleteMembers</a>. </p> <p>If you disassociate a member account that was added by invitation, the member account details obtained from this API, including the associated email addresses, will be retained. This is done so that the delegated administrator can invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html\">InviteMembers</a> API without the need to invoke the CreateMembers API again. To remove the details associated with a member account, the delegated administrator must invoke the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html\">DeleteMembers</a> API. </p> <p>When the member accounts added through Organizations are later disassociated, you (administrator) can't invite them by calling the InviteMembers API. You can create an association with these member accounts again only by calling the CreateMembers API.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty account with which you want to invite members.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            account_ids: <p>A list of account IDs of the accounts that you want to invite to GuardDuty as members.</p>
            disable_email_notification: <p>A Boolean value that specifies whether you want to disable email notification to the accounts that you are inviting to GuardDuty as members.</p>
            message: <p>The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.invite_members_request.InviteMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.invite_members_response.InviteMembersResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.invite_members

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.invite_members.async_invite_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.invite_members_request.InviteMembersRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
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

    async def list_coverage(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        filter_criteria: Optional[
            "aws_sdk_guardduty.types.coverage_filter_criteria.CoverageFilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_guardduty.types.coverage_sort_criteria.CoverageSortCriteria"
        ] = None,
    ) -> "aws_sdk_guardduty.types.list_coverage_response.ListCoverageResponse":
        r"""<p>Lists coverage details for your GuardDuty account. If you're a GuardDuty administrator, you can retrieve all resources associated with the active member accounts in your organization.</p> <p>Make sure the accounts have Runtime Monitoring enabled and GuardDuty agent running on their resources.</p>

        Args:
            detector_id: <p>The unique ID of the detector whose coverage details you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            filter_criteria: <p>Represents the criteria used to filter the coverage details.</p>
            sort_criteria: <p>Represents the criteria used to sort the coverage details.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_coverage_request.ListCoverageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_coverage_response.ListCoverageResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_coverage

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_coverage.async_list_coverage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_coverage_request.ListCoverageRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_coverage(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        filter_criteria: Optional[
            "aws_sdk_guardduty.types.coverage_filter_criteria.CoverageFilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_guardduty.types.coverage_sort_criteria.CoverageSortCriteria"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.coverage_resource.CoverageResource]":
        _token = next_token
        while True:
            _response = await self.list_coverage(
                detector_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter_criteria=filter_criteria,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_detectors(
        self,
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_detectors_response.ListDetectorsResponse":
        """<p>Lists detectorIds of all the existing Amazon GuardDuty detector resources.</p>

        Args:
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_detectors_request.ListDetectorsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_detectors_response.ListDetectorsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_detectors

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_detectors.async_list_detectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_detectors_request.ListDetectorsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_detectors(
        self,
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.detector_id.DetectorId]":
        _token = next_token
        while True:
            _response = await self.list_detectors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("detector_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_filters(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_filters_response.ListFiltersResponse":
        r"""<p>Returns a paginated list of the current filters.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_filters_request.ListFiltersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_filters_response.ListFiltersResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_filters

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_filters.async_list_filters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_filters_request.ListFiltersRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
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

    async def iter_list_filters(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.filter_name.FilterName]":
        _token = next_token
        while True:
            _response = await self.list_filters(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("filter_names",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_findings(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        finding_criteria: Optional[
            "aws_sdk_guardduty.types.finding_criteria.FindingCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_findings_response.ListFindingsResponse":
        r"""<p>Lists GuardDuty findings for the specified detector ID.</p> <p>There might be regional differences because some flags might not be available in all the Regions where GuardDuty is currently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The ID of the detector that specifies the GuardDuty service whose findings you want to list.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            finding_criteria: <p>Represents the criteria used for querying findings. Valid values include:</p> <ul> <li> <p>JSON field name</p> </li> <li> <p>accountId</p> </li> <li> <p>region</p> </li> <li> <p>confidence</p> </li> <li> <p>id</p> </li> <li> <p>resource.accessKeyDetails.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.principalId</p> </li> <li> <p>resource.accessKeyDetails.userName</p> </li> <li> <p>resource.accessKeyDetails.userType</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.id</p> </li> <li> <p>resource.instanceDetails.imageId</p> </li> <li> <p>resource.instanceDetails.instanceId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.ipv6Addresses</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicIp</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.subnetId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.vpcId</p> </li> <li> <p>resource.instanceDetails.tags.key</p> </li> <li> <p>resource.instanceDetails.tags.value</p> </li> <li> <p>resource.resourceType</p> </li> <li> <p>service.action.actionType</p> </li> <li> <p>service.action.awsApiCallAction.api</p> </li> <li> <p>service.action.awsApiCallAction.callerType</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.awsApiCallAction.serviceName</p> </li> <li> <p>service.action.dnsRequestAction.domain</p> </li> <li> <p>service.action.dnsRequestAction.domainWithSuffix</p> </li> <li> <p>service.action.networkConnectionAction.blocked</p> </li> <li> <p>service.action.networkConnectionAction.connectionDirection</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.protocol</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.port</p> </li> <li> <p>service.additionalInfo.threatListName</p> </li> <li> <p>service.archived</p> <p>When this attribute is set to 'true', only archived findings are listed. When it's set to 'false', only unarchived findings are listed. When this attribute is not set, all existing findings are listed.</p> </li> <li> <p>service.ebsVolumeScanDetails.scanId</p> </li> <li> <p>service.resourceRole</p> </li> <li> <p>severity</p> </li> <li> <p>type</p> </li> <li> <p>updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format: 1486685375000</p> </li> </ul>
            sort_criteria: <p>Represents the criteria used for sorting findings.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_findings_request.ListFindingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_findings_response.ListFindingsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_findings

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_findings.async_list_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_findings_request.ListFindingsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        if finding_criteria is not None:
            input_["finding_criteria"] = finding_criteria
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria
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

    async def iter_list_findings(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        finding_criteria: Optional[
            "aws_sdk_guardduty.types.finding_criteria.FindingCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.finding_id.FindingId]":
        _token = next_token
        while True:
            _response = await self.list_findings(
                detector_id,
                config_overrides=config_overrides,
                finding_criteria=finding_criteria,
                sort_criteria=sort_criteria,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("finding_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_invitations(
        self,
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_invitations_response.ListInvitationsResponse":
        """<p>Lists all GuardDuty membership invitations that were sent to the current Amazon Web Services account.</p>

        Args:
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_invitations_request.ListInvitationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_invitations_response.ListInvitationsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_invitations

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_invitations.async_list_invitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_invitations_request.ListInvitationsRequest = {}  # type: ignore[typeddict-item]
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
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.invitation.Invitation]":
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

    async def list_ip_sets(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_ip_sets_response.ListIPSetsResponse":
        r"""<p>Lists the IPSets of the GuardDuty service specified by the detector ID. If you use this operation from a member account, the IPSets returned are the IPSets from the associated administrator account.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_ip_sets_request.ListIPSetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_ip_sets_response.ListIPSetsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_ip_sets

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_ip_sets.async_list_ip_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_ip_sets_request.ListIPSetsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
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

    async def iter_list_ip_sets(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_ip_sets(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ip_set_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_malware_protection_plans(
        self,
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_malware_protection_plans_response.ListMalwareProtectionPlansResponse":
        """<p>Lists the Malware Protection plan IDs associated with the protected resources in your Amazon Web Services account.</p>

        Args:
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of <code>NextToken</code> from the previous response to continue listing data. The default page size is 100 plans.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_malware_protection_plans_request.ListMalwareProtectionPlansRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_malware_protection_plans_response.ListMalwareProtectionPlansResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_malware_protection_plans

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_malware_protection_plans.async_list_malware_protection_plans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_malware_protection_plans_request.ListMalwareProtectionPlansRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_malware_scans(
        self,
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
        filter_criteria: Optional[
            "aws_sdk_guardduty.types.list_malware_scans_filter_criteria.ListMalwareScansFilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "aws_sdk_guardduty.types.list_malware_scans_response.ListMalwareScansResponse":
        """<p>Returns a list of malware scans. Each member account can view the malware scans for their own accounts. An administrator can view the malware scans for all of its members' accounts.</p>

        Args:
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing results.</p>
            filter_criteria: <p>Represents the criteria used to filter the malware scan entries.</p>
            sort_criteria: <p>Represents the criteria used for sorting malware scan entries.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_malware_scans_request.ListMalwareScansRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_malware_scans_response.ListMalwareScansResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_malware_scans

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_malware_scans.async_list_malware_scans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_malware_scans_request.ListMalwareScansRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_criteria is not None:
            input_["filter_criteria"] = filter_criteria
        if sort_criteria is not None:
            input_["sort_criteria"] = sort_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_malware_scans(
        self,
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
        filter_criteria: Optional[
            "aws_sdk_guardduty.types.list_malware_scans_filter_criteria.ListMalwareScansFilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_guardduty.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.malware_scan.MalwareScan]":
        _token = next_token
        while True:
            _response = await self.list_malware_scans(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter_criteria=filter_criteria,
                sort_criteria=sort_criteria,
            )
            _page = _resolve_path(_response, ("scans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_members(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
        only_associated: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_members_response.ListMembersResponse":
        r"""<p>Lists details about all member accounts for the current GuardDuty administrator account.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the member.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
            only_associated: <p>Specifies whether to only return associated members or to return all members (including members who haven't been invited yet or have been disassociated). Member accounts must have been previously associated with the GuardDuty administrator account using <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html\"> <code>Create Members</code> </a>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_members_request.ListMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_members_response.ListMembersResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_members

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_members.async_list_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_members_request.ListMembersRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
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
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
        only_associated: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.member.Member]":
        _token = next_token
        while True:
            _response = await self.list_members(
                detector_id,
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
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse":
        """<p>Lists the accounts designated as GuardDuty delegated administrators. Only the organization's management account can run this API operation.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_organization_admin_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_organization_admin_accounts.async_list_organization_admin_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest = {}  # type: ignore[typeddict-item]
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
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.admin_account.AdminAccount]":
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

    async def list_publishing_destinations(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_publishing_destinations_response.ListPublishingDestinationsResponse":
        r"""<p>Returns a list of publishing destinations associated with the specified <code>detectorId</code>.</p>

        Args:
            detector_id: <p>The detector ID for which you want to retrieve the publishing destination.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_publishing_destinations_request.ListPublishingDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_publishing_destinations_response.ListPublishingDestinationsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_publishing_destinations

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_publishing_destinations.async_list_publishing_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_publishing_destinations_request.ListPublishingDestinationsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_guardduty.types.guard_duty_arn.GuardDutyArn",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for a resource. Tagging is currently supported for detectors, finding filters, IP sets, threat intel sets, and publishing destination, with a limit of 50 tags per resource. When invoked, this operation returns all assigned tags for a given resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the given GuardDuty resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_threat_entity_sets(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_threat_entity_sets_response.ListThreatEntitySetsResponse":
        r"""<p>Lists the threat entity sets associated with the specified GuardDuty detector ID. If you use this operation from a member account, the threat entity sets that are returned as a response, belong to the administrator account.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector that is associated with this threat entity set.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_threat_entity_sets_request.ListThreatEntitySetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_threat_entity_sets_response.ListThreatEntitySetsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_threat_entity_sets

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_threat_entity_sets.async_list_threat_entity_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_threat_entity_sets_request.ListThreatEntitySetsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
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

    async def iter_list_threat_entity_sets(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_threat_entity_sets(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("threat_entity_set_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_threat_intel_sets(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_threat_intel_sets_response.ListThreatIntelSetsResponse":
        r"""<p>Lists the ThreatIntelSets of the GuardDuty service specified by the detector ID. If you use this operation from a member account, the ThreatIntelSets associated with the administrator account are returned.</p>

        Args:
            detector_id: <p>The unique ID of the detector that is associated with the threatIntelSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>
            next_token: <p>You can use this parameter to paginate results in the response. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_threat_intel_sets_request.ListThreatIntelSetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_threat_intel_sets_response.ListThreatIntelSetsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_threat_intel_sets

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_threat_intel_sets.async_list_threat_intel_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_threat_intel_sets_request.ListThreatIntelSetsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
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

    async def iter_list_threat_intel_sets(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_threat_intel_sets(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("threat_intel_set_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_trusted_entity_sets(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "aws_sdk_guardduty.types.list_trusted_entity_sets_response.ListTrustedEntitySetsResponse":
        r"""<p>Lists the trusted entity sets associated with the specified GuardDuty detector ID. If you use this operation from a member account, the trusted entity sets that are returned as a response, belong to the administrator account.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector that is associated with this threat entity set.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            max_results: <p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50.</p>
            next_token: <p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.list_trusted_entity_sets_request.ListTrustedEntitySetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.list_trusted_entity_sets_response.ListTrustedEntitySetsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.list_trusted_entity_sets

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.list_trusted_entity_sets.async_list_trusted_entity_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.list_trusted_entity_sets_request.ListTrustedEntitySetsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
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

    async def iter_list_trusted_entity_sets(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        max_results: Optional["aws_sdk_guardduty.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_guardduty.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_guardduty.types.string.String]":
        _token = next_token
        while True:
            _response = await self.list_trusted_entity_sets(
                detector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("trusted_entity_set_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def send_object_malware_scan(
        self,
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        s3_object: Optional[
            "aws_sdk_guardduty.types.s3_object_for_send_object_malware_scan.S3ObjectForSendObjectMalwareScan"
        ] = None,
    ) -> "aws_sdk_guardduty.types.send_object_malware_scan_response.SendObjectMalwareScanResponse":
        r"""<p>Initiates a malware scan for a specific S3 object. This API allows you to perform on-demand malware scanning of individual objects in S3 buckets that have Malware Protection for S3 enabled.</p> <p>When you use this API, the Amazon Web Services service terms for GuardDuty Malware Protection apply. For more information, see <a href=\"http://aws.amazon.com/service-terms/#87._Amazon_GuardDuty\">Amazon Web Services service terms for GuardDuty Malware Protection</a>.</p>

        Args:
            s3_object: <p>The S3 object information for the object you want to scan. The bucket must have a Malware Protection plan configured to use this API.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.send_object_malware_scan_request.SendObjectMalwareScanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.send_object_malware_scan_response.SendObjectMalwareScanResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.send_object_malware_scan

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.send_object_malware_scan.async_send_object_malware_scan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.send_object_malware_scan_request.SendObjectMalwareScanRequest = {}  # type: ignore[typeddict-item]
        if s3_object is not None:
            input_["s3_object"] = s3_object

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_malware_scan(
        self,
        resource_arn: "aws_sdk_guardduty.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        client_token: Optional[
            "aws_sdk_guardduty.types.client_token.ClientToken"
        ] = None,
        scan_configuration: Optional[
            "aws_sdk_guardduty.types.start_malware_scan_configuration.StartMalwareScanConfiguration"
        ] = None,
    ) -> "aws_sdk_guardduty.types.start_malware_scan_response.StartMalwareScanResponse":
        r"""<p>Initiates the malware scan. Invoking this API will automatically create the <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/slr-permissions-malware-protection.html\">Service-linked role</a> in the corresponding account if the resourceArn belongs to an EC2 instance.</p> <p>When the malware scan starts, you can use the associated scan ID to track the status of the scan. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListMalwareScans.html\">ListMalwareScans</a> and <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMalwareScan.html\">GetMalwareScan</a>.</p> <p>When you use this API, the Amazon Web Services service terms for GuardDuty Malware Protection apply. For more information, see <a href=\"http://aws.amazon.com/service-terms/#87._Amazon_GuardDuty\">Amazon Web Services service terms for GuardDuty Malware Protection</a>.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource for which you invoked the API.</p>
            client_token: <p>The idempotency token for the create request.</p>
            scan_configuration: <p>Contains information about the configuration to be used for the malware scan.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.start_malware_scan_request.StartMalwareScanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.start_malware_scan_response.StartMalwareScanResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.start_malware_scan

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.start_malware_scan.async_start_malware_scan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.start_malware_scan_request.StartMalwareScanRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if scan_configuration is not None:
            input_["scan_configuration"] = scan_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_monitoring_members(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.start_monitoring_members_response.StartMonitoringMembersResponse":
        r"""<p>Turns on GuardDuty monitoring of the specified member accounts. Use this operation to restart monitoring of accounts that you stopped monitoring with the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_StopMonitoringMembers.html\">StopMonitoringMembers</a> operation.</p>

        Args:
            detector_id: <p>The unique ID of the detector of the GuardDuty administrator account associated with the member accounts to monitor.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            account_ids: <p>A list of account IDs of the GuardDuty member accounts to start monitoring.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.start_monitoring_members_request.StartMonitoringMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.start_monitoring_members_response.StartMonitoringMembersResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.start_monitoring_members

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.start_monitoring_members.async_start_monitoring_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.start_monitoring_members_request.StartMonitoringMembersRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_monitoring_members(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.stop_monitoring_members_response.StopMonitoringMembersResponse":
        r"""<p>Stops GuardDuty monitoring for the specified member accounts. Use the <code>StartMonitoringMembers</code> operation to restart monitoring for those accounts.</p> <p>With <code>autoEnableOrganizationMembers</code> configuration for your organization set to <code>ALL</code>, you'll receive an error if you attempt to stop monitoring the member accounts in your organization.</p>

        Args:
            detector_id: <p>The unique ID of the detector associated with the GuardDuty administrator account that is monitoring member accounts.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            account_ids: <p>A list of account IDs for the member accounts to stop monitoring.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.stop_monitoring_members_request.StopMonitoringMembersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.stop_monitoring_members_response.StopMonitoringMembersResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.stop_monitoring_members

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.stop_monitoring_members.async_stop_monitoring_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.stop_monitoring_members_request.StopMonitoringMembersRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["account_ids"] = account_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_guardduty.types.guard_duty_arn.GuardDutyArn",
        tags: "aws_sdk_guardduty.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the GuardDuty resource to apply a tag to.</p>
            tags: <p>The tags to be added to a resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def unarchive_findings(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        finding_ids: "aws_sdk_guardduty.types.finding_ids.FindingIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> (
        "aws_sdk_guardduty.types.unarchive_findings_response.UnarchiveFindingsResponse"
    ):
        r"""<p>Unarchives GuardDuty findings specified by the <code>findingIds</code>.</p>

        Args:
            detector_id: <p>The ID of the detector associated with the findings to unarchive.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            finding_ids: <p>The IDs of the findings to unarchive.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.unarchive_findings_request.UnarchiveFindingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.unarchive_findings_response.UnarchiveFindingsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.unarchive_findings

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.unarchive_findings.async_unarchive_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.unarchive_findings_request.UnarchiveFindingsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["finding_ids"] = finding_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_guardduty.types.guard_duty_arn.GuardDutyArn",
        tag_keys: "aws_sdk_guardduty.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
    ) -> "aws_sdk_guardduty.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource to remove tags from.</p>
            tag_keys: <p>The tag keys to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_detector(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        enable: Optional["aws_sdk_guardduty.types.boolean.Boolean"] = None,
        finding_publishing_frequency: Optional[
            "aws_sdk_guardduty.types.finding_publishing_frequency.FindingPublishingFrequency"
        ] = None,
        data_sources: Optional[
            "aws_sdk_guardduty.types.data_source_configurations.DataSourceConfigurations"
        ] = None,
        features: Optional[
            "aws_sdk_guardduty.types.detector_feature_configurations.DetectorFeatureConfigurations"
        ] = None,
    ) -> "aws_sdk_guardduty.types.update_detector_response.UpdateDetectorResponse":
        r"""<p>Updates the GuardDuty detector specified by the detector ID.</p> <p>Specifying both EKS Runtime Monitoring (<code>EKS_RUNTIME_MONITORING</code>) and Runtime Monitoring (<code>RUNTIME_MONITORING</code>) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html\">Runtime Monitoring</a>.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The unique ID of the detector to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            enable: <p>Specifies whether the detector is enabled or not enabled.</p>
            finding_publishing_frequency: <p>An enum value that specifies how frequently findings are exported, such as to CloudWatch Events.</p>
            data_sources: <p>Describes which data sources will be updated.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>
            features: <p>Provides the features that will be updated for the detector.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_detector_request.UpdateDetectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_detector_response.UpdateDetectorResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_detector

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_detector.async_update_detector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_detector_request.UpdateDetectorRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        if enable is not None:
            input_["enable"] = enable
        if finding_publishing_frequency is not None:
            input_["finding_publishing_frequency"] = finding_publishing_frequency
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if features is not None:
            input_["features"] = features

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_filter(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        filter_name: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        description: Optional[
            "aws_sdk_guardduty.types.filter_description.FilterDescription"
        ] = None,
        action: Optional["aws_sdk_guardduty.types.filter_action.FilterAction"] = None,
        rank: Optional["aws_sdk_guardduty.types.filter_rank.FilterRank"] = None,
        finding_criteria: Optional[
            "aws_sdk_guardduty.types.finding_criteria.FindingCriteria"
        ] = None,
    ) -> "aws_sdk_guardduty.types.update_filter_response.UpdateFilterResponse":
        r"""<p>Updates the filter specified by the filter name.</p>

        Args:
            detector_id: <p>The unique ID of the detector that specifies the GuardDuty service where you want to update a filter.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            filter_name: <p>The name of the filter.</p>
            description: <p>The description of the filter. Valid characters include alphanumeric characters, and special characters such as hyphen, period, colon, underscore, parentheses (<code>{ }</code>, <code>[ ]</code>, and <code>( )</code>), forward slash, horizontal tab, vertical tab, newline, form feed, return, and whitespace.</p>
            action: <p>Specifies the action that is to be applied to the findings that match the filter.</p> <p>Default: NOOP</p>
            rank: <p>Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.</p>
            finding_criteria: <p>Represents the criteria to be used in the filter for querying findings. The following fields are available for filtering:</p> <ul> <li> <p>accountId</p> </li> <li> <p>arn</p> </li> <li> <p>associatedAttackSequenceArn</p> </li> <li> <p>confidence</p> </li> <li> <p>createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>id</p> </li> <li> <p>partition</p> </li> <li> <p>region</p> </li> <li> <p>resource.accessKeyDetails.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.accessKeyId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.accountId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.arn</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.attributes.mfaAuthenticated</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.ec2RoleDelivery</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.invokedBy</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.accountId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.arn</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.principalId</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.type</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sessionIssuer.userName</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.sourceIdentity</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.webIdFederationData.attributes</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.sessionContext.webIdFederationData.federatedProvider</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.type</p> </li> <li> <p>resource.accessKeyDetails.userIdentity.userName</p> </li> <li> <p>resource.accessKeyDetails.userName</p> </li> <li> <p>resource.accessKeyDetails.userType</p> </li> <li> <p>resource.bedrockGuardrailDetails.guardrailArn</p> </li> <li> <p>resource.bedrockGuardrailDetails.guardrailVersion</p> </li> <li> <p>resource.containerDetails.containerRuntime</p> </li> <li> <p>resource.containerDetails.id</p> </li> <li> <p>resource.containerDetails.image</p> </li> <li> <p>resource.containerDetails.imagePrefix</p> </li> <li> <p>resource.containerDetails.name</p> </li> <li> <p>resource.containerDetails.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.containerDetails.securityContext.privileged</p> </li> <li> <p>resource.containerDetails.volumeMounts.mountPath</p> </li> <li> <p>resource.containerDetails.volumeMounts.name</p> </li> <li> <p>resource.ebsSnapshotDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.deviceName</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.encryptionType</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.kmsKeyArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeArn</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeSizeInGB</p> </li> <li> <p>resource.ebsVolumeDetails.scannedVolumeDetails.volumeType</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.deviceName</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.encryptionType</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.kmsKeyArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.snapshotArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeArn</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeSizeInGB</p> </li> <li> <p>resource.ebsVolumeDetails.skippedVolumeDetails.volumeType</p> </li> <li> <p>resource.ec2ImageDetails.imageArn</p> </li> <li> <p>resource.ecsClusterDetails.activeServicesCount</p> </li> <li> <p>resource.ecsClusterDetails.arn</p> </li> <li> <p>resource.ecsClusterDetails.name</p> </li> <li> <p>resource.ecsClusterDetails.registeredContainerInstancesCount</p> </li> <li> <p>resource.ecsClusterDetails.runningTasksCount</p> </li> <li> <p>resource.ecsClusterDetails.status</p> </li> <li> <p>resource.ecsClusterDetails.tags.key</p> </li> <li> <p>resource.ecsClusterDetails.tags.value</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.arn</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.containerRuntime</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.id</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.image</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.imagePrefix</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.name</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.securityContext.privileged</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.volumeMounts.mountPath</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.containers.volumeMounts.name</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.definitionArn</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.group</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.launchType</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.startedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.startedBy</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.tags.key</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.tags.value</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.version</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.volumes.hostPath.path</p> </li> <li> <p>resource.ecsClusterDetails.taskDetails.volumes.name</p> </li> <li> <p>resource.eksClusterDetails.arn</p> </li> <li> <p>resource.eksClusterDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.eksClusterDetails.name</p> </li> <li> <p>resource.eksClusterDetails.status</p> </li> <li> <p>resource.eksClusterDetails.tags.key</p> </li> <li> <p>resource.eksClusterDetails.tags.value</p> </li> <li> <p>resource.eksClusterDetails.vpcId</p> </li> <li> <p>resource.instanceDetails.availabilityZone</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.arn</p> </li> <li> <p>resource.instanceDetails.iamInstanceProfile.id</p> </li> <li> <p>resource.instanceDetails.imageDescription</p> </li> <li> <p>resource.instanceDetails.imageId</p> </li> <li> <p>resource.instanceDetails.instanceId</p> </li> <li> <p>resource.instanceDetails.instanceState</p> </li> <li> <p>resource.instanceDetails.instanceType</p> </li> <li> <p>resource.instanceDetails.launchTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.ipv6Addresses</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.networkInterfaceId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.privateIpAddresses.privateIpAddress</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicDnsName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.publicIp</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.securityGroups.groupName</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.subnetId</p> </li> <li> <p>resource.instanceDetails.networkInterfaces.vpcId</p> </li> <li> <p>resource.instanceDetails.outpostArn</p> </li> <li> <p>resource.instanceDetails.platform</p> </li> <li> <p>resource.instanceDetails.productCodes.productCodeId</p> </li> <li> <p>resource.instanceDetails.productCodes.productCodeType</p> </li> <li> <p>resource.instanceDetails.tags.key</p> </li> <li> <p>resource.instanceDetails.tags.value</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.groups</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser.groups</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser.username</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.sessionName</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.uid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesUserDetails.username</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.containerRuntime</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.id</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.image</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.imagePrefix</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.allowPrivilegeEscalation</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.securityContext.privileged</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.volumeMounts.mountPath</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.containers.volumeMounts.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostIpc</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostNetwork</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.hostPid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.name</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.namespace</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.serviceAccountName</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.type</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.uid</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.volumes.hostPath.path</p> </li> <li> <p>resource.kubernetesDetails.kubernetesWorkloadDetails.volumes.name</p> </li> <li> <p>resource.lambdaDetails.description</p> </li> <li> <p>resource.lambdaDetails.functionArn</p> </li> <li> <p>resource.lambdaDetails.functionName</p> </li> <li> <p>resource.lambdaDetails.functionVersion</p> </li> <li> <p>resource.lambdaDetails.lastModifiedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.lambdaDetails.revisionId</p> </li> <li> <p>resource.lambdaDetails.role</p> </li> <li> <p>resource.lambdaDetails.tags.key</p> </li> <li> <p>resource.lambdaDetails.tags.value</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.securityGroups.groupId</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.securityGroups.groupName</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.subnetIds</p> </li> <li> <p>resource.lambdaDetails.vpcConfig.vpcId</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbClusterIdentifier</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbInstanceArn</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbInstanceIdentifier</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbSecurityGroups.name</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbSecurityGroups.status</p> </li> <li> <p>resource.rdsDbInstanceDetails.dbiResourceId</p> </li> <li> <p>resource.rdsDbInstanceDetails.engine</p> </li> <li> <p>resource.rdsDbInstanceDetails.engineVersion</p> </li> <li> <p>resource.rdsDbInstanceDetails.iamDatabaseAuthenticationEnabled</p> </li> <li> <p>resource.rdsDbInstanceDetails.publiclyAccessible</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcId</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcSecurityGroups.status</p> </li> <li> <p>resource.rdsDbInstanceDetails.vpcSecurityGroups.vpcSecurityGroupId</p> </li> <li> <p>resource.rdsDbUserDetails.application</p> </li> <li> <p>resource.rdsDbUserDetails.authMethod</p> </li> <li> <p>resource.rdsDbUserDetails.database</p> </li> <li> <p>resource.rdsDbUserDetails.ssl</p> </li> <li> <p>resource.rdsDbUserDetails.user</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbClusterIdentifier</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupArn</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupIdentifier</p> </li> <li> <p>resource.rdsLimitlessDbDetails.dbShardGroupResourceId</p> </li> <li> <p>resource.rdsLimitlessDbDetails.engine</p> </li> <li> <p>resource.rdsLimitlessDbDetails.engineVersion</p> </li> <li> <p>resource.rdsLimitlessDbDetails.tags.key</p> </li> <li> <p>resource.rdsLimitlessDbDetails.tags.value</p> </li> <li> <p>resource.recoveryPointDetails.backupVaultName</p> </li> <li> <p>resource.recoveryPointDetails.recoveryPointArn</p> </li> <li> <p>resource.resourceType</p> </li> <li> <p>resource.s3BucketDetails.arn</p> </li> <li> <p>resource.s3BucketDetails.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>resource.s3BucketDetails.defaultServerSideEncryption.encryptionType</p> </li> <li> <p>resource.s3BucketDetails.defaultServerSideEncryption.kmsMasterKeyArn</p> </li> <li> <p>resource.s3BucketDetails.name</p> </li> <li> <p>resource.s3BucketDetails.owner.id</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.effectivePermission</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicPolicy</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.ignorePublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.restrictPublicBuckets</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicReadAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList.allowsPublicWriteAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.blockPublicPolicy</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.ignorePublicAcls</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess.restrictPublicBuckets</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicReadAccess</p> </li> <li> <p>resource.s3BucketDetails.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy.allowsPublicWriteAccess</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.eTag</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.hash</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.key</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.objectArn</p> </li> <li> <p>resource.s3BucketDetails.s3ObjectDetails.versionId</p> </li> <li> <p>resource.s3BucketDetails.tags.key</p> </li> <li> <p>resource.s3BucketDetails.tags.value</p> </li> <li> <p>resource.s3BucketDetails.type</p> </li> <li> <p>schemaVersion</p> </li> <li> <p>service.action.actionType</p> </li> <li> <p>service.action.awsApiCallAction.api</p> </li> <li> <p>service.action.awsApiCallAction.callerType</p> </li> <li> <p>service.action.awsApiCallAction.domainDetails.domain</p> </li> <li> <p>service.action.awsApiCallAction.errorCode</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.accountId</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.affiliated</p> </li> <li> <p>service.action.awsApiCallAction.remoteAccountDetails.awsServiceName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.awsApiCallAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.awsApiCallAction.serviceName</p> </li> <li> <p>service.action.awsApiCallAction.userAgent</p> </li> <li> <p>service.action.dnsRequestAction.blocked</p> </li> <li> <p>service.action.dnsRequestAction.domain</p> </li> <li> <p>service.action.dnsRequestAction.domainWithSuffix</p> </li> <li> <p>service.action.dnsRequestAction.protocol</p> </li> <li> <p>service.action.dnsRequestAction.vpcOwnerAccountId</p> </li> <li> <p>service.action.kubernetesApiCallAction.namespace</p> </li> <li> <p>service.action.kubernetesApiCallAction.parameters</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.kubernetesApiCallAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.kubernetesApiCallAction.requestUri</p> </li> <li> <p>service.action.kubernetesApiCallAction.resource</p> </li> <li> <p>service.action.kubernetesApiCallAction.resourceName</p> </li> <li> <p>service.action.kubernetesApiCallAction.sourceIPs</p> </li> <li> <p>service.action.kubernetesApiCallAction.statusCode</p> </li> <li> <p>service.action.kubernetesApiCallAction.subresource</p> </li> <li> <p>service.action.kubernetesApiCallAction.userAgent</p> </li> <li> <p>service.action.kubernetesApiCallAction.verb</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.allowed</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.namespace</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.resource</p> </li> <li> <p>service.action.kubernetesPermissionCheckedDetails.verb</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.kind</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.name</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.roleRefKind</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.roleRefName</p> </li> <li> <p>service.action.kubernetesRoleBindingDetails.uid</p> </li> <li> <p>service.action.kubernetesRoleDetails.kind</p> </li> <li> <p>service.action.kubernetesRoleDetails.name</p> </li> <li> <p>service.action.kubernetesRoleDetails.uid</p> </li> <li> <p>service.action.networkConnectionAction.blocked</p> </li> <li> <p>service.action.networkConnectionAction.connectionDirection</p> </li> <li> <p>service.action.networkConnectionAction.localIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.localIpDetails.ipAddressV6</p> </li> <li> <p>service.action.networkConnectionAction.localNetworkInterface</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.localPortDetails.portName</p> </li> <li> <p>service.action.networkConnectionAction.protocol</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.networkConnectionAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.port</p> </li> <li> <p>service.action.networkConnectionAction.remotePortDetails.portName</p> </li> <li> <p>service.action.portProbeAction.blocked</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localIpDetails.ipAddressV4</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localIpDetails.ipAddressV6</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localPortDetails.port</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.localPortDetails.portName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.portProbeAction.portProbeDetails.remoteIpDetails.organization.org</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.application</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.failedLoginAttempts</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.successfulLoginAttempts</p> </li> <li> <p>service.action.rdsLoginAttemptAction.loginAttributes.user</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.city.cityName</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.country.countryCode</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.country.countryName</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.geoLocation.lat</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.geoLocation.lon</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.ipAddressV4</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.ipAddressV6</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.asn</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.asnOrg</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.isp</p> </li> <li> <p>service.action.rdsLoginAttemptAction.remoteIpDetails.organization.org</p> </li> <li> <p>service.additionalInfo.agentDetails.agentId</p> </li> <li> <p>service.additionalInfo.agentDetails.agentVersion</p> </li> <li> <p>service.additionalInfo.anomalies.anomalousAPIs</p> </li> <li> <p>service.additionalInfo.authenticationMethod</p> </li> <li> <p>service.additionalInfo.averagePacketSizeIn</p> </li> <li> <p>service.additionalInfo.averagePacketSizeOut</p> </li> <li> <p>service.additionalInfo.context</p> </li> <li> <p>service.additionalInfo.domain</p> </li> <li> <p>service.additionalInfo.inBytes</p> </li> <li> <p>service.additionalInfo.localNetworkInterfaceOwner</p> </li> <li> <p>service.additionalInfo.localPort</p> </li> <li> <p>service.additionalInfo.outBytes</p> </li> <li> <p>service.additionalInfo.packetsIn</p> </li> <li> <p>service.additionalInfo.packetsOut</p> </li> <li> <p>service.additionalInfo.policyArn</p> </li> <li> <p>service.additionalInfo.policyName</p> </li> <li> <p>service.additionalInfo.remotePort</p> </li> <li> <p>service.additionalInfo.sample</p> </li> <li> <p>service.additionalInfo.scannedPort</p> </li> <li> <p>service.additionalInfo.threatFileSha256</p> </li> <li> <p>service.additionalInfo.threatListName</p> </li> <li> <p>service.additionalInfo.threatName</p> </li> <li> <p>service.additionalInfo.totalBytesIn</p> </li> <li> <p>service.additionalInfo.totalBytesOut</p> </li> <li> <p>service.additionalInfo.type</p> </li> <li> <p>service.additionalInfo.unusual.asnOrg</p> </li> <li> <p>service.additionalInfo.unusual.port</p> </li> <li> <p>service.additionalInfo.unusualProtocol</p> </li> <li> <p>service.additionalInfo.userAgent.fullUserAgent</p> </li> <li> <p>service.additionalInfo.userAgent.userAgentCategory</p> </li> <li> <p>service.additionalInfo.value</p> </li> <li> <p>service.additionalInfo.vpcOwnerAccountId</p> </li> <li> <p>service.archived</p> </li> <li> <p>service.count</p> </li> <li> <p>service.detection.sequence.actors.id</p> </li> <li> <p>service.detection.sequence.actors.process.name</p> </li> <li> <p>service.detection.sequence.actors.process.path</p> </li> <li> <p>service.detection.sequence.actors.process.sha256</p> </li> <li> <p>service.detection.sequence.actors.session.createdTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.actors.session.issuer</p> </li> <li> <p>service.detection.sequence.actors.session.mfaStatus</p> </li> <li> <p>service.detection.sequence.actors.session.uid</p> </li> <li> <p>service.detection.sequence.actors.user.account.account</p> </li> <li> <p>service.detection.sequence.actors.user.account.uid</p> </li> <li> <p>service.detection.sequence.actors.user.credentialUid</p> </li> <li> <p>service.detection.sequence.actors.user.name</p> </li> <li> <p>service.detection.sequence.actors.user.type</p> </li> <li> <p>service.detection.sequence.actors.user.uid</p> </li> <li> <p>service.detection.sequence.additionalSequenceTypes</p> </li> <li> <p>service.detection.sequence.description</p> </li> <li> <p>service.detection.sequence.endpoints.autonomousSystem.name</p> </li> <li> <p>service.detection.sequence.endpoints.autonomousSystem.number</p> </li> <li> <p>service.detection.sequence.endpoints.connection.direction</p> </li> <li> <p>service.detection.sequence.endpoints.domain</p> </li> <li> <p>service.detection.sequence.endpoints.id</p> </li> <li> <p>service.detection.sequence.endpoints.ip</p> </li> <li> <p>service.detection.sequence.endpoints.location.city</p> </li> <li> <p>service.detection.sequence.endpoints.location.country</p> </li> <li> <p>service.detection.sequence.endpoints.location.lat</p> </li> <li> <p>service.detection.sequence.endpoints.location.lon</p> </li> <li> <p>service.detection.sequence.endpoints.port</p> </li> <li> <p>service.detection.sequence.resources.accountId</p> </li> <li> <p>service.detection.sequence.resources.cloudPartition</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.principalId</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.userName</p> </li> <li> <p>service.detection.sequence.resources.data.accessKey.userType</p> </li> <li> <p>service.detection.sequence.resources.data.autoscalingAutoScalingGroup.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.cloudformationStack.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.container.image</p> </li> <li> <p>service.detection.sequence.resources.data.container.imageUid</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Image.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.availabilityZone</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.ec2NetworkInterfaceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.iamInstanceProfile.arn</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.iamInstanceProfile.id</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.imageDescription</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.instanceState</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.instanceType</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.outpostArn</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.platform</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.productCodes.productCodeId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Instance.productCodes.productCodeType</p> </li> <li> <p>service.detection.sequence.resources.data.ec2LaunchTemplate.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ec2LaunchTemplate.version</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.ipv6Addresses</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.privateIpAddresses.privateDnsName</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.privateIpAddresses.privateIpAddress</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.publicIp</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.securityGroups.groupId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.securityGroups.groupName</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.subNetId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2NetworkInterface.vpcId</p> </li> <li> <p>service.detection.sequence.resources.data.ec2Vpc.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsCluster.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsCluster.status</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.containerUids</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.launchType</p> </li> <li> <p>service.detection.sequence.resources.data.ecsTask.taskDefinitionArn</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.arn</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.status</p> </li> <li> <p>service.detection.sequence.resources.data.eksCluster.vpcId</p> </li> <li> <p>service.detection.sequence.resources.data.iamInstanceProfile.ec2InstanceUids</p> </li> <li> <p>service.detection.sequence.resources.data.iamInstanceProfile.id</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.containerUids</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.namespace</p> </li> <li> <p>service.detection.sequence.resources.data.kubernetesWorkload.type</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicAclAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicAclIgnoreBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicBucketRestrictBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.accountPublicAccess.publicPolicyAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicAclAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicAclIgnoreBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicBucketRestrictBehavior</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.bucketPublicAccess.publicPolicyAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.effectivePermission</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.encryptionKeyArn</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.encryptionType</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.ownerId</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.publicReadAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.publicWriteAccess</p> </li> <li> <p>service.detection.sequence.resources.data.s3Bucket.s3ObjectUids</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.eTag</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.key</p> </li> <li> <p>service.detection.sequence.resources.data.s3Object.versionId</p> </li> <li> <p>service.detection.sequence.resources.name</p> </li> <li> <p>service.detection.sequence.resources.region</p> </li> <li> <p>service.detection.sequence.resources.resourceType</p> </li> <li> <p>service.detection.sequence.resources.service</p> </li> <li> <p>service.detection.sequence.resources.tags.key</p> </li> <li> <p>service.detection.sequence.resources.tags.value</p> </li> <li> <p>service.detection.sequence.resources.uid</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.key</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.title</p> </li> <li> <p>service.detection.sequence.sequenceIndicators.values</p> </li> <li> <p>service.detection.sequence.signals.actorIds</p> </li> <li> <p>service.detection.sequence.signals.count</p> </li> <li> <p>service.detection.sequence.signals.createdAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.description</p> </li> <li> <p>service.detection.sequence.signals.endpointIds</p> </li> <li> <p>service.detection.sequence.signals.firstSeenAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.lastSeenAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.signals.name</p> </li> <li> <p>service.detection.sequence.signals.resourceUids</p> </li> <li> <p>service.detection.sequence.signals.severity</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.key</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.title</p> </li> <li> <p>service.detection.sequence.signals.signalIndicators.values</p> </li> <li> <p>service.detection.sequence.signals.type</p> </li> <li> <p>service.detection.sequence.signals.uid</p> </li> <li> <p>service.detection.sequence.signals.updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.detection.sequence.uid</p> </li> <li> <p>service.detectorId</p> </li> <li> <p>service.ebsVolumeScanDetails.scanCompletedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.count</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.severity</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.highestSeverityThreatDetails.threatName</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.files</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.totalGb</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.scannedItemCount.volumes</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.itemCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.shortened</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.fileName</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.filePath</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.hash</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.volumeArn</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.itemCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.name</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.severity</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.uniqueThreatNameCount</p> </li> <li> <p>service.ebsVolumeScanDetails.scanDetections.threatsDetectedItemCount.files</p> </li> <li> <p>service.ebsVolumeScanDetails.scanId</p> </li> <li> <p>service.ebsVolumeScanDetails.scanStartedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.ebsVolumeScanDetails.scanType</p> </li> <li> <p>service.ebsVolumeScanDetails.sources</p> </li> <li> <p>service.ebsVolumeScanDetails.triggerFindingId</p> </li> <li> <p>service.eventFirstSeen</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.eventLastSeen</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatFileSha256</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatListName</p> </li> <li> <p>service.evidence.threatIntelligenceDetails.threatNames</p> </li> <li> <p>service.featureName</p> </li> <li> <p>service.malwareScanDetails.scanCategory</p> </li> <li> <p>service.malwareScanDetails.scanConfiguration.incrementalScanDetails.baselineResourceArn</p> </li> <li> <p>service.malwareScanDetails.scanConfiguration.triggerType</p> </li> <li> <p>service.malwareScanDetails.scanId</p> </li> <li> <p>service.malwareScanDetails.scanType</p> </li> <li> <p>service.malwareScanDetails.threats.count</p> </li> <li> <p>service.malwareScanDetails.threats.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.additionalInfo.deviceName</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.additionalInfo.versionId</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.itemPath</p> </li> <li> <p>service.malwareScanDetails.threats.itemDetails.resourceArn</p> </li> <li> <p>service.malwareScanDetails.threats.itemPaths.hash</p> </li> <li> <p>service.malwareScanDetails.threats.itemPaths.nestedItemPath</p> </li> <li> <p>service.malwareScanDetails.threats.name</p> </li> <li> <p>service.malwareScanDetails.threats.source</p> </li> <li> <p>service.malwareScanDetails.uniqueThreatCount</p> </li> <li> <p>service.resourceRole</p> </li> <li> <p>service.runtimeDetails.context.addressFamily</p> </li> <li> <p>service.runtimeDetails.context.commandLineExample</p> </li> <li> <p>service.runtimeDetails.context.fileOperation</p> </li> <li> <p>service.runtimeDetails.context.filePath</p> </li> <li> <p>service.runtimeDetails.context.fileSystemType</p> </li> <li> <p>service.runtimeDetails.context.flags</p> </li> <li> <p>service.runtimeDetails.context.ianaProtocolNumber</p> </li> <li> <p>service.runtimeDetails.context.ldPreloadValue</p> </li> <li> <p>service.runtimeDetails.context.libraryPath</p> </li> <li> <p>service.runtimeDetails.context.memoryRegions</p> </li> <li> <p>service.runtimeDetails.context.modifiedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.euid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.executablePath</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.executableSha256</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.euid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.name</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.pid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.userId</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.name</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.pid</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.pwd</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.user</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.userId</p> </li> <li> <p>service.runtimeDetails.context.modifyingProcess.uuid</p> </li> <li> <p>service.runtimeDetails.context.moduleFilePath</p> </li> <li> <p>service.runtimeDetails.context.moduleName</p> </li> <li> <p>service.runtimeDetails.context.moduleSha256</p> </li> <li> <p>service.runtimeDetails.context.mountSource</p> </li> <li> <p>service.runtimeDetails.context.mountTarget</p> </li> <li> <p>service.runtimeDetails.context.relatedFilePaths</p> </li> <li> <p>service.runtimeDetails.context.releaseAgentPath</p> </li> <li> <p>service.runtimeDetails.context.runcBinaryPath</p> </li> <li> <p>service.runtimeDetails.context.scriptPath</p> </li> <li> <p>service.runtimeDetails.context.serviceName</p> </li> <li> <p>service.runtimeDetails.context.shellHistoryFilePath</p> </li> <li> <p>service.runtimeDetails.context.socketPath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.euid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.executablePath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.executableSha256</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.euid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.name</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.pid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.userId</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.name</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.namespacePid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.parentUuid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.pid</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.pwd</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.user</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.userId</p> </li> <li> <p>service.runtimeDetails.context.targetProcess.uuid</p> </li> <li> <p>service.runtimeDetails.context.threatFilePath</p> </li> <li> <p>service.runtimeDetails.context.toolCategory</p> </li> <li> <p>service.runtimeDetails.context.toolName</p> </li> <li> <p>service.runtimeDetails.process.euid</p> </li> <li> <p>service.runtimeDetails.process.executablePath</p> </li> <li> <p>service.runtimeDetails.process.executableSha256</p> </li> <li> <p>service.runtimeDetails.process.lineage.euid</p> </li> <li> <p>service.runtimeDetails.process.lineage.executablePath</p> </li> <li> <p>service.runtimeDetails.process.lineage.name</p> </li> <li> <p>service.runtimeDetails.process.lineage.namespacePid</p> </li> <li> <p>service.runtimeDetails.process.lineage.parentUuid</p> </li> <li> <p>service.runtimeDetails.process.lineage.pid</p> </li> <li> <p>service.runtimeDetails.process.lineage.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.process.lineage.userId</p> </li> <li> <p>service.runtimeDetails.process.lineage.uuid</p> </li> <li> <p>service.runtimeDetails.process.name</p> </li> <li> <p>service.runtimeDetails.process.namespacePid</p> </li> <li> <p>service.runtimeDetails.process.parentUuid</p> </li> <li> <p>service.runtimeDetails.process.pid</p> </li> <li> <p>service.runtimeDetails.process.pwd</p> </li> <li> <p>service.runtimeDetails.process.startTime</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> <li> <p>service.runtimeDetails.process.user</p> </li> <li> <p>service.runtimeDetails.process.userId</p> </li> <li> <p>service.runtimeDetails.process.uuid</p> </li> <li> <p>service.serviceName</p> </li> <li> <p>service.userFeedback</p> </li> <li> <p>severity</p> <p>To configure severity based filters, use the following for the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingCriteria.html\">FindingCriteria</a> condition:</p> <ul> <li> <p> <b>Low</b>: <code>[\"1\", \"2\", \"3\"]</code> </p> </li> <li> <p> <b>Medium</b>: <code>[\"4\", \"5\", \"6\"]</code> </p> </li> <li> <p> <b>High</b>: <code>[\"7\", \"8\"]</code> </p> </li> <li> <p> <b>Critical</b>: <code>[\"9\", \"10\"]</code> </p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html\">Findings severity levels</a> in the <i>Amazon GuardDuty User Guide</i>.</p> </li> <li> <p>type</p> </li> <li> <p>updatedAt</p> <p>Type: Timestamp in Unix Epoch millisecond format. Ex: 1486685375000</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_filter_request.UpdateFilterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_filter_response.UpdateFilterResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_filter

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_filter.async_update_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_filter_request.UpdateFilterRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["filter_name"] = filter_name
        if description is not None:
            input_["description"] = description
        if action is not None:
            input_["action"] = action
        if rank is not None:
            input_["rank"] = rank
        if finding_criteria is not None:
            input_["finding_criteria"] = finding_criteria

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_findings_feedback(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        finding_ids: "aws_sdk_guardduty.types.finding_ids.FindingIds",
        feedback: "aws_sdk_guardduty.types.feedback.Feedback",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        comments: Optional[
            "aws_sdk_guardduty.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> "aws_sdk_guardduty.types.update_findings_feedback_response.UpdateFindingsFeedbackResponse":
        r"""<p>Marks the specified GuardDuty findings as useful or not useful.</p>

        Args:
            detector_id: <p>The ID of the detector that is associated with the findings for which you want to update the feedback.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            finding_ids: <p>The IDs of the findings that you want to mark as useful or not useful.</p>
            feedback: <p>The feedback for the finding.</p>
            comments: <p>Additional feedback about the GuardDuty findings.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_findings_feedback_request.UpdateFindingsFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_findings_feedback_response.UpdateFindingsFeedbackResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_findings_feedback

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_findings_feedback.async_update_findings_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_findings_feedback_request.UpdateFindingsFeedbackRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["finding_ids"] = finding_ids
        input_["feedback"] = feedback
        if comments is not None:
            input_["comments"] = comments

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_ip_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        ip_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        name: Optional["aws_sdk_guardduty.types.name.Name"] = None,
        location: Optional["aws_sdk_guardduty.types.location.Location"] = None,
        activate: Optional["aws_sdk_guardduty.types.boolean.Boolean"] = None,
        expected_bucket_owner: Optional[
            "aws_sdk_guardduty.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_guardduty.types.update_ip_set_response.UpdateIPSetResponse":
        r"""<p>Updates the IPSet specified by the IPSet ID.</p>

        Args:
            detector_id: <p>The detectorID that specifies the GuardDuty service whose IPSet you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            ip_set_id: <p>The unique ID that specifies the IPSet that you want to update.</p>
            name: <p>The unique ID that specifies the IPSet that you want to update.</p>
            location: <p>The updated URI of the file that contains the IPSet. </p>
            activate: <p>The updated Boolean value that specifies whether the IPSet is active or not.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_ip_set_request.UpdateIPSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_ip_set_response.UpdateIPSetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_ip_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_ip_set.async_update_ip_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_ip_set_request.UpdateIPSetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["ip_set_id"] = ip_set_id
        if name is not None:
            input_["name"] = name
        if location is not None:
            input_["location"] = location
        if activate is not None:
            input_["activate"] = activate
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_malware_protection_plan(
        self,
        malware_protection_plan_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        role: Optional["aws_sdk_guardduty.types.string.String"] = None,
        actions: Optional[
            "aws_sdk_guardduty.types.malware_protection_plan_actions.MalwareProtectionPlanActions"
        ] = None,
        protected_resource: Optional[
            "aws_sdk_guardduty.types.update_protected_resource.UpdateProtectedResource"
        ] = None,
    ) -> None:
        """<p>Updates an existing Malware Protection plan resource.</p>

        Args:
            malware_protection_plan_id: <p>A unique identifier associated with the Malware Protection plan.</p>
            role: <p>Amazon Resource Name (ARN) of the IAM role with permissions to scan and add tags to the associated protected resource.</p>
            actions: <p>Information about whether the tags will be added to the S3 object after scanning.</p>
            protected_resource: <p>Information about the protected resource that is associated with the created Malware Protection plan. Presently, <code>S3Bucket</code> is the only supported protected resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_malware_protection_plan_request.UpdateMalwareProtectionPlanRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_malware_protection_plan

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_malware_protection_plan.async_update_malware_protection_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_malware_protection_plan_request.UpdateMalwareProtectionPlanRequest = {}  # type: ignore[typeddict-item]
        input_["malware_protection_plan_id"] = malware_protection_plan_id
        if role is not None:
            input_["role"] = role
        if actions is not None:
            input_["actions"] = actions
        if protected_resource is not None:
            input_["protected_resource"] = protected_resource

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_malware_scan_settings(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        scan_resource_criteria: Optional[
            "aws_sdk_guardduty.types.scan_resource_criteria.ScanResourceCriteria"
        ] = None,
        ebs_snapshot_preservation: Optional[
            "aws_sdk_guardduty.types.ebs_snapshot_preservation.EbsSnapshotPreservation"
        ] = None,
    ) -> "aws_sdk_guardduty.types.update_malware_scan_settings_response.UpdateMalwareScanSettingsResponse":
        r"""<p>Updates the malware scan settings.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The unique ID of the detector that specifies the GuardDuty service where you want to update scan settings.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            scan_resource_criteria: <p>Represents the criteria to be used in the filter for selecting resources to scan.</p>
            ebs_snapshot_preservation: <p>An enum value representing possible snapshot preservation settings.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_malware_scan_settings_request.UpdateMalwareScanSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_malware_scan_settings_response.UpdateMalwareScanSettingsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_malware_scan_settings

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_malware_scan_settings.async_update_malware_scan_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_malware_scan_settings_request.UpdateMalwareScanSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        if scan_resource_criteria is not None:
            input_["scan_resource_criteria"] = scan_resource_criteria
        if ebs_snapshot_preservation is not None:
            input_["ebs_snapshot_preservation"] = ebs_snapshot_preservation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_member_detectors(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        account_ids: "aws_sdk_guardduty.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        data_sources: Optional[
            "aws_sdk_guardduty.types.data_source_configurations.DataSourceConfigurations"
        ] = None,
        features: Optional[
            "aws_sdk_guardduty.types.member_features_configurations.MemberFeaturesConfigurations"
        ] = None,
    ) -> "aws_sdk_guardduty.types.update_member_detectors_response.UpdateMemberDetectorsResponse":
        r"""<p>Contains information on member accounts to be updated.</p> <p>Specifying both EKS Runtime Monitoring (<code>EKS_RUNTIME_MONITORING</code>) and Runtime Monitoring (<code>RUNTIME_MONITORING</code>) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html\">Runtime Monitoring</a>.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The detector ID of the administrator account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            account_ids: <p>A list of member account IDs to be updated.</p>
            data_sources: <p>Describes which data sources will be updated.</p>
            features: <p>A list of features that will be updated for the specified member accounts.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_member_detectors_request.UpdateMemberDetectorsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_member_detectors_response.UpdateMemberDetectorsResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_member_detectors

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_member_detectors.async_update_member_detectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_member_detectors_request.UpdateMemberDetectorsRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["account_ids"] = account_ids
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if features is not None:
            input_["features"] = features

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_organization_configuration(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        auto_enable: Optional["aws_sdk_guardduty.types.boolean.Boolean"] = None,
        data_sources: Optional[
            "aws_sdk_guardduty.types.organization_data_source_configurations.OrganizationDataSourceConfigurations"
        ] = None,
        features: Optional[
            "aws_sdk_guardduty.types.organization_features_configurations.OrganizationFeaturesConfigurations"
        ] = None,
        auto_enable_organization_members: Optional[
            "aws_sdk_guardduty.types.auto_enable_members.AutoEnableMembers"
        ] = None,
    ) -> "aws_sdk_guardduty.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse":
        r"""<p>Configures the delegated administrator account with the provided values. You must provide a value for either <code>autoEnableOrganizationMembers</code> or <code>autoEnable</code>, but not both. </p> <p>Specifying both EKS Runtime Monitoring (<code>EKS_RUNTIME_MONITORING</code>) and Runtime Monitoring (<code>RUNTIME_MONITORING</code>) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html\">Runtime Monitoring</a>.</p> <p>There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html\">Regions and endpoints</a>.</p>

        Args:
            detector_id: <p>The ID of the detector that configures the delegated administrator.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            auto_enable: <p>Represents whether to automatically enable member accounts in the organization. This applies to only new member accounts, not the existing member accounts. When a new account joins the organization, the chosen features will be enabled for them by default.</p> <p>Even though this is still supported, we recommend using <code>AutoEnableOrganizationMembers</code> to achieve the similar results. You must provide a value for either <code>autoEnableOrganizationMembers</code> or <code>autoEnable</code>.</p>
            data_sources: <p>Describes which data sources will be updated.</p>
            features: <p>A list of features that will be configured for the organization.</p>
            auto_enable_organization_members: <p>Indicates the auto-enablement configuration of GuardDuty for the member accounts in the organization. You must provide a value for either <code>autoEnableOrganizationMembers</code> or <code>autoEnable</code>. </p> <p>Use one of the following configuration values for <code>autoEnableOrganizationMembers</code>:</p> <ul> <li> <p> <code>NEW</code>: Indicates that when a new account joins the organization, they will have GuardDuty enabled automatically. </p> </li> <li> <p> <code>ALL</code>: Indicates that all accounts in the organization have GuardDuty enabled automatically. This includes <code>NEW</code> accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.</p> <p>It may take up to 24 hours to update the configuration for all the member accounts.</p> </li> <li> <p> <code>NONE</code>: Indicates that GuardDuty will not be automatically enabled for any account in the organization. The administrator must manage GuardDuty for each account in the organization individually.</p> <p>When you update the auto-enable setting from <code>ALL</code> or <code>NEW</code> to <code>NONE</code>, this action doesn't disable the corresponding option for your existing accounts. This configuration will apply to the new accounts that join the organization. After you update the auto-enable settings, no new account will have the corresponding option as enabled.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_organization_configuration_response.UpdateOrganizationConfigurationResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_organization_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_organization_configuration.async_update_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        if auto_enable is not None:
            input_["auto_enable"] = auto_enable
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if features is not None:
            input_["features"] = features
        if auto_enable_organization_members is not None:
            input_["auto_enable_organization_members"] = (
                auto_enable_organization_members
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_publishing_destination(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        destination_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        destination_properties: Optional[
            "aws_sdk_guardduty.types.destination_properties.DestinationProperties"
        ] = None,
    ) -> "aws_sdk_guardduty.types.update_publishing_destination_response.UpdatePublishingDestinationResponse":
        r"""<p>Updates information about the publishing destination specified by the <code>destinationId</code>.</p>

        Args:
            detector_id: <p>The ID of the detector associated with the publishing destinations to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            destination_id: <p>The ID of the publishing destination to update.</p>
            destination_properties: <p>A <code>DestinationProperties</code> object that includes the <code>DestinationArn</code> and <code>KmsKeyArn</code> of the publishing destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_publishing_destination_request.UpdatePublishingDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_publishing_destination_response.UpdatePublishingDestinationResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_publishing_destination

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_publishing_destination.async_update_publishing_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_publishing_destination_request.UpdatePublishingDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["destination_id"] = destination_id
        if destination_properties is not None:
            input_["destination_properties"] = destination_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_threat_entity_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        threat_entity_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        name: Optional["aws_sdk_guardduty.types.name.Name"] = None,
        location: Optional["aws_sdk_guardduty.types.location.Location"] = None,
        expected_bucket_owner: Optional[
            "aws_sdk_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
        ] = None,
        activate: Optional["aws_sdk_guardduty.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_guardduty.types.update_threat_entity_set_response.UpdateThreatEntitySetResponse":
        r"""<p>Updates the threat entity set associated with the specified <code>threatEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector associated with the threat entity set that you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            threat_entity_set_id: <p>The ID returned by GuardDuty after updating the threat entity set resource.</p>
            name: <p>A user-friendly name to identify the trusted entity set.</p> <p>The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (_).</p>
            location: <p>The URI of the file that contains the trusted entity set.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
            activate: <p>A boolean value that indicates whether GuardDuty is to start using this updated threat entity set. After you update an entity set, you will need to activate it again. It might take up to 15 minutes for the updated entity set to be effective.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_threat_entity_set_request.UpdateThreatEntitySetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_threat_entity_set_response.UpdateThreatEntitySetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_threat_entity_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_threat_entity_set.async_update_threat_entity_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_threat_entity_set_request.UpdateThreatEntitySetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["threat_entity_set_id"] = threat_entity_set_id
        if name is not None:
            input_["name"] = name
        if location is not None:
            input_["location"] = location
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner
        if activate is not None:
            input_["activate"] = activate

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_threat_intel_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        threat_intel_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        name: Optional["aws_sdk_guardduty.types.name.Name"] = None,
        location: Optional["aws_sdk_guardduty.types.location.Location"] = None,
        activate: Optional["aws_sdk_guardduty.types.boolean.Boolean"] = None,
        expected_bucket_owner: Optional[
            "aws_sdk_guardduty.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_guardduty.types.update_threat_intel_set_response.UpdateThreatIntelSetResponse":
        r"""<p>Updates the ThreatIntelSet specified by the ThreatIntelSet ID.</p>

        Args:
            detector_id: <p>The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            threat_intel_set_id: <p>The unique ID that specifies the ThreatIntelSet that you want to update.</p>
            name: <p>The unique ID that specifies the ThreatIntelSet that you want to update.</p>
            location: <p>The updated URI of the file that contains the ThreateIntelSet.</p>
            activate: <p>The updated Boolean value that specifies whether the ThreateIntelSet is active or not.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_threat_intel_set_request.UpdateThreatIntelSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_threat_intel_set_response.UpdateThreatIntelSetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_threat_intel_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_threat_intel_set.async_update_threat_intel_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_threat_intel_set_request.UpdateThreatIntelSetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["threat_intel_set_id"] = threat_intel_set_id
        if name is not None:
            input_["name"] = name
        if location is not None:
            input_["location"] = location
        if activate is not None:
            input_["activate"] = activate
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_trusted_entity_set(
        self,
        detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId",
        trusted_entity_set_id: "aws_sdk_guardduty.types.string.String",
        *,
        config_overrides: Optional[AsyncGuardDutyClientConfig] = None,
        name: Optional["aws_sdk_guardduty.types.name.Name"] = None,
        location: Optional["aws_sdk_guardduty.types.location.Location"] = None,
        expected_bucket_owner: Optional[
            "aws_sdk_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
        ] = None,
        activate: Optional["aws_sdk_guardduty.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_guardduty.types.update_trusted_entity_set_response.UpdateTrustedEntitySetResponse":
        r"""<p>Updates the trusted entity set associated with the specified <code>trustedEntitySetId</code>.</p>

        Args:
            detector_id: <p>The unique ID of the GuardDuty detector associated with the threat entity set that you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>
            trusted_entity_set_id: <p>The ID returned by GuardDuty after updating the trusted entity set resource.</p>
            name: <p>A user-friendly name to identify the trusted entity set.</p> <p>The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (_).</p>
            location: <p>The URI of the file that contains the trusted entity set.</p>
            expected_bucket_owner: <p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>
            activate: <p>A boolean value that indicates whether GuardDuty is to start using this updated trusted entity set. After you update an entity set, you will need to activate it again. It might take up to 15 minutes for the updated entity set to be effective.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_guardduty.types.update_trusted_entity_set_request.UpdateTrustedEntitySetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_guardduty.types.update_trusted_entity_set_response.UpdateTrustedEntitySetResponse"
        ]:
            import aws_sdk_guardduty._operations.guard_duty_api_service.update_trusted_entity_set

            (
                output,
                http_response,
            ) = await aws_sdk_guardduty._operations.guard_duty_api_service.update_trusted_entity_set.async_update_trusted_entity_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_guardduty.types.update_trusted_entity_set_request.UpdateTrustedEntitySetRequest = {}  # type: ignore[typeddict-item]
        input_["detector_id"] = detector_id
        input_["trusted_entity_set_id"] = trusted_entity_set_id
        if name is not None:
            input_["name"] = name
        if location is not None:
            input_["location"] = location
        if expected_bucket_owner is not None:
            input_["expected_bucket_owner"] = expected_bucket_owner
        if activate is not None:
            input_["activate"] = activate

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
