"""Generated from Smithy shape ``com.amazonaws.controltower#AWSControlTowerApis``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_controltower._auth._signers
import aws_sdk_controltower._auth._sigv4
from aws_sdk_controltower._auth._identity import Credentials
from aws_sdk_controltower._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_controltower._auth._zapros_handler import AuthMiddleware
from aws_sdk_controltower._resources.aws_control_tower_apis.baseline_operation_resource import (
    AsyncBaselineOperationResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.baseline_resource import (
    AsyncBaselineResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.control_operation_resource import (
    AsyncControlOperationResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.enabled_baseline_resource import (
    AsyncEnabledBaselineResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.enabled_control_resource import (
    AsyncEnabledControlResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.landing_zone_operation_resource import (
    AsyncLandingZoneOperationResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.landing_zone_resource import (
    AsyncLandingZoneResource,
)
from aws_sdk_controltower._resources.aws_control_tower_apis.tagging_resource import (
    AsyncTaggingResource,
)
from aws_sdk_controltower._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.control_identifier
    import aws_sdk_controltower.types.disable_control_input
    import aws_sdk_controltower.types.disable_control_output
    import aws_sdk_controltower.types.target_identifier


class AsyncControlTowerClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncControlTowerClient:
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
        self.config = AsyncControlTowerClientConfig(
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
        self.baseline_operation_resource = AsyncBaselineOperationResource(self)
        self.baseline_resource = AsyncBaselineResource(self)
        self.control_operation_resource = AsyncControlOperationResource(self)
        self.enabled_baseline_resource = AsyncEnabledBaselineResource(self)
        self.enabled_control_resource = AsyncEnabledControlResource(self)
        self.landing_zone_operation_resource = AsyncLandingZoneOperationResource(self)
        self.landing_zone_resource = AsyncLandingZoneResource(self)
        self.tagging_resource = AsyncTaggingResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncControlTowerClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncControlTowerClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def disable_control(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
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
        """<p>This API call turns off a control. It starts an asynchronous operation that deletes Amazon Web Services resources on the specified organizational unit and the accounts it contains. The resources will vary according to the control that you specify. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            control_identifier: <p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            enabled_control_identifier: <p>The ARN of the enabled control to be disabled, which uniquely identifies the control instance on the target organizational unit.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.disable_control_input.DisableControlInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.disable_control_output.DisableControlOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.disable_control

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.disable_control.async_disable_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.disable_control_input.DisableControlInput = {}  # type: ignore[typeddict-item]
        if control_identifier is not None:
            input_["control_identifier"] = control_identifier
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier
        if enabled_control_identifier is not None:
            input_["enabled_control_identifier"] = enabled_control_identifier

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
