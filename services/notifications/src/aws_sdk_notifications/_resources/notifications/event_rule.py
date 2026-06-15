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
    import aws_sdk_notifications.types.create_event_rule_request
    import aws_sdk_notifications.types.create_event_rule_response
    import aws_sdk_notifications.types.delete_event_rule_request
    import aws_sdk_notifications.types.delete_event_rule_response
    import aws_sdk_notifications.types.event_rule_arn
    import aws_sdk_notifications.types.event_rule_event_pattern
    import aws_sdk_notifications.types.event_rule_structure
    import aws_sdk_notifications.types.event_type
    import aws_sdk_notifications.types.get_event_rule_request
    import aws_sdk_notifications.types.get_event_rule_response
    import aws_sdk_notifications.types.list_event_rules_request
    import aws_sdk_notifications.types.list_event_rules_response
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.regions
    import aws_sdk_notifications.types.source
    import aws_sdk_notifications.types.update_event_rule_request
    import aws_sdk_notifications.types.update_event_rule_response
    from aws_sdk_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from aws_sdk_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class EventRule:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def create(
        self,
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        source: "aws_sdk_notifications.types.source.Source",
        event_type: "aws_sdk_notifications.types.event_type.EventType",
        regions: "aws_sdk_notifications.types.regions.Regions",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        event_pattern: Optional[
            "aws_sdk_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
        ] = None,
    ) -> (
        "aws_sdk_notifications.types.create_event_rule_response.CreateEventRuleResponse"
    ):
        r"""<p>Creates an <a href=\"https://docs.aws.amazon.com/notifications/latest/userguide/glossary.html\"> <code>EventRule</code> </a> that is associated with a specified <code>NotificationConfiguration</code>.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> associated with this <code>EventRule</code>.</p>
            source: <p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level\">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            event_type: <p>The event type to match.</p> <p>Must match one of the valid Amazon EventBridge event types. For example, EC2 Instance State-change Notification and Amazon CloudWatch Alarm State Change. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level\">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            event_pattern: <p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html\">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>
            regions: <p>A list of Amazon Web Services Regions that send events to this <code>EventRule</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.create_event_rule_request.CreateEventRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.create_event_rule_response.CreateEventRuleResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.create_event_rule

            output, http_response = (
                aws_sdk_notifications._operations.notifications.create_event_rule.create_event_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.create_event_rule_request.CreateEventRuleRequest = {}  # type: ignore[typeddict-item]
        input_["notification_configuration_arn"] = notification_configuration_arn
        input_["source"] = source
        input_["event_type"] = event_type
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern
        input_["regions"] = regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put(
        self,
        arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        event_pattern: Optional[
            "aws_sdk_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
        ] = None,
        regions: Optional["aws_sdk_notifications.types.regions.Regions"] = None,
    ) -> (
        "aws_sdk_notifications.types.update_event_rule_response.UpdateEventRuleResponse"
    ):
        r"""<p>Updates an existing <code>EventRule</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) to use to update the <code>EventRule</code>.</p>
            event_pattern: <p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html\">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>
            regions: <p>A list of Amazon Web Services Regions that sends events to this <code>EventRule</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.update_event_rule_request.UpdateEventRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.update_event_rule_response.UpdateEventRuleResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.update_event_rule

            output, http_response = (
                aws_sdk_notifications._operations.notifications.update_event_rule.update_event_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.update_event_rule_request.UpdateEventRuleRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern
        if regions is not None:
            input_["regions"] = regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.get_event_rule_response.GetEventRuleResponse":
        """<p>Returns a specified <code>EventRule</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>EventRule</code> to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.get_event_rule_request.GetEventRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.get_event_rule_response.GetEventRuleResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.get_event_rule

            output, http_response = (
                aws_sdk_notifications._operations.notifications.get_event_rule.get_event_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.get_event_rule_request.GetEventRuleRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> (
        "aws_sdk_notifications.types.delete_event_rule_response.DeleteEventRuleResponse"
    ):
        """<p>Deletes an <code>EventRule</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>EventRule</code> to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.delete_event_rule_request.DeleteEventRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.delete_event_rule_response.DeleteEventRuleResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.delete_event_rule

            output, http_response = (
                aws_sdk_notifications._operations.notifications.delete_event_rule.delete_event_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.delete_event_rule_request.DeleteEventRuleRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_event_rules_response.ListEventRulesResponse":
        """<p>Returns a list of <code>EventRules</code> according to specified filters, in reverse chronological order (newest first).</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code>.</p>
            max_results: <p>The maximum number of results to be returned in this call. The default value is 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notifications.types.list_event_rules_request.ListEventRulesRequest]",
        ) -> OperationResponse[
            "aws_sdk_notifications.types.list_event_rules_response.ListEventRulesResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_event_rules

            output, http_response = (
                aws_sdk_notifications._operations.notifications.list_event_rules.list_event_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.list_event_rules_request.ListEventRulesRequest = {}  # type: ignore[typeddict-item]
        input_["notification_configuration_arn"] = notification_configuration_arn
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


class AsyncEventRule:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def create(
        self,
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        source: "aws_sdk_notifications.types.source.Source",
        event_type: "aws_sdk_notifications.types.event_type.EventType",
        regions: "aws_sdk_notifications.types.regions.Regions",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        event_pattern: Optional[
            "aws_sdk_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
        ] = None,
    ) -> (
        "aws_sdk_notifications.types.create_event_rule_response.CreateEventRuleResponse"
    ):
        r"""<p>Creates an <a href=\"https://docs.aws.amazon.com/notifications/latest/userguide/glossary.html\"> <code>EventRule</code> </a> that is associated with a specified <code>NotificationConfiguration</code>.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code> associated with this <code>EventRule</code>.</p>
            source: <p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level\">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            event_type: <p>The event type to match.</p> <p>Must match one of the valid Amazon EventBridge event types. For example, EC2 Instance State-change Notification and Amazon CloudWatch Alarm State Change. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level\">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            event_pattern: <p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html\">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>
            regions: <p>A list of Amazon Web Services Regions that send events to this <code>EventRule</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.create_event_rule_request.CreateEventRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.create_event_rule_response.CreateEventRuleResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.create_event_rule

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.create_event_rule.async_create_event_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.create_event_rule_request.CreateEventRuleRequest = {}  # type: ignore[typeddict-item]
        input_["notification_configuration_arn"] = notification_configuration_arn
        input_["source"] = source
        input_["event_type"] = event_type
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern
        input_["regions"] = regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put(
        self,
        arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        event_pattern: Optional[
            "aws_sdk_notifications.types.event_rule_event_pattern.EventRuleEventPattern"
        ] = None,
        regions: Optional["aws_sdk_notifications.types.regions.Regions"] = None,
    ) -> (
        "aws_sdk_notifications.types.update_event_rule_response.UpdateEventRuleResponse"
    ):
        r"""<p>Updates an existing <code>EventRule</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) to use to update the <code>EventRule</code>.</p>
            event_pattern: <p>An additional event pattern used to further filter the events this <code>EventRule</code> receives.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html\">Amazon EventBridge event patterns</a> in the <i>Amazon EventBridge User Guide.</i> </p>
            regions: <p>A list of Amazon Web Services Regions that sends events to this <code>EventRule</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.update_event_rule_request.UpdateEventRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.update_event_rule_response.UpdateEventRuleResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.update_event_rule

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.update_event_rule.async_update_event_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.update_event_rule_request.UpdateEventRuleRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern
        if regions is not None:
            input_["regions"] = regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.get_event_rule_response.GetEventRuleResponse":
        """<p>Returns a specified <code>EventRule</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>EventRule</code> to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.get_event_rule_request.GetEventRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.get_event_rule_response.GetEventRuleResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.get_event_rule

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.get_event_rule.async_get_event_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.get_event_rule_request.GetEventRuleRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_notifications.types.event_rule_arn.EventRuleArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> (
        "aws_sdk_notifications.types.delete_event_rule_response.DeleteEventRuleResponse"
    ):
        """<p>Deletes an <code>EventRule</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>EventRule</code> to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.delete_event_rule_request.DeleteEventRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.delete_event_rule_response.DeleteEventRuleResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.delete_event_rule

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.delete_event_rule.async_delete_event_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.delete_event_rule_request.DeleteEventRuleRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_event_rules_response.ListEventRulesResponse":
        """<p>Returns a list of <code>EventRules</code> according to specified filters, in reverse chronological order (newest first).</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code>.</p>
            max_results: <p>The maximum number of results to be returned in this call. The default value is 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.list_event_rules_request.ListEventRulesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.list_event_rules_response.ListEventRulesResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_event_rules

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.list_event_rules.async_list_event_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.list_event_rules_request.ListEventRulesRequest = {}  # type: ignore[typeddict-item]
        input_["notification_configuration_arn"] = notification_configuration_arn
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
