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
