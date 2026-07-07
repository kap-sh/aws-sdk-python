"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#AnyScaleScalingPlannerFrontendService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_auto_scaling_plans._auth._signers
import aws_sdk_auto_scaling_plans._auth._sigv4
from aws_sdk_auto_scaling_plans._auth._identity import Credentials
from aws_sdk_auto_scaling_plans._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_auto_scaling_plans._auth._zapros_handler import AuthMiddleware
from aws_sdk_auto_scaling_plans._services._aws_config import aaws_config
from aws_sdk_auto_scaling_plans._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.application_source
    import aws_sdk_auto_scaling_plans.types.application_sources
    import aws_sdk_auto_scaling_plans.types.create_scaling_plan_request
    import aws_sdk_auto_scaling_plans.types.create_scaling_plan_response
    import aws_sdk_auto_scaling_plans.types.delete_scaling_plan_request
    import aws_sdk_auto_scaling_plans.types.delete_scaling_plan_response
    import aws_sdk_auto_scaling_plans.types.describe_scaling_plan_resources_request
    import aws_sdk_auto_scaling_plans.types.describe_scaling_plan_resources_response
    import aws_sdk_auto_scaling_plans.types.describe_scaling_plans_request
    import aws_sdk_auto_scaling_plans.types.describe_scaling_plans_response
    import aws_sdk_auto_scaling_plans.types.forecast_data_type
    import aws_sdk_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request
    import aws_sdk_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response
    import aws_sdk_auto_scaling_plans.types.max_results
    import aws_sdk_auto_scaling_plans.types.next_token
    import aws_sdk_auto_scaling_plans.types.scalable_dimension
    import aws_sdk_auto_scaling_plans.types.scaling_instructions
    import aws_sdk_auto_scaling_plans.types.scaling_plan_name
    import aws_sdk_auto_scaling_plans.types.scaling_plan_names
    import aws_sdk_auto_scaling_plans.types.scaling_plan_version
    import aws_sdk_auto_scaling_plans.types.service_namespace
    import aws_sdk_auto_scaling_plans.types.timestamp_type
    import aws_sdk_auto_scaling_plans.types.update_scaling_plan_request
    import aws_sdk_auto_scaling_plans.types.update_scaling_plan_response
    import aws_sdk_auto_scaling_plans.types.xml_string


class AsyncAutoScalingPlansClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncAutoScalingPlansClient:
    """A client for the ``AutoScalingPlans`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncAutoScalingPlansClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncAutoScalingPlansClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAutoScalingPlansClientConfig = config_overrides or {}
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

    async def create_scaling_plan(
        self,
        scaling_plan_name: "aws_sdk_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName",
        application_source: "aws_sdk_auto_scaling_plans.types.application_source.ApplicationSource",
        scaling_instructions: "aws_sdk_auto_scaling_plans.types.scaling_instructions.ScalingInstructions",
        *,
        config_overrides: Optional[AsyncAutoScalingPlansClientConfig] = None,
    ) -> "aws_sdk_auto_scaling_plans.types.create_scaling_plan_response.CreateScalingPlanResponse":
        r"""<p>Creates a scaling plan. </p>

        Args:
            scaling_plan_name: <p>The name of the scaling plan. Names cannot contain vertical bars, colons, or forward slashes.</p>
            application_source: <p>A CloudFormation stack or set of tags. You can create one scaling plan per application source.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ApplicationSource.html\">ApplicationSource</a> in the <i>AWS Auto Scaling API Reference</i>.</p>
            scaling_instructions: <p>The scaling instructions.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingInstruction.html\">ScalingInstruction</a> in the <i>AWS Auto Scaling API Reference</i>.</p>

        Raises:
            aws_sdk_auto_scaling_plans.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.</p>
            aws_sdk_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            aws_sdk_auto_scaling_plans.errors.limit_exceeded_exception.LimitExceededException: <p>Your account exceeded a limit. This exception is thrown when a per-account resource limit is exceeded.</p>
            aws_sdk_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            aws_sdk_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_auto_scaling_plans.types.create_scaling_plan_request.CreateScalingPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_auto_scaling_plans.types.create_scaling_plan_response.CreateScalingPlanResponse"
        ]:
            import aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.create_scaling_plan

            (
                output,
                http_response,
            ) = await aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.create_scaling_plan.async_create_scaling_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_auto_scaling_plans.types.create_scaling_plan_request.CreateScalingPlanRequest = {}  # type: ignore[typeddict-item]
        input_["scaling_plan_name"] = scaling_plan_name
        input_["application_source"] = application_source
        input_["scaling_instructions"] = scaling_instructions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_scaling_plan(
        self,
        scaling_plan_name: "aws_sdk_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName",
        scaling_plan_version: "aws_sdk_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion",
        *,
        config_overrides: Optional[AsyncAutoScalingPlansClientConfig] = None,
    ) -> "aws_sdk_auto_scaling_plans.types.delete_scaling_plan_response.DeleteScalingPlanResponse":
        """<p>Deletes the specified scaling plan.</p> <p>Deleting a scaling plan deletes the underlying <a>ScalingInstruction</a> for all of the scalable resources that are covered by the plan.</p> <p>If the plan has launched resources or has scaling activities in progress, you must delete those resources separately.</p>

        Args:
            scaling_plan_name: <p>The name of the scaling plan.</p>
            scaling_plan_version: <p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>

        Raises:
            aws_sdk_auto_scaling_plans.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.</p>
            aws_sdk_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            aws_sdk_auto_scaling_plans.errors.object_not_found_exception.ObjectNotFoundException: <p>The specified object could not be found.</p>
            aws_sdk_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            aws_sdk_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_auto_scaling_plans.types.delete_scaling_plan_request.DeleteScalingPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_auto_scaling_plans.types.delete_scaling_plan_response.DeleteScalingPlanResponse"
        ]:
            import aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.delete_scaling_plan

            (
                output,
                http_response,
            ) = await aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.delete_scaling_plan.async_delete_scaling_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_auto_scaling_plans.types.delete_scaling_plan_request.DeleteScalingPlanRequest = {}  # type: ignore[typeddict-item]
        input_["scaling_plan_name"] = scaling_plan_name
        input_["scaling_plan_version"] = scaling_plan_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_scaling_plan_resources(
        self,
        scaling_plan_name: "aws_sdk_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName",
        scaling_plan_version: "aws_sdk_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion",
        *,
        config_overrides: Optional[AsyncAutoScalingPlansClientConfig] = None,
        max_results: Optional[
            "aws_sdk_auto_scaling_plans.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_auto_scaling_plans.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_auto_scaling_plans.types.describe_scaling_plan_resources_response.DescribeScalingPlanResourcesResponse":
        """<p>Describes the scalable resources in the specified scaling plan.</p>

        Args:
            scaling_plan_name: <p>The name of the scaling plan.</p>
            scaling_plan_version: <p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>
            max_results: <p>The maximum number of scalable resources to return. The value must be between 1 and 50. The default value is 50.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            aws_sdk_auto_scaling_plans.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.</p>
            aws_sdk_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            aws_sdk_auto_scaling_plans.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token provided is not valid.</p>
            aws_sdk_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            aws_sdk_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_auto_scaling_plans.types.describe_scaling_plan_resources_request.DescribeScalingPlanResourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_auto_scaling_plans.types.describe_scaling_plan_resources_response.DescribeScalingPlanResourcesResponse"
        ]:
            import aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.describe_scaling_plan_resources

            (
                output,
                http_response,
            ) = await aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.describe_scaling_plan_resources.async_describe_scaling_plan_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_auto_scaling_plans.types.describe_scaling_plan_resources_request.DescribeScalingPlanResourcesRequest = {}  # type: ignore[typeddict-item]
        input_["scaling_plan_name"] = scaling_plan_name
        input_["scaling_plan_version"] = scaling_plan_version
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_scaling_plans(
        self,
        *,
        config_overrides: Optional[AsyncAutoScalingPlansClientConfig] = None,
        scaling_plan_names: Optional[
            "aws_sdk_auto_scaling_plans.types.scaling_plan_names.ScalingPlanNames"
        ] = None,
        scaling_plan_version: Optional[
            "aws_sdk_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion"
        ] = None,
        application_sources: Optional[
            "aws_sdk_auto_scaling_plans.types.application_sources.ApplicationSources"
        ] = None,
        max_results: Optional[
            "aws_sdk_auto_scaling_plans.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_auto_scaling_plans.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_auto_scaling_plans.types.describe_scaling_plans_response.DescribeScalingPlansResponse":
        """<p>Describes one or more of your scaling plans.</p>

        Args:
            scaling_plan_names: <p>The names of the scaling plans (up to 10). If you specify application sources, you cannot specify scaling plan names.</p>
            scaling_plan_version: <p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p> <note> <p>If you specify a scaling plan version, you must also specify a scaling plan name.</p> </note>
            application_sources: <p>The sources for the applications (up to 10). If you specify scaling plan names, you cannot specify application sources.</p>
            max_results: <p>The maximum number of scalable resources to return. This value can be between 1 and 50. The default value is 50.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            aws_sdk_auto_scaling_plans.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.</p>
            aws_sdk_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            aws_sdk_auto_scaling_plans.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The token provided is not valid.</p>
            aws_sdk_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            aws_sdk_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_auto_scaling_plans.types.describe_scaling_plans_request.DescribeScalingPlansRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_auto_scaling_plans.types.describe_scaling_plans_response.DescribeScalingPlansResponse"
        ]:
            import aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.describe_scaling_plans

            (
                output,
                http_response,
            ) = await aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.describe_scaling_plans.async_describe_scaling_plans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_auto_scaling_plans.types.describe_scaling_plans_request.DescribeScalingPlansRequest = {}  # type: ignore[typeddict-item]
        if scaling_plan_names is not None:
            input_["scaling_plan_names"] = scaling_plan_names
        if scaling_plan_version is not None:
            input_["scaling_plan_version"] = scaling_plan_version
        if application_sources is not None:
            input_["application_sources"] = application_sources
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_scaling_plan_resource_forecast_data(
        self,
        scaling_plan_name: "aws_sdk_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName",
        scaling_plan_version: "aws_sdk_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion",
        service_namespace: "aws_sdk_auto_scaling_plans.types.service_namespace.ServiceNamespace",
        resource_id: "aws_sdk_auto_scaling_plans.types.xml_string.XmlString",
        scalable_dimension: "aws_sdk_auto_scaling_plans.types.scalable_dimension.ScalableDimension",
        forecast_data_type: "aws_sdk_auto_scaling_plans.types.forecast_data_type.ForecastDataType",
        start_time: "aws_sdk_auto_scaling_plans.types.timestamp_type.TimestampType",
        end_time: "aws_sdk_auto_scaling_plans.types.timestamp_type.TimestampType",
        *,
        config_overrides: Optional[AsyncAutoScalingPlansClientConfig] = None,
    ) -> "aws_sdk_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.GetScalingPlanResourceForecastDataResponse":
        """<p>Retrieves the forecast data for a scalable resource.</p> <p>Capacity forecasts are represented as predicted values, or data points, that are calculated using historical data points from a specified CloudWatch load metric. Data points are available for up to 56 days. </p>

        Args:
            scaling_plan_name: <p>The name of the scaling plan.</p>
            scaling_plan_version: <p>The version number of the scaling plan. Currently, the only valid value is <code>1</code>.</p>
            service_namespace: <p>The namespace of the AWS service. The only valid value is <code>autoscaling</code>. </p>
            resource_id: <p>The ID of the resource. This string consists of a prefix (<code>autoScalingGroup</code>) followed by the name of a specified Auto Scaling group (<code>my-asg</code>). Example: <code>autoScalingGroup/my-asg</code>. </p>
            scalable_dimension: <p>The scalable dimension for the resource. The only valid value is <code>autoscaling:autoScalingGroup:DesiredCapacity</code>. </p>
            forecast_data_type: <p>The type of forecast data to get.</p> <ul> <li> <p> <code>LoadForecast</code>: The load metric forecast. </p> </li> <li> <p> <code>CapacityForecast</code>: The capacity forecast. </p> </li> <li> <p> <code>ScheduledActionMinCapacity</code>: The minimum capacity for each scheduled scaling action. This data is calculated as the larger of two values: the capacity forecast or the minimum capacity in the scaling instruction.</p> </li> <li> <p> <code>ScheduledActionMaxCapacity</code>: The maximum capacity for each scheduled scaling action. The calculation used is determined by the predictive scaling maximum capacity behavior setting in the scaling instruction.</p> </li> </ul>
            start_time: <p>The inclusive start time of the time range for the forecast data to get. The date and time can be at most 56 days before the current date and time. </p>
            end_time: <p>The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is seven days. </p> <p>Although this parameter can accept a date and time that is more than two days in the future, the availability of forecast data has limits. AWS Auto Scaling only issues forecasts for periods of two days in advance.</p>

        Raises:
            aws_sdk_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            aws_sdk_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            aws_sdk_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request.GetScalingPlanResourceForecastDataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_response.GetScalingPlanResourceForecastDataResponse"
        ]:
            import aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.get_scaling_plan_resource_forecast_data

            (
                output,
                http_response,
            ) = await aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.get_scaling_plan_resource_forecast_data.async_get_scaling_plan_resource_forecast_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_auto_scaling_plans.types.get_scaling_plan_resource_forecast_data_request.GetScalingPlanResourceForecastDataRequest = {}  # type: ignore[typeddict-item]
        input_["scaling_plan_name"] = scaling_plan_name
        input_["scaling_plan_version"] = scaling_plan_version
        input_["service_namespace"] = service_namespace
        input_["resource_id"] = resource_id
        input_["scalable_dimension"] = scalable_dimension
        input_["forecast_data_type"] = forecast_data_type
        input_["start_time"] = start_time
        input_["end_time"] = end_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_scaling_plan(
        self,
        scaling_plan_name: "aws_sdk_auto_scaling_plans.types.scaling_plan_name.ScalingPlanName",
        scaling_plan_version: "aws_sdk_auto_scaling_plans.types.scaling_plan_version.ScalingPlanVersion",
        *,
        config_overrides: Optional[AsyncAutoScalingPlansClientConfig] = None,
        application_source: Optional[
            "aws_sdk_auto_scaling_plans.types.application_source.ApplicationSource"
        ] = None,
        scaling_instructions: Optional[
            "aws_sdk_auto_scaling_plans.types.scaling_instructions.ScalingInstructions"
        ] = None,
    ) -> "aws_sdk_auto_scaling_plans.types.update_scaling_plan_response.UpdateScalingPlanResponse":
        r"""<p>Updates the specified scaling plan.</p> <p>You cannot update a scaling plan if it is in the process of being created, updated, or deleted.</p>

        Args:
            scaling_plan_name: <p>The name of the scaling plan.</p>
            scaling_plan_version: <p>The version number of the scaling plan. The only valid value is <code>1</code>. Currently, you cannot have multiple scaling plan versions.</p>
            application_source: <p>A CloudFormation stack or set of tags.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ApplicationSource.html\">ApplicationSource</a> in the <i>AWS Auto Scaling API Reference</i>.</p>
            scaling_instructions: <p>The scaling instructions.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingInstruction.html\">ScalingInstruction</a> in the <i>AWS Auto Scaling API Reference</i>.</p>

        Raises:
            aws_sdk_auto_scaling_plans.errors.concurrent_update_exception.ConcurrentUpdateException: <p>Concurrent updates caused an exception, for example, if you request an update to a scaling plan that already has a pending update.</p>
            aws_sdk_auto_scaling_plans.errors.internal_service_exception.InternalServiceException: <p>The service encountered an internal error.</p>
            aws_sdk_auto_scaling_plans.errors.object_not_found_exception.ObjectNotFoundException: <p>The specified object could not be found.</p>
            aws_sdk_auto_scaling_plans.errors.validation_exception.ValidationException: <p>An exception was thrown for a validation issue. Review the parameters provided.</p>
            aws_sdk_auto_scaling_plans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_auto_scaling_plans.types.update_scaling_plan_request.UpdateScalingPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_auto_scaling_plans.types.update_scaling_plan_response.UpdateScalingPlanResponse"
        ]:
            import aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.update_scaling_plan

            (
                output,
                http_response,
            ) = await aws_sdk_auto_scaling_plans._operations.any_scale_scaling_planner_frontend_service.update_scaling_plan.async_update_scaling_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_auto_scaling_plans.types.update_scaling_plan_request.UpdateScalingPlanRequest = {}  # type: ignore[typeddict-item]
        input_["scaling_plan_name"] = scaling_plan_name
        input_["scaling_plan_version"] = scaling_plan_version
        if application_source is not None:
            input_["application_source"] = application_source
        if scaling_instructions is not None:
            input_["scaling_instructions"] = scaling_instructions

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
