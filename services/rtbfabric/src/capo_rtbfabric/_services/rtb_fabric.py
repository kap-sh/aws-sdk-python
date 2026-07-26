"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RTBFabric``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_rtbfabric._auth._signers
import capo_rtbfabric._auth._sigv4
from capo_rtbfabric._auth._identity import Credentials
from capo_rtbfabric._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_rtbfabric._auth._zapros_handler import AuthMiddleware
from capo_rtbfabric._pagination import resolve_path as _resolve_path
from capo_rtbfabric._resources.rtb_fabric.gateway import Gateway
from capo_rtbfabric._resources.rtb_fabric.requester_gateway import RequesterGateway
from capo_rtbfabric._resources.rtb_fabric.responder_gateway import ResponderGateway
from capo_rtbfabric._services._aws_config import aws_config
from capo_rtbfabric._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.list_requester_gateways_request
    import capo_rtbfabric.types.list_requester_gateways_response
    import capo_rtbfabric.types.list_responder_gateways_request
    import capo_rtbfabric.types.list_responder_gateways_response
    import capo_rtbfabric.types.list_tags_for_resource_request
    import capo_rtbfabric.types.list_tags_for_resource_response
    import capo_rtbfabric.types.rtb_taggable_resource_arn
    import capo_rtbfabric.types.tag_key_list
    import capo_rtbfabric.types.tag_resource_request
    import capo_rtbfabric.types.tag_resource_response
    import capo_rtbfabric.types.tags_map
    import capo_rtbfabric.types.untag_resource_request
    import capo_rtbfabric.types.untag_resource_response


class RTBFabricClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class RTBFabricClient:
    """A client for the ``RTBFabric`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = RTBFabricClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.gateway = Gateway(self)
        self.requester_gateway = RequesterGateway(self)
        self.responder_gateway = ResponderGateway(self)

    def operation_options(
        self, config_overrides: Optional[RTBFabricClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: RTBFabricClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_requester_gateways(
        self,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_rtbfabric.types.list_requester_gateways_response.ListRequesterGatewaysResponse":
        """<p>Lists requester gateways.</p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>

        Raises:
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List requester gateways with default pagination
            Lists requester gateways using default pagination settings

            >>> client.list_requester_gateways(max_results=10)
            List requester gateways with pagination token
            Lists requester gateways using a pagination token to get the next page

            >>> client.list_requester_gateways(max_results=5, next_token='eyJsYXN0RXZhbHVhdGVkS2V5Ijp7ImlkIjp7IlMiOiJydGJhcHAtcmVxLTEyMzQ1In19fQ==')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.list_requester_gateways_request.ListRequesterGatewaysRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.list_requester_gateways_response.ListRequesterGatewaysResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_requester_gateways

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.list_requester_gateways.list_requester_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_requester_gateways_request.ListRequesterGatewaysRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_requester_gateways(
        self,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_rtbfabric.types.gateway_id.GatewayId]":
        _token = next_token
        while True:
            _response = self.list_requester_gateways(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("gateway_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_responder_gateways(
        self,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_rtbfabric.types.list_responder_gateways_response.ListResponderGatewaysResponse":
        """<p>Lists reponder gateways.</p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>

        Raises:
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List responder gateways with default pagination
            Lists responder gateways using default pagination settings

            >>> client.list_responder_gateways(max_results=10)
            List responder gateways with pagination token
            Lists responder gateways using a pagination token to get the next page

            >>> client.list_responder_gateways(max_results=3, next_token='eyJsYXN0RXZhbHVhdGVkS2V5Ijp7ImlkIjp7IlMiOiJydGJhcHAtcmVzcC01NDMyMSJ9fX0=')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.list_responder_gateways_request.ListResponderGatewaysRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.list_responder_gateways_response.ListResponderGatewaysResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_responder_gateways

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.list_responder_gateways.list_responder_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_responder_gateways_request.ListResponderGatewaysRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_responder_gateways(
        self,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_rtbfabric.types.gateway_id.GatewayId]":
        _token = next_token
        while True:
            _response = self.list_responder_gateways(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("gateway_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to retrieve tags.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List tags for a resource
            Lists tags for a resource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:rtbfabric:us-east-1:123456789012:gateway/rtb-gw-12345678')
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_tags_for_resource

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn",
        tags: "capo_rtbfabric.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Add tags to a resource
            Adds tags to a resource

            >>> client.tag_resource(resource_arn='arn:aws:rtbfabric:us-east-1:123456789012:gateway/rtb-gw-12345678', tags={'Environment': 'Production', 'Team': 'RTB'})
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.tag_resource

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn",
        tag_keys: "capo_rtbfabric.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The keys of the key-value pairs for the tag or tags you want to remove from the specified resource.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove tags from a resource
            Removes tags from a resource

            >>> client.untag_resource(resource_arn='arn:aws:rtbfabric:us-east-1:123456789012:gateway/rtb-gw-12345678', tag_keys=['Environment', 'Team'])
        """

        def _handler(
            req: "OperationRequest[capo_rtbfabric.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_rtbfabric.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.untag_resource

            output, http_response = (
                capo_rtbfabric._operations.rtb_fabric.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
