"""Generated from Smithy shape ``com.amazonaws.controltower#AWSControlTowerApis``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_controltower._auth._signers
import aws_sdk_controltower._auth._sigv4
from aws_sdk_controltower._auth._identity import Credentials
from aws_sdk_controltower._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_controltower._auth._zapros_handler import AuthMiddleware
from aws_sdk_controltower._resources.aws_control_tower_apis.baseline_operation_resource import (
    BaselineOperationResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.baseline_resource import (
    BaselineResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.control_operation_resource import (
    ControlOperationResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.enabled_baseline_resource import (
    EnabledBaselineResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.enabled_control_resource import (
    EnabledControlResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.landing_zone_operation_resource import (
    LandingZoneOperationResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.landing_zone_resource import (
    LandingZoneResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.tagging_resource import (
    TaggingResource,
)
from aws_sdk_controltower._services._aws_config import aws_config
from aws_sdk_controltower._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.control_identifier
    import aws_sdk_controltower.types.disable_control_input
    import aws_sdk_controltower.types.disable_control_output
    import aws_sdk_controltower.types.target_identifier


class ControlTowerClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ControlTowerClient:
    """A client for the ``ControlTower`` service.

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
        self._config = ControlTowerClientConfig(
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
        self.baseline_operation_resource = BaselineOperationResource(self)
        self.baseline_resource = BaselineResource(self)
        self.control_operation_resource = ControlOperationResource(self)
        self.enabled_baseline_resource = EnabledBaselineResource(self)
        self.enabled_control_resource = EnabledControlResource(self)
        self.landing_zone_operation_resource = LandingZoneOperationResource(self)
        self.landing_zone_resource = LandingZoneResource(self)
        self.tagging_resource = TaggingResource(self)

    def operation_options(
        self, config_overrides: Optional[ControlTowerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ControlTowerClientConfig = config_overrides or {}
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

    def disable_control(
        self,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        control_identifier: Optional[
            "aws_sdk_controltower.types.control_identifier.ControlIdentifier"
        ] = None,
        target_identifier: Optional[
            "aws_sdk_controltower.types.target_identifier.TargetIdentifier"
        ] = None,
        enabled_control_identifier: Optional[
            "aws_sdk_controltower.types.arn.Arn"
        ] = None,
    ) -> "aws_sdk_controltower.types.disable_control_output.DisableControlOutput":
        r"""<p>This API call turns off a control. It starts an asynchronous operation that deletes Amazon Web Services resources on the specified organizational unit and the accounts it contains. The resources will vary according to the control that you specify. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            control_identifier: <p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            enabled_control_identifier: <p>The ARN of the enabled control to be disabled, which uniquely identifies the control instance on the target organizational unit.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.disable_control_input.DisableControlInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.disable_control_output.DisableControlOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.disable_control

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.disable_control.disable_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.disable_control_input.DisableControlInput = {}  # type: ignore[typeddict-item]
        if control_identifier is not None:
            input_["control_identifier"] = control_identifier
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier
        if enabled_control_identifier is not None:
            input_["enabled_control_identifier"] = enabled_control_identifier

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
