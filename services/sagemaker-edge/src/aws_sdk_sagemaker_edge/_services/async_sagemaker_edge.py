"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#AmazonSageMakerEdge``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_sagemaker_edge._auth._signers
import aws_sdk_sagemaker_edge._auth._sigv4
from aws_sdk_sagemaker_edge._auth._identity import Credentials
from aws_sdk_sagemaker_edge._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_sagemaker_edge._auth._zapros_handler import AuthMiddleware
from aws_sdk_sagemaker_edge._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_sagemaker_edge.types.deployment_result
    import aws_sdk_sagemaker_edge.types.device_fleet_name
    import aws_sdk_sagemaker_edge.types.device_name
    import aws_sdk_sagemaker_edge.types.edge_metrics
    import aws_sdk_sagemaker_edge.types.get_deployments_request
    import aws_sdk_sagemaker_edge.types.get_deployments_result
    import aws_sdk_sagemaker_edge.types.get_device_registration_request
    import aws_sdk_sagemaker_edge.types.get_device_registration_result
    import aws_sdk_sagemaker_edge.types.models
    import aws_sdk_sagemaker_edge.types.send_heartbeat_request
    import aws_sdk_sagemaker_edge.types.version


class AsyncSagemakerEdgeClientConfig(TypedDict, total=False):
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


class AsyncSagemakerEdgeClient:
    """A client for the ``SagemakerEdge`` service.

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
        self.config = AsyncSagemakerEdgeClientConfig(
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
        self, config_overrides: Optional[AsyncSagemakerEdgeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSagemakerEdgeClientConfig = config_overrides or {}
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

    async def get_deployments(
        self,
        device_name: "aws_sdk_sagemaker_edge.types.device_name.DeviceName",
        device_fleet_name: "aws_sdk_sagemaker_edge.types.device_fleet_name.DeviceFleetName",
        *,
        config_overrides: Optional[AsyncSagemakerEdgeClientConfig] = None,
    ) -> "aws_sdk_sagemaker_edge.types.get_deployments_result.GetDeploymentsResult":
        """<p>Use to get the active deployments from a device.</p>

        Args:
            device_name: <p>The unique name of the device you want to get the configuration of active deployments from.</p>
            device_fleet_name: <p>The name of the fleet that the device belongs to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_edge.types.get_deployments_request.GetDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_edge.types.get_deployments_result.GetDeploymentsResult"
        ]:
            import aws_sdk_sagemaker_edge._operations.amazon_sage_maker_edge.get_deployments

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_edge._operations.amazon_sage_maker_edge.get_deployments.async_get_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_edge.types.get_deployments_request.GetDeploymentsRequest = {}  # type: ignore[typeddict-item]
        input_["device_name"] = device_name
        input_["device_fleet_name"] = device_fleet_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_device_registration(
        self,
        device_name: "aws_sdk_sagemaker_edge.types.device_name.DeviceName",
        device_fleet_name: "aws_sdk_sagemaker_edge.types.device_fleet_name.DeviceFleetName",
        *,
        config_overrides: Optional[AsyncSagemakerEdgeClientConfig] = None,
    ) -> "aws_sdk_sagemaker_edge.types.get_device_registration_result.GetDeviceRegistrationResult":
        """<p>Use to check if a device is registered with SageMaker Edge Manager.</p>

        Args:
            device_name: <p>The unique name of the device you want to get the registration status from.</p>
            device_fleet_name: <p>The name of the fleet that the device belongs to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_edge.types.get_device_registration_request.GetDeviceRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_edge.types.get_device_registration_result.GetDeviceRegistrationResult"
        ]:
            import aws_sdk_sagemaker_edge._operations.amazon_sage_maker_edge.get_device_registration

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_edge._operations.amazon_sage_maker_edge.get_device_registration.async_get_device_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_edge.types.get_device_registration_request.GetDeviceRegistrationRequest = {}  # type: ignore[typeddict-item]
        input_["device_name"] = device_name
        input_["device_fleet_name"] = device_fleet_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_heartbeat(
        self,
        agent_version: "aws_sdk_sagemaker_edge.types.version.Version",
        device_name: "aws_sdk_sagemaker_edge.types.device_name.DeviceName",
        device_fleet_name: "aws_sdk_sagemaker_edge.types.device_fleet_name.DeviceFleetName",
        *,
        config_overrides: Optional[AsyncSagemakerEdgeClientConfig] = None,
        agent_metrics: Optional[
            "aws_sdk_sagemaker_edge.types.edge_metrics.EdgeMetrics"
        ] = None,
        models: Optional["aws_sdk_sagemaker_edge.types.models.Models"] = None,
        deployment_result: Optional[
            "aws_sdk_sagemaker_edge.types.deployment_result.DeploymentResult"
        ] = None,
    ) -> None:
        """<p>Use to get the current status of devices registered on SageMaker Edge Manager.</p>

        Args:
            agent_metrics: <p>For internal use. Returns a list of SageMaker Edge Manager agent operating metrics.</p>
            models: <p>Returns a list of models deployed on the the device.</p>
            agent_version: <p>Returns the version of the agent.</p>
            device_name: <p>The unique name of the device.</p>
            device_fleet_name: <p>The name of the fleet that the device belongs to.</p>
            deployment_result: <p>Returns the result of a deployment on the device.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_edge.types.send_heartbeat_request.SendHeartbeatRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_sagemaker_edge._operations.amazon_sage_maker_edge.send_heartbeat

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_edge._operations.amazon_sage_maker_edge.send_heartbeat.async_send_heartbeat(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_edge.types.send_heartbeat_request.SendHeartbeatRequest = {}  # type: ignore[typeddict-item]
        if agent_metrics is not None:
            input_["agent_metrics"] = agent_metrics
        if models is not None:
            input_["models"] = models
        input_["agent_version"] = agent_version
        input_["device_name"] = device_name
        input_["device_fleet_name"] = device_fleet_name
        if deployment_result is not None:
            input_["deployment_result"] = deployment_result

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
