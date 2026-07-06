"""Generated from Smithy shape ``com.amazonaws.mediapackage#MediaPackage``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_mediapackage._auth._signers
import aws_sdk_mediapackage._auth._sigv4
from aws_sdk_mediapackage._auth._identity import Credentials
from aws_sdk_mediapackage._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_mediapackage._auth._zapros_handler import AuthMiddleware
from aws_sdk_mediapackage._pagination import resolve_path as _resolve_path
from aws_sdk_mediapackage._services._aws_config import aaws_config
from aws_sdk_mediapackage._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__integer
    import aws_sdk_mediapackage.types.__list_of__string
    import aws_sdk_mediapackage.types.__map_of__string
    import aws_sdk_mediapackage.types.__string
    import aws_sdk_mediapackage.types.authorization
    import aws_sdk_mediapackage.types.channel
    import aws_sdk_mediapackage.types.cmaf_package_create_or_update_parameters
    import aws_sdk_mediapackage.types.configure_logs_request
    import aws_sdk_mediapackage.types.configure_logs_response
    import aws_sdk_mediapackage.types.create_channel_request
    import aws_sdk_mediapackage.types.create_channel_response
    import aws_sdk_mediapackage.types.create_harvest_job_request
    import aws_sdk_mediapackage.types.create_harvest_job_response
    import aws_sdk_mediapackage.types.create_origin_endpoint_request
    import aws_sdk_mediapackage.types.create_origin_endpoint_response
    import aws_sdk_mediapackage.types.dash_package
    import aws_sdk_mediapackage.types.delete_channel_request
    import aws_sdk_mediapackage.types.delete_channel_response
    import aws_sdk_mediapackage.types.delete_origin_endpoint_request
    import aws_sdk_mediapackage.types.delete_origin_endpoint_response
    import aws_sdk_mediapackage.types.describe_channel_request
    import aws_sdk_mediapackage.types.describe_channel_response
    import aws_sdk_mediapackage.types.describe_harvest_job_request
    import aws_sdk_mediapackage.types.describe_harvest_job_response
    import aws_sdk_mediapackage.types.describe_origin_endpoint_request
    import aws_sdk_mediapackage.types.describe_origin_endpoint_response
    import aws_sdk_mediapackage.types.egress_access_logs
    import aws_sdk_mediapackage.types.harvest_job
    import aws_sdk_mediapackage.types.hls_package
    import aws_sdk_mediapackage.types.ingress_access_logs
    import aws_sdk_mediapackage.types.list_channels_request
    import aws_sdk_mediapackage.types.list_channels_response
    import aws_sdk_mediapackage.types.list_harvest_jobs_request
    import aws_sdk_mediapackage.types.list_harvest_jobs_response
    import aws_sdk_mediapackage.types.list_origin_endpoints_request
    import aws_sdk_mediapackage.types.list_origin_endpoints_response
    import aws_sdk_mediapackage.types.list_tags_for_resource_request
    import aws_sdk_mediapackage.types.list_tags_for_resource_response
    import aws_sdk_mediapackage.types.max_results
    import aws_sdk_mediapackage.types.mss_package
    import aws_sdk_mediapackage.types.origin_endpoint
    import aws_sdk_mediapackage.types.origination
    import aws_sdk_mediapackage.types.rotate_channel_credentials_request
    import aws_sdk_mediapackage.types.rotate_channel_credentials_response
    import aws_sdk_mediapackage.types.rotate_ingest_endpoint_credentials_request
    import aws_sdk_mediapackage.types.rotate_ingest_endpoint_credentials_response
    import aws_sdk_mediapackage.types.s3_destination
    import aws_sdk_mediapackage.types.tag_resource_request
    import aws_sdk_mediapackage.types.tags
    import aws_sdk_mediapackage.types.untag_resource_request
    import aws_sdk_mediapackage.types.update_channel_request
    import aws_sdk_mediapackage.types.update_channel_response
    import aws_sdk_mediapackage.types.update_origin_endpoint_request
    import aws_sdk_mediapackage.types.update_origin_endpoint_response


class AsyncMediaPackageClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncMediaPackageClient:
    """A client for the ``MediaPackage`` service.

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
        self._config = AsyncMediaPackageClientConfig(
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
        self, config_overrides: Optional[AsyncMediaPackageClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMediaPackageClientConfig = config_overrides or {}
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

    async def configure_logs(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        egress_access_logs: Optional[
            "aws_sdk_mediapackage.types.egress_access_logs.EgressAccessLogs"
        ] = None,
        ingress_access_logs: Optional[
            "aws_sdk_mediapackage.types.ingress_access_logs.IngressAccessLogs"
        ] = None,
    ) -> "aws_sdk_mediapackage.types.configure_logs_response.ConfigureLogsResponse":
        """Changes the Channel's properities to configure log subscription

        Args:
            id: The ID of the channel to log subscription.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.configure_logs_request.ConfigureLogsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.configure_logs_response.ConfigureLogsResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.configure_logs

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.configure_logs.async_configure_logs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.configure_logs_request.ConfigureLogsRequest = {}  # type: ignore[typeddict-item]
        if egress_access_logs is not None:
            input_["egress_access_logs"] = egress_access_logs
        input_["id"] = id
        if ingress_access_logs is not None:
            input_["ingress_access_logs"] = ingress_access_logs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_channel(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        description: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
        tags: Optional["aws_sdk_mediapackage.types.tags.Tags"] = None,
    ) -> "aws_sdk_mediapackage.types.create_channel_response.CreateChannelResponse":
        """Creates a new Channel.

        Args:
            description: A short text description of the Channel.
            id: The ID of the Channel. The ID must be unique within the region and it cannot be changed after a Channel is created.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.create_channel_request.CreateChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.create_channel_response.CreateChannelResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.create_channel

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.create_channel.async_create_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.create_channel_request.CreateChannelRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["id"] = id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_harvest_job(
        self,
        end_time: "aws_sdk_mediapackage.types.__string.__string",
        id: "aws_sdk_mediapackage.types.__string.__string",
        origin_endpoint_id: "aws_sdk_mediapackage.types.__string.__string",
        s3_destination: "aws_sdk_mediapackage.types.s3_destination.S3Destination",
        start_time: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> "aws_sdk_mediapackage.types.create_harvest_job_response.CreateHarvestJobResponse":
        """Creates a new HarvestJob record.

        Args:
            end_time: The end of the time-window which will be harvested
            id: The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted
            origin_endpoint_id: The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted.
            start_time: The start of the time-window which will be harvested

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.create_harvest_job_request.CreateHarvestJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.create_harvest_job_response.CreateHarvestJobResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.create_harvest_job

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.create_harvest_job.async_create_harvest_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.create_harvest_job_request.CreateHarvestJobRequest = {}  # type: ignore[typeddict-item]
        input_["end_time"] = end_time
        input_["id"] = id
        input_["origin_endpoint_id"] = origin_endpoint_id
        input_["s3_destination"] = s3_destination
        input_["start_time"] = start_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_origin_endpoint(
        self,
        channel_id: "aws_sdk_mediapackage.types.__string.__string",
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        authorization: Optional[
            "aws_sdk_mediapackage.types.authorization.Authorization"
        ] = None,
        cmaf_package: Optional[
            "aws_sdk_mediapackage.types.cmaf_package_create_or_update_parameters.CmafPackageCreateOrUpdateParameters"
        ] = None,
        dash_package: Optional[
            "aws_sdk_mediapackage.types.dash_package.DashPackage"
        ] = None,
        description: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
        hls_package: Optional[
            "aws_sdk_mediapackage.types.hls_package.HlsPackage"
        ] = None,
        manifest_name: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
        mss_package: Optional[
            "aws_sdk_mediapackage.types.mss_package.MssPackage"
        ] = None,
        origination: Optional[
            "aws_sdk_mediapackage.types.origination.Origination"
        ] = None,
        startover_window_seconds: Optional[
            "aws_sdk_mediapackage.types.__integer.__integer"
        ] = None,
        tags: Optional["aws_sdk_mediapackage.types.tags.Tags"] = None,
        time_delay_seconds: Optional[
            "aws_sdk_mediapackage.types.__integer.__integer"
        ] = None,
        whitelist: Optional[
            "aws_sdk_mediapackage.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "aws_sdk_mediapackage.types.create_origin_endpoint_response.CreateOriginEndpointResponse":
        r"""Creates a new OriginEndpoint record.

        Args:
            channel_id: The ID of the Channel that the OriginEndpoint will be associated with. This cannot be changed after the OriginEndpoint is created.
            description: A short text description of the OriginEndpoint.
            id: The ID of the OriginEndpoint. The ID must be unique within the region and it cannot be changed after the OriginEndpoint is created.
            manifest_name: A short string that will be used as the filename of the OriginEndpoint URL (defaults to \"index\").
            origination: Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
            startover_window_seconds: Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
            time_delay_seconds: Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
            whitelist: A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.create_origin_endpoint_request.CreateOriginEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.create_origin_endpoint_response.CreateOriginEndpointResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.create_origin_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.create_origin_endpoint.async_create_origin_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.create_origin_endpoint_request.CreateOriginEndpointRequest = {}  # type: ignore[typeddict-item]
        if authorization is not None:
            input_["authorization"] = authorization
        input_["channel_id"] = channel_id
        if cmaf_package is not None:
            input_["cmaf_package"] = cmaf_package
        if dash_package is not None:
            input_["dash_package"] = dash_package
        if description is not None:
            input_["description"] = description
        if hls_package is not None:
            input_["hls_package"] = hls_package
        input_["id"] = id
        if manifest_name is not None:
            input_["manifest_name"] = manifest_name
        if mss_package is not None:
            input_["mss_package"] = mss_package
        if origination is not None:
            input_["origination"] = origination
        if startover_window_seconds is not None:
            input_["startover_window_seconds"] = startover_window_seconds
        if tags is not None:
            input_["tags"] = tags
        if time_delay_seconds is not None:
            input_["time_delay_seconds"] = time_delay_seconds
        if whitelist is not None:
            input_["whitelist"] = whitelist

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_channel(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> "aws_sdk_mediapackage.types.delete_channel_response.DeleteChannelResponse":
        """Deletes an existing Channel.

        Args:
            id: The ID of the Channel to delete.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.delete_channel_request.DeleteChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.delete_channel_response.DeleteChannelResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.delete_channel

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.delete_channel.async_delete_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.delete_channel_request.DeleteChannelRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_origin_endpoint(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> "aws_sdk_mediapackage.types.delete_origin_endpoint_response.DeleteOriginEndpointResponse":
        """Deletes an existing OriginEndpoint.

        Args:
            id: The ID of the OriginEndpoint to delete.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.delete_origin_endpoint_request.DeleteOriginEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.delete_origin_endpoint_response.DeleteOriginEndpointResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.delete_origin_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.delete_origin_endpoint.async_delete_origin_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.delete_origin_endpoint_request.DeleteOriginEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_channel(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> "aws_sdk_mediapackage.types.describe_channel_response.DescribeChannelResponse":
        """Gets details about a Channel.

        Args:
            id: The ID of a Channel.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.describe_channel_request.DescribeChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.describe_channel_response.DescribeChannelResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.describe_channel

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.describe_channel.async_describe_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.describe_channel_request.DescribeChannelRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_harvest_job(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> "aws_sdk_mediapackage.types.describe_harvest_job_response.DescribeHarvestJobResponse":
        """Gets details about an existing HarvestJob.

        Args:
            id: The ID of the HarvestJob.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.describe_harvest_job_request.DescribeHarvestJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.describe_harvest_job_response.DescribeHarvestJobResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.describe_harvest_job

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.describe_harvest_job.async_describe_harvest_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.describe_harvest_job_request.DescribeHarvestJobRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_origin_endpoint(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> "aws_sdk_mediapackage.types.describe_origin_endpoint_response.DescribeOriginEndpointResponse":
        """Gets details about an existing OriginEndpoint.

        Args:
            id: The ID of the OriginEndpoint.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.describe_origin_endpoint_request.DescribeOriginEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.describe_origin_endpoint_response.DescribeOriginEndpointResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.describe_origin_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.describe_origin_endpoint.async_describe_origin_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.describe_origin_endpoint_request.DescribeOriginEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_channels(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediapackage.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
    ) -> "aws_sdk_mediapackage.types.list_channels_response.ListChannelsResponse":
        """Returns a collection of Channels.

        Args:
            max_results: Upper bound on number of records to return.
            next_token: A token used to resume pagination from the end of a previous request.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.list_channels_request.ListChannelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.list_channels_response.ListChannelsResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.list_channels

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.list_channels.async_list_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.list_channels_request.ListChannelsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_channels(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediapackage.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_mediapackage.types.channel.Channel]":
        _token = next_token
        while True:
            _response = await self.list_channels(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channels",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_harvest_jobs(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        include_channel_id: Optional[
            "aws_sdk_mediapackage.types.__string.__string"
        ] = None,
        include_status: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_mediapackage.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
    ) -> (
        "aws_sdk_mediapackage.types.list_harvest_jobs_response.ListHarvestJobsResponse"
    ):
        """Returns a collection of HarvestJob records.

        Args:
            include_channel_id: When specified, the request will return only HarvestJobs associated with the given Channel ID.
            include_status: When specified, the request will return only HarvestJobs in the given status.
            max_results: The upper bound on the number of records to return.
            next_token: A token used to resume pagination from the end of a previous request.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.list_harvest_jobs_request.ListHarvestJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.list_harvest_jobs_response.ListHarvestJobsResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.list_harvest_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.list_harvest_jobs.async_list_harvest_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.list_harvest_jobs_request.ListHarvestJobsRequest = {}  # type: ignore[typeddict-item]
        if include_channel_id is not None:
            input_["include_channel_id"] = include_channel_id
        if include_status is not None:
            input_["include_status"] = include_status
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

    async def iter_list_harvest_jobs(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        include_channel_id: Optional[
            "aws_sdk_mediapackage.types.__string.__string"
        ] = None,
        include_status: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_mediapackage.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_mediapackage.types.harvest_job.HarvestJob]":
        _token = next_token
        while True:
            _response = await self.list_harvest_jobs(
                config_overrides=config_overrides,
                include_channel_id=include_channel_id,
                include_status=include_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("harvest_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_origin_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        channel_id: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_mediapackage.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
    ) -> "aws_sdk_mediapackage.types.list_origin_endpoints_response.ListOriginEndpointsResponse":
        """Returns a collection of OriginEndpoint records.

        Args:
            channel_id: When specified, the request will return only OriginEndpoints associated with the given Channel ID.
            max_results: The upper bound on the number of records to return.
            next_token: A token used to resume pagination from the end of a previous request.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.list_origin_endpoints_request.ListOriginEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.list_origin_endpoints_response.ListOriginEndpointsResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.list_origin_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.list_origin_endpoints.async_list_origin_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.list_origin_endpoints_request.ListOriginEndpointsRequest = {}  # type: ignore[typeddict-item]
        if channel_id is not None:
            input_["channel_id"] = channel_id
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

    async def iter_list_origin_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        channel_id: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_mediapackage.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_mediapackage.types.origin_endpoint.OriginEndpoint]":
        _token = next_token
        while True:
            _response = await self.list_origin_endpoints(
                config_overrides=config_overrides,
                channel_id=channel_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("origin_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> "aws_sdk_mediapackage.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def rotate_channel_credentials(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> "aws_sdk_mediapackage.types.rotate_channel_credentials_response.RotateChannelCredentialsResponse":
        """Changes the Channel's first IngestEndpoint's username and password. WARNING - This API is deprecated. Please use RotateIngestEndpointCredentials instead

        Args:
            id: The ID of the channel to update.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.rotate_channel_credentials_request.RotateChannelCredentialsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.rotate_channel_credentials_response.RotateChannelCredentialsResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.rotate_channel_credentials

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.rotate_channel_credentials.async_rotate_channel_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.rotate_channel_credentials_request.RotateChannelCredentialsRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def rotate_ingest_endpoint_credentials(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        ingest_endpoint_id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> "aws_sdk_mediapackage.types.rotate_ingest_endpoint_credentials_response.RotateIngestEndpointCredentialsResponse":
        """Rotate the IngestEndpoint's username and password, as specified by the IngestEndpoint's id.

        Args:
            id: The ID of the channel the IngestEndpoint is on.
            ingest_endpoint_id: The id of the IngestEndpoint whose credentials should be rotated

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.rotate_ingest_endpoint_credentials_request.RotateIngestEndpointCredentialsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.rotate_ingest_endpoint_credentials_response.RotateIngestEndpointCredentialsResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.rotate_ingest_endpoint_credentials

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.rotate_ingest_endpoint_credentials.async_rotate_ingest_endpoint_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.rotate_ingest_endpoint_credentials_request.RotateIngestEndpointCredentialsRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["ingest_endpoint_id"] = ingest_endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_mediapackage.types.__string.__string",
        tags: "aws_sdk_mediapackage.types.__map_of__string.__mapOf__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> None:
        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_mediapackage._operations.media_package.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_mediapackage.types.__string.__string",
        tag_keys: "aws_sdk_mediapackage.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
    ) -> None:
        """untag_resource

        Args:
            tag_keys: The key(s) of tag to be deleted

        Raises:
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_mediapackage._operations.media_package.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_channel(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        description: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
    ) -> "aws_sdk_mediapackage.types.update_channel_response.UpdateChannelResponse":
        """Updates an existing Channel.

        Args:
            description: A short text description of the Channel.
            id: The ID of the Channel to update.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.update_channel_request.UpdateChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.update_channel_response.UpdateChannelResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.update_channel

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.update_channel.async_update_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.update_channel_request.UpdateChannelRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_origin_endpoint(
        self,
        id: "aws_sdk_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageClientConfig] = None,
        authorization: Optional[
            "aws_sdk_mediapackage.types.authorization.Authorization"
        ] = None,
        cmaf_package: Optional[
            "aws_sdk_mediapackage.types.cmaf_package_create_or_update_parameters.CmafPackageCreateOrUpdateParameters"
        ] = None,
        dash_package: Optional[
            "aws_sdk_mediapackage.types.dash_package.DashPackage"
        ] = None,
        description: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
        hls_package: Optional[
            "aws_sdk_mediapackage.types.hls_package.HlsPackage"
        ] = None,
        manifest_name: Optional["aws_sdk_mediapackage.types.__string.__string"] = None,
        mss_package: Optional[
            "aws_sdk_mediapackage.types.mss_package.MssPackage"
        ] = None,
        origination: Optional[
            "aws_sdk_mediapackage.types.origination.Origination"
        ] = None,
        startover_window_seconds: Optional[
            "aws_sdk_mediapackage.types.__integer.__integer"
        ] = None,
        time_delay_seconds: Optional[
            "aws_sdk_mediapackage.types.__integer.__integer"
        ] = None,
        whitelist: Optional[
            "aws_sdk_mediapackage.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "aws_sdk_mediapackage.types.update_origin_endpoint_response.UpdateOriginEndpointResponse":
        """Updates an existing OriginEndpoint.

        Args:
            description: A short text description of the OriginEndpoint.
            id: The ID of the OriginEndpoint to update.
            manifest_name: A short string that will be appended to the end of the Endpoint URL.
            origination: Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
            startover_window_seconds: Maximum duration (in seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
            time_delay_seconds: Amount of delay (in seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
            whitelist: A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.

        Raises:
            aws_sdk_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            aws_sdk_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            aws_sdk_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            aws_sdk_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            aws_sdk_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            aws_sdk_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediapackage.types.update_origin_endpoint_request.UpdateOriginEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediapackage.types.update_origin_endpoint_response.UpdateOriginEndpointResponse"
        ]:
            import aws_sdk_mediapackage._operations.media_package.update_origin_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_mediapackage._operations.media_package.update_origin_endpoint.async_update_origin_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediapackage.types.update_origin_endpoint_request.UpdateOriginEndpointRequest = {}  # type: ignore[typeddict-item]
        if authorization is not None:
            input_["authorization"] = authorization
        if cmaf_package is not None:
            input_["cmaf_package"] = cmaf_package
        if dash_package is not None:
            input_["dash_package"] = dash_package
        if description is not None:
            input_["description"] = description
        if hls_package is not None:
            input_["hls_package"] = hls_package
        input_["id"] = id
        if manifest_name is not None:
            input_["manifest_name"] = manifest_name
        if mss_package is not None:
            input_["mss_package"] = mss_package
        if origination is not None:
            input_["origination"] = origination
        if startover_window_seconds is not None:
            input_["startover_window_seconds"] = startover_window_seconds
        if time_delay_seconds is not None:
            input_["time_delay_seconds"] = time_delay_seconds
        if whitelist is not None:
            input_["whitelist"] = whitelist

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
