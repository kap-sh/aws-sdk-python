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
    import aws_sdk_nova_act.types.act_error
    import aws_sdk_nova_act.types.act_status
    import aws_sdk_nova_act.types.act_summary
    import aws_sdk_nova_act.types.call_results
    import aws_sdk_nova_act.types.client_token
    import aws_sdk_nova_act.types.create_act_request
    import aws_sdk_nova_act.types.create_act_response
    import aws_sdk_nova_act.types.invoke_act_step_request
    import aws_sdk_nova_act.types.invoke_act_step_response
    import aws_sdk_nova_act.types.list_acts_request
    import aws_sdk_nova_act.types.list_acts_response
    import aws_sdk_nova_act.types.max_results
    import aws_sdk_nova_act.types.next_token
    import aws_sdk_nova_act.types.sort_order
    import aws_sdk_nova_act.types.task
    import aws_sdk_nova_act.types.tool_specs
    import aws_sdk_nova_act.types.update_act_request
    import aws_sdk_nova_act.types.update_act_response
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_definition_name
    from aws_sdk_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
        AsyncNovaActClientConfig,
    )
    from aws_sdk_nova_act._services.nova_act import NovaActClient, NovaActClientConfig


class ActResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service

    def create(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        session_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        task: "aws_sdk_nova_act.types.task.Task",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        tool_specs: Optional["aws_sdk_nova_act.types.tool_specs.ToolSpecs"] = None,
        client_token: Optional[
            "aws_sdk_nova_act.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_nova_act.types.create_act_response.CreateActResponse":
        """<p>Creates a new AI task (act) within a session that can interact with tools and perform specific actions.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the session.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the session.</p>
            session_id: <p>The unique identifier of the session to create the act in.</p>
            task: <p>The task description that defines what the act should accomplish.</p>
            tool_specs: <p>A list of tool specifications that the act can invoke to complete its task.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.create_act_request.CreateActRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.create_act_response.CreateActResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_act

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_act.create_act(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.create_act_request.CreateActRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name
        input_["workflow_run_id"] = workflow_run_id
        input_["session_id"] = session_id
        input_["task"] = task
        if tool_specs is not None:
            input_["tool_specs"] = tool_specs
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        workflow_run_id: Optional[
            "aws_sdk_nova_act.types.uuid_string.UuidString"
        ] = None,
        session_id: Optional["aws_sdk_nova_act.types.uuid_string.UuidString"] = None,
        max_results: Optional["aws_sdk_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["aws_sdk_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_nova_act.types.list_acts_response.ListActsResponse":
        """<p>Lists all acts within a specific session with their current status and execution details.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the session.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the session.</p>
            session_id: <p>The unique identifier of the session to list acts for.</p>
            max_results: <p>The maximum number of acts to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned acts (ascending or descending).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.list_acts_request.ListActsRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.list_acts_response.ListActsResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_acts

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_acts.list_acts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.list_acts_request.ListActsRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name
        if workflow_run_id is not None:
            input_["workflow_run_id"] = workflow_run_id
        if session_id is not None:
            input_["session_id"] = session_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def invoke_act_step(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        session_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        act_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        call_results: "aws_sdk_nova_act.types.call_results.CallResults",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        previous_step_id: Optional[
            "aws_sdk_nova_act.types.uuid_string.UuidString"
        ] = None,
    ) -> "aws_sdk_nova_act.types.invoke_act_step_response.InvokeActStepResponse":
        """<p>Executes the next step of an act, processing tool call results and returning new tool calls if needed.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the act.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the act.</p>
            session_id: <p>The unique identifier of the session containing the act.</p>
            act_id: <p>The unique identifier of the act to invoke the next step for.</p>
            call_results: <p>The results from previous tool calls that the act requested.</p>
            previous_step_id: <p>The identifier of the previous step, used for tracking execution flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.invoke_act_step_request.InvokeActStepRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.invoke_act_step_response.InvokeActStepResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.invoke_act_step

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.invoke_act_step.invoke_act_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.invoke_act_step_request.InvokeActStepRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name
        input_["workflow_run_id"] = workflow_run_id
        input_["session_id"] = session_id
        input_["act_id"] = act_id
        input_["call_results"] = call_results
        if previous_step_id is not None:
            input_["previous_step_id"] = previous_step_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_act(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        session_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        act_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        status: "aws_sdk_nova_act.types.act_status.ActStatus",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        error: Optional["aws_sdk_nova_act.types.act_error.ActError"] = None,
    ) -> "aws_sdk_nova_act.types.update_act_response.UpdateActResponse":
        """<p>Updates an existing act's configuration, status, or error information.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the act.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the act.</p>
            session_id: <p>The unique identifier of the session containing the act.</p>
            act_id: <p>The unique identifier of the act to update.</p>
            status: <p>The new status to set for the act.</p>
            error: <p>Error information to associate with the act, if applicable.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.update_act_request.UpdateActRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.update_act_response.UpdateActResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.update_act

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.update_act.update_act(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.update_act_request.UpdateActRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name
        input_["workflow_run_id"] = workflow_run_id
        input_["session_id"] = session_id
        input_["act_id"] = act_id
        input_["status"] = status
        if error is not None:
            input_["error"] = error

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncActResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service

    async def create(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        session_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        task: "aws_sdk_nova_act.types.task.Task",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        tool_specs: Optional["aws_sdk_nova_act.types.tool_specs.ToolSpecs"] = None,
        client_token: Optional[
            "aws_sdk_nova_act.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_nova_act.types.create_act_response.CreateActResponse":
        """<p>Creates a new AI task (act) within a session that can interact with tools and perform specific actions.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the session.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the session.</p>
            session_id: <p>The unique identifier of the session to create the act in.</p>
            task: <p>The task description that defines what the act should accomplish.</p>
            tool_specs: <p>A list of tool specifications that the act can invoke to complete its task.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.create_act_request.CreateActRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.create_act_response.CreateActResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_act

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_act.async_create_act(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.create_act_request.CreateActRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name
        input_["workflow_run_id"] = workflow_run_id
        input_["session_id"] = session_id
        input_["task"] = task
        if tool_specs is not None:
            input_["tool_specs"] = tool_specs
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        workflow_run_id: Optional[
            "aws_sdk_nova_act.types.uuid_string.UuidString"
        ] = None,
        session_id: Optional["aws_sdk_nova_act.types.uuid_string.UuidString"] = None,
        max_results: Optional["aws_sdk_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["aws_sdk_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_nova_act.types.list_acts_response.ListActsResponse":
        """<p>Lists all acts within a specific session with their current status and execution details.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the session.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the session.</p>
            session_id: <p>The unique identifier of the session to list acts for.</p>
            max_results: <p>The maximum number of acts to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned acts (ascending or descending).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.list_acts_request.ListActsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.list_acts_response.ListActsResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_acts

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_acts.async_list_acts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.list_acts_request.ListActsRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name
        if workflow_run_id is not None:
            input_["workflow_run_id"] = workflow_run_id
        if session_id is not None:
            input_["session_id"] = session_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def invoke_act_step(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        session_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        act_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        call_results: "aws_sdk_nova_act.types.call_results.CallResults",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        previous_step_id: Optional[
            "aws_sdk_nova_act.types.uuid_string.UuidString"
        ] = None,
    ) -> "aws_sdk_nova_act.types.invoke_act_step_response.InvokeActStepResponse":
        """<p>Executes the next step of an act, processing tool call results and returning new tool calls if needed.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the act.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the act.</p>
            session_id: <p>The unique identifier of the session containing the act.</p>
            act_id: <p>The unique identifier of the act to invoke the next step for.</p>
            call_results: <p>The results from previous tool calls that the act requested.</p>
            previous_step_id: <p>The identifier of the previous step, used for tracking execution flow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.invoke_act_step_request.InvokeActStepRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.invoke_act_step_response.InvokeActStepResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.invoke_act_step

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.invoke_act_step.async_invoke_act_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.invoke_act_step_request.InvokeActStepRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name
        input_["workflow_run_id"] = workflow_run_id
        input_["session_id"] = session_id
        input_["act_id"] = act_id
        input_["call_results"] = call_results
        if previous_step_id is not None:
            input_["previous_step_id"] = previous_step_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_act(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        session_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        act_id: "aws_sdk_nova_act.types.uuid_string.UuidString",
        status: "aws_sdk_nova_act.types.act_status.ActStatus",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        error: Optional["aws_sdk_nova_act.types.act_error.ActError"] = None,
    ) -> "aws_sdk_nova_act.types.update_act_response.UpdateActResponse":
        """<p>Updates an existing act's configuration, status, or error information.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the act.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the act.</p>
            session_id: <p>The unique identifier of the session containing the act.</p>
            act_id: <p>The unique identifier of the act to update.</p>
            status: <p>The new status to set for the act.</p>
            error: <p>Error information to associate with the act, if applicable.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.update_act_request.UpdateActRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.update_act_response.UpdateActResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.update_act

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.update_act.async_update_act(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.update_act_request.UpdateActRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name
        input_["workflow_run_id"] = workflow_run_id
        input_["session_id"] = session_id
        input_["act_id"] = act_id
        input_["status"] = status
        if error is not None:
            input_["error"] = error

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
