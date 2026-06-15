"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#GiraffeMessageInTransitService``."""

import warnings
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_workmailmessageflow._auth._signers
import aws_sdk_workmailmessageflow._auth._sigv4
from aws_sdk_workmailmessageflow._auth._identity import Credentials
from aws_sdk_workmailmessageflow._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_workmailmessageflow._auth._zapros_handler import AuthMiddleware
from aws_sdk_workmailmessageflow._services._aws_config import aaws_config
from aws_sdk_workmailmessageflow._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_workmailmessageflow.types.get_raw_message_content_request
    import aws_sdk_workmailmessageflow.types.get_raw_message_content_response
    import aws_sdk_workmailmessageflow.types.message_id_type
    import aws_sdk_workmailmessageflow.types.put_raw_message_content_request
    import aws_sdk_workmailmessageflow.types.put_raw_message_content_response
    import aws_sdk_workmailmessageflow.types.raw_message_content


class AsyncWorkMailMessageFlowClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class AsyncWorkMailMessageFlowClient:
    """A client for the ``WorkMailMessageFlow`` service.

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
        self._config = AsyncWorkMailMessageFlowClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncWorkMailMessageFlowClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncWorkMailMessageFlowClientConfig = config_overrides or {}
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

    @asynccontextmanager
    async def get_raw_message_content(
        self,
        message_id: "aws_sdk_workmailmessageflow.types.message_id_type.messageIdType",
        *,
        config_overrides: Optional[AsyncWorkMailMessageFlowClientConfig] = None,
    ) -> "AsyncGenerator[aws_sdk_workmailmessageflow.types.get_raw_message_content_response.GetRawMessageContentResponse]":
        """<p>Retrieves the raw content of an in-transit email message, in MIME format.</p>

        Args:
            message_id: <p>The identifier of the email message to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workmailmessageflow.types.get_raw_message_content_request.GetRawMessageContentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workmailmessageflow.types.get_raw_message_content_response.GetRawMessageContentResponse"
        ]:
            import aws_sdk_workmailmessageflow._operations.giraffe_message_in_transit_service.get_raw_message_content

            (
                output,
                http_response,
            ) = await aws_sdk_workmailmessageflow._operations.giraffe_message_in_transit_service.get_raw_message_content.async_get_raw_message_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmailmessageflow.types.get_raw_message_content_request.GetRawMessageContentRequest = {}  # type: ignore[typeddict-item]
        input_["message_id"] = message_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    async def put_raw_message_content(
        self,
        message_id: "aws_sdk_workmailmessageflow.types.message_id_type.messageIdType",
        content: "aws_sdk_workmailmessageflow.types.raw_message_content.RawMessageContent",
        *,
        config_overrides: Optional[AsyncWorkMailMessageFlowClientConfig] = None,
    ) -> "aws_sdk_workmailmessageflow.types.put_raw_message_content_response.PutRawMessageContentResponse":
        r"""<p>Updates the raw content of an in-transit email message, in MIME format.</p> <p>This example describes how to update in-transit email message. For more information and examples for using this API, see <a href=\"https://docs.aws.amazon.com/workmail/latest/adminguide/update-with-lambda.html\"> Updating message content with AWS Lambda</a>.</p> <note> <p>Updates to an in-transit message only appear when you call <code>PutRawMessageContent</code> from an AWS Lambda function configured with a synchronous <a href=\"https://docs.aws.amazon.com/workmail/latest/adminguide/lambda.html#synchronous-rules\"> Run Lambda</a> rule. If you call <code>PutRawMessageContent</code> on a delivered or sent message, the message remains unchanged, even though <a href=\"https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_GetRawMessageContent.html\">GetRawMessageContent</a> returns an updated message. </p> </note>

        Args:
            message_id: <p>The identifier of the email message being updated.</p>
            content: <p>Describes the raw message content of the updated email message.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_workmailmessageflow.types.put_raw_message_content_request.PutRawMessageContentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_workmailmessageflow.types.put_raw_message_content_response.PutRawMessageContentResponse"
        ]:
            import aws_sdk_workmailmessageflow._operations.giraffe_message_in_transit_service.put_raw_message_content

            (
                output,
                http_response,
            ) = await aws_sdk_workmailmessageflow._operations.giraffe_message_in_transit_service.put_raw_message_content.async_put_raw_message_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workmailmessageflow.types.put_raw_message_content_request.PutRawMessageContentRequest = {}  # type: ignore[typeddict-item]
        input_["message_id"] = message_id
        input_["content"] = content

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
