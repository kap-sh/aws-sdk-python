from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_backupsearch._auth._signers
import aws_sdk_backupsearch._auth._sigv4
from aws_sdk_backupsearch._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.encryption_key_arn
    import aws_sdk_backupsearch.types.generic_id
    import aws_sdk_backupsearch.types.get_search_job_input
    import aws_sdk_backupsearch.types.get_search_job_output
    import aws_sdk_backupsearch.types.item_filters
    import aws_sdk_backupsearch.types.list_search_jobs_input
    import aws_sdk_backupsearch.types.list_search_jobs_output
    import aws_sdk_backupsearch.types.search_job_state
    import aws_sdk_backupsearch.types.search_scope
    import aws_sdk_backupsearch.types.start_search_job_input
    import aws_sdk_backupsearch.types.start_search_job_output
    import aws_sdk_backupsearch.types.stop_search_job_input
    import aws_sdk_backupsearch.types.stop_search_job_output
    import aws_sdk_backupsearch.types.tag_map
    from aws_sdk_backupsearch._services.async_backup_search import (
        AsyncBackupSearchClient,
        AsyncBackupSearchClientConfig,
    )
    from aws_sdk_backupsearch._services.backup_search import (
        BackupSearchClient,
        BackupSearchClientConfig,
    )


class SearchJob:
    def __init__(self, service: BackupSearchClient) -> None:
        self._service = service

    def create(
        self,
        search_scope: "aws_sdk_backupsearch.types.search_scope.SearchScope",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
        tags: Optional["aws_sdk_backupsearch.types.tag_map.TagMap"] = None,
        name: Optional[str] = None,
        encryption_key_arn: Optional[
            "aws_sdk_backupsearch.types.encryption_key_arn.EncryptionKeyArn"
        ] = None,
        client_token: Optional[str] = None,
        item_filters: Optional[
            "aws_sdk_backupsearch.types.item_filters.ItemFilters"
        ] = None,
    ) -> "aws_sdk_backupsearch.types.start_search_job_output.StartSearchJobOutput":
        """<p>This operation creates a search job which returns recovery points filtered by SearchScope and items filtered by ItemFilters.</p> <p>You can optionally include ClientToken, EncryptionKeyArn, Name, and/or Tags.</p>

        Args:
            tags: <p>List of tags returned by the operation.</p>
            name: <p>Include alphanumeric characters to create a name for this search job.</p>
            encryption_key_arn: <p>The encryption key for the specified search job.</p>
            client_token: <p>Include this parameter to allow multiple identical calls for idempotency.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.</p>
            search_scope: <p>This object can contain BackupResourceTypes, BackupResourceArns, BackupResourceCreationTime, BackupResourceTags, and SourceResourceArns to filter the recovery points returned by the search job.</p>
            item_filters: <p>Item Filters represent all input item properties specified when the search was created.</p> <p>Contains either EBSItemFilters or S3ItemFilters</p>

        Raises:
            aws_sdk_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            aws_sdk_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            aws_sdk_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            aws_sdk_backupsearch.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request denied due to exceeding the quota limits permitted.</p>
            aws_sdk_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backupsearch.types.start_search_job_input.StartSearchJobInput]",
        ) -> OperationResponse[
            "aws_sdk_backupsearch.types.start_search_job_output.StartSearchJobOutput"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.start_search_job

            output, http_response = (
                aws_sdk_backupsearch._operations.cryo_backup_search_service.start_search_job.start_search_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backupsearch.types.start_search_job_input.StartSearchJobInput = {}  # type: ignore[typeddict-item]
        if tags is not None:
            input_["tags"] = tags
        if name is not None:
            input_["name"] = name
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["search_scope"] = search_scope
        if item_filters is not None:
            input_["item_filters"] = item_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        search_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
    ) -> "aws_sdk_backupsearch.types.get_search_job_output.GetSearchJobOutput":
        """<p>This operation retrieves metadata of a search job, including its progress.</p>

        Args:
            search_job_identifier: <p>Required unique string that specifies the search job.</p>

        Raises:
            aws_sdk_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            aws_sdk_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            aws_sdk_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backupsearch.types.get_search_job_input.GetSearchJobInput]",
        ) -> OperationResponse[
            "aws_sdk_backupsearch.types.get_search_job_output.GetSearchJobOutput"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.get_search_job

            output, http_response = (
                aws_sdk_backupsearch._operations.cryo_backup_search_service.get_search_job.get_search_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backupsearch.types.get_search_job_input.GetSearchJobInput = {}  # type: ignore[typeddict-item]
        input_["search_job_identifier"] = search_job_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        search_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
    ) -> "aws_sdk_backupsearch.types.stop_search_job_output.StopSearchJobOutput":
        """<p>This operations ends a search job.</p> <p>Only a search job with a status of <code>RUNNING</code> can be stopped.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>

        Raises:
            aws_sdk_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            aws_sdk_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            aws_sdk_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            aws_sdk_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backupsearch.types.stop_search_job_input.StopSearchJobInput]",
        ) -> OperationResponse[
            "aws_sdk_backupsearch.types.stop_search_job_output.StopSearchJobOutput"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.stop_search_job

            output, http_response = (
                aws_sdk_backupsearch._operations.cryo_backup_search_service.stop_search_job.stop_search_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backupsearch.types.stop_search_job_input.StopSearchJobInput = {}  # type: ignore[typeddict-item]
        input_["search_job_identifier"] = search_job_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
        by_status: Optional[
            "aws_sdk_backupsearch.types.search_job_state.SearchJobState"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_backupsearch.types.list_search_jobs_output.ListSearchJobsOutput":
        """<p>This operation returns a list of search jobs belonging to an account.</p>

        Args:
            by_status: <p>Include this parameter to filter list by search job status.</p>
            next_token: <p>The next item following a partial list of returned search jobs.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            aws_sdk_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            aws_sdk_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backupsearch.types.list_search_jobs_input.ListSearchJobsInput]",
        ) -> OperationResponse[
            "aws_sdk_backupsearch.types.list_search_jobs_output.ListSearchJobsOutput"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.list_search_jobs

            output, http_response = (
                aws_sdk_backupsearch._operations.cryo_backup_search_service.list_search_jobs.list_search_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backupsearch.types.list_search_jobs_input.ListSearchJobsInput = {}  # type: ignore[typeddict-item]
        if by_status is not None:
            input_["by_status"] = by_status
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


class AsyncSearchJob:
    def __init__(self, service: AsyncBackupSearchClient) -> None:
        self._service = service

    async def create(
        self,
        search_scope: "aws_sdk_backupsearch.types.search_scope.SearchScope",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        tags: Optional["aws_sdk_backupsearch.types.tag_map.TagMap"] = None,
        name: Optional[str] = None,
        encryption_key_arn: Optional[
            "aws_sdk_backupsearch.types.encryption_key_arn.EncryptionKeyArn"
        ] = None,
        client_token: Optional[str] = None,
        item_filters: Optional[
            "aws_sdk_backupsearch.types.item_filters.ItemFilters"
        ] = None,
    ) -> "aws_sdk_backupsearch.types.start_search_job_output.StartSearchJobOutput":
        """<p>This operation creates a search job which returns recovery points filtered by SearchScope and items filtered by ItemFilters.</p> <p>You can optionally include ClientToken, EncryptionKeyArn, Name, and/or Tags.</p>

        Args:
            tags: <p>List of tags returned by the operation.</p>
            name: <p>Include alphanumeric characters to create a name for this search job.</p>
            encryption_key_arn: <p>The encryption key for the specified search job.</p>
            client_token: <p>Include this parameter to allow multiple identical calls for idempotency.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.</p>
            search_scope: <p>This object can contain BackupResourceTypes, BackupResourceArns, BackupResourceCreationTime, BackupResourceTags, and SourceResourceArns to filter the recovery points returned by the search job.</p>
            item_filters: <p>Item Filters represent all input item properties specified when the search was created.</p> <p>Contains either EBSItemFilters or S3ItemFilters</p>

        Raises:
            aws_sdk_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            aws_sdk_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            aws_sdk_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            aws_sdk_backupsearch.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request denied due to exceeding the quota limits permitted.</p>
            aws_sdk_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backupsearch.types.start_search_job_input.StartSearchJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backupsearch.types.start_search_job_output.StartSearchJobOutput"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.start_search_job

            (
                output,
                http_response,
            ) = await aws_sdk_backupsearch._operations.cryo_backup_search_service.start_search_job.async_start_search_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backupsearch.types.start_search_job_input.StartSearchJobInput = {}  # type: ignore[typeddict-item]
        if tags is not None:
            input_["tags"] = tags
        if name is not None:
            input_["name"] = name
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if client_token is not None:
            input_["client_token"] = client_token
        input_["search_scope"] = search_scope
        if item_filters is not None:
            input_["item_filters"] = item_filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        search_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "aws_sdk_backupsearch.types.get_search_job_output.GetSearchJobOutput":
        """<p>This operation retrieves metadata of a search job, including its progress.</p>

        Args:
            search_job_identifier: <p>Required unique string that specifies the search job.</p>

        Raises:
            aws_sdk_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            aws_sdk_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            aws_sdk_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backupsearch.types.get_search_job_input.GetSearchJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backupsearch.types.get_search_job_output.GetSearchJobOutput"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.get_search_job

            (
                output,
                http_response,
            ) = await aws_sdk_backupsearch._operations.cryo_backup_search_service.get_search_job.async_get_search_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backupsearch.types.get_search_job_input.GetSearchJobInput = {}  # type: ignore[typeddict-item]
        input_["search_job_identifier"] = search_job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        search_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "aws_sdk_backupsearch.types.stop_search_job_output.StopSearchJobOutput":
        """<p>This operations ends a search job.</p> <p>Only a search job with a status of <code>RUNNING</code> can be stopped.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>

        Raises:
            aws_sdk_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            aws_sdk_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            aws_sdk_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            aws_sdk_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backupsearch.types.stop_search_job_input.StopSearchJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backupsearch.types.stop_search_job_output.StopSearchJobOutput"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.stop_search_job

            (
                output,
                http_response,
            ) = await aws_sdk_backupsearch._operations.cryo_backup_search_service.stop_search_job.async_stop_search_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backupsearch.types.stop_search_job_input.StopSearchJobInput = {}  # type: ignore[typeddict-item]
        input_["search_job_identifier"] = search_job_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        by_status: Optional[
            "aws_sdk_backupsearch.types.search_job_state.SearchJobState"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_backupsearch.types.list_search_jobs_output.ListSearchJobsOutput":
        """<p>This operation returns a list of search jobs belonging to an account.</p>

        Args:
            by_status: <p>Include this parameter to filter list by search job status.</p>
            next_token: <p>The next item following a partial list of returned search jobs.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            aws_sdk_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            aws_sdk_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backupsearch.types.list_search_jobs_input.ListSearchJobsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backupsearch.types.list_search_jobs_output.ListSearchJobsOutput"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.list_search_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_backupsearch._operations.cryo_backup_search_service.list_search_jobs.async_list_search_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backupsearch.types.list_search_jobs_input.ListSearchJobsInput = {}  # type: ignore[typeddict-item]
        if by_status is not None:
            input_["by_status"] = by_status
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
