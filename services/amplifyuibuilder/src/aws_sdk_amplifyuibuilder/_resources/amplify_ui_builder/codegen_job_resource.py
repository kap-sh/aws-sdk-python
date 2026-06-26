from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_amplifyuibuilder._auth._signers
import aws_sdk_amplifyuibuilder._auth._sigv4
from aws_sdk_amplifyuibuilder._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
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
    from aws_sdk_amplifyuibuilder._services.amplify_ui_builder import (
        AmplifyUIBuilderClient,
        AmplifyUIBuilderClientConfig,
    )
    from aws_sdk_amplifyuibuilder._services.async_amplify_ui_builder import (
        AsyncAmplifyUIBuilderClient,
        AsyncAmplifyUIBuilderClientConfig,
    )


class CodegenJobResource:
    def __init__(self, service: AmplifyUIBuilderClient) -> None:
        self._service = service

    def create(
        self,
        app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        codegen_job_to_create: "aws_sdk_amplifyuibuilder.types.start_codegen_job_data.StartCodegenJobData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse":
        """<p>Starts a code generation job for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The idempotency token used to ensure that the code generation job request completes only once.</p>
            codegen_job_to_create: <p>The code generation job resource configuration.</p>

        Raises:
            aws_sdk_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            aws_sdk_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            aws_sdk_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job.start_codegen_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if client_token is not None:
            input_["client_token"] = client_token
        input_["codegen_job_to_create"] = codegen_job_to_create

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
    ) -> (
        "aws_sdk_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse"
    ):
        """<p>Returns an existing code generation job.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the code generation job.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app associated with the code generation job.</p>
            id: <p>The unique ID of the code generation job.</p>

        Raises:
            aws_sdk_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            aws_sdk_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            aws_sdk_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            aws_sdk_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job.get_codegen_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_amplifyuibuilder.types.list_codegen_jobs_limit.ListCodegenJobsLimit"
        ] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse":
        """<p>Retrieves a list of code generation jobs for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of jobs to retrieve.</p>

        Raises:
            aws_sdk_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            aws_sdk_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            aws_sdk_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs.list_codegen_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCodegenJobResource:
    def __init__(self, service: AsyncAmplifyUIBuilderClient) -> None:
        self._service = service

    async def create(
        self,
        app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        codegen_job_to_create: "aws_sdk_amplifyuibuilder.types.start_codegen_job_data.StartCodegenJobData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse":
        """<p>Starts a code generation job for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The idempotency token used to ensure that the code generation job request completes only once.</p>
            codegen_job_to_create: <p>The code generation job resource configuration.</p>

        Raises:
            aws_sdk_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            aws_sdk_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            aws_sdk_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job.async_start_codegen_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if client_token is not None:
            input_["client_token"] = client_token
        input_["codegen_job_to_create"] = codegen_job_to_create

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> (
        "aws_sdk_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse"
    ):
        """<p>Returns an existing code generation job.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the code generation job.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app associated with the code generation job.</p>
            id: <p>The unique ID of the code generation job.</p>

        Raises:
            aws_sdk_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            aws_sdk_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            aws_sdk_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            aws_sdk_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job.async_get_codegen_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        app_id: "aws_sdk_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_amplifyuibuilder.types.list_codegen_jobs_limit.ListCodegenJobsLimit"
        ] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse":
        """<p>Retrieves a list of code generation jobs for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of jobs to retrieve.</p>

        Raises:
            aws_sdk_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            aws_sdk_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            aws_sdk_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs.async_list_codegen_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
