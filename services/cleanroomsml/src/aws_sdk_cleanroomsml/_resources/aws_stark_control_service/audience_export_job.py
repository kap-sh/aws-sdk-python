from typing import TYPE_CHECKING, Optional

import aws_sdk_cleanroomsml._auth._signers
import aws_sdk_cleanroomsml._auth._sigv4
from aws_sdk_cleanroomsml._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_export_job_summary
    import aws_sdk_cleanroomsml.types.audience_generation_job_arn
    import aws_sdk_cleanroomsml.types.audience_size
    import aws_sdk_cleanroomsml.types.list_audience_export_jobs_request
    import aws_sdk_cleanroomsml.types.list_audience_export_jobs_response
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.start_audience_export_job_request
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class AudienceExportJob:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        audience_generation_job_arn: "aws_sdk_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        audience_size: "aws_sdk_cleanroomsml.types.audience_size.AudienceSize",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> None:
        """<p>Export an audience of a specified size after you have generated an audience.</p>

        Args:
            name: <p>The name of the audience export job.</p>
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you want to export.</p>
            description: <p>The description of the audience export job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.start_audience_export_job_request.StartAudienceExportJobRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_audience_export_job

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_audience_export_job.start_audience_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.start_audience_export_job_request.StartAudienceExportJobRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["audience_generation_job_arn"] = audience_generation_job_arn
        input["audience_size"] = audience_size
        if description is not None:
            input["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
        audience_generation_job_arn: Optional[
            "aws_sdk_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_audience_export_jobs_response.ListAudienceExportJobsResponse":
        """<p>Returns a list of the audience export jobs.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.list_audience_export_jobs_request.ListAudienceExportJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.list_audience_export_jobs_response.ListAudienceExportJobsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_export_jobs

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_export_jobs.list_audience_export_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.list_audience_export_jobs_request.ListAudienceExportJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if audience_generation_job_arn is not None:
            input["audience_generation_job_arn"] = audience_generation_job_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAudienceExportJob:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        audience_generation_job_arn: "aws_sdk_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        audience_size: "aws_sdk_cleanroomsml.types.audience_size.AudienceSize",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> None:
        """<p>Export an audience of a specified size after you have generated an audience.</p>

        Args:
            name: <p>The name of the audience export job.</p>
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you want to export.</p>
            description: <p>The description of the audience export job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.start_audience_export_job_request.StartAudienceExportJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_audience_export_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_audience_export_job.async_start_audience_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.start_audience_export_job_request.StartAudienceExportJobRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["audience_generation_job_arn"] = audience_generation_job_arn
        input["audience_size"] = audience_size
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
        audience_generation_job_arn: Optional[
            "aws_sdk_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_audience_export_jobs_response.ListAudienceExportJobsResponse":
        """<p>Returns a list of the audience export jobs.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_audience_export_jobs_request.ListAudienceExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_audience_export_jobs_response.ListAudienceExportJobsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_export_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_export_jobs.async_list_audience_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.list_audience_export_jobs_request.ListAudienceExportJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if audience_generation_job_arn is not None:
            input["audience_generation_job_arn"] = audience_generation_job_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
