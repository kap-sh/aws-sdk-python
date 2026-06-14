from typing import TYPE_CHECKING, Optional

import aws_sdk_omics._auth._signers
import aws_sdk_omics._auth._sigv4
from aws_sdk_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_omics.types.client_token
    import aws_sdk_omics.types.create_reference_store_request
    import aws_sdk_omics.types.create_reference_store_response
    import aws_sdk_omics.types.delete_reference_store_request
    import aws_sdk_omics.types.delete_reference_store_response
    import aws_sdk_omics.types.get_reference_import_job_request
    import aws_sdk_omics.types.get_reference_import_job_response
    import aws_sdk_omics.types.get_reference_store_request
    import aws_sdk_omics.types.get_reference_store_response
    import aws_sdk_omics.types.import_job_id
    import aws_sdk_omics.types.import_reference_filter
    import aws_sdk_omics.types.import_reference_job_item
    import aws_sdk_omics.types.list_reference_import_jobs_request
    import aws_sdk_omics.types.list_reference_import_jobs_response
    import aws_sdk_omics.types.list_reference_stores_request
    import aws_sdk_omics.types.list_reference_stores_response
    import aws_sdk_omics.types.next_token
    import aws_sdk_omics.types.reference_store_description
    import aws_sdk_omics.types.reference_store_detail
    import aws_sdk_omics.types.reference_store_filter
    import aws_sdk_omics.types.reference_store_id
    import aws_sdk_omics.types.reference_store_name
    import aws_sdk_omics.types.role_arn
    import aws_sdk_omics.types.sse_config
    import aws_sdk_omics.types.start_reference_import_job_request
    import aws_sdk_omics.types.start_reference_import_job_response
    import aws_sdk_omics.types.start_reference_import_job_source_list
    import aws_sdk_omics.types.tag_map
    from aws_sdk_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from aws_sdk_omics._services.omics import OmicsClient, OmicsClientConfig


class ReferenceStoreResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_omics.types.reference_store_name.ReferenceStoreName",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional[
            "aws_sdk_omics.types.reference_store_description.ReferenceStoreDescription"
        ] = None,
        sse_config: Optional["aws_sdk_omics.types.sse_config.SseConfig"] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
        client_token: Optional["aws_sdk_omics.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_omics.types.create_reference_store_response.CreateReferenceStoreResponse":
        """<p>Creates a reference store and returns metadata in JSON format. Reference stores are used to store reference genomes in FASTA format. A reference store is created when the first reference genome is imported. To import additional reference genomes from an Amazon S3 bucket, use the <code>StartReferenceImportJob</code> API operation. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html\">Creating a HealthOmics reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            tags: <p>Tags for the store.</p>
            client_token: <p>To ensure that requests don't run multiple times, specify a unique token for each request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.create_reference_store_request.CreateReferenceStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.create_reference_store_response.CreateReferenceStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_reference_store

            output, http_response = (
                aws_sdk_omics._operations.omics.create_reference_store.create_reference_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.create_reference_store_request.CreateReferenceStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if tags is not None:
            input_["tags"] = tags
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
        id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_reference_store_response.GetReferenceStoreResponse":
        """<p>Gets information about a reference store.</p>

        Args:
            id: <p>The store's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.get_reference_store_request.GetReferenceStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.get_reference_store_response.GetReferenceStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_reference_store

            output, http_response = (
                aws_sdk_omics._operations.omics.get_reference_store.get_reference_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_reference_store_request.GetReferenceStoreRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.delete_reference_store_response.DeleteReferenceStoreResponse":
        """<p>Deletes a reference store and returns a response with no body if the operation is successful. You can only delete a reference store when it does not contain any reference genomes. To empty a reference store, use <code>DeleteReference</code>.</p> <p>For more information about your workflow status, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/deleting-reference-and-sequence-stores.html\">Deleting HealthOmics reference and sequence stores</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The store's ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.delete_reference_store_request.DeleteReferenceStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.delete_reference_store_response.DeleteReferenceStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_reference_store

            output, http_response = (
                aws_sdk_omics._operations.omics.delete_reference_store.delete_reference_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_reference_store_request.DeleteReferenceStoreRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "aws_sdk_omics.types.reference_store_filter.ReferenceStoreFilter"
        ] = None,
    ) -> (
        "aws_sdk_omics.types.list_reference_stores_response.ListReferenceStoresResponse"
    ):
        """<p>Retrieves a list of reference stores linked to your account and returns their metadata in JSON format.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html\">Creating a reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.list_reference_stores_request.ListReferenceStoresRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.list_reference_stores_response.ListReferenceStoresResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_reference_stores

            output, http_response = (
                aws_sdk_omics._operations.omics.list_reference_stores.list_reference_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_reference_stores_request.ListReferenceStoresRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_reference_import_job(
        self,
        id: "aws_sdk_omics.types.import_job_id.ImportJobId",
        reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_reference_import_job_response.GetReferenceImportJobResponse":
        """<p>Monitors the status of a reference import job. This operation can be called after calling the <code>StartReferenceImportJob</code> operation.</p>

        Args:
            id: <p>The job's ID.</p>
            reference_store_id: <p>The job's reference store ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.get_reference_import_job_request.GetReferenceImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.get_reference_import_job_response.GetReferenceImportJobResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_reference_import_job

            output, http_response = (
                aws_sdk_omics._operations.omics.get_reference_import_job.get_reference_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_reference_import_job_request.GetReferenceImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["reference_store_id"] = reference_store_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_reference_import_jobs(
        self,
        reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "aws_sdk_omics.types.import_reference_filter.ImportReferenceFilter"
        ] = None,
    ) -> "aws_sdk_omics.types.list_reference_import_jobs_response.ListReferenceImportJobsResponse":
        """<p>Retrieves the metadata of one or more reference import jobs for a reference store.</p>

        Args:
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            reference_store_id: <p>The job's reference store ID.</p>
            filter: <p>A filter to apply to the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.list_reference_import_jobs_request.ListReferenceImportJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.list_reference_import_jobs_response.ListReferenceImportJobsResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_reference_import_jobs

            output, http_response = (
                aws_sdk_omics._operations.omics.list_reference_import_jobs.list_reference_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_reference_import_jobs_request.ListReferenceImportJobsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["reference_store_id"] = reference_store_id
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_reference_import_job(
        self,
        reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId",
        role_arn: "aws_sdk_omics.types.role_arn.RoleArn",
        sources: "aws_sdk_omics.types.start_reference_import_job_source_list.StartReferenceImportJobSourceList",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        client_token: Optional["aws_sdk_omics.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_omics.types.start_reference_import_job_response.StartReferenceImportJobResponse":
        """<p>Imports a reference genome from Amazon S3 into a specified reference store. You can have multiple reference genomes in a reference store. You can only import reference genomes one at a time into each reference store. Monitor the status of your reference import job by using the <code>GetReferenceImportJob</code> API operation.</p>

        Args:
            reference_store_id: <p>The job's reference store ID.</p>
            role_arn: <p>A service role for the job.</p>
            client_token: <p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>
            sources: <p>The job's source files.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.start_reference_import_job_request.StartReferenceImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.start_reference_import_job_response.StartReferenceImportJobResponse"
        ]:
            import aws_sdk_omics._operations.omics.start_reference_import_job

            output, http_response = (
                aws_sdk_omics._operations.omics.start_reference_import_job.start_reference_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.start_reference_import_job_request.StartReferenceImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["reference_store_id"] = reference_store_id
        input_["role_arn"] = role_arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncReferenceStoreResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_omics.types.reference_store_name.ReferenceStoreName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional[
            "aws_sdk_omics.types.reference_store_description.ReferenceStoreDescription"
        ] = None,
        sse_config: Optional["aws_sdk_omics.types.sse_config.SseConfig"] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
        client_token: Optional["aws_sdk_omics.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_omics.types.create_reference_store_response.CreateReferenceStoreResponse":
        """<p>Creates a reference store and returns metadata in JSON format. Reference stores are used to store reference genomes in FASTA format. A reference store is created when the first reference genome is imported. To import additional reference genomes from an Amazon S3 bucket, use the <code>StartReferenceImportJob</code> API operation. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html\">Creating a HealthOmics reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            tags: <p>Tags for the store.</p>
            client_token: <p>To ensure that requests don't run multiple times, specify a unique token for each request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.create_reference_store_request.CreateReferenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.create_reference_store_response.CreateReferenceStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_reference_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.create_reference_store.async_create_reference_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.create_reference_store_request.CreateReferenceStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if tags is not None:
            input_["tags"] = tags
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
        id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_reference_store_response.GetReferenceStoreResponse":
        """<p>Gets information about a reference store.</p>

        Args:
            id: <p>The store's ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.get_reference_store_request.GetReferenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.get_reference_store_response.GetReferenceStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_reference_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.get_reference_store.async_get_reference_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_reference_store_request.GetReferenceStoreRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.delete_reference_store_response.DeleteReferenceStoreResponse":
        """<p>Deletes a reference store and returns a response with no body if the operation is successful. You can only delete a reference store when it does not contain any reference genomes. To empty a reference store, use <code>DeleteReference</code>.</p> <p>For more information about your workflow status, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/deleting-reference-and-sequence-stores.html\">Deleting HealthOmics reference and sequence stores</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The store's ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.delete_reference_store_request.DeleteReferenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.delete_reference_store_response.DeleteReferenceStoreResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_reference_store

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.delete_reference_store.async_delete_reference_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_reference_store_request.DeleteReferenceStoreRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "aws_sdk_omics.types.reference_store_filter.ReferenceStoreFilter"
        ] = None,
    ) -> (
        "aws_sdk_omics.types.list_reference_stores_response.ListReferenceStoresResponse"
    ):
        """<p>Retrieves a list of reference stores linked to your account and returns their metadata in JSON format.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html\">Creating a reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.list_reference_stores_request.ListReferenceStoresRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.list_reference_stores_response.ListReferenceStoresResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_reference_stores

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.list_reference_stores.async_list_reference_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_reference_stores_request.ListReferenceStoresRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_reference_import_job(
        self,
        id: "aws_sdk_omics.types.import_job_id.ImportJobId",
        reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_reference_import_job_response.GetReferenceImportJobResponse":
        """<p>Monitors the status of a reference import job. This operation can be called after calling the <code>StartReferenceImportJob</code> operation.</p>

        Args:
            id: <p>The job's ID.</p>
            reference_store_id: <p>The job's reference store ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.get_reference_import_job_request.GetReferenceImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.get_reference_import_job_response.GetReferenceImportJobResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_reference_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.get_reference_import_job.async_get_reference_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_reference_import_job_request.GetReferenceImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["reference_store_id"] = reference_store_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_reference_import_jobs(
        self,
        reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "aws_sdk_omics.types.import_reference_filter.ImportReferenceFilter"
        ] = None,
    ) -> "aws_sdk_omics.types.list_reference_import_jobs_response.ListReferenceImportJobsResponse":
        """<p>Retrieves the metadata of one or more reference import jobs for a reference store.</p>

        Args:
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            reference_store_id: <p>The job's reference store ID.</p>
            filter: <p>A filter to apply to the list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.list_reference_import_jobs_request.ListReferenceImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.list_reference_import_jobs_response.ListReferenceImportJobsResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_reference_import_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.list_reference_import_jobs.async_list_reference_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_reference_import_jobs_request.ListReferenceImportJobsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["reference_store_id"] = reference_store_id
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_reference_import_job(
        self,
        reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId",
        role_arn: "aws_sdk_omics.types.role_arn.RoleArn",
        sources: "aws_sdk_omics.types.start_reference_import_job_source_list.StartReferenceImportJobSourceList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["aws_sdk_omics.types.client_token.ClientToken"] = None,
    ) -> "aws_sdk_omics.types.start_reference_import_job_response.StartReferenceImportJobResponse":
        """<p>Imports a reference genome from Amazon S3 into a specified reference store. You can have multiple reference genomes in a reference store. You can only import reference genomes one at a time into each reference store. Monitor the status of your reference import job by using the <code>GetReferenceImportJob</code> API operation.</p>

        Args:
            reference_store_id: <p>The job's reference store ID.</p>
            role_arn: <p>A service role for the job.</p>
            client_token: <p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>
            sources: <p>The job's source files.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.start_reference_import_job_request.StartReferenceImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.start_reference_import_job_response.StartReferenceImportJobResponse"
        ]:
            import aws_sdk_omics._operations.omics.start_reference_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.start_reference_import_job.async_start_reference_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.start_reference_import_job_request.StartReferenceImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["reference_store_id"] = reference_store_id
        input_["role_arn"] = role_arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["sources"] = sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
