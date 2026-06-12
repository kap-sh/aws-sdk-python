"""Generated from Smithy shape ``com.amazonaws.amplifybackend#AmplifyBackend``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_amplifybackend._auth._signers
import aws_sdk_amplifybackend._auth._sigv4
from aws_sdk_amplifybackend._auth._identity import Credentials
from aws_sdk_amplifybackend._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_amplifybackend._auth._zapros_handler import AuthMiddleware
from aws_sdk_amplifybackend._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__boolean
    import aws_sdk_amplifybackend.types.__integer_min1_max25
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.backend_api_resource_config
    import aws_sdk_amplifybackend.types.clone_backend_request
    import aws_sdk_amplifybackend.types.clone_backend_response
    import aws_sdk_amplifybackend.types.create_backend_api_request
    import aws_sdk_amplifybackend.types.create_backend_api_response
    import aws_sdk_amplifybackend.types.create_backend_auth_request
    import aws_sdk_amplifybackend.types.create_backend_auth_resource_config
    import aws_sdk_amplifybackend.types.create_backend_auth_response
    import aws_sdk_amplifybackend.types.create_backend_config_request
    import aws_sdk_amplifybackend.types.create_backend_config_response
    import aws_sdk_amplifybackend.types.create_backend_request
    import aws_sdk_amplifybackend.types.create_backend_response
    import aws_sdk_amplifybackend.types.create_backend_storage_request
    import aws_sdk_amplifybackend.types.create_backend_storage_resource_config
    import aws_sdk_amplifybackend.types.create_backend_storage_response
    import aws_sdk_amplifybackend.types.create_token_request
    import aws_sdk_amplifybackend.types.create_token_response
    import aws_sdk_amplifybackend.types.delete_backend_api_request
    import aws_sdk_amplifybackend.types.delete_backend_api_response
    import aws_sdk_amplifybackend.types.delete_backend_auth_request
    import aws_sdk_amplifybackend.types.delete_backend_auth_response
    import aws_sdk_amplifybackend.types.delete_backend_request
    import aws_sdk_amplifybackend.types.delete_backend_response
    import aws_sdk_amplifybackend.types.delete_backend_storage_request
    import aws_sdk_amplifybackend.types.delete_backend_storage_response
    import aws_sdk_amplifybackend.types.delete_token_request
    import aws_sdk_amplifybackend.types.delete_token_response
    import aws_sdk_amplifybackend.types.generate_backend_api_models_request
    import aws_sdk_amplifybackend.types.generate_backend_api_models_response
    import aws_sdk_amplifybackend.types.get_backend_api_models_request
    import aws_sdk_amplifybackend.types.get_backend_api_models_response
    import aws_sdk_amplifybackend.types.get_backend_api_request
    import aws_sdk_amplifybackend.types.get_backend_api_response
    import aws_sdk_amplifybackend.types.get_backend_auth_request
    import aws_sdk_amplifybackend.types.get_backend_auth_response
    import aws_sdk_amplifybackend.types.get_backend_job_request
    import aws_sdk_amplifybackend.types.get_backend_job_response
    import aws_sdk_amplifybackend.types.get_backend_request
    import aws_sdk_amplifybackend.types.get_backend_response
    import aws_sdk_amplifybackend.types.get_backend_storage_request
    import aws_sdk_amplifybackend.types.get_backend_storage_response
    import aws_sdk_amplifybackend.types.get_token_request
    import aws_sdk_amplifybackend.types.get_token_response
    import aws_sdk_amplifybackend.types.import_backend_auth_request
    import aws_sdk_amplifybackend.types.import_backend_auth_response
    import aws_sdk_amplifybackend.types.import_backend_storage_request
    import aws_sdk_amplifybackend.types.import_backend_storage_response
    import aws_sdk_amplifybackend.types.list_backend_jobs_request
    import aws_sdk_amplifybackend.types.list_backend_jobs_response
    import aws_sdk_amplifybackend.types.list_s3_buckets_request
    import aws_sdk_amplifybackend.types.list_s3_buckets_response
    import aws_sdk_amplifybackend.types.login_auth_config_req_obj
    import aws_sdk_amplifybackend.types.remove_all_backends_request
    import aws_sdk_amplifybackend.types.remove_all_backends_response
    import aws_sdk_amplifybackend.types.remove_backend_config_request
    import aws_sdk_amplifybackend.types.remove_backend_config_response
    import aws_sdk_amplifybackend.types.resource_config
    import aws_sdk_amplifybackend.types.service_name
    import aws_sdk_amplifybackend.types.update_backend_api_request
    import aws_sdk_amplifybackend.types.update_backend_api_response
    import aws_sdk_amplifybackend.types.update_backend_auth_request
    import aws_sdk_amplifybackend.types.update_backend_auth_resource_config
    import aws_sdk_amplifybackend.types.update_backend_auth_response
    import aws_sdk_amplifybackend.types.update_backend_config_request
    import aws_sdk_amplifybackend.types.update_backend_config_response
    import aws_sdk_amplifybackend.types.update_backend_job_request
    import aws_sdk_amplifybackend.types.update_backend_job_response
    import aws_sdk_amplifybackend.types.update_backend_storage_request
    import aws_sdk_amplifybackend.types.update_backend_storage_resource_config
    import aws_sdk_amplifybackend.types.update_backend_storage_response


class AsyncAmplifyBackendClientConfig(TypedDict, total=False):
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


class AsyncAmplifyBackendClient:
    """A client for the ``AmplifyBackend`` service.

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
        self.config = AsyncAmplifyBackendClientConfig(
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
        self, config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAmplifyBackendClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def clone_backend(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        target_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.clone_backend_response.CloneBackendResponse":
        """<p>This operation clones an existing backend.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            target_environment_name: <p>The name of the destination backend environment to be created.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.clone_backend_request.CloneBackendRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.clone_backend_response.CloneBackendResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.clone_backend

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.clone_backend.async_clone_backend(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.clone_backend_request.CloneBackendRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["target_environment_name"] = target_environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_backend(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        app_name: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        resource_config: Optional[
            "aws_sdk_amplifybackend.types.resource_config.ResourceConfig"
        ] = None,
        resource_name: Optional[
            "aws_sdk_amplifybackend.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_amplifybackend.types.create_backend_response.CreateBackendResponse":
        """<p>This operation creates a backend for an Amplify app. Backends are automatically created at the time of app creation.</p>

        Args:
            app_id: <p>The app ID.</p>
            app_name: <p>The name of the app.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for creating a backend.</p>
            resource_name: <p>The name of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.create_backend_request.CreateBackendRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.create_backend_response.CreateBackendResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.create_backend

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.create_backend.async_create_backend(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.create_backend_request.CreateBackendRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["app_name"] = app_name
        input["backend_environment_name"] = backend_environment_name
        if resource_config is not None:
            input["resource_config"] = resource_config
        if resource_name is not None:
            input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_backend_api(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_config: "aws_sdk_amplifybackend.types.backend_api_resource_config.BackendAPIResourceConfig",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.create_backend_api_response.CreateBackendAPIResponse":
        """<p>Creates a new backend API resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for this request.</p>
            resource_name: <p>The name of this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.create_backend_api_request.CreateBackendAPIRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.create_backend_api_response.CreateBackendAPIResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.create_backend_api

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.create_backend_api.async_create_backend_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.create_backend_api_request.CreateBackendAPIRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_config"] = resource_config
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_backend_auth(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_config: "aws_sdk_amplifybackend.types.create_backend_auth_resource_config.CreateBackendAuthResourceConfig",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.create_backend_auth_response.CreateBackendAuthResponse":
        """<p>Creates a new backend authentication resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for this request object.</p>
            resource_name: <p>The name of this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.create_backend_auth_request.CreateBackendAuthRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.create_backend_auth_response.CreateBackendAuthResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.create_backend_auth

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.create_backend_auth.async_create_backend_auth(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.create_backend_auth_request.CreateBackendAuthRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_config"] = resource_config
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_backend_config(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        backend_manager_app_id: Optional[
            "aws_sdk_amplifybackend.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_amplifybackend.types.create_backend_config_response.CreateBackendConfigResponse":
        """<p>Creates a config object for a backend.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_manager_app_id: <p>The app ID for the backend manager.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.create_backend_config_request.CreateBackendConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.create_backend_config_response.CreateBackendConfigResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.create_backend_config

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.create_backend_config.async_create_backend_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.create_backend_config_request.CreateBackendConfigRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        if backend_manager_app_id is not None:
            input["backend_manager_app_id"] = backend_manager_app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_backend_storage(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_config: "aws_sdk_amplifybackend.types.create_backend_storage_resource_config.CreateBackendStorageResourceConfig",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.create_backend_storage_response.CreateBackendStorageResponse":
        """<p>Creates a backend storage resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for creating backend storage.</p>
            resource_name: <p>The name of the storage resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.create_backend_storage_request.CreateBackendStorageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.create_backend_storage_response.CreateBackendStorageResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.create_backend_storage

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.create_backend_storage.async_create_backend_storage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.create_backend_storage_request.CreateBackendStorageRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_config"] = resource_config
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_token(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.create_token_response.CreateTokenResponse":
        """<p>Generates a one-time challenge code to authenticate a user into your Amplify Admin UI.</p>

        Args:
            app_id: <p>The app ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.create_token_request.CreateTokenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.create_token_response.CreateTokenResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.create_token

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.create_token.async_create_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.create_token_request.CreateTokenRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_backend(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.delete_backend_response.DeleteBackendResponse":
        """<p>Removes an existing environment from your Amplify project.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.delete_backend_request.DeleteBackendRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.delete_backend_response.DeleteBackendResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.delete_backend

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.delete_backend.async_delete_backend(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.delete_backend_request.DeleteBackendRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_backend_api(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        resource_config: Optional[
            "aws_sdk_amplifybackend.types.backend_api_resource_config.BackendAPIResourceConfig"
        ] = None,
    ) -> "aws_sdk_amplifybackend.types.delete_backend_api_response.DeleteBackendAPIResponse":
        """<p>Deletes an existing backend API resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>Defines the resource configuration for the data model in your Amplify project.</p>
            resource_name: <p>The name of this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.delete_backend_api_request.DeleteBackendAPIRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.delete_backend_api_response.DeleteBackendAPIResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.delete_backend_api

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.delete_backend_api.async_delete_backend_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.delete_backend_api_request.DeleteBackendAPIRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        if resource_config is not None:
            input["resource_config"] = resource_config
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_backend_auth(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.delete_backend_auth_response.DeleteBackendAuthResponse":
        """<p>Deletes an existing backend authentication resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.delete_backend_auth_request.DeleteBackendAuthRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.delete_backend_auth_response.DeleteBackendAuthResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.delete_backend_auth

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.delete_backend_auth.async_delete_backend_auth(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.delete_backend_auth_request.DeleteBackendAuthRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_backend_storage(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        service_name: "aws_sdk_amplifybackend.types.service_name.ServiceName",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.delete_backend_storage_response.DeleteBackendStorageResponse":
        """<p>Removes the specified backend storage resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of the storage resource.</p>
            service_name: <p>The name of the storage service.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.delete_backend_storage_request.DeleteBackendStorageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.delete_backend_storage_response.DeleteBackendStorageResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.delete_backend_storage

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.delete_backend_storage.async_delete_backend_storage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.delete_backend_storage_request.DeleteBackendStorageRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_name"] = resource_name
        input["service_name"] = service_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_token(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        session_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.delete_token_response.DeleteTokenResponse":
        """<p>Deletes the challenge token based on the given appId and sessionId.</p>

        Args:
            app_id: <p>The app ID.</p>
            session_id: <p>The session ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.delete_token_request.DeleteTokenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.delete_token_response.DeleteTokenResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.delete_token

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.delete_token.async_delete_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.delete_token_request.DeleteTokenRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["session_id"] = session_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def generate_backend_api_models(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.generate_backend_api_models_response.GenerateBackendAPIModelsResponse":
        """<p>Generates a model schema for an existing backend API resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.generate_backend_api_models_request.GenerateBackendAPIModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.generate_backend_api_models_response.GenerateBackendAPIModelsResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.generate_backend_api_models

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.generate_backend_api_models.async_generate_backend_api_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.generate_backend_api_models_request.GenerateBackendAPIModelsRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_backend(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        backend_environment_name: Optional[
            "aws_sdk_amplifybackend.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_amplifybackend.types.get_backend_response.GetBackendResponse":
        """<p>Provides project-level details for your Amplify UI project.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.get_backend_request.GetBackendRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.get_backend_response.GetBackendResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.get_backend

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.get_backend.async_get_backend(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.get_backend_request.GetBackendRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        if backend_environment_name is not None:
            input["backend_environment_name"] = backend_environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_backend_api(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        resource_config: Optional[
            "aws_sdk_amplifybackend.types.backend_api_resource_config.BackendAPIResourceConfig"
        ] = None,
    ) -> "aws_sdk_amplifybackend.types.get_backend_api_response.GetBackendAPIResponse":
        """<p>Gets the details for a backend API.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>Defines the resource configuration for the data model in your Amplify project.</p>
            resource_name: <p>The name of this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.get_backend_api_request.GetBackendAPIRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.get_backend_api_response.GetBackendAPIResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.get_backend_api

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.get_backend_api.async_get_backend_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.get_backend_api_request.GetBackendAPIRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        if resource_config is not None:
            input["resource_config"] = resource_config
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_backend_api_models(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.get_backend_api_models_response.GetBackendAPIModelsResponse":
        """<p>Gets a model introspection schema for an existing backend API resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.get_backend_api_models_request.GetBackendAPIModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.get_backend_api_models_response.GetBackendAPIModelsResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.get_backend_api_models

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.get_backend_api_models.async_get_backend_api_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.get_backend_api_models_request.GetBackendAPIModelsRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_backend_auth(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> (
        "aws_sdk_amplifybackend.types.get_backend_auth_response.GetBackendAuthResponse"
    ):
        """<p>Gets a backend auth details.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.get_backend_auth_request.GetBackendAuthRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.get_backend_auth_response.GetBackendAuthResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.get_backend_auth

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.get_backend_auth.async_get_backend_auth(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.get_backend_auth_request.GetBackendAuthRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_backend_job(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        job_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.get_backend_job_response.GetBackendJobResponse":
        """<p>Returns information about a specific job.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            job_id: <p>The ID for the job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.get_backend_job_request.GetBackendJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.get_backend_job_response.GetBackendJobResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.get_backend_job

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.get_backend_job.async_get_backend_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.get_backend_job_request.GetBackendJobRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_backend_storage(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.get_backend_storage_response.GetBackendStorageResponse":
        """<p>Gets details for a backend storage resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of the storage resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.get_backend_storage_request.GetBackendStorageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.get_backend_storage_response.GetBackendStorageResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.get_backend_storage

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.get_backend_storage.async_get_backend_storage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.get_backend_storage_request.GetBackendStorageRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_token(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        session_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.get_token_response.GetTokenResponse":
        """<p>Gets the challenge token based on the given appId and sessionId.</p>

        Args:
            app_id: <p>The app ID.</p>
            session_id: <p>The session ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.get_token_request.GetTokenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.get_token_response.GetTokenResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.get_token

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.get_token.async_get_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.get_token_request.GetTokenRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["session_id"] = session_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_backend_auth(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        native_client_id: "aws_sdk_amplifybackend.types.__string.__string",
        user_pool_id: "aws_sdk_amplifybackend.types.__string.__string",
        web_client_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        identity_pool_id: Optional[
            "aws_sdk_amplifybackend.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_amplifybackend.types.import_backend_auth_response.ImportBackendAuthResponse":
        """<p>Imports an existing backend authentication resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            identity_pool_id: <p>The ID of the Amazon Cognito identity pool.</p>
            native_client_id: <p>The ID of the Amazon Cognito native client.</p>
            user_pool_id: <p>The ID of the Amazon Cognito user pool.</p>
            web_client_id: <p>The ID of the Amazon Cognito web client.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.import_backend_auth_request.ImportBackendAuthRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.import_backend_auth_response.ImportBackendAuthResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.import_backend_auth

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.import_backend_auth.async_import_backend_auth(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.import_backend_auth_request.ImportBackendAuthRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        if identity_pool_id is not None:
            input["identity_pool_id"] = identity_pool_id
        input["native_client_id"] = native_client_id
        input["user_pool_id"] = user_pool_id
        input["web_client_id"] = web_client_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_backend_storage(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        service_name: "aws_sdk_amplifybackend.types.service_name.ServiceName",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        bucket_name: Optional["aws_sdk_amplifybackend.types.__string.__string"] = None,
    ) -> "aws_sdk_amplifybackend.types.import_backend_storage_response.ImportBackendStorageResponse":
        """<p>Imports an existing backend storage resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            bucket_name: <p>The name of the S3 bucket.</p>
            service_name: <p>The name of the storage service.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.import_backend_storage_request.ImportBackendStorageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.import_backend_storage_response.ImportBackendStorageResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.import_backend_storage

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.import_backend_storage.async_import_backend_storage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.import_backend_storage_request.ImportBackendStorageRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        if bucket_name is not None:
            input["bucket_name"] = bucket_name
        input["service_name"] = service_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_backend_jobs(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        job_id: Optional["aws_sdk_amplifybackend.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_amplifybackend.types.__integer_min1_max25.__integerMin1Max25"
        ] = None,
        next_token: Optional["aws_sdk_amplifybackend.types.__string.__string"] = None,
        operation: Optional["aws_sdk_amplifybackend.types.__string.__string"] = None,
        status: Optional["aws_sdk_amplifybackend.types.__string.__string"] = None,
    ) -> "aws_sdk_amplifybackend.types.list_backend_jobs_response.ListBackendJobsResponse":
        """<p>Lists the jobs for the backend of an Amplify app.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            job_id: <p>The ID for the job.</p>
            max_results: <p>The maximum number of results that you want in the response.</p>
            next_token: <p>The token for the next set of results.</p>
            operation: <p>Filters the list of response objects to include only those with the specified operation name.</p>
            status: <p>Filters the list of response objects to include only those with the specified status.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.list_backend_jobs_request.ListBackendJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.list_backend_jobs_response.ListBackendJobsResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.list_backend_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.list_backend_jobs.async_list_backend_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.list_backend_jobs_request.ListBackendJobsRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        if job_id is not None:
            input["job_id"] = job_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if operation is not None:
            input["operation"] = operation
        if status is not None:
            input["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_s3_buckets(
        self,
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        next_token: Optional["aws_sdk_amplifybackend.types.__string.__string"] = None,
    ) -> "aws_sdk_amplifybackend.types.list_s3_buckets_response.ListS3BucketsResponse":
        """<p>The list of S3 buckets in your account.</p>

        Args:
            next_token: <p>Reserved for future use.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.list_s3_buckets_request.ListS3BucketsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.list_s3_buckets_response.ListS3BucketsResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.list_s3_buckets

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.list_s3_buckets.async_list_s3_buckets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.list_s3_buckets_request.ListS3BucketsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_all_backends(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        clean_amplify_app: Optional[
            "aws_sdk_amplifybackend.types.__boolean.__boolean"
        ] = None,
    ) -> "aws_sdk_amplifybackend.types.remove_all_backends_response.RemoveAllBackendsResponse":
        """<p>Removes all backend environments from your Amplify project.</p>

        Args:
            app_id: <p>The app ID.</p>
            clean_amplify_app: <p>Cleans up the Amplify Console app if this value is set to true.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.remove_all_backends_request.RemoveAllBackendsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.remove_all_backends_response.RemoveAllBackendsResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.remove_all_backends

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.remove_all_backends.async_remove_all_backends(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.remove_all_backends_request.RemoveAllBackendsRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        if clean_amplify_app is not None:
            input["clean_amplify_app"] = clean_amplify_app

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_backend_config(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.remove_backend_config_response.RemoveBackendConfigResponse":
        """<p>Removes the AWS resources required to access the Amplify Admin UI.</p>

        Args:
            app_id: <p>The app ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.remove_backend_config_request.RemoveBackendConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.remove_backend_config_response.RemoveBackendConfigResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.remove_backend_config

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.remove_backend_config.async_remove_backend_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.remove_backend_config_request.RemoveBackendConfigRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_backend_api(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        resource_config: Optional[
            "aws_sdk_amplifybackend.types.backend_api_resource_config.BackendAPIResourceConfig"
        ] = None,
    ) -> "aws_sdk_amplifybackend.types.update_backend_api_response.UpdateBackendAPIResponse":
        """<p>Updates an existing backend API resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>Defines the resource configuration for the data model in your Amplify project.</p>
            resource_name: <p>The name of this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.update_backend_api_request.UpdateBackendAPIRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.update_backend_api_response.UpdateBackendAPIResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.update_backend_api

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.update_backend_api.async_update_backend_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.update_backend_api_request.UpdateBackendAPIRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        if resource_config is not None:
            input["resource_config"] = resource_config
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_backend_auth(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_config: "aws_sdk_amplifybackend.types.update_backend_auth_resource_config.UpdateBackendAuthResourceConfig",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.update_backend_auth_response.UpdateBackendAuthResponse":
        """<p>Updates an existing backend authentication resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for this request object.</p>
            resource_name: <p>The name of this resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.update_backend_auth_request.UpdateBackendAuthRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.update_backend_auth_response.UpdateBackendAuthResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.update_backend_auth

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.update_backend_auth.async_update_backend_auth(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.update_backend_auth_request.UpdateBackendAuthRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_config"] = resource_config
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_backend_config(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        login_auth_config: Optional[
            "aws_sdk_amplifybackend.types.login_auth_config_req_obj.LoginAuthConfigReqObj"
        ] = None,
    ) -> "aws_sdk_amplifybackend.types.update_backend_config_response.UpdateBackendConfigResponse":
        """<p>Updates the AWS resources required to access the Amplify Admin UI.</p>

        Args:
            app_id: <p>The app ID.</p>
            login_auth_config: <p>Describes the Amazon Cognito configuration for Admin UI access.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.update_backend_config_request.UpdateBackendConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.update_backend_config_response.UpdateBackendConfigResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.update_backend_config

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.update_backend_config.async_update_backend_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.update_backend_config_request.UpdateBackendConfigRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        if login_auth_config is not None:
            input["login_auth_config"] = login_auth_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_backend_job(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        job_id: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
        operation: Optional["aws_sdk_amplifybackend.types.__string.__string"] = None,
        status: Optional["aws_sdk_amplifybackend.types.__string.__string"] = None,
    ) -> "aws_sdk_amplifybackend.types.update_backend_job_response.UpdateBackendJobResponse":
        """<p>Updates a specific job.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            job_id: <p>The ID for the job.</p>
            operation: <p>Filters the list of response objects to include only those with the specified operation name.</p>
            status: <p>Filters the list of response objects to include only those with the specified status.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.update_backend_job_request.UpdateBackendJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.update_backend_job_response.UpdateBackendJobResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.update_backend_job

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.update_backend_job.async_update_backend_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.update_backend_job_request.UpdateBackendJobRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["job_id"] = job_id
        if operation is not None:
            input["operation"] = operation
        if status is not None:
            input["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_backend_storage(
        self,
        app_id: "aws_sdk_amplifybackend.types.__string.__string",
        backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string",
        resource_config: "aws_sdk_amplifybackend.types.update_backend_storage_resource_config.UpdateBackendStorageResourceConfig",
        resource_name: "aws_sdk_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AsyncAmplifyBackendClientConfig] = None,
    ) -> "aws_sdk_amplifybackend.types.update_backend_storage_response.UpdateBackendStorageResponse":
        """<p>Updates an existing backend storage resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for updating backend storage.</p>
            resource_name: <p>The name of the storage resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifybackend.types.update_backend_storage_request.UpdateBackendStorageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifybackend.types.update_backend_storage_response.UpdateBackendStorageResponse"
        ]:
            import aws_sdk_amplifybackend._operations.amplify_backend.update_backend_storage

            (
                output,
                http_response,
            ) = await aws_sdk_amplifybackend._operations.amplify_backend.update_backend_storage.async_update_backend_storage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_amplifybackend.types.update_backend_storage_request.UpdateBackendStorageRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["backend_environment_name"] = backend_environment_name
        input["resource_config"] = resource_config
        input["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
