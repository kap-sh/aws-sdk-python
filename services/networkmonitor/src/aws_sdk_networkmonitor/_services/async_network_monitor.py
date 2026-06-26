"""Generated from Smithy shape ``com.amazonaws.networkmonitor#NetworkMonitor``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_networkmonitor._auth._signers
import aws_sdk_networkmonitor._auth._sigv4
from aws_sdk_networkmonitor._auth._identity import Credentials
from aws_sdk_networkmonitor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_networkmonitor._auth._zapros_handler import AuthMiddleware
from aws_sdk_networkmonitor._resources.network_monitor.monitor_resource import (
    AsyncMonitorResource,
)
from aws_sdk_networkmonitor._resources.network_monitor.probe_resource import (
    AsyncProbeResource,
)
from aws_sdk_networkmonitor._services._aws_config import aaws_config
from aws_sdk_networkmonitor._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.arn
    import aws_sdk_networkmonitor.types.list_tags_for_resource_input
    import aws_sdk_networkmonitor.types.list_tags_for_resource_output
    import aws_sdk_networkmonitor.types.tag_key_list
    import aws_sdk_networkmonitor.types.tag_map
    import aws_sdk_networkmonitor.types.tag_resource_input
    import aws_sdk_networkmonitor.types.tag_resource_output
    import aws_sdk_networkmonitor.types.untag_resource_input
    import aws_sdk_networkmonitor.types.untag_resource_output


class AsyncNetworkMonitorClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncNetworkMonitorClient:
    """A client for the ``NetworkMonitor`` service.

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
        self._config = AsyncNetworkMonitorClientConfig(
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

        # resources
        self.monitor_resource = AsyncMonitorResource(self)
        self.probe_resource = AsyncProbeResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncNetworkMonitorClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_networkmonitor.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags assigned to this resource.</p>

        Args:
            resource_arn: <p>The </p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_networkmonitor.types.arn.Arn",
        tags: "aws_sdk_networkmonitor.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.tag_resource_output.TagResourceOutput":
        """<p>Adds key-value pairs to a monitor or probe.</p>

        Args:
            resource_arn: <p>The ARN of the monitor or probe to tag.</p>
            tags: <p>The list of key-value pairs assigned to the monitor or probe.</p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_networkmonitor.types.arn.Arn",
        tag_keys: "aws_sdk_networkmonitor.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a key-value pair from a monitor or probe.</p>

        Args:
            resource_arn: <p>The ARN of the monitor or probe that the tag should be removed from. </p>
            tag_keys: <p>The key-value pa</p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
