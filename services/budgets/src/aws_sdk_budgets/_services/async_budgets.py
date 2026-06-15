"""Generated from Smithy shape ``com.amazonaws.budgets#AWSBudgetServiceGateway``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_budgets._auth._signers
import aws_sdk_budgets._auth._sigv4
from aws_sdk_budgets._auth._identity import Credentials
from aws_sdk_budgets._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_budgets._auth._zapros_handler import AuthMiddleware
from aws_sdk_budgets._pagination import resolve_path as _resolve_path
from aws_sdk_budgets._services._aws_config import aaws_config
from aws_sdk_budgets._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.action
    import aws_sdk_budgets.types.action_history
    import aws_sdk_budgets.types.action_id
    import aws_sdk_budgets.types.action_threshold
    import aws_sdk_budgets.types.action_type
    import aws_sdk_budgets.types.amazon_resource_name
    import aws_sdk_budgets.types.approval_model
    import aws_sdk_budgets.types.budget
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.budget_notifications_for_account
    import aws_sdk_budgets.types.create_budget_action_request
    import aws_sdk_budgets.types.create_budget_action_response
    import aws_sdk_budgets.types.create_budget_request
    import aws_sdk_budgets.types.create_budget_response
    import aws_sdk_budgets.types.create_notification_request
    import aws_sdk_budgets.types.create_notification_response
    import aws_sdk_budgets.types.create_subscriber_request
    import aws_sdk_budgets.types.create_subscriber_response
    import aws_sdk_budgets.types.definition
    import aws_sdk_budgets.types.delete_budget_action_request
    import aws_sdk_budgets.types.delete_budget_action_response
    import aws_sdk_budgets.types.delete_budget_request
    import aws_sdk_budgets.types.delete_budget_response
    import aws_sdk_budgets.types.delete_notification_request
    import aws_sdk_budgets.types.delete_notification_response
    import aws_sdk_budgets.types.delete_subscriber_request
    import aws_sdk_budgets.types.delete_subscriber_response
    import aws_sdk_budgets.types.describe_budget_action_histories_request
    import aws_sdk_budgets.types.describe_budget_action_histories_response
    import aws_sdk_budgets.types.describe_budget_action_request
    import aws_sdk_budgets.types.describe_budget_action_response
    import aws_sdk_budgets.types.describe_budget_actions_for_account_request
    import aws_sdk_budgets.types.describe_budget_actions_for_account_response
    import aws_sdk_budgets.types.describe_budget_actions_for_budget_request
    import aws_sdk_budgets.types.describe_budget_actions_for_budget_response
    import aws_sdk_budgets.types.describe_budget_notifications_for_account_request
    import aws_sdk_budgets.types.describe_budget_notifications_for_account_response
    import aws_sdk_budgets.types.describe_budget_performance_history_request
    import aws_sdk_budgets.types.describe_budget_performance_history_response
    import aws_sdk_budgets.types.describe_budget_request
    import aws_sdk_budgets.types.describe_budget_response
    import aws_sdk_budgets.types.describe_budgets_request
    import aws_sdk_budgets.types.describe_budgets_response
    import aws_sdk_budgets.types.describe_notifications_for_budget_request
    import aws_sdk_budgets.types.describe_notifications_for_budget_response
    import aws_sdk_budgets.types.describe_subscribers_for_notification_request
    import aws_sdk_budgets.types.describe_subscribers_for_notification_response
    import aws_sdk_budgets.types.execute_budget_action_request
    import aws_sdk_budgets.types.execute_budget_action_response
    import aws_sdk_budgets.types.execution_type
    import aws_sdk_budgets.types.generic_string
    import aws_sdk_budgets.types.list_tags_for_resource_request
    import aws_sdk_budgets.types.list_tags_for_resource_response
    import aws_sdk_budgets.types.max_results
    import aws_sdk_budgets.types.max_results_budget_notifications
    import aws_sdk_budgets.types.max_results_describe_budgets
    import aws_sdk_budgets.types.notification
    import aws_sdk_budgets.types.notification_type
    import aws_sdk_budgets.types.notification_with_subscribers_list
    import aws_sdk_budgets.types.nullable_boolean
    import aws_sdk_budgets.types.resource_tag_key_list
    import aws_sdk_budgets.types.resource_tag_list
    import aws_sdk_budgets.types.role_arn
    import aws_sdk_budgets.types.subscriber
    import aws_sdk_budgets.types.subscribers
    import aws_sdk_budgets.types.tag_resource_request
    import aws_sdk_budgets.types.tag_resource_response
    import aws_sdk_budgets.types.time_period
    import aws_sdk_budgets.types.untag_resource_request
    import aws_sdk_budgets.types.untag_resource_response
    import aws_sdk_budgets.types.update_budget_action_request
    import aws_sdk_budgets.types.update_budget_action_response
    import aws_sdk_budgets.types.update_budget_request
    import aws_sdk_budgets.types.update_budget_response
    import aws_sdk_budgets.types.update_notification_request
    import aws_sdk_budgets.types.update_notification_response
    import aws_sdk_budgets.types.update_subscriber_request
    import aws_sdk_budgets.types.update_subscriber_response


class AsyncBudgetsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


class AsyncBudgetsClient:
    """A client for the ``Budgets`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncBudgetsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncBudgetsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBudgetsClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def create_budget(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget: "aws_sdk_budgets.types.budget.Budget",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        notifications_with_subscribers: Optional[
            "aws_sdk_budgets.types.notification_with_subscribers_list.NotificationWithSubscribersList"
        ] = None,
        resource_tags: Optional[
            "aws_sdk_budgets.types.resource_tag_list.ResourceTagList"
        ] = None,
    ) -> "aws_sdk_budgets.types.create_budget_response.CreateBudgetResponse":
        r"""<p>Creates a budget and, if included, notifications and subscribers. </p> <important> <p>Only one of <code>BudgetLimit</code> or <code>PlannedBudgetLimits</code> can be present in the syntax at one time. Use the syntax that matches your use case. The Request Syntax section shows the <code>BudgetLimit</code> syntax. For <code>PlannedBudgetLimits</code>, see the <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateBudget.html#API_CreateBudget_Examples\">Examples</a> section.</p> <p>Similarly, only one set of filter and metric selections can be present in the syntax at one time. Either <code>FilterExpression</code> and <code>Metrics</code> or <code>CostFilters</code> and <code>CostTypes</code>, not both or a different combination. We recommend using <code>FilterExpression</code> and <code>Metrics</code> as they provide more flexible and powerful filtering capabilities. The Request Syntax section shows the <code>FilterExpression</code>/<code>Metrics</code> syntax.</p> </important>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget.</p>
            budget: <p>The budget object that you want to create.</p>
            notifications_with_subscribers: <p>A notification that you want to associate with a budget. A budget can have up to five notifications, and each notification can have one SNS subscriber and up to 10 email subscribers. If you include notifications and subscribers in your <code>CreateBudget</code> call, Amazon Web Services creates the notifications and subscribers for you.</p>
            resource_tags: <p>An optional list of tags to associate with the specified budget. Each tag consists of a key and a value, and each key must be unique for the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.create_budget_request.CreateBudgetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.create_budget_response.CreateBudgetResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.create_budget

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.create_budget.async_create_budget(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.create_budget_request.CreateBudgetRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget"] = budget
        if notifications_with_subscribers is not None:
            input_["notifications_with_subscribers"] = notifications_with_subscribers
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_budget_action(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        notification_type: "aws_sdk_budgets.types.notification_type.NotificationType",
        action_type: "aws_sdk_budgets.types.action_type.ActionType",
        action_threshold: "aws_sdk_budgets.types.action_threshold.ActionThreshold",
        definition: "aws_sdk_budgets.types.definition.Definition",
        execution_role_arn: "aws_sdk_budgets.types.role_arn.RoleArn",
        approval_model: "aws_sdk_budgets.types.approval_model.ApprovalModel",
        subscribers: "aws_sdk_budgets.types.subscribers.Subscribers",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        resource_tags: Optional[
            "aws_sdk_budgets.types.resource_tag_list.ResourceTagList"
        ] = None,
    ) -> (
        "aws_sdk_budgets.types.create_budget_action_response.CreateBudgetActionResponse"
    ):
        """<p> Creates a budget action. </p>

        Args:
            action_type: <p> The type of action. This defines the type of tasks that can be carried out by this action. This field also determines the format for definition. </p>
            execution_role_arn: <p> The role passed for action execution and reversion. Roles and actions must be in the same account. </p>
            approval_model: <p> This specifies if the action needs manual or automatic approval. </p>
            resource_tags: <p>An optional list of tags to associate with the specified budget action. Each tag consists of a key and a value, and each key must be unique for the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.create_budget_action_request.CreateBudgetActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.create_budget_action_response.CreateBudgetActionResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.create_budget_action

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.create_budget_action.async_create_budget_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.create_budget_action_request.CreateBudgetActionRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["notification_type"] = notification_type
        input_["action_type"] = action_type
        input_["action_threshold"] = action_threshold
        input_["definition"] = definition
        input_["execution_role_arn"] = execution_role_arn
        input_["approval_model"] = approval_model
        input_["subscribers"] = subscribers
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_notification(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        notification: "aws_sdk_budgets.types.notification.Notification",
        subscribers: "aws_sdk_budgets.types.subscribers.Subscribers",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> (
        "aws_sdk_budgets.types.create_notification_response.CreateNotificationResponse"
    ):
        """<p>Creates a notification. You must create the budget before you create the associated notification.</p>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget that you want to create a notification for.</p>
            budget_name: <p>The name of the budget that you want Amazon Web Services to notify you about. Budget names must be unique within an account.</p>
            notification: <p>The notification that you want to create.</p>
            subscribers: <p>A list of subscribers that you want to associate with the notification. Each notification can have one SNS subscriber and up to 10 email subscribers.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.create_notification_request.CreateNotificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.create_notification_response.CreateNotificationResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.create_notification

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.create_notification.async_create_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.create_notification_request.CreateNotificationRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["notification"] = notification
        input_["subscribers"] = subscribers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_subscriber(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        notification: "aws_sdk_budgets.types.notification.Notification",
        subscriber: "aws_sdk_budgets.types.subscriber.Subscriber",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> "aws_sdk_budgets.types.create_subscriber_response.CreateSubscriberResponse":
        """<p>Creates a subscriber. You must create the associated budget and notification before you create the subscriber.</p>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget that you want to create a subscriber for.</p>
            budget_name: <p>The name of the budget that you want to subscribe to. Budget names must be unique within an account.</p>
            notification: <p>The notification that you want to create a subscriber for.</p>
            subscriber: <p>The subscriber that you want to associate with a budget notification.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.create_subscriber_request.CreateSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.create_subscriber_response.CreateSubscriberResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.create_subscriber

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.create_subscriber.async_create_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.create_subscriber_request.CreateSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["notification"] = notification
        input_["subscriber"] = subscriber

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_budget(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> "aws_sdk_budgets.types.delete_budget_response.DeleteBudgetResponse":
        """<p>Deletes a budget. You can delete your budget at any time.</p> <important> <p>Deleting a budget also deletes the notifications and subscribers that are associated with that budget.</p> </important>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget that you want to delete.</p>
            budget_name: <p>The name of the budget that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.delete_budget_request.DeleteBudgetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.delete_budget_response.DeleteBudgetResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.delete_budget

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.delete_budget.async_delete_budget(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.delete_budget_request.DeleteBudgetRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_budget_action(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        action_id: "aws_sdk_budgets.types.action_id.ActionId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> (
        "aws_sdk_budgets.types.delete_budget_action_response.DeleteBudgetActionResponse"
    ):
        """<p> Deletes a budget action. </p>

        Args:
            action_id: <p> A system-generated universally unique identifier (UUID) for the action. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.delete_budget_action_request.DeleteBudgetActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.delete_budget_action_response.DeleteBudgetActionResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.delete_budget_action

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.delete_budget_action.async_delete_budget_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.delete_budget_action_request.DeleteBudgetActionRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["action_id"] = action_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_notification(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        notification: "aws_sdk_budgets.types.notification.Notification",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> (
        "aws_sdk_budgets.types.delete_notification_response.DeleteNotificationResponse"
    ):
        """<p>Deletes a notification.</p> <important> <p>Deleting a notification also deletes the subscribers that are associated with the notification.</p> </important>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget whose notification you want to delete.</p>
            budget_name: <p>The name of the budget whose notification you want to delete.</p>
            notification: <p>The notification that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.delete_notification_request.DeleteNotificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.delete_notification_response.DeleteNotificationResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.delete_notification

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.delete_notification.async_delete_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.delete_notification_request.DeleteNotificationRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["notification"] = notification

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_subscriber(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        notification: "aws_sdk_budgets.types.notification.Notification",
        subscriber: "aws_sdk_budgets.types.subscriber.Subscriber",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> "aws_sdk_budgets.types.delete_subscriber_response.DeleteSubscriberResponse":
        """<p>Deletes a subscriber.</p> <important> <p>Deleting the last subscriber to a notification also deletes the notification.</p> </important>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget whose subscriber you want to delete.</p>
            budget_name: <p>The name of the budget whose subscriber you want to delete.</p>
            notification: <p>The notification whose subscriber you want to delete.</p>
            subscriber: <p>The subscriber that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.delete_subscriber_request.DeleteSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.delete_subscriber_response.DeleteSubscriberResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.delete_subscriber

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.delete_subscriber.async_delete_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.delete_subscriber_request.DeleteSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["notification"] = notification
        input_["subscriber"] = subscriber

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_budget(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        show_filter_expression: Optional[
            "aws_sdk_budgets.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_budgets.types.describe_budget_response.DescribeBudgetResponse":
        r"""<p>Describes a budget.</p> <important> <p>The Request Syntax section shows the <code>BudgetLimit</code> syntax. For <code>PlannedBudgetLimits</code>, see the <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudget.html#API_DescribeBudget_Examples\">Examples</a> section.</p> </important>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget that you want a description of.</p>
            budget_name: <p>The name of the budget that you want a description of.</p>
            show_filter_expression: <p>Specifies whether the response includes the filter expression associated with the budget. By showing the filter expression, you can see detailed filtering logic applied to the budget, such as Amazon Web Services services or tags that are being tracked.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.describe_budget_request.DescribeBudgetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.describe_budget_response.DescribeBudgetResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget.async_describe_budget(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.describe_budget_request.DescribeBudgetRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        if show_filter_expression is not None:
            input_["show_filter_expression"] = show_filter_expression

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_budget_action(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        action_id: "aws_sdk_budgets.types.action_id.ActionId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> "aws_sdk_budgets.types.describe_budget_action_response.DescribeBudgetActionResponse":
        """<p> Describes a budget action detail. </p>

        Args:
            action_id: <p> A system-generated universally unique identifier (UUID) for the action. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.describe_budget_action_request.DescribeBudgetActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.describe_budget_action_response.DescribeBudgetActionResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_action

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_action.async_describe_budget_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.describe_budget_action_request.DescribeBudgetActionRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["action_id"] = action_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_budget_action_histories(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        action_id: "aws_sdk_budgets.types.action_id.ActionId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        time_period: Optional["aws_sdk_budgets.types.time_period.TimePeriod"] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "aws_sdk_budgets.types.describe_budget_action_histories_response.DescribeBudgetActionHistoriesResponse":
        """<p> Describes a budget action history detail. </p>

        Args:
            action_id: <p> A system-generated universally unique identifier (UUID) for the action. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.describe_budget_action_histories_request.DescribeBudgetActionHistoriesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.describe_budget_action_histories_response.DescribeBudgetActionHistoriesResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_action_histories

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_action_histories.async_describe_budget_action_histories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.describe_budget_action_histories_request.DescribeBudgetActionHistoriesRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["action_id"] = action_id
        if time_period is not None:
            input_["time_period"] = time_period
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

    async def iter_describe_budget_action_histories(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        action_id: "aws_sdk_budgets.types.action_id.ActionId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        time_period: Optional["aws_sdk_budgets.types.time_period.TimePeriod"] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_budgets.types.action_history.ActionHistory]":
        _token = next_token
        while True:
            _response = await self.describe_budget_action_histories(
                account_id,
                budget_name,
                action_id,
                config_overrides=config_overrides,
                time_period=time_period,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("action_histories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_budget_actions_for_account(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "aws_sdk_budgets.types.describe_budget_actions_for_account_response.DescribeBudgetActionsForAccountResponse":
        """<p> Describes all of the budget actions for an account. </p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.describe_budget_actions_for_account_request.DescribeBudgetActionsForAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.describe_budget_actions_for_account_response.DescribeBudgetActionsForAccountResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_actions_for_account

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_actions_for_account.async_describe_budget_actions_for_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.describe_budget_actions_for_account_request.DescribeBudgetActionsForAccountRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
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

    async def iter_describe_budget_actions_for_account(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_budgets.types.action.Action]":
        _token = next_token
        while True:
            _response = await self.describe_budget_actions_for_account(
                account_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_budget_actions_for_budget(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "aws_sdk_budgets.types.describe_budget_actions_for_budget_response.DescribeBudgetActionsForBudgetResponse":
        """<p> Describes all of the budget actions for a budget. </p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.describe_budget_actions_for_budget_request.DescribeBudgetActionsForBudgetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.describe_budget_actions_for_budget_response.DescribeBudgetActionsForBudgetResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_actions_for_budget

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_actions_for_budget.async_describe_budget_actions_for_budget(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.describe_budget_actions_for_budget_request.DescribeBudgetActionsForBudgetRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
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

    async def iter_describe_budget_actions_for_budget(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_budgets.types.action.Action]":
        _token = next_token
        while True:
            _response = await self.describe_budget_actions_for_budget(
                account_id,
                budget_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_budget_notifications_for_account(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_budgets.types.max_results_budget_notifications.MaxResultsBudgetNotifications"
        ] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "aws_sdk_budgets.types.describe_budget_notifications_for_account_response.DescribeBudgetNotificationsForAccountResponse":
        """<p> Lists the budget names and notifications that are associated with an account. </p>

        Args:
            max_results: <p> An integer that represents how many budgets a paginated response contains. The default is 50. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.describe_budget_notifications_for_account_request.DescribeBudgetNotificationsForAccountRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.describe_budget_notifications_for_account_response.DescribeBudgetNotificationsForAccountResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_notifications_for_account

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_notifications_for_account.async_describe_budget_notifications_for_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.describe_budget_notifications_for_account_request.DescribeBudgetNotificationsForAccountRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
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

    async def iter_describe_budget_notifications_for_account(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_budgets.types.max_results_budget_notifications.MaxResultsBudgetNotifications"
        ] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_budgets.types.budget_notifications_for_account.BudgetNotificationsForAccount]":
        _token = next_token
        while True:
            _response = await self.describe_budget_notifications_for_account(
                account_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("budget_notifications_for_account",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_budget_performance_history(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        time_period: Optional["aws_sdk_budgets.types.time_period.TimePeriod"] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "aws_sdk_budgets.types.describe_budget_performance_history_response.DescribeBudgetPerformanceHistoryResponse":
        """<p>Describes the history for <code>DAILY</code>, <code>MONTHLY</code>, and <code>QUARTERLY</code> budgets. Budget history isn't available for <code>ANNUAL</code> budgets.</p>

        Args:
            time_period: <p>Retrieves how often the budget went into an <code>ALARM</code> state for the specified time period.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.describe_budget_performance_history_request.DescribeBudgetPerformanceHistoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.describe_budget_performance_history_response.DescribeBudgetPerformanceHistoryResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_performance_history

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budget_performance_history.async_describe_budget_performance_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.describe_budget_performance_history_request.DescribeBudgetPerformanceHistoryRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        if time_period is not None:
            input_["time_period"] = time_period
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

    async def describe_budgets(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_budgets.types.max_results_describe_budgets.MaxResultsDescribeBudgets"
        ] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
        show_filter_expression: Optional[
            "aws_sdk_budgets.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "aws_sdk_budgets.types.describe_budgets_response.DescribeBudgetsResponse":
        r"""<p>Lists the budgets that are associated with an account.</p> <important> <p>The Request Syntax section shows the <code>BudgetLimit</code> syntax. For <code>PlannedBudgetLimits</code>, see the <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgets.html#API_DescribeBudgets_Examples\">Examples</a> section.</p> </important>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budgets that you want to describe.</p>
            max_results: <p>An integer that represents how many budgets a paginated response contains. The default is 100.</p>
            next_token: <p>The pagination token that you include in your request to indicate the next set of results that you want to retrieve.</p>
            show_filter_expression: <p>Specifies whether the response includes the filter expression associated with the budgets. By showing the filter expression, you can see detailed filtering logic applied to the budgets, such as Amazon Web Services services or tags that are being tracked.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.describe_budgets_request.DescribeBudgetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.describe_budgets_response.DescribeBudgetsResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budgets

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.describe_budgets.async_describe_budgets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.describe_budgets_request.DescribeBudgetsRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if show_filter_expression is not None:
            input_["show_filter_expression"] = show_filter_expression

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_budgets(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_budgets.types.max_results_describe_budgets.MaxResultsDescribeBudgets"
        ] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
        show_filter_expression: Optional[
            "aws_sdk_budgets.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_budgets.types.budget.Budget]":
        _token = next_token
        while True:
            _response = await self.describe_budgets(
                account_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                show_filter_expression=show_filter_expression,
            )
            _page = _resolve_path(_response, ("budgets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_notifications_for_budget(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "aws_sdk_budgets.types.describe_notifications_for_budget_response.DescribeNotificationsForBudgetResponse":
        """<p>Lists the notifications that are associated with a budget.</p>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget whose notifications you want descriptions of.</p>
            budget_name: <p>The name of the budget whose notifications you want descriptions of.</p>
            max_results: <p>An optional integer that represents how many entries a paginated response contains.</p>
            next_token: <p>The pagination token that you include in your request to indicate the next set of results that you want to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.describe_notifications_for_budget_request.DescribeNotificationsForBudgetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.describe_notifications_for_budget_response.DescribeNotificationsForBudgetResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.describe_notifications_for_budget

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.describe_notifications_for_budget.async_describe_notifications_for_budget(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.describe_notifications_for_budget_request.DescribeNotificationsForBudgetRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
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

    async def iter_describe_notifications_for_budget(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_budgets.types.notification.Notification]":
        _token = next_token
        while True:
            _response = await self.describe_notifications_for_budget(
                account_id,
                budget_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("notifications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_subscribers_for_notification(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        notification: "aws_sdk_budgets.types.notification.Notification",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "aws_sdk_budgets.types.describe_subscribers_for_notification_response.DescribeSubscribersForNotificationResponse":
        """<p>Lists the subscribers that are associated with a notification.</p>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget whose subscribers you want descriptions of.</p>
            budget_name: <p>The name of the budget whose subscribers you want descriptions of.</p>
            notification: <p>The notification whose subscribers you want to list.</p>
            max_results: <p>An optional integer that represents how many entries a paginated response contains.</p>
            next_token: <p>The pagination token that you include in your request to indicate the next set of results that you want to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.describe_subscribers_for_notification_request.DescribeSubscribersForNotificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.describe_subscribers_for_notification_response.DescribeSubscribersForNotificationResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.describe_subscribers_for_notification

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.describe_subscribers_for_notification.async_describe_subscribers_for_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.describe_subscribers_for_notification_request.DescribeSubscribersForNotificationRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["notification"] = notification
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

    async def iter_describe_subscribers_for_notification(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        notification: "aws_sdk_budgets.types.notification.Notification",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        max_results: Optional["aws_sdk_budgets.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_budgets.types.generic_string.GenericString"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_budgets.types.subscriber.Subscriber]":
        _token = next_token
        while True:
            _response = await self.describe_subscribers_for_notification(
                account_id,
                budget_name,
                notification,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("subscribers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def execute_budget_action(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        action_id: "aws_sdk_budgets.types.action_id.ActionId",
        execution_type: "aws_sdk_budgets.types.execution_type.ExecutionType",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> "aws_sdk_budgets.types.execute_budget_action_response.ExecuteBudgetActionResponse":
        """<p> Executes a budget action. </p>

        Args:
            action_id: <p> A system-generated universally unique identifier (UUID) for the action. </p>
            execution_type: <p> The type of execution. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.execute_budget_action_request.ExecuteBudgetActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.execute_budget_action_response.ExecuteBudgetActionResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.execute_budget_action

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.execute_budget_action.async_execute_budget_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.execute_budget_action_request.ExecuteBudgetActionRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["action_id"] = action_id
        input_["execution_type"] = execution_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_budgets.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> "aws_sdk_budgets.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags associated with a budget or budget action resource.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_budgets.types.amazon_resource_name.AmazonResourceName",
        resource_tags: "aws_sdk_budgets.types.resource_tag_list.ResourceTagList",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> "aws_sdk_budgets.types.tag_resource_response.TagResourceResponse":
        """<p>Creates tags for a budget or budget action resource.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
            resource_tags: <p>The tags associated with the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["resource_tags"] = resource_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_budgets.types.amazon_resource_name.AmazonResourceName",
        resource_tag_keys: "aws_sdk_budgets.types.resource_tag_key_list.ResourceTagKeyList",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> "aws_sdk_budgets.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes tags associated with a budget or budget action resource.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
            resource_tag_keys: <p>The key that's associated with the tag.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["resource_tag_keys"] = resource_tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_budget(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        new_budget: "aws_sdk_budgets.types.budget.Budget",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> "aws_sdk_budgets.types.update_budget_response.UpdateBudgetResponse":
        r"""<p>Updates a budget. You can change every part of a budget except for the <code>budgetName</code> and the <code>calculatedSpend</code>. When you modify a budget, the <code>calculatedSpend</code> drops to zero until Amazon Web Services has new usage data to use for forecasting.</p> <important> <p>Only one of <code>BudgetLimit</code> or <code>PlannedBudgetLimits</code> can be present in the syntax at one time. Use the syntax that matches your case. The Request Syntax section shows the <code>BudgetLimit</code> syntax. For <code>PlannedBudgetLimits</code>, see the <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateBudget.html#API_UpdateBudget_Examples\">Examples</a> section.</p> <p>Similarly, only one set of filter and metric selections can be present in the syntax at one time. Either <code>FilterExpression</code> and <code>Metrics</code> or <code>CostFilters</code> and <code>CostTypes</code>, not both or a different combination. We recommend using <code>FilterExpression</code> and <code>Metrics</code> as they provide more flexible and powerful filtering capabilities. The Request Syntax section shows the <code>FilterExpression</code>/<code>Metrics</code> syntax.</p> </important>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget that you want to update.</p>
            new_budget: <p>The budget that you want to update your budget to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.update_budget_request.UpdateBudgetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.update_budget_response.UpdateBudgetResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.update_budget

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.update_budget.async_update_budget(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.update_budget_request.UpdateBudgetRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["new_budget"] = new_budget

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_budget_action(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        action_id: "aws_sdk_budgets.types.action_id.ActionId",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
        notification_type: Optional[
            "aws_sdk_budgets.types.notification_type.NotificationType"
        ] = None,
        action_threshold: Optional[
            "aws_sdk_budgets.types.action_threshold.ActionThreshold"
        ] = None,
        definition: Optional["aws_sdk_budgets.types.definition.Definition"] = None,
        execution_role_arn: Optional["aws_sdk_budgets.types.role_arn.RoleArn"] = None,
        approval_model: Optional[
            "aws_sdk_budgets.types.approval_model.ApprovalModel"
        ] = None,
        subscribers: Optional["aws_sdk_budgets.types.subscribers.Subscribers"] = None,
    ) -> (
        "aws_sdk_budgets.types.update_budget_action_response.UpdateBudgetActionResponse"
    ):
        """<p> Updates a budget action. </p>

        Args:
            action_id: <p> A system-generated universally unique identifier (UUID) for the action. </p>
            execution_role_arn: <p> The role passed for action execution and reversion. Roles and actions must be in the same account. </p>
            approval_model: <p> This specifies if the action needs manual or automatic approval. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.update_budget_action_request.UpdateBudgetActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.update_budget_action_response.UpdateBudgetActionResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.update_budget_action

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.update_budget_action.async_update_budget_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.update_budget_action_request.UpdateBudgetActionRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["action_id"] = action_id
        if notification_type is not None:
            input_["notification_type"] = notification_type
        if action_threshold is not None:
            input_["action_threshold"] = action_threshold
        if definition is not None:
            input_["definition"] = definition
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if approval_model is not None:
            input_["approval_model"] = approval_model
        if subscribers is not None:
            input_["subscribers"] = subscribers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_notification(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        old_notification: "aws_sdk_budgets.types.notification.Notification",
        new_notification: "aws_sdk_budgets.types.notification.Notification",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> (
        "aws_sdk_budgets.types.update_notification_response.UpdateNotificationResponse"
    ):
        """<p>Updates a notification.</p>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget whose notification you want to update.</p>
            budget_name: <p>The name of the budget whose notification you want to update.</p>
            old_notification: <p>The previous notification that is associated with a budget.</p>
            new_notification: <p>The updated notification to be associated with a budget.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.update_notification_request.UpdateNotificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.update_notification_response.UpdateNotificationResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.update_notification

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.update_notification.async_update_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.update_notification_request.UpdateNotificationRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["old_notification"] = old_notification
        input_["new_notification"] = new_notification

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_subscriber(
        self,
        account_id: "aws_sdk_budgets.types.account_id.AccountId",
        budget_name: "aws_sdk_budgets.types.budget_name.BudgetName",
        notification: "aws_sdk_budgets.types.notification.Notification",
        old_subscriber: "aws_sdk_budgets.types.subscriber.Subscriber",
        new_subscriber: "aws_sdk_budgets.types.subscriber.Subscriber",
        *,
        config_overrides: Optional[AsyncBudgetsClientConfig] = None,
    ) -> "aws_sdk_budgets.types.update_subscriber_response.UpdateSubscriberResponse":
        """<p>Updates a subscriber.</p>

        Args:
            account_id: <p>The <code>accountId</code> that is associated with the budget whose subscriber you want to update.</p>
            budget_name: <p>The name of the budget whose subscriber you want to update.</p>
            notification: <p>The notification whose subscriber you want to update.</p>
            old_subscriber: <p>The previous subscriber that is associated with a budget notification.</p>
            new_subscriber: <p>The updated subscriber that is associated with a budget notification.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_budgets.types.update_subscriber_request.UpdateSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_budgets.types.update_subscriber_response.UpdateSubscriberResponse"
        ]:
            import aws_sdk_budgets._operations.aws_budget_service_gateway.update_subscriber

            (
                output,
                http_response,
            ) = await aws_sdk_budgets._operations.aws_budget_service_gateway.update_subscriber.async_update_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_budgets.types.update_subscriber_request.UpdateSubscriberRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id
        input_["budget_name"] = budget_name
        input_["notification"] = notification
        input_["old_subscriber"] = old_subscriber
        input_["new_subscriber"] = new_subscriber

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
