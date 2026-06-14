import datetime
from typing import TYPE_CHECKING, Optional

from aws_sdk_bcm_pricing_calculator._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_name
    import aws_sdk_bcm_pricing_calculator.types.bill_scenario_summary
    import aws_sdk_bcm_pricing_calculator.types.client_token
    import aws_sdk_bcm_pricing_calculator.types.cost_category_arn
    import aws_sdk_bcm_pricing_calculator.types.create_bill_scenario_request
    import aws_sdk_bcm_pricing_calculator.types.create_bill_scenario_response
    import aws_sdk_bcm_pricing_calculator.types.delete_bill_scenario_request
    import aws_sdk_bcm_pricing_calculator.types.delete_bill_scenario_response
    import aws_sdk_bcm_pricing_calculator.types.filter_timestamp
    import aws_sdk_bcm_pricing_calculator.types.get_bill_scenario_request
    import aws_sdk_bcm_pricing_calculator.types.get_bill_scenario_response
    import aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum
    import aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filters
    import aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_request
    import aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_response
    import aws_sdk_bcm_pricing_calculator.types.max_results
    import aws_sdk_bcm_pricing_calculator.types.next_page_token
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.tags
    import aws_sdk_bcm_pricing_calculator.types.update_bill_scenario_request
    import aws_sdk_bcm_pricing_calculator.types.update_bill_scenario_response
    from aws_sdk_bcm_pricing_calculator._services.async_bcm_pricing_calculator import (
        AsyncBCMPricingCalculatorClient,
        AsyncBCMPricingCalculatorClientConfig,
    )
    from aws_sdk_bcm_pricing_calculator._services.bcm_pricing_calculator import (
        BCMPricingCalculatorClient,
        BCMPricingCalculatorClientConfig,
    )


class BillScenario:
    def __init__(self, service: BCMPricingCalculatorClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_bcm_pricing_calculator.types.tags.Tags"] = None,
        group_sharing_preference: Optional[
            "aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
        ] = None,
        cost_category_group_sharing_preference_arn: Optional[
            "aws_sdk_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
        ] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.create_bill_scenario_response.CreateBillScenarioResponse":
        """<p> Creates a new bill scenario to model potential changes to Amazon Web Services usage and costs. </p>

        Args:
            name: <p> A descriptive name for the bill scenario. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            tags: <p> The tags to apply to the bill scenario. </p>
            group_sharing_preference: <p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>
            cost_category_group_sharing_preference_arn: <p>The arn of the cost category used in the reserved and prioritized group sharing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_pricing_calculator.types.create_bill_scenario_request.CreateBillScenarioRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.create_bill_scenario_response.CreateBillScenarioResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_scenario

            output, http_response = (
                aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_scenario.create_bill_scenario(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.create_bill_scenario_request.CreateBillScenarioRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags
        if group_sharing_preference is not None:
            input["group_sharing_preference"] = group_sharing_preference
        if cost_category_group_sharing_preference_arn is not None:
            input["cost_category_group_sharing_preference_arn"] = (
                cost_category_group_sharing_preference_arn
            )

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.get_bill_scenario_response.GetBillScenarioResponse":
        """<p> Retrieves details of a specific bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to retrieve. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_pricing_calculator.types.get_bill_scenario_request.GetBillScenarioRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.get_bill_scenario_response.GetBillScenarioResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_scenario

            output, http_response = (
                aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_scenario.get_bill_scenario(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.get_bill_scenario_request.GetBillScenarioRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
        name: Optional[
            "aws_sdk_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
        group_sharing_preference: Optional[
            "aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
        ] = None,
        cost_category_group_sharing_preference_arn: Optional[
            "aws_sdk_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
        ] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.update_bill_scenario_response.UpdateBillScenarioResponse":
        """<p> Updates an existing bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to update. </p>
            name: <p> The new name for the bill scenario. </p>
            expires_at: <p> The new expiration date for the bill scenario. </p>
            group_sharing_preference: <p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>
            cost_category_group_sharing_preference_arn: <p>The arn of the cost category used in the reserved and prioritized group sharing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_pricing_calculator.types.update_bill_scenario_request.UpdateBillScenarioRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.update_bill_scenario_response.UpdateBillScenarioResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_scenario

            output, http_response = (
                aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_scenario.update_bill_scenario(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.update_bill_scenario_request.UpdateBillScenarioRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if name is not None:
            input["name"] = name
        if expires_at is not None:
            input["expires_at"] = expires_at
        if group_sharing_preference is not None:
            input["group_sharing_preference"] = group_sharing_preference
        if cost_category_group_sharing_preference_arn is not None:
            input["cost_category_group_sharing_preference_arn"] = (
                cost_category_group_sharing_preference_arn
            )

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.delete_bill_scenario_response.DeleteBillScenarioResponse":
        """<p> Deletes an existing bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to delete. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_pricing_calculator.types.delete_bill_scenario_request.DeleteBillScenarioRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.delete_bill_scenario_response.DeleteBillScenarioResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_scenario

            output, http_response = (
                aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_scenario.delete_bill_scenario(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.delete_bill_scenario_request.DeleteBillScenarioRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filters.ListBillScenariosFilters"
        ] = None,
        created_at_filter: Optional[
            "aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        next_token: Optional[
            "aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_response.ListBillScenariosResponse":
        """<p> Lists all bill scenarios for the account. </p>

        Args:
            filters: <p> Filters to apply to the list of bill scenarios. </p>
            created_at_filter: <p> Filter bill scenarios based on the creation date. </p>
            expires_at_filter: <p> Filter bill scenarios based on the expiration date. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_request.ListBillScenariosRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_response.ListBillScenariosResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenarios

            output, http_response = (
                aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenarios.list_bill_scenarios(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_request.ListBillScenariosRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if created_at_filter is not None:
            input["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input["expires_at_filter"] = expires_at_filter
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncBillScenario:
    def __init__(self, service: AsyncBCMPricingCalculatorClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_bcm_pricing_calculator.types.tags.Tags"] = None,
        group_sharing_preference: Optional[
            "aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
        ] = None,
        cost_category_group_sharing_preference_arn: Optional[
            "aws_sdk_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
        ] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.create_bill_scenario_response.CreateBillScenarioResponse":
        """<p> Creates a new bill scenario to model potential changes to Amazon Web Services usage and costs. </p>

        Args:
            name: <p> A descriptive name for the bill scenario. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            tags: <p> The tags to apply to the bill scenario. </p>
            group_sharing_preference: <p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>
            cost_category_group_sharing_preference_arn: <p>The arn of the cost category used in the reserved and prioritized group sharing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.create_bill_scenario_request.CreateBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.create_bill_scenario_response.CreateBillScenarioResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_scenario

            (
                output,
                http_response,
            ) = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_scenario.async_create_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.create_bill_scenario_request.CreateBillScenarioRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags
        if group_sharing_preference is not None:
            input["group_sharing_preference"] = group_sharing_preference
        if cost_category_group_sharing_preference_arn is not None:
            input["cost_category_group_sharing_preference_arn"] = (
                cost_category_group_sharing_preference_arn
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.get_bill_scenario_response.GetBillScenarioResponse":
        """<p> Retrieves details of a specific bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to retrieve. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.get_bill_scenario_request.GetBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.get_bill_scenario_response.GetBillScenarioResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_scenario

            (
                output,
                http_response,
            ) = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_scenario.async_get_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.get_bill_scenario_request.GetBillScenarioRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        name: Optional[
            "aws_sdk_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
        group_sharing_preference: Optional[
            "aws_sdk_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
        ] = None,
        cost_category_group_sharing_preference_arn: Optional[
            "aws_sdk_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
        ] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.update_bill_scenario_response.UpdateBillScenarioResponse":
        """<p> Updates an existing bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to update. </p>
            name: <p> The new name for the bill scenario. </p>
            expires_at: <p> The new expiration date for the bill scenario. </p>
            group_sharing_preference: <p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>
            cost_category_group_sharing_preference_arn: <p>The arn of the cost category used in the reserved and prioritized group sharing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.update_bill_scenario_request.UpdateBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.update_bill_scenario_response.UpdateBillScenarioResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_scenario

            (
                output,
                http_response,
            ) = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_scenario.async_update_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.update_bill_scenario_request.UpdateBillScenarioRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if name is not None:
            input["name"] = name
        if expires_at is not None:
            input["expires_at"] = expires_at
        if group_sharing_preference is not None:
            input["group_sharing_preference"] = group_sharing_preference
        if cost_category_group_sharing_preference_arn is not None:
            input["cost_category_group_sharing_preference_arn"] = (
                cost_category_group_sharing_preference_arn
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.delete_bill_scenario_response.DeleteBillScenarioResponse":
        """<p> Deletes an existing bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to delete. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.delete_bill_scenario_request.DeleteBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.delete_bill_scenario_response.DeleteBillScenarioResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_scenario

            (
                output,
                http_response,
            ) = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_scenario.async_delete_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.delete_bill_scenario_request.DeleteBillScenarioRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_filters.ListBillScenariosFilters"
        ] = None,
        created_at_filter: Optional[
            "aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        next_token: Optional[
            "aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_response.ListBillScenariosResponse":
        """<p> Lists all bill scenarios for the account. </p>

        Args:
            filters: <p> Filters to apply to the list of bill scenarios. </p>
            created_at_filter: <p> Filter bill scenarios based on the creation date. </p>
            expires_at_filter: <p> Filter bill scenarios based on the expiration date. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_request.ListBillScenariosRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_response.ListBillScenariosResponse"
        ]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenarios

            (
                output,
                http_response,
            ) = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenarios.async_list_bill_scenarios(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.list_bill_scenarios_request.ListBillScenariosRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if created_at_filter is not None:
            input["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input["expires_at_filter"] = expires_at_filter
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
