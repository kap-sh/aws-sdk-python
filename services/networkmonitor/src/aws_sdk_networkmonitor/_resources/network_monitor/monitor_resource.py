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
    import aws_sdk_networkmonitor.types.aggregation_period
    import aws_sdk_networkmonitor.types.create_monitor_input
    import aws_sdk_networkmonitor.types.create_monitor_output
    import aws_sdk_networkmonitor.types.create_monitor_probe_input_list
    import aws_sdk_networkmonitor.types.delete_monitor_input
    import aws_sdk_networkmonitor.types.delete_monitor_output
    import aws_sdk_networkmonitor.types.get_monitor_input
    import aws_sdk_networkmonitor.types.get_monitor_output
    import aws_sdk_networkmonitor.types.list_monitors_input
    import aws_sdk_networkmonitor.types.list_monitors_output
    import aws_sdk_networkmonitor.types.max_results
    import aws_sdk_networkmonitor.types.monitor_summary
    import aws_sdk_networkmonitor.types.pagination_token
    import aws_sdk_networkmonitor.types.resource_name
    import aws_sdk_networkmonitor.types.tag_map
    import aws_sdk_networkmonitor.types.update_monitor_input
    import aws_sdk_networkmonitor.types.update_monitor_output
    from aws_sdk_networkmonitor._services.async_network_monitor import (
        AsyncNetworkMonitorClient,
        AsyncNetworkMonitorClientConfig,
    )
    from aws_sdk_networkmonitor._services.network_monitor import (
        NetworkMonitorClient,
        NetworkMonitorClientConfig,
    )


class MonitorResource:
    def __init__(self, service: NetworkMonitorClient) -> None:
        self._service = service

    def put(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        probes: Optional[
            "aws_sdk_networkmonitor.types.create_monitor_probe_input_list.CreateMonitorProbeInputList"
        ] = None,
        aggregation_period: Optional[
            "aws_sdk_networkmonitor.types.aggregation_period.AggregationPeriod"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["aws_sdk_networkmonitor.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_networkmonitor.types.create_monitor_output.CreateMonitorOutput":
        """<p>Creates a monitor between a source subnet and destination IP address. Within a monitor you'll create one or more probes that monitor network traffic between your source Amazon Web Services VPC subnets and your destination IP addresses. Each probe then aggregates and sends metrics to Amazon CloudWatch.</p> <p>You can also create a monitor with probes using this command. For each probe, you define the following:</p> <ul> <li> <p> <code>source</code>—The subnet IDs where the probes will be created.</p> </li> <li> <p> <code>destination</code>— The target destination IP address for the probe.</p> </li> <li> <p> <code>destinationPort</code>—Required only if the protocol is <code>TCP</code>.</p> </li> <li> <p> <code>protocol</code>—The communication protocol between the source and destination. This will be either <code>TCP</code> or <code>ICMP</code>.</p> </li> <li> <p> <code>packetSize</code>—The size of the packets. This must be a number between <code>56</code> and <code>8500</code>.</p> </li> <li> <p>(Optional) <code>tags</code> —Key-value pairs created and assigned to the probe.</p> </li> </ul>

        Args:
            monitor_name: <p>The name identifying the monitor. It can contain only letters, underscores (_), or dashes (-), and can be up to 200 characters.</p>
            probes: <p>Displays a list of all of the probes created for a monitor.</p>
            aggregation_period: <p>The time, in seconds, that metrics are aggregated and sent to Amazon CloudWatch. Valid values are either <code>30</code> or <code>60</code>. <code>60</code> is the default if no period is chosen.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>
            tags: <p>The list of key-value pairs created and assigned to the monitor.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_networkmonitor.types.create_monitor_input.CreateMonitorInput]",
        ) -> OperationResponse[
            "aws_sdk_networkmonitor.types.create_monitor_output.CreateMonitorOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.create_monitor

            output, http_response = (
                aws_sdk_networkmonitor._operations.network_monitor.create_monitor.create_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_networkmonitor.types.create_monitor_input.CreateMonitorInput = {}  # type: ignore[typeddict-item]
        input["monitor_name"] = monitor_name
        if probes is not None:
            input["probes"] = probes
        if aggregation_period is not None:
            input["aggregation_period"] = aggregation_period
        if client_token is not None:
            input["client_token"] = client_token
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
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.get_monitor_output.GetMonitorOutput":
        """<p>Returns details about a specific monitor. </p> <p>This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor that details are returned for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_networkmonitor.types.get_monitor_input.GetMonitorInput]",
        ) -> OperationResponse[
            "aws_sdk_networkmonitor.types.get_monitor_output.GetMonitorOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.get_monitor

            output, http_response = (
                aws_sdk_networkmonitor._operations.network_monitor.get_monitor.get_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_networkmonitor.types.get_monitor_input.GetMonitorInput = {}  # type: ignore[typeddict-item]
        input["monitor_name"] = monitor_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        aggregation_period: "aws_sdk_networkmonitor.types.aggregation_period.AggregationPeriod",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.update_monitor_output.UpdateMonitorOutput":
        """<p>Updates the <code>aggregationPeriod</code> for a monitor. Monitors support an <code>aggregationPeriod</code> of either <code>30</code> or <code>60</code> seconds. This action requires the <code>monitorName</code> and <code>probeId</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor to update. </p>
            aggregation_period: <p>The aggregation time, in seconds, to change to. This must be either <code>30</code> or <code>60</code>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_networkmonitor.types.update_monitor_input.UpdateMonitorInput]",
        ) -> OperationResponse[
            "aws_sdk_networkmonitor.types.update_monitor_output.UpdateMonitorOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.update_monitor

            output, http_response = (
                aws_sdk_networkmonitor._operations.network_monitor.update_monitor.update_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_networkmonitor.types.update_monitor_input.UpdateMonitorInput = {}  # type: ignore[typeddict-item]
        input["monitor_name"] = monitor_name
        input["aggregation_period"] = aggregation_period

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.delete_monitor_output.DeleteMonitorOutput":
        """<p>Deletes a specified monitor.</p> <p>This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_networkmonitor.types.delete_monitor_input.DeleteMonitorInput]",
        ) -> OperationResponse[
            "aws_sdk_networkmonitor.types.delete_monitor_output.DeleteMonitorOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.delete_monitor

            output, http_response = (
                aws_sdk_networkmonitor._operations.network_monitor.delete_monitor.delete_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_networkmonitor.types.delete_monitor_input.DeleteMonitorInput = {}  # type: ignore[typeddict-item]
        input["monitor_name"] = monitor_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        next_token: Optional[
            "aws_sdk_networkmonitor.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_networkmonitor.types.max_results.MaxResults"
        ] = None,
        state: Optional[str] = None,
    ) -> "aws_sdk_networkmonitor.types.list_monitors_output.ListMonitorsOutput":
        """<p>Returns a list of all of your monitors.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            state: <p>The list of all monitors and their states.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_networkmonitor.types.list_monitors_input.ListMonitorsInput]",
        ) -> OperationResponse[
            "aws_sdk_networkmonitor.types.list_monitors_output.ListMonitorsOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.list_monitors

            output, http_response = (
                aws_sdk_networkmonitor._operations.network_monitor.list_monitors.list_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_networkmonitor.types.list_monitors_input.ListMonitorsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if state is not None:
            input["state"] = state

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncMonitorResource:
    def __init__(self, service: AsyncNetworkMonitorClient) -> None:
        self._service = service

    async def put(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
        probes: Optional[
            "aws_sdk_networkmonitor.types.create_monitor_probe_input_list.CreateMonitorProbeInputList"
        ] = None,
        aggregation_period: Optional[
            "aws_sdk_networkmonitor.types.aggregation_period.AggregationPeriod"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["aws_sdk_networkmonitor.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_networkmonitor.types.create_monitor_output.CreateMonitorOutput":
        """<p>Creates a monitor between a source subnet and destination IP address. Within a monitor you'll create one or more probes that monitor network traffic between your source Amazon Web Services VPC subnets and your destination IP addresses. Each probe then aggregates and sends metrics to Amazon CloudWatch.</p> <p>You can also create a monitor with probes using this command. For each probe, you define the following:</p> <ul> <li> <p> <code>source</code>—The subnet IDs where the probes will be created.</p> </li> <li> <p> <code>destination</code>— The target destination IP address for the probe.</p> </li> <li> <p> <code>destinationPort</code>—Required only if the protocol is <code>TCP</code>.</p> </li> <li> <p> <code>protocol</code>—The communication protocol between the source and destination. This will be either <code>TCP</code> or <code>ICMP</code>.</p> </li> <li> <p> <code>packetSize</code>—The size of the packets. This must be a number between <code>56</code> and <code>8500</code>.</p> </li> <li> <p>(Optional) <code>tags</code> —Key-value pairs created and assigned to the probe.</p> </li> </ul>

        Args:
            monitor_name: <p>The name identifying the monitor. It can contain only letters, underscores (_), or dashes (-), and can be up to 200 characters.</p>
            probes: <p>Displays a list of all of the probes created for a monitor.</p>
            aggregation_period: <p>The time, in seconds, that metrics are aggregated and sent to Amazon CloudWatch. Valid values are either <code>30</code> or <code>60</code>. <code>60</code> is the default if no period is chosen.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>
            tags: <p>The list of key-value pairs created and assigned to the monitor.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.create_monitor_input.CreateMonitorInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.create_monitor_output.CreateMonitorOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.create_monitor

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.create_monitor.async_create_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_networkmonitor.types.create_monitor_input.CreateMonitorInput = {}  # type: ignore[typeddict-item]
        input["monitor_name"] = monitor_name
        if probes is not None:
            input["probes"] = probes
        if aggregation_period is not None:
            input["aggregation_period"] = aggregation_period
        if client_token is not None:
            input["client_token"] = client_token
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
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.get_monitor_output.GetMonitorOutput":
        """<p>Returns details about a specific monitor. </p> <p>This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor that details are returned for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.get_monitor_input.GetMonitorInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.get_monitor_output.GetMonitorOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.get_monitor

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.get_monitor.async_get_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_networkmonitor.types.get_monitor_input.GetMonitorInput = {}  # type: ignore[typeddict-item]
        input["monitor_name"] = monitor_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        aggregation_period: "aws_sdk_networkmonitor.types.aggregation_period.AggregationPeriod",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.update_monitor_output.UpdateMonitorOutput":
        """<p>Updates the <code>aggregationPeriod</code> for a monitor. Monitors support an <code>aggregationPeriod</code> of either <code>30</code> or <code>60</code> seconds. This action requires the <code>monitorName</code> and <code>probeId</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor to update. </p>
            aggregation_period: <p>The aggregation time, in seconds, to change to. This must be either <code>30</code> or <code>60</code>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.update_monitor_input.UpdateMonitorInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.update_monitor_output.UpdateMonitorOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.update_monitor

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.update_monitor.async_update_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_networkmonitor.types.update_monitor_input.UpdateMonitorInput = {}  # type: ignore[typeddict-item]
        input["monitor_name"] = monitor_name
        input["aggregation_period"] = aggregation_period

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "aws_sdk_networkmonitor.types.delete_monitor_output.DeleteMonitorOutput":
        """<p>Deletes a specified monitor.</p> <p>This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.delete_monitor_input.DeleteMonitorInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.delete_monitor_output.DeleteMonitorOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.delete_monitor

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.delete_monitor.async_delete_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_networkmonitor.types.delete_monitor_input.DeleteMonitorInput = {}  # type: ignore[typeddict-item]
        input["monitor_name"] = monitor_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
        next_token: Optional[
            "aws_sdk_networkmonitor.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_networkmonitor.types.max_results.MaxResults"
        ] = None,
        state: Optional[str] = None,
    ) -> "aws_sdk_networkmonitor.types.list_monitors_output.ListMonitorsOutput":
        """<p>Returns a list of all of your monitors.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            state: <p>The list of all monitors and their states.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_networkmonitor.types.list_monitors_input.ListMonitorsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_networkmonitor.types.list_monitors_output.ListMonitorsOutput"
        ]:
            import aws_sdk_networkmonitor._operations.network_monitor.list_monitors

            (
                output,
                http_response,
            ) = await aws_sdk_networkmonitor._operations.network_monitor.list_monitors.async_list_monitors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_networkmonitor.types.list_monitors_input.ListMonitorsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if state is not None:
            input["state"] = state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
