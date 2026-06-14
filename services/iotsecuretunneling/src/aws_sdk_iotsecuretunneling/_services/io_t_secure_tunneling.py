"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#IoTSecuredTunneling``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_iotsecuretunneling._auth._signers
import aws_sdk_iotsecuretunneling._auth._sigv4
from aws_sdk_iotsecuretunneling._auth._identity import Credentials
from aws_sdk_iotsecuretunneling._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_iotsecuretunneling._auth._zapros_handler import AuthMiddleware
from aws_sdk_iotsecuretunneling._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.amazon_resource_name
    import aws_sdk_iotsecuretunneling.types.client_mode
    import aws_sdk_iotsecuretunneling.types.close_tunnel_request
    import aws_sdk_iotsecuretunneling.types.close_tunnel_response
    import aws_sdk_iotsecuretunneling.types.delete_flag
    import aws_sdk_iotsecuretunneling.types.describe_tunnel_request
    import aws_sdk_iotsecuretunneling.types.describe_tunnel_response
    import aws_sdk_iotsecuretunneling.types.description
    import aws_sdk_iotsecuretunneling.types.destination_config
    import aws_sdk_iotsecuretunneling.types.list_tags_for_resource_request
    import aws_sdk_iotsecuretunneling.types.list_tags_for_resource_response
    import aws_sdk_iotsecuretunneling.types.list_tunnels_request
    import aws_sdk_iotsecuretunneling.types.list_tunnels_response
    import aws_sdk_iotsecuretunneling.types.max_results
    import aws_sdk_iotsecuretunneling.types.next_token
    import aws_sdk_iotsecuretunneling.types.open_tunnel_request
    import aws_sdk_iotsecuretunneling.types.open_tunnel_response
    import aws_sdk_iotsecuretunneling.types.rotate_tunnel_access_token_request
    import aws_sdk_iotsecuretunneling.types.rotate_tunnel_access_token_response
    import aws_sdk_iotsecuretunneling.types.tag_key_list
    import aws_sdk_iotsecuretunneling.types.tag_list
    import aws_sdk_iotsecuretunneling.types.tag_resource_request
    import aws_sdk_iotsecuretunneling.types.tag_resource_response
    import aws_sdk_iotsecuretunneling.types.thing_name
    import aws_sdk_iotsecuretunneling.types.timeout_config
    import aws_sdk_iotsecuretunneling.types.tunnel_id
    import aws_sdk_iotsecuretunneling.types.untag_resource_request
    import aws_sdk_iotsecuretunneling.types.untag_resource_response


class IoTSecureTunnelingClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class IoTSecureTunnelingClient:
    """A client for the ``IoTSecureTunneling`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self.config = IoTSecureTunnelingClientConfig(
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
        self, config_overrides: Optional[IoTSecureTunnelingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: IoTSecureTunnelingClientConfig = config_overrides or {}
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

    def close_tunnel(
        self,
        tunnel_id: "aws_sdk_iotsecuretunneling.types.tunnel_id.TunnelId",
        *,
        config_overrides: Optional[IoTSecureTunnelingClientConfig] = None,
        delete: Optional[
            "aws_sdk_iotsecuretunneling.types.delete_flag.DeleteFlag"
        ] = None,
    ) -> "aws_sdk_iotsecuretunneling.types.close_tunnel_response.CloseTunnelResponse":
        """<p>Closes a tunnel identified by the unique tunnel id. When a <code>CloseTunnel</code> request is received, we close the WebSocket connections between the client and proxy server so no data can be transmitted.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">CloseTunnel</a> action.</p>

        Args:
            tunnel_id: <p>The ID of the tunnel to close.</p>
            delete: <p>When set to true, IoT Secure Tunneling deletes the tunnel data immediately.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotsecuretunneling.types.close_tunnel_request.CloseTunnelRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotsecuretunneling.types.close_tunnel_response.CloseTunnelResponse"
        ]:
            import aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.close_tunnel

            output, http_response = (
                aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.close_tunnel.close_tunnel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsecuretunneling.types.close_tunnel_request.CloseTunnelRequest = {}  # type: ignore[typeddict-item]
        input_["tunnel_id"] = tunnel_id
        if delete is not None:
            input_["delete"] = delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_tunnel(
        self,
        tunnel_id: "aws_sdk_iotsecuretunneling.types.tunnel_id.TunnelId",
        *,
        config_overrides: Optional[IoTSecureTunnelingClientConfig] = None,
    ) -> "aws_sdk_iotsecuretunneling.types.describe_tunnel_response.DescribeTunnelResponse":
        """<p>Gets information about a tunnel identified by the unique tunnel id.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">DescribeTunnel</a> action.</p>

        Args:
            tunnel_id: <p>The tunnel to describe.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotsecuretunneling.types.describe_tunnel_request.DescribeTunnelRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotsecuretunneling.types.describe_tunnel_response.DescribeTunnelResponse"
        ]:
            import aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.describe_tunnel

            output, http_response = (
                aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.describe_tunnel.describe_tunnel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsecuretunneling.types.describe_tunnel_request.DescribeTunnelRequest = {}  # type: ignore[typeddict-item]
        input_["tunnel_id"] = tunnel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_iotsecuretunneling.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[IoTSecureTunnelingClientConfig] = None,
    ) -> "aws_sdk_iotsecuretunneling.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotsecuretunneling.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotsecuretunneling.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.list_tags_for_resource

            output, http_response = (
                aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsecuretunneling.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tunnels(
        self,
        *,
        config_overrides: Optional[IoTSecureTunnelingClientConfig] = None,
        thing_name: Optional[
            "aws_sdk_iotsecuretunneling.types.thing_name.ThingName"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotsecuretunneling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_iotsecuretunneling.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_iotsecuretunneling.types.list_tunnels_response.ListTunnelsResponse":
        """<p>List all tunnels for an Amazon Web Services account. Tunnels are listed by creation time in descending order, newer tunnels will be listed before older tunnels.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">ListTunnels</a> action.</p>

        Args:
            thing_name: <p>The name of the IoT thing associated with the destination device.</p>
            max_results: <p>The maximum number of results to return at once.</p>
            next_token: <p>To retrieve the next set of results, the nextToken value from a previous response; otherwise null to receive the first set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotsecuretunneling.types.list_tunnels_request.ListTunnelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotsecuretunneling.types.list_tunnels_response.ListTunnelsResponse"
        ]:
            import aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.list_tunnels

            output, http_response = (
                aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.list_tunnels.list_tunnels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsecuretunneling.types.list_tunnels_request.ListTunnelsRequest = {}  # type: ignore[typeddict-item]
        if thing_name is not None:
            input_["thing_name"] = thing_name
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

    def open_tunnel(
        self,
        *,
        config_overrides: Optional[IoTSecureTunnelingClientConfig] = None,
        description: Optional[
            "aws_sdk_iotsecuretunneling.types.description.Description"
        ] = None,
        tags: Optional["aws_sdk_iotsecuretunneling.types.tag_list.TagList"] = None,
        destination_config: Optional[
            "aws_sdk_iotsecuretunneling.types.destination_config.DestinationConfig"
        ] = None,
        timeout_config: Optional[
            "aws_sdk_iotsecuretunneling.types.timeout_config.TimeoutConfig"
        ] = None,
    ) -> "aws_sdk_iotsecuretunneling.types.open_tunnel_response.OpenTunnelResponse":
        """<p>Creates a new tunnel, and returns two client access tokens for clients to use to connect to the IoT Secure Tunneling proxy server.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">OpenTunnel</a> action.</p>

        Args:
            description: <p>A short text description of the tunnel. </p>
            tags: <p>A collection of tag metadata.</p>
            destination_config: <p>The destination configuration for the OpenTunnel request.</p>
            timeout_config: <p>Timeout configuration for a tunnel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotsecuretunneling.types.open_tunnel_request.OpenTunnelRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotsecuretunneling.types.open_tunnel_response.OpenTunnelResponse"
        ]:
            import aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.open_tunnel

            output, http_response = (
                aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.open_tunnel.open_tunnel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsecuretunneling.types.open_tunnel_request.OpenTunnelRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if destination_config is not None:
            input_["destination_config"] = destination_config
        if timeout_config is not None:
            input_["timeout_config"] = timeout_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def rotate_tunnel_access_token(
        self,
        tunnel_id: "aws_sdk_iotsecuretunneling.types.tunnel_id.TunnelId",
        client_mode: "aws_sdk_iotsecuretunneling.types.client_mode.ClientMode",
        *,
        config_overrides: Optional[IoTSecureTunnelingClientConfig] = None,
        destination_config: Optional[
            "aws_sdk_iotsecuretunneling.types.destination_config.DestinationConfig"
        ] = None,
    ) -> "aws_sdk_iotsecuretunneling.types.rotate_tunnel_access_token_response.RotateTunnelAccessTokenResponse":
        """<p>Revokes the current client access token (CAT) and returns new CAT for clients to use when reconnecting to secure tunneling to access the same tunnel.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">RotateTunnelAccessToken</a> action.</p> <note> <p>Rotating the CAT doesn't extend the tunnel duration. For example, say the tunnel duration is 12 hours and the tunnel has already been open for 4 hours. When you rotate the access tokens, the new tokens that are generated can only be used for the remaining 8 hours.</p> </note>

        Args:
            tunnel_id: <p>The tunnel for which you want to rotate the access tokens.</p>
            client_mode: <p>The mode of the client that will use the client token, which can be either the source or destination, or both source and destination.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotsecuretunneling.types.rotate_tunnel_access_token_request.RotateTunnelAccessTokenRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotsecuretunneling.types.rotate_tunnel_access_token_response.RotateTunnelAccessTokenResponse"
        ]:
            import aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.rotate_tunnel_access_token

            output, http_response = (
                aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.rotate_tunnel_access_token.rotate_tunnel_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsecuretunneling.types.rotate_tunnel_access_token_request.RotateTunnelAccessTokenRequest = {}  # type: ignore[typeddict-item]
        input_["tunnel_id"] = tunnel_id
        input_["client_mode"] = client_mode
        if destination_config is not None:
            input_["destination_config"] = destination_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_iotsecuretunneling.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_iotsecuretunneling.types.tag_list.TagList",
        *,
        config_overrides: Optional[IoTSecureTunnelingClientConfig] = None,
    ) -> "aws_sdk_iotsecuretunneling.types.tag_resource_response.TagResourceResponse":
        """<p>A resource tag.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>The tags for the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotsecuretunneling.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotsecuretunneling.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.tag_resource

            output, http_response = (
                aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsecuretunneling.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_iotsecuretunneling.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_iotsecuretunneling.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[IoTSecureTunnelingClientConfig] = None,
    ) -> (
        "aws_sdk_iotsecuretunneling.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tag_keys: <p>The keys of the tags to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotsecuretunneling.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotsecuretunneling.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.untag_resource

            output, http_response = (
                aws_sdk_iotsecuretunneling._operations.io_t_secured_tunneling.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotsecuretunneling.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
