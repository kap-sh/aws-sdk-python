"""Generated from Smithy shape ``com.amazonaws.groundstation#GroundStation``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_groundstation._auth._signers
import aws_sdk_groundstation._auth._sigv4
from aws_sdk_groundstation._auth._identity import Credentials
from aws_sdk_groundstation._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_groundstation._auth._zapros_handler import AuthMiddleware
from aws_sdk_groundstation._resources.ground_station.agent import AsyncAgent
from aws_sdk_groundstation._resources.ground_station.config import AsyncConfig
from aws_sdk_groundstation._resources.ground_station.contact import AsyncContact
from aws_sdk_groundstation._resources.ground_station.dataflow_endpoint_group import (
    AsyncDataflowEndpointGroup,
)
from aws_sdk_groundstation._resources.ground_station.dataflow_endpoint_group_v2 import (
    AsyncDataflowEndpointGroupV2,
)
from aws_sdk_groundstation._resources.ground_station.ephemeris import AsyncEphemeris
from aws_sdk_groundstation._resources.ground_station.ground_station_resource import (
    AsyncGroundStationResource,
)
from aws_sdk_groundstation._resources.ground_station.mission_profile import (
    AsyncMissionProfile,
)
from aws_sdk_groundstation._resources.ground_station.satellite import AsyncSatellite
from aws_sdk_groundstation._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.any_arn
    import aws_sdk_groundstation.types.get_agent_task_response_url_request
    import aws_sdk_groundstation.types.get_agent_task_response_url_response
    import aws_sdk_groundstation.types.get_minute_usage_request
    import aws_sdk_groundstation.types.get_minute_usage_response
    import aws_sdk_groundstation.types.list_tags_for_resource_request
    import aws_sdk_groundstation.types.list_tags_for_resource_response
    import aws_sdk_groundstation.types.month
    import aws_sdk_groundstation.types.tag_keys
    import aws_sdk_groundstation.types.tag_resource_request
    import aws_sdk_groundstation.types.tag_resource_response
    import aws_sdk_groundstation.types.tags_map
    import aws_sdk_groundstation.types.untag_resource_request
    import aws_sdk_groundstation.types.untag_resource_response
    import aws_sdk_groundstation.types.uuid
    import aws_sdk_groundstation.types.year


class AsyncGroundStationClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncGroundStationClient:
    """A client for the ``GroundStation`` service.

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
        self._config = AsyncGroundStationClientConfig(
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

        # resources
        self.agent = AsyncAgent(self)
        self.config = AsyncConfig(self)
        self.contact = AsyncContact(self)
        self.dataflow_endpoint_group = AsyncDataflowEndpointGroup(self)
        self.dataflow_endpoint_group_v2 = AsyncDataflowEndpointGroupV2(self)
        self.ephemeris = AsyncEphemeris(self)
        self.ground_station_resource = AsyncGroundStationResource(self)
        self.mission_profile = AsyncMissionProfile(self)
        self.satellite = AsyncSatellite(self)

    def operation_options(
        self, config_overrides: Optional[AsyncGroundStationClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncGroundStationClientConfig = config_overrides or {}
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

    async def get_agent_task_response_url(
        self,
        agent_id: "aws_sdk_groundstation.types.uuid.Uuid",
        task_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.get_agent_task_response_url_response.GetAgentTaskResponseUrlResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Gets a presigned URL for uploading agent task response logs.</p>

        Args:
            agent_id: <p>UUID of agent requesting the response URL.</p>
            task_id: <p>GUID of the agent task for which the response URL is being requested.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.get_agent_task_response_url_request.GetAgentTaskResponseUrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.get_agent_task_response_url_response.GetAgentTaskResponseUrlResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.get_agent_task_response_url

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.get_agent_task_response_url.async_get_agent_task_response_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.get_agent_task_response_url_request.GetAgentTaskResponseUrlRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["task_id"] = task_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_minute_usage(
        self,
        month: "aws_sdk_groundstation.types.month.Month",
        year: "aws_sdk_groundstation.types.year.Year",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.get_minute_usage_response.GetMinuteUsageResponse":
        """<p>Returns the number of reserved minutes used by account.</p>

        Args:
            month: <p>The month being requested, with a value of 1-12.</p>
            year: <p>The year being requested, in the format of YYYY.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.get_minute_usage_request.GetMinuteUsageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.get_minute_usage_response.GetMinuteUsageResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.get_minute_usage

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.get_minute_usage.async_get_minute_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.get_minute_usage_request.GetMinuteUsageRequest = {}  # type: ignore[typeddict-item]
        input_["month"] = month
        input_["year"] = year

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_groundstation.types.any_arn.AnyArn",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a specified resource.</p>

        Args:
            resource_arn: <p>ARN of a resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_groundstation.types.any_arn.AnyArn",
        tags: "aws_sdk_groundstation.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns a tag to a resource.</p>

        Args:
            resource_arn: <p>ARN of a resource tag.</p>
            tags: <p>Tags assigned to a resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_groundstation.types.any_arn.AnyArn",
        tag_keys: "aws_sdk_groundstation.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.untag_resource_response.UntagResourceResponse":
        """<p>Deassigns a resource tag.</p>

        Args:
            resource_arn: <p>ARN of a resource.</p>
            tag_keys: <p>Keys of a resource tag.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
