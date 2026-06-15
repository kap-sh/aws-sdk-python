"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#AWSAcuitySignalingService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_kinesis_video_signaling._auth._signers
import aws_sdk_kinesis_video_signaling._auth._sigv4
from aws_sdk_kinesis_video_signaling._auth._identity import Credentials
from aws_sdk_kinesis_video_signaling._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_kinesis_video_signaling._auth._zapros_handler import AuthMiddleware
from aws_sdk_kinesis_video_signaling._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_signaling.types.client_id
    import aws_sdk_kinesis_video_signaling.types.get_ice_server_config_request
    import aws_sdk_kinesis_video_signaling.types.get_ice_server_config_response
    import aws_sdk_kinesis_video_signaling.types.message_payload
    import aws_sdk_kinesis_video_signaling.types.resource_arn
    import aws_sdk_kinesis_video_signaling.types.send_alexa_offer_to_master_request
    import aws_sdk_kinesis_video_signaling.types.send_alexa_offer_to_master_response
    import aws_sdk_kinesis_video_signaling.types.service
    import aws_sdk_kinesis_video_signaling.types.username


class AsyncKinesisVideoSignalingClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncKinesisVideoSignalingClient:
    """A client for the ``KinesisVideoSignaling`` service.

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
        self._config = AsyncKinesisVideoSignalingClientConfig(
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
        self, config_overrides: Optional[AsyncKinesisVideoSignalingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncKinesisVideoSignalingClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    async def get_ice_server_config(
        self,
        channel_arn: "aws_sdk_kinesis_video_signaling.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[AsyncKinesisVideoSignalingClientConfig] = None,
        client_id: Optional[
            "aws_sdk_kinesis_video_signaling.types.client_id.ClientId"
        ] = None,
        service: Optional[
            "aws_sdk_kinesis_video_signaling.types.service.Service"
        ] = None,
        username: Optional[
            "aws_sdk_kinesis_video_signaling.types.username.Username"
        ] = None,
    ) -> "aws_sdk_kinesis_video_signaling.types.get_ice_server_config_response.GetIceServerConfigResponse":
        r"""<p>Gets the Interactive Connectivity Establishment (ICE) server configuration information, including URIs, username, and password which can be used to configure the WebRTC connection. The ICE component uses this configuration information to setup the WebRTC connection, including authenticating with the Traversal Using Relays around NAT (TURN) relay server. </p> <p>TURN is a protocol that is used to improve the connectivity of peer-to-peer applications. By providing a cloud-based relay service, TURN ensures that a connection can be established even when one or more peers are incapable of a direct peer-to-peer connection. For more information, see <a href=\"https://tools.ietf.org/html/draft-uberti-rtcweb-turn-rest-00\">A REST API For Access To TURN Services</a>.</p> <p> You can invoke this API to establish a fallback mechanism in case either of the peers is unable to establish a direct peer-to-peer connection over a signaling channel. You must specify either a signaling channel ARN or the client ID in order to invoke this API.</p>

        Args:
            channel_arn: <p>The ARN of the signaling channel to be used for the peer-to-peer connection between configured peers. </p>
            client_id: <p>Unique identifier for the viewer. Must be unique within the signaling channel.</p>
            service: <p>Specifies the desired service. Currently, <code>TURN</code> is the only valid value.</p>
            username: <p>An optional user ID to be associated with the credentials.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video_signaling.types.get_ice_server_config_request.GetIceServerConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video_signaling.types.get_ice_server_config_response.GetIceServerConfigResponse"
        ]:
            import aws_sdk_kinesis_video_signaling._operations.aws_acuity_signaling_service.get_ice_server_config

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video_signaling._operations.aws_acuity_signaling_service.get_ice_server_config.async_get_ice_server_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video_signaling.types.get_ice_server_config_request.GetIceServerConfigRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if client_id is not None:
            input_["client_id"] = client_id
        if service is not None:
            input_["service"] = service
        if username is not None:
            input_["username"] = username

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_alexa_offer_to_master(
        self,
        channel_arn: "aws_sdk_kinesis_video_signaling.types.resource_arn.ResourceARN",
        sender_client_id: "aws_sdk_kinesis_video_signaling.types.client_id.ClientId",
        message_payload: "aws_sdk_kinesis_video_signaling.types.message_payload.MessagePayload",
        *,
        config_overrides: Optional[AsyncKinesisVideoSignalingClientConfig] = None,
    ) -> "aws_sdk_kinesis_video_signaling.types.send_alexa_offer_to_master_response.SendAlexaOfferToMasterResponse":
        """<p>This API allows you to connect WebRTC-enabled devices with Alexa display devices. When invoked, it sends the Alexa Session Description Protocol (SDP) offer to the master peer. The offer is delivered as soon as the master is connected to the specified signaling channel. This API returns the SDP answer from the connected master. If the master is not connected to the signaling channel, redelivery requests are made until the message expires.</p>

        Args:
            channel_arn: <p>The ARN of the signaling channel by which Alexa and the master peer communicate.</p>
            sender_client_id: <p>The unique identifier for the sender client.</p>
            message_payload: <p>The base64-encoded SDP offer content.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video_signaling.types.send_alexa_offer_to_master_request.SendAlexaOfferToMasterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video_signaling.types.send_alexa_offer_to_master_response.SendAlexaOfferToMasterResponse"
        ]:
            import aws_sdk_kinesis_video_signaling._operations.aws_acuity_signaling_service.send_alexa_offer_to_master

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video_signaling._operations.aws_acuity_signaling_service.send_alexa_offer_to_master.async_send_alexa_offer_to_master(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video_signaling.types.send_alexa_offer_to_master_request.SendAlexaOfferToMasterRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["sender_client_id"] = sender_client_id
        input_["message_payload"] = message_payload

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
