"""Generated from Smithy shape ``com.amazonaws.appmesh#AppMesh``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_app_mesh._auth._signers
import capo_app_mesh._auth._sigv4
from capo_app_mesh._auth._identity import Credentials
from capo_app_mesh._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_app_mesh._auth._zapros_handler import AuthMiddleware
from capo_app_mesh._pagination import resolve_path as _resolve_path
from capo_app_mesh._resources.app_mesh.mesh import AsyncMesh
from capo_app_mesh._services._aws_config import aaws_config
from capo_app_mesh._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_app_mesh.types.arn
    import capo_app_mesh.types.list_tags_for_resource_input
    import capo_app_mesh.types.list_tags_for_resource_output
    import capo_app_mesh.types.tag_key_list
    import capo_app_mesh.types.tag_list
    import capo_app_mesh.types.tag_ref
    import capo_app_mesh.types.tag_resource_input
    import capo_app_mesh.types.tag_resource_output
    import capo_app_mesh.types.tags_limit
    import capo_app_mesh.types.untag_resource_input
    import capo_app_mesh.types.untag_resource_output


class AsyncAppMeshClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncAppMeshClient:
    """A client for the ``AppMesh`` service.

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
        self._config = AsyncAppMeshClientConfig(
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
        self.mesh = AsyncMesh(self)

    def operation_options(
        self, config_overrides: Optional[AsyncAppMeshClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAppMeshClientConfig = config_overrides or {}
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
        resource_arn: "capo_app_mesh.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["capo_app_mesh.types.tags_limit.TagsLimit"] = None,
    ) -> "capo_app_mesh.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List the tags for an App Mesh resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListTagsForResource</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>
            limit: <p>The maximum number of tag results returned by <code>ListTagsForResource</code> in paginated output. When this parameter is used, <code>ListTagsForResource</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListTagsForResource</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListTagsForResource</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_app_mesh.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_app_mesh.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_app_mesh._operations.app_mesh.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_app_mesh.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["capo_app_mesh.types.tags_limit.TagsLimit"] = None,
    ) -> "AsyncIterator[capo_app_mesh.types.tag_ref.TagRef]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def tag_resource(
        self,
        resource_arn: "capo_app_mesh.types.arn.Arn",
        tags: "capo_app_mesh.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
    ) -> "capo_app_mesh.types.tag_resource_output.TagResourceOutput":
        """<p>Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource aren't specified in the request parameters, they aren't changed. When a resource is deleted, the tags associated with that resource are also deleted.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeds the maximum allowed number of tags allowed per resource. The current limit is 50 user tags per resource. You must reduce the number of tags in the request. None of the tags in this request were applied.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_app_mesh.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_app_mesh.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.tag_resource

            (
                output,
                http_response,
            ) = await capo_app_mesh._operations.app_mesh.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "capo_app_mesh.types.arn.Arn",
        tag_keys: "capo_app_mesh.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
    ) -> "capo_app_mesh.types.untag_resource_output.UntagResourceOutput":
        """<p>Deletes specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to delete tags from.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_app_mesh.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_app_mesh.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.untag_resource

            (
                output,
                http_response,
            ) = await capo_app_mesh._operations.app_mesh.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
