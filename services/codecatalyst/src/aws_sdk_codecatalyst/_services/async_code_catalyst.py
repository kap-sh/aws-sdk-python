"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CodeCatalyst``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_codecatalyst._auth._signers
import aws_sdk_codecatalyst._auth._sigv4
from aws_sdk_codecatalyst._auth._providers import (
    BearerTokenProvider,
    StaticBearerTokenProvider,
)
from aws_sdk_codecatalyst._auth._zapros_handler import AuthMiddleware
from aws_sdk_codecatalyst._resources.code_catalyst.access_token import AsyncAccessToken
from aws_sdk_codecatalyst._resources.code_catalyst.space import AsyncSpace
from aws_sdk_codecatalyst._services._aws_config import aaws_config
from aws_sdk_codecatalyst._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.get_user_details_request
    import aws_sdk_codecatalyst.types.get_user_details_response
    import aws_sdk_codecatalyst.types.verify_session_response


class AsyncCodeCatalystClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    region: str | None
    endpoint: str | None
    bearer_provider: BearerTokenProvider | None


class AsyncCodeCatalystClient:
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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        region: str | None = None,
        endpoint: str | None = None,
        bearer: str | None = None,
        bearer_provider: BearerTokenProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if bearer is not None and bearer_provider is not None:
            warnings.warn(
                "Both bearer and bearer_provider given; provider takes precedence"
            )
        if bearer_provider is None and bearer is not None:
            bearer_provider = StaticBearerTokenProvider(bearer)
        self._config = AsyncCodeCatalystClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "region": region,
                "endpoint": endpoint,
                "bearer_provider": bearer_provider,
            }
        )

        # resources
        self.access_token = AsyncAccessToken(self)
        self.space = AsyncSpace(self)

    def operation_options(
        self, config_overrides: Optional[AsyncCodeCatalystClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCodeCatalystClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            region=overrides.get("region", self._config.get("region")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            bearer_provider=overrides.get(
                "bearer_provider", self._config.get("bearer_provider")
            ),
        )
        return interceptors_, options_

    async def get_user_details(
        self,
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        id: Optional[str] = None,
        user_name: Optional[str] = None,
    ) -> "aws_sdk_codecatalyst.types.get_user_details_response.GetUserDetailsResponse":
        """<p>Returns information about a user. </p>

        Args:
            id: <p>The system-generated unique ID of the user. </p>
            user_name: <p>The name of the user as displayed in Amazon CodeCatalyst.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecatalyst.types.get_user_details_request.GetUserDetailsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecatalyst.types.get_user_details_response.GetUserDetailsResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.get_user_details

            (
                output,
                http_response,
            ) = await aws_sdk_codecatalyst._operations.code_catalyst.get_user_details.async_get_user_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecatalyst.types.get_user_details_request.GetUserDetailsRequest = {}  # type: ignore[typeddict-item]
        if id is not None:
            input_["id"] = id
        if user_name is not None:
            input_["user_name"] = user_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def verify_session(
        self, *, config_overrides: Optional[AsyncCodeCatalystClientConfig] = None
    ) -> "aws_sdk_codecatalyst.types.verify_session_response.VerifySessionResponse":
        """<p>Verifies whether the calling user has a valid Amazon CodeCatalyst login and session. If successful, this returns the ID of the user in Amazon CodeCatalyst.</p>

        Raises:
            aws_sdk_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            aws_sdk_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            aws_sdk_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            aws_sdk_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            aws_sdk_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            aws_sdk_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecatalyst.types.verify_session_response.VerifySessionResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.verify_session

            (
                output,
                http_response,
            ) = await aws_sdk_codecatalyst._operations.code_catalyst.verify_session.async_verify_session(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
