from typing import Optional, TYPE_CHECKING
from aws_sdk_amplifyuibuilder._services.async_amplify_ui_builder import ensure_async_iterator
from aws_sdk_amplifyuibuilder._services.amplify_ui_builder import ensure_sync_iterator
from aws_sdk_amplifyuibuilder._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_amplifyuibuilder._auth._signers
import aws_sdk_amplifyuibuilder._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_amplifyuibuilder._services.amplify_ui_builder import AmplifyUIBuilderClient, AmplifyUIBuilderClientConfig
    from aws_sdk_amplifyuibuilder._services.async_amplify_ui_builder import AsyncAmplifyUIBuilderClient, AsyncAmplifyUIBuilderClientConfig
    import aws_sdk_amplifyuibuilder.types.app_id
    import aws_sdk_amplifyuibuilder.types.codegen_job_summary
    import aws_sdk_amplifyuibuilder.types.get_codegen_job_request
    import aws_sdk_amplifyuibuilder.types.get_codegen_job_response
    import aws_sdk_amplifyuibuilder.types.list_codegen_jobs_limit
    import aws_sdk_amplifyuibuilder.types.list_codegen_jobs_request
    import aws_sdk_amplifyuibuilder.types.list_codegen_jobs_response
    import aws_sdk_amplifyuibuilder.types.start_codegen_job_data
    import aws_sdk_amplifyuibuilder.types.start_codegen_job_request
    import aws_sdk_amplifyuibuilder.types.start_codegen_job_response
    import aws_sdk_amplifyuibuilder.types.uuid

class CodegenJobResource:
    def __init__(self, service: AmplifyUIBuilderClient) -> None:
        self._service = service
    def create(self, app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId", environment_name: str, codegen_job_to_create: "aws_sdk_amplifyuibuilder.types.start_codegen_job_data.StartCodegenJobData", *, config_overrides: Optional[AmplifyUIBuilderClientConfig] = None, client_token: Optional[str] = None) -> "aws_sdk_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse":
        """<p>Starts a code generation job for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The idempotency token used to ensure that the code generation job request completes only once.</p>
            codegen_job_to_create: <p>The code generation job resource configuration.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest]') -> OperationResponse["aws_sdk_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse"]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job
            output, http_response = aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job.start_codegen_job(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        if client_token is not None:
            input["client_token"] = client_token
        input["codegen_job_to_create"] = codegen_job_to_create

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId", environment_name: str, id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid", *, config_overrides: Optional[AmplifyUIBuilderClientConfig] = None) -> "aws_sdk_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse":
        """<p>Returns an existing code generation job.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the code generation job.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app associated with the code generation job.</p>
            id: <p>The unique ID of the code generation job.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest]') -> OperationResponse["aws_sdk_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse"]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job
            output, http_response = aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job.get_codegen_job(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        input["id"] = id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId", environment_name: str, *, config_overrides: Optional[AmplifyUIBuilderClientConfig] = None, next_token: Optional[str] = None, max_results: Optional["aws_sdk_amplifyuibuilder.types.list_codegen_jobs_limit.ListCodegenJobsLimit"] = None) -> "aws_sdk_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse":
        """<p>Retrieves a list of code generation jobs for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of jobs to retrieve.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest]') -> OperationResponse["aws_sdk_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse"]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs
            output, http_response = aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs.list_codegen_jobs(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncCodegenJobResource:
    def __init__(self, service: AsyncAmplifyUIBuilderClient) -> None:
        self._service = service
    async def create(self, app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId", environment_name: str, codegen_job_to_create: "aws_sdk_amplifyuibuilder.types.start_codegen_job_data.StartCodegenJobData", *, config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None, client_token: Optional[str] = None) -> "aws_sdk_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse":
        """<p>Starts a code generation job for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The idempotency token used to ensure that the code generation job request completes only once.</p>
            codegen_job_to_create: <p>The code generation job resource configuration.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest]') -> AsyncOperationResponse["aws_sdk_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse"]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job
            output, http_response = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job.async_start_codegen_job(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        if client_token is not None:
            input["client_token"] = client_token
        input["codegen_job_to_create"] = codegen_job_to_create

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId", environment_name: str, id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid", *, config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None) -> "aws_sdk_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse":
        """<p>Returns an existing code generation job.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the code generation job.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app associated with the code generation job.</p>
            id: <p>The unique ID of the code generation job.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest]') -> AsyncOperationResponse["aws_sdk_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse"]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job
            output, http_response = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job.async_get_codegen_job(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        input["id"] = id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId", environment_name: str, *, config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None, next_token: Optional[str] = None, max_results: Optional["aws_sdk_amplifyuibuilder.types.list_codegen_jobs_limit.ListCodegenJobsLimit"] = None) -> "aws_sdk_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse":
        """<p>Retrieves a list of code generation jobs for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of jobs to retrieve.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest]') -> AsyncOperationResponse["aws_sdk_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse"]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs
            output, http_response = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs.async_list_codegen_jobs(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output