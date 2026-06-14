from typing import Optional, TYPE_CHECKING
from aws_sdk_datazone._services.async_data_zone import ensure_async_iterator
from aws_sdk_datazone._services.data_zone import ensure_sync_iterator
import datetime
from aws_sdk_datazone._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)
import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4

if TYPE_CHECKING:
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    import aws_sdk_datazone.types.cancel_metadata_generation_run_input
    import aws_sdk_datazone.types.cancel_metadata_generation_run_output
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_id
    import aws_sdk_datazone.types.get_metadata_generation_run_input
    import aws_sdk_datazone.types.get_metadata_generation_run_output
    import aws_sdk_datazone.types.list_metadata_generation_runs_input
    import aws_sdk_datazone.types.list_metadata_generation_runs_output
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.metadata_generation_run_identifier
    import aws_sdk_datazone.types.metadata_generation_run_item
    import aws_sdk_datazone.types.metadata_generation_run_status
    import aws_sdk_datazone.types.metadata_generation_run_target
    import aws_sdk_datazone.types.metadata_generation_run_type
    import aws_sdk_datazone.types.metadata_generation_run_types
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.start_metadata_generation_run_input
    import aws_sdk_datazone.types.start_metadata_generation_run_output


class MetadataGenerationRun:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        target: "aws_sdk_datazone.types.metadata_generation_run_target.MetadataGenerationRunTarget",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        type: Optional[
            "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        types: Optional[
            "aws_sdk_datazone.types.metadata_generation_run_types.MetadataGenerationRunTypes"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.start_metadata_generation_run_output.StartMetadataGenerationRunOutput":
        """<p>Starts the metadata generation run.</p> <p>Prerequisites:</p> <ul> <li> <p>Asset must be created and belong to the specified domain and project. </p> </li> <li> <p>Asset type must be supported for metadata generation (e.g., Amazon Web Services Glue table).</p> </li> <li> <p>Asset must have a structured schema with valid rows and columns.</p> </li> <li> <p>Valid values for --type: BUSINESS_DESCRIPTIONS, BUSINESS_NAMES, BUSINESS_GLOSSARY_ASSOCIATIONS.</p> </li> <li> <p>The user must have permission to run metadata generation in the domain/project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where you want to start a metadata generation run.</p>
            type: <p>The type of the metadata generation run.</p>
            types: <p>The types of the metadata generation run.</p>
            target: <p>The asset for which you want to start a metadata generation run.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
            owning_project_identifier: <p>The ID of the project that owns the asset for which you want to start a metadata generation run.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.start_metadata_generation_run_input.StartMetadataGenerationRunInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.start_metadata_generation_run_output.StartMetadataGenerationRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.start_metadata_generation_run

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.start_metadata_generation_run.start_metadata_generation_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.start_metadata_generation_run_input.StartMetadataGenerationRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if type is not None:
            input_["type"] = type
        if types is not None:
            input_["types"] = types
        input_["target"] = target
        if client_token is not None:
            input_["client_token"] = client_token
        input_["owning_project_identifier"] = owning_project_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        type: Optional[
            "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
    ) -> "aws_sdk_datazone.types.get_metadata_generation_run_output.GetMetadataGenerationRunOutput":
        """<p>Gets a metadata generation run in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Valid domain and run identifier. </p> </li> <li> <p>The metadata generation run must exist.</p> </li> <li> <p>User must have read access to the metadata run.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain the metadata generation run of which you want to get.</p>
            identifier: <p>The identifier of the metadata generation run.</p>
            type: <p>The type of the metadata generation run.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_metadata_generation_run_input.GetMetadataGenerationRunInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_metadata_generation_run_output.GetMetadataGenerationRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_metadata_generation_run

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_metadata_generation_run.get_metadata_generation_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_metadata_generation_run_input.GetMetadataGenerationRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.cancel_metadata_generation_run_output.CancelMetadataGenerationRunOutput":
        """<p>Cancels the metadata generation run.</p> <p>Prerequisites:</p> <ul> <li> <p>The run must exist and be in a cancelable status (e.g., SUBMITTED, IN_PROGRESS). </p> </li> <li> <p>Runs in SUCCEEDED status cannot be cancelled.</p> </li> <li> <p>User must have access to the run and cancel permissions.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the metadata generation run is to be cancelled.</p>
            identifier: <p>The ID of the metadata generation run.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.cancel_metadata_generation_run_input.CancelMetadataGenerationRunInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.cancel_metadata_generation_run_output.CancelMetadataGenerationRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.cancel_metadata_generation_run

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.cancel_metadata_generation_run.cancel_metadata_generation_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.cancel_metadata_generation_run_input.CancelMetadataGenerationRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        status: Optional[
            "aws_sdk_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
        ] = None,
        type: Optional[
            "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        target_identifier: Optional["aws_sdk_datazone.types.entity_id.EntityId"] = None,
    ) -> "aws_sdk_datazone.types.list_metadata_generation_runs_output.ListMetadataGenerationRunsOutput":
        """<p>Lists all metadata generation runs.</p> <p>Metadata generation runs represent automated processes that leverage AI/ML capabilities to create or enhance asset metadata at scale. This feature helps organizations maintain comprehensive and consistent metadata across large numbers of assets without manual intervention. It can automatically generate business descriptions, tags, and other metadata elements, significantly reducing the time and effort required for metadata management while improving consistency and completeness.</p> <p>Prerequisites:</p> <ul> <li> <p>Valid domain identifier. </p> </li> <li> <p>User must have access to metadata generation runs in the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where you want to list metadata generation runs.</p>
            status: <p>The status of the metadata generation runs.</p>
            type: <p>The type of the metadata generation runs.</p>
            next_token: <p>When the number of metadata generation runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of metadata generation runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>
            max_results: <p>The maximum number of metadata generation runs to return in a single call to ListMetadataGenerationRuns. When the number of metadata generation runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>
            target_identifier: <p>The target ID for which you want to list metadata generation runs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.list_metadata_generation_runs_input.ListMetadataGenerationRunsInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.list_metadata_generation_runs_output.ListMetadataGenerationRunsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_metadata_generation_runs

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.list_metadata_generation_runs.list_metadata_generation_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_metadata_generation_runs_input.ListMetadataGenerationRunsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncMetadataGenerationRun:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        target: "aws_sdk_datazone.types.metadata_generation_run_target.MetadataGenerationRunTarget",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type: Optional[
            "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        types: Optional[
            "aws_sdk_datazone.types.metadata_generation_run_types.MetadataGenerationRunTypes"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.start_metadata_generation_run_output.StartMetadataGenerationRunOutput":
        """<p>Starts the metadata generation run.</p> <p>Prerequisites:</p> <ul> <li> <p>Asset must be created and belong to the specified domain and project. </p> </li> <li> <p>Asset type must be supported for metadata generation (e.g., Amazon Web Services Glue table).</p> </li> <li> <p>Asset must have a structured schema with valid rows and columns.</p> </li> <li> <p>Valid values for --type: BUSINESS_DESCRIPTIONS, BUSINESS_NAMES, BUSINESS_GLOSSARY_ASSOCIATIONS.</p> </li> <li> <p>The user must have permission to run metadata generation in the domain/project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where you want to start a metadata generation run.</p>
            type: <p>The type of the metadata generation run.</p>
            types: <p>The types of the metadata generation run.</p>
            target: <p>The asset for which you want to start a metadata generation run.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
            owning_project_identifier: <p>The ID of the project that owns the asset for which you want to start a metadata generation run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.start_metadata_generation_run_input.StartMetadataGenerationRunInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.start_metadata_generation_run_output.StartMetadataGenerationRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.start_metadata_generation_run

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.start_metadata_generation_run.async_start_metadata_generation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.start_metadata_generation_run_input.StartMetadataGenerationRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if type is not None:
            input_["type"] = type
        if types is not None:
            input_["types"] = types
        input_["target"] = target
        if client_token is not None:
            input_["client_token"] = client_token
        input_["owning_project_identifier"] = owning_project_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type: Optional[
            "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
    ) -> "aws_sdk_datazone.types.get_metadata_generation_run_output.GetMetadataGenerationRunOutput":
        """<p>Gets a metadata generation run in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Valid domain and run identifier. </p> </li> <li> <p>The metadata generation run must exist.</p> </li> <li> <p>User must have read access to the metadata run.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain the metadata generation run of which you want to get.</p>
            identifier: <p>The identifier of the metadata generation run.</p>
            type: <p>The type of the metadata generation run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_metadata_generation_run_input.GetMetadataGenerationRunInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_metadata_generation_run_output.GetMetadataGenerationRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_metadata_generation_run

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_metadata_generation_run.async_get_metadata_generation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_metadata_generation_run_input.GetMetadataGenerationRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.cancel_metadata_generation_run_output.CancelMetadataGenerationRunOutput":
        """<p>Cancels the metadata generation run.</p> <p>Prerequisites:</p> <ul> <li> <p>The run must exist and be in a cancelable status (e.g., SUBMITTED, IN_PROGRESS). </p> </li> <li> <p>Runs in SUCCEEDED status cannot be cancelled.</p> </li> <li> <p>User must have access to the run and cancel permissions.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the metadata generation run is to be cancelled.</p>
            identifier: <p>The ID of the metadata generation run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.cancel_metadata_generation_run_input.CancelMetadataGenerationRunInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.cancel_metadata_generation_run_output.CancelMetadataGenerationRunOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.cancel_metadata_generation_run

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.cancel_metadata_generation_run.async_cancel_metadata_generation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.cancel_metadata_generation_run_input.CancelMetadataGenerationRunInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "aws_sdk_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
        ] = None,
        type: Optional[
            "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_datazone.types.max_results.MaxResults"] = None,
        target_identifier: Optional["aws_sdk_datazone.types.entity_id.EntityId"] = None,
    ) -> "aws_sdk_datazone.types.list_metadata_generation_runs_output.ListMetadataGenerationRunsOutput":
        """<p>Lists all metadata generation runs.</p> <p>Metadata generation runs represent automated processes that leverage AI/ML capabilities to create or enhance asset metadata at scale. This feature helps organizations maintain comprehensive and consistent metadata across large numbers of assets without manual intervention. It can automatically generate business descriptions, tags, and other metadata elements, significantly reducing the time and effort required for metadata management while improving consistency and completeness.</p> <p>Prerequisites:</p> <ul> <li> <p>Valid domain identifier. </p> </li> <li> <p>User must have access to metadata generation runs in the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where you want to list metadata generation runs.</p>
            status: <p>The status of the metadata generation runs.</p>
            type: <p>The type of the metadata generation runs.</p>
            next_token: <p>When the number of metadata generation runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of metadata generation runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>
            max_results: <p>The maximum number of metadata generation runs to return in a single call to ListMetadataGenerationRuns. When the number of metadata generation runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>
            target_identifier: <p>The target ID for which you want to list metadata generation runs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_metadata_generation_runs_input.ListMetadataGenerationRunsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_metadata_generation_runs_output.ListMetadataGenerationRunsOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_metadata_generation_runs

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_metadata_generation_runs.async_list_metadata_generation_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_metadata_generation_runs_input.ListMetadataGenerationRunsInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
