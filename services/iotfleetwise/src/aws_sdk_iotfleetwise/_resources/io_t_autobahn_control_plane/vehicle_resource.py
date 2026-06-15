from __future__ import annotations

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
    import aws_sdk_iotfleetwise.types.associate_vehicle_fleet_request
    import aws_sdk_iotfleetwise.types.associate_vehicle_fleet_response
    import aws_sdk_iotfleetwise.types.attribute_names_list
    import aws_sdk_iotfleetwise.types.attribute_values_list
    import aws_sdk_iotfleetwise.types.attributes_map
    import aws_sdk_iotfleetwise.types.create_vehicle_request
    import aws_sdk_iotfleetwise.types.create_vehicle_response
    import aws_sdk_iotfleetwise.types.delete_vehicle_request
    import aws_sdk_iotfleetwise.types.delete_vehicle_response
    import aws_sdk_iotfleetwise.types.disassociate_vehicle_fleet_request
    import aws_sdk_iotfleetwise.types.disassociate_vehicle_fleet_response
    import aws_sdk_iotfleetwise.types.fleet_id
    import aws_sdk_iotfleetwise.types.get_vehicle_request
    import aws_sdk_iotfleetwise.types.get_vehicle_response
    import aws_sdk_iotfleetwise.types.list_response_scope
    import aws_sdk_iotfleetwise.types.list_vehicles_max_results
    import aws_sdk_iotfleetwise.types.list_vehicles_request
    import aws_sdk_iotfleetwise.types.list_vehicles_response
    import aws_sdk_iotfleetwise.types.next_token
    import aws_sdk_iotfleetwise.types.state_template_association_identifiers
    import aws_sdk_iotfleetwise.types.state_template_associations
    import aws_sdk_iotfleetwise.types.tag_list
    import aws_sdk_iotfleetwise.types.update_mode
    import aws_sdk_iotfleetwise.types.update_vehicle_request
    import aws_sdk_iotfleetwise.types.update_vehicle_response
    import aws_sdk_iotfleetwise.types.vehicle_association_behavior
    import aws_sdk_iotfleetwise.types.vehicle_name
    import aws_sdk_iotfleetwise.types.vehicle_summary
    from aws_sdk_iotfleetwise._services.async_io_t_fleet_wise import (
        AsyncIoTFleetWiseClient,
        AsyncIoTFleetWiseClientConfig,
    )
    from aws_sdk_iotfleetwise._services.io_t_fleet_wise import (
        IoTFleetWiseClient,
        IoTFleetWiseClientConfig,
    )


class VehicleResource:
    def __init__(self, service: IoTFleetWiseClient) -> None:
        self._service = service

    def put(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        model_manifest_arn: "aws_sdk_iotfleetwise.types.arn.arn",
        decoder_manifest_arn: "aws_sdk_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        attributes: Optional[
            "aws_sdk_iotfleetwise.types.attributes_map.attributesMap"
        ] = None,
        association_behavior: Optional[
            "aws_sdk_iotfleetwise.types.vehicle_association_behavior.VehicleAssociationBehavior"
        ] = None,
        tags: Optional["aws_sdk_iotfleetwise.types.tag_list.TagList"] = None,
        state_templates: Optional[
            "aws_sdk_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse":
        r"""<p> Creates a vehicle, which is an instance of a vehicle model (model manifest). Vehicles created from the same vehicle model consist of the same signals inherited from the vehicle model.</p> <note> <p> If you have an existing Amazon Web Services IoT thing, you can use Amazon Web Services IoT FleetWise to create a vehicle and collect data from your thing. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-vehicle-cli.html\">Create a vehicle (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            vehicle_name: <p> The unique ID of the vehicle to create. </p>
            model_manifest_arn: <p> The Amazon Resource Name ARN of a vehicle model. </p>
            decoder_manifest_arn: <p> The ARN of a decoder manifest. </p>
            attributes: <p>Static information about a vehicle in a key-value pair. For example: <code>\"engineType\"</code> : <code>\"1.3 L R2\"</code> </p> <p>To use attributes with Campaigns or State Templates, you must include them using the request parameters <code>dataExtraDimensions</code> and/or <code>metadataExtraDimensions</code> (for state templates only) when creating your campaign/state template. </p>
            association_behavior: <p> An option to create a new Amazon Web Services IoT thing when creating a vehicle, or to validate an existing Amazon Web Services IoT thing as a vehicle. </p> <p>Default: <code/> </p>
            tags: <p>Metadata that can be used to manage the vehicle.</p>
            state_templates: <p>Associate state templates with the vehicle. You can monitor the last known state of the vehicle in near real time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.create_vehicle_request.CreateVehicleRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.create_vehicle

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.create_vehicle.create_vehicle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.create_vehicle_request.CreateVehicleRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name
        input_["model_manifest_arn"] = model_manifest_arn
        input_["decoder_manifest_arn"] = decoder_manifest_arn
        if attributes is not None:
            input_["attributes"] = attributes
        if association_behavior is not None:
            input_["association_behavior"] = association_behavior
        if tags is not None:
            input_["tags"] = tags
        if state_templates is not None:
            input_["state_templates"] = state_templates

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.get_vehicle_response.GetVehicleResponse":
        """<p> Retrieves information about a vehicle. </p>

        Args:
            vehicle_name: <p> The ID of the vehicle to retrieve information about. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.get_vehicle_request.GetVehicleRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.get_vehicle_response.GetVehicleResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_vehicle

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_vehicle.get_vehicle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.get_vehicle_request.GetVehicleRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        model_manifest_arn: Optional["aws_sdk_iotfleetwise.types.arn.arn"] = None,
        decoder_manifest_arn: Optional["aws_sdk_iotfleetwise.types.arn.arn"] = None,
        attributes: Optional[
            "aws_sdk_iotfleetwise.types.attributes_map.attributesMap"
        ] = None,
        attribute_update_mode: Optional[
            "aws_sdk_iotfleetwise.types.update_mode.UpdateMode"
        ] = None,
        state_templates_to_add: Optional[
            "aws_sdk_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
        ] = None,
        state_templates_to_remove: Optional[
            "aws_sdk_iotfleetwise.types.state_template_association_identifiers.StateTemplateAssociationIdentifiers"
        ] = None,
        state_templates_to_update: Optional[
            "aws_sdk_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.update_vehicle_response.UpdateVehicleResponse":
        r"""<p> Updates a vehicle.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            vehicle_name: <p>The unique ID of the vehicle to update.</p>
            model_manifest_arn: <p>The ARN of a vehicle model (model manifest) associated with the vehicle.</p>
            decoder_manifest_arn: <p>The ARN of the decoder manifest associated with this vehicle.</p>
            attributes: <p>Static information about a vehicle in a key-value pair. For example:</p> <p> <code>\"engineType\"</code> : <code>\"1.3 L R2\"</code> </p>
            attribute_update_mode: <p>The method the specified attributes will update the existing attributes on the vehicle. Use<code>Overwite</code> to replace the vehicle attributes with the specified attributes. Or use <code>Merge</code> to combine all attributes.</p> <p>This is required if attributes are present in the input.</p>
            state_templates_to_add: <p>Associate state templates with the vehicle.</p>
            state_templates_to_remove: <p>Remove state templates from the vehicle.</p>
            state_templates_to_update: <p>Change the <code>stateTemplateUpdateStrategy</code> of state templates already associated with the vehicle.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.update_vehicle_request.UpdateVehicleRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.update_vehicle_response.UpdateVehicleResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.update_vehicle

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.update_vehicle.update_vehicle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.update_vehicle_request.UpdateVehicleRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name
        if model_manifest_arn is not None:
            input_["model_manifest_arn"] = model_manifest_arn
        if decoder_manifest_arn is not None:
            input_["decoder_manifest_arn"] = decoder_manifest_arn
        if attributes is not None:
            input_["attributes"] = attributes
        if attribute_update_mode is not None:
            input_["attribute_update_mode"] = attribute_update_mode
        if state_templates_to_add is not None:
            input_["state_templates_to_add"] = state_templates_to_add
        if state_templates_to_remove is not None:
            input_["state_templates_to_remove"] = state_templates_to_remove
        if state_templates_to_update is not None:
            input_["state_templates_to_update"] = state_templates_to_update

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.delete_vehicle_response.DeleteVehicleResponse":
        """<p> Deletes a vehicle and removes it from any campaigns.</p>

        Args:
            vehicle_name: <p>The ID of the vehicle to delete. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.delete_vehicle_request.DeleteVehicleRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.delete_vehicle_response.DeleteVehicleResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.delete_vehicle

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.delete_vehicle.delete_vehicle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.delete_vehicle_request.DeleteVehicleRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        model_manifest_arn: Optional["aws_sdk_iotfleetwise.types.arn.arn"] = None,
        attribute_names: Optional[
            "aws_sdk_iotfleetwise.types.attribute_names_list.attributeNamesList"
        ] = None,
        attribute_values: Optional[
            "aws_sdk_iotfleetwise.types.attribute_values_list.attributeValuesList"
        ] = None,
        next_token: Optional["aws_sdk_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotfleetwise.types.list_vehicles_max_results.listVehiclesMaxResults"
        ] = None,
        list_response_scope: Optional[
            "aws_sdk_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.list_vehicles_response.ListVehiclesResponse":
        r"""<p> Retrieves a list of summaries of created vehicles. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            model_manifest_arn: <p> The Amazon Resource Name (ARN) of a vehicle model (model manifest). You can use this optional parameter to list only the vehicles created from a certain vehicle model. </p>
            attribute_names: <p>The fully qualified names of the attributes. You can use this optional parameter to list the vehicles containing all the attributes in the request. For example, <code>attributeNames</code> could be \"<code>Vehicle.Body.Engine.Type, Vehicle.Color</code>\" and the corresponding <code>attributeValues</code> could be \"<code>1.3 L R2, Blue</code>\" . In this case, the API will filter vehicles with an attribute name <code>Vehicle.Body.Engine.Type</code> that contains a value of <code>1.3 L R2</code> AND an attribute name <code>Vehicle.Color</code> that contains a value of \"<code>Blue</code>\". A request must contain unique values for the <code>attributeNames</code> filter and the matching number of <code>attributeValues</code> filters to return the subset of vehicles that match the attributes filter condition.</p>
            attribute_values: <p>Static information about a vehicle attribute value in string format. You can use this optional parameter in conjunction with <code>attributeNames</code> to list the vehicles containing all the <code>attributeValues</code> corresponding to the <code>attributeNames</code> filter. For example, <code>attributeValues</code> could be \"<code>1.3 L R2, Blue</code>\" and the corresponding <code>attributeNames</code> filter could be \"<code>Vehicle.Body.Engine.Type, Vehicle.Color</code>\". In this case, the API will filter vehicles with attribute name <code>Vehicle.Body.Engine.Type</code> that contains a value of <code>1.3 L R2</code> AND an attribute name <code>Vehicle.Color</code> that contains a value of \"<code>Blue</code>\". A request must contain unique values for the <code>attributeNames</code> filter and the matching number of <code>attributeValues</code> filter to return the subset of vehicles that match the attributes filter condition.</p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: vehicle name, Amazon Resource Name (ARN), creation time, and last modification time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.list_vehicles_request.ListVehiclesRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.list_vehicles_response.ListVehiclesResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.list_vehicles

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.list_vehicles.list_vehicles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.list_vehicles_request.ListVehiclesRequest = {}  # type: ignore[typeddict-item]
        if model_manifest_arn is not None:
            input_["model_manifest_arn"] = model_manifest_arn
        if attribute_names is not None:
            input_["attribute_names"] = attribute_names
        if attribute_values is not None:
            input_["attribute_values"] = attribute_values
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_vehicle_fleet(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.associate_vehicle_fleet_response.AssociateVehicleFleetResponse":
        """<p> Adds, or associates, a vehicle with a fleet. </p>

        Args:
            vehicle_name: <p> The unique ID of the vehicle to associate with the fleet. </p>
            fleet_id: <p> The ID of a fleet. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.associate_vehicle_fleet_request.AssociateVehicleFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.associate_vehicle_fleet_response.AssociateVehicleFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.associate_vehicle_fleet

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.associate_vehicle_fleet.associate_vehicle_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.associate_vehicle_fleet_request.AssociateVehicleFleetRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name
        input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_vehicle_fleet(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.disassociate_vehicle_fleet_response.DisassociateVehicleFleetResponse":
        """<p>Removes, or disassociates, a vehicle from a fleet. Disassociating a vehicle from a fleet doesn't delete the vehicle.</p>

        Args:
            vehicle_name: <p> The unique ID of the vehicle to disassociate from the fleet.</p>
            fleet_id: <p> The unique ID of a fleet. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.disassociate_vehicle_fleet_request.DisassociateVehicleFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.disassociate_vehicle_fleet_response.DisassociateVehicleFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.disassociate_vehicle_fleet

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.disassociate_vehicle_fleet.disassociate_vehicle_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.disassociate_vehicle_fleet_request.DisassociateVehicleFleetRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name
        input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncVehicleResource:
    def __init__(self, service: AsyncIoTFleetWiseClient) -> None:
        self._service = service

    async def put(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        model_manifest_arn: "aws_sdk_iotfleetwise.types.arn.arn",
        decoder_manifest_arn: "aws_sdk_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        attributes: Optional[
            "aws_sdk_iotfleetwise.types.attributes_map.attributesMap"
        ] = None,
        association_behavior: Optional[
            "aws_sdk_iotfleetwise.types.vehicle_association_behavior.VehicleAssociationBehavior"
        ] = None,
        tags: Optional["aws_sdk_iotfleetwise.types.tag_list.TagList"] = None,
        state_templates: Optional[
            "aws_sdk_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse":
        r"""<p> Creates a vehicle, which is an instance of a vehicle model (model manifest). Vehicles created from the same vehicle model consist of the same signals inherited from the vehicle model.</p> <note> <p> If you have an existing Amazon Web Services IoT thing, you can use Amazon Web Services IoT FleetWise to create a vehicle and collect data from your thing. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-vehicle-cli.html\">Create a vehicle (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            vehicle_name: <p> The unique ID of the vehicle to create. </p>
            model_manifest_arn: <p> The Amazon Resource Name ARN of a vehicle model. </p>
            decoder_manifest_arn: <p> The ARN of a decoder manifest. </p>
            attributes: <p>Static information about a vehicle in a key-value pair. For example: <code>\"engineType\"</code> : <code>\"1.3 L R2\"</code> </p> <p>To use attributes with Campaigns or State Templates, you must include them using the request parameters <code>dataExtraDimensions</code> and/or <code>metadataExtraDimensions</code> (for state templates only) when creating your campaign/state template. </p>
            association_behavior: <p> An option to create a new Amazon Web Services IoT thing when creating a vehicle, or to validate an existing Amazon Web Services IoT thing as a vehicle. </p> <p>Default: <code/> </p>
            tags: <p>Metadata that can be used to manage the vehicle.</p>
            state_templates: <p>Associate state templates with the vehicle. You can monitor the last known state of the vehicle in near real time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.create_vehicle_request.CreateVehicleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.create_vehicle_response.CreateVehicleResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.create_vehicle

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.create_vehicle.async_create_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.create_vehicle_request.CreateVehicleRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name
        input_["model_manifest_arn"] = model_manifest_arn
        input_["decoder_manifest_arn"] = decoder_manifest_arn
        if attributes is not None:
            input_["attributes"] = attributes
        if association_behavior is not None:
            input_["association_behavior"] = association_behavior
        if tags is not None:
            input_["tags"] = tags
        if state_templates is not None:
            input_["state_templates"] = state_templates

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.get_vehicle_response.GetVehicleResponse":
        """<p> Retrieves information about a vehicle. </p>

        Args:
            vehicle_name: <p> The ID of the vehicle to retrieve information about. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.get_vehicle_request.GetVehicleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.get_vehicle_response.GetVehicleResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_vehicle

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_vehicle.async_get_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.get_vehicle_request.GetVehicleRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        model_manifest_arn: Optional["aws_sdk_iotfleetwise.types.arn.arn"] = None,
        decoder_manifest_arn: Optional["aws_sdk_iotfleetwise.types.arn.arn"] = None,
        attributes: Optional[
            "aws_sdk_iotfleetwise.types.attributes_map.attributesMap"
        ] = None,
        attribute_update_mode: Optional[
            "aws_sdk_iotfleetwise.types.update_mode.UpdateMode"
        ] = None,
        state_templates_to_add: Optional[
            "aws_sdk_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
        ] = None,
        state_templates_to_remove: Optional[
            "aws_sdk_iotfleetwise.types.state_template_association_identifiers.StateTemplateAssociationIdentifiers"
        ] = None,
        state_templates_to_update: Optional[
            "aws_sdk_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.update_vehicle_response.UpdateVehicleResponse":
        r"""<p> Updates a vehicle.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html\">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

        Args:
            vehicle_name: <p>The unique ID of the vehicle to update.</p>
            model_manifest_arn: <p>The ARN of a vehicle model (model manifest) associated with the vehicle.</p>
            decoder_manifest_arn: <p>The ARN of the decoder manifest associated with this vehicle.</p>
            attributes: <p>Static information about a vehicle in a key-value pair. For example:</p> <p> <code>\"engineType\"</code> : <code>\"1.3 L R2\"</code> </p>
            attribute_update_mode: <p>The method the specified attributes will update the existing attributes on the vehicle. Use<code>Overwite</code> to replace the vehicle attributes with the specified attributes. Or use <code>Merge</code> to combine all attributes.</p> <p>This is required if attributes are present in the input.</p>
            state_templates_to_add: <p>Associate state templates with the vehicle.</p>
            state_templates_to_remove: <p>Remove state templates from the vehicle.</p>
            state_templates_to_update: <p>Change the <code>stateTemplateUpdateStrategy</code> of state templates already associated with the vehicle.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.update_vehicle_request.UpdateVehicleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.update_vehicle_response.UpdateVehicleResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.update_vehicle

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.update_vehicle.async_update_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.update_vehicle_request.UpdateVehicleRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name
        if model_manifest_arn is not None:
            input_["model_manifest_arn"] = model_manifest_arn
        if decoder_manifest_arn is not None:
            input_["decoder_manifest_arn"] = decoder_manifest_arn
        if attributes is not None:
            input_["attributes"] = attributes
        if attribute_update_mode is not None:
            input_["attribute_update_mode"] = attribute_update_mode
        if state_templates_to_add is not None:
            input_["state_templates_to_add"] = state_templates_to_add
        if state_templates_to_remove is not None:
            input_["state_templates_to_remove"] = state_templates_to_remove
        if state_templates_to_update is not None:
            input_["state_templates_to_update"] = state_templates_to_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.delete_vehicle_response.DeleteVehicleResponse":
        """<p> Deletes a vehicle and removes it from any campaigns.</p>

        Args:
            vehicle_name: <p>The ID of the vehicle to delete. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.delete_vehicle_request.DeleteVehicleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.delete_vehicle_response.DeleteVehicleResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.delete_vehicle

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.delete_vehicle.async_delete_vehicle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.delete_vehicle_request.DeleteVehicleRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        model_manifest_arn: Optional["aws_sdk_iotfleetwise.types.arn.arn"] = None,
        attribute_names: Optional[
            "aws_sdk_iotfleetwise.types.attribute_names_list.attributeNamesList"
        ] = None,
        attribute_values: Optional[
            "aws_sdk_iotfleetwise.types.attribute_values_list.attributeValuesList"
        ] = None,
        next_token: Optional["aws_sdk_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotfleetwise.types.list_vehicles_max_results.listVehiclesMaxResults"
        ] = None,
        list_response_scope: Optional[
            "aws_sdk_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.list_vehicles_response.ListVehiclesResponse":
        r"""<p> Retrieves a list of summaries of created vehicles. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            model_manifest_arn: <p> The Amazon Resource Name (ARN) of a vehicle model (model manifest). You can use this optional parameter to list only the vehicles created from a certain vehicle model. </p>
            attribute_names: <p>The fully qualified names of the attributes. You can use this optional parameter to list the vehicles containing all the attributes in the request. For example, <code>attributeNames</code> could be \"<code>Vehicle.Body.Engine.Type, Vehicle.Color</code>\" and the corresponding <code>attributeValues</code> could be \"<code>1.3 L R2, Blue</code>\" . In this case, the API will filter vehicles with an attribute name <code>Vehicle.Body.Engine.Type</code> that contains a value of <code>1.3 L R2</code> AND an attribute name <code>Vehicle.Color</code> that contains a value of \"<code>Blue</code>\". A request must contain unique values for the <code>attributeNames</code> filter and the matching number of <code>attributeValues</code> filters to return the subset of vehicles that match the attributes filter condition.</p>
            attribute_values: <p>Static information about a vehicle attribute value in string format. You can use this optional parameter in conjunction with <code>attributeNames</code> to list the vehicles containing all the <code>attributeValues</code> corresponding to the <code>attributeNames</code> filter. For example, <code>attributeValues</code> could be \"<code>1.3 L R2, Blue</code>\" and the corresponding <code>attributeNames</code> filter could be \"<code>Vehicle.Body.Engine.Type, Vehicle.Color</code>\". In this case, the API will filter vehicles with attribute name <code>Vehicle.Body.Engine.Type</code> that contains a value of <code>1.3 L R2</code> AND an attribute name <code>Vehicle.Color</code> that contains a value of \"<code>Blue</code>\". A request must contain unique values for the <code>attributeNames</code> filter and the matching number of <code>attributeValues</code> filter to return the subset of vehicles that match the attributes filter condition.</p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: vehicle name, Amazon Resource Name (ARN), creation time, and last modification time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.list_vehicles_request.ListVehiclesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.list_vehicles_response.ListVehiclesResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.list_vehicles

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.list_vehicles.async_list_vehicles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.list_vehicles_request.ListVehiclesRequest = {}  # type: ignore[typeddict-item]
        if model_manifest_arn is not None:
            input_["model_manifest_arn"] = model_manifest_arn
        if attribute_names is not None:
            input_["attribute_names"] = attribute_names
        if attribute_values is not None:
            input_["attribute_values"] = attribute_values
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_vehicle_fleet(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.associate_vehicle_fleet_response.AssociateVehicleFleetResponse":
        """<p> Adds, or associates, a vehicle with a fleet. </p>

        Args:
            vehicle_name: <p> The unique ID of the vehicle to associate with the fleet. </p>
            fleet_id: <p> The ID of a fleet. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.associate_vehicle_fleet_request.AssociateVehicleFleetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.associate_vehicle_fleet_response.AssociateVehicleFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.associate_vehicle_fleet

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.associate_vehicle_fleet.async_associate_vehicle_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.associate_vehicle_fleet_request.AssociateVehicleFleetRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name
        input_["fleet_id"] = fleet_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_vehicle_fleet(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        fleet_id: "aws_sdk_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.disassociate_vehicle_fleet_response.DisassociateVehicleFleetResponse":
        """<p>Removes, or disassociates, a vehicle from a fleet. Disassociating a vehicle from a fleet doesn't delete the vehicle.</p>

        Args:
            vehicle_name: <p> The unique ID of the vehicle to disassociate from the fleet.</p>
            fleet_id: <p> The unique ID of a fleet. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotfleetwise.types.disassociate_vehicle_fleet_request.DisassociateVehicleFleetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotfleetwise.types.disassociate_vehicle_fleet_response.DisassociateVehicleFleetResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.disassociate_vehicle_fleet

            (
                output,
                http_response,
            ) = await aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.disassociate_vehicle_fleet.async_disassociate_vehicle_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.disassociate_vehicle_fleet_request.DisassociateVehicleFleetRequest = {}  # type: ignore[typeddict-item]
        input_["vehicle_name"] = vehicle_name
        input_["fleet_id"] = fleet_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
