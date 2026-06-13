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
    import aws_sdk_sagemaker_geospatial.types.delete_vector_enrichment_job_input
    import aws_sdk_sagemaker_geospatial.types.delete_vector_enrichment_job_output
    import aws_sdk_sagemaker_geospatial.types.execution_role_arn
    import aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_input
    import aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_output
    import aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_output_config
    import aws_sdk_sagemaker_geospatial.types.get_vector_enrichment_job_input
    import aws_sdk_sagemaker_geospatial.types.get_vector_enrichment_job_output
    import aws_sdk_sagemaker_geospatial.types.kms_key
    import aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_input
    import aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output
    import aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output_config
    import aws_sdk_sagemaker_geospatial.types.next_token
    import aws_sdk_sagemaker_geospatial.types.sort_order
    import aws_sdk_sagemaker_geospatial.types.start_vector_enrichment_job_input
    import aws_sdk_sagemaker_geospatial.types.start_vector_enrichment_job_output
    import aws_sdk_sagemaker_geospatial.types.stop_vector_enrichment_job_input
    import aws_sdk_sagemaker_geospatial.types.stop_vector_enrichment_job_output
    import aws_sdk_sagemaker_geospatial.types.tags
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_config
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_input_config
    from aws_sdk_sagemaker_geospatial._services.async_sage_maker_geospatial import (
        AsyncSageMakerGeospatialClient,
        AsyncSageMakerGeospatialClientConfig,
    )
    from aws_sdk_sagemaker_geospatial._services.sage_maker_geospatial import (
        SageMakerGeospatialClient,
        SageMakerGeospatialClientConfig,
    )


class VectorEnrichmentJob:
    def __init__(self, service: SageMakerGeospatialClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        input_config: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_input_config.VectorEnrichmentJobInputConfig",
        job_config: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_config.VectorEnrichmentJobConfig",
        execution_role_arn: "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        kms_key_id: Optional[
            "aws_sdk_sagemaker_geospatial.types.kms_key.KmsKey"
        ] = None,
        tags: Optional["aws_sdk_sagemaker_geospatial.types.tags.Tags"] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.start_vector_enrichment_job_output.StartVectorEnrichmentJobOutput":
        """<p>Creates a Vector Enrichment job for the supplied job type. Currently, there are two supported job types: reverse geocoding and map matching.</p>

        Args:
            name: <p>The name of the Vector Enrichment job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            kms_key_id: <p>The Key Management Service key ID for server-side encryption.</p>
            input_config: <p>Input configuration information for the Vector Enrichment job.</p>
            job_config: <p>An object containing information about the job configuration.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            tags: <p>Each tag consists of a key and a value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.start_vector_enrichment_job_input.StartVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.start_vector_enrichment_job_output.StartVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.start_vector_enrichment_job

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.start_vector_enrichment_job.start_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.start_vector_enrichment_job_input.StartVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if client_token is not None:
            input["client_token"] = client_token
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        input["input_config"] = input_config
        input["job_config"] = job_config
        input["execution_role_arn"] = execution_role_arn
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.get_vector_enrichment_job_output.GetVectorEnrichmentJobOutput":
        """<p>Retrieves details of a Vector Enrichment Job for a given job Amazon Resource Name (ARN).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.get_vector_enrichment_job_input.GetVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.get_vector_enrichment_job_output.GetVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_vector_enrichment_job

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_vector_enrichment_job.get_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.get_vector_enrichment_job_input.GetVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.delete_vector_enrichment_job_output.DeleteVectorEnrichmentJobOutput":
        """<p>Use this operation to delete a Vector Enrichment job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job being deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.delete_vector_enrichment_job_input.DeleteVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.delete_vector_enrichment_job_output.DeleteVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.delete_vector_enrichment_job

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.delete_vector_enrichment_job.delete_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.delete_vector_enrichment_job_input.DeleteVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        status_equals: Optional[str] = None,
        sort_order: Optional[
            "aws_sdk_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "aws_sdk_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput":
        """<p>Retrieves a list of vector enrichment jobs.</p>

        Args:
            status_equals: <p>A filter that retrieves only jobs with a specific status.</p>
            sort_order: <p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>
            sort_by: <p>The parameter by which to sort the results.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The maximum number of items to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_vector_enrichment_jobs

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_vector_enrichment_jobs.list_vector_enrichment_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        if status_equals is not None:
            input["status_equals"] = status_equals
        if sort_order is not None:
            input["sort_order"] = sort_order
        if sort_by is not None:
            input["sort_by"] = sort_by
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def export_vector_enrichment_job(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        execution_role_arn: "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        output_config: "aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.ExportVectorEnrichmentJobOutputConfig",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_output.ExportVectorEnrichmentJobOutput":
        """<p>Use this operation to copy results of a Vector Enrichment job to an Amazon S3 location.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM rolewith permission to upload to the location in OutputConfig.</p>
            output_config: <p>Output location information for exporting Vector Enrichment Job results. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_input.ExportVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_output.ExportVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.export_vector_enrichment_job

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.export_vector_enrichment_job.export_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_input.ExportVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        if client_token is not None:
            input["client_token"] = client_token
        input["execution_role_arn"] = execution_role_arn
        input["output_config"] = output_config

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_vector_enrichment_job(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.stop_vector_enrichment_job_output.StopVectorEnrichmentJobOutput":
        """<p>Stops the Vector Enrichment job for a given job ARN.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.stop_vector_enrichment_job_input.StopVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.stop_vector_enrichment_job_output.StopVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.stop_vector_enrichment_job

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.stop_vector_enrichment_job.stop_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.stop_vector_enrichment_job_input.StopVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncVectorEnrichmentJob:
    def __init__(self, service: AsyncSageMakerGeospatialClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        input_config: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_input_config.VectorEnrichmentJobInputConfig",
        job_config: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_config.VectorEnrichmentJobConfig",
        execution_role_arn: "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        kms_key_id: Optional[
            "aws_sdk_sagemaker_geospatial.types.kms_key.KmsKey"
        ] = None,
        tags: Optional["aws_sdk_sagemaker_geospatial.types.tags.Tags"] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.start_vector_enrichment_job_output.StartVectorEnrichmentJobOutput":
        """<p>Creates a Vector Enrichment job for the supplied job type. Currently, there are two supported job types: reverse geocoding and map matching.</p>

        Args:
            name: <p>The name of the Vector Enrichment job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            kms_key_id: <p>The Key Management Service key ID for server-side encryption.</p>
            input_config: <p>Input configuration information for the Vector Enrichment job.</p>
            job_config: <p>An object containing information about the job configuration.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            tags: <p>Each tag consists of a key and a value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.start_vector_enrichment_job_input.StartVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.start_vector_enrichment_job_output.StartVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.start_vector_enrichment_job

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.start_vector_enrichment_job.async_start_vector_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.start_vector_enrichment_job_input.StartVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if client_token is not None:
            input["client_token"] = client_token
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        input["input_config"] = input_config
        input["job_config"] = job_config
        input["execution_role_arn"] = execution_role_arn
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.get_vector_enrichment_job_output.GetVectorEnrichmentJobOutput":
        """<p>Retrieves details of a Vector Enrichment Job for a given job Amazon Resource Name (ARN).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.get_vector_enrichment_job_input.GetVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.get_vector_enrichment_job_output.GetVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_vector_enrichment_job

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_vector_enrichment_job.async_get_vector_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.get_vector_enrichment_job_input.GetVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.delete_vector_enrichment_job_output.DeleteVectorEnrichmentJobOutput":
        """<p>Use this operation to delete a Vector Enrichment job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job being deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.delete_vector_enrichment_job_input.DeleteVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.delete_vector_enrichment_job_output.DeleteVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.delete_vector_enrichment_job

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.delete_vector_enrichment_job.async_delete_vector_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.delete_vector_enrichment_job_input.DeleteVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        status_equals: Optional[str] = None,
        sort_order: Optional[
            "aws_sdk_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "aws_sdk_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput":
        """<p>Retrieves a list of vector enrichment jobs.</p>

        Args:
            status_equals: <p>A filter that retrieves only jobs with a specific status.</p>
            sort_order: <p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>
            sort_by: <p>The parameter by which to sort the results.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The maximum number of items to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_vector_enrichment_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_vector_enrichment_jobs.async_list_vector_enrichment_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        if status_equals is not None:
            input["status_equals"] = status_equals
        if sort_order is not None:
            input["sort_order"] = sort_order
        if sort_by is not None:
            input["sort_by"] = sort_by
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def export_vector_enrichment_job(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        execution_role_arn: "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        output_config: "aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.ExportVectorEnrichmentJobOutputConfig",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_output.ExportVectorEnrichmentJobOutput":
        """<p>Use this operation to copy results of a Vector Enrichment job to an Amazon S3 location.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM rolewith permission to upload to the location in OutputConfig.</p>
            output_config: <p>Output location information for exporting Vector Enrichment Job results. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_input.ExportVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_output.ExportVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.export_vector_enrichment_job

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.export_vector_enrichment_job.async_export_vector_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.export_vector_enrichment_job_input.ExportVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        if client_token is not None:
            input["client_token"] = client_token
        input["execution_role_arn"] = execution_role_arn
        input["output_config"] = output_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_vector_enrichment_job(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.stop_vector_enrichment_job_output.StopVectorEnrichmentJobOutput":
        """<p>Stops the Vector Enrichment job for a given job ARN.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.stop_vector_enrichment_job_input.StopVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.stop_vector_enrichment_job_output.StopVectorEnrichmentJobOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.stop_vector_enrichment_job

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.stop_vector_enrichment_job.async_stop_vector_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_sagemaker_geospatial.types.stop_vector_enrichment_job_input.StopVectorEnrichmentJobInput = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
