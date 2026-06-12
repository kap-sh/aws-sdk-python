from typing import TYPE_CHECKING, Optional

from aws_sdk_partnercentral_selling._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.client_token
    import aws_sdk_partnercentral_selling.types.create_resource_snapshot_job_request
    import aws_sdk_partnercentral_selling.types.create_resource_snapshot_job_response
    import aws_sdk_partnercentral_selling.types.delete_resource_snapshot_job_request
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.get_resource_snapshot_job_request
    import aws_sdk_partnercentral_selling.types.get_resource_snapshot_job_response
    import aws_sdk_partnercentral_selling.types.list_resource_snapshot_jobs_request
    import aws_sdk_partnercentral_selling.types.list_resource_snapshot_jobs_response
    import aws_sdk_partnercentral_selling.types.page_size
    import aws_sdk_partnercentral_selling.types.resource_identifier
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_status
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_summary
    import aws_sdk_partnercentral_selling.types.resource_template_name
    import aws_sdk_partnercentral_selling.types.resource_type
    import aws_sdk_partnercentral_selling.types.sort_object
    import aws_sdk_partnercentral_selling.types.start_resource_snapshot_job_request
    import aws_sdk_partnercentral_selling.types.stop_resource_snapshot_job_request
    import aws_sdk_partnercentral_selling.types.tag_list
    from aws_sdk_partnercentral_selling._services.async_partner_central_selling import (
        AsyncPartnerCentralSellingClient,
        AsyncPartnerCentralSellingClientConfig,
    )
    from aws_sdk_partnercentral_selling._services.partner_central_selling import (
        PartnerCentralSellingClient,
        PartnerCentralSellingClientConfig,
    )


class ResourceSnapshotJob:
    def __init__(self, service: PartnerCentralSellingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "aws_sdk_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        tags: Optional["aws_sdk_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_selling.types.create_resource_snapshot_job_response.CreateResourceSnapshotJobResponse":
        """<p>Use this action to create a job to generate a snapshot of the specified resource within an engagement. It initiates an asynchronous process to create a resource snapshot. The job creates a new snapshot only if the resource state has changed, adhering to the same access control and immutability rules as direct snapshot creation.</p>

        Args:
            catalog: <p>Specifies the catalog in which to create the snapshot job. Valid values are <code>AWS</code> and <code> Sandbox</code>.</p>
            client_token: <p>A client-generated UUID used for idempotency check. The token helps prevent duplicate job creations.</p>
            engagement_identifier: <p>Specifies the identifier of the engagement associated with the resource to be snapshotted.</p>
            resource_type: <p>The type of resource for which the snapshot job is being created. Must be one of the supported resource types i.e. <code>Opportunity</code> </p>
            resource_identifier: <p>Specifies the identifier of the specific resource to be snapshotted. The format depends on the <code> ResourceType</code>.</p>
            resource_snapshot_template_identifier: <p>Specifies the name of the template that defines the schema for the snapshot.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.create_resource_snapshot_job_request.CreateResourceSnapshotJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.create_resource_snapshot_job_response.CreateResourceSnapshotJobResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot_job

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot_job.create_resource_snapshot_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.create_resource_snapshot_job_request.CreateResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["client_token"] = client_token
        input["engagement_identifier"] = engagement_identifier
        input["resource_type"] = resource_type
        input["resource_identifier"] = resource_identifier
        input["resource_snapshot_template_identifier"] = (
            resource_snapshot_template_identifier
        )
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
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.get_resource_snapshot_job_response.GetResourceSnapshotJobResponse":
        """<p>Use this action to retrieves information about a specific resource snapshot job.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p> AWS: Retrieves the snapshot job from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the snapshot job from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            resource_snapshot_job_identifier: <p>The unique identifier of the resource snapshot job to be retrieved. This identifier is crucial for pinpointing the specific job you want to query. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.get_resource_snapshot_job_request.GetResourceSnapshotJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.get_resource_snapshot_job_response.GetResourceSnapshotJobResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot_job

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot_job.get_resource_snapshot_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.get_resource_snapshot_job_request.GetResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["resource_snapshot_job_identifier"] = resource_snapshot_job_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p> Use this action to deletes a previously created resource snapshot job. The job must be in a stopped state before it can be deleted. </p>

        Args:
            catalog: <p> Specifies the catalog from which to delete the snapshot job. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>
            resource_snapshot_job_identifier: <p> The unique identifier of the resource snapshot job to be deleted. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.delete_resource_snapshot_job_request.DeleteResourceSnapshotJobRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.delete_resource_snapshot_job

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.delete_resource_snapshot_job.delete_resource_snapshot_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.delete_resource_snapshot_job_request.DeleteResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["resource_snapshot_job_identifier"] = resource_snapshot_job_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_selling.types.resource_snapshot_job_status.ResourceSnapshotJobStatus"
        ] = None,
        sort: Optional[
            "aws_sdk_partnercentral_selling.types.sort_object.SortObject"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_resource_snapshot_jobs_response.ListResourceSnapshotJobsResponse":
        """<p> Lists resource snapshot jobs owned by the customer. This operation supports various filtering scenarios, including listing all jobs owned by the caller, jobs for a specific engagement, jobs with a specific status, or any combination of these filters. </p>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            max_results: <p> The maximum number of results to return in a single call. If omitted, defaults to 50. </p>
            next_token: <p> The token for the next set of results. </p>
            engagement_identifier: <p> The identifier of the engagement to filter the response. </p>
            status: <p> The status of the jobs to filter the response. </p>
            sort: <p> Configures the sorting of the response. If omitted, results are sorted by <code>CreatedDate</code> in descending order. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.list_resource_snapshot_jobs_request.ListResourceSnapshotJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.list_resource_snapshot_jobs_response.ListResourceSnapshotJobsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshot_jobs

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshot_jobs.list_resource_snapshot_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.list_resource_snapshot_jobs_request.ListResourceSnapshotJobsRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if engagement_identifier is not None:
            input["engagement_identifier"] = engagement_identifier
        if status is not None:
            input["status"] = status
        if sort is not None:
            input["sort"] = sort

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_resource_snapshot_job(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Starts a resource snapshot job that has been previously created.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Starts the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Starts the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            resource_snapshot_job_identifier: <p>The identifier of the resource snapshot job to start.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.start_resource_snapshot_job_request.StartResourceSnapshotJobRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_resource_snapshot_job

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_resource_snapshot_job.start_resource_snapshot_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.start_resource_snapshot_job_request.StartResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["resource_snapshot_job_identifier"] = resource_snapshot_job_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_resource_snapshot_job(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Stops a resource snapshot job. The job must be started prior to being stopped.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Stops the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Stops the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            resource_snapshot_job_identifier: <p>The identifier of the job to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.stop_resource_snapshot_job_request.StopResourceSnapshotJobRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.stop_resource_snapshot_job

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.stop_resource_snapshot_job.stop_resource_snapshot_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.stop_resource_snapshot_job_request.StopResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["resource_snapshot_job_identifier"] = resource_snapshot_job_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncResourceSnapshotJob:
    def __init__(self, service: AsyncPartnerCentralSellingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier",
        resource_type: "aws_sdk_partnercentral_selling.types.resource_type.ResourceType",
        resource_identifier: "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier",
        resource_snapshot_template_identifier: "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        tags: Optional["aws_sdk_partnercentral_selling.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_partnercentral_selling.types.create_resource_snapshot_job_response.CreateResourceSnapshotJobResponse":
        """<p>Use this action to create a job to generate a snapshot of the specified resource within an engagement. It initiates an asynchronous process to create a resource snapshot. The job creates a new snapshot only if the resource state has changed, adhering to the same access control and immutability rules as direct snapshot creation.</p>

        Args:
            catalog: <p>Specifies the catalog in which to create the snapshot job. Valid values are <code>AWS</code> and <code> Sandbox</code>.</p>
            client_token: <p>A client-generated UUID used for idempotency check. The token helps prevent duplicate job creations.</p>
            engagement_identifier: <p>Specifies the identifier of the engagement associated with the resource to be snapshotted.</p>
            resource_type: <p>The type of resource for which the snapshot job is being created. Must be one of the supported resource types i.e. <code>Opportunity</code> </p>
            resource_identifier: <p>Specifies the identifier of the specific resource to be snapshotted. The format depends on the <code> ResourceType</code>.</p>
            resource_snapshot_template_identifier: <p>Specifies the name of the template that defines the schema for the snapshot.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.create_resource_snapshot_job_request.CreateResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.create_resource_snapshot_job_response.CreateResourceSnapshotJobResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot_job

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_resource_snapshot_job.async_create_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.create_resource_snapshot_job_request.CreateResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["client_token"] = client_token
        input["engagement_identifier"] = engagement_identifier
        input["resource_type"] = resource_type
        input["resource_identifier"] = resource_identifier
        input["resource_snapshot_template_identifier"] = (
            resource_snapshot_template_identifier
        )
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
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.get_resource_snapshot_job_response.GetResourceSnapshotJobResponse":
        """<p>Use this action to retrieves information about a specific resource snapshot job.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p> AWS: Retrieves the snapshot job from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the snapshot job from a sandbox environment used for testing or development purposes. </p> </li> </ul>
            resource_snapshot_job_identifier: <p>The unique identifier of the resource snapshot job to be retrieved. This identifier is crucial for pinpointing the specific job you want to query. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.get_resource_snapshot_job_request.GetResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.get_resource_snapshot_job_response.GetResourceSnapshotJobResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot_job

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_resource_snapshot_job.async_get_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.get_resource_snapshot_job_request.GetResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["resource_snapshot_job_identifier"] = resource_snapshot_job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p> Use this action to deletes a previously created resource snapshot job. The job must be in a stopped state before it can be deleted. </p>

        Args:
            catalog: <p> Specifies the catalog from which to delete the snapshot job. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>
            resource_snapshot_job_identifier: <p> The unique identifier of the resource snapshot job to be deleted. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.delete_resource_snapshot_job_request.DeleteResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.delete_resource_snapshot_job

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.delete_resource_snapshot_job.async_delete_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.delete_resource_snapshot_job_request.DeleteResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["resource_snapshot_job_identifier"] = resource_snapshot_job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_partnercentral_selling.types.page_size.PageSize"
        ] = None,
        next_token: Optional[str] = None,
        engagement_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
        ] = None,
        status: Optional[
            "aws_sdk_partnercentral_selling.types.resource_snapshot_job_status.ResourceSnapshotJobStatus"
        ] = None,
        sort: Optional[
            "aws_sdk_partnercentral_selling.types.sort_object.SortObject"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_resource_snapshot_jobs_response.ListResourceSnapshotJobsResponse":
        """<p> Lists resource snapshot jobs owned by the customer. This operation supports various filtering scenarios, including listing all jobs owned by the caller, jobs for a specific engagement, jobs with a specific status, or any combination of these filters. </p>

        Args:
            catalog: <p> Specifies the catalog related to the request. </p>
            max_results: <p> The maximum number of results to return in a single call. If omitted, defaults to 50. </p>
            next_token: <p> The token for the next set of results. </p>
            engagement_identifier: <p> The identifier of the engagement to filter the response. </p>
            status: <p> The status of the jobs to filter the response. </p>
            sort: <p> Configures the sorting of the response. If omitted, results are sorted by <code>CreatedDate</code> in descending order. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.list_resource_snapshot_jobs_request.ListResourceSnapshotJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_selling.types.list_resource_snapshot_jobs_response.ListResourceSnapshotJobsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshot_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_resource_snapshot_jobs.async_list_resource_snapshot_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.list_resource_snapshot_jobs_request.ListResourceSnapshotJobsRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if engagement_identifier is not None:
            input["engagement_identifier"] = engagement_identifier
        if status is not None:
            input["status"] = status
        if sort is not None:
            input["sort"] = sort

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_resource_snapshot_job(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Starts a resource snapshot job that has been previously created.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Starts the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Starts the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            resource_snapshot_job_identifier: <p>The identifier of the resource snapshot job to start.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.start_resource_snapshot_job_request.StartResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_resource_snapshot_job

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.start_resource_snapshot_job.async_start_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.start_resource_snapshot_job_request.StartResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["resource_snapshot_job_identifier"] = resource_snapshot_job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_resource_snapshot_job(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        resource_snapshot_job_identifier: "aws_sdk_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralSellingClientConfig] = None,
    ) -> None:
        """<p>Stops a resource snapshot job. The job must be started prior to being stopped.</p>

        Args:
            catalog: <p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Stops the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Stops the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>
            resource_snapshot_job_identifier: <p>The identifier of the job to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_selling.types.stop_resource_snapshot_job_request.StopResourceSnapshotJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.stop_resource_snapshot_job

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.stop_resource_snapshot_job.async_stop_resource_snapshot_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.stop_resource_snapshot_job_request.StopResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["resource_snapshot_job_identifier"] = resource_snapshot_job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
