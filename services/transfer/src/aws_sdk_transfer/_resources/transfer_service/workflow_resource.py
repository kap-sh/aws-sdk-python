from typing import TYPE_CHECKING, Optional

from aws_sdk_transfer._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_transfer.types.create_workflow_request
    import aws_sdk_transfer.types.create_workflow_response
    import aws_sdk_transfer.types.delete_workflow_request
    import aws_sdk_transfer.types.describe_workflow_request
    import aws_sdk_transfer.types.describe_workflow_response
    import aws_sdk_transfer.types.list_workflows_request
    import aws_sdk_transfer.types.list_workflows_response
    import aws_sdk_transfer.types.listed_workflow
    import aws_sdk_transfer.types.max_results
    import aws_sdk_transfer.types.next_token
    import aws_sdk_transfer.types.tags
    import aws_sdk_transfer.types.workflow_description
    import aws_sdk_transfer.types.workflow_id
    import aws_sdk_transfer.types.workflow_steps
    from aws_sdk_transfer._services.async_transfer import (
        AsyncTransferClient,
        AsyncTransferClientConfig,
    )
    from aws_sdk_transfer._services.transfer import TransferClient, TransferClientConfig


class WorkflowResource:
    def __init__(self, service: TransferClient) -> None:
        self._service = service

    def create(
        self,
        steps: "aws_sdk_transfer.types.workflow_steps.WorkflowSteps",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        description: Optional[
            "aws_sdk_transfer.types.workflow_description.WorkflowDescription"
        ] = None,
        on_exception_steps: Optional[
            "aws_sdk_transfer.types.workflow_steps.WorkflowSteps"
        ] = None,
        tags: Optional["aws_sdk_transfer.types.tags.Tags"] = None,
    ) -> "aws_sdk_transfer.types.create_workflow_response.CreateWorkflowResponse":
        """<p> Allows you to create a workflow with specified steps and step details the workflow invokes after file transfer completes. After creating a workflow, you can associate the workflow created with any transfer servers by specifying the <code>workflow-details</code> field in <code>CreateServer</code> and <code>UpdateServer</code> operations. </p>

        Args:
            description: <p>A textual description for the workflow.</p>
            steps: <p>Specifies the details for the steps that are in the specified workflow.</p> <p> The <code>TYPE</code> specifies which of the following actions is being taken for this step. </p> <ul> <li> <p> <b> <code>COPY</code> </b> - Copy the file to another location.</p> </li> <li> <p> <b> <code>CUSTOM</code> </b> - Perform a custom step with an Lambda function target.</p> </li> <li> <p> <b> <code>DECRYPT</code> </b> - Decrypt a file that was encrypted before it was uploaded.</p> </li> <li> <p> <b> <code>DELETE</code> </b> - Delete the file.</p> </li> <li> <p> <b> <code>TAG</code> </b> - Add a tag to the file.</p> </li> </ul> <note> <p> Currently, copying and tagging are supported only on S3. </p> </note> <p> For file location, you specify either the Amazon S3 bucket and key, or the Amazon EFS file system ID and path. </p>
            on_exception_steps: <p>Specifies the steps (actions) to take if errors are encountered during execution of the workflow.</p> <note> <p>For custom steps, the Lambda function needs to send <code>FAILURE</code> to the call back API to kick off the exception steps. Additionally, if the Lambda does not send <code>SUCCESS</code> before it times out, the exception steps are executed.</p> </note>
            tags: <p>Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.create_workflow

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.create_workflow.create_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.create_workflow_request.CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["steps"] = steps
        if on_exception_steps is not None:
            input_["on_exception_steps"] = on_exception_steps
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
        workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_workflow_response.DescribeWorkflowResponse":
        """<p>Describes the specified workflow.</p>

        Args:
            workflow_id: <p>A unique identifier for the workflow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.describe_workflow_request.DescribeWorkflowRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.describe_workflow_response.DescribeWorkflowResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_workflow

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.describe_workflow.describe_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.describe_workflow_request.DescribeWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified workflow.</p>

        Args:
            workflow_id: <p>A unique identifier for the workflow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_workflow

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.delete_workflow.delete_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.delete_workflow_request.DeleteWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Lists all workflows associated with your Amazon Web Services account for your current region.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p> <code>ListWorkflows</code> returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional workflows.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_workflows

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.list_workflows.list_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.list_workflows_request.ListWorkflowsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncWorkflowResource:
    def __init__(self, service: AsyncTransferClient) -> None:
        self._service = service

    async def create(
        self,
        steps: "aws_sdk_transfer.types.workflow_steps.WorkflowSteps",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        description: Optional[
            "aws_sdk_transfer.types.workflow_description.WorkflowDescription"
        ] = None,
        on_exception_steps: Optional[
            "aws_sdk_transfer.types.workflow_steps.WorkflowSteps"
        ] = None,
        tags: Optional["aws_sdk_transfer.types.tags.Tags"] = None,
    ) -> "aws_sdk_transfer.types.create_workflow_response.CreateWorkflowResponse":
        """<p> Allows you to create a workflow with specified steps and step details the workflow invokes after file transfer completes. After creating a workflow, you can associate the workflow created with any transfer servers by specifying the <code>workflow-details</code> field in <code>CreateServer</code> and <code>UpdateServer</code> operations. </p>

        Args:
            description: <p>A textual description for the workflow.</p>
            steps: <p>Specifies the details for the steps that are in the specified workflow.</p> <p> The <code>TYPE</code> specifies which of the following actions is being taken for this step. </p> <ul> <li> <p> <b> <code>COPY</code> </b> - Copy the file to another location.</p> </li> <li> <p> <b> <code>CUSTOM</code> </b> - Perform a custom step with an Lambda function target.</p> </li> <li> <p> <b> <code>DECRYPT</code> </b> - Decrypt a file that was encrypted before it was uploaded.</p> </li> <li> <p> <b> <code>DELETE</code> </b> - Delete the file.</p> </li> <li> <p> <b> <code>TAG</code> </b> - Add a tag to the file.</p> </li> </ul> <note> <p> Currently, copying and tagging are supported only on S3. </p> </note> <p> For file location, you specify either the Amazon S3 bucket and key, or the Amazon EFS file system ID and path. </p>
            on_exception_steps: <p>Specifies the steps (actions) to take if errors are encountered during execution of the workflow.</p> <note> <p>For custom steps, the Lambda function needs to send <code>FAILURE</code> to the call back API to kick off the exception steps. Additionally, if the Lambda does not send <code>SUCCESS</code> before it times out, the exception steps are executed.</p> </note>
            tags: <p>Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.create_workflow

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.create_workflow.async_create_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.create_workflow_request.CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input_["description"] = description
        input_["steps"] = steps
        if on_exception_steps is not None:
            input_["on_exception_steps"] = on_exception_steps
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
        workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_workflow_response.DescribeWorkflowResponse":
        """<p>Describes the specified workflow.</p>

        Args:
            workflow_id: <p>A unique identifier for the workflow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.describe_workflow_request.DescribeWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.describe_workflow_response.DescribeWorkflowResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_workflow

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.describe_workflow.async_describe_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.describe_workflow_request.DescribeWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified workflow.</p>

        Args:
            workflow_id: <p>A unique identifier for the workflow.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_workflow

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.delete_workflow.async_delete_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.delete_workflow_request.DeleteWorkflowRequest = {}  # type: ignore[typeddict-item]
        input_["workflow_id"] = workflow_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Lists all workflows associated with your Amazon Web Services account for your current region.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p> <code>ListWorkflows</code> returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional workflows.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_workflows

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.list_workflows.async_list_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.list_workflows_request.ListWorkflowsRequest = {}  # type: ignore[typeddict-item]
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
