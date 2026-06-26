from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_notifications._auth._signers
import aws_sdk_notifications._auth._sigv4
from aws_sdk_notifications._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_notifications.types.disable_notifications_access_for_organization_request
    import aws_sdk_notifications.types.disable_notifications_access_for_organization_response
    import aws_sdk_notifications.types.enable_notifications_access_for_organization_request
    import aws_sdk_notifications.types.enable_notifications_access_for_organization_response
    import aws_sdk_notifications.types.get_notifications_access_for_organization_request
    import aws_sdk_notifications.types.get_notifications_access_for_organization_response
    from aws_sdk_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from aws_sdk_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class OrganizationAccess:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def put(
        self, *, config_overrides: Optional[NotificationsClientConfig] = None
    ) -> "aws_sdk_notifications.types.enable_notifications_access_for_organization_response.EnableNotificationsAccessForOrganizationResponse":
        """<p>Enables service trust between User Notifications and Amazon Web Services Organizations.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.enable_notifications_access_for_organization_request.EnableNotificationsAccessForOrganizationRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.enable_notifications_access_for_organization_response.EnableNotificationsAccessForOrganizationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.enable_notifications_access_for_organization

            output, http_response = (
                aws_sdk_notifications._operations.notifications.enable_notifications_access_for_organization.enable_notifications_access_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.enable_notifications_access_for_organization_request.EnableNotificationsAccessForOrganizationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self, *, config_overrides: Optional[NotificationsClientConfig] = None
    ) -> "aws_sdk_notifications.types.get_notifications_access_for_organization_response.GetNotificationsAccessForOrganizationResponse":
        """<p>Returns the AccessStatus of Service Trust Enablement for User Notifications and Amazon Web Services Organizations.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.get_notifications_access_for_organization_request.GetNotificationsAccessForOrganizationRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.get_notifications_access_for_organization_response.GetNotificationsAccessForOrganizationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.get_notifications_access_for_organization

            output, http_response = (
                aws_sdk_notifications._operations.notifications.get_notifications_access_for_organization.get_notifications_access_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.get_notifications_access_for_organization_request.GetNotificationsAccessForOrganizationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self, *, config_overrides: Optional[NotificationsClientConfig] = None
    ) -> "aws_sdk_notifications.types.disable_notifications_access_for_organization_response.DisableNotificationsAccessForOrganizationResponse":
        """<p>Disables service trust between User Notifications and Amazon Web Services Organizations.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.disable_notifications_access_for_organization_request.DisableNotificationsAccessForOrganizationRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.disable_notifications_access_for_organization_response.DisableNotificationsAccessForOrganizationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.disable_notifications_access_for_organization

            output, http_response = (
                aws_sdk_notifications._operations.notifications.disable_notifications_access_for_organization.disable_notifications_access_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.disable_notifications_access_for_organization_request.DisableNotificationsAccessForOrganizationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncOrganizationAccess:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def put(
        self, *, config_overrides: Optional[AsyncNotificationsClientConfig] = None
    ) -> "aws_sdk_notifications.types.enable_notifications_access_for_organization_response.EnableNotificationsAccessForOrganizationResponse":
        """<p>Enables service trust between User Notifications and Amazon Web Services Organizations.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.enable_notifications_access_for_organization_request.EnableNotificationsAccessForOrganizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.enable_notifications_access_for_organization_response.EnableNotificationsAccessForOrganizationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.enable_notifications_access_for_organization

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.enable_notifications_access_for_organization.async_enable_notifications_access_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.enable_notifications_access_for_organization_request.EnableNotificationsAccessForOrganizationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self, *, config_overrides: Optional[AsyncNotificationsClientConfig] = None
    ) -> "aws_sdk_notifications.types.get_notifications_access_for_organization_response.GetNotificationsAccessForOrganizationResponse":
        """<p>Returns the AccessStatus of Service Trust Enablement for User Notifications and Amazon Web Services Organizations.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.get_notifications_access_for_organization_request.GetNotificationsAccessForOrganizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.get_notifications_access_for_organization_response.GetNotificationsAccessForOrganizationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.get_notifications_access_for_organization

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.get_notifications_access_for_organization.async_get_notifications_access_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.get_notifications_access_for_organization_request.GetNotificationsAccessForOrganizationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self, *, config_overrides: Optional[AsyncNotificationsClientConfig] = None
    ) -> "aws_sdk_notifications.types.disable_notifications_access_for_organization_response.DisableNotificationsAccessForOrganizationResponse":
        """<p>Disables service trust between User Notifications and Amazon Web Services Organizations.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.disable_notifications_access_for_organization_request.DisableNotificationsAccessForOrganizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.disable_notifications_access_for_organization_response.DisableNotificationsAccessForOrganizationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.disable_notifications_access_for_organization

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.disable_notifications_access_for_organization.async_disable_notifications_access_for_organization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.disable_notifications_access_for_organization_request.DisableNotificationsAccessForOrganizationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
