from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_iot_managed_integrations._auth._signers
import aws_sdk_iot_managed_integrations._auth._sigv4
from aws_sdk_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.account_association_id
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.connector_association_id
    import aws_sdk_iot_managed_integrations.types.connector_device_id_list
    import aws_sdk_iot_managed_integrations.types.custom_protocol_detail
    import aws_sdk_iot_managed_integrations.types.device_discovery_id
    import aws_sdk_iot_managed_integrations.types.device_discovery_status
    import aws_sdk_iot_managed_integrations.types.device_discovery_summary
    import aws_sdk_iot_managed_integrations.types.discovered_device_summary
    import aws_sdk_iot_managed_integrations.types.discovery_auth_material_string
    import aws_sdk_iot_managed_integrations.types.discovery_auth_material_type
    import aws_sdk_iot_managed_integrations.types.discovery_type
    import aws_sdk_iot_managed_integrations.types.get_device_discovery_request
    import aws_sdk_iot_managed_integrations.types.get_device_discovery_response
    import aws_sdk_iot_managed_integrations.types.list_device_discoveries_request
    import aws_sdk_iot_managed_integrations.types.list_device_discoveries_response
    import aws_sdk_iot_managed_integrations.types.list_discovered_devices_request
    import aws_sdk_iot_managed_integrations.types.list_discovered_devices_response
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.protocol_type
    import aws_sdk_iot_managed_integrations.types.start_device_discovery_request
    import aws_sdk_iot_managed_integrations.types.start_device_discovery_response
    import aws_sdk_iot_managed_integrations.types.tags_map
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class DeviceDiscoveryResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        discovery_type: "aws_sdk_iot_managed_integrations.types.discovery_type.DiscoveryType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        custom_protocol_detail: Optional[
            "aws_sdk_iot_managed_integrations.types.custom_protocol_detail.CustomProtocolDetail"
        ] = None,
        controller_identifier: Optional[
            "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
        connector_association_identifier: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
        ] = None,
        account_association_id: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
        authentication_material: Optional[
            "aws_sdk_iot_managed_integrations.types.discovery_auth_material_string.DiscoveryAuthMaterialString"
        ] = None,
        authentication_material_type: Optional[
            "aws_sdk_iot_managed_integrations.types.discovery_auth_material_type.DiscoveryAuthMaterialType"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
        connector_device_id_list: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_device_id_list.ConnectorDeviceIdList"
        ] = None,
        protocol: Optional[
            "aws_sdk_iot_managed_integrations.types.protocol_type.ProtocolType"
        ] = None,
        end_device_identifier: Optional[
            "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.start_device_discovery_response.StartDeviceDiscoveryResponse":
        """<p> This API is used to start device discovery for hub-connected and third-party-connected devices. The authentication material (install code) is delivered as a message to the controller instructing it to start the discovery.</p>

        Args:
            discovery_type: <p>The discovery type supporting the type of device to be discovered in the device discovery task request.</p>
            custom_protocol_detail: <p>Additional protocol-specific details required for device discovery, which vary based on the discovery type.</p> <note> <p>For a <code>DiscoveryType</code> of <code>CUSTOM</code>, the string-to-string map must have a key value of <code>Name</code> set to a non-empty-string.</p> </note>
            controller_identifier: <p>The id of the end-user's IoT hub.</p>
            connector_association_identifier: <p>The id of the connector association.</p>
            account_association_id: <p>The identifier of the cloud-to-cloud account association to use for discovery of third-party devices.</p>
            authentication_material: <p>The authentication material required to start the local device discovery job request.</p>
            authentication_material_type: <p>The type of authentication material used for device discovery jobs.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the device discovery request.</p>
            connector_device_id_list: <p>Used as a filter for PLA discoveries.</p>
            protocol: <p>The protocol type for capability rediscovery (ZWAVE, ZIGBEE, or CUSTOM).</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>
            end_device_identifier: <p>The unique id of the end device for capability rediscovery.</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.start_device_discovery_response.StartDeviceDiscoveryResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.start_device_discovery

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.start_device_discovery.start_device_discovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest = {}  # type: ignore[typeddict-item]
        input_["discovery_type"] = discovery_type
        if custom_protocol_detail is not None:
            input_["custom_protocol_detail"] = custom_protocol_detail
        if controller_identifier is not None:
            input_["controller_identifier"] = controller_identifier
        if connector_association_identifier is not None:
            input_["connector_association_identifier"] = (
                connector_association_identifier
            )
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id
        if authentication_material is not None:
            input_["authentication_material"] = authentication_material
        if authentication_material_type is not None:
            input_["authentication_material_type"] = authentication_material_type
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if connector_device_id_list is not None:
            input_["connector_device_id_list"] = connector_device_id_list
        if protocol is not None:
            input_["protocol"] = protocol
        if end_device_identifier is not None:
            input_["end_device_identifier"] = end_device_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse":
        """<p> Get the current state of a device discovery.</p>

        Args:
            identifier: <p>The id of the device discovery job request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_device_discovery_request.GetDeviceDiscoveryRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_device_discovery

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_device_discovery.get_device_discovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_device_discovery_request.GetDeviceDiscoveryRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        type_filter: Optional[
            "aws_sdk_iot_managed_integrations.types.discovery_type.DiscoveryType"
        ] = None,
        status_filter: Optional[
            "aws_sdk_iot_managed_integrations.types.device_discovery_status.DeviceDiscoveryStatus"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_device_discoveries_response.ListDeviceDiscoveriesResponse":
        """<p>Lists all device discovery tasks, with optional filtering by type and status.</p>

        Args:
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of device discovery jobs to return in a single response.</p>
            type_filter: <p>The discovery type to filter device discovery jobs by.</p>
            status_filter: <p>The status to filter device discovery jobs by.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_device_discoveries_request.ListDeviceDiscoveriesRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_device_discoveries_response.ListDeviceDiscoveriesResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_device_discoveries

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_device_discoveries.list_device_discoveries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_device_discoveries_request.ListDeviceDiscoveriesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type_filter is not None:
            input_["type_filter"] = type_filter
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_discovered_devices(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse":
        """<p>Lists all devices discovered during a specific device discovery task.</p>

        Args:
            identifier: <p>The identifier of the device discovery job to list discovered devices for.</p>
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of discovered devices to return in a single response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_discovered_devices_request.ListDiscoveredDevicesRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_discovered_devices

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_discovered_devices.list_discovered_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_discovered_devices_request.ListDiscoveredDevicesRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
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


class AsyncDeviceDiscoveryResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        discovery_type: "aws_sdk_iot_managed_integrations.types.discovery_type.DiscoveryType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        custom_protocol_detail: Optional[
            "aws_sdk_iot_managed_integrations.types.custom_protocol_detail.CustomProtocolDetail"
        ] = None,
        controller_identifier: Optional[
            "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
        connector_association_identifier: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
        ] = None,
        account_association_id: Optional[
            "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
        authentication_material: Optional[
            "aws_sdk_iot_managed_integrations.types.discovery_auth_material_string.DiscoveryAuthMaterialString"
        ] = None,
        authentication_material_type: Optional[
            "aws_sdk_iot_managed_integrations.types.discovery_auth_material_type.DiscoveryAuthMaterialType"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
        connector_device_id_list: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_device_id_list.ConnectorDeviceIdList"
        ] = None,
        protocol: Optional[
            "aws_sdk_iot_managed_integrations.types.protocol_type.ProtocolType"
        ] = None,
        end_device_identifier: Optional[
            "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.start_device_discovery_response.StartDeviceDiscoveryResponse":
        """<p> This API is used to start device discovery for hub-connected and third-party-connected devices. The authentication material (install code) is delivered as a message to the controller instructing it to start the discovery.</p>

        Args:
            discovery_type: <p>The discovery type supporting the type of device to be discovered in the device discovery task request.</p>
            custom_protocol_detail: <p>Additional protocol-specific details required for device discovery, which vary based on the discovery type.</p> <note> <p>For a <code>DiscoveryType</code> of <code>CUSTOM</code>, the string-to-string map must have a key value of <code>Name</code> set to a non-empty-string.</p> </note>
            controller_identifier: <p>The id of the end-user's IoT hub.</p>
            connector_association_identifier: <p>The id of the connector association.</p>
            account_association_id: <p>The identifier of the cloud-to-cloud account association to use for discovery of third-party devices.</p>
            authentication_material: <p>The authentication material required to start the local device discovery job request.</p>
            authentication_material_type: <p>The type of authentication material used for device discovery jobs.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the device discovery request.</p>
            connector_device_id_list: <p>Used as a filter for PLA discoveries.</p>
            protocol: <p>The protocol type for capability rediscovery (ZWAVE, ZIGBEE, or CUSTOM).</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>
            end_device_identifier: <p>The unique id of the end device for capability rediscovery.</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.start_device_discovery_response.StartDeviceDiscoveryResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.start_device_discovery

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.start_device_discovery.async_start_device_discovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest = {}  # type: ignore[typeddict-item]
        input_["discovery_type"] = discovery_type
        if custom_protocol_detail is not None:
            input_["custom_protocol_detail"] = custom_protocol_detail
        if controller_identifier is not None:
            input_["controller_identifier"] = controller_identifier
        if connector_association_identifier is not None:
            input_["connector_association_identifier"] = (
                connector_association_identifier
            )
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id
        if authentication_material is not None:
            input_["authentication_material"] = authentication_material
        if authentication_material_type is not None:
            input_["authentication_material_type"] = authentication_material_type
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if connector_device_id_list is not None:
            input_["connector_device_id_list"] = connector_device_id_list
        if protocol is not None:
            input_["protocol"] = protocol
        if end_device_identifier is not None:
            input_["end_device_identifier"] = end_device_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse":
        """<p> Get the current state of a device discovery.</p>

        Args:
            identifier: <p>The id of the device discovery job request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_device_discovery_request.GetDeviceDiscoveryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_device_discovery

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_device_discovery.async_get_device_discovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_device_discovery_request.GetDeviceDiscoveryRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        type_filter: Optional[
            "aws_sdk_iot_managed_integrations.types.discovery_type.DiscoveryType"
        ] = None,
        status_filter: Optional[
            "aws_sdk_iot_managed_integrations.types.device_discovery_status.DeviceDiscoveryStatus"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_device_discoveries_response.ListDeviceDiscoveriesResponse":
        """<p>Lists all device discovery tasks, with optional filtering by type and status.</p>

        Args:
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of device discovery jobs to return in a single response.</p>
            type_filter: <p>The discovery type to filter device discovery jobs by.</p>
            status_filter: <p>The status to filter device discovery jobs by.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_device_discoveries_request.ListDeviceDiscoveriesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_device_discoveries_response.ListDeviceDiscoveriesResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_device_discoveries

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_device_discoveries.async_list_device_discoveries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_device_discoveries_request.ListDeviceDiscoveriesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type_filter is not None:
            input_["type_filter"] = type_filter
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_discovered_devices(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse":
        """<p>Lists all devices discovered during a specific device discovery task.</p>

        Args:
            identifier: <p>The identifier of the device discovery job to list discovered devices for.</p>
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of discovered devices to return in a single response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_discovered_devices_request.ListDiscoveredDevicesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_discovered_devices

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_discovered_devices.async_list_discovered_devices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_discovered_devices_request.ListDiscoveredDevicesRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier
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
