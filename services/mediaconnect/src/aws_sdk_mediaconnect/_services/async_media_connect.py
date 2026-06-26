"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaConnect``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_mediaconnect._auth._signers
import aws_sdk_mediaconnect._auth._sigv4
from aws_sdk_mediaconnect._auth._identity import Credentials
from aws_sdk_mediaconnect._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_mediaconnect._auth._zapros_handler import AuthMiddleware
from aws_sdk_mediaconnect._pagination import resolve_path as _resolve_path
from aws_sdk_mediaconnect._resources.media_connect.bridge_resource import (
    AsyncBridgeResource,
)
from aws_sdk_mediaconnect._resources.media_connect.entitlement_resource import (
    AsyncEntitlementResource,
)
from aws_sdk_mediaconnect._resources.media_connect.flow_media_stream_resource import (
    AsyncFlowMediaStreamResource,
)
from aws_sdk_mediaconnect._resources.media_connect.flow_output_resource import (
    AsyncFlowOutputResource,
)
from aws_sdk_mediaconnect._resources.media_connect.flow_resource import (
    AsyncFlowResource,
)
from aws_sdk_mediaconnect._resources.media_connect.flow_source_resource import (
    AsyncFlowSourceResource,
)
from aws_sdk_mediaconnect._resources.media_connect.flow_vpc_interface_resource import (
    AsyncFlowVpcInterfaceResource,
)
from aws_sdk_mediaconnect._resources.media_connect.gateway_instance_resource import (
    AsyncGatewayInstanceResource,
)
from aws_sdk_mediaconnect._resources.media_connect.gateway_resource import (
    AsyncGatewayResource,
)
from aws_sdk_mediaconnect._resources.media_connect.offering_resource import (
    AsyncOfferingResource,
)
from aws_sdk_mediaconnect._resources.media_connect.reservation_resource import (
    AsyncReservationResource,
)
from aws_sdk_mediaconnect._resources.media_connect.router_input_resource import (
    AsyncRouterInputResource,
)
from aws_sdk_mediaconnect._resources.media_connect.router_network_interface_resource import (
    AsyncRouterNetworkInterfaceResource,
)
from aws_sdk_mediaconnect._resources.media_connect.router_output_resource import (
    AsyncRouterOutputResource,
)
from aws_sdk_mediaconnect._services._aws_config import aaws_config
from aws_sdk_mediaconnect._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_string
    import aws_sdk_mediaconnect.types.__map_of_string
    import aws_sdk_mediaconnect.types.list_entitlements_request
    import aws_sdk_mediaconnect.types.list_entitlements_response
    import aws_sdk_mediaconnect.types.list_tags_for_global_resource_request
    import aws_sdk_mediaconnect.types.list_tags_for_global_resource_response
    import aws_sdk_mediaconnect.types.list_tags_for_resource_request
    import aws_sdk_mediaconnect.types.list_tags_for_resource_response
    import aws_sdk_mediaconnect.types.listed_entitlement
    import aws_sdk_mediaconnect.types.max_results
    import aws_sdk_mediaconnect.types.tag_global_resource_request
    import aws_sdk_mediaconnect.types.tag_resource_request
    import aws_sdk_mediaconnect.types.untag_global_resource_request
    import aws_sdk_mediaconnect.types.untag_resource_request


class AsyncMediaConnectClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncMediaConnectClient:
    """A client for the ``MediaConnect`` service.

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
        self._config = AsyncMediaConnectClientConfig(
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
        self.bridge_resource = AsyncBridgeResource(self)
        self.entitlement_resource = AsyncEntitlementResource(self)
        self.flow_media_stream_resource = AsyncFlowMediaStreamResource(self)
        self.flow_output_resource = AsyncFlowOutputResource(self)
        self.flow_resource = AsyncFlowResource(self)
        self.flow_source_resource = AsyncFlowSourceResource(self)
        self.flow_vpc_interface_resource = AsyncFlowVpcInterfaceResource(self)
        self.gateway_instance_resource = AsyncGatewayInstanceResource(self)
        self.gateway_resource = AsyncGatewayResource(self)
        self.offering_resource = AsyncOfferingResource(self)
        self.reservation_resource = AsyncReservationResource(self)
        self.router_input_resource = AsyncRouterInputResource(self)
        self.router_network_interface_resource = AsyncRouterNetworkInterfaceResource(
            self
        )
        self.router_output_resource = AsyncRouterOutputResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncMediaConnectClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMediaConnectClientConfig = config_overrides or {}
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

    async def list_entitlements(
        self,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediaconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> (
        "aws_sdk_mediaconnect.types.list_entitlements_response.ListEntitlementsResponse"
    ):
        """<p> Displays a list of all entitlements that have been granted to this account. This request returns 20 results per page.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListEntitlements</code> request with set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 20 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListEntitlements</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListEntitlements</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.list_entitlements_request.ListEntitlementsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.list_entitlements_response.ListEntitlementsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_entitlements

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.list_entitlements.async_list_entitlements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.list_entitlements_request.ListEntitlementsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_entitlements(
        self,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediaconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> (
        "AsyncIterator[aws_sdk_mediaconnect.types.listed_entitlement.ListedEntitlement]"
    ):
        _token = next_token
        while True:
            _response = await self.list_entitlements(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entitlements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_global_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.list_tags_for_global_resource_response.ListTagsForGlobalResourceResponse":
        """<p>Lists the tags associated with a global resource in AWS Elemental MediaConnect. The API supports the following global resources: router inputs, router outputs and router network interfaces. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the global resource whose tags you want to list.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.list_tags_for_global_resource_request.ListTagsForGlobalResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.list_tags_for_global_resource_response.ListTagsForGlobalResourceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_tags_for_global_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.list_tags_for_global_resource.async_list_tags_for_global_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.list_tags_for_global_resource_request.ListTagsForGlobalResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

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
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> List all tags on a MediaConnect resource in the current region.</p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) that identifies the MediaConnect resource for which to list the tags.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_global_resource(
        self,
        resource_arn: str,
        tags: "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> None:
        """<p>Adds tags to a global resource in AWS Elemental MediaConnect. The API supports the following global resources: router inputs, router outputs and router network interfaces. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the global resource to tag.</p>
            tags: <p>A map of tag keys and values to add to the global resource.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.tag_global_resource_request.TagGlobalResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_mediaconnect._operations.media_connect.tag_global_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.tag_global_resource.async_tag_global_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.tag_global_resource_request.TagGlobalResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "aws_sdk_mediaconnect.types.__map_of_string.__mapOfString",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> None:
        """<p> Associates the specified tags to a resource with the specified <code>resourceArn</code> in the current region. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well.</p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) that identifies the MediaConnect resource to which to add tags.</p>
            tags: <p> A map from tag keys to values. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_mediaconnect._operations.media_connect.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_global_resource(
        self,
        resource_arn: str,
        tag_keys: "aws_sdk_mediaconnect.types.__list_of_string.__listOfString",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> None:
        """<p>Removes tags from a global resource in AWS Elemental MediaConnect. The API supports the following global resources: router inputs, router outputs and router network interfaces. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the global resource to remove tags from.</p>
            tag_keys: <p>The keys of the tags to remove from the global resource.</p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.untag_global_resource_request.UntagGlobalResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_mediaconnect._operations.media_connect.untag_global_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.untag_global_resource.async_untag_global_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.untag_global_resource_request.UntagGlobalResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: str,
        tag_keys: "aws_sdk_mediaconnect.types.__list_of_string.__listOfString",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> None:
        """<p> Deletes specified tags from a resource in the current region.</p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that you want to untag. </p>
            tag_keys: <p>The keys of the tags to be removed. </p>

        Raises:
            aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            aws_sdk_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            aws_sdk_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_mediaconnect._operations.media_connect.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconnect.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
