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
    import aws_sdk_notifications.types.aggregation_duration
    import aws_sdk_notifications.types.channel_arn
    import aws_sdk_notifications.types.create_notification_configuration_request
    import aws_sdk_notifications.types.create_notification_configuration_response
    import aws_sdk_notifications.types.delete_notification_configuration_request
    import aws_sdk_notifications.types.delete_notification_configuration_response
    import aws_sdk_notifications.types.get_notification_configuration_request
    import aws_sdk_notifications.types.get_notification_configuration_response
    import aws_sdk_notifications.types.list_notification_configurations_request
    import aws_sdk_notifications.types.list_notification_configurations_response
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.notification_configuration_description
    import aws_sdk_notifications.types.notification_configuration_name
    import aws_sdk_notifications.types.notification_configuration_status
    import aws_sdk_notifications.types.notification_configuration_structure
    import aws_sdk_notifications.types.notification_configuration_subtype
    import aws_sdk_notifications.types.source
    import aws_sdk_notifications.types.tag_map
    import aws_sdk_notifications.types.update_notification_configuration_request
    import aws_sdk_notifications.types.update_notification_configuration_response
    from aws_sdk_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from aws_sdk_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class NotificationConfiguration:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_notifications.types.notification_configuration_name.NotificationConfigurationName",
        description: "aws_sdk_notifications.types.notification_configuration_description.NotificationConfigurationDescription",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        aggregation_duration: Optional[
            "aws_sdk_notifications.types.aggregation_duration.AggregationDuration"
        ] = None,
        tags: Optional["aws_sdk_notifications.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_notifications.types.create_notification_configuration_response.CreateNotificationConfigurationResponse":
        """<p>Creates a new <code>NotificationConfiguration</code>.</p>

        Args:
            name: <p>The name of the <code>NotificationConfiguration</code>. Supports RFC 3986's unreserved characters.</p>
            description: <p>The description of the <code>NotificationConfiguration</code>.</p>
            aggregation_duration: <p>The aggregation preference of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>LONG</code> </p> <ul> <li> <p>Aggregate notifications for long periods of time (12 hours).</p> </li> </ul> </li> <li> <p> <code>SHORT</code> </p> <ul> <li> <p>Aggregate notifications for short periods of time (5 minutes).</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>Don't aggregate notifications.</p> </li> </ul> </li> </ul> </li> </ul>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.create_notification_configuration_request.CreateNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.create_notification_configuration_response.CreateNotificationConfigurationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.create_notification_configuration

            output, http_response = (
                aws_sdk_notifications._operations.notifications.create_notification_configuration.create_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.create_notification_configuration_request.CreateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["description"] = description
        if aggregation_duration is not None:
            input["aggregation_duration"] = aggregation_duration
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put(
        self,
        arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        name: Optional[
            "aws_sdk_notifications.types.notification_configuration_name.NotificationConfigurationName"
        ] = None,
        description: Optional[
            "aws_sdk_notifications.types.notification_configuration_description.NotificationConfigurationDescription"
        ] = None,
        aggregation_duration: Optional[
            "aws_sdk_notifications.types.aggregation_duration.AggregationDuration"
        ] = None,
    ) -> "aws_sdk_notifications.types.update_notification_configuration_response.UpdateNotificationConfigurationResponse":
        """<p>Updates a <code>NotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) used to update the <code>NotificationConfiguration</code>.</p>
            name: <p>The name of the <code>NotificationConfiguration</code>.</p>
            description: <p>The description of the <code>NotificationConfiguration</code>.</p>
            aggregation_duration: <p>The aggregation preference of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>LONG</code> </p> <ul> <li> <p>Aggregate notifications for long periods of time (12 hours).</p> </li> </ul> </li> <li> <p> <code>SHORT</code> </p> <ul> <li> <p>Aggregate notifications for short periods of time (5 minutes).</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>Don't aggregate notifications.</p> </li> </ul> </li> </ul> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.update_notification_configuration_response.UpdateNotificationConfigurationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.update_notification_configuration

            output, http_response = (
                aws_sdk_notifications._operations.notifications.update_notification_configuration.update_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if aggregation_duration is not None:
            input["aggregation_duration"] = aggregation_duration

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.get_notification_configuration_response.GetNotificationConfigurationResponse":
        """<p>Returns a specified <code>NotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.get_notification_configuration_request.GetNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.get_notification_configuration_response.GetNotificationConfigurationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.get_notification_configuration

            output, http_response = (
                aws_sdk_notifications._operations.notifications.get_notification_configuration.get_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.get_notification_configuration_request.GetNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.delete_notification_configuration_response.DeleteNotificationConfigurationResponse":
        """<p>Deletes a <code>NotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.delete_notification_configuration_response.DeleteNotificationConfigurationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.delete_notification_configuration

            output, http_response = (
                aws_sdk_notifications._operations.notifications.delete_notification_configuration.delete_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
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
        event_rule_source: Optional["aws_sdk_notifications.types.source.Source"] = None,
        channel_arn: Optional[
            "aws_sdk_notifications.types.channel_arn.ChannelArn"
        ] = None,
        status: Optional[
            "aws_sdk_notifications.types.notification_configuration_status.NotificationConfigurationStatus"
        ] = None,
        subtype: Optional[
            "aws_sdk_notifications.types.notification_configuration_subtype.NotificationConfigurationSubtype"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse":
        """<p>Returns a list of abbreviated <code>NotificationConfigurations</code> according to specified filters, in reverse chronological order (newest first).</p>

        Args:
            event_rule_source: <p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level\">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to match.</p>
            status: <p>The <code>NotificationConfiguration</code> status to match.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ACTIVE</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>ACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>PARTIALLY_ACTIVE</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> <li> <p>Any call can be run.</p> </li> </ul> </li> <li> <p> <code>INACTIVE</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>INACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>DELETING</code> </p> <ul> <li> <p>This <code>NotificationConfiguration</code> is being deleted.</p> </li> <li> <p>Only <code>GET</code> and <code>LIST</code> calls can be run.</p> </li> </ul> </li> </ul> </li> </ul>
            subtype: <p>The subtype used to filter the notification configurations in the request.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.list_notification_configurations_request.ListNotificationConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_notification_configurations

            output, http_response = (
                aws_sdk_notifications._operations.notifications.list_notification_configurations.list_notification_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.list_notification_configurations_request.ListNotificationConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if event_rule_source is not None:
            input["event_rule_source"] = event_rule_source
        if channel_arn is not None:
            input["channel_arn"] = channel_arn
        if status is not None:
            input["status"] = status
        if subtype is not None:
            input["subtype"] = subtype
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


class AsyncNotificationConfiguration:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_notifications.types.notification_configuration_name.NotificationConfigurationName",
        description: "aws_sdk_notifications.types.notification_configuration_description.NotificationConfigurationDescription",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        aggregation_duration: Optional[
            "aws_sdk_notifications.types.aggregation_duration.AggregationDuration"
        ] = None,
        tags: Optional["aws_sdk_notifications.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_notifications.types.create_notification_configuration_response.CreateNotificationConfigurationResponse":
        """<p>Creates a new <code>NotificationConfiguration</code>.</p>

        Args:
            name: <p>The name of the <code>NotificationConfiguration</code>. Supports RFC 3986's unreserved characters.</p>
            description: <p>The description of the <code>NotificationConfiguration</code>.</p>
            aggregation_duration: <p>The aggregation preference of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>LONG</code> </p> <ul> <li> <p>Aggregate notifications for long periods of time (12 hours).</p> </li> </ul> </li> <li> <p> <code>SHORT</code> </p> <ul> <li> <p>Aggregate notifications for short periods of time (5 minutes).</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>Don't aggregate notifications.</p> </li> </ul> </li> </ul> </li> </ul>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.create_notification_configuration_request.CreateNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.create_notification_configuration_response.CreateNotificationConfigurationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.create_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.create_notification_configuration.async_create_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.create_notification_configuration_request.CreateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["description"] = description
        if aggregation_duration is not None:
            input["aggregation_duration"] = aggregation_duration
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put(
        self,
        arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        name: Optional[
            "aws_sdk_notifications.types.notification_configuration_name.NotificationConfigurationName"
        ] = None,
        description: Optional[
            "aws_sdk_notifications.types.notification_configuration_description.NotificationConfigurationDescription"
        ] = None,
        aggregation_duration: Optional[
            "aws_sdk_notifications.types.aggregation_duration.AggregationDuration"
        ] = None,
    ) -> "aws_sdk_notifications.types.update_notification_configuration_response.UpdateNotificationConfigurationResponse":
        """<p>Updates a <code>NotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) used to update the <code>NotificationConfiguration</code>.</p>
            name: <p>The name of the <code>NotificationConfiguration</code>.</p>
            description: <p>The description of the <code>NotificationConfiguration</code>.</p>
            aggregation_duration: <p>The aggregation preference of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>LONG</code> </p> <ul> <li> <p>Aggregate notifications for long periods of time (12 hours).</p> </li> </ul> </li> <li> <p> <code>SHORT</code> </p> <ul> <li> <p>Aggregate notifications for short periods of time (5 minutes).</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>Don't aggregate notifications.</p> </li> </ul> </li> </ul> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.update_notification_configuration_response.UpdateNotificationConfigurationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.update_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.update_notification_configuration.async_update_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if aggregation_duration is not None:
            input["aggregation_duration"] = aggregation_duration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.get_notification_configuration_response.GetNotificationConfigurationResponse":
        """<p>Returns a specified <code>NotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.get_notification_configuration_request.GetNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.get_notification_configuration_response.GetNotificationConfigurationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.get_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.get_notification_configuration.async_get_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.get_notification_configuration_request.GetNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.delete_notification_configuration_response.DeleteNotificationConfigurationResponse":
        """<p>Deletes a <code>NotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.delete_notification_configuration_response.DeleteNotificationConfigurationResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.delete_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.delete_notification_configuration.async_delete_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
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
        event_rule_source: Optional["aws_sdk_notifications.types.source.Source"] = None,
        channel_arn: Optional[
            "aws_sdk_notifications.types.channel_arn.ChannelArn"
        ] = None,
        status: Optional[
            "aws_sdk_notifications.types.notification_configuration_status.NotificationConfigurationStatus"
        ] = None,
        subtype: Optional[
            "aws_sdk_notifications.types.notification_configuration_subtype.NotificationConfigurationSubtype"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse":
        """<p>Returns a list of abbreviated <code>NotificationConfigurations</code> according to specified filters, in reverse chronological order (newest first).</p>

        Args:
            event_rule_source: <p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level\">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to match.</p>
            status: <p>The <code>NotificationConfiguration</code> status to match.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>ACTIVE</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>ACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>PARTIALLY_ACTIVE</code> </p> <ul> <li> <p>Some <code>EventRules</code> are <code>ACTIVE</code> and some are <code>INACTIVE</code>. Any call can be run.</p> </li> <li> <p>Any call can be run.</p> </li> </ul> </li> <li> <p> <code>INACTIVE</code> </p> <ul> <li> <p>All <code>EventRules</code> are <code>INACTIVE</code> and any call can be run.</p> </li> </ul> </li> <li> <p> <code>DELETING</code> </p> <ul> <li> <p>This <code>NotificationConfiguration</code> is being deleted.</p> </li> <li> <p>Only <code>GET</code> and <code>LIST</code> calls can be run.</p> </li> </ul> </li> </ul> </li> </ul>
            subtype: <p>The subtype used to filter the notification configurations in the request.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.list_notification_configurations_request.ListNotificationConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.list_notification_configurations_response.ListNotificationConfigurationsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_notification_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.list_notification_configurations.async_list_notification_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_notifications.types.list_notification_configurations_request.ListNotificationConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if event_rule_source is not None:
            input["event_rule_source"] = event_rule_source
        if channel_arn is not None:
            input["channel_arn"] = channel_arn
        if status is not None:
            input["status"] = status
        if subtype is not None:
            input["subtype"] = subtype
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
