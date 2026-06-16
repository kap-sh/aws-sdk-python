"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#NetworkFlowMonitor``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_networkflowmonitor._auth._signers
import aws_sdk_networkflowmonitor._auth._sigv4
from aws_sdk_networkflowmonitor._auth._identity import Credentials
from aws_sdk_networkflowmonitor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_networkflowmonitor._auth._zapros_handler import AuthMiddleware
from aws_sdk_networkflowmonitor._resources.network_flow_monitor.monitor_resource import (
    AsyncMonitorResource,
)
from aws_sdk_networkflowmonitor._resources.network_flow_monitor.scope_resource import (
    AsyncScopeResource,
)
from aws_sdk_networkflowmonitor._services._aws_config import aaws_config
from aws_sdk_networkflowmonitor._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.arn
    import aws_sdk_networkflowmonitor.types.list_tags_for_resource_input
    import aws_sdk_networkflowmonitor.types.list_tags_for_resource_output
    import aws_sdk_networkflowmonitor.types.tag_key_list
    import aws_sdk_networkflowmonitor.types.tag_map
    import aws_sdk_networkflowmonitor.types.tag_resource_input
    import aws_sdk_networkflowmonitor.types.tag_resource_output
    import aws_sdk_networkflowmonitor.types.untag_resource_input
    import aws_sdk_networkflowmonitor.types.untag_resource_output


class AsyncNetworkFlowMonitorClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncNetworkFlowMonitorClient:
    """A client for the ``NetworkFlowMonitor`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncNetworkFlowMonitorClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.monitor_resource = AsyncMonitorResource(self)
        self.scope_resource = AsyncScopeResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncNetworkFlowMonitorClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_networkflowmonitor.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "aws_sdk_networkflowmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns all the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkflowmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkflowmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_networkflowmonitor._operations.network_flow_monitor.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_networkflowmonitor._operations.network_flow_monitor.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_networkflowmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_networkflowmonitor.types.arn.Arn",
        tags: "aws_sdk_networkflowmonitor.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "aws_sdk_networkflowmonitor.types.tag_resource_output.TagResourceOutput":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags for a resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkflowmonitor.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkflowmonitor.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_networkflowmonitor._operations.network_flow_monitor.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_networkflowmonitor._operations.network_flow_monitor.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_networkflowmonitor.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_networkflowmonitor.types.arn.Arn",
        tag_keys: "aws_sdk_networkflowmonitor.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "aws_sdk_networkflowmonitor.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>Keys that you specified when you tagged a resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkflowmonitor.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkflowmonitor.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_networkflowmonitor._operations.network_flow_monitor.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_networkflowmonitor._operations.network_flow_monitor.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_networkflowmonitor.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
