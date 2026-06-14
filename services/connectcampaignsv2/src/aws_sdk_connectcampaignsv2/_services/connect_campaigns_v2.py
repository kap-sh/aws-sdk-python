"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#AmazonConnectCampaignServiceV2``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_connectcampaignsv2._auth._signers
import aws_sdk_connectcampaignsv2._auth._sigv4
from aws_sdk_connectcampaignsv2._auth._identity import Credentials
from aws_sdk_connectcampaignsv2._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_connectcampaignsv2._auth._zapros_handler import AuthMiddleware
from aws_sdk_connectcampaignsv2._pagination import resolve_path as _resolve_path
from aws_sdk_connectcampaignsv2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn
    import aws_sdk_connectcampaignsv2.types.campaign_deletion_policy
    import aws_sdk_connectcampaignsv2.types.campaign_filters
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.campaign_id_list
    import aws_sdk_connectcampaignsv2.types.campaign_name
    import aws_sdk_connectcampaignsv2.types.campaign_summary
    import aws_sdk_connectcampaignsv2.types.channel_subtype
    import aws_sdk_connectcampaignsv2.types.channel_subtype_config
    import aws_sdk_connectcampaignsv2.types.communication_limits_config
    import aws_sdk_connectcampaignsv2.types.communication_limits_config_type
    import aws_sdk_connectcampaignsv2.types.communication_time_config
    import aws_sdk_connectcampaignsv2.types.communication_time_config_type
    import aws_sdk_connectcampaignsv2.types.create_campaign_request
    import aws_sdk_connectcampaignsv2.types.create_campaign_response
    import aws_sdk_connectcampaignsv2.types.delete_campaign_channel_subtype_config_request
    import aws_sdk_connectcampaignsv2.types.delete_campaign_communication_limits_request
    import aws_sdk_connectcampaignsv2.types.delete_campaign_communication_time_request
    import aws_sdk_connectcampaignsv2.types.delete_campaign_entry_limits_request
    import aws_sdk_connectcampaignsv2.types.delete_campaign_request
    import aws_sdk_connectcampaignsv2.types.delete_connect_instance_config_request
    import aws_sdk_connectcampaignsv2.types.delete_connect_instance_integration_request
    import aws_sdk_connectcampaignsv2.types.delete_instance_onboarding_job_request
    import aws_sdk_connectcampaignsv2.types.describe_campaign_request
    import aws_sdk_connectcampaignsv2.types.describe_campaign_response
    import aws_sdk_connectcampaignsv2.types.encryption_config
    import aws_sdk_connectcampaignsv2.types.entry_limits_config
    import aws_sdk_connectcampaignsv2.types.external_campaign_type
    import aws_sdk_connectcampaignsv2.types.get_campaign_state_batch_request
    import aws_sdk_connectcampaignsv2.types.get_campaign_state_batch_response
    import aws_sdk_connectcampaignsv2.types.get_campaign_state_request
    import aws_sdk_connectcampaignsv2.types.get_campaign_state_response
    import aws_sdk_connectcampaignsv2.types.get_connect_instance_config_request
    import aws_sdk_connectcampaignsv2.types.get_connect_instance_config_response
    import aws_sdk_connectcampaignsv2.types.get_instance_communication_limits_request
    import aws_sdk_connectcampaignsv2.types.get_instance_communication_limits_response
    import aws_sdk_connectcampaignsv2.types.get_instance_onboarding_job_status_request
    import aws_sdk_connectcampaignsv2.types.get_instance_onboarding_job_status_response
    import aws_sdk_connectcampaignsv2.types.instance_communication_limits_config
    import aws_sdk_connectcampaignsv2.types.instance_id
    import aws_sdk_connectcampaignsv2.types.integration_config
    import aws_sdk_connectcampaignsv2.types.integration_identifier
    import aws_sdk_connectcampaignsv2.types.integration_summary
    import aws_sdk_connectcampaignsv2.types.list_campaigns_request
    import aws_sdk_connectcampaignsv2.types.list_campaigns_response
    import aws_sdk_connectcampaignsv2.types.list_connect_instance_integrations_request
    import aws_sdk_connectcampaignsv2.types.list_connect_instance_integrations_response
    import aws_sdk_connectcampaignsv2.types.list_tags_for_resource_request
    import aws_sdk_connectcampaignsv2.types.list_tags_for_resource_response
    import aws_sdk_connectcampaignsv2.types.max_results
    import aws_sdk_connectcampaignsv2.types.next_token
    import aws_sdk_connectcampaignsv2.types.outbound_request_list
    import aws_sdk_connectcampaignsv2.types.pause_campaign_request
    import aws_sdk_connectcampaignsv2.types.profile_outbound_request_list
    import aws_sdk_connectcampaignsv2.types.put_connect_instance_integration_request
    import aws_sdk_connectcampaignsv2.types.put_instance_communication_limits_request
    import aws_sdk_connectcampaignsv2.types.put_outbound_request_batch_request
    import aws_sdk_connectcampaignsv2.types.put_outbound_request_batch_response
    import aws_sdk_connectcampaignsv2.types.put_profile_outbound_request_batch_request
    import aws_sdk_connectcampaignsv2.types.put_profile_outbound_request_batch_response
    import aws_sdk_connectcampaignsv2.types.resume_campaign_request
    import aws_sdk_connectcampaignsv2.types.schedule
    import aws_sdk_connectcampaignsv2.types.source
    import aws_sdk_connectcampaignsv2.types.start_campaign_request
    import aws_sdk_connectcampaignsv2.types.start_instance_onboarding_job_request
    import aws_sdk_connectcampaignsv2.types.start_instance_onboarding_job_response
    import aws_sdk_connectcampaignsv2.types.stop_campaign_request
    import aws_sdk_connectcampaignsv2.types.tag_key_list
    import aws_sdk_connectcampaignsv2.types.tag_map
    import aws_sdk_connectcampaignsv2.types.tag_resource_request
    import aws_sdk_connectcampaignsv2.types.untag_resource_request
    import aws_sdk_connectcampaignsv2.types.update_campaign_channel_subtype_config_request
    import aws_sdk_connectcampaignsv2.types.update_campaign_communication_limits_request
    import aws_sdk_connectcampaignsv2.types.update_campaign_communication_time_request
    import aws_sdk_connectcampaignsv2.types.update_campaign_entry_limits_request
    import aws_sdk_connectcampaignsv2.types.update_campaign_flow_association_request
    import aws_sdk_connectcampaignsv2.types.update_campaign_name_request
    import aws_sdk_connectcampaignsv2.types.update_campaign_schedule_request
    import aws_sdk_connectcampaignsv2.types.update_campaign_source_request


class ConnectCampaignsV2ClientConfig(TypedDict, total=False):
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


class ConnectCampaignsV2Client:
    """A client for the ``ConnectCampaignsV2`` service.

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
        self.config = ConnectCampaignsV2ClientConfig(
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
        self, config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ConnectCampaignsV2ClientConfig = config_overrides or {}
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

    def create_campaign(
        self,
        name: "aws_sdk_connectcampaignsv2.types.campaign_name.CampaignName",
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
        channel_subtype_config: Optional[
            "aws_sdk_connectcampaignsv2.types.channel_subtype_config.ChannelSubtypeConfig"
        ] = None,
        type: Optional[
            "aws_sdk_connectcampaignsv2.types.external_campaign_type.ExternalCampaignType"
        ] = None,
        source: Optional["aws_sdk_connectcampaignsv2.types.source.Source"] = None,
        connect_campaign_flow_arn: Optional[
            "aws_sdk_connectcampaignsv2.types.arn.Arn"
        ] = None,
        schedule: Optional["aws_sdk_connectcampaignsv2.types.schedule.Schedule"] = None,
        entry_limits_config: Optional[
            "aws_sdk_connectcampaignsv2.types.entry_limits_config.EntryLimitsConfig"
        ] = None,
        communication_time_config: Optional[
            "aws_sdk_connectcampaignsv2.types.communication_time_config.CommunicationTimeConfig"
        ] = None,
        communication_limits_override: Optional[
            "aws_sdk_connectcampaignsv2.types.communication_limits_config.CommunicationLimitsConfig"
        ] = None,
        tags: Optional["aws_sdk_connectcampaignsv2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.create_campaign_response.CreateCampaignResponse":
        """Creates a campaign for the specified Amazon Connect account. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.create_campaign_request.CreateCampaignRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.create_campaign

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.create_campaign.create_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.create_campaign_request.CreateCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["connect_instance_id"] = connect_instance_id
        if channel_subtype_config is not None:
            input_["channel_subtype_config"] = channel_subtype_config
        if type is not None:
            input_["type"] = type
        if source is not None:
            input_["source"] = source
        if connect_campaign_flow_arn is not None:
            input_["connect_campaign_flow_arn"] = connect_campaign_flow_arn
        if schedule is not None:
            input_["schedule"] = schedule
        if entry_limits_config is not None:
            input_["entry_limits_config"] = entry_limits_config
        if communication_time_config is not None:
            input_["communication_time_config"] = communication_time_config
        if communication_limits_override is not None:
            input_["communication_limits_override"] = communication_limits_override
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_campaign(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Deletes a campaign from the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_campaign

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_campaign.delete_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.delete_campaign_request.DeleteCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_campaign_channel_subtype_config(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        channel_subtype: "aws_sdk_connectcampaignsv2.types.channel_subtype.ChannelSubtype",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Deletes the channel subtype config of a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.delete_campaign_channel_subtype_config_request.DeleteCampaignChannelSubtypeConfigRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_campaign_channel_subtype_config

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_campaign_channel_subtype_config.delete_campaign_channel_subtype_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.delete_campaign_channel_subtype_config_request.DeleteCampaignChannelSubtypeConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["channel_subtype"] = channel_subtype

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_campaign_communication_limits(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        config: "aws_sdk_connectcampaignsv2.types.communication_limits_config_type.CommunicationLimitsConfigType",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Deletes the communication limits config for a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.delete_campaign_communication_limits_request.DeleteCampaignCommunicationLimitsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_campaign_communication_limits

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_campaign_communication_limits.delete_campaign_communication_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.delete_campaign_communication_limits_request.DeleteCampaignCommunicationLimitsRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["config"] = config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_campaign_communication_time(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        config: "aws_sdk_connectcampaignsv2.types.communication_time_config_type.CommunicationTimeConfigType",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Deletes the communication time config for a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.delete_campaign_communication_time_request.DeleteCampaignCommunicationTimeRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_campaign_communication_time

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_campaign_communication_time.delete_campaign_communication_time(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.delete_campaign_communication_time_request.DeleteCampaignCommunicationTimeRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["config"] = config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_campaign_entry_limits(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Deletes the entry limits config for a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.delete_campaign_entry_limits_request.DeleteCampaignEntryLimitsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_campaign_entry_limits

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_campaign_entry_limits.delete_campaign_entry_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.delete_campaign_entry_limits_request.DeleteCampaignEntryLimitsRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_connect_instance_config(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
        campaign_deletion_policy: Optional[
            "aws_sdk_connectcampaignsv2.types.campaign_deletion_policy.CampaignDeletionPolicy"
        ] = None,
    ) -> None:
        """Deletes a connect instance config from the specified AWS account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.delete_connect_instance_config_request.DeleteConnectInstanceConfigRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_connect_instance_config

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_connect_instance_config.delete_connect_instance_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.delete_connect_instance_config_request.DeleteConnectInstanceConfigRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id
        if campaign_deletion_policy is not None:
            input_["campaign_deletion_policy"] = campaign_deletion_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_connect_instance_integration(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        integration_identifier: "aws_sdk_connectcampaignsv2.types.integration_identifier.IntegrationIdentifier",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Delete the integration for the specified Amazon Connect instance."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.delete_connect_instance_integration_request.DeleteConnectInstanceIntegrationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_connect_instance_integration

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_connect_instance_integration.delete_connect_instance_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.delete_connect_instance_integration_request.DeleteConnectInstanceIntegrationRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id
        input_["integration_identifier"] = integration_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_instance_onboarding_job(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Delete the Connect Campaigns onboarding job for the specified Amazon Connect instance."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.delete_instance_onboarding_job_request.DeleteInstanceOnboardingJobRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_instance_onboarding_job

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.delete_instance_onboarding_job.delete_instance_onboarding_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.delete_instance_onboarding_job_request.DeleteInstanceOnboardingJobRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_campaign(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.describe_campaign_response.DescribeCampaignResponse":
        """Describes the specific campaign."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.describe_campaign_request.DescribeCampaignRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.describe_campaign_response.DescribeCampaignResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.describe_campaign

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.describe_campaign.describe_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.describe_campaign_request.DescribeCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_campaign_state(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.get_campaign_state_response.GetCampaignStateResponse":
        """Get state of a campaign for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.get_campaign_state_request.GetCampaignStateRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.get_campaign_state_response.GetCampaignStateResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.get_campaign_state

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.get_campaign_state.get_campaign_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.get_campaign_state_request.GetCampaignStateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_campaign_state_batch(
        self,
        campaign_ids: "aws_sdk_connectcampaignsv2.types.campaign_id_list.CampaignIdList",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.get_campaign_state_batch_response.GetCampaignStateBatchResponse":
        """Get state of campaigns for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.get_campaign_state_batch_request.GetCampaignStateBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.get_campaign_state_batch_response.GetCampaignStateBatchResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.get_campaign_state_batch

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.get_campaign_state_batch.get_campaign_state_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.get_campaign_state_batch_request.GetCampaignStateBatchRequest = {}  # type: ignore[typeddict-item]
        input_["campaign_ids"] = campaign_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_connect_instance_config(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.get_connect_instance_config_response.GetConnectInstanceConfigResponse":
        """Get the specific Connect instance config."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.get_connect_instance_config_request.GetConnectInstanceConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.get_connect_instance_config_response.GetConnectInstanceConfigResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.get_connect_instance_config

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.get_connect_instance_config.get_connect_instance_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.get_connect_instance_config_request.GetConnectInstanceConfigRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_instance_communication_limits(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.get_instance_communication_limits_response.GetInstanceCommunicationLimitsResponse":
        """Get the instance communication limits."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.get_instance_communication_limits_request.GetInstanceCommunicationLimitsRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.get_instance_communication_limits_response.GetInstanceCommunicationLimitsResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.get_instance_communication_limits

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.get_instance_communication_limits.get_instance_communication_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.get_instance_communication_limits_request.GetInstanceCommunicationLimitsRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_instance_onboarding_job_status(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.get_instance_onboarding_job_status_response.GetInstanceOnboardingJobStatusResponse":
        """Get the specific instance onboarding job status."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.get_instance_onboarding_job_status_request.GetInstanceOnboardingJobStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.get_instance_onboarding_job_status_response.GetInstanceOnboardingJobStatusResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.get_instance_onboarding_job_status

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.get_instance_onboarding_job_status.get_instance_onboarding_job_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.get_instance_onboarding_job_status_request.GetInstanceOnboardingJobStatusRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_campaigns(
        self,
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcampaignsv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_connectcampaignsv2.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "aws_sdk_connectcampaignsv2.types.campaign_filters.CampaignFilters"
        ] = None,
    ) -> (
        "aws_sdk_connectcampaignsv2.types.list_campaigns_response.ListCampaignsResponse"
    ):
        """Provides summary information about the campaigns under the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.list_campaigns_request.ListCampaignsRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.list_campaigns_response.ListCampaignsResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.list_campaigns

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.list_campaigns.list_campaigns(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.list_campaigns_request.ListCampaignsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_campaigns(
        self,
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcampaignsv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_connectcampaignsv2.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "aws_sdk_connectcampaignsv2.types.campaign_filters.CampaignFilters"
        ] = None,
    ) -> "Iterator[aws_sdk_connectcampaignsv2.types.campaign_summary.CampaignSummary]":
        _token = next_token
        while True:
            _response = self.list_campaigns(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("campaign_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_connect_instance_integrations(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcampaignsv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_connectcampaignsv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.list_connect_instance_integrations_response.ListConnectInstanceIntegrationsResponse":
        """Provides summary information about the integration under the specified Connect instance."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.list_connect_instance_integrations_request.ListConnectInstanceIntegrationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.list_connect_instance_integrations_response.ListConnectInstanceIntegrationsResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.list_connect_instance_integrations

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.list_connect_instance_integrations.list_connect_instance_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.list_connect_instance_integrations_request.ListConnectInstanceIntegrationsRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id
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

    def iter_list_connect_instance_integrations(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcampaignsv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_connectcampaignsv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_connectcampaignsv2.types.integration_summary.IntegrationSummary]":
        _token = next_token
        while True:
            _response = self.list_connect_instance_integrations(
                connect_instance_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("integration_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        arn: "aws_sdk_connectcampaignsv2.types.arn.Arn",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """List tags for a resource."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.list_tags_for_resource

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def pause_campaign(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Pauses a campaign for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.pause_campaign_request.PauseCampaignRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.pause_campaign

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.pause_campaign.pause_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.pause_campaign_request.PauseCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_connect_instance_integration(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        integration_config: "aws_sdk_connectcampaignsv2.types.integration_config.IntegrationConfig",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Put or update the integration for the specified Amazon Connect instance."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.put_connect_instance_integration_request.PutConnectInstanceIntegrationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.put_connect_instance_integration

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.put_connect_instance_integration.put_connect_instance_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.put_connect_instance_integration_request.PutConnectInstanceIntegrationRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id
        input_["integration_config"] = integration_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_instance_communication_limits(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        communication_limits_config: "aws_sdk_connectcampaignsv2.types.instance_communication_limits_config.InstanceCommunicationLimitsConfig",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Put the instance communication limits. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.put_instance_communication_limits_request.PutInstanceCommunicationLimitsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.put_instance_communication_limits

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.put_instance_communication_limits.put_instance_communication_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.put_instance_communication_limits_request.PutInstanceCommunicationLimitsRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id
        input_["communication_limits_config"] = communication_limits_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_outbound_request_batch(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        outbound_requests: "aws_sdk_connectcampaignsv2.types.outbound_request_list.OutboundRequestList",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.put_outbound_request_batch_response.PutOutboundRequestBatchResponse":
        """Creates outbound requests for the specified campaign Amazon Connect account. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.put_outbound_request_batch_request.PutOutboundRequestBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.put_outbound_request_batch_response.PutOutboundRequestBatchResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.put_outbound_request_batch

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.put_outbound_request_batch.put_outbound_request_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.put_outbound_request_batch_request.PutOutboundRequestBatchRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["outbound_requests"] = outbound_requests

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_profile_outbound_request_batch(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        profile_outbound_requests: "aws_sdk_connectcampaignsv2.types.profile_outbound_request_list.ProfileOutboundRequestList",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.put_profile_outbound_request_batch_response.PutProfileOutboundRequestBatchResponse":
        """Takes in a list of profile outbound requests to be placed as part of an outbound campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.put_profile_outbound_request_batch_request.PutProfileOutboundRequestBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.put_profile_outbound_request_batch_response.PutProfileOutboundRequestBatchResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.put_profile_outbound_request_batch

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.put_profile_outbound_request_batch.put_profile_outbound_request_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.put_profile_outbound_request_batch_request.PutProfileOutboundRequestBatchRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["profile_outbound_requests"] = profile_outbound_requests

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def resume_campaign(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Stops a campaign for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.resume_campaign_request.ResumeCampaignRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.resume_campaign

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.resume_campaign.resume_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.resume_campaign_request.ResumeCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_campaign(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Starts a campaign for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.start_campaign_request.StartCampaignRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.start_campaign

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.start_campaign.start_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.start_campaign_request.StartCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_instance_onboarding_job(
        self,
        connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId",
        encryption_config: "aws_sdk_connectcampaignsv2.types.encryption_config.EncryptionConfig",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> "aws_sdk_connectcampaignsv2.types.start_instance_onboarding_job_response.StartInstanceOnboardingJobResponse":
        """Onboard the specific Amazon Connect instance to Connect Campaigns."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.start_instance_onboarding_job_request.StartInstanceOnboardingJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaignsv2.types.start_instance_onboarding_job_response.StartInstanceOnboardingJobResponse"
        ]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.start_instance_onboarding_job

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.start_instance_onboarding_job.start_instance_onboarding_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.start_instance_onboarding_job_request.StartInstanceOnboardingJobRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id
        input_["encryption_config"] = encryption_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_campaign(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Stops a campaign for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.stop_campaign_request.StopCampaignRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.stop_campaign

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.stop_campaign.stop_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.stop_campaign_request.StopCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        arn: "aws_sdk_connectcampaignsv2.types.arn.Arn",
        tags: "aws_sdk_connectcampaignsv2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Tag a resource."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.tag_resource

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        arn: "aws_sdk_connectcampaignsv2.types.arn.Arn",
        tag_keys: "aws_sdk_connectcampaignsv2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Untag a resource."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.untag_resource

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_channel_subtype_config(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        channel_subtype_config: "aws_sdk_connectcampaignsv2.types.channel_subtype_config.ChannelSubtypeConfig",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Updates the channel subtype config of a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.update_campaign_channel_subtype_config_request.UpdateCampaignChannelSubtypeConfigRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_channel_subtype_config

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_channel_subtype_config.update_campaign_channel_subtype_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.update_campaign_channel_subtype_config_request.UpdateCampaignChannelSubtypeConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["channel_subtype_config"] = channel_subtype_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_communication_limits(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        communication_limits_override: "aws_sdk_connectcampaignsv2.types.communication_limits_config.CommunicationLimitsConfig",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Updates the communication limits config for a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.update_campaign_communication_limits_request.UpdateCampaignCommunicationLimitsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_communication_limits

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_communication_limits.update_campaign_communication_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.update_campaign_communication_limits_request.UpdateCampaignCommunicationLimitsRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["communication_limits_override"] = communication_limits_override

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_communication_time(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        communication_time_config: "aws_sdk_connectcampaignsv2.types.communication_time_config.CommunicationTimeConfig",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Updates the communication time config for a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.update_campaign_communication_time_request.UpdateCampaignCommunicationTimeRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_communication_time

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_communication_time.update_campaign_communication_time(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.update_campaign_communication_time_request.UpdateCampaignCommunicationTimeRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["communication_time_config"] = communication_time_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_entry_limits(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        entry_limits_config: "aws_sdk_connectcampaignsv2.types.entry_limits_config.EntryLimitsConfig",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Updates the entry limits config for a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.update_campaign_entry_limits_request.UpdateCampaignEntryLimitsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_entry_limits

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_entry_limits.update_campaign_entry_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.update_campaign_entry_limits_request.UpdateCampaignEntryLimitsRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["entry_limits_config"] = entry_limits_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_flow_association(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        connect_campaign_flow_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Updates the campaign flow associated with a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.update_campaign_flow_association_request.UpdateCampaignFlowAssociationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_flow_association

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_flow_association.update_campaign_flow_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.update_campaign_flow_association_request.UpdateCampaignFlowAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["connect_campaign_flow_arn"] = connect_campaign_flow_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_name(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        name: "aws_sdk_connectcampaignsv2.types.campaign_name.CampaignName",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Updates the name of a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.update_campaign_name_request.UpdateCampaignNameRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_name

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_name.update_campaign_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.update_campaign_name_request.UpdateCampaignNameRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_schedule(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        schedule: "aws_sdk_connectcampaignsv2.types.schedule.Schedule",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Updates the schedule for a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.update_campaign_schedule_request.UpdateCampaignScheduleRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_schedule

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_schedule.update_campaign_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.update_campaign_schedule_request.UpdateCampaignScheduleRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["schedule"] = schedule

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_source(
        self,
        id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId",
        source: "aws_sdk_connectcampaignsv2.types.source.Source",
        *,
        config_overrides: Optional[ConnectCampaignsV2ClientConfig] = None,
    ) -> None:
        """Updates the campaign source with a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaignsv2.types.update_campaign_source_request.UpdateCampaignSourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_source

            output, http_response = (
                aws_sdk_connectcampaignsv2._operations.amazon_connect_campaign_service_v2.update_campaign_source.update_campaign_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaignsv2.types.update_campaign_source_request.UpdateCampaignSourceRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["source"] = source

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
