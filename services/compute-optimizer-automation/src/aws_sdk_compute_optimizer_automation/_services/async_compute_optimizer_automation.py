"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ComputeOptimizerAutomationService``."""

import datetime
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

from aws_sdk_compute_optimizer_automation._auth._identity import Credentials
from aws_sdk_compute_optimizer_automation._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_compute_optimizer_automation._auth._zapros_handler import AuthMiddleware
from aws_sdk_compute_optimizer_automation._pagination import (
    resolve_path as _resolve_path,
)
from aws_sdk_compute_optimizer_automation._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.account_id_list
    import aws_sdk_compute_optimizer_automation.types.account_info
    import aws_sdk_compute_optimizer_automation.types.associate_accounts_request
    import aws_sdk_compute_optimizer_automation.types.associate_accounts_response
    import aws_sdk_compute_optimizer_automation.types.automation_event
    import aws_sdk_compute_optimizer_automation.types.automation_event_filter_list
    import aws_sdk_compute_optimizer_automation.types.automation_event_step
    import aws_sdk_compute_optimizer_automation.types.automation_event_summary
    import aws_sdk_compute_optimizer_automation.types.automation_rule
    import aws_sdk_compute_optimizer_automation.types.client_token
    import aws_sdk_compute_optimizer_automation.types.create_automation_rule_request
    import aws_sdk_compute_optimizer_automation.types.create_automation_rule_response
    import aws_sdk_compute_optimizer_automation.types.criteria
    import aws_sdk_compute_optimizer_automation.types.delete_automation_rule_request
    import aws_sdk_compute_optimizer_automation.types.delete_automation_rule_response
    import aws_sdk_compute_optimizer_automation.types.disassociate_accounts_request
    import aws_sdk_compute_optimizer_automation.types.disassociate_accounts_response
    import aws_sdk_compute_optimizer_automation.types.enrollment_status
    import aws_sdk_compute_optimizer_automation.types.event_id
    import aws_sdk_compute_optimizer_automation.types.filter_list
    import aws_sdk_compute_optimizer_automation.types.get_automation_event_request
    import aws_sdk_compute_optimizer_automation.types.get_automation_event_response
    import aws_sdk_compute_optimizer_automation.types.get_automation_rule_request
    import aws_sdk_compute_optimizer_automation.types.get_automation_rule_response
    import aws_sdk_compute_optimizer_automation.types.get_enrollment_configuration_request
    import aws_sdk_compute_optimizer_automation.types.get_enrollment_configuration_response
    import aws_sdk_compute_optimizer_automation.types.list_accounts_request
    import aws_sdk_compute_optimizer_automation.types.list_accounts_response
    import aws_sdk_compute_optimizer_automation.types.list_automation_event_steps_request
    import aws_sdk_compute_optimizer_automation.types.list_automation_event_steps_response
    import aws_sdk_compute_optimizer_automation.types.list_automation_event_summaries_request
    import aws_sdk_compute_optimizer_automation.types.list_automation_event_summaries_response
    import aws_sdk_compute_optimizer_automation.types.list_automation_events_request
    import aws_sdk_compute_optimizer_automation.types.list_automation_events_response
    import aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_request
    import aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_response
    import aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_summaries_request
    import aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_summaries_response
    import aws_sdk_compute_optimizer_automation.types.list_automation_rules_request
    import aws_sdk_compute_optimizer_automation.types.list_automation_rules_response
    import aws_sdk_compute_optimizer_automation.types.list_recommended_action_summaries_request
    import aws_sdk_compute_optimizer_automation.types.list_recommended_action_summaries_response
    import aws_sdk_compute_optimizer_automation.types.list_recommended_actions_request
    import aws_sdk_compute_optimizer_automation.types.list_recommended_actions_response
    import aws_sdk_compute_optimizer_automation.types.list_tags_for_resource_request
    import aws_sdk_compute_optimizer_automation.types.list_tags_for_resource_response
    import aws_sdk_compute_optimizer_automation.types.next_token
    import aws_sdk_compute_optimizer_automation.types.organization_configuration
    import aws_sdk_compute_optimizer_automation.types.organization_scope
    import aws_sdk_compute_optimizer_automation.types.preview_result
    import aws_sdk_compute_optimizer_automation.types.preview_result_summary
    import aws_sdk_compute_optimizer_automation.types.recommended_action
    import aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list
    import aws_sdk_compute_optimizer_automation.types.recommended_action_id
    import aws_sdk_compute_optimizer_automation.types.recommended_action_summary
    import aws_sdk_compute_optimizer_automation.types.recommended_action_type_list
    import aws_sdk_compute_optimizer_automation.types.rollback_automation_event_request
    import aws_sdk_compute_optimizer_automation.types.rollback_automation_event_response
    import aws_sdk_compute_optimizer_automation.types.rule_arn
    import aws_sdk_compute_optimizer_automation.types.rule_description
    import aws_sdk_compute_optimizer_automation.types.rule_name
    import aws_sdk_compute_optimizer_automation.types.rule_status
    import aws_sdk_compute_optimizer_automation.types.rule_type
    import aws_sdk_compute_optimizer_automation.types.schedule
    import aws_sdk_compute_optimizer_automation.types.start_automation_event_request
    import aws_sdk_compute_optimizer_automation.types.start_automation_event_response
    import aws_sdk_compute_optimizer_automation.types.tag_key_list
    import aws_sdk_compute_optimizer_automation.types.tag_list
    import aws_sdk_compute_optimizer_automation.types.tag_resource_request
    import aws_sdk_compute_optimizer_automation.types.tag_resource_response
    import aws_sdk_compute_optimizer_automation.types.untag_resource_request
    import aws_sdk_compute_optimizer_automation.types.untag_resource_response
    import aws_sdk_compute_optimizer_automation.types.update_automation_rule_request
    import aws_sdk_compute_optimizer_automation.types.update_automation_rule_response
    import aws_sdk_compute_optimizer_automation.types.update_enrollment_configuration_request
    import aws_sdk_compute_optimizer_automation.types.update_enrollment_configuration_response


class AsyncComputeOptimizerAutomationClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncComputeOptimizerAutomationClient:
    """A client for the ``ComputeOptimizerAutomation`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self.config = AsyncComputeOptimizerAutomationClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncComputeOptimizerAutomationClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_accounts(
        self,
        account_ids: "aws_sdk_compute_optimizer_automation.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.associate_accounts_response.AssociateAccountsResponse":
        """<p>Associates one or more member accounts with your organization's management account, enabling centralized implementation of optimization actions across those accounts. Once associated, the management account (or a delegated administrator) can apply recommended actions to the member account. When you associate a member account, its organization rule mode is automatically set to \"Any allowed,\" which permits the management account to create Automation rules that automatically apply actions to that account. If the member account has not previously enabled the Automation feature, the association process automatically enables it.</p> <note> <p>Only the management account or a delegated administrator can perform this action.</p> </note>

        Args:
            account_ids: <p> The IDs of the member accounts to associate. You can specify up to 50 account IDs. </p>
            client_token: <p> A unique identifier to ensure idempotency of the request. Valid for 24 hours after creation. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.associate_accounts_request.AssociateAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.associate_accounts_response.AssociateAccountsResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.associate_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.associate_accounts.async_associate_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.associate_accounts_request.AssociateAccountsRequest = {}  # type: ignore[typeddict-item]
        input["account_ids"] = account_ids
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_automation_rule(
        self,
        name: "aws_sdk_compute_optimizer_automation.types.rule_name.RuleName",
        rule_type: "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType",
        recommended_action_types: "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList",
        schedule: "aws_sdk_compute_optimizer_automation.types.schedule.Schedule",
        status: "aws_sdk_compute_optimizer_automation.types.rule_status.RuleStatus",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        description: Optional[
            "aws_sdk_compute_optimizer_automation.types.rule_description.RuleDescription"
        ] = None,
        organization_configuration: Optional[
            "aws_sdk_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
        ] = None,
        priority: Optional[str] = None,
        criteria: Optional[
            "aws_sdk_compute_optimizer_automation.types.criteria.Criteria"
        ] = None,
        tags: Optional[
            "aws_sdk_compute_optimizer_automation.types.tag_list.TagList"
        ] = None,
        client_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.create_automation_rule_response.CreateAutomationRuleResponse":
        """<p> Creates a new automation rule to apply recommended actions to resources based on specified criteria. </p>

        Args:
            name: <p> The name of the automation rule. </p>
            description: <p> A description of the automation rule. </p>
            rule_type: <p> The type of rule. </p> <note> <p>Only the management account or a delegated administrator can set the ruleType to be OrganizationRule.</p> </note>
            organization_configuration: <p> Configuration for organization-level rules. Required for OrganizationRule type. </p>
            priority: <p>A string representation of a decimal number between 0 and 1 (having up to 30 digits after the decimal point) that determines the priority of the rule. When multiple rules match the same recommended action, Compute Optimizer assigns the action to the rule with the lowest priority value (highest priority), even if that rule is scheduled to run later than other matching rules. </p>
            recommended_action_types: <p> The types of recommended actions this rule will automate. </p>
            criteria: <p>A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. </p>
            schedule: <p> The schedule for when the rule should run. </p>
            status: <p>The status of the rule </p>
            tags: <p> The tags to associate with the rule. </p>
            client_token: <p> A unique identifier to ensure idempotency of the request. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.create_automation_rule_request.CreateAutomationRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.create_automation_rule_response.CreateAutomationRuleResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.create_automation_rule

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.create_automation_rule.async_create_automation_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.create_automation_rule_request.CreateAutomationRuleRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["rule_type"] = rule_type
        if organization_configuration is not None:
            input["organization_configuration"] = organization_configuration
        if priority is not None:
            input["priority"] = priority
        input["recommended_action_types"] = recommended_action_types
        if criteria is not None:
            input["criteria"] = criteria
        input["schedule"] = schedule
        input["status"] = status
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_automation_rule(
        self,
        rule_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn",
        rule_revision: int,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.delete_automation_rule_response.DeleteAutomationRuleResponse":
        """<p> Deletes an existing automation rule. </p>

        Args:
            rule_arn: <p> The ARN of the rule to delete. </p>
            rule_revision: <p> The revision number of the rule to delete. </p>
            client_token: <p> A unique identifier to ensure idempotency of the request. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.delete_automation_rule_request.DeleteAutomationRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.delete_automation_rule_response.DeleteAutomationRuleResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.delete_automation_rule

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.delete_automation_rule.async_delete_automation_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.delete_automation_rule_request.DeleteAutomationRuleRequest = {}  # type: ignore[typeddict-item]
        input["rule_arn"] = rule_arn
        input["rule_revision"] = rule_revision
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_accounts(
        self,
        account_ids: "aws_sdk_compute_optimizer_automation.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.disassociate_accounts_response.DisassociateAccountsResponse":
        """<p> Disassociates member accounts from your organization's management account, removing centralized automation capabilities. Once disassociated, organization rules no longer apply to the member account, and the management account (or delegated administrator) cannot create Automation rules for that account. </p> <note> <p>Only the management account or a delegated administrator can perform this action.</p> </note>

        Args:
            account_ids: <p> The IDs of the member accounts to disassociate. </p>
            client_token: <p> A unique identifier to ensure idempotency of the request. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.disassociate_accounts_request.DisassociateAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.disassociate_accounts_response.DisassociateAccountsResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.disassociate_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.disassociate_accounts.async_disassociate_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.disassociate_accounts_request.DisassociateAccountsRequest = {}  # type: ignore[typeddict-item]
        input["account_ids"] = account_ids
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_automation_event(
        self,
        event_id: "aws_sdk_compute_optimizer_automation.types.event_id.EventId",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.get_automation_event_response.GetAutomationEventResponse":
        """<p> Retrieves details about a specific automation event. </p>

        Args:
            event_id: <p> The ID of the automation event to retrieve. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.get_automation_event_request.GetAutomationEventRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.get_automation_event_response.GetAutomationEventResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.get_automation_event

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.get_automation_event.async_get_automation_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.get_automation_event_request.GetAutomationEventRequest = {}  # type: ignore[typeddict-item]
        input["event_id"] = event_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_automation_rule(
        self,
        rule_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.get_automation_rule_response.GetAutomationRuleResponse":
        """<p> Retrieves details about a specific automation rule. </p>

        Args:
            rule_arn: <p> The ARN of the rule to retrieve. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.get_automation_rule_request.GetAutomationRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.get_automation_rule_response.GetAutomationRuleResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.get_automation_rule

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.get_automation_rule.async_get_automation_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.get_automation_rule_request.GetAutomationRuleRequest = {}  # type: ignore[typeddict-item]
        input["rule_arn"] = rule_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_enrollment_configuration(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.get_enrollment_configuration_response.GetEnrollmentConfigurationResponse":
        """<p> Retrieves the current enrollment configuration for Compute Optimizer Automation. </p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.get_enrollment_configuration_request.GetEnrollmentConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.get_enrollment_configuration_response.GetEnrollmentConfigurationResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.get_enrollment_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.get_enrollment_configuration.async_get_enrollment_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.get_enrollment_configuration_request.GetEnrollmentConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_accounts(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.list_accounts_response.ListAccountsResponse":
        """<p> Lists the accounts in your organization that are enrolled in Compute Optimizer and whether they have enabled Automation. </p> <note> <p>Only the management account or a delegated administrator can perform this action.</p> </note>

        Args:
            max_results: <p> The maximum number of results to return in a single call. </p>
            next_token: <p> The token for the next page of results. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.list_accounts_request.ListAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.list_accounts_response.ListAccountsResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_accounts.async_list_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.list_accounts_request.ListAccountsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_accounts(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_compute_optimizer_automation.types.account_info.AccountInfo]":
        _token = next_token
        while True:
            _response = await self.list_accounts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_automation_events(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        filters: Optional[
            "aws_sdk_compute_optimizer_automation.types.automation_event_filter_list.AutomationEventFilterList"
        ] = None,
        start_time_inclusive: Optional[datetime.datetime] = None,
        end_time_exclusive: Optional[datetime.datetime] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.list_automation_events_response.ListAutomationEventsResponse":
        """<p>Lists automation events based on specified filters. You can retrieve events that were created within the past year. </p>

        Args:
            filters: <p> The filters to apply to the list of automation events. </p>
            start_time_inclusive: <p> The start of the time range to query for events. </p>
            end_time_exclusive: <p> The end of the time range to query for events. </p>
            max_results: <p> The maximum number of results to return in a single call. </p>
            next_token: <p> The token for the next page of results. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.list_automation_events_request.ListAutomationEventsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.list_automation_events_response.ListAutomationEventsResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_events

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_events.async_list_automation_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.list_automation_events_request.ListAutomationEventsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if start_time_inclusive is not None:
            input["start_time_inclusive"] = start_time_inclusive
        if end_time_exclusive is not None:
            input["end_time_exclusive"] = end_time_exclusive
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

    async def iter_list_automation_events(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        filters: Optional[
            "aws_sdk_compute_optimizer_automation.types.automation_event_filter_list.AutomationEventFilterList"
        ] = None,
        start_time_inclusive: Optional[datetime.datetime] = None,
        end_time_exclusive: Optional[datetime.datetime] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_compute_optimizer_automation.types.automation_event.AutomationEvent]":
        _token = next_token
        while True:
            _response = await self.list_automation_events(
                config_overrides=config_overrides,
                filters=filters,
                start_time_inclusive=start_time_inclusive,
                end_time_exclusive=end_time_exclusive,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("automation_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_automation_event_steps(
        self,
        event_id: "aws_sdk_compute_optimizer_automation.types.event_id.EventId",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.list_automation_event_steps_response.ListAutomationEventStepsResponse":
        """<p>Lists the steps for a specific automation event. You can only list steps for events created within the past year. </p>

        Args:
            event_id: <p> The ID of the automation event. </p>
            max_results: <p>The maximum number of automation event steps to return in a single response. Valid range is 1-1000.</p>
            next_token: <p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.list_automation_event_steps_request.ListAutomationEventStepsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.list_automation_event_steps_response.ListAutomationEventStepsResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_event_steps

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_event_steps.async_list_automation_event_steps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.list_automation_event_steps_request.ListAutomationEventStepsRequest = {}  # type: ignore[typeddict-item]
        input["event_id"] = event_id
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

    async def iter_list_automation_event_steps(
        self,
        event_id: "aws_sdk_compute_optimizer_automation.types.event_id.EventId",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_compute_optimizer_automation.types.automation_event_step.AutomationEventStep]":
        _token = next_token
        while True:
            _response = await self.list_automation_event_steps(
                event_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("automation_event_steps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_automation_event_summaries(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        filters: Optional[
            "aws_sdk_compute_optimizer_automation.types.automation_event_filter_list.AutomationEventFilterList"
        ] = None,
        start_date_inclusive: Optional[str] = None,
        end_date_exclusive: Optional[str] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.list_automation_event_summaries_response.ListAutomationEventSummariesResponse":
        """<p>Provides a summary of automation events based on specified filters. Only events created within the past year will be included in the summary. </p>

        Args:
            filters: <p> The filters to apply to the list of automation event summaries. </p>
            start_date_inclusive: <p>The start date for filtering automation event summaries, inclusive. Events created on or after this date will be included.</p>
            end_date_exclusive: <p>The end date for filtering automation event summaries, exclusive. Events created before this date will be included.</p>
            max_results: <p>The maximum number of automation event summaries to return in a single response. Valid range is 1-1000.</p>
            next_token: <p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.list_automation_event_summaries_request.ListAutomationEventSummariesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.list_automation_event_summaries_response.ListAutomationEventSummariesResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_event_summaries

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_event_summaries.async_list_automation_event_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.list_automation_event_summaries_request.ListAutomationEventSummariesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if start_date_inclusive is not None:
            input["start_date_inclusive"] = start_date_inclusive
        if end_date_exclusive is not None:
            input["end_date_exclusive"] = end_date_exclusive
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

    async def iter_list_automation_event_summaries(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        filters: Optional[
            "aws_sdk_compute_optimizer_automation.types.automation_event_filter_list.AutomationEventFilterList"
        ] = None,
        start_date_inclusive: Optional[str] = None,
        end_date_exclusive: Optional[str] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_compute_optimizer_automation.types.automation_event_summary.AutomationEventSummary]":
        _token = next_token
        while True:
            _response = await self.list_automation_event_summaries(
                config_overrides=config_overrides,
                filters=filters,
                start_date_inclusive=start_date_inclusive,
                end_date_exclusive=end_date_exclusive,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("automation_event_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_automation_rule_preview(
        self,
        rule_type: "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType",
        recommended_action_types: "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        organization_scope: Optional[
            "aws_sdk_compute_optimizer_automation.types.organization_scope.OrganizationScope"
        ] = None,
        criteria: Optional[
            "aws_sdk_compute_optimizer_automation.types.criteria.Criteria"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_response.ListAutomationRulePreviewResponse":
        """<p>Returns a preview of the recommended actions that match your Automation rule's configuration and criteria. </p>

        Args:
            rule_type: <p> The type of rule. </p> <note> <p>Only the management account or a delegated administrator can set the ruleType to be OrganizationRule.</p> </note>
            organization_scope: <p> The organizational scope for the rule preview. </p>
            recommended_action_types: <p> The types of recommended actions to include in the preview. </p>
            criteria: <p>A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. </p>
            max_results: <p>The maximum number of automation rule preview results to return in a single response. Valid range is 1-1000.</p>
            next_token: <p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_request.ListAutomationRulePreviewRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_response.ListAutomationRulePreviewResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_rule_preview

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_rule_preview.async_list_automation_rule_preview(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_request.ListAutomationRulePreviewRequest = {}  # type: ignore[typeddict-item]
        input["rule_type"] = rule_type
        if organization_scope is not None:
            input["organization_scope"] = organization_scope
        input["recommended_action_types"] = recommended_action_types
        if criteria is not None:
            input["criteria"] = criteria
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

    async def iter_list_automation_rule_preview(
        self,
        rule_type: "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType",
        recommended_action_types: "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        organization_scope: Optional[
            "aws_sdk_compute_optimizer_automation.types.organization_scope.OrganizationScope"
        ] = None,
        criteria: Optional[
            "aws_sdk_compute_optimizer_automation.types.criteria.Criteria"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_compute_optimizer_automation.types.preview_result.PreviewResult]":
        _token = next_token
        while True:
            _response = await self.list_automation_rule_preview(
                rule_type,
                recommended_action_types,
                config_overrides=config_overrides,
                organization_scope=organization_scope,
                criteria=criteria,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("preview_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_automation_rule_preview_summaries(
        self,
        rule_type: "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType",
        recommended_action_types: "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        organization_scope: Optional[
            "aws_sdk_compute_optimizer_automation.types.organization_scope.OrganizationScope"
        ] = None,
        criteria: Optional[
            "aws_sdk_compute_optimizer_automation.types.criteria.Criteria"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_summaries_response.ListAutomationRulePreviewSummariesResponse":
        """<p>Returns a summary of the recommended actions that match your rule preview configuration and criteria. </p>

        Args:
            rule_type: <p>The type of rule.</p>
            organization_scope: <p>The organizational scope for the rule preview.</p>
            recommended_action_types: <p>The types of recommended actions to include in the preview.</p>
            max_results: <p>The maximum number of automation rule preview summaries to return in a single response. Valid range is 1-1000.</p>
            next_token: <p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_summaries_request.ListAutomationRulePreviewSummariesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_summaries_response.ListAutomationRulePreviewSummariesResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_rule_preview_summaries

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_rule_preview_summaries.async_list_automation_rule_preview_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.list_automation_rule_preview_summaries_request.ListAutomationRulePreviewSummariesRequest = {}  # type: ignore[typeddict-item]
        input["rule_type"] = rule_type
        if organization_scope is not None:
            input["organization_scope"] = organization_scope
        input["recommended_action_types"] = recommended_action_types
        if criteria is not None:
            input["criteria"] = criteria
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

    async def iter_list_automation_rule_preview_summaries(
        self,
        rule_type: "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType",
        recommended_action_types: "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        organization_scope: Optional[
            "aws_sdk_compute_optimizer_automation.types.organization_scope.OrganizationScope"
        ] = None,
        criteria: Optional[
            "aws_sdk_compute_optimizer_automation.types.criteria.Criteria"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_compute_optimizer_automation.types.preview_result_summary.PreviewResultSummary]":
        _token = next_token
        while True:
            _response = await self.list_automation_rule_preview_summaries(
                rule_type,
                recommended_action_types,
                config_overrides=config_overrides,
                organization_scope=organization_scope,
                criteria=criteria,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("preview_result_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_automation_rules(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        filters: Optional[
            "aws_sdk_compute_optimizer_automation.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.list_automation_rules_response.ListAutomationRulesResponse":
        """<p> Lists the automation rules that match specified filters. </p>

        Args:
            filters: <p> The filters to apply to the list of automation rules. </p>
            max_results: <p>The maximum number of automation rules to return in a single response. Valid range is 1-1000.</p>
            next_token: <p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.list_automation_rules_request.ListAutomationRulesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.list_automation_rules_response.ListAutomationRulesResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_rules

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_automation_rules.async_list_automation_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.list_automation_rules_request.ListAutomationRulesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
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

    async def iter_list_automation_rules(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        filters: Optional[
            "aws_sdk_compute_optimizer_automation.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_compute_optimizer_automation.types.automation_rule.AutomationRule]":
        _token = next_token
        while True:
            _response = await self.list_automation_rules(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("automation_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recommended_actions(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        filters: Optional[
            "aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list.RecommendedActionFilterList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.list_recommended_actions_response.ListRecommendedActionsResponse":
        """<p> Lists the recommended actions based that match specified filters. </p> <note> <p>Management accounts and delegated administrators can retrieve recommended actions that include associated member accounts. You can associate a member account using <code>AssociateAccounts</code>.</p> </note>

        Args:
            filters: <p> The filters to apply to the list of recommended actions. </p>
            max_results: <p>The maximum number of recommended actions to return in a single response. Valid range is 1-1000.</p>
            next_token: <p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.list_recommended_actions_request.ListRecommendedActionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.list_recommended_actions_response.ListRecommendedActionsResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_recommended_actions

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_recommended_actions.async_list_recommended_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.list_recommended_actions_request.ListRecommendedActionsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
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

    async def iter_list_recommended_actions(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        filters: Optional[
            "aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list.RecommendedActionFilterList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_compute_optimizer_automation.types.recommended_action.RecommendedAction]":
        _token = next_token
        while True:
            _response = await self.list_recommended_actions(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recommended_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recommended_action_summaries(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        filters: Optional[
            "aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list.RecommendedActionFilterList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.list_recommended_action_summaries_response.ListRecommendedActionSummariesResponse":
        """<p> Provides a summary of recommended actions based on specified filters. </p> <note> <p>Management accounts and delegated administrators can retrieve recommended actions that include associated member accounts. You can associate a member account using <code>AssociateAccounts</code>.</p> </note>

        Args:
            filters: <p>A list of filters to apply when retrieving recommended action summaries. Filters can be based on resource type, action type, account ID, and other criteria.</p>
            max_results: <p>The maximum number of recommended action summaries to return in a single response. Valid range is 1-1000.</p>
            next_token: <p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.list_recommended_action_summaries_request.ListRecommendedActionSummariesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.list_recommended_action_summaries_response.ListRecommendedActionSummariesResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_recommended_action_summaries

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_recommended_action_summaries.async_list_recommended_action_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.list_recommended_action_summaries_request.ListRecommendedActionSummariesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
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

    async def iter_list_recommended_action_summaries(
        self,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        filters: Optional[
            "aws_sdk_compute_optimizer_automation.types.recommended_action_filter_list.RecommendedActionFilterList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_compute_optimizer_automation.types.recommended_action_summary.RecommendedActionSummary]":
        _token = next_token
        while True:
            _response = await self.list_recommended_action_summaries(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recommended_action_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Lists the tags for a specified resource. </p>

        Args:
            resource_arn: <p> The ARN of the resource to list tags for. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def rollback_automation_event(
        self,
        event_id: "aws_sdk_compute_optimizer_automation.types.event_id.EventId",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.rollback_automation_event_response.RollbackAutomationEventResponse":
        """<p> Initiates a rollback for a completed automation event. </p> <note> <p>Management accounts and delegated administrators can only initiate a rollback for events belonging to associated member accounts. You can associate a member account using <code>AssociateAccounts</code>.</p> </note>

        Args:
            event_id: <p> The ID of the automation event to roll back. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.rollback_automation_event_request.RollbackAutomationEventRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.rollback_automation_event_response.RollbackAutomationEventResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.rollback_automation_event

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.rollback_automation_event.async_rollback_automation_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.rollback_automation_event_request.RollbackAutomationEventRequest = {}  # type: ignore[typeddict-item]
        input["event_id"] = event_id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_automation_event(
        self,
        recommended_action_id: "aws_sdk_compute_optimizer_automation.types.recommended_action_id.RecommendedActionId",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.start_automation_event_response.StartAutomationEventResponse":
        """<p> Initiates a one-time, on-demand automation for the specified recommended action. </p> <note> <p>Management accounts and delegated administrators can only initiate recommended actions for associated member accounts. You can associate a member account using <code>AssociateAccounts</code>.</p> </note>

        Args:
            recommended_action_id: <p> The ID of the recommended action to automate. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.start_automation_event_request.StartAutomationEventRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.start_automation_event_response.StartAutomationEventResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.start_automation_event

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.start_automation_event.async_start_automation_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.start_automation_event_request.StartAutomationEventRequest = {}  # type: ignore[typeddict-item]
        input["recommended_action_id"] = recommended_action_id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn",
        rule_revision: int,
        tags: "aws_sdk_compute_optimizer_automation.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.tag_resource_response.TagResourceResponse":
        """<p> Adds tags to the specified resource. </p>

        Args:
            resource_arn: <p> The ARN of the resource to tag. </p>
            rule_revision: <p>The revision number of the automation rule to tag. This ensures you're tagging the correct version of the rule.</p>
            tags: <p> The tags to add to the resource. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["rule_revision"] = rule_revision
        input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn",
        rule_revision: int,
        tag_keys: "aws_sdk_compute_optimizer_automation.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes tags from the specified resource. </p>

        Args:
            resource_arn: <p> The ARN of the resource to untag. </p>
            rule_revision: <p>The revision number of the automation rule to untag. This ensures you're untagging the correct version of the rule.</p>
            tag_keys: <p> The keys of the tags to remove from the resource. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["rule_revision"] = rule_revision
        input["tag_keys"] = tag_keys
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_automation_rule(
        self,
        rule_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn",
        rule_revision: int,
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        name: Optional[
            "aws_sdk_compute_optimizer_automation.types.rule_name.RuleName"
        ] = None,
        description: Optional[
            "aws_sdk_compute_optimizer_automation.types.rule_description.RuleDescription"
        ] = None,
        rule_type: Optional[
            "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType"
        ] = None,
        organization_configuration: Optional[
            "aws_sdk_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
        ] = None,
        priority: Optional[str] = None,
        recommended_action_types: Optional[
            "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
        ] = None,
        criteria: Optional[
            "aws_sdk_compute_optimizer_automation.types.criteria.Criteria"
        ] = None,
        schedule: Optional[
            "aws_sdk_compute_optimizer_automation.types.schedule.Schedule"
        ] = None,
        status: Optional[
            "aws_sdk_compute_optimizer_automation.types.rule_status.RuleStatus"
        ] = None,
        client_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.update_automation_rule_response.UpdateAutomationRuleResponse":
        """<p> Updates an existing automation rule. </p>

        Args:
            rule_arn: <p> The ARN of the rule to update. </p>
            rule_revision: <p> The revision number of the rule to update. </p>
            name: <p>The updated name of the automation rule. Must be 1-128 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>
            description: <p>The updated description of the automation rule. Can be up to 1024 characters long and contain alphanumeric characters, underscores, hyphens, spaces, and certain special characters.</p>
            rule_type: <p>The updated type of automation rule. Can be either OrganizationRule for organization-wide rules or AccountRule for account-specific rules.</p>
            organization_configuration: <p>Updated configuration settings for organization-wide rules, including rule application order and target account IDs.</p>
            priority: <p>The updated priority level of the automation rule, used to determine execution order when multiple rules apply to the same resource.</p>
            recommended_action_types: <p>Updated list of recommended action types that this rule can execute, such as SnapshotAndDeleteUnattachedEbsVolume or UpgradeEbsVolumeType.</p>
            schedule: <p>The updated schedule configuration for when the automation rule should execute, including cron expression, timezone, and execution window.</p>
            status: <p>The updated status of the automation rule. Can be Active or Inactive.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.update_automation_rule_request.UpdateAutomationRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.update_automation_rule_response.UpdateAutomationRuleResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.update_automation_rule

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.update_automation_rule.async_update_automation_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.update_automation_rule_request.UpdateAutomationRuleRequest = {}  # type: ignore[typeddict-item]
        input["rule_arn"] = rule_arn
        input["rule_revision"] = rule_revision
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if rule_type is not None:
            input["rule_type"] = rule_type
        if organization_configuration is not None:
            input["organization_configuration"] = organization_configuration
        if priority is not None:
            input["priority"] = priority
        if recommended_action_types is not None:
            input["recommended_action_types"] = recommended_action_types
        if criteria is not None:
            input["criteria"] = criteria
        if schedule is not None:
            input["schedule"] = schedule
        if status is not None:
            input["status"] = status
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_enrollment_configuration(
        self,
        status: "aws_sdk_compute_optimizer_automation.types.enrollment_status.EnrollmentStatus",
        *,
        config_overrides: Optional[AsyncComputeOptimizerAutomationClientConfig] = None,
        client_token: Optional[
            "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_compute_optimizer_automation.types.update_enrollment_configuration_response.UpdateEnrollmentConfigurationResponse":
        """<p>Updates your account’s Compute Optimizer Automation enrollment configuration. </p>

        Args:
            status: <p>The desired enrollment status. </p> <ul> <li> <p>Active - Enables the Automation feature for your account.</p> </li> <li> <p>Inactive - Disables the Automation feature for your account and stops all of your automation rules. If you opt in again later, all rules will be inactive, and you must enable the rules you want to run. You must wait at least 24 hours after opting out to opt in again.</p> </li> </ul> <note> <p>The <code>Pending</code> and <code>Failed</code> options cannot be used to update the enrollment status of an account. They are returned in the response of a request to update the enrollment status of an account.</p> <p>If you are a member account, your account must be disassociated from your organization’s management account before you can disable Automation. Contact your administrator to make this change.</p> </note>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_compute_optimizer_automation.types.update_enrollment_configuration_request.UpdateEnrollmentConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_compute_optimizer_automation.types.update_enrollment_configuration_response.UpdateEnrollmentConfigurationResponse"
        ]:
            import aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.update_enrollment_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_compute_optimizer_automation._operations.compute_optimizer_automation_service.update_enrollment_configuration.async_update_enrollment_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_compute_optimizer_automation.types.update_enrollment_configuration_request.UpdateEnrollmentConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["status"] = status
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
