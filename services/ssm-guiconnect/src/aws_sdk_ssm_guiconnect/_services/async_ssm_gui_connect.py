"""Generated from Smithy shape ``com.amazonaws.ssmguiconnect#SSMGuiConnect``."""

import warnings
from typing import Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

from aws_sdk_ssm_guiconnect._auth._identity import Credentials
from aws_sdk_ssm_guiconnect._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_ssm_guiconnect._auth._zapros_handler import AuthMiddleware
from aws_sdk_ssm_guiconnect._resources.ssm_gui_connect.connection import AsyncConnection
from aws_sdk_ssm_guiconnect._resources.ssm_gui_connect.connection_access import (
    AsyncConnectionAccess,
)
from aws_sdk_ssm_guiconnect._resources.ssm_gui_connect.connection_preferences import (
    AsyncConnectionPreferences,
)
from aws_sdk_ssm_guiconnect._resources.ssm_gui_connect.connections_collection import (
    AsyncConnectionsCollection,
)
from aws_sdk_ssm_guiconnect._resources.ssm_gui_connect.modify_connection_preferences import (
    AsyncModifyConnectionPreferences,
)
from aws_sdk_ssm_guiconnect._resources.ssm_gui_connect.modify_recording_preferences import (
    AsyncModifyRecordingPreferences,
)
from aws_sdk_ssm_guiconnect._resources.ssm_gui_connect.recording_preferences import (
    AsyncRecordingPreferences,
)
from aws_sdk_ssm_guiconnect._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    aretry,
)


class AsyncSSMGuiConnectClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncSSMGuiConnectClient:
    """A client for the ``SSMGuiConnect`` service.

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
        self._config = AsyncSSMGuiConnectClientConfig(
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

        # resources
        self.connection = AsyncConnection(self)
        self.connection_access = AsyncConnectionAccess(self)
        self.connection_preferences = AsyncConnectionPreferences(self)
        self.connections_collection = AsyncConnectionsCollection(self)
        self.modify_connection_preferences = AsyncModifyConnectionPreferences(self)
        self.modify_recording_preferences = AsyncModifyRecordingPreferences(self)
        self.recording_preferences = AsyncRecordingPreferences(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSSMGuiConnectClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSSMGuiConnectClientConfig = config_overrides or {}
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
