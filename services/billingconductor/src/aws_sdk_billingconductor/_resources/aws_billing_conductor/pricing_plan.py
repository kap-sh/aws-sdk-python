from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_billingconductor._auth._signers
import aws_sdk_billingconductor._auth._sigv4
from aws_sdk_billingconductor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.associate_pricing_rules_input
    import aws_sdk_billingconductor.types.associate_pricing_rules_output
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.client_token
    import aws_sdk_billingconductor.types.create_pricing_plan_input
    import aws_sdk_billingconductor.types.create_pricing_plan_output
    import aws_sdk_billingconductor.types.delete_pricing_plan_input
    import aws_sdk_billingconductor.types.delete_pricing_plan_output
    import aws_sdk_billingconductor.types.disassociate_pricing_rules_input
    import aws_sdk_billingconductor.types.disassociate_pricing_rules_output
    import aws_sdk_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input
    import aws_sdk_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output
    import aws_sdk_billingconductor.types.list_pricing_plans_filter
    import aws_sdk_billingconductor.types.list_pricing_plans_input
    import aws_sdk_billingconductor.types.list_pricing_plans_output
    import aws_sdk_billingconductor.types.max_pricing_plan_results
    import aws_sdk_billingconductor.types.max_pricing_rule_results
    import aws_sdk_billingconductor.types.pricing_plan_arn
    import aws_sdk_billingconductor.types.pricing_plan_description
    import aws_sdk_billingconductor.types.pricing_plan_list_element
    import aws_sdk_billingconductor.types.pricing_plan_name
    import aws_sdk_billingconductor.types.pricing_rule_arn
    import aws_sdk_billingconductor.types.pricing_rule_arns_input
    import aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input
    import aws_sdk_billingconductor.types.tag_map
    import aws_sdk_billingconductor.types.token
    import aws_sdk_billingconductor.types.update_pricing_plan_input
    import aws_sdk_billingconductor.types.update_pricing_plan_output
    from aws_sdk_billingconductor._services.async_billingconductor import (
        AsyncbillingconductorClient,
        AsyncbillingconductorClientConfig,
    )
    from aws_sdk_billingconductor._services.billingconductor import (
        billingconductorClient,
        billingconductorClientConfig,
    )


class PricingPlan:
    def __init__(self, service: billingconductorClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_billingconductor.types.pricing_plan_name.PricingPlanName",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        client_token: Optional[
            "aws_sdk_billingconductor.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_billingconductor.types.pricing_plan_description.PricingPlanDescription"
        ] = None,
        pricing_rule_arns: Optional[
            "aws_sdk_billingconductor.types.pricing_rule_arns_input.PricingRuleArnsInput"
        ] = None,
        tags: Optional["aws_sdk_billingconductor.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_billingconductor.types.create_pricing_plan_output.CreatePricingPlanOutput":
        """<p>Creates a pricing plan that is used for computing Amazon Web Services charges for billing groups. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p>The name of the pricing plan. The names must be unique to each pricing plan. </p>
            description: <p>The description of the pricing plan. </p>
            pricing_rule_arns: <p> A list of Amazon Resource Names (ARNs) that define the pricing plan parameters. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a pricing plan. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.create_pricing_plan_output.CreatePricingPlanOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.create_pricing_plan

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.create_pricing_plan.create_pricing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if pricing_rule_arns is not None:
            input_["pricing_rule_arns"] = pricing_rule_arns
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        name: Optional[
            "aws_sdk_billingconductor.types.pricing_plan_name.PricingPlanName"
        ] = None,
        description: Optional[
            "aws_sdk_billingconductor.types.pricing_plan_description.PricingPlanDescription"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput":
        """<p>This updates an existing pricing plan. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pricing plan that you're updating. </p>
            name: <p>The name of the pricing plan. The name must be unique to each pricing plan. </p>
            description: <p>The description of the pricing plan. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.update_pricing_plan

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.update_pricing_plan.update_pricing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.delete_pricing_plan_output.DeletePricingPlanOutput":
        """<p>Deletes a pricing plan. The pricing plan must not be associated with any billing groups to delete successfully.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pricing plan that you're deleting. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.delete_pricing_plan_input.DeletePricingPlanInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.delete_pricing_plan_output.DeletePricingPlanOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.delete_pricing_plan

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.delete_pricing_plan.delete_pricing_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.delete_pricing_plan_input.DeletePricingPlanInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_pricing_plans_filter.ListPricingPlansFilter"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
    ) -> "aws_sdk_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput":
        """<p>A paginated call to get pricing plans for the given billing period. If you don't provide a billing period, the current billing period is used. </p>

        Args:
            billing_period: <p>The preferred billing period to get pricing plan. </p>
            filters: <p>A <code>ListPricingPlansFilter</code> that specifies the Amazon Resource Name (ARNs) of pricing plans to retrieve pricing plans information.</p>
            max_results: <p>The maximum number of pricing plans to retrieve.</p>
            next_token: <p>The pagination token that's used on subsequent call to get pricing plans. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.list_pricing_plans_input.ListPricingPlansInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_pricing_plans

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.list_pricing_plans.list_pricing_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_pricing_plans_input.ListPricingPlansInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if filters is not None:
            input_["filters"] = filters
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

    def associate_pricing_rules(
        self,
        arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        pricing_rule_arns: "aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.associate_pricing_rules_output.AssociatePricingRulesOutput":
        """<p>Connects an array of <code>PricingRuleArns</code> to a defined <code>PricingPlan</code>. The maximum number <code>PricingRuleArn</code> that can be associated in one call is 30. </p>

        Args:
            arn: <p> The <code>PricingPlanArn</code> that the <code>PricingRuleArns</code> are associated with. </p>
            pricing_rule_arns: <p> The <code>PricingRuleArns</code> that are associated with the Pricing Plan. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.associate_pricing_rules_input.AssociatePricingRulesInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.associate_pricing_rules_output.AssociatePricingRulesOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.associate_pricing_rules

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.associate_pricing_rules.associate_pricing_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.associate_pricing_rules_input.AssociatePricingRulesInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["pricing_rule_arns"] = pricing_rule_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_pricing_rules(
        self,
        arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        pricing_rule_arns: "aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.disassociate_pricing_rules_output.DisassociatePricingRulesOutput":
        """<p> Disassociates a list of pricing rules from a pricing plan. </p>

        Args:
            arn: <p> The pricing plan Amazon Resource Name (ARN) to disassociate pricing rules from. </p>
            pricing_rule_arns: <p> A list containing the Amazon Resource Name (ARN) of the pricing rules that will be disassociated. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.disassociate_pricing_rules_input.DisassociatePricingRulesInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.disassociate_pricing_rules_output.DisassociatePricingRulesOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.disassociate_pricing_rules

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.disassociate_pricing_rules.disassociate_pricing_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.disassociate_pricing_rules_input.DisassociatePricingRulesInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["pricing_rule_arns"] = pricing_rule_arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_pricing_plans_associated_with_pricing_rule(
        self,
        pricing_rule_arn: "aws_sdk_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
    ) -> "aws_sdk_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output.ListPricingPlansAssociatedWithPricingRuleOutput":
        """<p> A list of the pricing plans that are associated with a pricing rule. </p>

        Args:
            billing_period: <p> The pricing plan billing period for which associations will be listed. </p>
            pricing_rule_arn: <p> The pricing rule Amazon Resource Name (ARN) for which associations will be listed. </p>
            max_results: <p> The optional maximum number of pricing rule associations to retrieve. </p>
            next_token: <p> The optional pagination token returned by a previous call. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input.ListPricingPlansAssociatedWithPricingRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output.ListPricingPlansAssociatedWithPricingRuleOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_pricing_plans_associated_with_pricing_rule

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.list_pricing_plans_associated_with_pricing_rule.list_pricing_plans_associated_with_pricing_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input.ListPricingPlansAssociatedWithPricingRuleInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input_["billing_period"] = billing_period
        input_["pricing_rule_arn"] = pricing_rule_arn
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


class AsyncPricingPlan:
    def __init__(self, service: AsyncbillingconductorClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_billingconductor.types.pricing_plan_name.PricingPlanName",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "aws_sdk_billingconductor.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "aws_sdk_billingconductor.types.pricing_plan_description.PricingPlanDescription"
        ] = None,
        pricing_rule_arns: Optional[
            "aws_sdk_billingconductor.types.pricing_rule_arns_input.PricingRuleArnsInput"
        ] = None,
        tags: Optional["aws_sdk_billingconductor.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_billingconductor.types.create_pricing_plan_output.CreatePricingPlanOutput":
        """<p>Creates a pricing plan that is used for computing Amazon Web Services charges for billing groups. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p>The name of the pricing plan. The names must be unique to each pricing plan. </p>
            description: <p>The description of the pricing plan. </p>
            pricing_rule_arns: <p> A list of Amazon Resource Names (ARNs) that define the pricing plan parameters. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a pricing plan. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.create_pricing_plan_output.CreatePricingPlanOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.create_pricing_plan

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.create_pricing_plan.async_create_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if pricing_rule_arns is not None:
            input_["pricing_rule_arns"] = pricing_rule_arns
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        name: Optional[
            "aws_sdk_billingconductor.types.pricing_plan_name.PricingPlanName"
        ] = None,
        description: Optional[
            "aws_sdk_billingconductor.types.pricing_plan_description.PricingPlanDescription"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput":
        """<p>This updates an existing pricing plan. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pricing plan that you're updating. </p>
            name: <p>The name of the pricing plan. The name must be unique to each pricing plan. </p>
            description: <p>The description of the pricing plan. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.update_pricing_plan

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.update_pricing_plan.async_update_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.delete_pricing_plan_output.DeletePricingPlanOutput":
        """<p>Deletes a pricing plan. The pricing plan must not be associated with any billing groups to delete successfully.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pricing plan that you're deleting. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.delete_pricing_plan_input.DeletePricingPlanInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.delete_pricing_plan_output.DeletePricingPlanOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.delete_pricing_plan

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.delete_pricing_plan.async_delete_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.delete_pricing_plan_input.DeletePricingPlanInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_pricing_plans_filter.ListPricingPlansFilter"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
    ) -> "aws_sdk_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput":
        """<p>A paginated call to get pricing plans for the given billing period. If you don't provide a billing period, the current billing period is used. </p>

        Args:
            billing_period: <p>The preferred billing period to get pricing plan. </p>
            filters: <p>A <code>ListPricingPlansFilter</code> that specifies the Amazon Resource Name (ARNs) of pricing plans to retrieve pricing plans information.</p>
            max_results: <p>The maximum number of pricing plans to retrieve.</p>
            next_token: <p>The pagination token that's used on subsequent call to get pricing plans. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.list_pricing_plans_input.ListPricingPlansInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_pricing_plans

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.list_pricing_plans.async_list_pricing_plans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_pricing_plans_input.ListPricingPlansInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if filters is not None:
            input_["filters"] = filters
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

    async def associate_pricing_rules(
        self,
        arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        pricing_rule_arns: "aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.associate_pricing_rules_output.AssociatePricingRulesOutput":
        """<p>Connects an array of <code>PricingRuleArns</code> to a defined <code>PricingPlan</code>. The maximum number <code>PricingRuleArn</code> that can be associated in one call is 30. </p>

        Args:
            arn: <p> The <code>PricingPlanArn</code> that the <code>PricingRuleArns</code> are associated with. </p>
            pricing_rule_arns: <p> The <code>PricingRuleArns</code> that are associated with the Pricing Plan. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.associate_pricing_rules_input.AssociatePricingRulesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.associate_pricing_rules_output.AssociatePricingRulesOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.associate_pricing_rules

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.associate_pricing_rules.async_associate_pricing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.associate_pricing_rules_input.AssociatePricingRulesInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["pricing_rule_arns"] = pricing_rule_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_pricing_rules(
        self,
        arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        pricing_rule_arns: "aws_sdk_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.disassociate_pricing_rules_output.DisassociatePricingRulesOutput":
        """<p> Disassociates a list of pricing rules from a pricing plan. </p>

        Args:
            arn: <p> The pricing plan Amazon Resource Name (ARN) to disassociate pricing rules from. </p>
            pricing_rule_arns: <p> A list containing the Amazon Resource Name (ARN) of the pricing rules that will be disassociated. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.disassociate_pricing_rules_input.DisassociatePricingRulesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.disassociate_pricing_rules_output.DisassociatePricingRulesOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.disassociate_pricing_rules

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.disassociate_pricing_rules.async_disassociate_pricing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.disassociate_pricing_rules_input.DisassociatePricingRulesInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["pricing_rule_arns"] = pricing_rule_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_pricing_plans_associated_with_pricing_rule(
        self,
        pricing_rule_arn: "aws_sdk_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
    ) -> "aws_sdk_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output.ListPricingPlansAssociatedWithPricingRuleOutput":
        """<p> A list of the pricing plans that are associated with a pricing rule. </p>

        Args:
            billing_period: <p> The pricing plan billing period for which associations will be listed. </p>
            pricing_rule_arn: <p> The pricing rule Amazon Resource Name (ARN) for which associations will be listed. </p>
            max_results: <p> The optional maximum number of pricing rule associations to retrieve. </p>
            next_token: <p> The optional pagination token returned by a previous call. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input.ListPricingPlansAssociatedWithPricingRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output.ListPricingPlansAssociatedWithPricingRuleOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_pricing_plans_associated_with_pricing_rule

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.list_pricing_plans_associated_with_pricing_rule.async_list_pricing_plans_associated_with_pricing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input.ListPricingPlansAssociatedWithPricingRuleInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input_["billing_period"] = billing_period
        input_["pricing_rule_arn"] = pricing_rule_arn
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
