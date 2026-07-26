"""Generated from Smithy shape ``com.amazonaws.braket#Braket``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_braket._auth._signers
import capo_braket._auth._sigv4
from capo_braket._auth._identity import Credentials
from capo_braket._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_braket._auth._zapros_handler import AuthMiddleware
from capo_braket._resources.braket.device_resource import AsyncDeviceResource
from capo_braket._resources.braket.job_resource import AsyncJobResource
from capo_braket._resources.braket.quantum_task_resource import AsyncQuantumTaskResource
from capo_braket._resources.braket.spending_limit_resource import (
    AsyncSpendingLimitResource,
)
from capo_braket._services._aws_config import aaws_config
from capo_braket._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_braket.types.list_tags_for_resource_request
    import capo_braket.types.list_tags_for_resource_response
    import capo_braket.types.tag_keys
    import capo_braket.types.tag_resource_request
    import capo_braket.types.tag_resource_response
    import capo_braket.types.tags_map
    import capo_braket.types.untag_resource_request
    import capo_braket.types.untag_resource_response


class AsyncBraketClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncBraketClient:
    """A client for the ``Braket`` service.

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
        self._config = AsyncBraketClientConfig(
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
        self.device_resource = AsyncDeviceResource(self)
        self.job_resource = AsyncJobResource(self)
        self.quantum_task_resource = AsyncQuantumTaskResource(self)
        self.spending_limit_resource = AsyncSpendingLimitResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBraketClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBraketClientConfig = config_overrides or {}
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
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> (
        "capo_braket.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Shows the tags associated with this resource.</p>

        Args:
            resource_arn: <p>Specify the <code>resourceArn</code> for the resource whose tags to display.</p>

        Raises:
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_braket._operations.braket.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_braket.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "capo_braket.types.tag_resource_response.TagResourceResponse":
        """<p>Add a tag to the specified resource.</p>

        Args:
            resource_arn: <p>Specify the <code>resourceArn</code> of the resource to which a tag will be added.</p>
            tags: <p>Specify the tags to add to the resource. Tags can be specified as a key-value map.</p>

        Raises:
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_braket._operations.braket.tag_resource

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: str,
        tag_keys: "capo_braket.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "capo_braket.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from a resource.</p>

        Args:
            resource_arn: <p>Specify the <code>resourceArn</code> for the resource from which to remove the tags.</p>
            tag_keys: <p>Specify the keys for the tags to remove from the resource.</p>

        Raises:
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_braket._operations.braket.untag_resource

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_braket.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
