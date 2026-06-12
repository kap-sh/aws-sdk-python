from typing import Optional, TYPE_CHECKING
from aws_sdk_timestream_influxdb._services.async_timestream_influx_db import ensure_async_iterator
from aws_sdk_timestream_influxdb._services.timestream_influx_db import ensure_sync_iterator
from aws_sdk_timestream_influxdb._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
if TYPE_CHECKING:
    from aws_sdk_timestream_influxdb._services.timestream_influx_db import TimestreamInfluxDBClient, TimestreamInfluxDBClientConfig
    from aws_sdk_timestream_influxdb._services.async_timestream_influx_db import AsyncTimestreamInfluxDBClient, AsyncTimestreamInfluxDBClientConfig
    import aws_sdk_timestream_influxdb.types.create_db_parameter_group_input
    import aws_sdk_timestream_influxdb.types.create_db_parameter_group_output
    import aws_sdk_timestream_influxdb.types.db_parameter_group_identifier
    import aws_sdk_timestream_influxdb.types.db_parameter_group_name
    import aws_sdk_timestream_influxdb.types.db_parameter_group_summary
    import aws_sdk_timestream_influxdb.types.get_db_parameter_group_input
    import aws_sdk_timestream_influxdb.types.get_db_parameter_group_output
    import aws_sdk_timestream_influxdb.types.list_db_parameter_groups_input
    import aws_sdk_timestream_influxdb.types.list_db_parameter_groups_output
    import aws_sdk_timestream_influxdb.types.max_results
    import aws_sdk_timestream_influxdb.types.next_token
    import aws_sdk_timestream_influxdb.types.parameters
    import aws_sdk_timestream_influxdb.types.request_tag_map

class DbParameterGroupResource:
    def __init__(self, service: TimestreamInfluxDBClient) -> None:
        self._service = service
    def create(self, name: "aws_sdk_timestream_influxdb.types.db_parameter_group_name.DbParameterGroupName", *, config_overrides: Optional[TimestreamInfluxDBClientConfig] = None, description: Optional[str] = None, parameters: Optional["aws_sdk_timestream_influxdb.types.parameters.Parameters"] = None, tags: Optional["aws_sdk_timestream_influxdb.types.request_tag_map.RequestTagMap"] = None) -> "aws_sdk_timestream_influxdb.types.create_db_parameter_group_output.CreateDbParameterGroupOutput":
        """<p>Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.</p>

        Args:
            name: <p>The name of the DB parameter group. The name must be unique per customer and per region.</p>
            description: <p>A description of the DB parameter group.</p>
            parameters: <p>A list of the parameters that comprise the DB parameter group.</p>
            tags: <p>A list of key-value pairs to associate with the DB parameter group.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_timestream_influxdb.types.create_db_parameter_group_input.CreateDbParameterGroupInput]') -> OperationResponse["aws_sdk_timestream_influxdb.types.create_db_parameter_group_output.CreateDbParameterGroupOutput"]:
            import aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_parameter_group
            output, http_response = aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_parameter_group.create_db_parameter_group(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_timestream_influxdb.types.create_db_parameter_group_input.CreateDbParameterGroupInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if parameters is not None:
            input["parameters"] = parameters
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, identifier: "aws_sdk_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier", *, config_overrides: Optional[TimestreamInfluxDBClientConfig] = None) -> "aws_sdk_timestream_influxdb.types.get_db_parameter_group_output.GetDbParameterGroupOutput":
        """<p>Returns a Timestream for InfluxDB DB parameter group.</p>

        Args:
            identifier: <p>The id of the DB parameter group.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_timestream_influxdb.types.get_db_parameter_group_input.GetDbParameterGroupInput]') -> OperationResponse["aws_sdk_timestream_influxdb.types.get_db_parameter_group_output.GetDbParameterGroupOutput"]:
            import aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_parameter_group
            output, http_response = aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_parameter_group.get_db_parameter_group(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_timestream_influxdb.types.get_db_parameter_group_input.GetDbParameterGroupInput = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[TimestreamInfluxDBClientConfig] = None, next_token: Optional["aws_sdk_timestream_influxdb.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_timestream_influxdb.types.max_results.MaxResults"] = None) -> "aws_sdk_timestream_influxdb.types.list_db_parameter_groups_output.ListDbParameterGroupsOutput":
        """<p>Returns a list of Timestream for InfluxDB DB parameter groups.</p>

        Args:
            next_token: <p>The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_timestream_influxdb.types.list_db_parameter_groups_input.ListDbParameterGroupsInput]') -> OperationResponse["aws_sdk_timestream_influxdb.types.list_db_parameter_groups_output.ListDbParameterGroupsOutput"]:
            import aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_parameter_groups
            output, http_response = aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_parameter_groups.list_db_parameter_groups(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_timestream_influxdb.types.list_db_parameter_groups_input.ListDbParameterGroupsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncDbParameterGroupResource:
    def __init__(self, service: AsyncTimestreamInfluxDBClient) -> None:
        self._service = service
    async def create(self, name: "aws_sdk_timestream_influxdb.types.db_parameter_group_name.DbParameterGroupName", *, config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None, description: Optional[str] = None, parameters: Optional["aws_sdk_timestream_influxdb.types.parameters.Parameters"] = None, tags: Optional["aws_sdk_timestream_influxdb.types.request_tag_map.RequestTagMap"] = None) -> "aws_sdk_timestream_influxdb.types.create_db_parameter_group_output.CreateDbParameterGroupOutput":
        """<p>Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.</p>

        Args:
            name: <p>The name of the DB parameter group. The name must be unique per customer and per region.</p>
            description: <p>A description of the DB parameter group.</p>
            parameters: <p>A list of the parameters that comprise the DB parameter group.</p>
            tags: <p>A list of key-value pairs to associate with the DB parameter group.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_timestream_influxdb.types.create_db_parameter_group_input.CreateDbParameterGroupInput]') -> AsyncOperationResponse["aws_sdk_timestream_influxdb.types.create_db_parameter_group_output.CreateDbParameterGroupOutput"]:
            import aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_parameter_group
            output, http_response = await aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.create_db_parameter_group.async_create_db_parameter_group(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_timestream_influxdb.types.create_db_parameter_group_input.CreateDbParameterGroupInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if parameters is not None:
            input["parameters"] = parameters
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, identifier: "aws_sdk_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier", *, config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None) -> "aws_sdk_timestream_influxdb.types.get_db_parameter_group_output.GetDbParameterGroupOutput":
        """<p>Returns a Timestream for InfluxDB DB parameter group.</p>

        Args:
            identifier: <p>The id of the DB parameter group.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_timestream_influxdb.types.get_db_parameter_group_input.GetDbParameterGroupInput]') -> AsyncOperationResponse["aws_sdk_timestream_influxdb.types.get_db_parameter_group_output.GetDbParameterGroupOutput"]:
            import aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_parameter_group
            output, http_response = await aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.get_db_parameter_group.async_get_db_parameter_group(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_timestream_influxdb.types.get_db_parameter_group_input.GetDbParameterGroupInput = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncTimestreamInfluxDBClientConfig] = None, next_token: Optional["aws_sdk_timestream_influxdb.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_timestream_influxdb.types.max_results.MaxResults"] = None) -> "aws_sdk_timestream_influxdb.types.list_db_parameter_groups_output.ListDbParameterGroupsOutput":
        """<p>Returns a list of Timestream for InfluxDB DB parameter groups.</p>

        Args:
            next_token: <p>The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
            max_results: <p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_timestream_influxdb.types.list_db_parameter_groups_input.ListDbParameterGroupsInput]') -> AsyncOperationResponse["aws_sdk_timestream_influxdb.types.list_db_parameter_groups_output.ListDbParameterGroupsOutput"]:
            import aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_parameter_groups
            output, http_response = await aws_sdk_timestream_influxdb._operations.amazon_timestream_influx_db.list_db_parameter_groups.async_list_db_parameter_groups(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_timestream_influxdb.types.list_db_parameter_groups_input.ListDbParameterGroupsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output