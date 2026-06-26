from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from aws_sdk_odb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database_backup_status
    import aws_sdk_odb.types.autonomous_database_backup_summary
    import aws_sdk_odb.types.autonomous_database_backup_type
    import aws_sdk_odb.types.create_autonomous_database_backup_input
    import aws_sdk_odb.types.create_autonomous_database_backup_output
    import aws_sdk_odb.types.delete_autonomous_database_backup_input
    import aws_sdk_odb.types.delete_autonomous_database_backup_output
    import aws_sdk_odb.types.general_input_string
    import aws_sdk_odb.types.get_autonomous_database_backup_input
    import aws_sdk_odb.types.get_autonomous_database_backup_output
    import aws_sdk_odb.types.list_autonomous_database_backups_input
    import aws_sdk_odb.types.list_autonomous_database_backups_output
    import aws_sdk_odb.types.request_tag_map
    import aws_sdk_odb.types.resource_display_name
    import aws_sdk_odb.types.resource_id
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.update_autonomous_database_backup_input
    import aws_sdk_odb.types.update_autonomous_database_backup_output
    from aws_sdk_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from aws_sdk_odb._services.odb import odbClient, odbClientConfig


class AutonomousDatabaseBackupResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def create(
        self,
        autonomous_database_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        display_name: Optional[
            "aws_sdk_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        retention_period_in_days: Optional[int] = None,
        client_token: Optional[
            "aws_sdk_odb.types.general_input_string.GeneralInputString"
        ] = None,
        tags: Optional["aws_sdk_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "aws_sdk_odb.types.create_autonomous_database_backup_output.CreateAutonomousDatabaseBackupOutput":
        """<p>Creates a new backup of the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to back up.</p>
            display_name: <p>The user-friendly name for the Autonomous Database backup.</p>
            retention_period_in_days: <p>The retention period, in days, for the Autonomous Database backup.</p>
            client_token: <p>A client-provided token to ensure the idempotency of the request.</p>
            tags: <p>The list of resource tags to apply to the Autonomous Database backup. Each tag is a key-value pair with no predefined name, type, or namespace.</p>

        Raises:
            aws_sdk_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            aws_sdk_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            aws_sdk_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            aws_sdk_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            aws_sdk_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            aws_sdk_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            aws_sdk_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.create_autonomous_database_backup_input.CreateAutonomousDatabaseBackupInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.create_autonomous_database_backup_output.CreateAutonomousDatabaseBackupOutput"
        ]:
            import aws_sdk_odb._operations.odb.create_autonomous_database_backup

            output, http_response = (
                aws_sdk_odb._operations.odb.create_autonomous_database_backup.create_autonomous_database_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.create_autonomous_database_backup_input.CreateAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
        input_["autonomous_database_id"] = autonomous_database_id
        if display_name is not None:
            input_["display_name"] = display_name
        if retention_period_in_days is not None:
            input_["retention_period_in_days"] = retention_period_in_days
        if client_token is not None:
            input_["client_token"] = client_token
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
        autonomous_database_backup_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.get_autonomous_database_backup_output.GetAutonomousDatabaseBackupOutput":
        """<p>Gets information about a specific Autonomous Database backup.</p>

        Args:
            autonomous_database_backup_id: <p>The unique identifier of the Autonomous Database backup to retrieve information about.</p>

        Raises:
            aws_sdk_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            aws_sdk_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            aws_sdk_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            aws_sdk_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            aws_sdk_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.get_autonomous_database_backup_input.GetAutonomousDatabaseBackupInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.get_autonomous_database_backup_output.GetAutonomousDatabaseBackupOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_autonomous_database_backup

            output, http_response = (
                aws_sdk_odb._operations.odb.get_autonomous_database_backup.get_autonomous_database_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_autonomous_database_backup_input.GetAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
        input_["autonomous_database_backup_id"] = autonomous_database_backup_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        autonomous_database_backup_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        retention_period_in_days: Optional[int] = None,
    ) -> "aws_sdk_odb.types.update_autonomous_database_backup_output.UpdateAutonomousDatabaseBackupOutput":
        """<p>Updates the properties of an Autonomous Database backup.</p>

        Args:
            autonomous_database_backup_id: <p>The unique identifier of the Autonomous Database backup to update.</p>
            retention_period_in_days: <p>The retention period, in days, for the Autonomous Database backup.</p>

        Raises:
            aws_sdk_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            aws_sdk_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            aws_sdk_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            aws_sdk_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            aws_sdk_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            aws_sdk_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.update_autonomous_database_backup_input.UpdateAutonomousDatabaseBackupInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.update_autonomous_database_backup_output.UpdateAutonomousDatabaseBackupOutput"
        ]:
            import aws_sdk_odb._operations.odb.update_autonomous_database_backup

            output, http_response = (
                aws_sdk_odb._operations.odb.update_autonomous_database_backup.update_autonomous_database_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.update_autonomous_database_backup_input.UpdateAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
        input_["autonomous_database_backup_id"] = autonomous_database_backup_id
        if retention_period_in_days is not None:
            input_["retention_period_in_days"] = retention_period_in_days

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        autonomous_database_backup_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput":
        """<p>Deletes the specified Autonomous Database backup.</p>

        Args:
            autonomous_database_backup_id: <p>The unique identifier of the Autonomous Database backup to delete.</p>

        Raises:
            aws_sdk_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            aws_sdk_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            aws_sdk_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            aws_sdk_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            aws_sdk_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            aws_sdk_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.delete_autonomous_database_backup_input.DeleteAutonomousDatabaseBackupInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput"
        ]:
            import aws_sdk_odb._operations.odb.delete_autonomous_database_backup

            output, http_response = (
                aws_sdk_odb._operations.odb.delete_autonomous_database_backup.delete_autonomous_database_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.delete_autonomous_database_backup_input.DeleteAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
        input_["autonomous_database_backup_id"] = autonomous_database_backup_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        autonomous_database_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        status: Optional[
            "aws_sdk_odb.types.autonomous_database_backup_status.AutonomousDatabaseBackupStatus"
        ] = None,
        type: Optional[
            "aws_sdk_odb.types.autonomous_database_backup_type.AutonomousDatabaseBackupType"
        ] = None,
    ) -> "aws_sdk_odb.types.list_autonomous_database_backups_output.ListAutonomousDatabaseBackupsOutput":
        """<p>Lists the backups of the specified Autonomous Database.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            autonomous_database_id: <p>The unique identifier of the Autonomous Database whose backups you want to list.</p>
            status: <p>The status of the Autonomous Database backups to return results for.</p>
            type: <p>The type of the Autonomous Database backups to return results for.</p>

        Raises:
            aws_sdk_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            aws_sdk_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            aws_sdk_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            aws_sdk_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            aws_sdk_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_autonomous_database_backups_input.ListAutonomousDatabaseBackupsInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_autonomous_database_backups_output.ListAutonomousDatabaseBackupsOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_autonomous_database_backups

            output, http_response = (
                aws_sdk_odb._operations.odb.list_autonomous_database_backups.list_autonomous_database_backups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_autonomous_database_backups_input.ListAutonomousDatabaseBackupsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["autonomous_database_id"] = autonomous_database_id
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAutonomousDatabaseBackupResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def create(
        self,
        autonomous_database_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        display_name: Optional[
            "aws_sdk_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        retention_period_in_days: Optional[int] = None,
        client_token: Optional[
            "aws_sdk_odb.types.general_input_string.GeneralInputString"
        ] = None,
        tags: Optional["aws_sdk_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "aws_sdk_odb.types.create_autonomous_database_backup_output.CreateAutonomousDatabaseBackupOutput":
        """<p>Creates a new backup of the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to back up.</p>
            display_name: <p>The user-friendly name for the Autonomous Database backup.</p>
            retention_period_in_days: <p>The retention period, in days, for the Autonomous Database backup.</p>
            client_token: <p>A client-provided token to ensure the idempotency of the request.</p>
            tags: <p>The list of resource tags to apply to the Autonomous Database backup. Each tag is a key-value pair with no predefined name, type, or namespace.</p>

        Raises:
            aws_sdk_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            aws_sdk_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            aws_sdk_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            aws_sdk_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            aws_sdk_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            aws_sdk_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            aws_sdk_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.create_autonomous_database_backup_input.CreateAutonomousDatabaseBackupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.create_autonomous_database_backup_output.CreateAutonomousDatabaseBackupOutput"
        ]:
            import aws_sdk_odb._operations.odb.create_autonomous_database_backup

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.create_autonomous_database_backup.async_create_autonomous_database_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.create_autonomous_database_backup_input.CreateAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
        input_["autonomous_database_id"] = autonomous_database_id
        if display_name is not None:
            input_["display_name"] = display_name
        if retention_period_in_days is not None:
            input_["retention_period_in_days"] = retention_period_in_days
        if client_token is not None:
            input_["client_token"] = client_token
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
        autonomous_database_backup_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.get_autonomous_database_backup_output.GetAutonomousDatabaseBackupOutput":
        """<p>Gets information about a specific Autonomous Database backup.</p>

        Args:
            autonomous_database_backup_id: <p>The unique identifier of the Autonomous Database backup to retrieve information about.</p>

        Raises:
            aws_sdk_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            aws_sdk_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            aws_sdk_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            aws_sdk_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            aws_sdk_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.get_autonomous_database_backup_input.GetAutonomousDatabaseBackupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.get_autonomous_database_backup_output.GetAutonomousDatabaseBackupOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_autonomous_database_backup

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.get_autonomous_database_backup.async_get_autonomous_database_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_autonomous_database_backup_input.GetAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
        input_["autonomous_database_backup_id"] = autonomous_database_backup_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        autonomous_database_backup_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        retention_period_in_days: Optional[int] = None,
    ) -> "aws_sdk_odb.types.update_autonomous_database_backup_output.UpdateAutonomousDatabaseBackupOutput":
        """<p>Updates the properties of an Autonomous Database backup.</p>

        Args:
            autonomous_database_backup_id: <p>The unique identifier of the Autonomous Database backup to update.</p>
            retention_period_in_days: <p>The retention period, in days, for the Autonomous Database backup.</p>

        Raises:
            aws_sdk_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            aws_sdk_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            aws_sdk_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            aws_sdk_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            aws_sdk_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            aws_sdk_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.update_autonomous_database_backup_input.UpdateAutonomousDatabaseBackupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.update_autonomous_database_backup_output.UpdateAutonomousDatabaseBackupOutput"
        ]:
            import aws_sdk_odb._operations.odb.update_autonomous_database_backup

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.update_autonomous_database_backup.async_update_autonomous_database_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.update_autonomous_database_backup_input.UpdateAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
        input_["autonomous_database_backup_id"] = autonomous_database_backup_id
        if retention_period_in_days is not None:
            input_["retention_period_in_days"] = retention_period_in_days

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        autonomous_database_backup_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput":
        """<p>Deletes the specified Autonomous Database backup.</p>

        Args:
            autonomous_database_backup_id: <p>The unique identifier of the Autonomous Database backup to delete.</p>

        Raises:
            aws_sdk_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            aws_sdk_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            aws_sdk_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            aws_sdk_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            aws_sdk_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            aws_sdk_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.delete_autonomous_database_backup_input.DeleteAutonomousDatabaseBackupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput"
        ]:
            import aws_sdk_odb._operations.odb.delete_autonomous_database_backup

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.delete_autonomous_database_backup.async_delete_autonomous_database_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.delete_autonomous_database_backup_input.DeleteAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
        input_["autonomous_database_backup_id"] = autonomous_database_backup_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        autonomous_database_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        status: Optional[
            "aws_sdk_odb.types.autonomous_database_backup_status.AutonomousDatabaseBackupStatus"
        ] = None,
        type: Optional[
            "aws_sdk_odb.types.autonomous_database_backup_type.AutonomousDatabaseBackupType"
        ] = None,
    ) -> "aws_sdk_odb.types.list_autonomous_database_backups_output.ListAutonomousDatabaseBackupsOutput":
        """<p>Lists the backups of the specified Autonomous Database.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            autonomous_database_id: <p>The unique identifier of the Autonomous Database whose backups you want to list.</p>
            status: <p>The status of the Autonomous Database backups to return results for.</p>
            type: <p>The type of the Autonomous Database backups to return results for.</p>

        Raises:
            aws_sdk_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            aws_sdk_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            aws_sdk_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            aws_sdk_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            aws_sdk_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.list_autonomous_database_backups_input.ListAutonomousDatabaseBackupsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.list_autonomous_database_backups_output.ListAutonomousDatabaseBackupsOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_autonomous_database_backups

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.list_autonomous_database_backups.async_list_autonomous_database_backups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_autonomous_database_backups_input.ListAutonomousDatabaseBackupsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["autonomous_database_id"] = autonomous_database_id
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
