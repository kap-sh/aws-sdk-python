from typing import TYPE_CHECKING, Optional

import aws_sdk_controltower._auth._signers
import aws_sdk_controltower._auth._sigv4
from aws_sdk_controltower._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_controltower.types.baseline_arn
    import aws_sdk_controltower.types.baseline_summary
    import aws_sdk_controltower.types.get_baseline_input
    import aws_sdk_controltower.types.get_baseline_output
    import aws_sdk_controltower.types.list_baselines_input
    import aws_sdk_controltower.types.list_baselines_max_results
    import aws_sdk_controltower.types.list_baselines_output
    from aws_sdk_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from aws_sdk_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class BaselineResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def read(
        self,
        baseline_identifier: "aws_sdk_controltower.types.baseline_arn.BaselineArn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.get_baseline_output.GetBaselineOutput":
        """<p>Retrieve details about an existing <code>Baseline</code> resource by specifying its identifier. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_identifier: <p>The ARN of the <code>Baseline</code> resource to be retrieved.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.get_baseline_input.GetBaselineInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.get_baseline_output.GetBaselineOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_baseline

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.get_baseline.get_baseline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.get_baseline_input.GetBaselineInput = {}  # type: ignore[typeddict-item]
        input_["baseline_identifier"] = baseline_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_controltower.types.list_baselines_max_results.ListBaselinesMaxResults"
        ] = None,
    ) -> "aws_sdk_controltower.types.list_baselines_output.ListBaselinesOutput":
        """<p>Returns a summary list of all available baselines. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.list_baselines_input.ListBaselinesInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.list_baselines_output.ListBaselinesOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_baselines

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.list_baselines.list_baselines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.list_baselines_input.ListBaselinesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncBaselineResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def read(
        self,
        baseline_identifier: "aws_sdk_controltower.types.baseline_arn.BaselineArn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.get_baseline_output.GetBaselineOutput":
        """<p>Retrieve details about an existing <code>Baseline</code> resource by specifying its identifier. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_identifier: <p>The ARN of the <code>Baseline</code> resource to be retrieved.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.get_baseline_input.GetBaselineInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.get_baseline_output.GetBaselineOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_baseline

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.get_baseline.async_get_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.get_baseline_input.GetBaselineInput = {}  # type: ignore[typeddict-item]
        input_["baseline_identifier"] = baseline_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_controltower.types.list_baselines_max_results.ListBaselinesMaxResults"
        ] = None,
    ) -> "aws_sdk_controltower.types.list_baselines_output.ListBaselinesOutput":
        """<p>Returns a summary list of all available baselines. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.list_baselines_input.ListBaselinesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.list_baselines_output.ListBaselinesOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_baselines

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.list_baselines.async_list_baselines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.list_baselines_input.ListBaselinesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
