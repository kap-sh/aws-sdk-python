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
    import aws_sdk_notifications.types.channel_identifier
    import aws_sdk_notifications.types.get_managed_notification_configuration_request
    import aws_sdk_notifications.types.get_managed_notification_configuration_response
    import aws_sdk_notifications.types.list_managed_notification_configurations_request
    import aws_sdk_notifications.types.list_managed_notification_configurations_response
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn
    import aws_sdk_notifications.types.managed_notification_configuration_structure
    import aws_sdk_notifications.types.next_token
    from aws_sdk_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from aws_sdk_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class ManagedNotificationConfiguration:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def read(
        self,
        arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.get_managed_notification_configuration_response.GetManagedNotificationConfigurationResponse":
        """<p>Returns a specified <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.get_managed_notification_configuration_request.GetManagedNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.get_managed_notification_configuration_response.GetManagedNotificationConfigurationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.get_managed_notification_configuration

            output, http_response = (
                aws_sdk_notifications._operations.notifications.get_managed_notification_configuration.get_managed_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.get_managed_notification_configuration_request.GetManagedNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        channel_identifier: Optional[
            "aws_sdk_notifications.types.channel_identifier.ChannelIdentifier"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_managed_notification_configurations_response.ListManagedNotificationConfigurationsResponse":
        """<p>Returns a list of Managed Notification Configurations according to specified filters, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            channel_identifier: <p>The identifier or ARN of the notification channel to filter configurations by.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous ListManagedNotificationChannelAssociations call. Next token uses Base64 encoding.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.list_managed_notification_configurations_request.ListManagedNotificationConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.list_managed_notification_configurations_response.ListManagedNotificationConfigurationsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_managed_notification_configurations

            output, http_response = (
                aws_sdk_notifications._operations.notifications.list_managed_notification_configurations.list_managed_notification_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.list_managed_notification_configurations_request.ListManagedNotificationConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if channel_identifier is not None:
            input["channel_identifier"] = channel_identifier
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


class AsyncManagedNotificationConfiguration:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def read(
        self,
        arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.get_managed_notification_configuration_response.GetManagedNotificationConfigurationResponse":
        """<p>Returns a specified <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.get_managed_notification_configuration_request.GetManagedNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.get_managed_notification_configuration_response.GetManagedNotificationConfigurationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.get_managed_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.get_managed_notification_configuration.async_get_managed_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.get_managed_notification_configuration_request.GetManagedNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        channel_identifier: Optional[
            "aws_sdk_notifications.types.channel_identifier.ChannelIdentifier"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_managed_notification_configurations_response.ListManagedNotificationConfigurationsResponse":
        """<p>Returns a list of Managed Notification Configurations according to specified filters, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            channel_identifier: <p>The identifier or ARN of the notification channel to filter configurations by.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous ListManagedNotificationChannelAssociations call. Next token uses Base64 encoding.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.list_managed_notification_configurations_request.ListManagedNotificationConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.list_managed_notification_configurations_response.ListManagedNotificationConfigurationsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_managed_notification_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.list_managed_notification_configurations.async_list_managed_notification_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.list_managed_notification_configurations_request.ListManagedNotificationConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if channel_identifier is not None:
            input["channel_identifier"] = channel_identifier
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
