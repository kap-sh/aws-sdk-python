"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#ApiGatewayManagementApi``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_apigatewaymanagementapi._auth._signers
import aws_sdk_apigatewaymanagementapi._auth._sigv4
from aws_sdk_apigatewaymanagementapi._auth._identity import Credentials
from aws_sdk_apigatewaymanagementapi._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_apigatewaymanagementapi._auth._zapros_handler import AuthMiddleware
from aws_sdk_apigatewaymanagementapi._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_apigatewaymanagementapi.types.__string
    import aws_sdk_apigatewaymanagementapi.types.data
    import aws_sdk_apigatewaymanagementapi.types.delete_connection_request
    import aws_sdk_apigatewaymanagementapi.types.get_connection_request
    import aws_sdk_apigatewaymanagementapi.types.get_connection_response
    import aws_sdk_apigatewaymanagementapi.types.post_to_connection_request


class ApiGatewayManagementApiClientConfig(TypedDict, total=False):
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


class ApiGatewayManagementApiClient:
    """A client for the ``ApiGatewayManagementApi`` service.

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
        self.config = ApiGatewayManagementApiClientConfig(
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
        self, config_overrides: Optional[ApiGatewayManagementApiClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ApiGatewayManagementApiClientConfig = config_overrides or {}
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

    def delete_connection(
        self,
        connection_id: "aws_sdk_apigatewaymanagementapi.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayManagementApiClientConfig] = None,
    ) -> None:
        """<p>Delete the connection with the provided id.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_apigatewaymanagementapi.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_apigatewaymanagementapi._operations.api_gateway_management_api.delete_connection

            output, http_response = (
                aws_sdk_apigatewaymanagementapi._operations.api_gateway_management_api.delete_connection.delete_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_apigatewaymanagementapi.types.delete_connection_request.DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_connection(
        self,
        connection_id: "aws_sdk_apigatewaymanagementapi.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayManagementApiClientConfig] = None,
    ) -> "aws_sdk_apigatewaymanagementapi.types.get_connection_response.GetConnectionResponse":
        """<p>Get information about the connection with the provided id.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_apigatewaymanagementapi.types.get_connection_request.GetConnectionRequest]",
        ) -> OperationResponse[
            "aws_sdk_apigatewaymanagementapi.types.get_connection_response.GetConnectionResponse"
        ]:
            import aws_sdk_apigatewaymanagementapi._operations.api_gateway_management_api.get_connection

            output, http_response = (
                aws_sdk_apigatewaymanagementapi._operations.api_gateway_management_api.get_connection.get_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_apigatewaymanagementapi.types.get_connection_request.GetConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def post_to_connection(
        self,
        data: "aws_sdk_apigatewaymanagementapi.types.data.Data",
        connection_id: "aws_sdk_apigatewaymanagementapi.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayManagementApiClientConfig] = None,
    ) -> None:
        """<p>Sends the provided data to the specified connection.</p>

        Args:
            data: <p>The data to be sent to the client specified by its connection id.</p>
            connection_id: <p>The identifier of the connection that a specific client is using.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_apigatewaymanagementapi.types.post_to_connection_request.PostToConnectionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_apigatewaymanagementapi._operations.api_gateway_management_api.post_to_connection

            output, http_response = (
                aws_sdk_apigatewaymanagementapi._operations.api_gateway_management_api.post_to_connection.post_to_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_apigatewaymanagementapi.types.post_to_connection_request.PostToConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["data"] = data
        input_["connection_id"] = connection_id

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
