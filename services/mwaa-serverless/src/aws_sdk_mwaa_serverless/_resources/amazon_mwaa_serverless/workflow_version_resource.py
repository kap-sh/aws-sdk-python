from typing import TYPE_CHECKING, Optional

from aws_sdk_mwaa_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.list_workflow_versions_request
    import aws_sdk_mwaa_serverless.types.list_workflow_versions_response
    import aws_sdk_mwaa_serverless.types.workflow_arn
    import aws_sdk_mwaa_serverless.types.workflow_version_summary
    from aws_sdk_mwaa_serverless._services.async_mwaa_serverless import (
        AsyncMWAAServerlessClient,
        AsyncMWAAServerlessClientConfig,
    )
    from aws_sdk_mwaa_serverless._services.mwaa_serverless import (
        MWAAServerlessClient,
        MWAAServerlessClientConfig,
    )


class WorkflowVersionResource:
    def __init__(self, service: MWAAServerlessClient) -> None:
        self._service = service

    def list(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_mwaa_serverless.types.list_workflow_versions_response.ListWorkflowVersionsResponse":
        """<p>Lists all versions of a specified workflow, with optional pagination support.</p>

        Args:
            max_results: <p>The maximum number of workflow versions to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowVersions</code>.</p>
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow for which you want to list versions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mwaa_serverless.types.list_workflow_versions_request.ListWorkflowVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mwaa_serverless.types.list_workflow_versions_response.ListWorkflowVersionsResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_versions

            output, http_response = (
                aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_versions.list_workflow_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.list_workflow_versions_request.ListWorkflowVersionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["workflow_arn"] = workflow_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncWorkflowVersionResource:
    def __init__(self, service: AsyncMWAAServerlessClient) -> None:
        self._service = service

    async def list(
        self,
        workflow_arn: "aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_mwaa_serverless.types.list_workflow_versions_response.ListWorkflowVersionsResponse":
        """<p>Lists all versions of a specified workflow, with optional pagination support.</p>

        Args:
            max_results: <p>The maximum number of workflow versions to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowVersions</code>.</p>
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow for which you want to list versions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mwaa_serverless.types.list_workflow_versions_request.ListWorkflowVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mwaa_serverless.types.list_workflow_versions_response.ListWorkflowVersionsResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_versions

            (
                output,
                http_response,
            ) = await aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_versions.async_list_workflow_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.list_workflow_versions_request.ListWorkflowVersionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["workflow_arn"] = workflow_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
