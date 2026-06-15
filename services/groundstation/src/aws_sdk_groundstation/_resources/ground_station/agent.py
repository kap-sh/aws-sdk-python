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
    import aws_sdk_groundstation.types.agent_details
    import aws_sdk_groundstation.types.aggregate_status
    import aws_sdk_groundstation.types.component_status_list
    import aws_sdk_groundstation.types.discovery_data
    import aws_sdk_groundstation.types.get_agent_configuration_request
    import aws_sdk_groundstation.types.get_agent_configuration_response
    import aws_sdk_groundstation.types.register_agent_request
    import aws_sdk_groundstation.types.register_agent_response
    import aws_sdk_groundstation.types.tags_map
    import aws_sdk_groundstation.types.update_agent_status_request
    import aws_sdk_groundstation.types.update_agent_status_response
    import aws_sdk_groundstation.types.uuid
    from aws_sdk_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from aws_sdk_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class Agent:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def create(
        self,
        discovery_data: "aws_sdk_groundstation.types.discovery_data.DiscoveryData",
        agent_details: "aws_sdk_groundstation.types.agent_details.AgentDetails",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        tags: Optional["aws_sdk_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_groundstation.types.register_agent_response.RegisterAgentResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p> Registers a new agent with AWS Ground Station. </p>

        Args:
            discovery_data: <p>Data for associating an agent with the capabilities it is managing.</p>
            agent_details: <p>Detailed information about the agent being registered.</p>
            tags: <p>Tags assigned to an <code>Agent</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.register_agent_request.RegisterAgentRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.register_agent_response.RegisterAgentResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.register_agent

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.register_agent.register_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.register_agent_request.RegisterAgentRequest = {}  # type: ignore[typeddict-item]
        input_["discovery_data"] = discovery_data
        input_["agent_details"] = agent_details
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
        agent_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.get_agent_configuration_response.GetAgentConfigurationResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Gets the latest configuration information for a registered agent.</p>

        Args:
            agent_id: <p>UUID of agent to get configuration information for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.get_agent_configuration_request.GetAgentConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.get_agent_configuration_response.GetAgentConfigurationResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.get_agent_configuration

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.get_agent_configuration.get_agent_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.get_agent_configuration_request.GetAgentConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        agent_id: "aws_sdk_groundstation.types.uuid.Uuid",
        task_id: "aws_sdk_groundstation.types.uuid.Uuid",
        aggregate_status: "aws_sdk_groundstation.types.aggregate_status.AggregateStatus",
        component_statuses: "aws_sdk_groundstation.types.component_status_list.ComponentStatusList",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.update_agent_status_response.UpdateAgentStatusResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Update the status of the agent.</p>

        Args:
            agent_id: <p>UUID of agent to update.</p>
            task_id: <p>GUID of agent task.</p>
            aggregate_status: <p>Aggregate status for agent.</p>
            component_statuses: <p>List of component statuses for agent.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.update_agent_status_request.UpdateAgentStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.update_agent_status_response.UpdateAgentStatusResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.update_agent_status

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.update_agent_status.update_agent_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.update_agent_status_request.UpdateAgentStatusRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["task_id"] = task_id
        input_["aggregate_status"] = aggregate_status
        input_["component_statuses"] = component_statuses

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAgent:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def create(
        self,
        discovery_data: "aws_sdk_groundstation.types.discovery_data.DiscoveryData",
        agent_details: "aws_sdk_groundstation.types.agent_details.AgentDetails",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        tags: Optional["aws_sdk_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_groundstation.types.register_agent_response.RegisterAgentResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p> Registers a new agent with AWS Ground Station. </p>

        Args:
            discovery_data: <p>Data for associating an agent with the capabilities it is managing.</p>
            agent_details: <p>Detailed information about the agent being registered.</p>
            tags: <p>Tags assigned to an <code>Agent</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.register_agent_request.RegisterAgentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.register_agent_response.RegisterAgentResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.register_agent

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.register_agent.async_register_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.register_agent_request.RegisterAgentRequest = {}  # type: ignore[typeddict-item]
        input_["discovery_data"] = discovery_data
        input_["agent_details"] = agent_details
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
        agent_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.get_agent_configuration_response.GetAgentConfigurationResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Gets the latest configuration information for a registered agent.</p>

        Args:
            agent_id: <p>UUID of agent to get configuration information for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.get_agent_configuration_request.GetAgentConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.get_agent_configuration_response.GetAgentConfigurationResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.get_agent_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.get_agent_configuration.async_get_agent_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.get_agent_configuration_request.GetAgentConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        agent_id: "aws_sdk_groundstation.types.uuid.Uuid",
        task_id: "aws_sdk_groundstation.types.uuid.Uuid",
        aggregate_status: "aws_sdk_groundstation.types.aggregate_status.AggregateStatus",
        component_statuses: "aws_sdk_groundstation.types.component_status_list.ComponentStatusList",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.update_agent_status_response.UpdateAgentStatusResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Update the status of the agent.</p>

        Args:
            agent_id: <p>UUID of agent to update.</p>
            task_id: <p>GUID of agent task.</p>
            aggregate_status: <p>Aggregate status for agent.</p>
            component_statuses: <p>List of component statuses for agent.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.update_agent_status_request.UpdateAgentStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.update_agent_status_response.UpdateAgentStatusResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.update_agent_status

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.update_agent_status.async_update_agent_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.update_agent_status_request.UpdateAgentStatusRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["task_id"] = task_id
        input_["aggregate_status"] = aggregate_status
        input_["component_statuses"] = component_statuses

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
