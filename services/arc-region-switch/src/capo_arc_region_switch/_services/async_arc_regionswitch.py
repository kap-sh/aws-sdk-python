"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ArcRegionSwitch``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_arc_region_switch._auth._signers
import capo_arc_region_switch._auth._sigv4
from capo_arc_region_switch._auth._identity import Credentials
from capo_arc_region_switch._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_arc_region_switch._auth._zapros_handler import AuthMiddleware
from capo_arc_region_switch._pagination import resolve_path as _resolve_path
from capo_arc_region_switch._resources.arc_region_switch.region_switch_plan import (
    AsyncRegionSwitchPlan,
)
from capo_arc_region_switch._services._aws_config import aaws_config
from capo_arc_region_switch._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_arc_region_switch.types.abbreviated_execution
    import capo_arc_region_switch.types.abbreviated_plan
    import capo_arc_region_switch.types.approval
    import capo_arc_region_switch.types.approve_plan_execution_step_request
    import capo_arc_region_switch.types.approve_plan_execution_step_response
    import capo_arc_region_switch.types.cancel_plan_execution_request
    import capo_arc_region_switch.types.cancel_plan_execution_response
    import capo_arc_region_switch.types.execution_action
    import capo_arc_region_switch.types.execution_comment
    import capo_arc_region_switch.types.execution_event
    import capo_arc_region_switch.types.execution_id
    import capo_arc_region_switch.types.execution_mode
    import capo_arc_region_switch.types.execution_state
    import capo_arc_region_switch.types.get_plan_evaluation_status_request
    import capo_arc_region_switch.types.get_plan_evaluation_status_response
    import capo_arc_region_switch.types.get_plan_execution_request
    import capo_arc_region_switch.types.get_plan_execution_response
    import capo_arc_region_switch.types.get_plan_execution_step_states_max_results
    import capo_arc_region_switch.types.get_plan_in_region_request
    import capo_arc_region_switch.types.get_plan_in_region_response
    import capo_arc_region_switch.types.list_execution_events_max_results
    import capo_arc_region_switch.types.list_executions_max_results
    import capo_arc_region_switch.types.list_plan_execution_events_request
    import capo_arc_region_switch.types.list_plan_execution_events_response
    import capo_arc_region_switch.types.list_plan_executions_request
    import capo_arc_region_switch.types.list_plan_executions_response
    import capo_arc_region_switch.types.list_plans_in_region_request
    import capo_arc_region_switch.types.list_plans_in_region_response
    import capo_arc_region_switch.types.list_route53_health_checks_in_region_request
    import capo_arc_region_switch.types.list_route53_health_checks_in_region_response
    import capo_arc_region_switch.types.list_route53_health_checks_request
    import capo_arc_region_switch.types.list_route53_health_checks_response
    import capo_arc_region_switch.types.max_results
    import capo_arc_region_switch.types.next_token
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.recovery_execution_id
    import capo_arc_region_switch.types.resource_warning
    import capo_arc_region_switch.types.route53_health_check
    import capo_arc_region_switch.types.route53_hosted_zone_id
    import capo_arc_region_switch.types.route53_record_name
    import capo_arc_region_switch.types.start_plan_execution_request
    import capo_arc_region_switch.types.start_plan_execution_response
    import capo_arc_region_switch.types.step_name
    import capo_arc_region_switch.types.step_state
    import capo_arc_region_switch.types.update_plan_execution_action
    import capo_arc_region_switch.types.update_plan_execution_request
    import capo_arc_region_switch.types.update_plan_execution_response
    import capo_arc_region_switch.types.update_plan_execution_step_action
    import capo_arc_region_switch.types.update_plan_execution_step_request
    import capo_arc_region_switch.types.update_plan_execution_step_response


class AsyncARCRegionswitchClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncARCRegionswitchClient:
    """A client for the ``ARCRegionswitch`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncARCRegionswitchClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.region_switch_plan = AsyncRegionSwitchPlan(self)

    def operation_options(
        self, config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncARCRegionswitchClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def approve_plan_execution_step(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        step_name: "capo_arc_region_switch.types.step_name.StepName",
        approval: "capo_arc_region_switch.types.approval.Approval",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        comment: Optional[
            "capo_arc_region_switch.types.execution_comment.ExecutionComment"
        ] = None,
    ) -> "capo_arc_region_switch.types.approve_plan_execution_step_response.ApprovePlanExecutionStepResponse":
        """<p>Approves a step in a plan execution that requires manual approval. When you create a plan, you can include approval steps that require manual intervention before the execution can proceed. This operation allows you to provide that approval.</p> <p>You must specify the plan ARN, execution ID, step name, and approval status. You can also provide an optional comment explaining the approval decision.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan.</p>
            execution_id: <p>The execution identifier of a plan execution.</p>
            step_name: <p>The name of a step in a plan execution.</p>
            approval: <p>The status of approval for a plan execution step. </p>
            comment: <p>A comment that you can enter about a plan execution.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.approve_plan_execution_step_request.ApprovePlanExecutionStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.approve_plan_execution_step_response.ApprovePlanExecutionStepResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.approve_plan_execution_step

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.approve_plan_execution_step.async_approve_plan_execution_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.approve_plan_execution_step_request.ApprovePlanExecutionStepRequest = {}  # type: ignore[typeddict-item]
        input_["plan_arn"] = plan_arn
        input_["execution_id"] = execution_id
        input_["step_name"] = step_name
        input_["approval"] = approval
        if comment is not None:
            input_["comment"] = comment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_plan_execution(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        comment: Optional[
            "capo_arc_region_switch.types.execution_comment.ExecutionComment"
        ] = None,
    ) -> "capo_arc_region_switch.types.cancel_plan_execution_response.CancelPlanExecutionResponse":
        """<p>Cancels an in-progress plan execution. This operation stops the execution of the plan and prevents any further steps from being processed.</p> <p>You must specify the plan ARN and execution ID. You can also provide an optional comment explaining why the execution was canceled.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan.</p>
            execution_id: <p>The execution identifier of a plan execution.</p>
            comment: <p>A comment that you can enter about canceling a plan execution step.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.cancel_plan_execution_request.CancelPlanExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.cancel_plan_execution_response.CancelPlanExecutionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.cancel_plan_execution

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.cancel_plan_execution.async_cancel_plan_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.cancel_plan_execution_request.CancelPlanExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["plan_arn"] = plan_arn
        input_["execution_id"] = execution_id
        if comment is not None:
            input_["comment"] = comment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_plan_evaluation_status(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.get_plan_evaluation_status_response.GetPlanEvaluationStatusResponse":
        """<p>Retrieves the evaluation status of a Region switch plan. The evaluation status provides information about the last time the plan was evaluated and any warnings or issues detected.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the Region switch plan to retrieve evaluation status for.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.get_plan_evaluation_status_request.GetPlanEvaluationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.get_plan_evaluation_status_response.GetPlanEvaluationStatusResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.get_plan_evaluation_status

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.get_plan_evaluation_status.async_get_plan_evaluation_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.get_plan_evaluation_status_request.GetPlanEvaluationStatusRequest = {}  # type: ignore[typeddict-item]
        input_["plan_arn"] = plan_arn
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

    async def iter_get_plan_evaluation_status(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.resource_warning.ResourceWarning]":
        _token = next_token
        while True:
            _response = await self.get_plan_evaluation_status(
                plan_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("warnings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_plan_execution(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.get_plan_execution_step_states_max_results.GetPlanExecutionStepStatesMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_arc_region_switch.types.get_plan_execution_response.GetPlanExecutionResponse":
        """<p>Retrieves detailed information about a specific plan execution. You must specify the plan ARN and execution ID.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan with the execution to retrieve.</p>
            execution_id: <p>The execution identifier of a plan execution.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.get_plan_execution_request.GetPlanExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.get_plan_execution_response.GetPlanExecutionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.get_plan_execution

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.get_plan_execution.async_get_plan_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.get_plan_execution_request.GetPlanExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["plan_arn"] = plan_arn
        input_["execution_id"] = execution_id
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

    async def iter_get_plan_execution(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.get_plan_execution_step_states_max_results.GetPlanExecutionStepStatesMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.step_state.StepState]":
        _token = next_token
        while True:
            _response = await self.get_plan_execution(
                plan_arn,
                execution_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("step_states",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_plan_in_region(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.get_plan_in_region_response.GetPlanInRegionResponse":
        """<p>Retrieves information about a Region switch plan in a specific Amazon Web Services Region. This operation is useful for getting Region-specific information about a plan.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan in Region.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.get_plan_in_region_request.GetPlanInRegionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.get_plan_in_region_response.GetPlanInRegionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.get_plan_in_region

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.get_plan_in_region.async_get_plan_in_region(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.get_plan_in_region_request.GetPlanInRegionRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_plan_execution_events(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.list_execution_events_max_results.ListExecutionEventsMaxResults"
        ] = None,
        next_token: Optional[str] = None,
        name: Optional["capo_arc_region_switch.types.step_name.StepName"] = None,
    ) -> "capo_arc_region_switch.types.list_plan_execution_events_response.ListPlanExecutionEventsResponse":
        """<p>Lists the events that occurred during a plan execution. These events provide a detailed timeline of the execution process.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan.</p>
            execution_id: <p>The execution identifier of a plan execution.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            name: <p>The name of the plan execution event.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_plan_execution_events_request.ListPlanExecutionEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_plan_execution_events_response.ListPlanExecutionEventsResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_plan_execution_events

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_plan_execution_events.async_list_plan_execution_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_plan_execution_events_request.ListPlanExecutionEventsRequest = {}  # type: ignore[typeddict-item]
        input_["plan_arn"] = plan_arn
        input_["execution_id"] = execution_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_plan_execution_events(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.list_execution_events_max_results.ListExecutionEventsMaxResults"
        ] = None,
        next_token: Optional[str] = None,
        name: Optional["capo_arc_region_switch.types.step_name.StepName"] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.execution_event.ExecutionEvent]":
        _token = next_token
        while True:
            _response = await self.list_plan_execution_events(
                plan_arn,
                execution_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name=name,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_plan_executions(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.list_executions_max_results.ListExecutionsMaxResults"
        ] = None,
        next_token: Optional[str] = None,
        state: Optional[
            "capo_arc_region_switch.types.execution_state.ExecutionState"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_plan_executions_response.ListPlanExecutionsResponse":
        """<p>Lists the executions of a Region switch plan. This operation returns information about both current and historical executions.</p>

        Args:
            plan_arn: <p>The ARN for the plan.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            state: <p>The state of the plan execution. For example, the plan execution might be In Progress.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_plan_executions_request.ListPlanExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_plan_executions_response.ListPlanExecutionsResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_plan_executions

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_plan_executions.async_list_plan_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_plan_executions_request.ListPlanExecutionsRequest = {}  # type: ignore[typeddict-item]
        input_["plan_arn"] = plan_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state is not None:
            input_["state"] = state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_plan_executions(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.list_executions_max_results.ListExecutionsMaxResults"
        ] = None,
        next_token: Optional[str] = None,
        state: Optional[
            "capo_arc_region_switch.types.execution_state.ExecutionState"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.abbreviated_execution.AbbreviatedExecution]":
        _token = next_token
        while True:
            _response = await self.list_plan_executions(
                plan_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state=state,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_plans_in_region(
        self,
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_plans_in_region_response.ListPlansInRegionResponse":
        """<p>Lists all Region switch plans in your Amazon Web Services account that are available in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_plans_in_region_request.ListPlansInRegionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_plans_in_region_response.ListPlansInRegionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_plans_in_region

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_plans_in_region.async_list_plans_in_region(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_plans_in_region_request.ListPlansInRegionRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_plans_in_region(
        self,
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.abbreviated_plan.AbbreviatedPlan]":
        _token = next_token
        while True:
            _response = await self.list_plans_in_region(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("plans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_route53_health_checks(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        hosted_zone_id: Optional[
            "capo_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
        ] = None,
        record_name: Optional[
            "capo_arc_region_switch.types.route53_record_name.Route53RecordName"
        ] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_route53_health_checks_response.ListRoute53HealthChecksResponse":
        """<p>List the Amazon Route 53 health checks.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Amazon Route 53 health check request.</p>
            hosted_zone_id: <p>The hosted zone ID for the health checks.</p>
            record_name: <p>The record name for the health checks.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.illegal_argument_exception.IllegalArgumentException: <p>The request processing has an invalid argument.</p>
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_route53_health_checks_request.ListRoute53HealthChecksRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_route53_health_checks_response.ListRoute53HealthChecksResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_route53_health_checks

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_route53_health_checks.async_list_route53_health_checks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_route53_health_checks_request.ListRoute53HealthChecksRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if hosted_zone_id is not None:
            input_["hosted_zone_id"] = hosted_zone_id
        if record_name is not None:
            input_["record_name"] = record_name
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

    async def iter_list_route53_health_checks(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        hosted_zone_id: Optional[
            "capo_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
        ] = None,
        record_name: Optional[
            "capo_arc_region_switch.types.route53_record_name.Route53RecordName"
        ] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.route53_health_check.Route53HealthCheck]":
        _token = next_token
        while True:
            _response = await self.list_route53_health_checks(
                arn,
                config_overrides=config_overrides,
                hosted_zone_id=hosted_zone_id,
                record_name=record_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("health_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_route53_health_checks_in_region(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        hosted_zone_id: Optional[
            "capo_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
        ] = None,
        record_name: Optional[
            "capo_arc_region_switch.types.route53_record_name.Route53RecordName"
        ] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_route53_health_checks_in_region_response.ListRoute53HealthChecksInRegionResponse":
        """<p>List the Amazon Route 53 health checks in a specific Amazon Web Services Region.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Arc Region Switch Plan.</p>
            hosted_zone_id: <p>The hosted zone ID for the health checks.</p>
            record_name: <p>The record name for the health checks.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.illegal_argument_exception.IllegalArgumentException: <p>The request processing has an invalid argument.</p>
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example ListRoute53HealthChecksInRegion

            >>> await client.list_route53_health_checks_in_region(arn='arn:aws:arc-region-switch::123456789012:plan/example:000000', hosted_zone_id='Z0123456789ABCDEFGHI', record_name='my.record.name', max_results=10, next_token='eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxfQ')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_route53_health_checks_in_region_request.ListRoute53HealthChecksInRegionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_route53_health_checks_in_region_response.ListRoute53HealthChecksInRegionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_route53_health_checks_in_region

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_route53_health_checks_in_region.async_list_route53_health_checks_in_region(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_route53_health_checks_in_region_request.ListRoute53HealthChecksInRegionRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if hosted_zone_id is not None:
            input_["hosted_zone_id"] = hosted_zone_id
        if record_name is not None:
            input_["record_name"] = record_name
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

    async def iter_list_route53_health_checks_in_region(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        hosted_zone_id: Optional[
            "capo_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
        ] = None,
        record_name: Optional[
            "capo_arc_region_switch.types.route53_record_name.Route53RecordName"
        ] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.route53_health_check.Route53HealthCheck]":
        _token = next_token
        while True:
            _response = await self.list_route53_health_checks_in_region(
                arn,
                config_overrides=config_overrides,
                hosted_zone_id=hosted_zone_id,
                record_name=record_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("health_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_plan_execution(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        target_region: str,
        action: "capo_arc_region_switch.types.execution_action.ExecutionAction",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        mode: Optional[
            "capo_arc_region_switch.types.execution_mode.ExecutionMode"
        ] = None,
        comment: Optional[
            "capo_arc_region_switch.types.execution_comment.ExecutionComment"
        ] = None,
        latest_version: Optional[str] = None,
        recovery_execution_id: Optional[
            "capo_arc_region_switch.types.recovery_execution_id.RecoveryExecutionId"
        ] = None,
    ) -> "capo_arc_region_switch.types.start_plan_execution_response.StartPlanExecutionResponse":
        """<p>Starts the execution of a Region switch plan. You can execute a plan in either <code>graceful</code> or <code>ungraceful</code> mode.</p> <p>Specifing <code>ungraceful</code> mode either changes the behavior of the execution blocks in a workflow or skips specific execution blocks.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan to execute.</p>
            target_region: <p>The Amazon Web Services Region to target with this execution. This is the Region that traffic will be shifted to or from, depending on the action.</p>
            action: <p>The action to perform. Valid values are <code>activate</code> (to shift traffic to the target Region) or <code>deactivate</code> (to shift traffic away from the target Region).</p>
            mode: <p>The plan execution mode. Valid values are <code>graceful</code>, for starting the execution in graceful mode, or <code>ungraceful</code>, for starting the execution in ungraceful mode.</p>
            comment: <p>An optional comment explaining why the plan execution is being started.</p>
            latest_version: <p>A boolean value indicating whether to use the latest version of the plan. If set to false, you must specify a specific version.</p>
            recovery_execution_id: <p>The execution identifier of the recovery execution that ran in the opposite region post-recovery is ran in. Required when starting a post-recovery execution.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.illegal_argument_exception.IllegalArgumentException: <p>The request processing has an invalid argument.</p>
            capo_arc_region_switch.errors.illegal_state_exception.IllegalStateException: <p>The operation failed because the current state of the resource doesn't allow the operation to proceed.</p> <p>HTTP Status Code: 400</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.start_plan_execution_request.StartPlanExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.start_plan_execution_response.StartPlanExecutionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.start_plan_execution

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.start_plan_execution.async_start_plan_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.start_plan_execution_request.StartPlanExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["plan_arn"] = plan_arn
        input_["target_region"] = target_region
        input_["action"] = action
        if mode is not None:
            input_["mode"] = mode
        if comment is not None:
            input_["comment"] = comment
        if latest_version is not None:
            input_["latest_version"] = latest_version
        if recovery_execution_id is not None:
            input_["recovery_execution_id"] = recovery_execution_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_plan_execution(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        action: "capo_arc_region_switch.types.update_plan_execution_action.UpdatePlanExecutionAction",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        comment: Optional[
            "capo_arc_region_switch.types.execution_comment.ExecutionComment"
        ] = None,
    ) -> "capo_arc_region_switch.types.update_plan_execution_response.UpdatePlanExecutionResponse":
        """<p>Updates an in-progress plan execution. This operation allows you to modify certain aspects of the execution, such as adding a comment or changing the action.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan with the execution to update.</p>
            execution_id: <p>The execution identifier of a plan execution.</p>
            action: <p>The action specified for a plan execution, for example, Switch to Graceful or Pause.</p>
            comment: <p>An optional comment about the plan execution.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.illegal_state_exception.IllegalStateException: <p>The operation failed because the current state of the resource doesn't allow the operation to proceed.</p> <p>HTTP Status Code: 400</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.update_plan_execution_request.UpdatePlanExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.update_plan_execution_response.UpdatePlanExecutionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.update_plan_execution

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.update_plan_execution.async_update_plan_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.update_plan_execution_request.UpdatePlanExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["plan_arn"] = plan_arn
        input_["execution_id"] = execution_id
        input_["action"] = action
        if comment is not None:
            input_["comment"] = comment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_plan_execution_step(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        comment: "capo_arc_region_switch.types.execution_comment.ExecutionComment",
        step_name: str,
        action_to_take: "capo_arc_region_switch.types.update_plan_execution_step_action.UpdatePlanExecutionStepAction",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.update_plan_execution_step_response.UpdatePlanExecutionStepResponse":
        """<p>Updates a specific step in an in-progress plan execution. This operation allows you to modify the step's comment or action.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan containing the execution step to update.</p>
            execution_id: <p>The unique identifier of the plan execution containing the step to update.</p>
            comment: <p>An optional comment about the plan execution.</p>
            step_name: <p>The name of the execution step to update.</p>
            action_to_take: <p>The updated action to take for the step. This can be used to skip or retry a step.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.update_plan_execution_step_request.UpdatePlanExecutionStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.update_plan_execution_step_response.UpdatePlanExecutionStepResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.update_plan_execution_step

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.update_plan_execution_step.async_update_plan_execution_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.update_plan_execution_step_request.UpdatePlanExecutionStepRequest = {}  # type: ignore[typeddict-item]
        input_["plan_arn"] = plan_arn
        input_["execution_id"] = execution_id
        input_["comment"] = comment
        input_["step_name"] = step_name
        input_["action_to_take"] = action_to_take

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
