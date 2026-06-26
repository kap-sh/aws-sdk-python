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
    import aws_sdk_notifications.types.account_contact_type
    import aws_sdk_notifications.types.associate_managed_notification_account_contact_request
    import aws_sdk_notifications.types.associate_managed_notification_account_contact_response
    import aws_sdk_notifications.types.disassociate_managed_notification_account_contact_request
    import aws_sdk_notifications.types.disassociate_managed_notification_account_contact_response
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn
    from aws_sdk_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from aws_sdk_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class ManagedNotificationAccountContactAssociation:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def put(
        self,
        contact_identifier: "aws_sdk_notifications.types.account_contact_type.AccountContactType",
        managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.associate_managed_notification_account_contact_response.AssociateManagedNotificationAccountContactResponse":
        """<p>Associates an Account Contact with a particular <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            contact_identifier: <p>A unique value of an Account Contact Type to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the Account Contact.</p>

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
            req: "OperationRequest[aws_sdk_notifications.types.associate_managed_notification_account_contact_request.AssociateManagedNotificationAccountContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.associate_managed_notification_account_contact_response.AssociateManagedNotificationAccountContactResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.associate_managed_notification_account_contact

            output, http_response = (
                aws_sdk_notifications._operations.notifications.associate_managed_notification_account_contact.associate_managed_notification_account_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.associate_managed_notification_account_contact_request.AssociateManagedNotificationAccountContactRequest = {}  # type: ignore[typeddict-item]
        input_["contact_identifier"] = contact_identifier
        input_["managed_notification_configuration_arn"] = (
            managed_notification_configuration_arn
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        contact_identifier: "aws_sdk_notifications.types.account_contact_type.AccountContactType",
        managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.disassociate_managed_notification_account_contact_response.DisassociateManagedNotificationAccountContactResponse":
        """<p>Disassociates an Account Contact with a particular <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            contact_identifier: <p>The unique value of an Account Contact Type to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the Account Contact.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.disassociate_managed_notification_account_contact_request.DisassociateManagedNotificationAccountContactRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.disassociate_managed_notification_account_contact_response.DisassociateManagedNotificationAccountContactResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.disassociate_managed_notification_account_contact

            output, http_response = (
                aws_sdk_notifications._operations.notifications.disassociate_managed_notification_account_contact.disassociate_managed_notification_account_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.disassociate_managed_notification_account_contact_request.DisassociateManagedNotificationAccountContactRequest = {}  # type: ignore[typeddict-item]
        input_["contact_identifier"] = contact_identifier
        input_["managed_notification_configuration_arn"] = (
            managed_notification_configuration_arn
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncManagedNotificationAccountContactAssociation:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def put(
        self,
        contact_identifier: "aws_sdk_notifications.types.account_contact_type.AccountContactType",
        managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.associate_managed_notification_account_contact_response.AssociateManagedNotificationAccountContactResponse":
        """<p>Associates an Account Contact with a particular <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            contact_identifier: <p>A unique value of an Account Contact Type to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the Account Contact.</p>

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
            req: "AsyncOperationRequest[aws_sdk_notifications.types.associate_managed_notification_account_contact_request.AssociateManagedNotificationAccountContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.associate_managed_notification_account_contact_response.AssociateManagedNotificationAccountContactResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.associate_managed_notification_account_contact

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.associate_managed_notification_account_contact.async_associate_managed_notification_account_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.associate_managed_notification_account_contact_request.AssociateManagedNotificationAccountContactRequest = {}  # type: ignore[typeddict-item]
        input_["contact_identifier"] = contact_identifier
        input_["managed_notification_configuration_arn"] = (
            managed_notification_configuration_arn
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        contact_identifier: "aws_sdk_notifications.types.account_contact_type.AccountContactType",
        managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.disassociate_managed_notification_account_contact_response.DisassociateManagedNotificationAccountContactResponse":
        """<p>Disassociates an Account Contact with a particular <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            contact_identifier: <p>The unique value of an Account Contact Type to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the Account Contact.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.disassociate_managed_notification_account_contact_request.DisassociateManagedNotificationAccountContactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.disassociate_managed_notification_account_contact_response.DisassociateManagedNotificationAccountContactResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.disassociate_managed_notification_account_contact

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.disassociate_managed_notification_account_contact.async_disassociate_managed_notification_account_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.disassociate_managed_notification_account_contact_request.DisassociateManagedNotificationAccountContactRequest = {}  # type: ignore[typeddict-item]
        input_["contact_identifier"] = contact_identifier
        input_["managed_notification_configuration_arn"] = (
            managed_notification_configuration_arn
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
