from __future__ import annotations

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
    import aws_sdk_cleanroomsml.types.audience_generation_job_arn
    import aws_sdk_cleanroomsml.types.audience_generation_job_data_source
    import aws_sdk_cleanroomsml.types.audience_generation_job_summary
    import aws_sdk_cleanroomsml.types.configured_audience_model_arn
    import aws_sdk_cleanroomsml.types.delete_audience_generation_job_request
    import aws_sdk_cleanroomsml.types.get_audience_generation_job_request
    import aws_sdk_cleanroomsml.types.get_audience_generation_job_response
    import aws_sdk_cleanroomsml.types.list_audience_generation_jobs_request
    import aws_sdk_cleanroomsml.types.list_audience_generation_jobs_response
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.start_audience_generation_job_request
    import aws_sdk_cleanroomsml.types.start_audience_generation_job_response
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.uuid
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class AudienceGenerationJob:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        seed_audience: "aws_sdk_cleanroomsml.types.audience_generation_job_data_source.AudienceGenerationJobDataSource",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        include_seed_in_output: Optional[bool] = None,
        collaboration_id: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_cleanroomsml.types.start_audience_generation_job_response.StartAudienceGenerationJobResponse":
        """<p>Information necessary to start the audience generation job.</p>

        Args:
            name: <p>The name of the audience generation job.</p>
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that is used for this audience generation job.</p>
            seed_audience: <p>The seed audience that is used to generate the audience.</p>
            include_seed_in_output: <p>Whether the seed audience is included in the audience generation output.</p>
            collaboration_id: <p>The identifier of the collaboration that contains the audience generation job.</p>
            description: <p>The description of the audience generation job.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.start_audience_generation_job_response.StartAudienceGenerationJobResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_audience_generation_job

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_audience_generation_job.start_audience_generation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["configured_audience_model_arn"] = configured_audience_model_arn
        input_["seed_audience"] = seed_audience
        if include_seed_in_output is not None:
            input_["include_seed_in_output"] = include_seed_in_output
        if collaboration_id is not None:
            input_["collaboration_id"] = collaboration_id
        if description is not None:
            input_["description"] = description
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
        audience_generation_job_arn: "aws_sdk_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse":
        """<p>Returns information about an audience generation job.</p>

        Args:
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.get_audience_generation_job_request.GetAudienceGenerationJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_audience_generation_job

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_audience_generation_job.get_audience_generation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_audience_generation_job_request.GetAudienceGenerationJobRequest = {}  # type: ignore[typeddict-item]
        input_["audience_generation_job_arn"] = audience_generation_job_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        audience_generation_job_arn: "aws_sdk_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified audience generation job, and removes all data associated with the job.</p>

        Args:
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.delete_audience_generation_job_request.DeleteAudienceGenerationJobRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_audience_generation_job

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_audience_generation_job.delete_audience_generation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.delete_audience_generation_job_request.DeleteAudienceGenerationJobRequest = {}  # type: ignore[typeddict-item]
        input_["audience_generation_job_arn"] = audience_generation_job_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
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
        configured_audience_model_arn: Optional[
            "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
        ] = None,
        collaboration_id: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_audience_generation_jobs_response.ListAudienceGenerationJobsResponse":
        """<p>Returns a list of audience generation jobs.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that was used for the audience generation jobs that you are interested in.</p>
            collaboration_id: <p>The identifier of the collaboration that contains the audience generation jobs that you are interested in.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.list_audience_generation_jobs_request.ListAudienceGenerationJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.list_audience_generation_jobs_response.ListAudienceGenerationJobsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_generation_jobs

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_generation_jobs.list_audience_generation_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_audience_generation_jobs_request.ListAudienceGenerationJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if configured_audience_model_arn is not None:
            input_["configured_audience_model_arn"] = configured_audience_model_arn
        if collaboration_id is not None:
            input_["collaboration_id"] = collaboration_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAudienceGenerationJob:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        seed_audience: "aws_sdk_cleanroomsml.types.audience_generation_job_data_source.AudienceGenerationJobDataSource",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        include_seed_in_output: Optional[bool] = None,
        collaboration_id: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_cleanroomsml.types.start_audience_generation_job_response.StartAudienceGenerationJobResponse":
        """<p>Information necessary to start the audience generation job.</p>

        Args:
            name: <p>The name of the audience generation job.</p>
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that is used for this audience generation job.</p>
            seed_audience: <p>The seed audience that is used to generate the audience.</p>
            include_seed_in_output: <p>Whether the seed audience is included in the audience generation output.</p>
            collaboration_id: <p>The identifier of the collaboration that contains the audience generation job.</p>
            description: <p>The description of the audience generation job.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.start_audience_generation_job_response.StartAudienceGenerationJobResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_audience_generation_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_audience_generation_job.async_start_audience_generation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["configured_audience_model_arn"] = configured_audience_model_arn
        input_["seed_audience"] = seed_audience
        if include_seed_in_output is not None:
            input_["include_seed_in_output"] = include_seed_in_output
        if collaboration_id is not None:
            input_["collaboration_id"] = collaboration_id
        if description is not None:
            input_["description"] = description
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
        audience_generation_job_arn: "aws_sdk_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse":
        """<p>Returns information about an audience generation job.</p>

        Args:
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_audience_generation_job_request.GetAudienceGenerationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_audience_generation_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_audience_generation_job.async_get_audience_generation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_audience_generation_job_request.GetAudienceGenerationJobRequest = {}  # type: ignore[typeddict-item]
        input_["audience_generation_job_arn"] = audience_generation_job_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        audience_generation_job_arn: "aws_sdk_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified audience generation job, and removes all data associated with the job.</p>

        Args:
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.delete_audience_generation_job_request.DeleteAudienceGenerationJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_audience_generation_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_audience_generation_job.async_delete_audience_generation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.delete_audience_generation_job_request.DeleteAudienceGenerationJobRequest = {}  # type: ignore[typeddict-item]
        input_["audience_generation_job_arn"] = audience_generation_job_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
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
        configured_audience_model_arn: Optional[
            "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
        ] = None,
        collaboration_id: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_audience_generation_jobs_response.ListAudienceGenerationJobsResponse":
        """<p>Returns a list of audience generation jobs.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that was used for the audience generation jobs that you are interested in.</p>
            collaboration_id: <p>The identifier of the collaboration that contains the audience generation jobs that you are interested in.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_audience_generation_jobs_request.ListAudienceGenerationJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_audience_generation_jobs_response.ListAudienceGenerationJobsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_generation_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_audience_generation_jobs.async_list_audience_generation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_audience_generation_jobs_request.ListAudienceGenerationJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if configured_audience_model_arn is not None:
            input_["configured_audience_model_arn"] = configured_audience_model_arn
        if collaboration_id is not None:
            input_["collaboration_id"] = collaboration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
