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
    import aws_sdk_billingconductor.types.account_id
    import aws_sdk_billingconductor.types.batch_associate_resources_to_custom_line_item_input
    import aws_sdk_billingconductor.types.batch_associate_resources_to_custom_line_item_output
    import aws_sdk_billingconductor.types.batch_disassociate_resources_from_custom_line_item_input
    import aws_sdk_billingconductor.types.batch_disassociate_resources_from_custom_line_item_output
    import aws_sdk_billingconductor.types.billing_group_arn
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.client_token
    import aws_sdk_billingconductor.types.computation_rule_enum
    import aws_sdk_billingconductor.types.create_custom_line_item_input
    import aws_sdk_billingconductor.types.create_custom_line_item_output
    import aws_sdk_billingconductor.types.custom_line_item_arn
    import aws_sdk_billingconductor.types.custom_line_item_batch_associations_list
    import aws_sdk_billingconductor.types.custom_line_item_batch_disassociations_list
    import aws_sdk_billingconductor.types.custom_line_item_billing_period_range
    import aws_sdk_billingconductor.types.custom_line_item_charge_details
    import aws_sdk_billingconductor.types.custom_line_item_description
    import aws_sdk_billingconductor.types.custom_line_item_list_element
    import aws_sdk_billingconductor.types.custom_line_item_name
    import aws_sdk_billingconductor.types.custom_line_item_version_list_element
    import aws_sdk_billingconductor.types.delete_custom_line_item_input
    import aws_sdk_billingconductor.types.delete_custom_line_item_output
    import aws_sdk_billingconductor.types.list_custom_line_item_versions_filter
    import aws_sdk_billingconductor.types.list_custom_line_item_versions_input
    import aws_sdk_billingconductor.types.list_custom_line_item_versions_output
    import aws_sdk_billingconductor.types.list_custom_line_items_filter
    import aws_sdk_billingconductor.types.list_custom_line_items_input
    import aws_sdk_billingconductor.types.list_custom_line_items_output
    import aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_filter
    import aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_input
    import aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_output
    import aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_response_element
    import aws_sdk_billingconductor.types.max_custom_line_item_results
    import aws_sdk_billingconductor.types.presentation_object
    import aws_sdk_billingconductor.types.tag_map
    import aws_sdk_billingconductor.types.token
    import aws_sdk_billingconductor.types.update_custom_line_item_charge_details
    import aws_sdk_billingconductor.types.update_custom_line_item_input
    import aws_sdk_billingconductor.types.update_custom_line_item_output
    from aws_sdk_billingconductor._services.async_billingconductor import (
        AsyncbillingconductorClient,
        AsyncbillingconductorClientConfig,
    )
    from aws_sdk_billingconductor._services.billingconductor import (
        billingconductorClient,
        billingconductorClientConfig,
    )


class CustomLineItem:
    def __init__(self, service: billingconductorClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_billingconductor.types.custom_line_item_name.CustomLineItemName",
        description: "aws_sdk_billingconductor.types.custom_line_item_description.CustomLineItemDescription",
        billing_group_arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        charge_details: "aws_sdk_billingconductor.types.custom_line_item_charge_details.CustomLineItemChargeDetails",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        client_token: Optional[
            "aws_sdk_billingconductor.types.client_token.ClientToken"
        ] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
        tags: Optional["aws_sdk_billingconductor.types.tag_map.TagMap"] = None,
        account_id: Optional[
            "aws_sdk_billingconductor.types.account_id.AccountId"
        ] = None,
        computation_rule: Optional[
            "aws_sdk_billingconductor.types.computation_rule_enum.ComputationRuleEnum"
        ] = None,
        presentation_details: Optional[
            "aws_sdk_billingconductor.types.presentation_object.PresentationObject"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.create_custom_line_item_output.CreateCustomLineItemOutput":
        """<p>Creates a custom line item that can be used to create a one-time fixed charge that can be applied to a single billing group for the current or previous billing period. The one-time fixed charge is either a fee or discount. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The name of the custom line item. </p>
            description: <p> The description of the custom line item. This is shown on the Bills page in association with the charge value. </p>
            billing_group_arn: <p> The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to. </p>
            billing_period_range: <p> A time range for which the custom line item is effective. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a custom line item. </p>
            charge_details: <p> A <code>CustomLineItemChargeDetails</code> that describes the charge details for a custom line item. </p>
            account_id: <p>The Amazon Web Services account in which this custom line item will be applied to.</p>
            computation_rule: <p> Specifies how the custom line item charges are computed. </p>
            presentation_details: <p> Details controlling how the custom line item charges are presented in the bill. Contains specifications for which service the charges will be shown under. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.create_custom_line_item_input.CreateCustomLineItemInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.create_custom_line_item_output.CreateCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.create_custom_line_item

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.create_custom_line_item.create_custom_line_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.create_custom_line_item_input.CreateCustomLineItemInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        input_["description"] = description
        input_["billing_group_arn"] = billing_group_arn
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range
        if tags is not None:
            input_["tags"] = tags
        input_["charge_details"] = charge_details
        if account_id is not None:
            input_["account_id"] = account_id
        if computation_rule is not None:
            input_["computation_rule"] = computation_rule
        if presentation_details is not None:
            input_["presentation_details"] = presentation_details

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        name: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_name.CustomLineItemName"
        ] = None,
        description: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
        ] = None,
        charge_details: Optional[
            "aws_sdk_billingconductor.types.update_custom_line_item_charge_details.UpdateCustomLineItemChargeDetails"
        ] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.update_custom_line_item_output.UpdateCustomLineItemOutput":
        """<p> Update an existing custom line item in the current or previous billing period. </p>

        Args:
            arn: <p> The ARN of the custom line item to be updated. </p>
            name: <p> The new name for the custom line item. </p>
            description: <p> The new line item description of the custom line item. </p>
            charge_details: <p> A <code>ListCustomLineItemChargeDetails</code> containing the new charge details for the custom line item. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.update_custom_line_item_input.UpdateCustomLineItemInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.update_custom_line_item_output.UpdateCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.update_custom_line_item

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.update_custom_line_item.update_custom_line_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.update_custom_line_item_input.UpdateCustomLineItemInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if charge_details is not None:
            input_["charge_details"] = charge_details
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.delete_custom_line_item_output.DeleteCustomLineItemOutput":
        """<p> Deletes the custom line item identified by the given ARN in the current, or previous billing period. </p>

        Args:
            arn: <p> The ARN of the custom line item to be deleted. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.delete_custom_line_item_input.DeleteCustomLineItemInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.delete_custom_line_item_output.DeleteCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.delete_custom_line_item

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.delete_custom_line_item.delete_custom_line_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.delete_custom_line_item_input.DeleteCustomLineItemInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

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
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_custom_line_items_filter.ListCustomLineItemsFilter"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.list_custom_line_items_output.ListCustomLineItemsOutput":
        """<p> A paginated call to get a list of all custom line items (FFLIs) for the given billing period. If you don't provide a billing period, the current billing period is used. </p>

        Args:
            billing_period: <p> The preferred billing period to get custom line items (FFLIs). </p>
            max_results: <p> The maximum number of billing groups to retrieve. </p>
            next_token: <p> The pagination token that's used on subsequent calls to get custom line items (FFLIs). </p>
            filters: <p>A <code>ListCustomLineItemsFilter</code> that specifies the custom line item names and/or billing group Amazon Resource Names (ARNs) to retrieve FFLI information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.list_custom_line_items_input.ListCustomLineItemsInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.list_custom_line_items_output.ListCustomLineItemsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_custom_line_items

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.list_custom_line_items.list_custom_line_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_custom_line_items_input.ListCustomLineItemsInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_associate_resources_to_custom_line_item(
        self,
        target_arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        resource_arns: "aws_sdk_billingconductor.types.custom_line_item_batch_associations_list.CustomLineItemBatchAssociationsList",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.batch_associate_resources_to_custom_line_item_output.BatchAssociateResourcesToCustomLineItemOutput":
        """<p> Associates a batch of resources to a percentage custom line item. </p>

        Args:
            target_arn: <p> A percentage custom line item ARN to associate the resources to. </p>
            resource_arns: <p> A list containing the ARNs of the resources to be associated. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.batch_associate_resources_to_custom_line_item_input.BatchAssociateResourcesToCustomLineItemInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.batch_associate_resources_to_custom_line_item_output.BatchAssociateResourcesToCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.batch_associate_resources_to_custom_line_item

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.batch_associate_resources_to_custom_line_item.batch_associate_resources_to_custom_line_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.batch_associate_resources_to_custom_line_item_input.BatchAssociateResourcesToCustomLineItemInput = {}  # type: ignore[typeddict-item]
        input_["target_arn"] = target_arn
        input_["resource_arns"] = resource_arns
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_disassociate_resources_from_custom_line_item(
        self,
        target_arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        resource_arns: "aws_sdk_billingconductor.types.custom_line_item_batch_disassociations_list.CustomLineItemBatchDisassociationsList",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.batch_disassociate_resources_from_custom_line_item_output.BatchDisassociateResourcesFromCustomLineItemOutput":
        """<p> Disassociates a batch of resources from a percentage custom line item. </p>

        Args:
            target_arn: <p> A percentage custom line item ARN to disassociate the resources from. </p>
            resource_arns: <p> A list containing the ARNs of resources to be disassociated. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.batch_disassociate_resources_from_custom_line_item_input.BatchDisassociateResourcesFromCustomLineItemInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.batch_disassociate_resources_from_custom_line_item_output.BatchDisassociateResourcesFromCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.batch_disassociate_resources_from_custom_line_item

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.batch_disassociate_resources_from_custom_line_item.batch_disassociate_resources_from_custom_line_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.batch_disassociate_resources_from_custom_line_item_input.BatchDisassociateResourcesFromCustomLineItemInput = {}  # type: ignore[typeddict-item]
        input_["target_arn"] = target_arn
        input_["resource_arns"] = resource_arns
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_custom_line_item_versions(
        self,
        arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_custom_line_item_versions_filter.ListCustomLineItemVersionsFilter"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.list_custom_line_item_versions_output.ListCustomLineItemVersionsOutput":
        """<p>A paginated call to get a list of all custom line item versions.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for the custom line item.</p>
            max_results: <p>The maximum number of custom line item versions to retrieve.</p>
            next_token: <p>The pagination token that's used on subsequent calls to retrieve custom line item versions.</p>
            filters: <p>A <code>ListCustomLineItemVersionsFilter</code> that specifies the billing period range in which the custom line item versions are applied.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.list_custom_line_item_versions_input.ListCustomLineItemVersionsInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.list_custom_line_item_versions_output.ListCustomLineItemVersionsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_custom_line_item_versions

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.list_custom_line_item_versions.list_custom_line_item_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_custom_line_item_versions_input.ListCustomLineItemVersionsInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_resources_associated_to_custom_line_item(
        self,
        arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[billingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_filter.ListResourcesAssociatedToCustomLineItemFilter"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_output.ListResourcesAssociatedToCustomLineItemOutput":
        """<p> List the resources that are associated to a custom line item. </p>

        Args:
            billing_period: <p> The billing period for which the resource associations will be listed. </p>
            arn: <p> The ARN of the custom line item for which the resource associations will be listed. </p>
            max_results: <p> (Optional) The maximum number of resource associations to be retrieved. </p>
            next_token: <p> (Optional) The pagination token that's returned by a previous request. </p>
            filters: <p> (Optional) A <code>ListResourcesAssociatedToCustomLineItemFilter</code> that can specify the types of resources that should be retrieved. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_input.ListResourcesAssociatedToCustomLineItemInput]",
        ) -> OperationResponse[
            "aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_output.ListResourcesAssociatedToCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_resources_associated_to_custom_line_item

            output, http_response = (
                aws_sdk_billingconductor._operations.aws_billing_conductor.list_resources_associated_to_custom_line_item.list_resources_associated_to_custom_line_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_input.ListResourcesAssociatedToCustomLineItemInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input_["billing_period"] = billing_period
        input_["arn"] = arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCustomLineItem:
    def __init__(self, service: AsyncbillingconductorClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_billingconductor.types.custom_line_item_name.CustomLineItemName",
        description: "aws_sdk_billingconductor.types.custom_line_item_description.CustomLineItemDescription",
        billing_group_arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        charge_details: "aws_sdk_billingconductor.types.custom_line_item_charge_details.CustomLineItemChargeDetails",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "aws_sdk_billingconductor.types.client_token.ClientToken"
        ] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
        tags: Optional["aws_sdk_billingconductor.types.tag_map.TagMap"] = None,
        account_id: Optional[
            "aws_sdk_billingconductor.types.account_id.AccountId"
        ] = None,
        computation_rule: Optional[
            "aws_sdk_billingconductor.types.computation_rule_enum.ComputationRuleEnum"
        ] = None,
        presentation_details: Optional[
            "aws_sdk_billingconductor.types.presentation_object.PresentationObject"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.create_custom_line_item_output.CreateCustomLineItemOutput":
        """<p>Creates a custom line item that can be used to create a one-time fixed charge that can be applied to a single billing group for the current or previous billing period. The one-time fixed charge is either a fee or discount. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The name of the custom line item. </p>
            description: <p> The description of the custom line item. This is shown on the Bills page in association with the charge value. </p>
            billing_group_arn: <p> The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to. </p>
            billing_period_range: <p> A time range for which the custom line item is effective. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a custom line item. </p>
            charge_details: <p> A <code>CustomLineItemChargeDetails</code> that describes the charge details for a custom line item. </p>
            account_id: <p>The Amazon Web Services account in which this custom line item will be applied to.</p>
            computation_rule: <p> Specifies how the custom line item charges are computed. </p>
            presentation_details: <p> Details controlling how the custom line item charges are presented in the bill. Contains specifications for which service the charges will be shown under. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.create_custom_line_item_input.CreateCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.create_custom_line_item_output.CreateCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.create_custom_line_item

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.create_custom_line_item.async_create_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.create_custom_line_item_input.CreateCustomLineItemInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        input_["description"] = description
        input_["billing_group_arn"] = billing_group_arn
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range
        if tags is not None:
            input_["tags"] = tags
        input_["charge_details"] = charge_details
        if account_id is not None:
            input_["account_id"] = account_id
        if computation_rule is not None:
            input_["computation_rule"] = computation_rule
        if presentation_details is not None:
            input_["presentation_details"] = presentation_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        name: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_name.CustomLineItemName"
        ] = None,
        description: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
        ] = None,
        charge_details: Optional[
            "aws_sdk_billingconductor.types.update_custom_line_item_charge_details.UpdateCustomLineItemChargeDetails"
        ] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.update_custom_line_item_output.UpdateCustomLineItemOutput":
        """<p> Update an existing custom line item in the current or previous billing period. </p>

        Args:
            arn: <p> The ARN of the custom line item to be updated. </p>
            name: <p> The new name for the custom line item. </p>
            description: <p> The new line item description of the custom line item. </p>
            charge_details: <p> A <code>ListCustomLineItemChargeDetails</code> containing the new charge details for the custom line item. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.update_custom_line_item_input.UpdateCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.update_custom_line_item_output.UpdateCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.update_custom_line_item

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.update_custom_line_item.async_update_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.update_custom_line_item_input.UpdateCustomLineItemInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if charge_details is not None:
            input_["charge_details"] = charge_details
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.delete_custom_line_item_output.DeleteCustomLineItemOutput":
        """<p> Deletes the custom line item identified by the given ARN in the current, or previous billing period. </p>

        Args:
            arn: <p> The ARN of the custom line item to be deleted. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.delete_custom_line_item_input.DeleteCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.delete_custom_line_item_output.DeleteCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.delete_custom_line_item

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.delete_custom_line_item.async_delete_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.delete_custom_line_item_input.DeleteCustomLineItemInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

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
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_custom_line_items_filter.ListCustomLineItemsFilter"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.list_custom_line_items_output.ListCustomLineItemsOutput":
        """<p> A paginated call to get a list of all custom line items (FFLIs) for the given billing period. If you don't provide a billing period, the current billing period is used. </p>

        Args:
            billing_period: <p> The preferred billing period to get custom line items (FFLIs). </p>
            max_results: <p> The maximum number of billing groups to retrieve. </p>
            next_token: <p> The pagination token that's used on subsequent calls to get custom line items (FFLIs). </p>
            filters: <p>A <code>ListCustomLineItemsFilter</code> that specifies the custom line item names and/or billing group Amazon Resource Names (ARNs) to retrieve FFLI information.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.list_custom_line_items_input.ListCustomLineItemsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.list_custom_line_items_output.ListCustomLineItemsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_custom_line_items

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.list_custom_line_items.async_list_custom_line_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_custom_line_items_input.ListCustomLineItemsInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_associate_resources_to_custom_line_item(
        self,
        target_arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        resource_arns: "aws_sdk_billingconductor.types.custom_line_item_batch_associations_list.CustomLineItemBatchAssociationsList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.batch_associate_resources_to_custom_line_item_output.BatchAssociateResourcesToCustomLineItemOutput":
        """<p> Associates a batch of resources to a percentage custom line item. </p>

        Args:
            target_arn: <p> A percentage custom line item ARN to associate the resources to. </p>
            resource_arns: <p> A list containing the ARNs of the resources to be associated. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.batch_associate_resources_to_custom_line_item_input.BatchAssociateResourcesToCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.batch_associate_resources_to_custom_line_item_output.BatchAssociateResourcesToCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.batch_associate_resources_to_custom_line_item

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.batch_associate_resources_to_custom_line_item.async_batch_associate_resources_to_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.batch_associate_resources_to_custom_line_item_input.BatchAssociateResourcesToCustomLineItemInput = {}  # type: ignore[typeddict-item]
        input_["target_arn"] = target_arn
        input_["resource_arns"] = resource_arns
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_disassociate_resources_from_custom_line_item(
        self,
        target_arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        resource_arns: "aws_sdk_billingconductor.types.custom_line_item_batch_disassociations_list.CustomLineItemBatchDisassociationsList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.batch_disassociate_resources_from_custom_line_item_output.BatchDisassociateResourcesFromCustomLineItemOutput":
        """<p> Disassociates a batch of resources from a percentage custom line item. </p>

        Args:
            target_arn: <p> A percentage custom line item ARN to disassociate the resources from. </p>
            resource_arns: <p> A list containing the ARNs of resources to be disassociated. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.batch_disassociate_resources_from_custom_line_item_input.BatchDisassociateResourcesFromCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.batch_disassociate_resources_from_custom_line_item_output.BatchDisassociateResourcesFromCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.batch_disassociate_resources_from_custom_line_item

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.batch_disassociate_resources_from_custom_line_item.async_batch_disassociate_resources_from_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.batch_disassociate_resources_from_custom_line_item_input.BatchDisassociateResourcesFromCustomLineItemInput = {}  # type: ignore[typeddict-item]
        input_["target_arn"] = target_arn
        input_["resource_arns"] = resource_arns
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_custom_line_item_versions(
        self,
        arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_custom_line_item_versions_filter.ListCustomLineItemVersionsFilter"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.list_custom_line_item_versions_output.ListCustomLineItemVersionsOutput":
        """<p>A paginated call to get a list of all custom line item versions.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for the custom line item.</p>
            max_results: <p>The maximum number of custom line item versions to retrieve.</p>
            next_token: <p>The pagination token that's used on subsequent calls to retrieve custom line item versions.</p>
            filters: <p>A <code>ListCustomLineItemVersionsFilter</code> that specifies the billing period range in which the custom line item versions are applied.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.list_custom_line_item_versions_input.ListCustomLineItemVersionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.list_custom_line_item_versions_output.ListCustomLineItemVersionsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_custom_line_item_versions

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.list_custom_line_item_versions.async_list_custom_line_item_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_custom_line_item_versions_input.ListCustomLineItemVersionsInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_resources_associated_to_custom_line_item(
        self,
        arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_filter.ListResourcesAssociatedToCustomLineItemFilter"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_output.ListResourcesAssociatedToCustomLineItemOutput":
        """<p> List the resources that are associated to a custom line item. </p>

        Args:
            billing_period: <p> The billing period for which the resource associations will be listed. </p>
            arn: <p> The ARN of the custom line item for which the resource associations will be listed. </p>
            max_results: <p> (Optional) The maximum number of resource associations to be retrieved. </p>
            next_token: <p> (Optional) The pagination token that's returned by a previous request. </p>
            filters: <p> (Optional) A <code>ListResourcesAssociatedToCustomLineItemFilter</code> that can specify the types of resources that should be retrieved. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_input.ListResourcesAssociatedToCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_output.ListResourcesAssociatedToCustomLineItemOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_resources_associated_to_custom_line_item

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.list_resources_associated_to_custom_line_item.async_list_resources_associated_to_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_input.ListResourcesAssociatedToCustomLineItemInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input_["billing_period"] = billing_period
        input_["arn"] = arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
