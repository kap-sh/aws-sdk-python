"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#AmazonConnectCampaignService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_connectcampaigns._auth._signers
import aws_sdk_connectcampaigns._auth._sigv4
from aws_sdk_connectcampaigns._auth._identity import Credentials
from aws_sdk_connectcampaigns._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_connectcampaigns._auth._zapros_handler import AuthMiddleware
from aws_sdk_connectcampaigns._pagination import resolve_path as _resolve_path
from aws_sdk_connectcampaigns._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.answer_machine_detection_config
    import aws_sdk_connectcampaigns.types.arn
    import aws_sdk_connectcampaigns.types.campaign_filters
    import aws_sdk_connectcampaigns.types.campaign_id
    import aws_sdk_connectcampaigns.types.campaign_id_list
    import aws_sdk_connectcampaigns.types.campaign_name
    import aws_sdk_connectcampaigns.types.campaign_summary
    import aws_sdk_connectcampaigns.types.contact_flow_id
    import aws_sdk_connectcampaigns.types.create_campaign_request
    import aws_sdk_connectcampaigns.types.create_campaign_response
    import aws_sdk_connectcampaigns.types.delete_campaign_request
    import aws_sdk_connectcampaigns.types.delete_connect_instance_config_request
    import aws_sdk_connectcampaigns.types.delete_instance_onboarding_job_request
    import aws_sdk_connectcampaigns.types.describe_campaign_request
    import aws_sdk_connectcampaigns.types.describe_campaign_response
    import aws_sdk_connectcampaigns.types.dial_request_list
    import aws_sdk_connectcampaigns.types.dialer_config
    import aws_sdk_connectcampaigns.types.encryption_config
    import aws_sdk_connectcampaigns.types.get_campaign_state_batch_request
    import aws_sdk_connectcampaigns.types.get_campaign_state_batch_response
    import aws_sdk_connectcampaigns.types.get_campaign_state_request
    import aws_sdk_connectcampaigns.types.get_campaign_state_response
    import aws_sdk_connectcampaigns.types.get_connect_instance_config_request
    import aws_sdk_connectcampaigns.types.get_connect_instance_config_response
    import aws_sdk_connectcampaigns.types.get_instance_onboarding_job_status_request
    import aws_sdk_connectcampaigns.types.get_instance_onboarding_job_status_response
    import aws_sdk_connectcampaigns.types.instance_id
    import aws_sdk_connectcampaigns.types.list_campaigns_request
    import aws_sdk_connectcampaigns.types.list_campaigns_response
    import aws_sdk_connectcampaigns.types.list_tags_for_resource_request
    import aws_sdk_connectcampaigns.types.list_tags_for_resource_response
    import aws_sdk_connectcampaigns.types.max_results
    import aws_sdk_connectcampaigns.types.next_token
    import aws_sdk_connectcampaigns.types.outbound_call_config
    import aws_sdk_connectcampaigns.types.pause_campaign_request
    import aws_sdk_connectcampaigns.types.put_dial_request_batch_request
    import aws_sdk_connectcampaigns.types.put_dial_request_batch_response
    import aws_sdk_connectcampaigns.types.resume_campaign_request
    import aws_sdk_connectcampaigns.types.source_phone_number
    import aws_sdk_connectcampaigns.types.start_campaign_request
    import aws_sdk_connectcampaigns.types.start_instance_onboarding_job_request
    import aws_sdk_connectcampaigns.types.start_instance_onboarding_job_response
    import aws_sdk_connectcampaigns.types.stop_campaign_request
    import aws_sdk_connectcampaigns.types.tag_key_list
    import aws_sdk_connectcampaigns.types.tag_map
    import aws_sdk_connectcampaigns.types.tag_resource_request
    import aws_sdk_connectcampaigns.types.untag_resource_request
    import aws_sdk_connectcampaigns.types.update_campaign_dialer_config_request
    import aws_sdk_connectcampaigns.types.update_campaign_name_request
    import aws_sdk_connectcampaigns.types.update_campaign_outbound_call_config_request


class ConnectCampaignsClientConfig(TypedDict, total=False):
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


class ConnectCampaignsClient:
    """A client for the ``ConnectCampaigns`` service.

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
        self.config = ConnectCampaignsClientConfig(
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
        self, config_overrides: Optional[ConnectCampaignsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ConnectCampaignsClientConfig = config_overrides or {}
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
        name: "aws_sdk_connectcampaigns.types.campaign_name.CampaignName",
        connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId",
        dialer_config: "aws_sdk_connectcampaigns.types.dialer_config.DialerConfig",
        outbound_call_config: "aws_sdk_connectcampaigns.types.outbound_call_config.OutboundCallConfig",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
        tags: Optional["aws_sdk_connectcampaigns.types.tag_map.TagMap"] = None,
    ) -> (
        "aws_sdk_connectcampaigns.types.create_campaign_response.CreateCampaignResponse"
    ):
        """Creates a campaign for the specified Amazon Connect account. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.create_campaign_request.CreateCampaignRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaigns.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.create_campaign

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.create_campaign.create_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.create_campaign_request.CreateCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["connect_instance_id"] = connect_instance_id
        input_["dialer_config"] = dialer_config
        input_["outbound_call_config"] = outbound_call_config
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
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Deletes a campaign from the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.delete_campaign

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.delete_campaign.delete_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.delete_campaign_request.DeleteCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_connect_instance_config(
        self,
        connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Deletes a connect instance config from the specified AWS account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.delete_connect_instance_config_request.DeleteConnectInstanceConfigRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.delete_connect_instance_config

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.delete_connect_instance_config.delete_connect_instance_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.delete_connect_instance_config_request.DeleteConnectInstanceConfigRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_instance_onboarding_job(
        self,
        connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Delete the Connect Campaigns onboarding job for the specified Amazon Connect instance."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.delete_instance_onboarding_job_request.DeleteInstanceOnboardingJobRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.delete_instance_onboarding_job

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.delete_instance_onboarding_job.delete_instance_onboarding_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.delete_instance_onboarding_job_request.DeleteInstanceOnboardingJobRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_campaign(
        self,
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> "aws_sdk_connectcampaigns.types.describe_campaign_response.DescribeCampaignResponse":
        """Describes the specific campaign."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.describe_campaign_request.DescribeCampaignRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaigns.types.describe_campaign_response.DescribeCampaignResponse"
        ]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.describe_campaign

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.describe_campaign.describe_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.describe_campaign_request.DescribeCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_campaign_state(
        self,
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> "aws_sdk_connectcampaigns.types.get_campaign_state_response.GetCampaignStateResponse":
        """Get state of a campaign for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.get_campaign_state_request.GetCampaignStateRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaigns.types.get_campaign_state_response.GetCampaignStateResponse"
        ]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.get_campaign_state

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.get_campaign_state.get_campaign_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.get_campaign_state_request.GetCampaignStateRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_campaign_state_batch(
        self,
        campaign_ids: "aws_sdk_connectcampaigns.types.campaign_id_list.CampaignIdList",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> "aws_sdk_connectcampaigns.types.get_campaign_state_batch_response.GetCampaignStateBatchResponse":
        """Get state of campaigns for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.get_campaign_state_batch_request.GetCampaignStateBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaigns.types.get_campaign_state_batch_response.GetCampaignStateBatchResponse"
        ]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.get_campaign_state_batch

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.get_campaign_state_batch.get_campaign_state_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.get_campaign_state_batch_request.GetCampaignStateBatchRequest = {}  # type: ignore[typeddict-item]
        input_["campaign_ids"] = campaign_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_connect_instance_config(
        self,
        connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> "aws_sdk_connectcampaigns.types.get_connect_instance_config_response.GetConnectInstanceConfigResponse":
        """Get the specific Connect instance config."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.get_connect_instance_config_request.GetConnectInstanceConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaigns.types.get_connect_instance_config_response.GetConnectInstanceConfigResponse"
        ]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.get_connect_instance_config

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.get_connect_instance_config.get_connect_instance_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.get_connect_instance_config_request.GetConnectInstanceConfigRequest = {}  # type: ignore[typeddict-item]
        input_["connect_instance_id"] = connect_instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_instance_onboarding_job_status(
        self,
        connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> "aws_sdk_connectcampaigns.types.get_instance_onboarding_job_status_response.GetInstanceOnboardingJobStatusResponse":
        """Get the specific instance onboarding job status."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.get_instance_onboarding_job_status_request.GetInstanceOnboardingJobStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaigns.types.get_instance_onboarding_job_status_response.GetInstanceOnboardingJobStatusResponse"
        ]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.get_instance_onboarding_job_status

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.get_instance_onboarding_job_status.get_instance_onboarding_job_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.get_instance_onboarding_job_status_request.GetInstanceOnboardingJobStatusRequest = {}  # type: ignore[typeddict-item]
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
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcampaigns.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_connectcampaigns.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "aws_sdk_connectcampaigns.types.campaign_filters.CampaignFilters"
        ] = None,
    ) -> "aws_sdk_connectcampaigns.types.list_campaigns_response.ListCampaignsResponse":
        """Provides summary information about the campaigns under the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.list_campaigns_request.ListCampaignsRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaigns.types.list_campaigns_response.ListCampaignsResponse"
        ]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.list_campaigns

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.list_campaigns.list_campaigns(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.list_campaigns_request.ListCampaignsRequest = {}  # type: ignore[typeddict-item]
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
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcampaigns.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_connectcampaigns.types.next_token.NextToken"
        ] = None,
        filters: Optional[
            "aws_sdk_connectcampaigns.types.campaign_filters.CampaignFilters"
        ] = None,
    ) -> "Iterator[aws_sdk_connectcampaigns.types.campaign_summary.CampaignSummary]":
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

    def list_tags_for_resource(
        self,
        arn: "aws_sdk_connectcampaigns.types.arn.Arn",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> "aws_sdk_connectcampaigns.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """List tags for a resource."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaigns.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def pause_campaign(
        self,
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Pauses a campaign for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.pause_campaign_request.PauseCampaignRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.pause_campaign

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.pause_campaign.pause_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.pause_campaign_request.PauseCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_dial_request_batch(
        self,
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        dial_requests: "aws_sdk_connectcampaigns.types.dial_request_list.DialRequestList",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> "aws_sdk_connectcampaigns.types.put_dial_request_batch_response.PutDialRequestBatchResponse":
        """Creates dials requests for the specified campaign Amazon Connect account. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.put_dial_request_batch_request.PutDialRequestBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaigns.types.put_dial_request_batch_response.PutDialRequestBatchResponse"
        ]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.put_dial_request_batch

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.put_dial_request_batch.put_dial_request_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.put_dial_request_batch_request.PutDialRequestBatchRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["dial_requests"] = dial_requests

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def resume_campaign(
        self,
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Stops a campaign for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.resume_campaign_request.ResumeCampaignRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.resume_campaign

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.resume_campaign.resume_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.resume_campaign_request.ResumeCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_campaign(
        self,
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Starts a campaign for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.start_campaign_request.StartCampaignRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.start_campaign

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.start_campaign.start_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.start_campaign_request.StartCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_instance_onboarding_job(
        self,
        connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId",
        encryption_config: "aws_sdk_connectcampaigns.types.encryption_config.EncryptionConfig",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> "aws_sdk_connectcampaigns.types.start_instance_onboarding_job_response.StartInstanceOnboardingJobResponse":
        """Onboard the specific Amazon Connect instance to Connect Campaigns."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.start_instance_onboarding_job_request.StartInstanceOnboardingJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcampaigns.types.start_instance_onboarding_job_response.StartInstanceOnboardingJobResponse"
        ]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.start_instance_onboarding_job

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.start_instance_onboarding_job.start_instance_onboarding_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.start_instance_onboarding_job_request.StartInstanceOnboardingJobRequest = {}  # type: ignore[typeddict-item]
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
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Stops a campaign for the specified Amazon Connect account."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.stop_campaign_request.StopCampaignRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.stop_campaign

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.stop_campaign.stop_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.stop_campaign_request.StopCampaignRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        arn: "aws_sdk_connectcampaigns.types.arn.Arn",
        tags: "aws_sdk_connectcampaigns.types.tag_map.TagMap",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Tag a resource."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.tag_resource

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        arn: "aws_sdk_connectcampaigns.types.arn.Arn",
        tag_keys: "aws_sdk_connectcampaigns.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Untag a resource."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.untag_resource

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_dialer_config(
        self,
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        dialer_config: "aws_sdk_connectcampaigns.types.dialer_config.DialerConfig",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Updates the dialer config of a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.update_campaign_dialer_config_request.UpdateCampaignDialerConfigRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_dialer_config

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_dialer_config.update_campaign_dialer_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.update_campaign_dialer_config_request.UpdateCampaignDialerConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["dialer_config"] = dialer_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_name(
        self,
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        name: "aws_sdk_connectcampaigns.types.campaign_name.CampaignName",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
    ) -> None:
        """Updates the name of a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.update_campaign_name_request.UpdateCampaignNameRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_name

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_name.update_campaign_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.update_campaign_name_request.UpdateCampaignNameRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_campaign_outbound_call_config(
        self,
        id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId",
        *,
        config_overrides: Optional[ConnectCampaignsClientConfig] = None,
        connect_contact_flow_id: Optional[
            "aws_sdk_connectcampaigns.types.contact_flow_id.ContactFlowId"
        ] = None,
        connect_source_phone_number: Optional[
            "aws_sdk_connectcampaigns.types.source_phone_number.SourcePhoneNumber"
        ] = None,
        answer_machine_detection_config: Optional[
            "aws_sdk_connectcampaigns.types.answer_machine_detection_config.AnswerMachineDetectionConfig"
        ] = None,
    ) -> None:
        """Updates the outbound call config of a campaign. This API is idempotent."""

        def _handler(
            req: "OperationRequest[aws_sdk_connectcampaigns.types.update_campaign_outbound_call_config_request.UpdateCampaignOutboundCallConfigRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_outbound_call_config

            output, http_response = (
                aws_sdk_connectcampaigns._operations.amazon_connect_campaign_service.update_campaign_outbound_call_config.update_campaign_outbound_call_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connectcampaigns.types.update_campaign_outbound_call_config_request.UpdateCampaignOutboundCallConfigRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if connect_contact_flow_id is not None:
            input_["connect_contact_flow_id"] = connect_contact_flow_id
        if connect_source_phone_number is not None:
            input_["connect_source_phone_number"] = connect_source_phone_number
        if answer_machine_detection_config is not None:
            input_["answer_machine_detection_config"] = answer_machine_detection_config

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
