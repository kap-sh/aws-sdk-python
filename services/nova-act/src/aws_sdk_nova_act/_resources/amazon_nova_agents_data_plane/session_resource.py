from typing import TYPE_CHECKING, Optional

import aws_sdk_nova_act._auth._signers
import aws_sdk_nova_act._auth._sigv4
from aws_sdk_nova_act._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.client_token
    import aws_sdk_nova_act.types.create_session_request
    import aws_sdk_nova_act.types.create_session_response
    import aws_sdk_nova_act.types.list_sessions_request
    import aws_sdk_nova_act.types.list_sessions_response
    import aws_sdk_nova_act.types.max_results
    import aws_sdk_nova_act.types.next_token
    import aws_sdk_nova_act.types.session_summary
    import aws_sdk_nova_act.types.sort_order
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_definition_name
    from aws_sdk_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
        AsyncNovaActClientConfig,
    )
    from aws_sdk_nova_act._services.nova_act import NovaActClient, NovaActClientConfig


class SessionResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service

    def create(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        client_token: Optional[
            "aws_sdk_nova_act.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_nova_act.types.create_session_response.CreateSessionResponse":
        """<p>Creates a new session context within a workflow run to manage conversation state and acts.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to create the session in.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.create_session_request.CreateSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.create_session_response.CreateSessionResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_session

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_session.create_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.create_session_request.CreateSessionRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["workflow_run_id"] = workflow_run_id
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["aws_sdk_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["aws_sdk_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_nova_act.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists all sessions within a specific workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to list sessions for.</p>
            max_results: <p>The maximum number of sessions to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned sessions (ascending or descending).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.list_sessions_response.ListSessionsResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_sessions

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.list_sessions_request.ListSessionsRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["workflow_run_id"] = workflow_run_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSessionResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service

    async def create(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        client_token: Optional[
            "aws_sdk_nova_act.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_nova_act.types.create_session_response.CreateSessionResponse":
        """<p>Creates a new session context within a workflow run to manage conversation state and acts.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to create the session in.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.create_session_request.CreateSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.create_session_response.CreateSessionResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_session

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_session.async_create_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.create_session_request.CreateSessionRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["workflow_run_id"] = workflow_run_id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        max_results: Optional["aws_sdk_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["aws_sdk_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_nova_act.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists all sessions within a specific workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to list sessions for.</p>
            max_results: <p>The maximum number of sessions to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned sessions (ascending or descending).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.list_sessions_response.ListSessionsResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_sessions

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_nova_act.types.list_sessions_request.ListSessionsRequest = {}  # type: ignore[typeddict-item]
        input["workflow_definition_name"] = workflow_definition_name
        input["workflow_run_id"] = workflow_run_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if sort_order is not None:
            input["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
