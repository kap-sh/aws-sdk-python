"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#AmplifyUIBuilder``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_amplifyuibuilder._auth._signers
import capo_amplifyuibuilder._auth._sigv4
from capo_amplifyuibuilder._auth._identity import Credentials
from capo_amplifyuibuilder._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_amplifyuibuilder._auth._zapros_handler import AuthMiddleware
from capo_amplifyuibuilder._resources.amplify_ui_builder.codegen_job_resource import (
    AsyncCodegenJobResource,
)
from capo_amplifyuibuilder._resources.amplify_ui_builder.component_resource import (
    AsyncComponentResource,
)
from capo_amplifyuibuilder._resources.amplify_ui_builder.form_resource import (
    AsyncFormResource,
)
from capo_amplifyuibuilder._resources.amplify_ui_builder.theme_resource import (
    AsyncThemeResource,
)
from capo_amplifyuibuilder._services._aws_config import aaws_config
from capo_amplifyuibuilder._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.exchange_code_for_token_request
    import capo_amplifyuibuilder.types.exchange_code_for_token_request_body
    import capo_amplifyuibuilder.types.exchange_code_for_token_response
    import capo_amplifyuibuilder.types.get_metadata_request
    import capo_amplifyuibuilder.types.get_metadata_response
    import capo_amplifyuibuilder.types.list_tags_for_resource_request
    import capo_amplifyuibuilder.types.list_tags_for_resource_response
    import capo_amplifyuibuilder.types.put_metadata_flag_body
    import capo_amplifyuibuilder.types.put_metadata_flag_request
    import capo_amplifyuibuilder.types.refresh_token_request
    import capo_amplifyuibuilder.types.refresh_token_request_body
    import capo_amplifyuibuilder.types.refresh_token_response
    import capo_amplifyuibuilder.types.tag_key_list
    import capo_amplifyuibuilder.types.tag_resource_request
    import capo_amplifyuibuilder.types.tag_resource_response
    import capo_amplifyuibuilder.types.tags
    import capo_amplifyuibuilder.types.token_providers
    import capo_amplifyuibuilder.types.untag_resource_request
    import capo_amplifyuibuilder.types.untag_resource_response


class AsyncAmplifyUIBuilderClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncAmplifyUIBuilderClient:
    """A client for the ``AmplifyUIBuilder`` service.

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
        self._config = AsyncAmplifyUIBuilderClientConfig(
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
        self.codegen_job_resource = AsyncCodegenJobResource(self)
        self.component_resource = AsyncComponentResource(self)
        self.form_resource = AsyncFormResource(self)
        self.theme_resource = AsyncThemeResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAmplifyUIBuilderClientConfig = config_overrides or {}
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

    async def exchange_code_for_token(
        self,
        provider: "capo_amplifyuibuilder.types.token_providers.TokenProviders",
        request: "capo_amplifyuibuilder.types.exchange_code_for_token_request_body.ExchangeCodeForTokenRequestBody",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.exchange_code_for_token_response.ExchangeCodeForTokenResponse":
        """<note> <p>This is for internal use.</p> </note> <p>Amplify uses this action to exchange an access code for a token.</p>

        Args:
            provider: <p>The third-party provider for the token. The only valid value is <code>figma</code>.</p>
            request: <p>Describes the configuration of the request.</p>

        Raises:
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.exchange_code_for_token_request.ExchangeCodeForTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.exchange_code_for_token_response.ExchangeCodeForTokenResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.exchange_code_for_token

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.exchange_code_for_token.async_exchange_code_for_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.exchange_code_for_token_request.ExchangeCodeForTokenRequest = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider
        input_["request"] = request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_metadata(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.get_metadata_response.GetMetadataResponse":
        """<p>Returns existing metadata for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>

        Raises:
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.unauthorized_exception.UnauthorizedException: <p>You don't have permission to perform this operation.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.get_metadata_request.GetMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.get_metadata_response.GetMetadataResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_metadata

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.get_metadata.async_get_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.get_metadata_request.GetMetadataRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a specified Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) to use to list tags.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.unauthorized_exception.UnauthorizedException: <p>You don't have permission to perform this operation.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_metadata_flag(
        self,
        app_id: str,
        environment_name: str,
        feature_name: str,
        body: "capo_amplifyuibuilder.types.put_metadata_flag_body.PutMetadataFlagBody",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> None:
        """<p>Stores the metadata information about a feature on a form.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            feature_name: <p>The name of the feature associated with the metadata.</p>
            body: <p>The metadata information to store.</p>

        Raises:
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.unauthorized_exception.UnauthorizedException: <p>You don't have permission to perform this operation.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.put_metadata_flag_request.PutMetadataFlagRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.put_metadata_flag

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.put_metadata_flag.async_put_metadata_flag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.put_metadata_flag_request.PutMetadataFlagRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["feature_name"] = feature_name
        input_["body"] = body

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def refresh_token(
        self,
        provider: "capo_amplifyuibuilder.types.token_providers.TokenProviders",
        refresh_token_body: "capo_amplifyuibuilder.types.refresh_token_request_body.RefreshTokenRequestBody",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.refresh_token_response.RefreshTokenResponse":
        """<note> <p>This is for internal use.</p> </note> <p>Amplify uses this action to refresh a previously issued access token that might have expired.</p>

        Args:
            provider: <p>The third-party provider for the token. The only valid value is <code>figma</code>.</p>
            refresh_token_body: <p>Information about the refresh token request.</p>

        Raises:
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.refresh_token_request.RefreshTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.refresh_token_response.RefreshTokenResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.refresh_token

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.refresh_token.async_refresh_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.refresh_token_request.RefreshTokenRequest = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider
        input_["refresh_token_body"] = refresh_token_body

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_amplifyuibuilder.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.tag_resource_response.TagResourceResponse":
        """<p>Tags the resource with a tag key and value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) to use to tag a resource.</p>
            tags: <p>A list of tag key value pairs for a specified Amazon Resource Name (ARN).</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.unauthorized_exception.UnauthorizedException: <p>You don't have permission to perform this operation.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.tag_resource

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        tag_keys: "capo_amplifyuibuilder.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.untag_resource_response.UntagResourceResponse":
        """<p>Untags a resource with a specified Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) to use to untag a resource.</p>
            tag_keys: <p>The tag keys to use to untag a resource.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.unauthorized_exception.UnauthorizedException: <p>You don't have permission to perform this operation.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.untag_resource

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
