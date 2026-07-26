"""Generated from Smithy shape ``com.amazonaws.arczonalshift#PercDataPlane``."""

import warnings
from typing import Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

from capo_arc_zonal_shift._auth._identity import Credentials
from capo_arc_zonal_shift._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_arc_zonal_shift._auth._zapros_handler import AuthMiddleware
from capo_arc_zonal_shift._resources.perc_data_plane.autoshift import Autoshift
from capo_arc_zonal_shift._resources.perc_data_plane.autoshift_observer_notification import (
    AutoshiftObserverNotification,
)
from capo_arc_zonal_shift._resources.perc_data_plane.autoshift_trigger_resource import (
    AutoshiftTriggerResource,
)
from capo_arc_zonal_shift._resources.perc_data_plane.managed_resource import (
    ManagedResource,
)
from capo_arc_zonal_shift._resources.perc_data_plane.practice_run_configuration_resource import (
    PracticeRunConfigurationResource,
)
from capo_arc_zonal_shift._resources.perc_data_plane.zonal_shift_resource import (
    ZonalShiftResource,
)
from capo_arc_zonal_shift._resources.perc_data_plane.zonal_shifts import ZonalShifts
from capo_arc_zonal_shift._services._aws_config import aws_config
from capo_arc_zonal_shift._services._pipeline import (
    Interceptor,
    OperationOptions,
    retry,
)


class ARCZonalShiftClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ARCZonalShiftClient:
    """A client for the ``ARCZonalShift`` service.

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
        self._config = ARCZonalShiftClientConfig(
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

        # resources
        self.autoshift = Autoshift(self)
        self.autoshift_observer_notification = AutoshiftObserverNotification(self)
        self.autoshift_trigger_resource = AutoshiftTriggerResource(self)
        self.managed_resource = ManagedResource(self)
        self.practice_run_configuration_resource = PracticeRunConfigurationResource(
            self
        )
        self.zonal_shift_resource = ZonalShiftResource(self)
        self.zonal_shifts = ZonalShifts(self)

    def operation_options(
        self, config_overrides: Optional[ARCZonalShiftClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ARCZonalShiftClientConfig = config_overrides or {}
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
