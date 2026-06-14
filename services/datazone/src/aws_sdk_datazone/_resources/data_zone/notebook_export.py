from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4
from aws_sdk_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.export_id
    import aws_sdk_datazone.types.file_format
    import aws_sdk_datazone.types.get_notebook_export_input
    import aws_sdk_datazone.types.get_notebook_export_output
    import aws_sdk_datazone.types.notebook_id
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.start_notebook_export_input
    import aws_sdk_datazone.types.start_notebook_export_output
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )


class NotebookExport:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        notebook_identifier: "aws_sdk_datazone.types.notebook_id.NotebookId",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        file_format: "aws_sdk_datazone.types.file_format.FileFormat",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_datazone.types.start_notebook_export_output.StartNotebookExportOutput"
    ):
        """<p>Starts a notebook export in Amazon SageMaker Unified Studio. This operation exports a notebook to a specified file format and stores the output in Amazon Simple Storage Service.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to export the notebook.</p>
            notebook_identifier: <p>The identifier of the notebook to export.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook.</p>
            file_format: <p>The file format for the notebook export. Valid values are <code>PDF</code> and <code>IPYNB</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.start_notebook_export_input.StartNotebookExportInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.start_notebook_export_output.StartNotebookExportOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.start_notebook_export

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.start_notebook_export.start_notebook_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.start_notebook_export_input.StartNotebookExportInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["notebook_identifier"] = notebook_identifier
        input_["owning_project_identifier"] = owning_project_identifier
        input_["file_format"] = file_format
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
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.export_id.ExportId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_notebook_export_output.GetNotebookExportOutput":
        """<p>Gets the details of a notebook export in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook export exists.</p>
            identifier: <p>The identifier of the notebook export.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_notebook_export_input.GetNotebookExportInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_notebook_export_output.GetNotebookExportOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_notebook_export

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_notebook_export.get_notebook_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_notebook_export_input.GetNotebookExportInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncNotebookExport:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        notebook_identifier: "aws_sdk_datazone.types.notebook_id.NotebookId",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        file_format: "aws_sdk_datazone.types.file_format.FileFormat",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_datazone.types.start_notebook_export_output.StartNotebookExportOutput"
    ):
        """<p>Starts a notebook export in Amazon SageMaker Unified Studio. This operation exports a notebook to a specified file format and stores the output in Amazon Simple Storage Service.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to export the notebook.</p>
            notebook_identifier: <p>The identifier of the notebook to export.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook.</p>
            file_format: <p>The file format for the notebook export. Valid values are <code>PDF</code> and <code>IPYNB</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.start_notebook_export_input.StartNotebookExportInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.start_notebook_export_output.StartNotebookExportOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.start_notebook_export

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.start_notebook_export.async_start_notebook_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.start_notebook_export_input.StartNotebookExportInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["notebook_identifier"] = notebook_identifier
        input_["owning_project_identifier"] = owning_project_identifier
        input_["file_format"] = file_format
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
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.export_id.ExportId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_notebook_export_output.GetNotebookExportOutput":
        """<p>Gets the details of a notebook export in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook export exists.</p>
            identifier: <p>The identifier of the notebook export.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_notebook_export_input.GetNotebookExportInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_notebook_export_output.GetNotebookExportOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_notebook_export

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_notebook_export.async_get_notebook_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_notebook_export_input.GetNotebookExportInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
