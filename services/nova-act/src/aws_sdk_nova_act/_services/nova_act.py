"""Generated from Smithy shape ``com.amazonaws.novaact#AmazonNovaAgentsDataPlane``."""

import warnings
from typing import Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

from aws_sdk_nova_act._auth._identity import Credentials
from aws_sdk_nova_act._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_nova_act._auth._zapros_handler import AuthMiddleware
from aws_sdk_nova_act._resources.amazon_nova_agents_data_plane.act_resource import (
    ActResource,
)
from aws_sdk_nova_act._resources.amazon_nova_agents_data_plane.model_resource import (
    ModelResource,
)
from aws_sdk_nova_act._resources.amazon_nova_agents_data_plane.service_linked_role_resource import (
    ServiceLinkedRoleResource,
)
from aws_sdk_nova_act._resources.amazon_nova_agents_data_plane.session_resource import (
    SessionResource,
)
from aws_sdk_nova_act._resources.amazon_nova_agents_data_plane.workflow_definition_resource import (
    WorkflowDefinitionResource,
)
from aws_sdk_nova_act._resources.amazon_nova_agents_data_plane.workflow_run_resource import (
    WorkflowRunResource,
)
from aws_sdk_nova_act._services._aws_config import aws_config
from aws_sdk_nova_act._services._pipeline import (
    Interceptor,
    OperationOptions,
    retry,
)


class NovaActClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


class NovaActClient:
    """A client for the ``NovaAct`` service.

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
        self._config = NovaActClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.act_resource = ActResource(self)
        self.model_resource = ModelResource(self)
        self.service_linked_role_resource = ServiceLinkedRoleResource(self)
        self.session_resource = SessionResource(self)
        self.workflow_definition_resource = WorkflowDefinitionResource(self)
        self.workflow_run_resource = WorkflowRunResource(self)

    def operation_options(
        self, config_overrides: Optional[NovaActClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: NovaActClientConfig = config_overrides or {}
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
