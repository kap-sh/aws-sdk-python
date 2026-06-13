from typing import TYPE_CHECKING, Optional

import aws_sdk_mgn._auth._signers
import aws_sdk_mgn._auth._sigv4
from aws_sdk_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.export_id
    import aws_sdk_mgn.types.export_task
    import aws_sdk_mgn.types.export_task_error
    import aws_sdk_mgn.types.list_export_errors_request
    import aws_sdk_mgn.types.list_export_errors_response
    import aws_sdk_mgn.types.list_exports_request
    import aws_sdk_mgn.types.list_exports_request_filters
    import aws_sdk_mgn.types.list_exports_response
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.s3_bucket_name
    import aws_sdk_mgn.types.s3_key
    import aws_sdk_mgn.types.start_export_request
    import aws_sdk_mgn.types.start_export_response
    import aws_sdk_mgn.types.tags_map
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from aws_sdk_mgn._services.mgn import mgnClient, mgnClientConfig


class ExportResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        s3_bucket: "aws_sdk_mgn.types.s3_bucket_name.S3BucketName",
        s3_key: "aws_sdk_mgn.types.s3_key.S3Key",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        s3_bucket_owner: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_mgn.types.start_export_response.StartExportResponse":
        """<p>Start export.</p>

        Args:
            s3_bucket: <p>Start export request s3 bucket.</p>
            s3_key: <p>Start export request s3key.</p>
            s3_bucket_owner: <p>Start export request s3 bucket owner.</p>
            tags: <p>Start import request tags.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.start_export_request.StartExportRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.start_export_response.StartExportResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_export

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.start_export.start_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.start_export_request.StartExportRequest = {}  # type: ignore[typeddict-item]
        input["s3_bucket"] = s3_bucket
        input["s3_key"] = s3_key
        if s3_bucket_owner is not None:
            input["s3_bucket_owner"] = s3_bucket_owner
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_exports_request_filters.ListExportsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_exports_response.ListExportsResponse":
        """<p>List exports.</p>

        Args:
            max_results: <p>List export request max results.</p>
            next_token: <p>List export request next token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_exports_request.ListExportsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_exports_response.ListExportsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_exports

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_exports.list_exports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.list_exports_request.ListExportsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_export_errors(
        self,
        export_id: "aws_sdk_mgn.types.export_id.ExportID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_export_errors_response.ListExportErrorsResponse":
        """<p>List export errors.</p>

        Args:
            export_id: <p>List export errors request export id.</p>
            max_results: <p>List export errors request max results.</p>
            next_token: <p>List export errors request next token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_export_errors_request.ListExportErrorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_export_errors_response.ListExportErrorsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_export_errors

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_export_errors.list_export_errors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.list_export_errors_request.ListExportErrorsRequest = {}  # type: ignore[typeddict-item]
        input["export_id"] = export_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncExportResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        s3_bucket: "aws_sdk_mgn.types.s3_bucket_name.S3BucketName",
        s3_key: "aws_sdk_mgn.types.s3_key.S3Key",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        s3_bucket_owner: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_mgn.types.start_export_response.StartExportResponse":
        """<p>Start export.</p>

        Args:
            s3_bucket: <p>Start export request s3 bucket.</p>
            s3_key: <p>Start export request s3key.</p>
            s3_bucket_owner: <p>Start export request s3 bucket owner.</p>
            tags: <p>Start import request tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.start_export_request.StartExportRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.start_export_response.StartExportResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_export

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.start_export.async_start_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.start_export_request.StartExportRequest = {}  # type: ignore[typeddict-item]
        input["s3_bucket"] = s3_bucket
        input["s3_key"] = s3_key
        if s3_bucket_owner is not None:
            input["s3_bucket_owner"] = s3_bucket_owner
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_exports_request_filters.ListExportsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_exports_response.ListExportsResponse":
        """<p>List exports.</p>

        Args:
            max_results: <p>List export request max results.</p>
            next_token: <p>List export request next token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_exports_request.ListExportsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_exports_response.ListExportsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_exports

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_exports.async_list_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.list_exports_request.ListExportsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_export_errors(
        self,
        export_id: "aws_sdk_mgn.types.export_id.ExportID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_export_errors_response.ListExportErrorsResponse":
        """<p>List export errors.</p>

        Args:
            export_id: <p>List export errors request export id.</p>
            max_results: <p>List export errors request max results.</p>
            next_token: <p>List export errors request next token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_export_errors_request.ListExportErrorsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_export_errors_response.ListExportErrorsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_export_errors

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_export_errors.async_list_export_errors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.list_export_errors_request.ListExportErrorsRequest = {}  # type: ignore[typeddict-item]
        input["export_id"] = export_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
