from __future__ import annotations

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
    import aws_sdk_nova_act.types.create_workflow_definition_request
    import aws_sdk_nova_act.types.create_workflow_definition_response
    import aws_sdk_nova_act.types.delete_workflow_definition_request
    import aws_sdk_nova_act.types.delete_workflow_definition_response
    import aws_sdk_nova_act.types.get_workflow_definition_request
    import aws_sdk_nova_act.types.get_workflow_definition_response
    import aws_sdk_nova_act.types.list_workflow_definitions_request
    import aws_sdk_nova_act.types.list_workflow_definitions_response
    import aws_sdk_nova_act.types.max_results
    import aws_sdk_nova_act.types.next_token
    import aws_sdk_nova_act.types.sort_order
    import aws_sdk_nova_act.types.workflow_definition_name
    import aws_sdk_nova_act.types.workflow_definition_summary
    import aws_sdk_nova_act.types.workflow_description
    import aws_sdk_nova_act.types.workflow_export_config
    from aws_sdk_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
        AsyncNovaActClientConfig,
    )
    from aws_sdk_nova_act._services.nova_act import NovaActClient, NovaActClientConfig


class WorkflowDefinitionResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        description: Optional[
            "aws_sdk_nova_act.types.workflow_description.WorkflowDescription"
        ] = None,
        export_config: Optional[
            "aws_sdk_nova_act.types.workflow_export_config.WorkflowExportConfig"
        ] = None,
        client_token: Optional[
            "aws_sdk_nova_act.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_nova_act.types.create_workflow_definition_response.CreateWorkflowDefinitionResponse":
        """<p>Creates a new workflow definition template that can be used to execute multiple workflow runs.</p>

        Args:
            name: <p>The name of the workflow definition. Must be unique within your account and region.</p>
            description: <p>An optional description of the workflow definition's purpose and functionality.</p>
            export_config: <p>Configuration for exporting workflow execution data to Amazon Simple Storage Service.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.create_workflow_definition_response.CreateWorkflowDefinitionResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_definition

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_definition.create_workflow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if export_config is not None:
            input_["export_config"] = export_config
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "aws_sdk_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse":
        """<p>Retrieves the details and configuration of a specific workflow definition.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.get_workflow_definition_request.GetWorkflowDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_definition

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_definition.get_workflow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.get_workflow_definition_request.GetWorkflowDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "aws_sdk_nova_act.types.delete_workflow_definition_response.DeleteWorkflowDefinitionResponse":
        """<p>Deletes a workflow definition and all associated resources. This operation cannot be undone.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.delete_workflow_definition_request.DeleteWorkflowDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.delete_workflow_definition_response.DeleteWorkflowDefinitionResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_definition

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_definition.delete_workflow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.delete_workflow_definition_request.DeleteWorkflowDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["aws_sdk_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["aws_sdk_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_nova_act.types.list_workflow_definitions_response.ListWorkflowDefinitionsResponse":
        """<p>Lists all workflow definitions in your account with optional filtering and pagination.</p>

        Args:
            max_results: <p>The maximum number of workflow definitions to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned workflow definitions (ascending or descending).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.list_workflow_definitions_request.ListWorkflowDefinitionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.list_workflow_definitions_response.ListWorkflowDefinitionsResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_definitions

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_definitions.list_workflow_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.list_workflow_definitions_request.ListWorkflowDefinitionsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncWorkflowDefinitionResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        description: Optional[
            "aws_sdk_nova_act.types.workflow_description.WorkflowDescription"
        ] = None,
        export_config: Optional[
            "aws_sdk_nova_act.types.workflow_export_config.WorkflowExportConfig"
        ] = None,
        client_token: Optional[
            "aws_sdk_nova_act.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_nova_act.types.create_workflow_definition_response.CreateWorkflowDefinitionResponse":
        """<p>Creates a new workflow definition template that can be used to execute multiple workflow runs.</p>

        Args:
            name: <p>The name of the workflow definition. Must be unique within your account and region.</p>
            description: <p>An optional description of the workflow definition's purpose and functionality.</p>
            export_config: <p>Configuration for exporting workflow execution data to Amazon Simple Storage Service.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.create_workflow_definition_response.CreateWorkflowDefinitionResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_definition

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_definition.async_create_workflow_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if export_config is not None:
            input_["export_config"] = export_config
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> "aws_sdk_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse":
        """<p>Retrieves the details and configuration of a specific workflow definition.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.get_workflow_definition_request.GetWorkflowDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_definition

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_definition.async_get_workflow_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.get_workflow_definition_request.GetWorkflowDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        workflow_definition_name: "aws_sdk_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> "aws_sdk_nova_act.types.delete_workflow_definition_response.DeleteWorkflowDefinitionResponse":
        """<p>Deletes a workflow definition and all associated resources. This operation cannot be undone.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.delete_workflow_definition_request.DeleteWorkflowDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.delete_workflow_definition_response.DeleteWorkflowDefinitionResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_definition

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_definition.async_delete_workflow_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.delete_workflow_definition_request.DeleteWorkflowDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_definition_name"] = workflow_definition_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        max_results: Optional["aws_sdk_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["aws_sdk_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "aws_sdk_nova_act.types.list_workflow_definitions_response.ListWorkflowDefinitionsResponse":
        """<p>Lists all workflow definitions in your account with optional filtering and pagination.</p>

        Args:
            max_results: <p>The maximum number of workflow definitions to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned workflow definitions (ascending or descending).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.list_workflow_definitions_request.ListWorkflowDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.list_workflow_definitions_response.ListWorkflowDefinitionsResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_definitions

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_definitions.async_list_workflow_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.list_workflow_definitions_request.ListWorkflowDefinitionsRequest = {}  # type: ignore[typeddict-item]
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
