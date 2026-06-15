from __future__ import annotations

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
    import aws_sdk_controltower.types.control_operation_filter
    import aws_sdk_controltower.types.control_operation_summary
    import aws_sdk_controltower.types.get_control_operation_input
    import aws_sdk_controltower.types.get_control_operation_output
    import aws_sdk_controltower.types.list_control_operations_input
    import aws_sdk_controltower.types.list_control_operations_max_results
    import aws_sdk_controltower.types.list_control_operations_next_token
    import aws_sdk_controltower.types.list_control_operations_output
    import aws_sdk_controltower.types.operation_identifier
    from aws_sdk_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from aws_sdk_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class ControlOperationResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def read(
        self,
        operation_identifier: "aws_sdk_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.get_control_operation_output.GetControlOperationOutput":
        r"""<p>Returns the status of a particular <code>EnableControl</code> or <code>DisableControl</code> operation. Displays a message in case of error. Details for an operation are available for 90 days. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            operation_identifier: <p>The ID of the asynchronous operation, which is used to track status. The operation is available for 90 days.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.get_control_operation_input.GetControlOperationInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.get_control_operation_output.GetControlOperationOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_control_operation

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.get_control_operation.get_control_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.get_control_operation_input.GetControlOperationInput = {}  # type: ignore[typeddict-item]
        input_["operation_identifier"] = operation_identifier

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
        filter: Optional[
            "aws_sdk_controltower.types.control_operation_filter.ControlOperationFilter"
        ] = None,
        next_token: Optional[
            "aws_sdk_controltower.types.list_control_operations_next_token.ListControlOperationsNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_controltower.types.list_control_operations_max_results.ListControlOperationsMaxResults"
        ] = None,
    ) -> "aws_sdk_controltower.types.list_control_operations_output.ListControlOperationsOutput":
        r"""<p>Provides a list of operations in progress or queued. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html#list-control-operations-api-examples\">ListControlOperation examples</a>.</p>

        Args:
            filter: <p>An input filter for the <code>ListControlOperations</code> API that lets you select the types of control operations to view.</p>
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.list_control_operations_input.ListControlOperationsInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.list_control_operations_output.ListControlOperationsOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_control_operations

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.list_control_operations.list_control_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.list_control_operations_input.ListControlOperationsInput = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
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


class AsyncControlOperationResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def read(
        self,
        operation_identifier: "aws_sdk_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.get_control_operation_output.GetControlOperationOutput":
        r"""<p>Returns the status of a particular <code>EnableControl</code> or <code>DisableControl</code> operation. Displays a message in case of error. Details for an operation are available for 90 days. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            operation_identifier: <p>The ID of the asynchronous operation, which is used to track status. The operation is available for 90 days.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.get_control_operation_input.GetControlOperationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.get_control_operation_output.GetControlOperationOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_control_operation

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.get_control_operation.async_get_control_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.get_control_operation_input.GetControlOperationInput = {}  # type: ignore[typeddict-item]
        input_["operation_identifier"] = operation_identifier

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
        filter: Optional[
            "aws_sdk_controltower.types.control_operation_filter.ControlOperationFilter"
        ] = None,
        next_token: Optional[
            "aws_sdk_controltower.types.list_control_operations_next_token.ListControlOperationsNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_controltower.types.list_control_operations_max_results.ListControlOperationsMaxResults"
        ] = None,
    ) -> "aws_sdk_controltower.types.list_control_operations_output.ListControlOperationsOutput":
        r"""<p>Provides a list of operations in progress or queued. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html#list-control-operations-api-examples\">ListControlOperation examples</a>.</p>

        Args:
            filter: <p>An input filter for the <code>ListControlOperations</code> API that lets you select the types of control operations to view.</p>
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.list_control_operations_input.ListControlOperationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.list_control_operations_output.ListControlOperationsOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_control_operations

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.list_control_operations.async_list_control_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.list_control_operations_input.ListControlOperationsInput = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
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
