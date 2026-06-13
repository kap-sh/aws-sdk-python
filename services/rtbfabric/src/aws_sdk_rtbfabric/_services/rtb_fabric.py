"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RTBFabric``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_rtbfabric._auth._signers
import aws_sdk_rtbfabric._auth._sigv4
from aws_sdk_rtbfabric._auth._identity import Credentials
from aws_sdk_rtbfabric._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_rtbfabric._auth._zapros_handler import AuthMiddleware
from aws_sdk_rtbfabric._pagination import resolve_path as _resolve_path
from aws_sdk_rtbfabric._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.list_requester_gateways_request
    import aws_sdk_rtbfabric.types.list_requester_gateways_response
    import aws_sdk_rtbfabric.types.list_responder_gateways_request
    import aws_sdk_rtbfabric.types.list_responder_gateways_response
    import aws_sdk_rtbfabric.types.list_tags_for_resource_request
    import aws_sdk_rtbfabric.types.list_tags_for_resource_response
    import aws_sdk_rtbfabric.types.rtb_taggable_resource_arn
    import aws_sdk_rtbfabric.types.tag_key_list
    import aws_sdk_rtbfabric.types.tag_resource_request
    import aws_sdk_rtbfabric.types.tag_resource_response
    import aws_sdk_rtbfabric.types.tags_map
    import aws_sdk_rtbfabric.types.untag_resource_request
    import aws_sdk_rtbfabric.types.untag_resource_response


class RTBFabricClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = RTBFabricClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[RTBFabricClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: RTBFabricClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_requester_gateways(
        self,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_rtbfabric.types.list_requester_gateways_response.ListRequesterGatewaysResponse":
        """<p>Lists requester gateways.</p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>

        Examples:
            List requester gateways with default pagination
            Lists requester gateways using default pagination settings

            >>> client.list_requester_gateways(max_results=10)
            List requester gateways with pagination token
            Lists requester gateways using a pagination token to get the next page

            >>> client.list_requester_gateways(max_results=5, next_token='eyJsYXN0RXZhbHVhdGVkS2V5Ijp7ImlkIjp7IlMiOiJydGJhcHAtcmVxLTEyMzQ1In19fQ==')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.list_requester_gateways_request.ListRequesterGatewaysRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.list_requester_gateways_response.ListRequesterGatewaysResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.list_requester_gateways

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.list_requester_gateways.list_requester_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.list_requester_gateways_request.ListRequesterGatewaysRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
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
    ) -> "Iterator[aws_sdk_rtbfabric.types.gateway_id.GatewayId]":
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
    ) -> "aws_sdk_rtbfabric.types.list_responder_gateways_response.ListResponderGatewaysResponse":
        """<p>Lists reponder gateways.</p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>

        Examples:
            List responder gateways with default pagination
            Lists responder gateways using default pagination settings

            >>> client.list_responder_gateways(max_results=10)
            List responder gateways with pagination token
            Lists responder gateways using a pagination token to get the next page

            >>> client.list_responder_gateways(max_results=3, next_token='eyJsYXN0RXZhbHVhdGVkS2V5Ijp7ImlkIjp7IlMiOiJydGJhcHAtcmVzcC01NDMyMSJ9fX0=')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.list_responder_gateways_request.ListResponderGatewaysRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.list_responder_gateways_response.ListResponderGatewaysResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.list_responder_gateways

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.list_responder_gateways.list_responder_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.list_responder_gateways_request.ListResponderGatewaysRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
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
    ) -> "Iterator[aws_sdk_rtbfabric.types.gateway_id.GatewayId]":
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
        resource_arn: "aws_sdk_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to retrieve tags.</p>

        Examples:
            List tags for a resource
            Lists tags for a resource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:rtbfabric:us-east-1:123456789012:gateway/rtb-gw-12345678')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.list_tags_for_resource

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn",
        tags: "aws_sdk_rtbfabric.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Examples:
            Add tags to a resource
            Adds tags to a resource

            >>> client.tag_resource(resource_arn='arn:aws:rtbfabric:us-east-1:123456789012:gateway/rtb-gw-12345678', tags={'Environment': 'Production', 'Team': 'RTB'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.tag_resource

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn",
        tag_keys: "aws_sdk_rtbfabric.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The keys of the key-value pairs for the tag or tags you want to remove from the specified resource.</p>

        Examples:
            Remove tags from a resource
            Removes tags from a resource

            >>> client.untag_resource(resource_arn='arn:aws:rtbfabric:us-east-1:123456789012:gateway/rtb-gw-12345678', tag_keys=['Environment', 'Team'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.untag_resource

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
