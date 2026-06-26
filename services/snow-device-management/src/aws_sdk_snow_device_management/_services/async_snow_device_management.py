"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#SnowDeviceManagement``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_snow_device_management._auth._signers
import aws_sdk_snow_device_management._auth._sigv4
from aws_sdk_snow_device_management._auth._identity import Credentials
from aws_sdk_snow_device_management._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_snow_device_management._auth._zapros_handler import AuthMiddleware
from aws_sdk_snow_device_management._resources.snow_device_management.managed_device import (
    AsyncManagedDevice,
)
from aws_sdk_snow_device_management._resources.snow_device_management.task import (
    AsyncTask,
)
from aws_sdk_snow_device_management._services._aws_config import aaws_config
from aws_sdk_snow_device_management._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.list_tags_for_resource_input
    import aws_sdk_snow_device_management.types.list_tags_for_resource_output
    import aws_sdk_snow_device_management.types.tag_keys
    import aws_sdk_snow_device_management.types.tag_map
    import aws_sdk_snow_device_management.types.tag_resource_input
    import aws_sdk_snow_device_management.types.untag_resource_input


class AsyncSnowDeviceManagementClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSnowDeviceManagementClient:
    """A client for the ``SnowDeviceManagement`` service.

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
        self._config = AsyncSnowDeviceManagementClientConfig(
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
        self.managed_device = AsyncManagedDevice(self)
        self.task = AsyncTask(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSnowDeviceManagementClientConfig = config_overrides or {}
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
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> "aws_sdk_snow_device_management.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns a list of tags for a managed device or task.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the device or task.</p>

        Raises:
            aws_sdk_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            aws_sdk_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_snow_device_management.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
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
        tags: "aws_sdk_snow_device_management.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> None:
        """<p>Adds or replaces tags on a device or task.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the device or task.</p>
            tags: <p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>

        Raises:
            aws_sdk_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            aws_sdk_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_snow_device_management._operations.snow_device_management.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        tag_keys: "aws_sdk_snow_device_management.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> None:
        """<p>Removes a tag from a device or task.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the device or task.</p>
            tag_keys: <p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>

        Raises:
            aws_sdk_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            aws_sdk_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_snow_device_management._operations.snow_device_management.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
