from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_groundstation._auth._signers
import aws_sdk_groundstation._auth._sigv4
from aws_sdk_groundstation._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.get_satellite_request
    import aws_sdk_groundstation.types.get_satellite_response
    import aws_sdk_groundstation.types.list_satellites_request
    import aws_sdk_groundstation.types.list_satellites_response
    import aws_sdk_groundstation.types.pagination_max_results
    import aws_sdk_groundstation.types.pagination_token
    import aws_sdk_groundstation.types.satellite_list_item
    import aws_sdk_groundstation.types.uuid
    from aws_sdk_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from aws_sdk_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class Satellite:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def read(
        self,
        satellite_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.get_satellite_response.GetSatelliteResponse":
        """<p>Returns a satellite.</p>

        Args:
            satellite_id: <p>UUID of a satellite.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.get_satellite_request.GetSatelliteRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.get_satellite_response.GetSatelliteResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.get_satellite

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.get_satellite.get_satellite(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.get_satellite_request.GetSatelliteRequest = {}  # type: ignore[typeddict-item]
        input_["satellite_id"] = satellite_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        max_results: Optional[
            "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_groundstation.types.list_satellites_response.ListSatellitesResponse":
        """<p>Returns a list of satellites.</p>

        Args:
            max_results: <p>Maximum number of satellites returned.</p>
            next_token: <p>Next token that can be supplied in the next call to get the next page of satellites.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.list_satellites_request.ListSatellitesRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.list_satellites_response.ListSatellitesResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_satellites

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.list_satellites.list_satellites(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_satellites_request.ListSatellitesRequest = {}  # type: ignore[typeddict-item]
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


class AsyncSatellite:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def read(
        self,
        satellite_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.get_satellite_response.GetSatelliteResponse":
        """<p>Returns a satellite.</p>

        Args:
            satellite_id: <p>UUID of a satellite.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.get_satellite_request.GetSatelliteRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.get_satellite_response.GetSatelliteResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.get_satellite

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.get_satellite.async_get_satellite(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.get_satellite_request.GetSatelliteRequest = {}  # type: ignore[typeddict-item]
        input_["satellite_id"] = satellite_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_groundstation.types.list_satellites_response.ListSatellitesResponse":
        """<p>Returns a list of satellites.</p>

        Args:
            max_results: <p>Maximum number of satellites returned.</p>
            next_token: <p>Next token that can be supplied in the next call to get the next page of satellites.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.list_satellites_request.ListSatellitesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.list_satellites_response.ListSatellitesResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_satellites

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.list_satellites.async_list_satellites(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_satellites_request.ListSatellitesRequest = {}  # type: ignore[typeddict-item]
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
