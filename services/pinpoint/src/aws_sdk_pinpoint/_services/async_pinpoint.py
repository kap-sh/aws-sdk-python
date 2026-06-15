"""Generated from Smithy shape ``com.amazonaws.pinpoint#Pinpoint``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_pinpoint._auth._signers
import aws_sdk_pinpoint._auth._sigv4
from aws_sdk_pinpoint._auth._identity import Credentials
from aws_sdk_pinpoint._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_pinpoint._auth._zapros_handler import AuthMiddleware
from aws_sdk_pinpoint._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.__timestamp_iso8601
    import aws_sdk_pinpoint.types.adm_channel_request
    import aws_sdk_pinpoint.types.apns_channel_request
    import aws_sdk_pinpoint.types.apns_sandbox_channel_request
    import aws_sdk_pinpoint.types.apns_voip_channel_request
    import aws_sdk_pinpoint.types.apns_voip_sandbox_channel_request
    import aws_sdk_pinpoint.types.baidu_channel_request
    import aws_sdk_pinpoint.types.create_app_request
    import aws_sdk_pinpoint.types.create_app_response
    import aws_sdk_pinpoint.types.create_application_request
    import aws_sdk_pinpoint.types.create_campaign_request
    import aws_sdk_pinpoint.types.create_campaign_response
    import aws_sdk_pinpoint.types.create_email_template_request
    import aws_sdk_pinpoint.types.create_email_template_response
    import aws_sdk_pinpoint.types.create_export_job_request
    import aws_sdk_pinpoint.types.create_export_job_response
    import aws_sdk_pinpoint.types.create_import_job_request
    import aws_sdk_pinpoint.types.create_import_job_response
    import aws_sdk_pinpoint.types.create_in_app_template_request
    import aws_sdk_pinpoint.types.create_in_app_template_response
    import aws_sdk_pinpoint.types.create_journey_request
    import aws_sdk_pinpoint.types.create_journey_response
    import aws_sdk_pinpoint.types.create_push_template_request
    import aws_sdk_pinpoint.types.create_push_template_response
    import aws_sdk_pinpoint.types.create_recommender_configuration_request
    import aws_sdk_pinpoint.types.create_recommender_configuration_response
    import aws_sdk_pinpoint.types.create_recommender_configuration_shape
    import aws_sdk_pinpoint.types.create_segment_request
    import aws_sdk_pinpoint.types.create_segment_response
    import aws_sdk_pinpoint.types.create_sms_template_request
    import aws_sdk_pinpoint.types.create_sms_template_response
    import aws_sdk_pinpoint.types.create_voice_template_request
    import aws_sdk_pinpoint.types.create_voice_template_response
    import aws_sdk_pinpoint.types.delete_adm_channel_request
    import aws_sdk_pinpoint.types.delete_adm_channel_response
    import aws_sdk_pinpoint.types.delete_apns_channel_request
    import aws_sdk_pinpoint.types.delete_apns_channel_response
    import aws_sdk_pinpoint.types.delete_apns_sandbox_channel_request
    import aws_sdk_pinpoint.types.delete_apns_sandbox_channel_response
    import aws_sdk_pinpoint.types.delete_apns_voip_channel_request
    import aws_sdk_pinpoint.types.delete_apns_voip_channel_response
    import aws_sdk_pinpoint.types.delete_apns_voip_sandbox_channel_request
    import aws_sdk_pinpoint.types.delete_apns_voip_sandbox_channel_response
    import aws_sdk_pinpoint.types.delete_app_request
    import aws_sdk_pinpoint.types.delete_app_response
    import aws_sdk_pinpoint.types.delete_baidu_channel_request
    import aws_sdk_pinpoint.types.delete_baidu_channel_response
    import aws_sdk_pinpoint.types.delete_campaign_request
    import aws_sdk_pinpoint.types.delete_campaign_response
    import aws_sdk_pinpoint.types.delete_email_channel_request
    import aws_sdk_pinpoint.types.delete_email_channel_response
    import aws_sdk_pinpoint.types.delete_email_template_request
    import aws_sdk_pinpoint.types.delete_email_template_response
    import aws_sdk_pinpoint.types.delete_endpoint_request
    import aws_sdk_pinpoint.types.delete_endpoint_response
    import aws_sdk_pinpoint.types.delete_event_stream_request
    import aws_sdk_pinpoint.types.delete_event_stream_response
    import aws_sdk_pinpoint.types.delete_gcm_channel_request
    import aws_sdk_pinpoint.types.delete_gcm_channel_response
    import aws_sdk_pinpoint.types.delete_in_app_template_request
    import aws_sdk_pinpoint.types.delete_in_app_template_response
    import aws_sdk_pinpoint.types.delete_journey_request
    import aws_sdk_pinpoint.types.delete_journey_response
    import aws_sdk_pinpoint.types.delete_push_template_request
    import aws_sdk_pinpoint.types.delete_push_template_response
    import aws_sdk_pinpoint.types.delete_recommender_configuration_request
    import aws_sdk_pinpoint.types.delete_recommender_configuration_response
    import aws_sdk_pinpoint.types.delete_segment_request
    import aws_sdk_pinpoint.types.delete_segment_response
    import aws_sdk_pinpoint.types.delete_sms_channel_request
    import aws_sdk_pinpoint.types.delete_sms_channel_response
    import aws_sdk_pinpoint.types.delete_sms_template_request
    import aws_sdk_pinpoint.types.delete_sms_template_response
    import aws_sdk_pinpoint.types.delete_user_endpoints_request
    import aws_sdk_pinpoint.types.delete_user_endpoints_response
    import aws_sdk_pinpoint.types.delete_voice_channel_request
    import aws_sdk_pinpoint.types.delete_voice_channel_response
    import aws_sdk_pinpoint.types.delete_voice_template_request
    import aws_sdk_pinpoint.types.delete_voice_template_response
    import aws_sdk_pinpoint.types.email_channel_request
    import aws_sdk_pinpoint.types.email_template_request
    import aws_sdk_pinpoint.types.endpoint_batch_request
    import aws_sdk_pinpoint.types.endpoint_request
    import aws_sdk_pinpoint.types.events_request
    import aws_sdk_pinpoint.types.export_job_request
    import aws_sdk_pinpoint.types.gcm_channel_request
    import aws_sdk_pinpoint.types.get_adm_channel_request
    import aws_sdk_pinpoint.types.get_adm_channel_response
    import aws_sdk_pinpoint.types.get_apns_channel_request
    import aws_sdk_pinpoint.types.get_apns_channel_response
    import aws_sdk_pinpoint.types.get_apns_sandbox_channel_request
    import aws_sdk_pinpoint.types.get_apns_sandbox_channel_response
    import aws_sdk_pinpoint.types.get_apns_voip_channel_request
    import aws_sdk_pinpoint.types.get_apns_voip_channel_response
    import aws_sdk_pinpoint.types.get_apns_voip_sandbox_channel_request
    import aws_sdk_pinpoint.types.get_apns_voip_sandbox_channel_response
    import aws_sdk_pinpoint.types.get_app_request
    import aws_sdk_pinpoint.types.get_app_response
    import aws_sdk_pinpoint.types.get_application_date_range_kpi_request
    import aws_sdk_pinpoint.types.get_application_date_range_kpi_response
    import aws_sdk_pinpoint.types.get_application_settings_request
    import aws_sdk_pinpoint.types.get_application_settings_response
    import aws_sdk_pinpoint.types.get_apps_request
    import aws_sdk_pinpoint.types.get_apps_response
    import aws_sdk_pinpoint.types.get_baidu_channel_request
    import aws_sdk_pinpoint.types.get_baidu_channel_response
    import aws_sdk_pinpoint.types.get_campaign_activities_request
    import aws_sdk_pinpoint.types.get_campaign_activities_response
    import aws_sdk_pinpoint.types.get_campaign_date_range_kpi_request
    import aws_sdk_pinpoint.types.get_campaign_date_range_kpi_response
    import aws_sdk_pinpoint.types.get_campaign_request
    import aws_sdk_pinpoint.types.get_campaign_response
    import aws_sdk_pinpoint.types.get_campaign_version_request
    import aws_sdk_pinpoint.types.get_campaign_version_response
    import aws_sdk_pinpoint.types.get_campaign_versions_request
    import aws_sdk_pinpoint.types.get_campaign_versions_response
    import aws_sdk_pinpoint.types.get_campaigns_request
    import aws_sdk_pinpoint.types.get_campaigns_response
    import aws_sdk_pinpoint.types.get_channels_request
    import aws_sdk_pinpoint.types.get_channels_response
    import aws_sdk_pinpoint.types.get_email_channel_request
    import aws_sdk_pinpoint.types.get_email_channel_response
    import aws_sdk_pinpoint.types.get_email_template_request
    import aws_sdk_pinpoint.types.get_email_template_response
    import aws_sdk_pinpoint.types.get_endpoint_request
    import aws_sdk_pinpoint.types.get_endpoint_response
    import aws_sdk_pinpoint.types.get_event_stream_request
    import aws_sdk_pinpoint.types.get_event_stream_response
    import aws_sdk_pinpoint.types.get_export_job_request
    import aws_sdk_pinpoint.types.get_export_job_response
    import aws_sdk_pinpoint.types.get_export_jobs_request
    import aws_sdk_pinpoint.types.get_export_jobs_response
    import aws_sdk_pinpoint.types.get_gcm_channel_request
    import aws_sdk_pinpoint.types.get_gcm_channel_response
    import aws_sdk_pinpoint.types.get_import_job_request
    import aws_sdk_pinpoint.types.get_import_job_response
    import aws_sdk_pinpoint.types.get_import_jobs_request
    import aws_sdk_pinpoint.types.get_import_jobs_response
    import aws_sdk_pinpoint.types.get_in_app_messages_request
    import aws_sdk_pinpoint.types.get_in_app_messages_response
    import aws_sdk_pinpoint.types.get_in_app_template_request
    import aws_sdk_pinpoint.types.get_in_app_template_response
    import aws_sdk_pinpoint.types.get_journey_date_range_kpi_request
    import aws_sdk_pinpoint.types.get_journey_date_range_kpi_response
    import aws_sdk_pinpoint.types.get_journey_execution_activity_metrics_request
    import aws_sdk_pinpoint.types.get_journey_execution_activity_metrics_response
    import aws_sdk_pinpoint.types.get_journey_execution_metrics_request
    import aws_sdk_pinpoint.types.get_journey_execution_metrics_response
    import aws_sdk_pinpoint.types.get_journey_request
    import aws_sdk_pinpoint.types.get_journey_response
    import aws_sdk_pinpoint.types.get_journey_run_execution_activity_metrics_request
    import aws_sdk_pinpoint.types.get_journey_run_execution_activity_metrics_response
    import aws_sdk_pinpoint.types.get_journey_run_execution_metrics_request
    import aws_sdk_pinpoint.types.get_journey_run_execution_metrics_response
    import aws_sdk_pinpoint.types.get_journey_runs_request
    import aws_sdk_pinpoint.types.get_journey_runs_response
    import aws_sdk_pinpoint.types.get_push_template_request
    import aws_sdk_pinpoint.types.get_push_template_response
    import aws_sdk_pinpoint.types.get_recommender_configuration_request
    import aws_sdk_pinpoint.types.get_recommender_configuration_response
    import aws_sdk_pinpoint.types.get_recommender_configurations_request
    import aws_sdk_pinpoint.types.get_recommender_configurations_response
    import aws_sdk_pinpoint.types.get_segment_export_jobs_request
    import aws_sdk_pinpoint.types.get_segment_export_jobs_response
    import aws_sdk_pinpoint.types.get_segment_import_jobs_request
    import aws_sdk_pinpoint.types.get_segment_import_jobs_response
    import aws_sdk_pinpoint.types.get_segment_request
    import aws_sdk_pinpoint.types.get_segment_response
    import aws_sdk_pinpoint.types.get_segment_version_request
    import aws_sdk_pinpoint.types.get_segment_version_response
    import aws_sdk_pinpoint.types.get_segment_versions_request
    import aws_sdk_pinpoint.types.get_segment_versions_response
    import aws_sdk_pinpoint.types.get_segments_request
    import aws_sdk_pinpoint.types.get_segments_response
    import aws_sdk_pinpoint.types.get_sms_channel_request
    import aws_sdk_pinpoint.types.get_sms_channel_response
    import aws_sdk_pinpoint.types.get_sms_template_request
    import aws_sdk_pinpoint.types.get_sms_template_response
    import aws_sdk_pinpoint.types.get_user_endpoints_request
    import aws_sdk_pinpoint.types.get_user_endpoints_response
    import aws_sdk_pinpoint.types.get_voice_channel_request
    import aws_sdk_pinpoint.types.get_voice_channel_response
    import aws_sdk_pinpoint.types.get_voice_template_request
    import aws_sdk_pinpoint.types.get_voice_template_response
    import aws_sdk_pinpoint.types.import_job_request
    import aws_sdk_pinpoint.types.in_app_template_request
    import aws_sdk_pinpoint.types.journey_state_request
    import aws_sdk_pinpoint.types.list_journeys_request
    import aws_sdk_pinpoint.types.list_journeys_response
    import aws_sdk_pinpoint.types.list_of__string
    import aws_sdk_pinpoint.types.list_tags_for_resource_request
    import aws_sdk_pinpoint.types.list_tags_for_resource_response
    import aws_sdk_pinpoint.types.list_template_versions_request
    import aws_sdk_pinpoint.types.list_template_versions_response
    import aws_sdk_pinpoint.types.list_templates_request
    import aws_sdk_pinpoint.types.list_templates_response
    import aws_sdk_pinpoint.types.message_request
    import aws_sdk_pinpoint.types.number_validate_request
    import aws_sdk_pinpoint.types.phone_number_validate_request
    import aws_sdk_pinpoint.types.phone_number_validate_response
    import aws_sdk_pinpoint.types.push_notification_template_request
    import aws_sdk_pinpoint.types.put_event_stream_request
    import aws_sdk_pinpoint.types.put_event_stream_response
    import aws_sdk_pinpoint.types.put_events_request
    import aws_sdk_pinpoint.types.put_events_response
    import aws_sdk_pinpoint.types.remove_attributes_request
    import aws_sdk_pinpoint.types.remove_attributes_response
    import aws_sdk_pinpoint.types.send_messages_request
    import aws_sdk_pinpoint.types.send_messages_response
    import aws_sdk_pinpoint.types.send_otp_message_request
    import aws_sdk_pinpoint.types.send_otp_message_request_parameters
    import aws_sdk_pinpoint.types.send_otp_message_response
    import aws_sdk_pinpoint.types.send_users_message_request
    import aws_sdk_pinpoint.types.send_users_messages_request
    import aws_sdk_pinpoint.types.send_users_messages_response
    import aws_sdk_pinpoint.types.sms_channel_request
    import aws_sdk_pinpoint.types.sms_template_request
    import aws_sdk_pinpoint.types.tag_resource_request
    import aws_sdk_pinpoint.types.tags_model
    import aws_sdk_pinpoint.types.template_active_version_request
    import aws_sdk_pinpoint.types.untag_resource_request
    import aws_sdk_pinpoint.types.update_adm_channel_request
    import aws_sdk_pinpoint.types.update_adm_channel_response
    import aws_sdk_pinpoint.types.update_apns_channel_request
    import aws_sdk_pinpoint.types.update_apns_channel_response
    import aws_sdk_pinpoint.types.update_apns_sandbox_channel_request
    import aws_sdk_pinpoint.types.update_apns_sandbox_channel_response
    import aws_sdk_pinpoint.types.update_apns_voip_channel_request
    import aws_sdk_pinpoint.types.update_apns_voip_channel_response
    import aws_sdk_pinpoint.types.update_apns_voip_sandbox_channel_request
    import aws_sdk_pinpoint.types.update_apns_voip_sandbox_channel_response
    import aws_sdk_pinpoint.types.update_application_settings_request
    import aws_sdk_pinpoint.types.update_application_settings_response
    import aws_sdk_pinpoint.types.update_attributes_request
    import aws_sdk_pinpoint.types.update_baidu_channel_request
    import aws_sdk_pinpoint.types.update_baidu_channel_response
    import aws_sdk_pinpoint.types.update_campaign_request
    import aws_sdk_pinpoint.types.update_campaign_response
    import aws_sdk_pinpoint.types.update_email_channel_request
    import aws_sdk_pinpoint.types.update_email_channel_response
    import aws_sdk_pinpoint.types.update_email_template_request
    import aws_sdk_pinpoint.types.update_email_template_response
    import aws_sdk_pinpoint.types.update_endpoint_request
    import aws_sdk_pinpoint.types.update_endpoint_response
    import aws_sdk_pinpoint.types.update_endpoints_batch_request
    import aws_sdk_pinpoint.types.update_endpoints_batch_response
    import aws_sdk_pinpoint.types.update_gcm_channel_request
    import aws_sdk_pinpoint.types.update_gcm_channel_response
    import aws_sdk_pinpoint.types.update_in_app_template_request
    import aws_sdk_pinpoint.types.update_in_app_template_response
    import aws_sdk_pinpoint.types.update_journey_request
    import aws_sdk_pinpoint.types.update_journey_response
    import aws_sdk_pinpoint.types.update_journey_state_request
    import aws_sdk_pinpoint.types.update_journey_state_response
    import aws_sdk_pinpoint.types.update_push_template_request
    import aws_sdk_pinpoint.types.update_push_template_response
    import aws_sdk_pinpoint.types.update_recommender_configuration_request
    import aws_sdk_pinpoint.types.update_recommender_configuration_response
    import aws_sdk_pinpoint.types.update_recommender_configuration_shape
    import aws_sdk_pinpoint.types.update_segment_request
    import aws_sdk_pinpoint.types.update_segment_response
    import aws_sdk_pinpoint.types.update_sms_channel_request
    import aws_sdk_pinpoint.types.update_sms_channel_response
    import aws_sdk_pinpoint.types.update_sms_template_request
    import aws_sdk_pinpoint.types.update_sms_template_response
    import aws_sdk_pinpoint.types.update_template_active_version_request
    import aws_sdk_pinpoint.types.update_template_active_version_response
    import aws_sdk_pinpoint.types.update_voice_channel_request
    import aws_sdk_pinpoint.types.update_voice_channel_response
    import aws_sdk_pinpoint.types.update_voice_template_request
    import aws_sdk_pinpoint.types.update_voice_template_response
    import aws_sdk_pinpoint.types.verify_otp_message_request
    import aws_sdk_pinpoint.types.verify_otp_message_request_parameters
    import aws_sdk_pinpoint.types.verify_otp_message_response
    import aws_sdk_pinpoint.types.voice_channel_request
    import aws_sdk_pinpoint.types.voice_template_request
    import aws_sdk_pinpoint.types.write_application_settings_request
    import aws_sdk_pinpoint.types.write_campaign_request
    import aws_sdk_pinpoint.types.write_event_stream
    import aws_sdk_pinpoint.types.write_journey_request
    import aws_sdk_pinpoint.types.write_segment_request


class AsyncPinpointClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncPinpointClient:
    """A client for the ``Pinpoint`` service.

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
        self._config = AsyncPinpointClientConfig(
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
        self, config_overrides: Optional[AsyncPinpointClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPinpointClientConfig = config_overrides or {}
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

    async def create_app(
        self,
        create_application_request: "aws_sdk_pinpoint.types.create_application_request.CreateApplicationRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_app_response.CreateAppResponse":
        """<p>Creates an application.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_app_request.CreateAppRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_app_response.CreateAppResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_app

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_app.async_create_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_app_request.CreateAppRequest = {}  # type: ignore[typeddict-item]
        input_["create_application_request"] = create_application_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_campaign(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        write_campaign_request: "aws_sdk_pinpoint.types.write_campaign_request.WriteCampaignRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_campaign_response.CreateCampaignResponse":
        """<p>Creates a new campaign for an application or updates the settings of an existing campaign for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_campaign_request.CreateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_campaign

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_campaign.async_create_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_campaign_request.CreateCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["write_campaign_request"] = write_campaign_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_email_template(
        self,
        email_template_request: "aws_sdk_pinpoint.types.email_template_request.EmailTemplateRequest",
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_email_template_response.CreateEmailTemplateResponse":
        """<p>Creates a message template for messages that are sent through the email channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_email_template_request.CreateEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_email_template_response.CreateEmailTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_email_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_email_template.async_create_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_email_template_request.CreateEmailTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["email_template_request"] = email_template_request
        input_["template_name"] = template_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_export_job(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        export_job_request: "aws_sdk_pinpoint.types.export_job_request.ExportJobRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_export_job_response.CreateExportJobResponse":
        """<p>Creates an export job for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_export_job_request.CreateExportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_export_job_response.CreateExportJobResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_export_job

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_export_job.async_create_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_export_job_request.CreateExportJobRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["export_job_request"] = export_job_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_import_job(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        import_job_request: "aws_sdk_pinpoint.types.import_job_request.ImportJobRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_import_job_response.CreateImportJobResponse":
        """<p>Creates an import job for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_import_job_request.CreateImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_import_job_response.CreateImportJobResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_import_job.async_create_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_import_job_request.CreateImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["import_job_request"] = import_job_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_in_app_template(
        self,
        in_app_template_request: "aws_sdk_pinpoint.types.in_app_template_request.InAppTemplateRequest",
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_in_app_template_response.CreateInAppTemplateResponse":
        """<p>Creates a new message template for messages using the in-app message channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_in_app_template_request.CreateInAppTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_in_app_template_response.CreateInAppTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_in_app_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_in_app_template.async_create_in_app_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_in_app_template_request.CreateInAppTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["in_app_template_request"] = in_app_template_request
        input_["template_name"] = template_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_journey(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        write_journey_request: "aws_sdk_pinpoint.types.write_journey_request.WriteJourneyRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_journey_response.CreateJourneyResponse":
        """<p>Creates a journey for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_journey_request.CreateJourneyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_journey_response.CreateJourneyResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_journey

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_journey.async_create_journey(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_journey_request.CreateJourneyRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["write_journey_request"] = write_journey_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_push_template(
        self,
        push_notification_template_request: "aws_sdk_pinpoint.types.push_notification_template_request.PushNotificationTemplateRequest",
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_push_template_response.CreatePushTemplateResponse":
        """<p>Creates a message template for messages that are sent through a push notification channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_push_template_request.CreatePushTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_push_template_response.CreatePushTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_push_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_push_template.async_create_push_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_push_template_request.CreatePushTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["push_notification_template_request"] = (
            push_notification_template_request
        )
        input_["template_name"] = template_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_recommender_configuration(
        self,
        create_recommender_configuration: "aws_sdk_pinpoint.types.create_recommender_configuration_shape.CreateRecommenderConfigurationShape",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_recommender_configuration_response.CreateRecommenderConfigurationResponse":
        """<p>Creates an Amazon Pinpoint configuration for a recommender model.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_recommender_configuration_request.CreateRecommenderConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_recommender_configuration_response.CreateRecommenderConfigurationResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_recommender_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_recommender_configuration.async_create_recommender_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_recommender_configuration_request.CreateRecommenderConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["create_recommender_configuration"] = create_recommender_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_segment(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        write_segment_request: "aws_sdk_pinpoint.types.write_segment_request.WriteSegmentRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_segment_response.CreateSegmentResponse":
        """<p>Creates a new segment for an application or updates the configuration, dimension, and other settings for an existing segment that's associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_segment_request.CreateSegmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_segment_response.CreateSegmentResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_segment

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_segment.async_create_segment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_segment_request.CreateSegmentRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["write_segment_request"] = write_segment_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_sms_template(
        self,
        sms_template_request: "aws_sdk_pinpoint.types.sms_template_request.SMSTemplateRequest",
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> (
        "aws_sdk_pinpoint.types.create_sms_template_response.CreateSmsTemplateResponse"
    ):
        """<p>Creates a message template for messages that are sent through the SMS channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_sms_template_request.CreateSmsTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_sms_template_response.CreateSmsTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_sms_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_sms_template.async_create_sms_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_sms_template_request.CreateSmsTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["sms_template_request"] = sms_template_request
        input_["template_name"] = template_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_voice_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        voice_template_request: "aws_sdk_pinpoint.types.voice_template_request.VoiceTemplateRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.create_voice_template_response.CreateVoiceTemplateResponse":
        """<p>Creates a message template for messages that are sent through the voice channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.create_voice_template_request.CreateVoiceTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.create_voice_template_response.CreateVoiceTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.create_voice_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.create_voice_template.async_create_voice_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.create_voice_template_request.CreateVoiceTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        input_["voice_template_request"] = voice_template_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_adm_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_adm_channel_response.DeleteAdmChannelResponse":
        """<p>Disables the ADM channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_adm_channel_request.DeleteAdmChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_adm_channel_response.DeleteAdmChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_adm_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_adm_channel.async_delete_adm_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_adm_channel_request.DeleteAdmChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_apns_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> (
        "aws_sdk_pinpoint.types.delete_apns_channel_response.DeleteApnsChannelResponse"
    ):
        """<p>Disables the APNs channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_apns_channel_request.DeleteApnsChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_apns_channel_response.DeleteApnsChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_apns_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_apns_channel.async_delete_apns_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_apns_channel_request.DeleteApnsChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_apns_sandbox_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_apns_sandbox_channel_response.DeleteApnsSandboxChannelResponse":
        """<p>Disables the APNs sandbox channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_apns_sandbox_channel_request.DeleteApnsSandboxChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_apns_sandbox_channel_response.DeleteApnsSandboxChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_apns_sandbox_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_apns_sandbox_channel.async_delete_apns_sandbox_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_apns_sandbox_channel_request.DeleteApnsSandboxChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_apns_voip_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_apns_voip_channel_response.DeleteApnsVoipChannelResponse":
        """<p>Disables the APNs VoIP channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_apns_voip_channel_request.DeleteApnsVoipChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_apns_voip_channel_response.DeleteApnsVoipChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_apns_voip_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_apns_voip_channel.async_delete_apns_voip_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_apns_voip_channel_request.DeleteApnsVoipChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_apns_voip_sandbox_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_apns_voip_sandbox_channel_response.DeleteApnsVoipSandboxChannelResponse":
        """<p>Disables the APNs VoIP sandbox channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_apns_voip_sandbox_channel_request.DeleteApnsVoipSandboxChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_apns_voip_sandbox_channel_response.DeleteApnsVoipSandboxChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_apns_voip_sandbox_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_apns_voip_sandbox_channel.async_delete_apns_voip_sandbox_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_apns_voip_sandbox_channel_request.DeleteApnsVoipSandboxChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_app(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_app_response.DeleteAppResponse":
        """<p>Deletes an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_app_request.DeleteAppRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_app_response.DeleteAppResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_app

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_app.async_delete_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_app_request.DeleteAppRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_baidu_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_baidu_channel_response.DeleteBaiduChannelResponse":
        """<p>Disables the Baidu channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_baidu_channel_request.DeleteBaiduChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_baidu_channel_response.DeleteBaiduChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_baidu_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_baidu_channel.async_delete_baidu_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_baidu_channel_request.DeleteBaiduChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_campaign(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        campaign_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_campaign_response.DeleteCampaignResponse":
        """<p>Deletes a campaign from an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_campaign_response.DeleteCampaignResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_campaign

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_campaign.async_delete_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_campaign_request.DeleteCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["campaign_id"] = campaign_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_email_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_email_channel_response.DeleteEmailChannelResponse":
        """<p>Disables the email channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_email_channel_request.DeleteEmailChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_email_channel_response.DeleteEmailChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_email_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_email_channel.async_delete_email_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_email_channel_request.DeleteEmailChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_email_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.delete_email_template_response.DeleteEmailTemplateResponse":
        r"""<p>Deletes a message template for messages that were sent through the email channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_email_template_request.DeleteEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_email_template_response.DeleteEmailTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_email_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_email_template.async_delete_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_email_template_request.DeleteEmailTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_endpoint(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        endpoint_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_endpoint_response.DeleteEndpointResponse":
        """<p>Deletes an endpoint from an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            endpoint_id: <p>The case insensitive unique identifier for the endpoint. The identifier can't contain <code>$</code>, <code>{</code> or <code>}</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_endpoint_request.DeleteEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_endpoint_response.DeleteEndpointResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_endpoint.async_delete_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_endpoint_request.DeleteEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["endpoint_id"] = endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_event_stream(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> (
        "aws_sdk_pinpoint.types.delete_event_stream_response.DeleteEventStreamResponse"
    ):
        """<p>Deletes the event stream for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_event_stream_request.DeleteEventStreamRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_event_stream_response.DeleteEventStreamResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_event_stream

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_event_stream.async_delete_event_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_event_stream_request.DeleteEventStreamRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_gcm_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_gcm_channel_response.DeleteGcmChannelResponse":
        """<p>Disables the GCM channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_gcm_channel_request.DeleteGcmChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_gcm_channel_response.DeleteGcmChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_gcm_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_gcm_channel.async_delete_gcm_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_gcm_channel_request.DeleteGcmChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_in_app_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.delete_in_app_template_response.DeleteInAppTemplateResponse":
        r"""<p>Deletes a message template for messages sent using the in-app message channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_in_app_template_request.DeleteInAppTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_in_app_template_response.DeleteInAppTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_in_app_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_in_app_template.async_delete_in_app_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_in_app_template_request.DeleteInAppTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_journey(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_journey_response.DeleteJourneyResponse":
        """<p>Deletes a journey from an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_journey_request.DeleteJourneyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_journey_response.DeleteJourneyResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_journey

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_journey.async_delete_journey(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_journey_request.DeleteJourneyRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["journey_id"] = journey_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_push_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.delete_push_template_response.DeletePushTemplateResponse":
        r"""<p>Deletes a message template for messages that were sent through a push notification channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_push_template_request.DeletePushTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_push_template_response.DeletePushTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_push_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_push_template.async_delete_push_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_push_template_request.DeletePushTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_recommender_configuration(
        self,
        recommender_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_recommender_configuration_response.DeleteRecommenderConfigurationResponse":
        """<p>Deletes an Amazon Pinpoint configuration for a recommender model.</p>

        Args:
            recommender_id: <p>The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_recommender_configuration_request.DeleteRecommenderConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_recommender_configuration_response.DeleteRecommenderConfigurationResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_recommender_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_recommender_configuration.async_delete_recommender_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_recommender_configuration_request.DeleteRecommenderConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["recommender_id"] = recommender_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_segment(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        segment_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_segment_response.DeleteSegmentResponse":
        """<p>Deletes a segment from an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            segment_id: <p>The unique identifier for the segment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_segment_request.DeleteSegmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_segment_response.DeleteSegmentResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_segment

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_segment.async_delete_segment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_segment_request.DeleteSegmentRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["segment_id"] = segment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_sms_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_sms_channel_response.DeleteSmsChannelResponse":
        """<p>Disables the SMS channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_sms_channel_request.DeleteSmsChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_sms_channel_response.DeleteSmsChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_sms_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_sms_channel.async_delete_sms_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_sms_channel_request.DeleteSmsChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_sms_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> (
        "aws_sdk_pinpoint.types.delete_sms_template_response.DeleteSmsTemplateResponse"
    ):
        r"""<p>Deletes a message template for messages that were sent through the SMS channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_sms_template_request.DeleteSmsTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_sms_template_response.DeleteSmsTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_sms_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_sms_template.async_delete_sms_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_sms_template_request.DeleteSmsTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_user_endpoints(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        user_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_user_endpoints_response.DeleteUserEndpointsResponse":
        """<p>Deletes all the endpoints that are associated with a specific user ID.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            user_id: <p>The unique identifier for the user.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_user_endpoints_request.DeleteUserEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_user_endpoints_response.DeleteUserEndpointsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_user_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_user_endpoints.async_delete_user_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_user_endpoints_request.DeleteUserEndpointsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_voice_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.delete_voice_channel_response.DeleteVoiceChannelResponse":
        """<p>Disables the voice channel for an application and deletes any existing settings for the channel.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_voice_channel_request.DeleteVoiceChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_voice_channel_response.DeleteVoiceChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_voice_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_voice_channel.async_delete_voice_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_voice_channel_request.DeleteVoiceChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_voice_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.delete_voice_template_response.DeleteVoiceTemplateResponse":
        r"""<p>Deletes a message template for messages that were sent through the voice channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.delete_voice_template_request.DeleteVoiceTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.delete_voice_template_response.DeleteVoiceTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.delete_voice_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.delete_voice_template.async_delete_voice_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.delete_voice_template_request.DeleteVoiceTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_adm_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_adm_channel_response.GetAdmChannelResponse":
        """<p>Retrieves information about the status and settings of the ADM channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_adm_channel_request.GetAdmChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_adm_channel_response.GetAdmChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_adm_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_adm_channel.async_get_adm_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_adm_channel_request.GetAdmChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_apns_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_apns_channel_response.GetApnsChannelResponse":
        """<p>Retrieves information about the status and settings of the APNs channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_apns_channel_request.GetApnsChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_apns_channel_response.GetApnsChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_apns_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_apns_channel.async_get_apns_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_apns_channel_request.GetApnsChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_apns_sandbox_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_apns_sandbox_channel_response.GetApnsSandboxChannelResponse":
        """<p>Retrieves information about the status and settings of the APNs sandbox channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_apns_sandbox_channel_request.GetApnsSandboxChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_apns_sandbox_channel_response.GetApnsSandboxChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_apns_sandbox_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_apns_sandbox_channel.async_get_apns_sandbox_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_apns_sandbox_channel_request.GetApnsSandboxChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_apns_voip_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_apns_voip_channel_response.GetApnsVoipChannelResponse":
        """<p>Retrieves information about the status and settings of the APNs VoIP channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_apns_voip_channel_request.GetApnsVoipChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_apns_voip_channel_response.GetApnsVoipChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_apns_voip_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_apns_voip_channel.async_get_apns_voip_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_apns_voip_channel_request.GetApnsVoipChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_apns_voip_sandbox_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_apns_voip_sandbox_channel_response.GetApnsVoipSandboxChannelResponse":
        """<p>Retrieves information about the status and settings of the APNs VoIP sandbox channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_apns_voip_sandbox_channel_request.GetApnsVoipSandboxChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_apns_voip_sandbox_channel_response.GetApnsVoipSandboxChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_apns_voip_sandbox_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_apns_voip_sandbox_channel.async_get_apns_voip_sandbox_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_apns_voip_sandbox_channel_request.GetApnsVoipSandboxChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_app(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_app_response.GetAppResponse":
        """<p>Retrieves information about an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_app_request.GetAppRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_app_response.GetAppResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_app

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_app.async_get_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_app_request.GetAppRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_application_date_range_kpi(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        kpi_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        end_time: Optional[
            "aws_sdk_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
        next_token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        start_time: Optional[
            "aws_sdk_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
    ) -> "aws_sdk_pinpoint.types.get_application_date_range_kpi_response.GetApplicationDateRangeKpiResponse":
        r"""<p>Retrieves (queries) pre-aggregated data for a standard metric that applies to an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            end_time: <p>The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.</p>
            kpi_name: <p>The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the <a href=\"https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\">Amazon Pinpoint Developer Guide</a>.</p>
            next_token: <p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            start_time: <p>The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_application_date_range_kpi_request.GetApplicationDateRangeKpiRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_application_date_range_kpi_response.GetApplicationDateRangeKpiResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_application_date_range_kpi

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_application_date_range_kpi.async_get_application_date_range_kpi(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_application_date_range_kpi_request.GetApplicationDateRangeKpiRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if end_time is not None:
            input_["end_time"] = end_time
        input_["kpi_name"] = kpi_name
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        if start_time is not None:
            input_["start_time"] = start_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_application_settings(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_application_settings_response.GetApplicationSettingsResponse":
        """<p>Retrieves information about the settings for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_application_settings_request.GetApplicationSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_application_settings_response.GetApplicationSettingsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_application_settings

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_application_settings.async_get_application_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_application_settings_request.GetApplicationSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_apps(
        self,
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_apps_response.GetAppsResponse":
        """<p>Retrieves information about all the applications that are associated with your Amazon Pinpoint account.</p>

        Args:
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_apps_request.GetAppsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_apps_response.GetAppsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_apps

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_apps.async_get_apps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_apps_request.GetAppsRequest = {}  # type: ignore[typeddict-item]
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_baidu_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_baidu_channel_response.GetBaiduChannelResponse":
        """<p>Retrieves information about the status and settings of the Baidu channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_baidu_channel_request.GetBaiduChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_baidu_channel_response.GetBaiduChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_baidu_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_baidu_channel.async_get_baidu_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_baidu_channel_request.GetBaiduChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_campaign(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        campaign_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_campaign_response.GetCampaignResponse":
        """<p>Retrieves information about the status, configuration, and other settings for a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_campaign_request.GetCampaignRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_campaign_response.GetCampaignResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_campaign

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_campaign.async_get_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_campaign_request.GetCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["campaign_id"] = campaign_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_campaign_activities(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        campaign_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_campaign_activities_response.GetCampaignActivitiesResponse":
        """<p>Retrieves information about all the activities for a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_campaign_activities_request.GetCampaignActivitiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_campaign_activities_response.GetCampaignActivitiesResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_campaign_activities

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_campaign_activities.async_get_campaign_activities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_campaign_activities_request.GetCampaignActivitiesRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["campaign_id"] = campaign_id
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_campaign_date_range_kpi(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        campaign_id: "aws_sdk_pinpoint.types.__string.__string",
        kpi_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        end_time: Optional[
            "aws_sdk_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
        next_token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        start_time: Optional[
            "aws_sdk_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
    ) -> "aws_sdk_pinpoint.types.get_campaign_date_range_kpi_response.GetCampaignDateRangeKpiResponse":
        r"""<p>Retrieves (queries) pre-aggregated data for a standard metric that applies to a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
            end_time: <p>The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.</p>
            kpi_name: <p>The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the <a href=\"https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\">Amazon Pinpoint Developer Guide</a>.</p>
            next_token: <p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            start_time: <p>The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_campaign_date_range_kpi_request.GetCampaignDateRangeKpiRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_campaign_date_range_kpi_response.GetCampaignDateRangeKpiResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_campaign_date_range_kpi

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_campaign_date_range_kpi.async_get_campaign_date_range_kpi(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_campaign_date_range_kpi_request.GetCampaignDateRangeKpiRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["campaign_id"] = campaign_id
        if end_time is not None:
            input_["end_time"] = end_time
        input_["kpi_name"] = kpi_name
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        if start_time is not None:
            input_["start_time"] = start_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_campaigns(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_campaigns_response.GetCampaignsResponse":
        """<p>Retrieves information about the status, configuration, and other settings for all the campaigns that are associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_campaigns_request.GetCampaignsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_campaigns_response.GetCampaignsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_campaigns

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_campaigns.async_get_campaigns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_campaigns_request.GetCampaignsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_campaign_version(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        campaign_id: "aws_sdk_pinpoint.types.__string.__string",
        version: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_campaign_version_response.GetCampaignVersionResponse":
        """<p>Retrieves information about the status, configuration, and other settings for a specific version of a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
            version: <p>The unique version number (Version property) for the campaign version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_campaign_version_request.GetCampaignVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_campaign_version_response.GetCampaignVersionResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_campaign_version

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_campaign_version.async_get_campaign_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_campaign_version_request.GetCampaignVersionRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["campaign_id"] = campaign_id
        input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_campaign_versions(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        campaign_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_campaign_versions_response.GetCampaignVersionsResponse":
        """<p>Retrieves information about the status, configuration, and other settings for all versions of a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_campaign_versions_request.GetCampaignVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_campaign_versions_response.GetCampaignVersionsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_campaign_versions

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_campaign_versions.async_get_campaign_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_campaign_versions_request.GetCampaignVersionsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["campaign_id"] = campaign_id
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_channels(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_channels_response.GetChannelsResponse":
        """<p>Retrieves information about the history and status of each channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_channels_request.GetChannelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_channels_response.GetChannelsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_channels

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_channels.async_get_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_channels_request.GetChannelsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_email_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_email_channel_response.GetEmailChannelResponse":
        """<p>Retrieves information about the status and settings of the email channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_email_channel_request.GetEmailChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_email_channel_response.GetEmailChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_email_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_email_channel.async_get_email_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_email_channel_request.GetEmailChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_email_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_email_template_response.GetEmailTemplateResponse":
        r"""<p>Retrieves the content and settings of a message template for messages that are sent through the email channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_email_template_request.GetEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_email_template_response.GetEmailTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_email_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_email_template.async_get_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_email_template_request.GetEmailTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_endpoint(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        endpoint_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_endpoint_response.GetEndpointResponse":
        """<p>Retrieves information about the settings and attributes of a specific endpoint for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            endpoint_id: <p>The case insensitive unique identifier for the endpoint. The identifier can't contain <code>$</code>, <code>{</code> or <code>}</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_endpoint_request.GetEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_endpoint_response.GetEndpointResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_endpoint.async_get_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_endpoint_request.GetEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["endpoint_id"] = endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_event_stream(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_event_stream_response.GetEventStreamResponse":
        """<p>Retrieves information about the event stream settings for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_event_stream_request.GetEventStreamRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_event_stream_response.GetEventStreamResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_event_stream

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_event_stream.async_get_event_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_event_stream_request.GetEventStreamRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_export_job(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        job_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_export_job_response.GetExportJobResponse":
        """<p>Retrieves information about the status and settings of a specific export job for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            job_id: <p>The unique identifier for the job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_export_job_request.GetExportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_export_job_response.GetExportJobResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_export_job

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_export_job.async_get_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_export_job_request.GetExportJobRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_export_jobs(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_export_jobs_response.GetExportJobsResponse":
        """<p>Retrieves information about the status and settings of all the export jobs for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_export_jobs_request.GetExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_export_jobs_response.GetExportJobsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_export_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_export_jobs.async_get_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_export_jobs_request.GetExportJobsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_gcm_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_gcm_channel_response.GetGcmChannelResponse":
        """<p>Retrieves information about the status and settings of the GCM channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_gcm_channel_request.GetGcmChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_gcm_channel_response.GetGcmChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_gcm_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_gcm_channel.async_get_gcm_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_gcm_channel_request.GetGcmChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_import_job(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        job_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_import_job_response.GetImportJobResponse":
        """<p>Retrieves information about the status and settings of a specific import job for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            job_id: <p>The unique identifier for the job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_import_job_request.GetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_import_job_response.GetImportJobResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_import_job.async_get_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_import_job_request.GetImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_import_jobs(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_import_jobs_response.GetImportJobsResponse":
        """<p>Retrieves information about the status and settings of all the import jobs for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_import_jobs_request.GetImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_import_jobs_response.GetImportJobsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_import_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_import_jobs.async_get_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_import_jobs_request.GetImportJobsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_in_app_messages(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        endpoint_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_in_app_messages_response.GetInAppMessagesResponse":
        """<p>Retrieves the in-app messages targeted for the provided endpoint ID.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            endpoint_id: <p>The unique identifier for the endpoint.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_in_app_messages_request.GetInAppMessagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_in_app_messages_response.GetInAppMessagesResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_in_app_messages

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_in_app_messages.async_get_in_app_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_in_app_messages_request.GetInAppMessagesRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["endpoint_id"] = endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_in_app_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_in_app_template_response.GetInAppTemplateResponse":
        r"""<p>Retrieves the content and settings of a message template for messages sent through the in-app channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_in_app_template_request.GetInAppTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_in_app_template_response.GetInAppTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_in_app_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_in_app_template.async_get_in_app_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_in_app_template_request.GetInAppTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_journey(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_journey_response.GetJourneyResponse":
        """<p>Retrieves information about the status, configuration, and other settings for a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_journey_request.GetJourneyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_journey_response.GetJourneyResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_journey

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_journey.async_get_journey(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_journey_request.GetJourneyRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["journey_id"] = journey_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_journey_date_range_kpi(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_id: "aws_sdk_pinpoint.types.__string.__string",
        kpi_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        end_time: Optional[
            "aws_sdk_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
        next_token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        start_time: Optional[
            "aws_sdk_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
        ] = None,
    ) -> "aws_sdk_pinpoint.types.get_journey_date_range_kpi_response.GetJourneyDateRangeKpiResponse":
        r"""<p>Retrieves (queries) pre-aggregated data for a standard engagement metric that applies to a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            end_time: <p>The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            kpi_name: <p>The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the <a href=\"https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\">Amazon Pinpoint Developer Guide</a>.</p>
            next_token: <p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            start_time: <p>The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_journey_date_range_kpi_request.GetJourneyDateRangeKpiRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_journey_date_range_kpi_response.GetJourneyDateRangeKpiResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_journey_date_range_kpi

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_journey_date_range_kpi.async_get_journey_date_range_kpi(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_journey_date_range_kpi_request.GetJourneyDateRangeKpiRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if end_time is not None:
            input_["end_time"] = end_time
        input_["journey_id"] = journey_id
        input_["kpi_name"] = kpi_name
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        if start_time is not None:
            input_["start_time"] = start_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_journey_execution_activity_metrics(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_activity_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        next_token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_journey_execution_activity_metrics_response.GetJourneyExecutionActivityMetricsResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey activity.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_activity_id: <p>The unique identifier for the journey activity.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            next_token: <p>The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_journey_execution_activity_metrics_request.GetJourneyExecutionActivityMetricsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_journey_execution_activity_metrics_response.GetJourneyExecutionActivityMetricsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_journey_execution_activity_metrics

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_journey_execution_activity_metrics.async_get_journey_execution_activity_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_journey_execution_activity_metrics_request.GetJourneyExecutionActivityMetricsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["journey_activity_id"] = journey_activity_id
        input_["journey_id"] = journey_id
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_journey_execution_metrics(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        next_token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_journey_execution_metrics_response.GetJourneyExecutionMetricsResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            next_token: <p>The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_journey_execution_metrics_request.GetJourneyExecutionMetricsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_journey_execution_metrics_response.GetJourneyExecutionMetricsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_journey_execution_metrics

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_journey_execution_metrics.async_get_journey_execution_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_journey_execution_metrics_request.GetJourneyExecutionMetricsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["journey_id"] = journey_id
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_journey_run_execution_activity_metrics(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_activity_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_id: "aws_sdk_pinpoint.types.__string.__string",
        run_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        next_token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_journey_run_execution_activity_metrics_response.GetJourneyRunExecutionActivityMetricsResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard run execution metric that applies to a journey activity.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_activity_id: <p>The unique identifier for the journey activity.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            next_token: <p>The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            run_id: <p>The unique identifier for the journey run.</p>

        Examples:
            To get the activity execution metrics for a journey run
            The following example gets activity execution metrics for a single run of a journey.

            >>> await client.get_journey_run_execution_activity_metrics(application_id='11111111112222222222333333333344', journey_id='aaaaaaaaaabbbbbbbbbbccccccccccdd', run_id='99999999998888888888777777777766', journey_activity_id='AAAAAAAAAA')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_journey_run_execution_activity_metrics_request.GetJourneyRunExecutionActivityMetricsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_journey_run_execution_activity_metrics_response.GetJourneyRunExecutionActivityMetricsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_journey_run_execution_activity_metrics

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_journey_run_execution_activity_metrics.async_get_journey_run_execution_activity_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_journey_run_execution_activity_metrics_request.GetJourneyRunExecutionActivityMetricsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["journey_activity_id"] = journey_activity_id
        input_["journey_id"] = journey_id
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_journey_run_execution_metrics(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_id: "aws_sdk_pinpoint.types.__string.__string",
        run_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        next_token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_journey_run_execution_metrics_response.GetJourneyRunExecutionMetricsResponse":
        """<p>Retrieves (queries) pre-aggregated data for a standard run execution metric that applies to a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            next_token: <p>The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            run_id: <p>The unique identifier for the journey run.</p>

        Examples:
            To get the execution metrics for a journey run
            The following example gets execution metrics for a single run of a journey.

            >>> await client.get_journey_run_execution_metrics(application_id='11111111112222222222333333333344', journey_id='aaaaaaaaaabbbbbbbbbbccccccccccdd', run_id='99999999998888888888777777777766')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_journey_run_execution_metrics_request.GetJourneyRunExecutionMetricsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_journey_run_execution_metrics_response.GetJourneyRunExecutionMetricsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_journey_run_execution_metrics

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_journey_run_execution_metrics.async_get_journey_run_execution_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_journey_run_execution_metrics_request.GetJourneyRunExecutionMetricsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["journey_id"] = journey_id
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_journey_runs(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_journey_runs_response.GetJourneyRunsResponse":
        """<p>Provides information about the runs of a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>

        Examples:
            To get the runs of a journey
            The following example gets the runs of a journey.

            >>> await client.get_journey_runs(application_id='11111111112222222222333333333344', journey_id='aaaaaaaaaabbbbbbbbbbccccccccccdd')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_journey_runs_request.GetJourneyRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_journey_runs_response.GetJourneyRunsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_journey_runs

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_journey_runs.async_get_journey_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_journey_runs_request.GetJourneyRunsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["journey_id"] = journey_id
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_push_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_push_template_response.GetPushTemplateResponse":
        r"""<p>Retrieves the content and settings of a message template for messages that are sent through a push notification channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_push_template_request.GetPushTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_push_template_response.GetPushTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_push_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_push_template.async_get_push_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_push_template_request.GetPushTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_recommender_configuration(
        self,
        recommender_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_recommender_configuration_response.GetRecommenderConfigurationResponse":
        """<p>Retrieves information about an Amazon Pinpoint configuration for a recommender model.</p>

        Args:
            recommender_id: <p>The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_recommender_configuration_request.GetRecommenderConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_recommender_configuration_response.GetRecommenderConfigurationResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_recommender_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_recommender_configuration.async_get_recommender_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_recommender_configuration_request.GetRecommenderConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["recommender_id"] = recommender_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_recommender_configurations(
        self,
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_recommender_configurations_response.GetRecommenderConfigurationsResponse":
        """<p>Retrieves information about all the recommender model configurations that are associated with your Amazon Pinpoint account.</p>

        Args:
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_recommender_configurations_request.GetRecommenderConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_recommender_configurations_response.GetRecommenderConfigurationsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_recommender_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_recommender_configurations.async_get_recommender_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_recommender_configurations_request.GetRecommenderConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_segment(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        segment_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_segment_response.GetSegmentResponse":
        """<p>Retrieves information about the configuration, dimension, and other settings for a specific segment that's associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            segment_id: <p>The unique identifier for the segment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_segment_request.GetSegmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_segment_response.GetSegmentResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_segment

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_segment.async_get_segment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_segment_request.GetSegmentRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["segment_id"] = segment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_segment_export_jobs(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        segment_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_segment_export_jobs_response.GetSegmentExportJobsResponse":
        """<p>Retrieves information about the status and settings of the export jobs for a segment.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            segment_id: <p>The unique identifier for the segment.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_segment_export_jobs_request.GetSegmentExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_segment_export_jobs_response.GetSegmentExportJobsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_segment_export_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_segment_export_jobs.async_get_segment_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_segment_export_jobs_request.GetSegmentExportJobsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if page_size is not None:
            input_["page_size"] = page_size
        input_["segment_id"] = segment_id
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_segment_import_jobs(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        segment_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_segment_import_jobs_response.GetSegmentImportJobsResponse":
        """<p>Retrieves information about the status and settings of the import jobs for a segment.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            segment_id: <p>The unique identifier for the segment.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_segment_import_jobs_request.GetSegmentImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_segment_import_jobs_response.GetSegmentImportJobsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_segment_import_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_segment_import_jobs.async_get_segment_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_segment_import_jobs_request.GetSegmentImportJobsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if page_size is not None:
            input_["page_size"] = page_size
        input_["segment_id"] = segment_id
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_segments(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_segments_response.GetSegmentsResponse":
        """<p>Retrieves information about the configuration, dimension, and other settings for all the segments that are associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_segments_request.GetSegmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_segments_response.GetSegmentsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_segments

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_segments.async_get_segments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_segments_request.GetSegmentsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_segment_version(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        segment_id: "aws_sdk_pinpoint.types.__string.__string",
        version: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> (
        "aws_sdk_pinpoint.types.get_segment_version_response.GetSegmentVersionResponse"
    ):
        """<p>Retrieves information about the configuration, dimension, and other settings for a specific version of a segment that's associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            segment_id: <p>The unique identifier for the segment.</p>
            version: <p>The unique version number (Version property) for the campaign version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_segment_version_request.GetSegmentVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_segment_version_response.GetSegmentVersionResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_segment_version

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_segment_version.async_get_segment_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_segment_version_request.GetSegmentVersionRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["segment_id"] = segment_id
        input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_segment_versions(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        segment_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_segment_versions_response.GetSegmentVersionsResponse":
        """<p>Retrieves information about the configuration, dimension, and other settings for all the versions of a specific segment that's associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            segment_id: <p>The unique identifier for the segment.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_segment_versions_request.GetSegmentVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_segment_versions_response.GetSegmentVersionsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_segment_versions

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_segment_versions.async_get_segment_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_segment_versions_request.GetSegmentVersionsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if page_size is not None:
            input_["page_size"] = page_size
        input_["segment_id"] = segment_id
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_sms_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_sms_channel_response.GetSmsChannelResponse":
        """<p>Retrieves information about the status and settings of the SMS channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_sms_channel_request.GetSmsChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_sms_channel_response.GetSmsChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_sms_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_sms_channel.async_get_sms_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_sms_channel_request.GetSmsChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_sms_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_sms_template_response.GetSmsTemplateResponse":
        r"""<p>Retrieves the content and settings of a message template for messages that are sent through the SMS channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_sms_template_request.GetSmsTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_sms_template_response.GetSmsTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_sms_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_sms_template.async_get_sms_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_sms_template_request.GetSmsTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_user_endpoints(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        user_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_user_endpoints_response.GetUserEndpointsResponse":
        """<p>Retrieves information about all the endpoints that are associated with a specific user ID.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            user_id: <p>The unique identifier for the user.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_user_endpoints_request.GetUserEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_user_endpoints_response.GetUserEndpointsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_user_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_user_endpoints.async_get_user_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_user_endpoints_request.GetUserEndpointsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_voice_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.get_voice_channel_response.GetVoiceChannelResponse":
        """<p>Retrieves information about the status and settings of the voice channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_voice_channel_request.GetVoiceChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_voice_channel_response.GetVoiceChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_voice_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_voice_channel.async_get_voice_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_voice_channel_request.GetVoiceChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_voice_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.get_voice_template_response.GetVoiceTemplateResponse":
        r"""<p>Retrieves the content and settings of a message template for messages that are sent through the voice channel.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.get_voice_template_request.GetVoiceTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.get_voice_template_response.GetVoiceTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.get_voice_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.get_voice_template.async_get_voice_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.get_voice_template_request.GetVoiceTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_journeys(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.list_journeys_response.ListJourneysResponse":
        """<p>Retrieves information about the status, configuration, and other settings for all the journeys that are associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            token: <p>The NextToken string that specifies which page of results to return in a paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.list_journeys_request.ListJourneysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.list_journeys_response.ListJourneysResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.list_journeys

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.list_journeys.async_list_journeys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.list_journeys_request.ListJourneysRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if page_size is not None:
            input_["page_size"] = page_size
        if token is not None:
            input_["token"] = token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves all the tags (keys and values) that are associated with an application, campaign, message template, or segment.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_templates(
        self,
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        next_token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        prefix: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        template_type: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.list_templates_response.ListTemplatesResponse":
        """<p>Retrieves information about all the message templates that are associated with your Amazon Pinpoint account.</p>

        Args:
            next_token: <p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            prefix: <p>The substring to match in the names of the message templates to include in the results. If you specify this value, Amazon Pinpoint returns only those templates whose names begin with the value that you specify.</p>
            template_type: <p>The type of message template to include in the results. Valid values are: EMAIL, PUSH, SMS, and VOICE. To include all types of templates in the results, don't include this parameter in your request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.list_templates_request.ListTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.list_templates_response.ListTemplatesResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.list_templates

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.list_templates.async_list_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.list_templates_request.ListTemplatesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        if prefix is not None:
            input_["prefix"] = prefix
        if template_type is not None:
            input_["template_type"] = template_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_template_versions(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        template_type: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        next_token: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
        page_size: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.list_template_versions_response.ListTemplateVersionsResponse":
        """<p>Retrieves information about all the versions of a specific message template.</p>

        Args:
            next_token: <p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            page_size: <p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            template_type: <p>The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.list_template_versions_request.ListTemplateVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.list_template_versions_response.ListTemplateVersionsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.list_template_versions

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.list_template_versions.async_list_template_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.list_template_versions_request.ListTemplateVersionsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size
        input_["template_name"] = template_name
        input_["template_type"] = template_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def phone_number_validate(
        self,
        number_validate_request: "aws_sdk_pinpoint.types.number_validate_request.NumberValidateRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.phone_number_validate_response.PhoneNumberValidateResponse":
        """<p>Retrieves information about a phone number.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.phone_number_validate_request.PhoneNumberValidateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.phone_number_validate_response.PhoneNumberValidateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.phone_number_validate

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.phone_number_validate.async_phone_number_validate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.phone_number_validate_request.PhoneNumberValidateRequest = {}  # type: ignore[typeddict-item]
        input_["number_validate_request"] = number_validate_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_events(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        events_request: "aws_sdk_pinpoint.types.events_request.EventsRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.put_events_response.PutEventsResponse":
        """<p>Creates a new event to record for endpoints, or creates or updates endpoint data that existing events are associated with.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.put_events_request.PutEventsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.put_events_response.PutEventsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.put_events

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.put_events.async_put_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.put_events_request.PutEventsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["events_request"] = events_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_event_stream(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        write_event_stream: "aws_sdk_pinpoint.types.write_event_stream.WriteEventStream",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.put_event_stream_response.PutEventStreamResponse":
        """<p>Creates a new event stream for an application or updates the settings of an existing event stream for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.put_event_stream_request.PutEventStreamRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.put_event_stream_response.PutEventStreamResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.put_event_stream

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.put_event_stream.async_put_event_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.put_event_stream_request.PutEventStreamRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["write_event_stream"] = write_event_stream

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_attributes(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        attribute_type: "aws_sdk_pinpoint.types.__string.__string",
        update_attributes_request: "aws_sdk_pinpoint.types.update_attributes_request.UpdateAttributesRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.remove_attributes_response.RemoveAttributesResponse":
        """<p>Removes one or more custom attributes, of the same attribute type, from the application. Existing endpoints still have the attributes but Amazon Pinpoint will stop capturing new or changed values for these attributes.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            attribute_type: <p>The type of attribute or attributes to remove. Valid values are:</p> <ul><li><p>endpoint-custom-attributes - Custom attributes that describe endpoints, such as the date when an associated user opted in or out of receiving communications from you through a specific type of channel.</p></li> <li><p>endpoint-metric-attributes - Custom metrics that your app reports to Amazon Pinpoint for endpoints, such as the number of app sessions or the number of items left in a cart.</p></li> <li><p>endpoint-user-attributes - Custom attributes that describe users, such as first name, last name, and age.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.remove_attributes_request.RemoveAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.remove_attributes_response.RemoveAttributesResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.remove_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.remove_attributes.async_remove_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.remove_attributes_request.RemoveAttributesRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["attribute_type"] = attribute_type
        input_["update_attributes_request"] = update_attributes_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_messages(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        message_request: "aws_sdk_pinpoint.types.message_request.MessageRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.send_messages_response.SendMessagesResponse":
        """<p>Creates and sends a direct message.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.send_messages_request.SendMessagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.send_messages_response.SendMessagesResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.send_messages

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.send_messages.async_send_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.send_messages_request.SendMessagesRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["message_request"] = message_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_otp_message(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        send_otp_message_request_parameters: "aws_sdk_pinpoint.types.send_otp_message_request_parameters.SendOTPMessageRequestParameters",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.send_otp_message_response.SendOTPMessageResponse":
        """<p>Send an OTP message</p>

        Args:
            application_id: <p>The unique ID of your Amazon Pinpoint application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.send_otp_message_request.SendOTPMessageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.send_otp_message_response.SendOTPMessageResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.send_otp_message

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.send_otp_message.async_send_otp_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.send_otp_message_request.SendOTPMessageRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["send_otp_message_request_parameters"] = (
            send_otp_message_request_parameters
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_users_messages(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        send_users_message_request: "aws_sdk_pinpoint.types.send_users_message_request.SendUsersMessageRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> (
        "aws_sdk_pinpoint.types.send_users_messages_response.SendUsersMessagesResponse"
    ):
        """<p>Creates and sends a message to a list of users.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.send_users_messages_request.SendUsersMessagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.send_users_messages_response.SendUsersMessagesResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.send_users_messages

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.send_users_messages.async_send_users_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.send_users_messages_request.SendUsersMessagesRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["send_users_message_request"] = send_users_message_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_pinpoint.types.__string.__string",
        tags_model: "aws_sdk_pinpoint.types.tags_model.TagsModel",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> None:
        """<p>Adds one or more tags (keys and values) to an application, campaign, message template, or segment.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_pinpoint._operations.pinpoint.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags_model"] = tags_model

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_pinpoint.types.__string.__string",
        tag_keys: "aws_sdk_pinpoint.types.list_of__string.ListOf__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> None:
        """<p>Removes one or more tags (keys and values) from an application, campaign, message template, or segment.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The key of the tag to remove from the resource. To remove multiple tags, append the tagKeys parameter and argument for each additional tag to remove, separated by an ampersand (&amp;).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_pinpoint._operations.pinpoint.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_adm_channel(
        self,
        adm_channel_request: "aws_sdk_pinpoint.types.adm_channel_request.ADMChannelRequest",
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_adm_channel_response.UpdateAdmChannelResponse":
        """<p>Enables the ADM channel for an application or updates the status and settings of the ADM channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_adm_channel_request.UpdateAdmChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_adm_channel_response.UpdateAdmChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_adm_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_adm_channel.async_update_adm_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_adm_channel_request.UpdateAdmChannelRequest = {}  # type: ignore[typeddict-item]
        input_["adm_channel_request"] = adm_channel_request
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_apns_channel(
        self,
        apns_channel_request: "aws_sdk_pinpoint.types.apns_channel_request.APNSChannelRequest",
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> (
        "aws_sdk_pinpoint.types.update_apns_channel_response.UpdateApnsChannelResponse"
    ):
        """<p>Enables the APNs channel for an application or updates the status and settings of the APNs channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_apns_channel_request.UpdateApnsChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_apns_channel_response.UpdateApnsChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_apns_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_apns_channel.async_update_apns_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_apns_channel_request.UpdateApnsChannelRequest = {}  # type: ignore[typeddict-item]
        input_["apns_channel_request"] = apns_channel_request
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_apns_sandbox_channel(
        self,
        apns_sandbox_channel_request: "aws_sdk_pinpoint.types.apns_sandbox_channel_request.APNSSandboxChannelRequest",
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_apns_sandbox_channel_response.UpdateApnsSandboxChannelResponse":
        """<p>Enables the APNs sandbox channel for an application or updates the status and settings of the APNs sandbox channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_apns_sandbox_channel_request.UpdateApnsSandboxChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_apns_sandbox_channel_response.UpdateApnsSandboxChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_apns_sandbox_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_apns_sandbox_channel.async_update_apns_sandbox_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_apns_sandbox_channel_request.UpdateApnsSandboxChannelRequest = {}  # type: ignore[typeddict-item]
        input_["apns_sandbox_channel_request"] = apns_sandbox_channel_request
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_apns_voip_channel(
        self,
        apns_voip_channel_request: "aws_sdk_pinpoint.types.apns_voip_channel_request.APNSVoipChannelRequest",
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_apns_voip_channel_response.UpdateApnsVoipChannelResponse":
        """<p>Enables the APNs VoIP channel for an application or updates the status and settings of the APNs VoIP channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_apns_voip_channel_request.UpdateApnsVoipChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_apns_voip_channel_response.UpdateApnsVoipChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_apns_voip_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_apns_voip_channel.async_update_apns_voip_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_apns_voip_channel_request.UpdateApnsVoipChannelRequest = {}  # type: ignore[typeddict-item]
        input_["apns_voip_channel_request"] = apns_voip_channel_request
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_apns_voip_sandbox_channel(
        self,
        apns_voip_sandbox_channel_request: "aws_sdk_pinpoint.types.apns_voip_sandbox_channel_request.APNSVoipSandboxChannelRequest",
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_apns_voip_sandbox_channel_response.UpdateApnsVoipSandboxChannelResponse":
        """<p>Enables the APNs VoIP sandbox channel for an application or updates the status and settings of the APNs VoIP sandbox channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_apns_voip_sandbox_channel_request.UpdateApnsVoipSandboxChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_apns_voip_sandbox_channel_response.UpdateApnsVoipSandboxChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_apns_voip_sandbox_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_apns_voip_sandbox_channel.async_update_apns_voip_sandbox_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_apns_voip_sandbox_channel_request.UpdateApnsVoipSandboxChannelRequest = {}  # type: ignore[typeddict-item]
        input_["apns_voip_sandbox_channel_request"] = apns_voip_sandbox_channel_request
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_application_settings(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        write_application_settings_request: "aws_sdk_pinpoint.types.write_application_settings_request.WriteApplicationSettingsRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_application_settings_response.UpdateApplicationSettingsResponse":
        """<p>Updates the settings for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_application_settings_request.UpdateApplicationSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_application_settings_response.UpdateApplicationSettingsResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_application_settings

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_application_settings.async_update_application_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_application_settings_request.UpdateApplicationSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["write_application_settings_request"] = (
            write_application_settings_request
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_baidu_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        baidu_channel_request: "aws_sdk_pinpoint.types.baidu_channel_request.BaiduChannelRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_baidu_channel_response.UpdateBaiduChannelResponse":
        """<p>Enables the Baidu channel for an application or updates the status and settings of the Baidu channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_baidu_channel_request.UpdateBaiduChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_baidu_channel_response.UpdateBaiduChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_baidu_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_baidu_channel.async_update_baidu_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_baidu_channel_request.UpdateBaiduChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["baidu_channel_request"] = baidu_channel_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_campaign(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        campaign_id: "aws_sdk_pinpoint.types.__string.__string",
        write_campaign_request: "aws_sdk_pinpoint.types.write_campaign_request.WriteCampaignRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_campaign_response.UpdateCampaignResponse":
        """<p>Updates the configuration and other settings for a campaign.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            campaign_id: <p>The unique identifier for the campaign.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_campaign_request.UpdateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_campaign_response.UpdateCampaignResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_campaign

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_campaign.async_update_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_campaign_request.UpdateCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["campaign_id"] = campaign_id
        input_["write_campaign_request"] = write_campaign_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_email_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        email_channel_request: "aws_sdk_pinpoint.types.email_channel_request.EmailChannelRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_email_channel_response.UpdateEmailChannelResponse":
        """<p>Enables the email channel for an application or updates the status and settings of the email channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_email_channel_request.UpdateEmailChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_email_channel_response.UpdateEmailChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_email_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_email_channel.async_update_email_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_email_channel_request.UpdateEmailChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["email_channel_request"] = email_channel_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_email_template(
        self,
        email_template_request: "aws_sdk_pinpoint.types.email_template_request.EmailTemplateRequest",
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        create_new_version: Optional[
            "aws_sdk_pinpoint.types.__boolean.__boolean"
        ] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.update_email_template_response.UpdateEmailTemplateResponse":
        r"""<p>Updates an existing message template for messages that are sent through the email channel.</p>

        Args:
            create_new_version: <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_email_template_request.UpdateEmailTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_email_template_response.UpdateEmailTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_email_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_email_template.async_update_email_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_email_template_request.UpdateEmailTemplateRequest = {}  # type: ignore[typeddict-item]
        if create_new_version is not None:
            input_["create_new_version"] = create_new_version
        input_["email_template_request"] = email_template_request
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_endpoint(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        endpoint_id: "aws_sdk_pinpoint.types.__string.__string",
        endpoint_request: "aws_sdk_pinpoint.types.endpoint_request.EndpointRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_endpoint_response.UpdateEndpointResponse":
        """<p>Creates a new endpoint for an application or updates the settings and attributes of an existing endpoint for an application. You can also use this operation to define custom attributes for an endpoint. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            endpoint_id: <p>The case insensitive unique identifier for the endpoint. The identifier can't contain <code>$</code>, <code>{</code> or <code>}</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_endpoint_request.UpdateEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_endpoint_response.UpdateEndpointResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_endpoint.async_update_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_endpoint_request.UpdateEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["endpoint_id"] = endpoint_id
        input_["endpoint_request"] = endpoint_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_endpoints_batch(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        endpoint_batch_request: "aws_sdk_pinpoint.types.endpoint_batch_request.EndpointBatchRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_endpoints_batch_response.UpdateEndpointsBatchResponse":
        """<p>Creates a new batch of endpoints for an application or updates the settings and attributes of a batch of existing endpoints for an application. You can also use this operation to define custom attributes for a batch of endpoints. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_endpoints_batch_request.UpdateEndpointsBatchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_endpoints_batch_response.UpdateEndpointsBatchResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_endpoints_batch

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_endpoints_batch.async_update_endpoints_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_endpoints_batch_request.UpdateEndpointsBatchRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["endpoint_batch_request"] = endpoint_batch_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_gcm_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        gcm_channel_request: "aws_sdk_pinpoint.types.gcm_channel_request.GCMChannelRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_gcm_channel_response.UpdateGcmChannelResponse":
        """<p>Enables the GCM channel for an application or updates the status and settings of the GCM channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_gcm_channel_request.UpdateGcmChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_gcm_channel_response.UpdateGcmChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_gcm_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_gcm_channel.async_update_gcm_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_gcm_channel_request.UpdateGcmChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["gcm_channel_request"] = gcm_channel_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_in_app_template(
        self,
        in_app_template_request: "aws_sdk_pinpoint.types.in_app_template_request.InAppTemplateRequest",
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        create_new_version: Optional[
            "aws_sdk_pinpoint.types.__boolean.__boolean"
        ] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.update_in_app_template_response.UpdateInAppTemplateResponse":
        r"""<p>Updates an existing message template for messages sent through the in-app message channel.</p>

        Args:
            create_new_version: <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_in_app_template_request.UpdateInAppTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_in_app_template_response.UpdateInAppTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_in_app_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_in_app_template.async_update_in_app_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_in_app_template_request.UpdateInAppTemplateRequest = {}  # type: ignore[typeddict-item]
        if create_new_version is not None:
            input_["create_new_version"] = create_new_version
        input_["in_app_template_request"] = in_app_template_request
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_journey(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_id: "aws_sdk_pinpoint.types.__string.__string",
        write_journey_request: "aws_sdk_pinpoint.types.write_journey_request.WriteJourneyRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_journey_response.UpdateJourneyResponse":
        """<p>Updates the configuration and other settings for a journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_journey_request.UpdateJourneyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_journey_response.UpdateJourneyResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_journey

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_journey.async_update_journey(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_journey_request.UpdateJourneyRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["journey_id"] = journey_id
        input_["write_journey_request"] = write_journey_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_journey_state(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_id: "aws_sdk_pinpoint.types.__string.__string",
        journey_state_request: "aws_sdk_pinpoint.types.journey_state_request.JourneyStateRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_journey_state_response.UpdateJourneyStateResponse":
        """<p>Cancels (stops) an active journey.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            journey_id: <p>The unique identifier for the journey.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_journey_state_request.UpdateJourneyStateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_journey_state_response.UpdateJourneyStateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_journey_state

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_journey_state.async_update_journey_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_journey_state_request.UpdateJourneyStateRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["journey_id"] = journey_id
        input_["journey_state_request"] = journey_state_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_push_template(
        self,
        push_notification_template_request: "aws_sdk_pinpoint.types.push_notification_template_request.PushNotificationTemplateRequest",
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        create_new_version: Optional[
            "aws_sdk_pinpoint.types.__boolean.__boolean"
        ] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.update_push_template_response.UpdatePushTemplateResponse":
        r"""<p>Updates an existing message template for messages that are sent through a push notification channel.</p>

        Args:
            create_new_version: <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_push_template_request.UpdatePushTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_push_template_response.UpdatePushTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_push_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_push_template.async_update_push_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_push_template_request.UpdatePushTemplateRequest = {}  # type: ignore[typeddict-item]
        if create_new_version is not None:
            input_["create_new_version"] = create_new_version
        input_["push_notification_template_request"] = (
            push_notification_template_request
        )
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_recommender_configuration(
        self,
        recommender_id: "aws_sdk_pinpoint.types.__string.__string",
        update_recommender_configuration: "aws_sdk_pinpoint.types.update_recommender_configuration_shape.UpdateRecommenderConfigurationShape",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_recommender_configuration_response.UpdateRecommenderConfigurationResponse":
        """<p>Updates an Amazon Pinpoint configuration for a recommender model.</p>

        Args:
            recommender_id: <p>The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_recommender_configuration_request.UpdateRecommenderConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_recommender_configuration_response.UpdateRecommenderConfigurationResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_recommender_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_recommender_configuration.async_update_recommender_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_recommender_configuration_request.UpdateRecommenderConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["recommender_id"] = recommender_id
        input_["update_recommender_configuration"] = update_recommender_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_segment(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        segment_id: "aws_sdk_pinpoint.types.__string.__string",
        write_segment_request: "aws_sdk_pinpoint.types.write_segment_request.WriteSegmentRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_segment_response.UpdateSegmentResponse":
        """<p>Creates a new segment for an application or updates the configuration, dimension, and other settings for an existing segment that's associated with an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
            segment_id: <p>The unique identifier for the segment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_segment_request.UpdateSegmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_segment_response.UpdateSegmentResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_segment

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_segment.async_update_segment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_segment_request.UpdateSegmentRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["segment_id"] = segment_id
        input_["write_segment_request"] = write_segment_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_sms_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        sms_channel_request: "aws_sdk_pinpoint.types.sms_channel_request.SMSChannelRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_sms_channel_response.UpdateSmsChannelResponse":
        """<p>Enables the SMS channel for an application or updates the status and settings of the SMS channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_sms_channel_request.UpdateSmsChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_sms_channel_response.UpdateSmsChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_sms_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_sms_channel.async_update_sms_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_sms_channel_request.UpdateSmsChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["sms_channel_request"] = sms_channel_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_sms_template(
        self,
        sms_template_request: "aws_sdk_pinpoint.types.sms_template_request.SMSTemplateRequest",
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        create_new_version: Optional[
            "aws_sdk_pinpoint.types.__boolean.__boolean"
        ] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> (
        "aws_sdk_pinpoint.types.update_sms_template_response.UpdateSmsTemplateResponse"
    ):
        r"""<p>Updates an existing message template for messages that are sent through the SMS channel.</p>

        Args:
            create_new_version: <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_sms_template_request.UpdateSmsTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_sms_template_response.UpdateSmsTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_sms_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_sms_template.async_update_sms_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_sms_template_request.UpdateSmsTemplateRequest = {}  # type: ignore[typeddict-item]
        if create_new_version is not None:
            input_["create_new_version"] = create_new_version
        input_["sms_template_request"] = sms_template_request
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_template_active_version(
        self,
        template_active_version_request: "aws_sdk_pinpoint.types.template_active_version_request.TemplateActiveVersionRequest",
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        template_type: "aws_sdk_pinpoint.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_template_active_version_response.UpdateTemplateActiveVersionResponse":
        """<p>Changes the status of a specific version of a message template to <i>active</i>.</p>

        Args:
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            template_type: <p>The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_template_active_version_request.UpdateTemplateActiveVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_template_active_version_response.UpdateTemplateActiveVersionResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_template_active_version

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_template_active_version.async_update_template_active_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_template_active_version_request.UpdateTemplateActiveVersionRequest = {}  # type: ignore[typeddict-item]
        input_["template_active_version_request"] = template_active_version_request
        input_["template_name"] = template_name
        input_["template_type"] = template_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_voice_channel(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        voice_channel_request: "aws_sdk_pinpoint.types.voice_channel_request.VoiceChannelRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.update_voice_channel_response.UpdateVoiceChannelResponse":
        """<p>Enables the voice channel for an application or updates the status and settings of the voice channel for an application.</p>

        Args:
            application_id: <p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_voice_channel_request.UpdateVoiceChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_voice_channel_response.UpdateVoiceChannelResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_voice_channel

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_voice_channel.async_update_voice_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_voice_channel_request.UpdateVoiceChannelRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["voice_channel_request"] = voice_channel_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_voice_template(
        self,
        template_name: "aws_sdk_pinpoint.types.__string.__string",
        voice_template_request: "aws_sdk_pinpoint.types.voice_template_request.VoiceTemplateRequest",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
        create_new_version: Optional[
            "aws_sdk_pinpoint.types.__boolean.__boolean"
        ] = None,
        version: Optional["aws_sdk_pinpoint.types.__string.__string"] = None,
    ) -> "aws_sdk_pinpoint.types.update_voice_template_response.UpdateVoiceTemplateResponse":
        r"""<p>Updates an existing message template for messages that are sent through the voice channel.</p>

        Args:
            create_new_version: <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
            template_name: <p>The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.</p>
            version: <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.update_voice_template_request.UpdateVoiceTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.update_voice_template_response.UpdateVoiceTemplateResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.update_voice_template

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.update_voice_template.async_update_voice_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.update_voice_template_request.UpdateVoiceTemplateRequest = {}  # type: ignore[typeddict-item]
        if create_new_version is not None:
            input_["create_new_version"] = create_new_version
        input_["template_name"] = template_name
        if version is not None:
            input_["version"] = version
        input_["voice_template_request"] = voice_template_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def verify_otp_message(
        self,
        application_id: "aws_sdk_pinpoint.types.__string.__string",
        verify_otp_message_request_parameters: "aws_sdk_pinpoint.types.verify_otp_message_request_parameters.VerifyOTPMessageRequestParameters",
        *,
        config_overrides: Optional[AsyncPinpointClientConfig] = None,
    ) -> "aws_sdk_pinpoint.types.verify_otp_message_response.VerifyOTPMessageResponse":
        """<p>Verify an OTP</p>

        Args:
            application_id: <p>The unique ID of your Amazon Pinpoint application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pinpoint.types.verify_otp_message_request.VerifyOTPMessageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pinpoint.types.verify_otp_message_response.VerifyOTPMessageResponse"
        ]:
            import aws_sdk_pinpoint._operations.pinpoint.verify_otp_message

            (
                output,
                http_response,
            ) = await aws_sdk_pinpoint._operations.pinpoint.verify_otp_message.async_verify_otp_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_pinpoint.types.verify_otp_message_request.VerifyOTPMessageRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["verify_otp_message_request_parameters"] = (
            verify_otp_message_request_parameters
        )

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
