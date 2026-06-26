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
    import aws_sdk_notifications.types.deregister_notification_hub_request
    import aws_sdk_notifications.types.deregister_notification_hub_response
    import aws_sdk_notifications.types.list_notification_hubs_request
    import aws_sdk_notifications.types.list_notification_hubs_response
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_hub_overview
    import aws_sdk_notifications.types.region
    import aws_sdk_notifications.types.register_notification_hub_request
    import aws_sdk_notifications.types.register_notification_hub_response
    from aws_sdk_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from aws_sdk_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class NotificationHub:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def put(
        self,
        notification_hub_region: "aws_sdk_notifications.types.region.Region",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.register_notification_hub_response.RegisterNotificationHubResponse":
        """<p>Registers a <code>NotificationConfiguration</code> in the specified Region.</p> <p>There is a maximum of one <code>NotificationConfiguration</code> per Region. You can have a maximum of 3 <code>NotificationHub</code> resources at a time.</p>

        Args:
            notification_hub_region: <p>The Region of the <code>NotificationHub</code>.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.register_notification_hub_request.RegisterNotificationHubRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.register_notification_hub_response.RegisterNotificationHubResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.register_notification_hub

            output, http_response = (
                aws_sdk_notifications._operations.notifications.register_notification_hub.register_notification_hub(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.register_notification_hub_request.RegisterNotificationHubRequest = {}  # type: ignore[typeddict-item]
        input_["notification_hub_region"] = notification_hub_region

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        notification_hub_region: "aws_sdk_notifications.types.region.Region",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.deregister_notification_hub_response.DeregisterNotificationHubResponse":
        """<p>Deregisters a <code>NotificationConfiguration</code> in the specified Region.</p> <note> <p>You can't deregister the last <code>NotificationHub</code> in the account. <code>NotificationEvents</code> stored in the deregistered <code>NotificationConfiguration</code> are no longer be visible. Recreating a new <code>NotificationConfiguration</code> in the same Region restores access to those <code>NotificationEvents</code>.</p> </note>

        Args:
            notification_hub_region: <p>The <code>NotificationConfiguration</code> Region.</p>

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
            req: "OperationRequest[aws_sdk_notifications.types.deregister_notification_hub_request.DeregisterNotificationHubRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.deregister_notification_hub_response.DeregisterNotificationHubResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.deregister_notification_hub

            output, http_response = (
                aws_sdk_notifications._operations.notifications.deregister_notification_hub.deregister_notification_hub(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.deregister_notification_hub_request.DeregisterNotificationHubRequest = {}  # type: ignore[typeddict-item]
        input_["notification_hub_region"] = notification_hub_region

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
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_notification_hubs_response.ListNotificationHubsResponse":
        """<p>Returns a list of <code>NotificationHubs</code>.</p>

        Args:
            max_results: <p>The maximum number of records to list in a single response.</p>
            next_token: <p>A pagination token. Set to null to start listing notification hubs from the start.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.list_notification_hubs_request.ListNotificationHubsRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.list_notification_hubs_response.ListNotificationHubsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_notification_hubs

            output, http_response = (
                aws_sdk_notifications._operations.notifications.list_notification_hubs.list_notification_hubs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.list_notification_hubs_request.ListNotificationHubsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncNotificationHub:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def put(
        self,
        notification_hub_region: "aws_sdk_notifications.types.region.Region",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.register_notification_hub_response.RegisterNotificationHubResponse":
        """<p>Registers a <code>NotificationConfiguration</code> in the specified Region.</p> <p>There is a maximum of one <code>NotificationConfiguration</code> per Region. You can have a maximum of 3 <code>NotificationHub</code> resources at a time.</p>

        Args:
            notification_hub_region: <p>The Region of the <code>NotificationHub</code>.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.register_notification_hub_request.RegisterNotificationHubRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.register_notification_hub_response.RegisterNotificationHubResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.register_notification_hub

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.register_notification_hub.async_register_notification_hub(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.register_notification_hub_request.RegisterNotificationHubRequest = {}  # type: ignore[typeddict-item]
        input_["notification_hub_region"] = notification_hub_region

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        notification_hub_region: "aws_sdk_notifications.types.region.Region",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.deregister_notification_hub_response.DeregisterNotificationHubResponse":
        """<p>Deregisters a <code>NotificationConfiguration</code> in the specified Region.</p> <note> <p>You can't deregister the last <code>NotificationHub</code> in the account. <code>NotificationEvents</code> stored in the deregistered <code>NotificationConfiguration</code> are no longer be visible. Recreating a new <code>NotificationConfiguration</code> in the same Region restores access to those <code>NotificationEvents</code>.</p> </note>

        Args:
            notification_hub_region: <p>The <code>NotificationConfiguration</code> Region.</p>

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
            req: "AsyncOperationRequest[aws_sdk_notifications.types.deregister_notification_hub_request.DeregisterNotificationHubRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.deregister_notification_hub_response.DeregisterNotificationHubResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.deregister_notification_hub

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.deregister_notification_hub.async_deregister_notification_hub(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.deregister_notification_hub_request.DeregisterNotificationHubRequest = {}  # type: ignore[typeddict-item]
        input_["notification_hub_region"] = notification_hub_region

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
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_notification_hubs_response.ListNotificationHubsResponse":
        """<p>Returns a list of <code>NotificationHubs</code>.</p>

        Args:
            max_results: <p>The maximum number of records to list in a single response.</p>
            next_token: <p>A pagination token. Set to null to start listing notification hubs from the start.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.list_notification_hubs_request.ListNotificationHubsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.list_notification_hubs_response.ListNotificationHubsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_notification_hubs

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.list_notification_hubs.async_list_notification_hubs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.list_notification_hubs_request.ListNotificationHubsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
