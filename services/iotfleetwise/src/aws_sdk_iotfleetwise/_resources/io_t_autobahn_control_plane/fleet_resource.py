from typing import TYPE_CHECKING, Optional

from aws_sdk_iotfleetwise._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.create_fleet_request
    import aws_sdk_iotfleetwise.types.create_fleet_response
    import aws_sdk_iotfleetwise.types.delete_fleet_request
    import aws_sdk_iotfleetwise.types.delete_fleet_response
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.fleet_id
    import aws_sdk_iotfleetwise.types.fleet_summary
    import aws_sdk_iotfleetwise.types.get_fleet_request
    import aws_sdk_iotfleetwise.types.get_fleet_response
    import aws_sdk_iotfleetwise.types.list_fleets_request
    import aws_sdk_iotfleetwise.types.list_fleets_response
    import aws_sdk_iotfleetwise.types.list_response_scope
    import aws_sdk_iotfleetwise.types.max_results
    import aws_sdk_iotfleetwise.types.next_token
    import aws_sdk_iotfleetwise.types.tag_list
    import aws_sdk_iotfleetwise.types.update_fleet_request
    import aws_sdk_iotfleetwise.types.update_fleet_response
    from aws_sdk_iotfleetwise._services.async_io_t_fleet_wise import (
        AsyncIoTFleetWiseClient,
        AsyncIoTFleetWiseClientConfig,
    )
    from aws_sdk_iotfleetwise._services.io_t_fleet_wise import (
        IoTFleetWiseClient,
        IoTFleetWiseClientConfig,
    )


class FleetResource:
    def __init__(self, service: IoTFleetWiseClient) -> None:
        self._service = service

    def put(
        self,
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        signal_catalog_arn: "aws_sdk_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional[
            "aws_sdk_iotfleetwise.types.description.description"
        ] = None,
        tags: Optional["aws_sdk_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_iotfleetwise.types.create_fleet_response.CreateFleetResponse":
        """<p> Creates a fleet that represents a group of vehicles. </p> <note> <p>You must create both a signal catalog and vehicles before you can create a fleet. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html\">Fleets</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            fleet_id: <p> The unique ID of the fleet to create. </p>
            description: <p> A brief description of the fleet to create. </p>
            signal_catalog_arn: <p> The Amazon Resource Name (ARN) of a signal catalog. </p>
            tags: <p>Metadata that can be used to manage the fleet.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.create_fleet_request.CreateFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.create_fleet_response.CreateFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.create_fleet

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.create_fleet.create_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iotfleetwise.types.create_fleet_request.CreateFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_id"] = fleet_id
        if description is not None:
            input["description"] = description
        input["signal_catalog_arn"] = signal_catalog_arn
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.get_fleet_response.GetFleetResponse":
        """<p> Retrieves information about a fleet. </p>

        Args:
            fleet_id: <p> The ID of the fleet to retrieve information about. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.get_fleet_request.GetFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.get_fleet_response.GetFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_fleet

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_fleet.get_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iotfleetwise.types.get_fleet_request.GetFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional[
            "aws_sdk_iotfleetwise.types.description.description"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.update_fleet_response.UpdateFleetResponse":
        """<p> Updates the description of an existing fleet. </p>

        Args:
            fleet_id: <p> The ID of the fleet to update. </p>
            description: <p> An updated description of the fleet. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.update_fleet_request.UpdateFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.update_fleet_response.UpdateFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.update_fleet

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.update_fleet.update_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iotfleetwise.types.update_fleet_request.UpdateFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_id"] = fleet_id
        if description is not None:
            input["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.delete_fleet_response.DeleteFleetResponse":
        """<p> Deletes a fleet. Before you delete a fleet, all vehicles must be dissociated from the fleet. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-fleet-cli.html\">Delete a fleet (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            fleet_id: <p> The ID of the fleet to delete. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.delete_fleet_request.DeleteFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.delete_fleet_response.DeleteFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.delete_fleet

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.delete_fleet.delete_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iotfleetwise.types.delete_fleet_request.DeleteFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotfleetwise.types.max_results.maxResults"
        ] = None,
        list_response_scope: Optional[
            "aws_sdk_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.list_fleets_response.ListFleetsResponse":
        """<p> Retrieves information for each created fleet in an Amazon Web Services account. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: fleet ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.list_fleets_request.ListFleetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.list_fleets_response.ListFleetsResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets.list_fleets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iotfleetwise.types.list_fleets_request.ListFleetsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if list_response_scope is not None:
            input["list_response_scope"] = list_response_scope

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncFleetResource:
    def __init__(self, service: AsyncIoTFleetWiseClient) -> None:
        self._service = service

    async def put(
        self,
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        signal_catalog_arn: "aws_sdk_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional[
            "aws_sdk_iotfleetwise.types.description.description"
        ] = None,
        tags: Optional["aws_sdk_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_iotfleetwise.types.create_fleet_response.CreateFleetResponse":
        """<p> Creates a fleet that represents a group of vehicles. </p> <note> <p>You must create both a signal catalog and vehicles before you can create a fleet. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html\">Fleets</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            fleet_id: <p> The unique ID of the fleet to create. </p>
            description: <p> A brief description of the fleet to create. </p>
            signal_catalog_arn: <p> The Amazon Resource Name (ARN) of a signal catalog. </p>
            tags: <p>Metadata that can be used to manage the fleet.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.create_fleet_request.CreateFleetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.create_fleet_response.CreateFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.create_fleet

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.create_fleet.async_create_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iotfleetwise.types.create_fleet_request.CreateFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_id"] = fleet_id
        if description is not None:
            input["description"] = description
        input["signal_catalog_arn"] = signal_catalog_arn
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.get_fleet_response.GetFleetResponse":
        """<p> Retrieves information about a fleet. </p>

        Args:
            fleet_id: <p> The ID of the fleet to retrieve information about. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.get_fleet_request.GetFleetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.get_fleet_response.GetFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_fleet

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_fleet.async_get_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iotfleetwise.types.get_fleet_request.GetFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_id"] = fleet_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional[
            "aws_sdk_iotfleetwise.types.description.description"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.update_fleet_response.UpdateFleetResponse":
        """<p> Updates the description of an existing fleet. </p>

        Args:
            fleet_id: <p> The ID of the fleet to update. </p>
            description: <p> An updated description of the fleet. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.update_fleet_request.UpdateFleetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.update_fleet_response.UpdateFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.update_fleet

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.update_fleet.async_update_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iotfleetwise.types.update_fleet_request.UpdateFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_id"] = fleet_id
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.delete_fleet_response.DeleteFleetResponse":
        """<p> Deletes a fleet. Before you delete a fleet, all vehicles must be dissociated from the fleet. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-fleet-cli.html\">Delete a fleet (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            fleet_id: <p> The ID of the fleet to delete. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.delete_fleet_request.DeleteFleetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.delete_fleet_response.DeleteFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.delete_fleet

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.delete_fleet.async_delete_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iotfleetwise.types.delete_fleet_request.DeleteFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_id"] = fleet_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotfleetwise.types.max_results.maxResults"
        ] = None,
        list_response_scope: Optional[
            "aws_sdk_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.list_fleets_response.ListFleetsResponse":
        """<p> Retrieves information for each created fleet in an Amazon Web Services account. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: fleet ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.list_fleets_request.ListFleetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.list_fleets_response.ListFleetsResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets.async_list_fleets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_iotfleetwise.types.list_fleets_request.ListFleetsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if list_response_scope is not None:
            input["list_response_scope"] = list_response_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
