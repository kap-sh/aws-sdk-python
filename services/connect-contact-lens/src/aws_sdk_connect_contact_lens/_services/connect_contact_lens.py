"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#AmazonConnectContactLens``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_connect_contact_lens._auth._signers
import aws_sdk_connect_contact_lens._auth._sigv4
from aws_sdk_connect_contact_lens._auth._identity import Credentials
from aws_sdk_connect_contact_lens._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_connect_contact_lens._auth._zapros_handler import AuthMiddleware
from aws_sdk_connect_contact_lens._services._aws_config import aws_config
from aws_sdk_connect_contact_lens._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_connect_contact_lens.types.contact_id
    import aws_sdk_connect_contact_lens.types.instance_id
    import aws_sdk_connect_contact_lens.types.list_realtime_contact_analysis_segments_request
    import aws_sdk_connect_contact_lens.types.list_realtime_contact_analysis_segments_response
    import aws_sdk_connect_contact_lens.types.max_results
    import aws_sdk_connect_contact_lens.types.next_token


class ConnectContactLensClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ConnectContactLensClient:
    """A client for the ``ConnectContactLens`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = ConnectContactLensClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[ConnectContactLensClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ConnectContactLensClientConfig = config_overrides or {}
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

    def list_realtime_contact_analysis_segments(
        self,
        instance_id: "aws_sdk_connect_contact_lens.types.instance_id.InstanceId",
        contact_id: "aws_sdk_connect_contact_lens.types.contact_id.ContactId",
        *,
        config_overrides: Optional[ConnectContactLensClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connect_contact_lens.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_connect_contact_lens.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_connect_contact_lens.types.list_realtime_contact_analysis_segments_response.ListRealtimeContactAnalysisSegmentsResponse":
        """<p>Provides a list of analysis segments for a real-time analysis session.</p>

        Args:
            instance_id: <p>The identifier of the Amazon Connect instance.</p>
            contact_id: <p>The identifier of the contact.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connect_contact_lens.types.list_realtime_contact_analysis_segments_request.ListRealtimeContactAnalysisSegmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_connect_contact_lens.types.list_realtime_contact_analysis_segments_response.ListRealtimeContactAnalysisSegmentsResponse"
        ]:
            import aws_sdk_connect_contact_lens._operations.amazon_connect_contact_lens.list_realtime_contact_analysis_segments

            output, http_response = (
                aws_sdk_connect_contact_lens._operations.amazon_connect_contact_lens.list_realtime_contact_analysis_segments.list_realtime_contact_analysis_segments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connect_contact_lens.types.list_realtime_contact_analysis_segments_request.ListRealtimeContactAnalysisSegmentsRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["contact_id"] = contact_id
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
