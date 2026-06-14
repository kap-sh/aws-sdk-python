from __future__ import annotations

from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager, contextmanager
from typing import TYPE_CHECKING, Optional

import aws_sdk_sagemaker_geospatial._auth._signers
import aws_sdk_sagemaker_geospatial._auth._sigv4
from aws_sdk_sagemaker_geospatial._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.delete_earth_observation_job_input
    import aws_sdk_sagemaker_geospatial.types.delete_earth_observation_job_output
    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn
    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_status
    import aws_sdk_sagemaker_geospatial.types.execution_role_arn
    import aws_sdk_sagemaker_geospatial.types.export_earth_observation_job_input
    import aws_sdk_sagemaker_geospatial.types.export_earth_observation_job_output
    import aws_sdk_sagemaker_geospatial.types.get_earth_observation_job_input
    import aws_sdk_sagemaker_geospatial.types.get_earth_observation_job_output
    import aws_sdk_sagemaker_geospatial.types.get_tile_input
    import aws_sdk_sagemaker_geospatial.types.get_tile_output
    import aws_sdk_sagemaker_geospatial.types.input_config_input
    import aws_sdk_sagemaker_geospatial.types.job_config_input
    import aws_sdk_sagemaker_geospatial.types.kms_key
    import aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_input
    import aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output
    import aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output_config
    import aws_sdk_sagemaker_geospatial.types.next_token
    import aws_sdk_sagemaker_geospatial.types.output_config_input
    import aws_sdk_sagemaker_geospatial.types.output_type
    import aws_sdk_sagemaker_geospatial.types.sort_order
    import aws_sdk_sagemaker_geospatial.types.start_earth_observation_job_input
    import aws_sdk_sagemaker_geospatial.types.start_earth_observation_job_output
    import aws_sdk_sagemaker_geospatial.types.stop_earth_observation_job_input
    import aws_sdk_sagemaker_geospatial.types.stop_earth_observation_job_output
    import aws_sdk_sagemaker_geospatial.types.string_list_input
    import aws_sdk_sagemaker_geospatial.types.tags
    import aws_sdk_sagemaker_geospatial.types.target_options
    from aws_sdk_sagemaker_geospatial._services.async_sage_maker_geospatial import (
        AsyncSageMakerGeospatialClient,
        AsyncSageMakerGeospatialClientConfig,
    )
    from aws_sdk_sagemaker_geospatial._services.sage_maker_geospatial import (
        SageMakerGeospatialClient,
        SageMakerGeospatialClientConfig,
    )


class EarthObservationJob:
    def __init__(self, service: SageMakerGeospatialClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        input_config: "aws_sdk_sagemaker_geospatial.types.input_config_input.InputConfigInput",
        job_config: "aws_sdk_sagemaker_geospatial.types.job_config_input.JobConfigInput",
        execution_role_arn: "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        kms_key_id: Optional[
            "aws_sdk_sagemaker_geospatial.types.kms_key.KmsKey"
        ] = None,
        tags: Optional["aws_sdk_sagemaker_geospatial.types.tags.Tags"] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput":
        """<p>Use this operation to create an Earth observation job.</p>

        Args:
            name: <p>The name of the Earth Observation job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            kms_key_id: <p>The Key Management Service key ID for server-side encryption.</p>
            input_config: <p>Input configuration information for the Earth Observation job.</p>
            job_config: <p>An object containing information about the job configuration.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            tags: <p>Each tag consists of a key and a value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.start_earth_observation_job

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.start_earth_observation_job.start_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        input_["input_config"] = input_config
        input_["job_config"] = job_config
        input_["execution_role_arn"] = execution_role_arn
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
        arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput":
        """<p>Get the details for a previously initiated Earth Observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.get_earth_observation_job_input.GetEarthObservationJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_earth_observation_job

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_earth_observation_job.get_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.get_earth_observation_job_input.GetEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.delete_earth_observation_job_output.DeleteEarthObservationJobOutput":
        """<p>Use this operation to delete an Earth Observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job being deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.delete_earth_observation_job_input.DeleteEarthObservationJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.delete_earth_observation_job_output.DeleteEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.delete_earth_observation_job

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.delete_earth_observation_job.delete_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.delete_earth_observation_job_input.DeleteEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        status_equals: Optional[
            "aws_sdk_sagemaker_geospatial.types.earth_observation_job_status.EarthObservationJobStatus"
        ] = None,
        sort_order: Optional[
            "aws_sdk_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "aws_sdk_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput":
        """<p>Use this operation to get a list of the Earth Observation jobs associated with the calling Amazon Web Services account.</p>

        Args:
            status_equals: <p>A filter that retrieves only jobs with a specific status.</p>
            sort_order: <p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>
            sort_by: <p>The parameter by which to sort the results.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The total number of items to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_earth_observation_jobs

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_earth_observation_jobs.list_earth_observation_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    def export_earth_observation_job(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        execution_role_arn: "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        output_config: "aws_sdk_sagemaker_geospatial.types.output_config_input.OutputConfigInput",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        export_source_images: Optional[bool] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.export_earth_observation_job_output.ExportEarthObservationJobOutput":
        """<p>Use this operation to export results of an Earth Observation job and optionally source images used as input to the EOJ to an Amazon S3 location.</p>

        Args:
            arn: <p>The input Amazon Resource Name (ARN) of the Earth Observation job being exported.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            output_config: <p>An object containing information about the output file.</p>
            export_source_images: <p>The source images provided to the Earth Observation job being exported.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.export_earth_observation_job_input.ExportEarthObservationJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.export_earth_observation_job_output.ExportEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.export_earth_observation_job

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.export_earth_observation_job.export_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.export_earth_observation_job_input.ExportEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["execution_role_arn"] = execution_role_arn
        input_["output_config"] = output_config
        if export_source_images is not None:
            input_["export_source_images"] = export_source_images

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    @contextmanager
    def get_tile(
        self,
        x: int,
        y: int,
        z: int,
        image_assets: "aws_sdk_sagemaker_geospatial.types.string_list_input.StringListInput",
        target: "aws_sdk_sagemaker_geospatial.types.target_options.TargetOptions",
        arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        image_mask: Optional[bool] = None,
        output_format: Optional[str] = None,
        time_range_filter: Optional[str] = None,
        property_filters: Optional[str] = None,
        output_data_type: Optional[
            "aws_sdk_sagemaker_geospatial.types.output_type.OutputType"
        ] = None,
        execution_role_arn: Optional[
            "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
        ] = None,
    ) -> "Generator[aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput]":
        """<p>Gets a web mercator tile for the given Earth Observation job.</p>

        Args:
            x: <p>The x coordinate of the tile input.</p>
            y: <p>The y coordinate of the tile input.</p>
            z: <p>The z coordinate of the tile input.</p>
            image_assets: <p>The particular assets or bands to tile.</p>
            target: <p>Determines what part of the Earth Observation job to tile. 'INPUT' or 'OUTPUT' are the valid options.</p>
            arn: <p>The Amazon Resource Name (ARN) of the tile operation.</p>
            image_mask: <p>Determines whether or not to return a valid data mask.</p>
            output_format: <p>The data format of the output tile. The formats include .npy, .png and .jpg.</p>
            time_range_filter: <p>Time range filter applied to imagery to find the images to tile.</p>
            property_filters: <p>Property filters for the imagery to tile.</p>
            output_data_type: <p>The output data type of the tile operation.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specify.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.get_tile_input.GetTileInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_tile

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_tile.get_tile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.get_tile_input.GetTileInput = {}  # type: ignore[typeddict-item]
        input_["x"] = x
        input_["y"] = y
        input_["z"] = z
        input_["image_assets"] = image_assets
        input_["target"] = target
        input_["arn"] = arn
        if image_mask is not None:
            input_["image_mask"] = image_mask
        if output_format is not None:
            input_["output_format"] = output_format
        if time_range_filter is not None:
            input_["time_range_filter"] = time_range_filter
        if property_filters is not None:
            input_["property_filters"] = property_filters
        if output_data_type is not None:
            input_["output_data_type"] = output_data_type
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    def stop_earth_observation_job(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.stop_earth_observation_job_output.StopEarthObservationJobOutput":
        """<p>Use this operation to stop an existing earth observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job being stopped.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.stop_earth_observation_job_input.StopEarthObservationJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.stop_earth_observation_job_output.StopEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.stop_earth_observation_job

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.stop_earth_observation_job.stop_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.stop_earth_observation_job_input.StopEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEarthObservationJob:
    def __init__(self, service: AsyncSageMakerGeospatialClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        input_config: "aws_sdk_sagemaker_geospatial.types.input_config_input.InputConfigInput",
        job_config: "aws_sdk_sagemaker_geospatial.types.job_config_input.JobConfigInput",
        execution_role_arn: "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        kms_key_id: Optional[
            "aws_sdk_sagemaker_geospatial.types.kms_key.KmsKey"
        ] = None,
        tags: Optional["aws_sdk_sagemaker_geospatial.types.tags.Tags"] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput":
        """<p>Use this operation to create an Earth observation job.</p>

        Args:
            name: <p>The name of the Earth Observation job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            kms_key_id: <p>The Key Management Service key ID for server-side encryption.</p>
            input_config: <p>Input configuration information for the Earth Observation job.</p>
            job_config: <p>An object containing information about the job configuration.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            tags: <p>Each tag consists of a key and a value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.start_earth_observation_job

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.start_earth_observation_job.async_start_earth_observation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        input_["input_config"] = input_config
        input_["job_config"] = job_config
        input_["execution_role_arn"] = execution_role_arn
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
        arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput":
        """<p>Get the details for a previously initiated Earth Observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.get_earth_observation_job_input.GetEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_earth_observation_job

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_earth_observation_job.async_get_earth_observation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.get_earth_observation_job_input.GetEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.delete_earth_observation_job_output.DeleteEarthObservationJobOutput":
        """<p>Use this operation to delete an Earth Observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job being deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.delete_earth_observation_job_input.DeleteEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.delete_earth_observation_job_output.DeleteEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.delete_earth_observation_job

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.delete_earth_observation_job.async_delete_earth_observation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.delete_earth_observation_job_input.DeleteEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        status_equals: Optional[
            "aws_sdk_sagemaker_geospatial.types.earth_observation_job_status.EarthObservationJobStatus"
        ] = None,
        sort_order: Optional[
            "aws_sdk_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "aws_sdk_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput":
        """<p>Use this operation to get a list of the Earth Observation jobs associated with the calling Amazon Web Services account.</p>

        Args:
            status_equals: <p>A filter that retrieves only jobs with a specific status.</p>
            sort_order: <p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>
            sort_by: <p>The parameter by which to sort the results.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The total number of items to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_earth_observation_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_earth_observation_jobs.async_list_earth_observation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def export_earth_observation_job(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        execution_role_arn: "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        output_config: "aws_sdk_sagemaker_geospatial.types.output_config_input.OutputConfigInput",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        export_source_images: Optional[bool] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.export_earth_observation_job_output.ExportEarthObservationJobOutput":
        """<p>Use this operation to export results of an Earth Observation job and optionally source images used as input to the EOJ to an Amazon S3 location.</p>

        Args:
            arn: <p>The input Amazon Resource Name (ARN) of the Earth Observation job being exported.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            output_config: <p>An object containing information about the output file.</p>
            export_source_images: <p>The source images provided to the Earth Observation job being exported.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.export_earth_observation_job_input.ExportEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.export_earth_observation_job_output.ExportEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.export_earth_observation_job

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.export_earth_observation_job.async_export_earth_observation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.export_earth_observation_job_input.ExportEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["execution_role_arn"] = execution_role_arn
        input_["output_config"] = output_config
        if export_source_images is not None:
            input_["export_source_images"] = export_source_images

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    @asynccontextmanager
    async def get_tile(
        self,
        x: int,
        y: int,
        z: int,
        image_assets: "aws_sdk_sagemaker_geospatial.types.string_list_input.StringListInput",
        target: "aws_sdk_sagemaker_geospatial.types.target_options.TargetOptions",
        arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        image_mask: Optional[bool] = None,
        output_format: Optional[str] = None,
        time_range_filter: Optional[str] = None,
        property_filters: Optional[str] = None,
        output_data_type: Optional[
            "aws_sdk_sagemaker_geospatial.types.output_type.OutputType"
        ] = None,
        execution_role_arn: Optional[
            "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
        ] = None,
    ) -> "AsyncGenerator[aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput]":
        """<p>Gets a web mercator tile for the given Earth Observation job.</p>

        Args:
            x: <p>The x coordinate of the tile input.</p>
            y: <p>The y coordinate of the tile input.</p>
            z: <p>The z coordinate of the tile input.</p>
            image_assets: <p>The particular assets or bands to tile.</p>
            target: <p>Determines what part of the Earth Observation job to tile. 'INPUT' or 'OUTPUT' are the valid options.</p>
            arn: <p>The Amazon Resource Name (ARN) of the tile operation.</p>
            image_mask: <p>Determines whether or not to return a valid data mask.</p>
            output_format: <p>The data format of the output tile. The formats include .npy, .png and .jpg.</p>
            time_range_filter: <p>Time range filter applied to imagery to find the images to tile.</p>
            property_filters: <p>Property filters for the imagery to tile.</p>
            output_data_type: <p>The output data type of the tile operation.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specify.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.get_tile_input.GetTileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_tile

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_tile.async_get_tile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.get_tile_input.GetTileInput = {}  # type: ignore[typeddict-item]
        input_["x"] = x
        input_["y"] = y
        input_["z"] = z
        input_["image_assets"] = image_assets
        input_["target"] = target
        input_["arn"] = arn
        if image_mask is not None:
            input_["image_mask"] = image_mask
        if output_format is not None:
            input_["output_format"] = output_format
        if time_range_filter is not None:
            input_["time_range_filter"] = time_range_filter
        if property_filters is not None:
            input_["property_filters"] = property_filters
        if output_data_type is not None:
            input_["output_data_type"] = output_data_type
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    async def stop_earth_observation_job(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.stop_earth_observation_job_output.StopEarthObservationJobOutput":
        """<p>Use this operation to stop an existing earth observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job being stopped.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.stop_earth_observation_job_input.StopEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.stop_earth_observation_job_output.StopEarthObservationJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.stop_earth_observation_job

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.stop_earth_observation_job.async_stop_earth_observation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.stop_earth_observation_job_input.StopEarthObservationJobInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
