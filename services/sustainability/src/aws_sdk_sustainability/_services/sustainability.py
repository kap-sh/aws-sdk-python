"""Generated from Smithy shape ``com.amazonaws.sustainability#AwsSustainabilityApiService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_sustainability._auth._signers
import aws_sdk_sustainability._auth._sigv4
from aws_sdk_sustainability._auth._identity import Credentials
from aws_sdk_sustainability._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_sustainability._auth._zapros_handler import AuthMiddleware
from aws_sdk_sustainability._pagination import resolve_path as _resolve_path
from aws_sdk_sustainability._services._aws_config import aws_config
from aws_sdk_sustainability._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.dimension_entry
    import aws_sdk_sustainability.types.dimension_list
    import aws_sdk_sustainability.types.emissions_type_list
    import aws_sdk_sustainability.types.estimated_carbon_emissions
    import aws_sdk_sustainability.types.filter_expression
    import aws_sdk_sustainability.types.get_estimated_carbon_emissions_dimension_values_request
    import aws_sdk_sustainability.types.get_estimated_carbon_emissions_dimension_values_response
    import aws_sdk_sustainability.types.get_estimated_carbon_emissions_request
    import aws_sdk_sustainability.types.get_estimated_carbon_emissions_response
    import aws_sdk_sustainability.types.granularity_configuration
    import aws_sdk_sustainability.types.max_results
    import aws_sdk_sustainability.types.next_token
    import aws_sdk_sustainability.types.time_granularity
    import aws_sdk_sustainability.types.time_period


class SustainabilityClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


class SustainabilityClient:
    """A client for the ``Sustainability`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
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
        self._config = SustainabilityClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[SustainabilityClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SustainabilityClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def get_estimated_carbon_emissions(
        self,
        time_period: "aws_sdk_sustainability.types.time_period.TimePeriod",
        *,
        config_overrides: Optional[SustainabilityClientConfig] = None,
        group_by: Optional[
            "aws_sdk_sustainability.types.dimension_list.DimensionList"
        ] = None,
        filter_by: Optional[
            "aws_sdk_sustainability.types.filter_expression.FilterExpression"
        ] = None,
        emissions_types: Optional[
            "aws_sdk_sustainability.types.emissions_type_list.EmissionsTypeList"
        ] = None,
        granularity: Optional[
            "aws_sdk_sustainability.types.time_granularity.TimeGranularity"
        ] = None,
        granularity_configuration: Optional[
            "aws_sdk_sustainability.types.granularity_configuration.GranularityConfiguration"
        ] = None,
        max_results: Optional[
            "aws_sdk_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_sustainability.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_sustainability.types.get_estimated_carbon_emissions_response.GetEstimatedCarbonEmissionsResponse":
        """<p>Returns estimated carbon emission values based on customer grouping and filtering parameters. We recommend using pagination to ensure that the operation returns quickly and successfully. </p>

        Args:
            time_period: <p>The date range for fetching estimated carbon emissions.</p>
            group_by: <p>The dimensions available for grouping estimated carbon emissions.</p>
            filter_by: <p>The criteria for filtering estimated carbon emissions.</p>
            emissions_types: <p>The emission types to include in the results. If absent, returns <code>TOTAL_LBM_CARBON_EMISSIONS</code> and <code>TOTAL_MBM_CARBON_EMISSIONS</code> emissions types. </p>
            granularity: <p>The time granularity for the results. If absent, uses <code>MONTHLY</code> time granularity.</p>
            granularity_configuration: <p>Configuration for fiscal year calculations when using <code>YEARLY_FISCAL</code> or <code>QUARTERLY_FISCAL</code> granularity. </p>
            max_results: <p>The maximum number of results to return in a single call. Default is 40.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>

        Examples:
            GetEstimatedCarbonEmissionsSuccess

            >>> client.get_estimated_carbon_emissions(time_period={'Start': '2025-01-01T00:00:00.000Z', 'End': '2025-12-31T23:59:59.999Z'}, group_by=['SERVICE'], emissions_types=['TOTAL_LBM_CARBON_EMISSIONS', 'TOTAL_MBM_CARBON_EMISSIONS', 'TOTAL_SCOPE_1_CARBON_EMISSIONS', 'TOTAL_SCOPE_2_LBM_CARBON_EMISSIONS', 'TOTAL_SCOPE_2_MBM_CARBON_EMISSIONS', 'TOTAL_SCOPE_3_LBM_CARBON_EMISSIONS', 'TOTAL_SCOPE_3_MBM_CARBON_EMISSIONS'], granularity='MONTHLY')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sustainability.types.get_estimated_carbon_emissions_request.GetEstimatedCarbonEmissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_sustainability.types.get_estimated_carbon_emissions_response.GetEstimatedCarbonEmissionsResponse"
        ]:
            import aws_sdk_sustainability._operations.aws_sustainability_api_service.get_estimated_carbon_emissions

            output, http_response = (
                aws_sdk_sustainability._operations.aws_sustainability_api_service.get_estimated_carbon_emissions.get_estimated_carbon_emissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sustainability.types.get_estimated_carbon_emissions_request.GetEstimatedCarbonEmissionsRequest = {}  # type: ignore[typeddict-item]
        input_["time_period"] = time_period
        if group_by is not None:
            input_["group_by"] = group_by
        if filter_by is not None:
            input_["filter_by"] = filter_by
        if emissions_types is not None:
            input_["emissions_types"] = emissions_types
        if granularity is not None:
            input_["granularity"] = granularity
        if granularity_configuration is not None:
            input_["granularity_configuration"] = granularity_configuration
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_estimated_carbon_emissions(
        self,
        time_period: "aws_sdk_sustainability.types.time_period.TimePeriod",
        *,
        config_overrides: Optional[SustainabilityClientConfig] = None,
        group_by: Optional[
            "aws_sdk_sustainability.types.dimension_list.DimensionList"
        ] = None,
        filter_by: Optional[
            "aws_sdk_sustainability.types.filter_expression.FilterExpression"
        ] = None,
        emissions_types: Optional[
            "aws_sdk_sustainability.types.emissions_type_list.EmissionsTypeList"
        ] = None,
        granularity: Optional[
            "aws_sdk_sustainability.types.time_granularity.TimeGranularity"
        ] = None,
        granularity_configuration: Optional[
            "aws_sdk_sustainability.types.granularity_configuration.GranularityConfiguration"
        ] = None,
        max_results: Optional[
            "aws_sdk_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_sustainability.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_sustainability.types.estimated_carbon_emissions.EstimatedCarbonEmissions]":
        _token = next_token
        while True:
            _response = self.get_estimated_carbon_emissions(
                time_period,
                config_overrides=config_overrides,
                group_by=group_by,
                filter_by=filter_by,
                emissions_types=emissions_types,
                granularity=granularity,
                granularity_configuration=granularity_configuration,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_estimated_carbon_emissions_dimension_values(
        self,
        time_period: "aws_sdk_sustainability.types.time_period.TimePeriod",
        dimensions: "aws_sdk_sustainability.types.dimension_list.DimensionList",
        *,
        config_overrides: Optional[SustainabilityClientConfig] = None,
        max_results: Optional[
            "aws_sdk_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_sustainability.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_sustainability.types.get_estimated_carbon_emissions_dimension_values_response.GetEstimatedCarbonEmissionsDimensionValuesResponse":
        """<p>Returns the possible dimension values available for a customer's account. We recommend using pagination to ensure that the operation returns quickly and successfully. </p>

        Args:
            time_period: <p>The date range for fetching the dimension values.</p>
            dimensions: <p>The dimensions available for grouping estimated carbon emissions.</p>
            max_results: <p>The maximum number of results to return in a single call. Default is 40.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>

        Examples:
            GetEstimatedCarbonEmissionsDimensionValuesSuccess

            >>> client.get_estimated_carbon_emissions_dimension_values(time_period={'Start': '2025-01-01T00:00:00.000Z', 'End': '2025-12-31T23:59:59.999Z'}, dimensions=['REGION', 'SERVICE', 'USAGE_ACCOUNT_ID'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sustainability.types.get_estimated_carbon_emissions_dimension_values_request.GetEstimatedCarbonEmissionsDimensionValuesRequest]",
        ) -> OperationResponse[
            "aws_sdk_sustainability.types.get_estimated_carbon_emissions_dimension_values_response.GetEstimatedCarbonEmissionsDimensionValuesResponse"
        ]:
            import aws_sdk_sustainability._operations.aws_sustainability_api_service.get_estimated_carbon_emissions_dimension_values

            output, http_response = (
                aws_sdk_sustainability._operations.aws_sustainability_api_service.get_estimated_carbon_emissions_dimension_values.get_estimated_carbon_emissions_dimension_values(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sustainability.types.get_estimated_carbon_emissions_dimension_values_request.GetEstimatedCarbonEmissionsDimensionValuesRequest = {}  # type: ignore[typeddict-item]
        input_["time_period"] = time_period
        input_["dimensions"] = dimensions
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_estimated_carbon_emissions_dimension_values(
        self,
        time_period: "aws_sdk_sustainability.types.time_period.TimePeriod",
        dimensions: "aws_sdk_sustainability.types.dimension_list.DimensionList",
        *,
        config_overrides: Optional[SustainabilityClientConfig] = None,
        max_results: Optional[
            "aws_sdk_sustainability.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_sustainability.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_sustainability.types.dimension_entry.DimensionEntry]":
        _token = next_token
        while True:
            _response = self.get_estimated_carbon_emissions_dimension_values(
                time_period,
                dimensions,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
