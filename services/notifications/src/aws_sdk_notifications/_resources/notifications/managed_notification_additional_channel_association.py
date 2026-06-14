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
    import aws_sdk_notifications.types.associate_managed_notification_additional_channel_request
    import aws_sdk_notifications.types.associate_managed_notification_additional_channel_response
    import aws_sdk_notifications.types.channel_arn
    import aws_sdk_notifications.types.disassociate_managed_notification_additional_channel_request
    import aws_sdk_notifications.types.disassociate_managed_notification_additional_channel_response
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn
    from aws_sdk_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from aws_sdk_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class ManagedNotificationAdditionalChannelAssociation:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def put(
        self,
        channel_arn: "aws_sdk_notifications.types.channel_arn.ChannelArn",
        managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.associate_managed_notification_additional_channel_response.AssociateManagedNotificationAdditionalChannelResponse":
        """<p>Associates an additional Channel with a particular <code>ManagedNotificationConfiguration</code>.</p> <p>Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p> <p>Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and email (notifications-contacts).</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the additional Channel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.associate_managed_notification_additional_channel_request.AssociateManagedNotificationAdditionalChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.associate_managed_notification_additional_channel_response.AssociateManagedNotificationAdditionalChannelResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.associate_managed_notification_additional_channel

            output, http_response = (
                aws_sdk_notifications._operations.notifications.associate_managed_notification_additional_channel.associate_managed_notification_additional_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.associate_managed_notification_additional_channel_request.AssociateManagedNotificationAdditionalChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
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
        channel_arn: "aws_sdk_notifications.types.channel_arn.ChannelArn",
        managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.disassociate_managed_notification_additional_channel_response.DisassociateManagedNotificationAdditionalChannelResponse":
        """<p>Disassociates an additional Channel from a particular <code>ManagedNotificationConfiguration</code>.</p> <p>Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the Managed Notification Configuration to associate with the additional Channel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.disassociate_managed_notification_additional_channel_request.DisassociateManagedNotificationAdditionalChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.disassociate_managed_notification_additional_channel_response.DisassociateManagedNotificationAdditionalChannelResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.disassociate_managed_notification_additional_channel

            output, http_response = (
                aws_sdk_notifications._operations.notifications.disassociate_managed_notification_additional_channel.disassociate_managed_notification_additional_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.disassociate_managed_notification_additional_channel_request.DisassociateManagedNotificationAdditionalChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["managed_notification_configuration_arn"] = (
            managed_notification_configuration_arn
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncManagedNotificationAdditionalChannelAssociation:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def put(
        self,
        channel_arn: "aws_sdk_notifications.types.channel_arn.ChannelArn",
        managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.associate_managed_notification_additional_channel_response.AssociateManagedNotificationAdditionalChannelResponse":
        """<p>Associates an additional Channel with a particular <code>ManagedNotificationConfiguration</code>.</p> <p>Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p> <p>Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and email (notifications-contacts).</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the additional Channel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.associate_managed_notification_additional_channel_request.AssociateManagedNotificationAdditionalChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.associate_managed_notification_additional_channel_response.AssociateManagedNotificationAdditionalChannelResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.associate_managed_notification_additional_channel

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.associate_managed_notification_additional_channel.async_associate_managed_notification_additional_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.associate_managed_notification_additional_channel_request.AssociateManagedNotificationAdditionalChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
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
        channel_arn: "aws_sdk_notifications.types.channel_arn.ChannelArn",
        managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.disassociate_managed_notification_additional_channel_response.DisassociateManagedNotificationAdditionalChannelResponse":
        """<p>Disassociates an additional Channel from a particular <code>ManagedNotificationConfiguration</code>.</p> <p>Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the Managed Notification Configuration to associate with the additional Channel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.disassociate_managed_notification_additional_channel_request.DisassociateManagedNotificationAdditionalChannelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.disassociate_managed_notification_additional_channel_response.DisassociateManagedNotificationAdditionalChannelResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.disassociate_managed_notification_additional_channel

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.disassociate_managed_notification_additional_channel.async_disassociate_managed_notification_additional_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.disassociate_managed_notification_additional_channel_request.DisassociateManagedNotificationAdditionalChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["managed_notification_configuration_arn"] = (
            managed_notification_configuration_arn
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
