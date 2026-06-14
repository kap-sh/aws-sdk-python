import datetime
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
    import aws_sdk_notifications.types.account_id
    import aws_sdk_notifications.types.get_managed_notification_event_request
    import aws_sdk_notifications.types.get_managed_notification_event_response
    import aws_sdk_notifications.types.list_managed_notification_events_request
    import aws_sdk_notifications.types.list_managed_notification_events_response
    import aws_sdk_notifications.types.locale_code
    import aws_sdk_notifications.types.managed_notification_event_arn
    import aws_sdk_notifications.types.managed_notification_event_overview
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.organizational_unit_id
    import aws_sdk_notifications.types.source
    from aws_sdk_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from aws_sdk_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class ManagedNotificationEventResource:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def read(
        self,
        arn: "aws_sdk_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        locale: Optional["aws_sdk_notifications.types.locale_code.LocaleCode"] = None,
    ) -> "aws_sdk_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse":
        """<p>Returns a specified <code>ManagedNotificationEvent</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationEvent</code> to return.</p>
            locale: <p>The locale code of the language used for the retrieved <code>ManagedNotificationEvent</code>. The default locale is English <code>(en_US)</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.get_managed_notification_event_request.GetManagedNotificationEventRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.get_managed_notification_event

            output, http_response = (
                aws_sdk_notifications._operations.notifications.get_managed_notification_event.get_managed_notification_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.get_managed_notification_event_request.GetManagedNotificationEventRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if locale is not None:
            input_["locale"] = locale

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        locale: Optional["aws_sdk_notifications.types.locale_code.LocaleCode"] = None,
        source: Optional["aws_sdk_notifications.types.source.Source"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
        organizational_unit_id: Optional[
            "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
        related_account: Optional[
            "aws_sdk_notifications.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_notifications.types.list_managed_notification_events_response.ListManagedNotificationEventsResponse":
        """<p>Returns a list of Managed Notification Events according to specified filters, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            start_time: <p>The earliest time of events to return from this call.</p>
            end_time: <p>Latest time of events to return from this call.</p>
            locale: <p>The locale code of the language used for the retrieved NotificationEvent. The default locale is English (en_US).</p>
            source: <p>The Amazon Web Services service the event originates from. For example aws.cloudwatch.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListManagedNotificationChannelAssociations</code> call. Next token uses Base64 encoding.</p>
            organizational_unit_id: <p>The Organizational Unit Id that an Amazon Web Services account belongs to.</p>
            related_account: <p>The Amazon Web Services account ID associated with the Managed Notification Events.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.list_managed_notification_events_request.ListManagedNotificationEventsRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.list_managed_notification_events_response.ListManagedNotificationEventsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_managed_notification_events

            output, http_response = (
                aws_sdk_notifications._operations.notifications.list_managed_notification_events.list_managed_notification_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.list_managed_notification_events_request.ListManagedNotificationEventsRequest = {}  # type: ignore[typeddict-item]
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if locale is not None:
            input_["locale"] = locale
        if source is not None:
            input_["source"] = source
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id
        if related_account is not None:
            input_["related_account"] = related_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncManagedNotificationEventResource:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def read(
        self,
        arn: "aws_sdk_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        locale: Optional["aws_sdk_notifications.types.locale_code.LocaleCode"] = None,
    ) -> "aws_sdk_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse":
        """<p>Returns a specified <code>ManagedNotificationEvent</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationEvent</code> to return.</p>
            locale: <p>The locale code of the language used for the retrieved <code>ManagedNotificationEvent</code>. The default locale is English <code>(en_US)</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.get_managed_notification_event_request.GetManagedNotificationEventRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.get_managed_notification_event

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.get_managed_notification_event.async_get_managed_notification_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.get_managed_notification_event_request.GetManagedNotificationEventRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        locale: Optional["aws_sdk_notifications.types.locale_code.LocaleCode"] = None,
        source: Optional["aws_sdk_notifications.types.source.Source"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
        organizational_unit_id: Optional[
            "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
        related_account: Optional[
            "aws_sdk_notifications.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_notifications.types.list_managed_notification_events_response.ListManagedNotificationEventsResponse":
        """<p>Returns a list of Managed Notification Events according to specified filters, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            start_time: <p>The earliest time of events to return from this call.</p>
            end_time: <p>Latest time of events to return from this call.</p>
            locale: <p>The locale code of the language used for the retrieved NotificationEvent. The default locale is English (en_US).</p>
            source: <p>The Amazon Web Services service the event originates from. For example aws.cloudwatch.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListManagedNotificationChannelAssociations</code> call. Next token uses Base64 encoding.</p>
            organizational_unit_id: <p>The Organizational Unit Id that an Amazon Web Services account belongs to.</p>
            related_account: <p>The Amazon Web Services account ID associated with the Managed Notification Events.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.list_managed_notification_events_request.ListManagedNotificationEventsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.list_managed_notification_events_response.ListManagedNotificationEventsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_managed_notification_events

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.list_managed_notification_events.async_list_managed_notification_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.list_managed_notification_events_request.ListManagedNotificationEventsRequest = {}  # type: ignore[typeddict-item]
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if locale is not None:
            input_["locale"] = locale
        if source is not None:
            input_["source"] = source
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id
        if related_account is not None:
            input_["related_account"] = related_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
