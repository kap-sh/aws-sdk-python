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
    import aws_sdk_controltower.types.get_landing_zone_operation_input
    import aws_sdk_controltower.types.get_landing_zone_operation_output
    import aws_sdk_controltower.types.landing_zone_operation_filter
    import aws_sdk_controltower.types.landing_zone_operation_summary
    import aws_sdk_controltower.types.list_landing_zone_operations_input
    import aws_sdk_controltower.types.list_landing_zone_operations_max_results
    import aws_sdk_controltower.types.list_landing_zone_operations_output
    import aws_sdk_controltower.types.operation_identifier
    from aws_sdk_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from aws_sdk_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class LandingZoneOperationResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def read(
        self,
        operation_identifier: "aws_sdk_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.get_landing_zone_operation_output.GetLandingZoneOperationOutput":
        """<p>Returns the status of the specified landing zone operation. Details for an operation are available for 90 days.</p>

        Args:
            operation_identifier: <p>A unique identifier assigned to a landing zone operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.get_landing_zone_operation_input.GetLandingZoneOperationInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.get_landing_zone_operation_output.GetLandingZoneOperationOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_landing_zone_operation

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.get_landing_zone_operation.get_landing_zone_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.get_landing_zone_operation_input.GetLandingZoneOperationInput = {}  # type: ignore[typeddict-item]
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
            "aws_sdk_controltower.types.landing_zone_operation_filter.LandingZoneOperationFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_controltower.types.list_landing_zone_operations_max_results.ListLandingZoneOperationsMaxResults"
        ] = None,
    ) -> "aws_sdk_controltower.types.list_landing_zone_operations_output.ListLandingZoneOperationsOutput":
        """<p>Lists all landing zone operations from the past 90 days. Results are sorted by time, with the most recent operation first.</p>

        Args:
            filter: <p>An input filter for the <code>ListLandingZoneOperations</code> API that lets you select the types of landing zone operations to view.</p>
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>How many results to return per API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.list_landing_zone_operations_input.ListLandingZoneOperationsInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.list_landing_zone_operations_output.ListLandingZoneOperationsOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_landing_zone_operations

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.list_landing_zone_operations.list_landing_zone_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.list_landing_zone_operations_input.ListLandingZoneOperationsInput = {}  # type: ignore[typeddict-item]
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


class AsyncLandingZoneOperationResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def read(
        self,
        operation_identifier: "aws_sdk_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.get_landing_zone_operation_output.GetLandingZoneOperationOutput":
        """<p>Returns the status of the specified landing zone operation. Details for an operation are available for 90 days.</p>

        Args:
            operation_identifier: <p>A unique identifier assigned to a landing zone operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.get_landing_zone_operation_input.GetLandingZoneOperationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.get_landing_zone_operation_output.GetLandingZoneOperationOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.get_landing_zone_operation

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.get_landing_zone_operation.async_get_landing_zone_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.get_landing_zone_operation_input.GetLandingZoneOperationInput = {}  # type: ignore[typeddict-item]
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
            "aws_sdk_controltower.types.landing_zone_operation_filter.LandingZoneOperationFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_controltower.types.list_landing_zone_operations_max_results.ListLandingZoneOperationsMaxResults"
        ] = None,
    ) -> "aws_sdk_controltower.types.list_landing_zone_operations_output.ListLandingZoneOperationsOutput":
        """<p>Lists all landing zone operations from the past 90 days. Results are sorted by time, with the most recent operation first.</p>

        Args:
            filter: <p>An input filter for the <code>ListLandingZoneOperations</code> API that lets you select the types of landing zone operations to view.</p>
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>How many results to return per API call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.list_landing_zone_operations_input.ListLandingZoneOperationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.list_landing_zone_operations_output.ListLandingZoneOperationsOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_landing_zone_operations

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.list_landing_zone_operations.async_list_landing_zone_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.list_landing_zone_operations_input.ListLandingZoneOperationsInput = {}  # type: ignore[typeddict-item]
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
