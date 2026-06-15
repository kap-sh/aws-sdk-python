"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#SageMakerMetricsService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_sagemaker_metrics._auth._signers
import aws_sdk_sagemaker_metrics._auth._sigv4
from aws_sdk_sagemaker_metrics._auth._identity import Credentials
from aws_sdk_sagemaker_metrics._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_sagemaker_metrics._auth._zapros_handler import AuthMiddleware
from aws_sdk_sagemaker_metrics._services._aws_config import aaws_config
from aws_sdk_sagemaker_metrics._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_sagemaker_metrics.types.batch_get_metrics_request
    import aws_sdk_sagemaker_metrics.types.batch_get_metrics_response
    import aws_sdk_sagemaker_metrics.types.batch_put_metrics_request
    import aws_sdk_sagemaker_metrics.types.batch_put_metrics_response
    import aws_sdk_sagemaker_metrics.types.experiment_entity_name
    import aws_sdk_sagemaker_metrics.types.metric_query_list
    import aws_sdk_sagemaker_metrics.types.raw_metric_data_list


class AsyncSageMakerMetricsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class AsyncSageMakerMetricsClient:
    """A client for the ``SageMakerMetrics`` service.

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
        self._config = AsyncSageMakerMetricsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSageMakerMetricsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSageMakerMetricsClientConfig = config_overrides or {}
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

    async def batch_get_metrics(
        self,
        metric_queries: "aws_sdk_sagemaker_metrics.types.metric_query_list.MetricQueryList",
        *,
        config_overrides: Optional[AsyncSageMakerMetricsClientConfig] = None,
    ) -> "aws_sdk_sagemaker_metrics.types.batch_get_metrics_response.BatchGetMetricsResponse":
        """<p>Used to retrieve training metrics from SageMaker.</p>

        Args:
            metric_queries: <p>Queries made to retrieve training metrics from SageMaker.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_metrics.types.batch_get_metrics_request.BatchGetMetricsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_metrics.types.batch_get_metrics_response.BatchGetMetricsResponse"
        ]:
            import aws_sdk_sagemaker_metrics._operations.sage_maker_metrics_service.batch_get_metrics

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_metrics._operations.sage_maker_metrics_service.batch_get_metrics.async_batch_get_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_metrics.types.batch_get_metrics_request.BatchGetMetricsRequest = {}  # type: ignore[typeddict-item]
        input_["metric_queries"] = metric_queries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_put_metrics(
        self,
        trial_component_name: "aws_sdk_sagemaker_metrics.types.experiment_entity_name.ExperimentEntityName",
        metric_data: "aws_sdk_sagemaker_metrics.types.raw_metric_data_list.RawMetricDataList",
        *,
        config_overrides: Optional[AsyncSageMakerMetricsClientConfig] = None,
    ) -> "aws_sdk_sagemaker_metrics.types.batch_put_metrics_response.BatchPutMetricsResponse":
        """<p>Used to ingest training metrics into SageMaker. These metrics can be visualized in SageMaker Studio. </p>

        Args:
            trial_component_name: <p>The name of the Trial Component to associate with the metrics. The Trial Component name must be entirely lowercase.</p>
            metric_data: <p>A list of raw metric values to put.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_metrics.types.batch_put_metrics_request.BatchPutMetricsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_metrics.types.batch_put_metrics_response.BatchPutMetricsResponse"
        ]:
            import aws_sdk_sagemaker_metrics._operations.sage_maker_metrics_service.batch_put_metrics

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_metrics._operations.sage_maker_metrics_service.batch_put_metrics.async_batch_put_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_metrics.types.batch_put_metrics_request.BatchPutMetricsRequest = {}  # type: ignore[typeddict-item]
        input_["trial_component_name"] = trial_component_name
        input_["metric_data"] = metric_data

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
