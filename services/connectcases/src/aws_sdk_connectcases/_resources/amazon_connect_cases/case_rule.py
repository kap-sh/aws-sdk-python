from typing import TYPE_CHECKING, Optional

import aws_sdk_connectcases._auth._signers
import aws_sdk_connectcases._auth._sigv4
from aws_sdk_connectcases._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.batch_get_case_rule_request
    import aws_sdk_connectcases.types.batch_get_case_rule_response
    import aws_sdk_connectcases.types.case_rule_description
    import aws_sdk_connectcases.types.case_rule_details
    import aws_sdk_connectcases.types.case_rule_id
    import aws_sdk_connectcases.types.case_rule_identifier_list
    import aws_sdk_connectcases.types.case_rule_name
    import aws_sdk_connectcases.types.case_rule_summary
    import aws_sdk_connectcases.types.create_case_rule_request
    import aws_sdk_connectcases.types.create_case_rule_response
    import aws_sdk_connectcases.types.delete_case_rule_request
    import aws_sdk_connectcases.types.delete_case_rule_response
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.list_case_rules_request
    import aws_sdk_connectcases.types.list_case_rules_response
    import aws_sdk_connectcases.types.max_results
    import aws_sdk_connectcases.types.next_token
    import aws_sdk_connectcases.types.update_case_rule_request
    import aws_sdk_connectcases.types.update_case_rule_response
    from aws_sdk_connectcases._services.async_connect_cases import (
        AsyncConnectCasesClient,
        AsyncConnectCasesClientConfig,
    )
    from aws_sdk_connectcases._services.connect_cases import (
        ConnectCasesClient,
        ConnectCasesClientConfig,
    )


class CaseRule:
    def __init__(self, service: ConnectCasesClient) -> None:
        self._service = service

    def create(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        name: "aws_sdk_connectcases.types.case_rule_name.CaseRuleName",
        rule: "aws_sdk_connectcases.types.case_rule_details.CaseRuleDetails",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        description: Optional[
            "aws_sdk_connectcases.types.case_rule_description.CaseRuleDescription"
        ] = None,
    ) -> "aws_sdk_connectcases.types.create_case_rule_response.CreateCaseRuleResponse":
        """<p>Creates a new case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            name: <p>Name of the case rule.</p>
            description: <p>The description of a case rule.</p>
            rule: <p>Represents what rule type should take place, under what conditions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.create_case_rule_request.CreateCaseRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.create_case_rule_response.CreateCaseRuleResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.create_case_rule

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.create_case_rule.create_case_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.create_case_rule_request.CreateCaseRuleRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["rule"] = rule

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        case_rule_id: "aws_sdk_connectcases.types.case_rule_id.CaseRuleId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        name: Optional["aws_sdk_connectcases.types.case_rule_name.CaseRuleName"] = None,
        description: Optional[
            "aws_sdk_connectcases.types.case_rule_description.CaseRuleDescription"
        ] = None,
        rule: Optional[
            "aws_sdk_connectcases.types.case_rule_details.CaseRuleDetails"
        ] = None,
    ) -> "aws_sdk_connectcases.types.update_case_rule_response.UpdateCaseRuleResponse":
        """<p>Updates a case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rule_id: <p>Unique identifier of a case rule.</p>
            name: <p>Name of the case rule.</p>
            description: <p>Description of a case rule.</p>
            rule: <p>Represents what rule type should take place, under what conditions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.update_case_rule_request.UpdateCaseRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.update_case_rule_response.UpdateCaseRuleResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.update_case_rule

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.update_case_rule.update_case_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.update_case_rule_request.UpdateCaseRuleRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["case_rule_id"] = case_rule_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if rule is not None:
            input_["rule"] = rule

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        case_rule_id: "aws_sdk_connectcases.types.case_rule_id.CaseRuleId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.delete_case_rule_response.DeleteCaseRuleResponse":
        """<p>Deletes a case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rule_id: <p>Unique identifier of a case rule.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.delete_case_rule_request.DeleteCaseRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.delete_case_rule_response.DeleteCaseRuleResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.delete_case_rule

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.delete_case_rule.delete_case_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.delete_case_rule_request.DeleteCaseRuleRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["case_rule_id"] = case_rule_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcases.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.list_case_rules_response.ListCaseRulesResponse":
        """<p>Lists all case rules in a Cases domain. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.list_case_rules_request.ListCaseRulesRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.list_case_rules_response.ListCaseRulesResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.list_case_rules

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.list_case_rules.list_case_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.list_case_rules_request.ListCaseRulesRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
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

    def batch_get_case_rule(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        case_rules: "aws_sdk_connectcases.types.case_rule_identifier_list.CaseRuleIdentifierList",
        *,
        config_overrides: Optional[ConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.batch_get_case_rule_response.BatchGetCaseRuleResponse":
        """<p>Gets a batch of case rules. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rules: <p>A list of case rule identifiers.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_connectcases.types.batch_get_case_rule_request.BatchGetCaseRuleRequest]",
        ) -> OperationResponse[
            "aws_sdk_connectcases.types.batch_get_case_rule_response.BatchGetCaseRuleResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.batch_get_case_rule

            output, http_response = (
                aws_sdk_connectcases._operations.amazon_connect_cases.batch_get_case_rule.batch_get_case_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.batch_get_case_rule_request.BatchGetCaseRuleRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["case_rules"] = case_rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCaseRule:
    def __init__(self, service: AsyncConnectCasesClient) -> None:
        self._service = service

    async def create(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        name: "aws_sdk_connectcases.types.case_rule_name.CaseRuleName",
        rule: "aws_sdk_connectcases.types.case_rule_details.CaseRuleDetails",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        description: Optional[
            "aws_sdk_connectcases.types.case_rule_description.CaseRuleDescription"
        ] = None,
    ) -> "aws_sdk_connectcases.types.create_case_rule_response.CreateCaseRuleResponse":
        """<p>Creates a new case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            name: <p>Name of the case rule.</p>
            description: <p>The description of a case rule.</p>
            rule: <p>Represents what rule type should take place, under what conditions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.create_case_rule_request.CreateCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.create_case_rule_response.CreateCaseRuleResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.create_case_rule

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.create_case_rule.async_create_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.create_case_rule_request.CreateCaseRuleRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["rule"] = rule

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        case_rule_id: "aws_sdk_connectcases.types.case_rule_id.CaseRuleId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        name: Optional["aws_sdk_connectcases.types.case_rule_name.CaseRuleName"] = None,
        description: Optional[
            "aws_sdk_connectcases.types.case_rule_description.CaseRuleDescription"
        ] = None,
        rule: Optional[
            "aws_sdk_connectcases.types.case_rule_details.CaseRuleDetails"
        ] = None,
    ) -> "aws_sdk_connectcases.types.update_case_rule_response.UpdateCaseRuleResponse":
        """<p>Updates a case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rule_id: <p>Unique identifier of a case rule.</p>
            name: <p>Name of the case rule.</p>
            description: <p>Description of a case rule.</p>
            rule: <p>Represents what rule type should take place, under what conditions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.update_case_rule_request.UpdateCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.update_case_rule_response.UpdateCaseRuleResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.update_case_rule

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.update_case_rule.async_update_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.update_case_rule_request.UpdateCaseRuleRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["case_rule_id"] = case_rule_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if rule is not None:
            input_["rule"] = rule

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        case_rule_id: "aws_sdk_connectcases.types.case_rule_id.CaseRuleId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.delete_case_rule_response.DeleteCaseRuleResponse":
        """<p>Deletes a case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rule_id: <p>Unique identifier of a case rule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.delete_case_rule_request.DeleteCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.delete_case_rule_response.DeleteCaseRuleResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.delete_case_rule

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.delete_case_rule.async_delete_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.delete_case_rule_request.DeleteCaseRuleRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["case_rule_id"] = case_rule_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[
            "aws_sdk_connectcases.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_connectcases.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_connectcases.types.list_case_rules_response.ListCaseRulesResponse":
        """<p>Lists all case rules in a Cases domain. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.list_case_rules_request.ListCaseRulesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.list_case_rules_response.ListCaseRulesResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.list_case_rules

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.list_case_rules.async_list_case_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.list_case_rules_request.ListCaseRulesRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
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

    async def batch_get_case_rule(
        self,
        domain_id: "aws_sdk_connectcases.types.domain_id.DomainId",
        case_rules: "aws_sdk_connectcases.types.case_rule_identifier_list.CaseRuleIdentifierList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "aws_sdk_connectcases.types.batch_get_case_rule_response.BatchGetCaseRuleResponse":
        """<p>Gets a batch of case rules. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html\">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rules: <p>A list of case rule identifiers.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connectcases.types.batch_get_case_rule_request.BatchGetCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connectcases.types.batch_get_case_rule_response.BatchGetCaseRuleResponse"
        ]:
            import aws_sdk_connectcases._operations.amazon_connect_cases.batch_get_case_rule

            (
                output,
                http_response,
            ) = await aws_sdk_connectcases._operations.amazon_connect_cases.batch_get_case_rule.async_batch_get_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_connectcases.types.batch_get_case_rule_request.BatchGetCaseRuleRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["case_rules"] = case_rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
