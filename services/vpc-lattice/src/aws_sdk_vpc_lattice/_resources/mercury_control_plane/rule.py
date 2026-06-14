from typing import TYPE_CHECKING, Optional

import aws_sdk_vpc_lattice._auth._signers
import aws_sdk_vpc_lattice._auth._sigv4
from aws_sdk_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.create_rule_request
    import aws_sdk_vpc_lattice.types.create_rule_response
    import aws_sdk_vpc_lattice.types.delete_rule_request
    import aws_sdk_vpc_lattice.types.delete_rule_response
    import aws_sdk_vpc_lattice.types.get_rule_request
    import aws_sdk_vpc_lattice.types.get_rule_response
    import aws_sdk_vpc_lattice.types.list_rules_request
    import aws_sdk_vpc_lattice.types.list_rules_response
    import aws_sdk_vpc_lattice.types.listener_identifier
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.rule_action
    import aws_sdk_vpc_lattice.types.rule_identifier
    import aws_sdk_vpc_lattice.types.rule_match
    import aws_sdk_vpc_lattice.types.rule_name
    import aws_sdk_vpc_lattice.types.rule_priority
    import aws_sdk_vpc_lattice.types.rule_summary
    import aws_sdk_vpc_lattice.types.service_identifier
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.update_rule_request
    import aws_sdk_vpc_lattice.types.update_rule_response
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class Rule:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        name: "aws_sdk_vpc_lattice.types.rule_name.RuleName",
        match: "aws_sdk_vpc_lattice.types.rule_match.RuleMatch",
        priority: "aws_sdk_vpc_lattice.types.rule_priority.RulePriority",
        action: "aws_sdk_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_rule_response.CreateRuleResponse":
        """<p>Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            name: <p>The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            match: <p>The rule match.</p>
            priority: <p>The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.</p>
            action: <p>The action for the default rule.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the rule.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.create_rule_request.CreateRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.create_rule_response.CreateRuleResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_rule

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.create_rule.create_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_rule_request.CreateRuleRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["name"] = name
        input_["match"] = match
        input_["priority"] = priority
        input_["action"] = action
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "aws_sdk_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_rule_response.GetRuleResponse":
        """<p>Retrieves information about the specified listener rules. You can also retrieve information about the default listener rule. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the listener rule.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_rule_request.GetRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_rule_response.GetRuleResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_rule

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_rule.get_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_rule_request.GetRuleRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["rule_identifier"] = rule_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "aws_sdk_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        match: Optional["aws_sdk_vpc_lattice.types.rule_match.RuleMatch"] = None,
        priority: Optional[
            "aws_sdk_vpc_lattice.types.rule_priority.RulePriority"
        ] = None,
        action: Optional["aws_sdk_vpc_lattice.types.rule_action.RuleAction"] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_rule_response.UpdateRuleResponse":
        """<p>Updates a specified rule for the listener. You can't modify a default listener rule. To modify a default listener rule, use <code>UpdateListener</code>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the rule.</p>
            match: <p>The rule match.</p>
            priority: <p>The rule priority. A listener can't have multiple rules with the same priority.</p>
            action: <p>Information about the action for the specified listener rule.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.update_rule_request.UpdateRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.update_rule_response.UpdateRuleResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_rule

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.update_rule.update_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_rule_request.UpdateRuleRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["rule_identifier"] = rule_identifier
        if match is not None:
            input_["match"] = match
        if priority is not None:
            input_["priority"] = priority
        if action is not None:
            input_["action"] = action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "aws_sdk_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_rule_response.DeleteRuleResponse":
        """<p>Deletes a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. You can delete additional listener rules, but you cannot delete the default rule.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the rule.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_rule_request.DeleteRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_rule_response.DeleteRuleResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_rule

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_rule.delete_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_rule_request.DeleteRuleRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["rule_identifier"] = rule_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_rules_response.ListRulesResponse":
        """<p>Lists the rules for the specified listener.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_rules_request.ListRulesRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_rules_response.ListRulesResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_rules

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_rules.list_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_rules_request.ListRulesRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
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


class AsyncRule:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        name: "aws_sdk_vpc_lattice.types.rule_name.RuleName",
        match: "aws_sdk_vpc_lattice.types.rule_match.RuleMatch",
        priority: "aws_sdk_vpc_lattice.types.rule_priority.RulePriority",
        action: "aws_sdk_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_rule_response.CreateRuleResponse":
        """<p>Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            name: <p>The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            match: <p>The rule match.</p>
            priority: <p>The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.</p>
            action: <p>The action for the default rule.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the rule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.create_rule_request.CreateRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.create_rule_response.CreateRuleResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_rule

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.create_rule.async_create_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_rule_request.CreateRuleRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["name"] = name
        input_["match"] = match
        input_["priority"] = priority
        input_["action"] = action
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "aws_sdk_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_rule_response.GetRuleResponse":
        """<p>Retrieves information about the specified listener rules. You can also retrieve information about the default listener rule. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the listener rule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_rule_request.GetRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_rule_response.GetRuleResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_rule

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_rule.async_get_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_rule_request.GetRuleRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["rule_identifier"] = rule_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "aws_sdk_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        match: Optional["aws_sdk_vpc_lattice.types.rule_match.RuleMatch"] = None,
        priority: Optional[
            "aws_sdk_vpc_lattice.types.rule_priority.RulePriority"
        ] = None,
        action: Optional["aws_sdk_vpc_lattice.types.rule_action.RuleAction"] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_rule_response.UpdateRuleResponse":
        """<p>Updates a specified rule for the listener. You can't modify a default listener rule. To modify a default listener rule, use <code>UpdateListener</code>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the rule.</p>
            match: <p>The rule match.</p>
            priority: <p>The rule priority. A listener can't have multiple rules with the same priority.</p>
            action: <p>Information about the action for the specified listener rule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.update_rule_request.UpdateRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.update_rule_response.UpdateRuleResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_rule

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.update_rule.async_update_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_rule_request.UpdateRuleRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["rule_identifier"] = rule_identifier
        if match is not None:
            input_["match"] = match
        if priority is not None:
            input_["priority"] = priority
        if action is not None:
            input_["action"] = action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "aws_sdk_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_rule_response.DeleteRuleResponse":
        """<p>Deletes a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. You can delete additional listener rules, but you cannot delete the default rule.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the rule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_rule_request.DeleteRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_rule_response.DeleteRuleResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_rule

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_rule.async_delete_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_rule_request.DeleteRuleRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
        input_["rule_identifier"] = rule_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_rules_response.ListRulesResponse":
        """<p>Lists the rules for the specified listener.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_rules_request.ListRulesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_rules_response.ListRulesResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_rules

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_rules.async_list_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_rules_request.ListRulesRequest = {}  # type: ignore[typeddict-item]
        input_["service_identifier"] = service_identifier
        input_["listener_identifier"] = listener_identifier
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
