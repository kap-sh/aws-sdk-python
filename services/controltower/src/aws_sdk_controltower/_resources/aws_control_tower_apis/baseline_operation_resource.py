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
    import aws_sdk_controltower.types.get_baseline_operation_input
    import aws_sdk_controltower.types.get_baseline_operation_output
    import aws_sdk_controltower.types.operation_identifier
    from aws_sdk_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from aws_sdk_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class BaselineOperationResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def read(
        self,
        operation_identifier: "aws_sdk_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.get_baseline_operation_output.GetBaselineOperationOutput":
        """<p>Returns the details of an asynchronous baseline operation, as initiated by any of these APIs: <code>EnableBaseline</code>, <code>DisableBaseline</code>, <code>UpdateEnabledBaseline</code>, <code>ResetEnabledBaseline</code>. A status message is displayed in case of operation failure. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            operation_identifier: <p>The operation ID returned from mutating asynchronous APIs (Enable, Disable, Update, Reset).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.get_baseline_operation_input.GetBaselineOperationInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.get_baseline_operation_output.GetBaselineOperationOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_baseline_operation

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.get_baseline_operation.get_baseline_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.get_baseline_operation_input.GetBaselineOperationInput = {}  # type: ignore[typeddict-item]
        input_["operation_identifier"] = operation_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncBaselineOperationResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def read(
        self,
        operation_identifier: "aws_sdk_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.get_baseline_operation_output.GetBaselineOperationOutput":
        """<p>Returns the details of an asynchronous baseline operation, as initiated by any of these APIs: <code>EnableBaseline</code>, <code>DisableBaseline</code>, <code>UpdateEnabledBaseline</code>, <code>ResetEnabledBaseline</code>. A status message is displayed in case of operation failure. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            operation_identifier: <p>The operation ID returned from mutating asynchronous APIs (Enable, Disable, Update, Reset).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.get_baseline_operation_input.GetBaselineOperationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.get_baseline_operation_output.GetBaselineOperationOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_baseline_operation

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.get_baseline_operation.async_get_baseline_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.get_baseline_operation_input.GetBaselineOperationInput = {}  # type: ignore[typeddict-item]
        input_["operation_identifier"] = operation_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
