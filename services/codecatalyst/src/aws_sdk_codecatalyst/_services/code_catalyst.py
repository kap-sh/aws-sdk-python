"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CodeCatalyst``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_codecatalyst._auth._signers
import aws_sdk_codecatalyst._auth._sigv4
from aws_sdk_codecatalyst._auth._providers import (
    BearerTokenProvider,
    StaticBearerTokenProvider,
)
from aws_sdk_codecatalyst._auth._zapros_handler import AuthMiddleware
from aws_sdk_codecatalyst._resources.code_catalyst.access_token import AccessToken
from aws_sdk_codecatalyst._resources.code_catalyst.space import Space
from aws_sdk_codecatalyst._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.get_user_details_request
    import aws_sdk_codecatalyst.types.get_user_details_response
    import aws_sdk_codecatalyst.types.verify_session_response


class CodeCatalystClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    region: str | None
    endpoint: str | None
    bearer_provider: BearerTokenProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class CodeCatalystClient:
    """A client for the ``CodeCatalyst`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        bearer: Bearer token for authentication.
        bearer_provider: Provider that resolves bearer tokens. Takes precedence over ``bearer``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        region: str | None = None,
        endpoint: str | None = None,
        bearer: str | None = None,
        bearer_provider: BearerTokenProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if bearer is not None and bearer_provider is not None:
            warnings.warn(
                "Both bearer and bearer_provider given; provider takes precedence"
            )
        if bearer_provider is None and bearer is not None:
            bearer_provider = StaticBearerTokenProvider(bearer)
        self.config = CodeCatalystClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_fips": use_fips,
                "region": region,
                "endpoint": endpoint,
                "bearer_provider": bearer_provider,
            }
        )
        # resources
        self.access_token = AccessToken(self)
        self.space = Space(self)

    def operation_options(
        self, config_overrides: Optional[CodeCatalystClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CodeCatalystClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            region=overrides.get("region", self.config.get("region")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            bearer_provider=overrides.get(
                "bearer_provider", self.config.get("bearer_provider")
            ),
        )
        return interceptors_, options_

    def get_user_details(
        self,
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        id: Optional[str] = None,
        user_name: Optional[str] = None,
    ) -> "aws_sdk_codecatalyst.types.get_user_details_response.GetUserDetailsResponse":
        """<p>Returns information about a user. </p>

        Args:
            id: <p>The system-generated unique ID of the user. </p>
            user_name: <p>The name of the user as displayed in Amazon CodeCatalyst.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codecatalyst.types.get_user_details_request.GetUserDetailsRequest]",
        ) -> OperationResponse[
            "aws_sdk_codecatalyst.types.get_user_details_response.GetUserDetailsResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.get_user_details

            output, http_response = (
                aws_sdk_codecatalyst._operations.code_catalyst.get_user_details.get_user_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.get_user_details_request.GetUserDetailsRequest = {}  # type: ignore[typeddict-item]
        if id is not None:
            input_["id"] = id
        if user_name is not None:
            input_["user_name"] = user_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def verify_session(
        self, *, config_overrides: Optional[CodeCatalystClientConfig] = None
    ) -> "aws_sdk_codecatalyst.types.verify_session_response.VerifySessionResponse":
        """<p>Verifies whether the calling user has a valid Amazon CodeCatalyst login and session. If successful, this returns the ID of the user in Amazon CodeCatalyst.</p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_codecatalyst.types.verify_session_response.VerifySessionResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.verify_session

            output, http_response = (
                aws_sdk_codecatalyst._operations.code_catalyst.verify_session.verify_session(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
