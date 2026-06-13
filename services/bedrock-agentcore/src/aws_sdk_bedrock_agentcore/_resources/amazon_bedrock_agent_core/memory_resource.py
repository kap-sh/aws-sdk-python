from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import ensure_async_iterator
from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import ensure_sync_iterator
from aws_sdk_bedrock_agentcore._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agentcore._auth._signers
import aws_sdk_bedrock_agentcore._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import BedrockAgentCoreClient, BedrockAgentCoreClientConfig
    from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import AsyncBedrockAgentCoreClient, AsyncBedrockAgentCoreClientConfig
    import aws_sdk_bedrock_agentcore.types.actor_id
    import aws_sdk_bedrock_agentcore.types.actor_summary
    import aws_sdk_bedrock_agentcore.types.batch_create_memory_records_input
    import aws_sdk_bedrock_agentcore.types.batch_create_memory_records_output
    import aws_sdk_bedrock_agentcore.types.batch_delete_memory_records_input
    import aws_sdk_bedrock_agentcore.types.batch_delete_memory_records_output
    import aws_sdk_bedrock_agentcore.types.batch_update_memory_records_input
    import aws_sdk_bedrock_agentcore.types.batch_update_memory_records_output
    import aws_sdk_bedrock_agentcore.types.branch
    import aws_sdk_bedrock_agentcore.types.create_event_input
    import aws_sdk_bedrock_agentcore.types.create_event_output
    import aws_sdk_bedrock_agentcore.types.delete_event_input
    import aws_sdk_bedrock_agentcore.types.delete_event_output
    import aws_sdk_bedrock_agentcore.types.delete_memory_record_input
    import aws_sdk_bedrock_agentcore.types.delete_memory_record_output
    import aws_sdk_bedrock_agentcore.types.event
    import aws_sdk_bedrock_agentcore.types.event_id
    import aws_sdk_bedrock_agentcore.types.extraction_job
    import aws_sdk_bedrock_agentcore.types.extraction_job_filter_input
    import aws_sdk_bedrock_agentcore.types.extraction_job_metadata
    import aws_sdk_bedrock_agentcore.types.filter_input
    import aws_sdk_bedrock_agentcore.types.get_event_input
    import aws_sdk_bedrock_agentcore.types.get_event_output
    import aws_sdk_bedrock_agentcore.types.get_memory_record_input
    import aws_sdk_bedrock_agentcore.types.get_memory_record_output
    import aws_sdk_bedrock_agentcore.types.list_actors_input
    import aws_sdk_bedrock_agentcore.types.list_actors_output
    import aws_sdk_bedrock_agentcore.types.list_events_input
    import aws_sdk_bedrock_agentcore.types.list_events_output
    import aws_sdk_bedrock_agentcore.types.list_memory_extraction_jobs_input
    import aws_sdk_bedrock_agentcore.types.list_memory_extraction_jobs_output
    import aws_sdk_bedrock_agentcore.types.list_memory_records_input
    import aws_sdk_bedrock_agentcore.types.list_memory_records_output
    import aws_sdk_bedrock_agentcore.types.list_sessions_input
    import aws_sdk_bedrock_agentcore.types.list_sessions_output
    import aws_sdk_bedrock_agentcore.types.max_results
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.memory_metadata_filter_list
    import aws_sdk_bedrock_agentcore.types.memory_record_id
    import aws_sdk_bedrock_agentcore.types.memory_record_summary
    import aws_sdk_bedrock_agentcore.types.memory_records_create_input_list
    import aws_sdk_bedrock_agentcore.types.memory_records_delete_input_list
    import aws_sdk_bedrock_agentcore.types.memory_records_update_input_list
    import aws_sdk_bedrock_agentcore.types.memory_strategy_id
    import aws_sdk_bedrock_agentcore.types.metadata_map
    import aws_sdk_bedrock_agentcore.types.namespace
    import aws_sdk_bedrock_agentcore.types.pagination_token
    import aws_sdk_bedrock_agentcore.types.payload_type_list
    import aws_sdk_bedrock_agentcore.types.retrieve_memory_records_input
    import aws_sdk_bedrock_agentcore.types.retrieve_memory_records_output
    import aws_sdk_bedrock_agentcore.types.search_criteria
    import aws_sdk_bedrock_agentcore.types.session_filter
    import aws_sdk_bedrock_agentcore.types.session_id
    import aws_sdk_bedrock_agentcore.types.session_summary
    import aws_sdk_bedrock_agentcore.types.start_memory_extraction_job_input
    import aws_sdk_bedrock_agentcore.types.start_memory_extraction_job_output

class MemoryResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service
    def batch_create_memory_records(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", records: "aws_sdk_bedrock_agentcore.types.memory_records_create_input_list.MemoryRecordsCreateInputList", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, client_token: Optional[str] = None) -> "aws_sdk_bedrock_agentcore.types.batch_create_memory_records_output.BatchCreateMemoryRecordsOutput":
        """<p>Creates multiple memory records in a single batch operation for the specified memory with custom content.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be created.</p>
            records: <p>A list of memory record creation inputs to be processed in the batch operation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the batch request.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.batch_create_memory_records_output.BatchCreateMemoryRecordsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_create_memory_records
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_create_memory_records.batch_create_memory_records(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["records"] = records
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def batch_delete_memory_records(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", records: "aws_sdk_bedrock_agentcore.types.memory_records_delete_input_list.MemoryRecordsDeleteInputList", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.batch_delete_memory_records_output.BatchDeleteMemoryRecordsOutput":
        """<p>Deletes multiple memory records in a single batch operation from the specified memory.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be deleted.</p>
            records: <p>A list of memory record deletion inputs to be processed in the batch operation.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.batch_delete_memory_records_input.BatchDeleteMemoryRecordsInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.batch_delete_memory_records_output.BatchDeleteMemoryRecordsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_delete_memory_records
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_delete_memory_records.batch_delete_memory_records(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.batch_delete_memory_records_input.BatchDeleteMemoryRecordsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["records"] = records

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def batch_update_memory_records(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", records: "aws_sdk_bedrock_agentcore.types.memory_records_update_input_list.MemoryRecordsUpdateInputList", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.batch_update_memory_records_output.BatchUpdateMemoryRecordsOutput":
        """<p>Updates multiple memory records with custom content in a single batch operation within the specified memory.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be updated.</p>
            records: <p>A list of memory record update inputs to be processed in the batch operation.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.batch_update_memory_records_output.BatchUpdateMemoryRecordsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_update_memory_records
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_update_memory_records.batch_update_memory_records(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["records"] = records

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def create_event(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId", event_timestamp: datetime.datetime, payload: "aws_sdk_bedrock_agentcore.types.payload_type_list.PayloadTypeList", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, session_id: Optional["aws_sdk_bedrock_agentcore.types.session_id.SessionId"] = None, branch: Optional["aws_sdk_bedrock_agentcore.types.branch.Branch"] = None, client_token: Optional[str] = None, metadata: Optional["aws_sdk_bedrock_agentcore.types.metadata_map.MetadataMap"] = None) -> "aws_sdk_bedrock_agentcore.types.create_event_output.CreateEventOutput":
        """<p>Creates an event in an AgentCore Memory resource. Events represent interactions or activities that occur within a session and are associated with specific actors.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:CreateEvent</code> permission.</p> <p>This operation is subject to request rate limiting.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource in which to create the event.</p>
            actor_id: <p>The identifier of the actor associated with this event. An actor represents an entity that participates in sessions and generates events.</p>
            session_id: <p>The identifier of the session in which this event occurs. A session represents a sequence of related events.</p>
            event_timestamp: <p>The timestamp when the event occurred. If not specified, the current time is used.</p>
            payload: <p>The content payload of the event. This can include conversational data or binary content.</p>
            branch: <p>The branch information for this event. Branches allow for organizing events into different conversation threads or paths.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>
            metadata: <p>The key-value metadata to attach to the event.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.create_event_input.CreateEventInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.create_event_output.CreateEventOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_event
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_event.create_event(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.create_event_input.CreateEventInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["actor_id"] = actor_id
        if session_id is not None:
            input["session_id"] = session_id
        input["event_timestamp"] = event_timestamp
        input["payload"] = payload
        if branch is not None:
            input["branch"] = branch
        if client_token is not None:
            input["client_token"] = client_token
        if metadata is not None:
            input["metadata"] = metadata

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete_event(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", session_id: "aws_sdk_bedrock_agentcore.types.session_id.SessionId", event_id: "aws_sdk_bedrock_agentcore.types.event_id.EventId", actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.delete_event_output.DeleteEventOutput":
        """<p>Deletes an event from an AgentCore Memory resource. When you delete an event, it is permanently removed.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:DeleteEvent</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to delete the event.</p>
            session_id: <p>The identifier of the session containing the event to delete.</p>
            event_id: <p>The identifier of the event to delete.</p>
            actor_id: <p>The identifier of the actor associated with the event to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.delete_event_input.DeleteEventInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.delete_event_output.DeleteEventOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_event
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_event.delete_event(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.delete_event_input.DeleteEventInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["session_id"] = session_id
        input["event_id"] = event_id
        input["actor_id"] = actor_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete_memory_record(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", memory_record_id: "aws_sdk_bedrock_agentcore.types.memory_record_id.MemoryRecordId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.delete_memory_record_output.DeleteMemoryRecordOutput":
        """<p>Deletes a memory record from an AgentCore Memory resource. When you delete a memory record, it is permanently removed.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:DeleteMemoryRecord</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to delete the memory record.</p>
            memory_record_id: <p>The identifier of the memory record to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.delete_memory_record_input.DeleteMemoryRecordInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.delete_memory_record_output.DeleteMemoryRecordOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_memory_record
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_memory_record.delete_memory_record(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.delete_memory_record_input.DeleteMemoryRecordInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["memory_record_id"] = memory_record_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_event(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", session_id: "aws_sdk_bedrock_agentcore.types.session_id.SessionId", actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId", event_id: "aws_sdk_bedrock_agentcore.types.event_id.EventId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_event_output.GetEventOutput":
        """<p>Retrieves information about a specific event in an AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:GetEvent</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource containing the event.</p>
            session_id: <p>The identifier of the session containing the event.</p>
            actor_id: <p>The identifier of the actor associated with the event.</p>
            event_id: <p>The identifier of the event to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.get_event_input.GetEventInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.get_event_output.GetEventOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_event
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_event.get_event(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_event_input.GetEventInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["session_id"] = session_id
        input["actor_id"] = actor_id
        input["event_id"] = event_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_memory_record(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", memory_record_id: "aws_sdk_bedrock_agentcore.types.memory_record_id.MemoryRecordId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput":
        """<p>Retrieves a specific memory record from an AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:GetMemoryRecord</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource containing the memory record.</p>
            memory_record_id: <p>The identifier of the memory record to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.get_memory_record_input.GetMemoryRecordInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_memory_record
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_memory_record.get_memory_record(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_memory_record_input.GetMemoryRecordInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["memory_record_id"] = memory_record_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_actors(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_bedrock_agentcore.types.list_actors_output.ListActorsOutput":
        """<p>Lists all actors in an AgentCore Memory resource. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListActors</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list actors.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_actors_input.ListActorsInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_actors_output.ListActorsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_actors
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_actors.list_actors(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_actors_input.ListActorsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_events(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", session_id: "aws_sdk_bedrock_agentcore.types.session_id.SessionId", actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, include_payloads: Optional[bool] = None, filter: Optional["aws_sdk_bedrock_agentcore.types.filter_input.FilterInput"] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_bedrock_agentcore.types.list_events_output.ListEventsOutput":
        """<p>Lists events in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListEvents</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list events.</p>
            session_id: <p>The identifier of the session for which to list events.</p>
            actor_id: <p>The identifier of the actor for which to list events.</p>
            include_payloads: <p>Specifies whether to include event payloads in the response. Set to true to include payloads, or false to exclude them.</p>
            filter: <p>Filter criteria to apply when listing events.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_events_input.ListEventsInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_events_output.ListEventsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_events
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_events.list_events(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_events_input.ListEventsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["session_id"] = session_id
        input["actor_id"] = actor_id
        if include_payloads is not None:
            input["include_payloads"] = include_payloads
        if filter is not None:
            input["filter"] = filter
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_memory_extraction_jobs(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, max_results: Optional[int] = None, filter: Optional["aws_sdk_bedrock_agentcore.types.extraction_job_filter_input.ExtractionJobFilterInput"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_bedrock_agentcore.types.list_memory_extraction_jobs_output.ListMemoryExtractionJobsOutput":
        """<p>Lists all long-term memory extraction jobs that are eligible to be started with optional filtering.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListMemoryExtractionJobs</code> permission.</p>

        Args:
            memory_id: <p>The unique identifier of the memory to list extraction jobs for.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            filter: <p>Filter criteria to apply when listing extraction jobs.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_memory_extraction_jobs_input.ListMemoryExtractionJobsInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_memory_extraction_jobs_output.ListMemoryExtractionJobsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_extraction_jobs
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_extraction_jobs.list_memory_extraction_jobs(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_memory_extraction_jobs_input.ListMemoryExtractionJobsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        if max_results is not None:
            input["max_results"] = max_results
        if filter is not None:
            input["filter"] = filter
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_memory_records(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, namespace: Optional["aws_sdk_bedrock_agentcore.types.namespace.Namespace"] = None, namespace_path: Optional["aws_sdk_bedrock_agentcore.types.namespace.Namespace"] = None, memory_strategy_id: Optional["aws_sdk_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None, metadata_filters: Optional["aws_sdk_bedrock_agentcore.types.memory_metadata_filter_list.MemoryMetadataFilterList"] = None) -> "aws_sdk_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput":
        """<p>Lists memory records in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListMemoryRecords</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list memory records.</p>
            namespace: <p>The namespace prefix to filter memory records by. Returns all memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            namespace_path: <p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            memory_strategy_id: <p>The memory strategy identifier to filter memory records by. If specified, only memory records with this strategy ID are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            metadata_filters: <p>A list of metadata filter expressions to scope the returned memory records.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_memory_records_input.ListMemoryRecordsInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_records
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_records.list_memory_records(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_memory_records_input.ListMemoryRecordsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        if namespace is not None:
            input["namespace"] = namespace
        if namespace_path is not None:
            input["namespace_path"] = namespace_path
        if memory_strategy_id is not None:
            input["memory_strategy_id"] = memory_strategy_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if metadata_filters is not None:
            input["metadata_filters"] = metadata_filters

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_sessions(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None, filter: Optional["aws_sdk_bedrock_agentcore.types.session_filter.SessionFilter"] = None) -> "aws_sdk_bedrock_agentcore.types.list_sessions_output.ListSessionsOutput":
        """<p>Lists sessions in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>Empty sessions are automatically deleted after one day.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListSessions</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list sessions.</p>
            actor_id: <p>The identifier of the actor for which to list sessions. </p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filter: <p>Filter criteria to apply when listing sessions.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.list_sessions_input.ListSessionsInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.list_sessions_output.ListSessionsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_sessions
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_sessions.list_sessions(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_sessions_input.ListSessionsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["actor_id"] = actor_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filter is not None:
            input["filter"] = filter

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def retrieve_memory_records(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", search_criteria: "aws_sdk_bedrock_agentcore.types.search_criteria.SearchCriteria", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, namespace: Optional["aws_sdk_bedrock_agentcore.types.namespace.Namespace"] = None, namespace_path: Optional["aws_sdk_bedrock_agentcore.types.namespace.Namespace"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None) -> "aws_sdk_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput":
        """<p>Searches for and retrieves memory records from an AgentCore Memory resource based on specified search criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:RetrieveMemoryRecords</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to retrieve memory records.</p>
            namespace: <p>The namespace prefix to filter memory records by. Searches for memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            namespace_path: <p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            search_criteria: <p>The search criteria to use for finding relevant memory records. This includes the search query, memory strategy ID, and other search parameters.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.retrieve_memory_records
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.retrieve_memory_records.retrieve_memory_records(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        if namespace is not None:
            input["namespace"] = namespace
        if namespace_path is not None:
            input["namespace_path"] = namespace_path
        input["search_criteria"] = search_criteria
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def start_memory_extraction_job(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", extraction_job: "aws_sdk_bedrock_agentcore.types.extraction_job.ExtractionJob", *, config_overrides: Optional[BedrockAgentCoreClientConfig] = None, client_token: Optional[str] = None) -> "aws_sdk_bedrock_agentcore.types.start_memory_extraction_job_output.StartMemoryExtractionJobOutput":
        """<p> Starts a memory extraction job that processes events that failed extraction previously in an AgentCore Memory resource and produces structured memory records. When earlier extraction attempts have left events unprocessed, this job will pick up and extract those as well. </p> <p>To use this operation, you must have the <code>bedrock-agentcore:StartMemoryExtractionJob</code> permission.</p>

        Args:
            memory_id: <p>The unique identifier of the memory for which to start extraction jobs.</p>
            extraction_job: <p>Extraction job to start in this operation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the request.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agentcore.types.start_memory_extraction_job_input.StartMemoryExtractionJobInput]') -> OperationResponse["aws_sdk_bedrock_agentcore.types.start_memory_extraction_job_output.StartMemoryExtractionJobOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_memory_extraction_job
            output, http_response = aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_memory_extraction_job.start_memory_extraction_job(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.start_memory_extraction_job_input.StartMemoryExtractionJobInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["extraction_job"] = extraction_job
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncMemoryResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service
    async def batch_create_memory_records(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", records: "aws_sdk_bedrock_agentcore.types.memory_records_create_input_list.MemoryRecordsCreateInputList", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, client_token: Optional[str] = None) -> "aws_sdk_bedrock_agentcore.types.batch_create_memory_records_output.BatchCreateMemoryRecordsOutput":
        """<p>Creates multiple memory records in a single batch operation for the specified memory with custom content.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be created.</p>
            records: <p>A list of memory record creation inputs to be processed in the batch operation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the batch request.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.batch_create_memory_records_output.BatchCreateMemoryRecordsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_create_memory_records
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_create_memory_records.async_batch_create_memory_records(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["records"] = records
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def batch_delete_memory_records(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", records: "aws_sdk_bedrock_agentcore.types.memory_records_delete_input_list.MemoryRecordsDeleteInputList", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.batch_delete_memory_records_output.BatchDeleteMemoryRecordsOutput":
        """<p>Deletes multiple memory records in a single batch operation from the specified memory.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be deleted.</p>
            records: <p>A list of memory record deletion inputs to be processed in the batch operation.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.batch_delete_memory_records_input.BatchDeleteMemoryRecordsInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.batch_delete_memory_records_output.BatchDeleteMemoryRecordsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_delete_memory_records
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_delete_memory_records.async_batch_delete_memory_records(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.batch_delete_memory_records_input.BatchDeleteMemoryRecordsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["records"] = records

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def batch_update_memory_records(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", records: "aws_sdk_bedrock_agentcore.types.memory_records_update_input_list.MemoryRecordsUpdateInputList", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.batch_update_memory_records_output.BatchUpdateMemoryRecordsOutput":
        """<p>Updates multiple memory records with custom content in a single batch operation within the specified memory.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be updated.</p>
            records: <p>A list of memory record update inputs to be processed in the batch operation.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.batch_update_memory_records_output.BatchUpdateMemoryRecordsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_update_memory_records
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_update_memory_records.async_batch_update_memory_records(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["records"] = records

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def create_event(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId", event_timestamp: datetime.datetime, payload: "aws_sdk_bedrock_agentcore.types.payload_type_list.PayloadTypeList", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, session_id: Optional["aws_sdk_bedrock_agentcore.types.session_id.SessionId"] = None, branch: Optional["aws_sdk_bedrock_agentcore.types.branch.Branch"] = None, client_token: Optional[str] = None, metadata: Optional["aws_sdk_bedrock_agentcore.types.metadata_map.MetadataMap"] = None) -> "aws_sdk_bedrock_agentcore.types.create_event_output.CreateEventOutput":
        """<p>Creates an event in an AgentCore Memory resource. Events represent interactions or activities that occur within a session and are associated with specific actors.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:CreateEvent</code> permission.</p> <p>This operation is subject to request rate limiting.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource in which to create the event.</p>
            actor_id: <p>The identifier of the actor associated with this event. An actor represents an entity that participates in sessions and generates events.</p>
            session_id: <p>The identifier of the session in which this event occurs. A session represents a sequence of related events.</p>
            event_timestamp: <p>The timestamp when the event occurred. If not specified, the current time is used.</p>
            payload: <p>The content payload of the event. This can include conversational data or binary content.</p>
            branch: <p>The branch information for this event. Branches allow for organizing events into different conversation threads or paths.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>
            metadata: <p>The key-value metadata to attach to the event.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.create_event_input.CreateEventInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.create_event_output.CreateEventOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_event
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_event.async_create_event(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.create_event_input.CreateEventInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["actor_id"] = actor_id
        if session_id is not None:
            input["session_id"] = session_id
        input["event_timestamp"] = event_timestamp
        input["payload"] = payload
        if branch is not None:
            input["branch"] = branch
        if client_token is not None:
            input["client_token"] = client_token
        if metadata is not None:
            input["metadata"] = metadata

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete_event(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", session_id: "aws_sdk_bedrock_agentcore.types.session_id.SessionId", event_id: "aws_sdk_bedrock_agentcore.types.event_id.EventId", actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.delete_event_output.DeleteEventOutput":
        """<p>Deletes an event from an AgentCore Memory resource. When you delete an event, it is permanently removed.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:DeleteEvent</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to delete the event.</p>
            session_id: <p>The identifier of the session containing the event to delete.</p>
            event_id: <p>The identifier of the event to delete.</p>
            actor_id: <p>The identifier of the actor associated with the event to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.delete_event_input.DeleteEventInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.delete_event_output.DeleteEventOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_event
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_event.async_delete_event(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.delete_event_input.DeleteEventInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["session_id"] = session_id
        input["event_id"] = event_id
        input["actor_id"] = actor_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete_memory_record(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", memory_record_id: "aws_sdk_bedrock_agentcore.types.memory_record_id.MemoryRecordId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.delete_memory_record_output.DeleteMemoryRecordOutput":
        """<p>Deletes a memory record from an AgentCore Memory resource. When you delete a memory record, it is permanently removed.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:DeleteMemoryRecord</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to delete the memory record.</p>
            memory_record_id: <p>The identifier of the memory record to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.delete_memory_record_input.DeleteMemoryRecordInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.delete_memory_record_output.DeleteMemoryRecordOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_memory_record
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_memory_record.async_delete_memory_record(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.delete_memory_record_input.DeleteMemoryRecordInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["memory_record_id"] = memory_record_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_event(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", session_id: "aws_sdk_bedrock_agentcore.types.session_id.SessionId", actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId", event_id: "aws_sdk_bedrock_agentcore.types.event_id.EventId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_event_output.GetEventOutput":
        """<p>Retrieves information about a specific event in an AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:GetEvent</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource containing the event.</p>
            session_id: <p>The identifier of the session containing the event.</p>
            actor_id: <p>The identifier of the actor associated with the event.</p>
            event_id: <p>The identifier of the event to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_event_input.GetEventInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.get_event_output.GetEventOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_event
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_event.async_get_event(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_event_input.GetEventInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["session_id"] = session_id
        input["actor_id"] = actor_id
        input["event_id"] = event_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_memory_record(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", memory_record_id: "aws_sdk_bedrock_agentcore.types.memory_record_id.MemoryRecordId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None) -> "aws_sdk_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput":
        """<p>Retrieves a specific memory record from an AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:GetMemoryRecord</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource containing the memory record.</p>
            memory_record_id: <p>The identifier of the memory record to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_memory_record_input.GetMemoryRecordInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_memory_record
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_memory_record.async_get_memory_record(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.get_memory_record_input.GetMemoryRecordInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["memory_record_id"] = memory_record_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_actors(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_bedrock_agentcore.types.list_actors_output.ListActorsOutput":
        """<p>Lists all actors in an AgentCore Memory resource. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListActors</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list actors.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_actors_input.ListActorsInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_actors_output.ListActorsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_actors
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_actors.async_list_actors(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_actors_input.ListActorsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_events(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", session_id: "aws_sdk_bedrock_agentcore.types.session_id.SessionId", actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, include_payloads: Optional[bool] = None, filter: Optional["aws_sdk_bedrock_agentcore.types.filter_input.FilterInput"] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_bedrock_agentcore.types.list_events_output.ListEventsOutput":
        """<p>Lists events in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListEvents</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list events.</p>
            session_id: <p>The identifier of the session for which to list events.</p>
            actor_id: <p>The identifier of the actor for which to list events.</p>
            include_payloads: <p>Specifies whether to include event payloads in the response. Set to true to include payloads, or false to exclude them.</p>
            filter: <p>Filter criteria to apply when listing events.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_events_input.ListEventsInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_events_output.ListEventsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_events
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_events.async_list_events(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_events_input.ListEventsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["session_id"] = session_id
        input["actor_id"] = actor_id
        if include_payloads is not None:
            input["include_payloads"] = include_payloads
        if filter is not None:
            input["filter"] = filter
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_memory_extraction_jobs(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, max_results: Optional[int] = None, filter: Optional["aws_sdk_bedrock_agentcore.types.extraction_job_filter_input.ExtractionJobFilterInput"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None) -> "aws_sdk_bedrock_agentcore.types.list_memory_extraction_jobs_output.ListMemoryExtractionJobsOutput":
        """<p>Lists all long-term memory extraction jobs that are eligible to be started with optional filtering.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListMemoryExtractionJobs</code> permission.</p>

        Args:
            memory_id: <p>The unique identifier of the memory to list extraction jobs for.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            filter: <p>Filter criteria to apply when listing extraction jobs.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_memory_extraction_jobs_input.ListMemoryExtractionJobsInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_memory_extraction_jobs_output.ListMemoryExtractionJobsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_extraction_jobs
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_extraction_jobs.async_list_memory_extraction_jobs(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_memory_extraction_jobs_input.ListMemoryExtractionJobsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        if max_results is not None:
            input["max_results"] = max_results
        if filter is not None:
            input["filter"] = filter
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_memory_records(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, namespace: Optional["aws_sdk_bedrock_agentcore.types.namespace.Namespace"] = None, namespace_path: Optional["aws_sdk_bedrock_agentcore.types.namespace.Namespace"] = None, memory_strategy_id: Optional["aws_sdk_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None, metadata_filters: Optional["aws_sdk_bedrock_agentcore.types.memory_metadata_filter_list.MemoryMetadataFilterList"] = None) -> "aws_sdk_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput":
        """<p>Lists memory records in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListMemoryRecords</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list memory records.</p>
            namespace: <p>The namespace prefix to filter memory records by. Returns all memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            namespace_path: <p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            memory_strategy_id: <p>The memory strategy identifier to filter memory records by. If specified, only memory records with this strategy ID are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            metadata_filters: <p>A list of metadata filter expressions to scope the returned memory records.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_memory_records_input.ListMemoryRecordsInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_records
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_records.async_list_memory_records(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_memory_records_input.ListMemoryRecordsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        if namespace is not None:
            input["namespace"] = namespace
        if namespace_path is not None:
            input["namespace_path"] = namespace_path
        if memory_strategy_id is not None:
            input["memory_strategy_id"] = memory_strategy_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if metadata_filters is not None:
            input["metadata_filters"] = metadata_filters

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_sessions(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", actor_id: "aws_sdk_bedrock_agentcore.types.actor_id.ActorId", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None, filter: Optional["aws_sdk_bedrock_agentcore.types.session_filter.SessionFilter"] = None) -> "aws_sdk_bedrock_agentcore.types.list_sessions_output.ListSessionsOutput":
        """<p>Lists sessions in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>Empty sessions are automatically deleted after one day.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListSessions</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list sessions.</p>
            actor_id: <p>The identifier of the actor for which to list sessions. </p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filter: <p>Filter criteria to apply when listing sessions.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.list_sessions_input.ListSessionsInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.list_sessions_output.ListSessionsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_sessions
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_sessions.async_list_sessions(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.list_sessions_input.ListSessionsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["actor_id"] = actor_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filter is not None:
            input["filter"] = filter

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def retrieve_memory_records(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", search_criteria: "aws_sdk_bedrock_agentcore.types.search_criteria.SearchCriteria", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, namespace: Optional["aws_sdk_bedrock_agentcore.types.namespace.Namespace"] = None, namespace_path: Optional["aws_sdk_bedrock_agentcore.types.namespace.Namespace"] = None, next_token: Optional["aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"] = None, max_results: Optional["aws_sdk_bedrock_agentcore.types.max_results.MaxResults"] = None) -> "aws_sdk_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput":
        """<p>Searches for and retrieves memory records from an AgentCore Memory resource based on specified search criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:RetrieveMemoryRecords</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to retrieve memory records.</p>
            namespace: <p>The namespace prefix to filter memory records by. Searches for memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            namespace_path: <p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            search_criteria: <p>The search criteria to use for finding relevant memory records. This includes the search query, memory strategy ID, and other search parameters.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.retrieve_memory_records
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.retrieve_memory_records.async_retrieve_memory_records(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        if namespace is not None:
            input["namespace"] = namespace
        if namespace_path is not None:
            input["namespace_path"] = namespace_path
        input["search_criteria"] = search_criteria
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def start_memory_extraction_job(self, memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId", extraction_job: "aws_sdk_bedrock_agentcore.types.extraction_job.ExtractionJob", *, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None, client_token: Optional[str] = None) -> "aws_sdk_bedrock_agentcore.types.start_memory_extraction_job_output.StartMemoryExtractionJobOutput":
        """<p> Starts a memory extraction job that processes events that failed extraction previously in an AgentCore Memory resource and produces structured memory records. When earlier extraction attempts have left events unprocessed, this job will pick up and extract those as well. </p> <p>To use this operation, you must have the <code>bedrock-agentcore:StartMemoryExtractionJob</code> permission.</p>

        Args:
            memory_id: <p>The unique identifier of the memory for which to start extraction jobs.</p>
            extraction_job: <p>Extraction job to start in this operation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the request.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.start_memory_extraction_job_input.StartMemoryExtractionJobInput]') -> AsyncOperationResponse["aws_sdk_bedrock_agentcore.types.start_memory_extraction_job_output.StartMemoryExtractionJobOutput"]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_memory_extraction_job
            output, http_response = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_memory_extraction_job.async_start_memory_extraction_job(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agentcore.types.start_memory_extraction_job_input.StartMemoryExtractionJobInput = {}  # type: ignore[typeddict-item]
        input["memory_id"] = memory_id
        input["extraction_job"] = extraction_job
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output