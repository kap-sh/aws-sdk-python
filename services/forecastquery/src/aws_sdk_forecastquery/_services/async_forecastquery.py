"""Generated from Smithy shape ``com.amazonaws.forecastquery#AmazonForecastRuntime``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_forecastquery._auth._signers
import aws_sdk_forecastquery._auth._sigv4
from aws_sdk_forecastquery._auth._identity import Credentials
from aws_sdk_forecastquery._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_forecastquery._auth._zapros_handler import AuthMiddleware
from aws_sdk_forecastquery._services._aws_config import aaws_config
from aws_sdk_forecastquery._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_forecastquery.types.arn
    import aws_sdk_forecastquery.types.date_time
    import aws_sdk_forecastquery.types.filters
    import aws_sdk_forecastquery.types.long_arn
    import aws_sdk_forecastquery.types.next_token
    import aws_sdk_forecastquery.types.query_forecast_request
    import aws_sdk_forecastquery.types.query_forecast_response
    import aws_sdk_forecastquery.types.query_what_if_forecast_request
    import aws_sdk_forecastquery.types.query_what_if_forecast_response


class AsyncforecastqueryClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class AsyncforecastqueryClient:
    """A client for the ``forecastquery`` service.

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
        self._config = AsyncforecastqueryClientConfig(
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
        self, config_overrides: Optional[AsyncforecastqueryClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncforecastqueryClientConfig = config_overrides or {}
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

    async def query_forecast(
        self,
        forecast_arn: "aws_sdk_forecastquery.types.arn.Arn",
        filters: "aws_sdk_forecastquery.types.filters.Filters",
        *,
        config_overrides: Optional[AsyncforecastqueryClientConfig] = None,
        start_date: Optional["aws_sdk_forecastquery.types.date_time.DateTime"] = None,
        end_date: Optional["aws_sdk_forecastquery.types.date_time.DateTime"] = None,
        next_token: Optional["aws_sdk_forecastquery.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_forecastquery.types.query_forecast_response.QueryForecastResponse":
        r"""<p>Retrieves a forecast for a single item, filtered by the supplied criteria.</p> <p>The criteria is a key-value pair. The key is either <code>item_id</code> (or the equivalent non-timestamp, non-target field) from the <code>TARGET_TIME_SERIES</code> dataset, or one of the forecast dimensions specified as part of the <code>FeaturizationConfig</code> object.</p> <p>By default, <code>QueryForecast</code> returns the complete date range for the filtered forecast. You can request a specific date range.</p> <p>To get the full forecast, use the <a href=\"https://docs.aws.amazon.com/en_us/forecast/latest/dg/API_CreateForecastExportJob.html\">CreateForecastExportJob</a> operation.</p> <note> <p>The forecasts generated by Amazon Forecast are in the same timezone as the dataset that was used to create the predictor.</p> </note>

        Args:
            forecast_arn: <p>The Amazon Resource Name (ARN) of the forecast to query.</p>
            start_date: <p>The start date for the forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T08:00:00.</p>
            end_date: <p>The end date for the forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T20:00:00. </p>
            filters: <p>The filtering criteria to apply when retrieving the forecast. For example, to get the forecast for <code>client_21</code> in the electricity usage dataset, specify the following:</p> <p> <code>{\"item_id\" : \"client_21\"}</code> </p> <p>To get the full forecast, use the <a href=\"https://docs.aws.amazon.com/en_us/forecast/latest/dg/API_CreateForecastExportJob.html\">CreateForecastExportJob</a> operation.</p>
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_forecastquery.types.query_forecast_request.QueryForecastRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_forecastquery.types.query_forecast_response.QueryForecastResponse"
        ]:
            import aws_sdk_forecastquery._operations.amazon_forecast_runtime.query_forecast

            (
                output,
                http_response,
            ) = await aws_sdk_forecastquery._operations.amazon_forecast_runtime.query_forecast.async_query_forecast(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_forecastquery.types.query_forecast_request.QueryForecastRequest = {}  # type: ignore[typeddict-item]
        input_["forecast_arn"] = forecast_arn
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def query_what_if_forecast(
        self,
        what_if_forecast_arn: "aws_sdk_forecastquery.types.long_arn.LongArn",
        filters: "aws_sdk_forecastquery.types.filters.Filters",
        *,
        config_overrides: Optional[AsyncforecastqueryClientConfig] = None,
        start_date: Optional["aws_sdk_forecastquery.types.date_time.DateTime"] = None,
        end_date: Optional["aws_sdk_forecastquery.types.date_time.DateTime"] = None,
        next_token: Optional["aws_sdk_forecastquery.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_forecastquery.types.query_what_if_forecast_response.QueryWhatIfForecastResponse":
        r"""<p>Retrieves a what-if forecast.</p>

        Args:
            what_if_forecast_arn: <p>The Amazon Resource Name (ARN) of the what-if forecast to query.</p>
            start_date: <p>The start date for the what-if forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T08:00:00.</p>
            end_date: <p>The end date for the what-if forecast. Specify the date using this format: yyyy-MM-dd'T'HH:mm:ss (ISO 8601 format). For example, 2015-01-01T20:00:00. </p>
            filters: <p>The filtering criteria to apply when retrieving the forecast. For example, to get the forecast for <code>client_21</code> in the electricity usage dataset, specify the following:</p> <p> <code>{\"item_id\" : \"client_21\"}</code> </p> <p>To get the full what-if forecast, use the <a href=\"https://docs.aws.amazon.com/en_us/forecast/latest/dg/API_CreateWhatIfForecastExport.html\">CreateForecastExportJob</a> operation.</p>
            next_token: <p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_forecastquery.types.query_what_if_forecast_request.QueryWhatIfForecastRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_forecastquery.types.query_what_if_forecast_response.QueryWhatIfForecastResponse"
        ]:
            import aws_sdk_forecastquery._operations.amazon_forecast_runtime.query_what_if_forecast

            (
                output,
                http_response,
            ) = await aws_sdk_forecastquery._operations.amazon_forecast_runtime.query_what_if_forecast.async_query_what_if_forecast(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_forecastquery.types.query_what_if_forecast_request.QueryWhatIfForecastRequest = {}  # type: ignore[typeddict-item]
        input_["what_if_forecast_arn"] = what_if_forecast_arn
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

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
