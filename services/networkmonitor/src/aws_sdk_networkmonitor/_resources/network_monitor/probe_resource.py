from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_networkmonitor._auth._signers
import aws_sdk_networkmonitor._auth._sigv4
from aws_sdk_networkmonitor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.create_probe_input
    import aws_sdk_networkmonitor.types.create_probe_output
    import aws_sdk_networkmonitor.types.delete_probe_input
    import aws_sdk_networkmonitor.types.delete_probe_output
    import aws_sdk_networkmonitor.types.destination
    import aws_sdk_networkmonitor.types.get_probe_input
    import aws_sdk_networkmonitor.types.get_probe_output
    import aws_sdk_networkmonitor.types.packet_size
    import aws_sdk_networkmonitor.types.port
    import aws_sdk_networkmonitor.types.probe_id
    import aws_sdk_networkmonitor.types.probe_input
    import aws_sdk_networkmonitor.types.probe_state
    import aws_sdk_networkmonitor.types.protocol
    import aws_sdk_networkmonitor.types.resource_name
    import aws_sdk_networkmonitor.types.tag_map
    import aws_sdk_networkmonitor.types.update_probe_input
    import aws_sdk_networkmonitor.types.update_probe_output
    from aws_sdk_networkmonitor._services.async_network_monitor import (
        AsyncNetworkMonitorClient,
        AsyncNetworkMonitorClientConfig,
    )
    from aws_sdk_networkmonitor._services.network_monitor import (
        NetworkMonitorClient,
        NetworkMonitorClientConfig,
    )


class ProbeResource:
    def __init__(self, service: NetworkMonitorClient) -> None:
        self._service = service

    def create(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        probe: "aws_sdk_networkmonitor.types.probe_input.ProbeInput",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["aws_sdk_networkmonitor.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_networkmonitor.types.create_probe_output.CreateProbeOutput":
        """<p>Create a probe within a monitor. Once you create a probe, and it begins monitoring your network traffic, you'll incur billing charges for that probe. This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. Note the name of the <code>monitorName</code> you want to create the probe for.</p>

        Args:
            monitor_name: <p>The name of the monitor to associated with the probe. </p>
            probe: <p>Describes the details of an individual probe for a monitor.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>
            tags: <p>The list of key-value pairs created and assigned to the probe.</p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_networkmonitor.types.create_probe_input.CreateProbeInput]",
        ) -> OperationResponse[
            "aws_sdk_networkmonitor.types.create_probe_output.CreateProbeOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.create_probe

            output, http_response = (
                aws_sdk_networkmonitor._operations.network_monitor.create_probe.create_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.create_probe_input.CreateProbeInput = {}  # type: ignore[typeddict-item]
        input_["monitor_name"] = monitor_name
        input_["probe"] = probe
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        probe_id: "aws_sdk_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.get_probe_output.GetProbeOutput":
        """<p>Returns the details about a probe. This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. </p>

        Args:
            monitor_name: <p>The name of the monitor associated with the probe. Run <code>ListMonitors</code> to get a list of monitor names.</p>
            probe_id: <p>The ID of the probe to get information about. Run <code>GetMonitor</code> action to get a list of probes and probe IDs for the monitor.</p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_networkmonitor.types.get_probe_input.GetProbeInput]",
        ) -> OperationResponse[
            "aws_sdk_networkmonitor.types.get_probe_output.GetProbeOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.get_probe

            output, http_response = (
                aws_sdk_networkmonitor._operations.network_monitor.get_probe.get_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.get_probe_input.GetProbeInput = {}  # type: ignore[typeddict-item]
        input_["monitor_name"] = monitor_name
        input_["probe_id"] = probe_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        probe_id: "aws_sdk_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        state: Optional["aws_sdk_networkmonitor.types.probe_state.ProbeState"] = None,
        destination: Optional[
            "aws_sdk_networkmonitor.types.destination.Destination"
        ] = None,
        destination_port: Optional["aws_sdk_networkmonitor.types.port.Port"] = None,
        protocol: Optional["aws_sdk_networkmonitor.types.protocol.Protocol"] = None,
        packet_size: Optional[
            "aws_sdk_networkmonitor.types.packet_size.PacketSize"
        ] = None,
    ) -> "aws_sdk_networkmonitor.types.update_probe_output.UpdateProbeOutput":
        """<p>Updates a monitor probe. This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. </p> <p>You can update the following para create a monitor with probes using this command. For each probe, you define the following:</p> <ul> <li> <p> <code>state</code>—The state of the probe.</p> </li> <li> <p> <code>destination</code>— The target destination IP address for the probe.</p> </li> <li> <p> <code>destinationPort</code>—Required only if the protocol is <code>TCP</code>.</p> </li> <li> <p> <code>protocol</code>—The communication protocol between the source and destination. This will be either <code>TCP</code> or <code>ICMP</code>.</p> </li> <li> <p> <code>packetSize</code>—The size of the packets. This must be a number between <code>56</code> and <code>8500</code>.</p> </li> <li> <p>(Optional) <code>tags</code> —Key-value pairs created and assigned to the probe.</p> </li> </ul>

        Args:
            monitor_name: <p>The name of the monitor that the probe was updated for.</p>
            probe_id: <p>The ID of the probe to update.</p>
            state: <p>The state of the probe update.</p>
            destination: <p>The updated IP address for the probe destination. This must be either an IPv4 or IPv6 address.</p>
            destination_port: <p>The updated port for the probe destination. This is required only if the <code>protocol</code> is <code>TCP</code> and must be a number between <code>1</code> and <code>65536</code>.</p>
            protocol: <p>The updated network protocol for the destination. This can be either <code>TCP</code> or <code>ICMP</code>. If the protocol is <code>TCP</code>, then <code>port</code> is also required.</p>
            packet_size: <p>he updated packets size for network traffic between the source and destination. This must be a number between <code>56</code> and <code>8500</code>.</p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_networkmonitor.types.update_probe_input.UpdateProbeInput]",
        ) -> OperationResponse[
            "aws_sdk_networkmonitor.types.update_probe_output.UpdateProbeOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.update_probe

            output, http_response = (
                aws_sdk_networkmonitor._operations.network_monitor.update_probe.update_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.update_probe_input.UpdateProbeInput = {}  # type: ignore[typeddict-item]
        input_["monitor_name"] = monitor_name
        input_["probe_id"] = probe_id
        if state is not None:
            input_["state"] = state
        if destination is not None:
            input_["destination"] = destination
        if destination_port is not None:
            input_["destination_port"] = destination_port
        if protocol is not None:
            input_["protocol"] = protocol
        if packet_size is not None:
            input_["packet_size"] = packet_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        probe_id: "aws_sdk_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.delete_probe_output.DeleteProbeOutput":
        """<p>Deletes the specified probe. Once a probe is deleted you'll no longer incur any billing fees for that probe.</p> <p>This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. You can only delete a single probe at a time using this action. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete. </p>
            probe_id: <p>The ID of the probe to delete. </p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_networkmonitor.types.delete_probe_input.DeleteProbeInput]",
        ) -> OperationResponse[
            "aws_sdk_networkmonitor.types.delete_probe_output.DeleteProbeOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.delete_probe

            output, http_response = (
                aws_sdk_networkmonitor._operations.network_monitor.delete_probe.delete_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.delete_probe_input.DeleteProbeInput = {}  # type: ignore[typeddict-item]
        input_["monitor_name"] = monitor_name
        input_["probe_id"] = probe_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncProbeResource:
    def __init__(self, service: AsyncNetworkMonitorClient) -> None:
        self._service = service

    async def create(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        probe: "aws_sdk_networkmonitor.types.probe_input.ProbeInput",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["aws_sdk_networkmonitor.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_networkmonitor.types.create_probe_output.CreateProbeOutput":
        """<p>Create a probe within a monitor. Once you create a probe, and it begins monitoring your network traffic, you'll incur billing charges for that probe. This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. Note the name of the <code>monitorName</code> you want to create the probe for.</p>

        Args:
            monitor_name: <p>The name of the monitor to associated with the probe. </p>
            probe: <p>Describes the details of an individual probe for a monitor.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>
            tags: <p>The list of key-value pairs created and assigned to the probe.</p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.create_probe_input.CreateProbeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.create_probe_output.CreateProbeOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.create_probe

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.create_probe.async_create_probe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.create_probe_input.CreateProbeInput = {}  # type: ignore[typeddict-item]
        input_["monitor_name"] = monitor_name
        input_["probe"] = probe
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        probe_id: "aws_sdk_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.get_probe_output.GetProbeOutput":
        """<p>Returns the details about a probe. This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. </p>

        Args:
            monitor_name: <p>The name of the monitor associated with the probe. Run <code>ListMonitors</code> to get a list of monitor names.</p>
            probe_id: <p>The ID of the probe to get information about. Run <code>GetMonitor</code> action to get a list of probes and probe IDs for the monitor.</p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.get_probe_input.GetProbeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.get_probe_output.GetProbeOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.get_probe

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.get_probe.async_get_probe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.get_probe_input.GetProbeInput = {}  # type: ignore[typeddict-item]
        input_["monitor_name"] = monitor_name
        input_["probe_id"] = probe_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        probe_id: "aws_sdk_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
        state: Optional["aws_sdk_networkmonitor.types.probe_state.ProbeState"] = None,
        destination: Optional[
            "aws_sdk_networkmonitor.types.destination.Destination"
        ] = None,
        destination_port: Optional["aws_sdk_networkmonitor.types.port.Port"] = None,
        protocol: Optional["aws_sdk_networkmonitor.types.protocol.Protocol"] = None,
        packet_size: Optional[
            "aws_sdk_networkmonitor.types.packet_size.PacketSize"
        ] = None,
    ) -> "aws_sdk_networkmonitor.types.update_probe_output.UpdateProbeOutput":
        """<p>Updates a monitor probe. This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. </p> <p>You can update the following para create a monitor with probes using this command. For each probe, you define the following:</p> <ul> <li> <p> <code>state</code>—The state of the probe.</p> </li> <li> <p> <code>destination</code>— The target destination IP address for the probe.</p> </li> <li> <p> <code>destinationPort</code>—Required only if the protocol is <code>TCP</code>.</p> </li> <li> <p> <code>protocol</code>—The communication protocol between the source and destination. This will be either <code>TCP</code> or <code>ICMP</code>.</p> </li> <li> <p> <code>packetSize</code>—The size of the packets. This must be a number between <code>56</code> and <code>8500</code>.</p> </li> <li> <p>(Optional) <code>tags</code> —Key-value pairs created and assigned to the probe.</p> </li> </ul>

        Args:
            monitor_name: <p>The name of the monitor that the probe was updated for.</p>
            probe_id: <p>The ID of the probe to update.</p>
            state: <p>The state of the probe update.</p>
            destination: <p>The updated IP address for the probe destination. This must be either an IPv4 or IPv6 address.</p>
            destination_port: <p>The updated port for the probe destination. This is required only if the <code>protocol</code> is <code>TCP</code> and must be a number between <code>1</code> and <code>65536</code>.</p>
            protocol: <p>The updated network protocol for the destination. This can be either <code>TCP</code> or <code>ICMP</code>. If the protocol is <code>TCP</code>, then <code>port</code> is also required.</p>
            packet_size: <p>he updated packets size for network traffic between the source and destination. This must be a number between <code>56</code> and <code>8500</code>.</p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.update_probe_input.UpdateProbeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.update_probe_output.UpdateProbeOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.update_probe

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.update_probe.async_update_probe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.update_probe_input.UpdateProbeInput = {}  # type: ignore[typeddict-item]
        input_["monitor_name"] = monitor_name
        input_["probe_id"] = probe_id
        if state is not None:
            input_["state"] = state
        if destination is not None:
            input_["destination"] = destination
        if destination_port is not None:
            input_["destination_port"] = destination_port
        if protocol is not None:
            input_["protocol"] = protocol
        if packet_size is not None:
            input_["packet_size"] = packet_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        probe_id: "aws_sdk_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.delete_probe_output.DeleteProbeOutput":
        """<p>Deletes the specified probe. Once a probe is deleted you'll no longer incur any billing fees for that probe.</p> <p>This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. You can only delete a single probe at a time using this action. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete. </p>
            probe_id: <p>The ID of the probe to delete. </p>

        Raises:
            aws_sdk_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            aws_sdk_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            aws_sdk_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            aws_sdk_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            aws_sdk_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.delete_probe_input.DeleteProbeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.delete_probe_output.DeleteProbeOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.delete_probe

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.delete_probe.async_delete_probe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_networkmonitor.types.delete_probe_input.DeleteProbeInput = {}  # type: ignore[typeddict-item]
        input_["monitor_name"] = monitor_name
        input_["probe_id"] = probe_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
