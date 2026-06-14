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
    import aws_sdk_groundstation.types.create_dataflow_endpoint_group_request
    import aws_sdk_groundstation.types.dataflow_endpoint_group_duration_in_seconds
    import aws_sdk_groundstation.types.dataflow_endpoint_group_id_response
    import aws_sdk_groundstation.types.dataflow_endpoint_list_item
    import aws_sdk_groundstation.types.delete_dataflow_endpoint_group_request
    import aws_sdk_groundstation.types.endpoint_details_list
    import aws_sdk_groundstation.types.get_dataflow_endpoint_group_request
    import aws_sdk_groundstation.types.get_dataflow_endpoint_group_response
    import aws_sdk_groundstation.types.list_dataflow_endpoint_groups_request
    import aws_sdk_groundstation.types.list_dataflow_endpoint_groups_response
    import aws_sdk_groundstation.types.pagination_max_results
    import aws_sdk_groundstation.types.pagination_token
    import aws_sdk_groundstation.types.tags_map
    import aws_sdk_groundstation.types.uuid
    from aws_sdk_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from aws_sdk_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class DataflowEndpointGroup:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def create(
        self,
        endpoint_details: "aws_sdk_groundstation.types.endpoint_details_list.EndpointDetailsList",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        tags: Optional["aws_sdk_groundstation.types.tags_map.TagsMap"] = None,
        contact_pre_pass_duration_seconds: Optional[
            "aws_sdk_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "aws_sdk_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
    ) -> "aws_sdk_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse":
        """<p>Creates a <code>DataflowEndpoint</code> group containing the specified list of <code> DataflowEndpoint</code> objects.</p> <p>The <code>name</code> field in each endpoint is used in your mission profile <code> DataflowEndpointConfig</code> to specify which endpoints to use during a contact.</p> <p>When a contact uses multiple <code>DataflowEndpointConfig</code> objects, each <code> Config</code> must match a <code>DataflowEndpoint</code> in the same group.</p>

        Args:
            endpoint_details: <p>Endpoint details of each endpoint in the dataflow endpoint group. All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix <a href=\"https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AwsGroundStationAgentEndpoint.html\"> AWS Ground Station Agent endpoints</a> with <a href=\"https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html\">Dataflow endpoints</a> in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type. </p>
            tags: <p>Tags of a dataflow endpoint group.</p>
            contact_pre_pass_duration_seconds: <p> Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a <code>PREPASS</code> state. A <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html\">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>PREPASS</code> state. </p>
            contact_post_pass_duration_seconds: <p> Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a <code>POSTPASS</code> state. A <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html\">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>POSTPASS</code> state. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.create_dataflow_endpoint_group_request.CreateDataflowEndpointGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.create_dataflow_endpoint_group

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.create_dataflow_endpoint_group.create_dataflow_endpoint_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.create_dataflow_endpoint_group_request.CreateDataflowEndpointGroupRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_details"] = endpoint_details
        if tags is not None:
            input_["tags"] = tags
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        dataflow_endpoint_group_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.get_dataflow_endpoint_group_response.GetDataflowEndpointGroupResponse":
        """<p>Returns the dataflow endpoint group.</p>

        Args:
            dataflow_endpoint_group_id: <p>UUID of a dataflow endpoint group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.get_dataflow_endpoint_group_request.GetDataflowEndpointGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.get_dataflow_endpoint_group_response.GetDataflowEndpointGroupResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.get_dataflow_endpoint_group

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.get_dataflow_endpoint_group.get_dataflow_endpoint_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.get_dataflow_endpoint_group_request.GetDataflowEndpointGroupRequest = {}  # type: ignore[typeddict-item]
        input_["dataflow_endpoint_group_id"] = dataflow_endpoint_group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        dataflow_endpoint_group_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse":
        """<p>Deletes a dataflow endpoint group.</p>

        Args:
            dataflow_endpoint_group_id: <p>UUID of a dataflow endpoint group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.delete_dataflow_endpoint_group_request.DeleteDataflowEndpointGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.delete_dataflow_endpoint_group

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.delete_dataflow_endpoint_group.delete_dataflow_endpoint_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.delete_dataflow_endpoint_group_request.DeleteDataflowEndpointGroupRequest = {}  # type: ignore[typeddict-item]
        input_["dataflow_endpoint_group_id"] = dataflow_endpoint_group_id

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
    ) -> "aws_sdk_groundstation.types.list_dataflow_endpoint_groups_response.ListDataflowEndpointGroupsResponse":
        """<p>Returns a list of <code>DataflowEndpoint</code> groups.</p>

        Args:
            max_results: <p>Maximum number of dataflow endpoint groups returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListDataflowEndpointGroups</code> call. Used to get the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.list_dataflow_endpoint_groups_request.ListDataflowEndpointGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.list_dataflow_endpoint_groups_response.ListDataflowEndpointGroupsResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_dataflow_endpoint_groups

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.list_dataflow_endpoint_groups.list_dataflow_endpoint_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_dataflow_endpoint_groups_request.ListDataflowEndpointGroupsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncDataflowEndpointGroup:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def create(
        self,
        endpoint_details: "aws_sdk_groundstation.types.endpoint_details_list.EndpointDetailsList",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        tags: Optional["aws_sdk_groundstation.types.tags_map.TagsMap"] = None,
        contact_pre_pass_duration_seconds: Optional[
            "aws_sdk_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "aws_sdk_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
    ) -> "aws_sdk_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse":
        """<p>Creates a <code>DataflowEndpoint</code> group containing the specified list of <code> DataflowEndpoint</code> objects.</p> <p>The <code>name</code> field in each endpoint is used in your mission profile <code> DataflowEndpointConfig</code> to specify which endpoints to use during a contact.</p> <p>When a contact uses multiple <code>DataflowEndpointConfig</code> objects, each <code> Config</code> must match a <code>DataflowEndpoint</code> in the same group.</p>

        Args:
            endpoint_details: <p>Endpoint details of each endpoint in the dataflow endpoint group. All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix <a href=\"https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AwsGroundStationAgentEndpoint.html\"> AWS Ground Station Agent endpoints</a> with <a href=\"https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html\">Dataflow endpoints</a> in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type. </p>
            tags: <p>Tags of a dataflow endpoint group.</p>
            contact_pre_pass_duration_seconds: <p> Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a <code>PREPASS</code> state. A <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html\">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>PREPASS</code> state. </p>
            contact_post_pass_duration_seconds: <p> Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a <code>POSTPASS</code> state. A <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html\">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>POSTPASS</code> state. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.create_dataflow_endpoint_group_request.CreateDataflowEndpointGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.create_dataflow_endpoint_group

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.create_dataflow_endpoint_group.async_create_dataflow_endpoint_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.create_dataflow_endpoint_group_request.CreateDataflowEndpointGroupRequest = {}  # type: ignore[typeddict-item]
        input_["endpoint_details"] = endpoint_details
        if tags is not None:
            input_["tags"] = tags
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        dataflow_endpoint_group_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.get_dataflow_endpoint_group_response.GetDataflowEndpointGroupResponse":
        """<p>Returns the dataflow endpoint group.</p>

        Args:
            dataflow_endpoint_group_id: <p>UUID of a dataflow endpoint group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.get_dataflow_endpoint_group_request.GetDataflowEndpointGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.get_dataflow_endpoint_group_response.GetDataflowEndpointGroupResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.get_dataflow_endpoint_group

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.get_dataflow_endpoint_group.async_get_dataflow_endpoint_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.get_dataflow_endpoint_group_request.GetDataflowEndpointGroupRequest = {}  # type: ignore[typeddict-item]
        input_["dataflow_endpoint_group_id"] = dataflow_endpoint_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        dataflow_endpoint_group_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse":
        """<p>Deletes a dataflow endpoint group.</p>

        Args:
            dataflow_endpoint_group_id: <p>UUID of a dataflow endpoint group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.delete_dataflow_endpoint_group_request.DeleteDataflowEndpointGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.dataflow_endpoint_group_id_response.DataflowEndpointGroupIdResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.delete_dataflow_endpoint_group

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.delete_dataflow_endpoint_group.async_delete_dataflow_endpoint_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.delete_dataflow_endpoint_group_request.DeleteDataflowEndpointGroupRequest = {}  # type: ignore[typeddict-item]
        input_["dataflow_endpoint_group_id"] = dataflow_endpoint_group_id

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
    ) -> "aws_sdk_groundstation.types.list_dataflow_endpoint_groups_response.ListDataflowEndpointGroupsResponse":
        """<p>Returns a list of <code>DataflowEndpoint</code> groups.</p>

        Args:
            max_results: <p>Maximum number of dataflow endpoint groups returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListDataflowEndpointGroups</code> call. Used to get the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_groundstation.types.list_dataflow_endpoint_groups_request.ListDataflowEndpointGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_groundstation.types.list_dataflow_endpoint_groups_response.ListDataflowEndpointGroupsResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_dataflow_endpoint_groups

            (
                output,
                http_response,
            ) = await aws_sdk_groundstation._operations.ground_station.list_dataflow_endpoint_groups.async_list_dataflow_endpoint_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_dataflow_endpoint_groups_request.ListDataflowEndpointGroupsRequest = {}  # type: ignore[typeddict-item]
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
