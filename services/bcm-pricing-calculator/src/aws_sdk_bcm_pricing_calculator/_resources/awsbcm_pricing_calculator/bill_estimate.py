from typing import Optional, TYPE_CHECKING
from aws_sdk_bcm_pricing_calculator._services.async_bcm_pricing_calculator import ensure_async_iterator
from aws_sdk_bcm_pricing_calculator._services.bcm_pricing_calculator import ensure_sync_iterator
from aws_sdk_bcm_pricing_calculator._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
if TYPE_CHECKING:
    from aws_sdk_bcm_pricing_calculator._services.bcm_pricing_calculator import BCMPricingCalculatorClient, BCMPricingCalculatorClientConfig
    from aws_sdk_bcm_pricing_calculator._services.async_bcm_pricing_calculator import AsyncBCMPricingCalculatorClient, AsyncBCMPricingCalculatorClientConfig
    import aws_sdk_bcm_pricing_calculator.types.bill_estimate_name
    import aws_sdk_bcm_pricing_calculator.types.bill_estimate_summary
    import aws_sdk_bcm_pricing_calculator.types.client_token
    import aws_sdk_bcm_pricing_calculator.types.create_bill_estimate_request
    import aws_sdk_bcm_pricing_calculator.types.create_bill_estimate_response
    import aws_sdk_bcm_pricing_calculator.types.delete_bill_estimate_request
    import aws_sdk_bcm_pricing_calculator.types.delete_bill_estimate_response
    import aws_sdk_bcm_pricing_calculator.types.filter_timestamp
    import aws_sdk_bcm_pricing_calculator.types.get_bill_estimate_request
    import aws_sdk_bcm_pricing_calculator.types.get_bill_estimate_response
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filters
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_request
    import aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_response
    import aws_sdk_bcm_pricing_calculator.types.max_results
    import aws_sdk_bcm_pricing_calculator.types.next_page_token
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.tags
    import aws_sdk_bcm_pricing_calculator.types.update_bill_estimate_request
    import aws_sdk_bcm_pricing_calculator.types.update_bill_estimate_response

class BillEstimate:
    def __init__(self, service: BCMPricingCalculatorClient) -> None:
        self._service = service
    def create(self, bill_scenario_id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", name: "aws_sdk_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName", *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None, client_token: Optional["aws_sdk_bcm_pricing_calculator.types.client_token.ClientToken"] = None, tags: Optional["aws_sdk_bcm_pricing_calculator.types.tags.Tags"] = None) -> "aws_sdk_bcm_pricing_calculator.types.create_bill_estimate_response.CreateBillEstimateResponse":
        """<p> Create a Bill estimate from a Bill scenario. In the Bill scenario you can model usage addition, usage changes, and usage removal. You can also model commitment addition and commitment removal. After all changes in a Bill scenario is made satisfactorily, you can call this API with a Bill scenario ID to generate the Bill estimate. Bill estimate calculates the pre-tax cost for your consolidated billing family, incorporating all modeled usage and commitments alongside existing usage and commitments from your most recent completed anniversary bill, with any applicable discounts applied. </p>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to create a Bill estimate. </p>
            name: <p> The name of the Bill estimate that will be created. Names must be unique for an account. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>
            tags: <p> An optional list of tags to associate with the specified BillEstimate. You can use resource tags to control access to your BillEstimate using IAM policies. Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags: </p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services. </p> </li> <li> <p>The maximum length of a key is 128 characters.</p> </li> <li> <p>The maximum length of a value is 256 characters.</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code>.</p> </li> <li> <p>Keys and values are case sensitive.</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services.</p> </li> </ul>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_pricing_calculator.types.create_bill_estimate_request.CreateBillEstimateRequest]') -> OperationResponse["aws_sdk_bcm_pricing_calculator.types.create_bill_estimate_response.CreateBillEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_estimate
            output, http_response = aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_estimate.create_bill_estimate(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.create_bill_estimate_request.CreateBillEstimateRequest = {}  # type: ignore[typeddict-item]
        input["bill_scenario_id"] = bill_scenario_id
        input["name"] = name
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.get_bill_estimate_response.GetBillEstimateResponse":
        """<p> Retrieves details of a specific bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to retrieve. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_pricing_calculator.types.get_bill_estimate_request.GetBillEstimateRequest]') -> OperationResponse["aws_sdk_bcm_pricing_calculator.types.get_bill_estimate_response.GetBillEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_estimate
            output, http_response = aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_estimate.get_bill_estimate(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.get_bill_estimate_request.GetBillEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None, name: Optional["aws_sdk_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"] = None, expires_at: Optional[datetime.datetime] = None) -> "aws_sdk_bcm_pricing_calculator.types.update_bill_estimate_response.UpdateBillEstimateResponse":
        """<p> Updates an existing bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to update. </p>
            name: <p> The new name for the bill estimate. </p>
            expires_at: <p> The new expiration date for the bill estimate. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_pricing_calculator.types.update_bill_estimate_request.UpdateBillEstimateRequest]') -> OperationResponse["aws_sdk_bcm_pricing_calculator.types.update_bill_estimate_response.UpdateBillEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_estimate
            output, http_response = aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_estimate.update_bill_estimate(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.update_bill_estimate_request.UpdateBillEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if name is not None:
            input["name"] = name
        if expires_at is not None:
            input["expires_at"] = expires_at

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.delete_bill_estimate_response.DeleteBillEstimateResponse":
        """<p> Deletes an existing bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to delete. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_pricing_calculator.types.delete_bill_estimate_request.DeleteBillEstimateRequest]') -> OperationResponse["aws_sdk_bcm_pricing_calculator.types.delete_bill_estimate_response.DeleteBillEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_estimate
            output, http_response = aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_estimate.delete_bill_estimate(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.delete_bill_estimate_request.DeleteBillEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None, filters: Optional["aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filters.ListBillEstimatesFilters"] = None, created_at_filter: Optional["aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"] = None, expires_at_filter: Optional["aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"] = None, next_token: Optional["aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"] = None, max_results: Optional["aws_sdk_bcm_pricing_calculator.types.max_results.MaxResults"] = None) -> "aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_response.ListBillEstimatesResponse":
        """<p> Lists all bill estimates for the account. </p>

        Args:
            filters: <p> Filters to apply to the list of bill estimates. </p>
            created_at_filter: <p> Filter bill estimates based on the creation date. </p>
            expires_at_filter: <p> Filter bill estimates based on the expiration date. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_request.ListBillEstimatesRequest]') -> OperationResponse["aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_response.ListBillEstimatesResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimates
            output, http_response = aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimates.list_bill_estimates(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_request.ListBillEstimatesRequest = {}  # type: ignore[typeddict-item]
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

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncBillEstimate:
    def __init__(self, service: AsyncBCMPricingCalculatorClient) -> None:
        self._service = service
    async def create(self, bill_scenario_id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", name: "aws_sdk_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None, client_token: Optional["aws_sdk_bcm_pricing_calculator.types.client_token.ClientToken"] = None, tags: Optional["aws_sdk_bcm_pricing_calculator.types.tags.Tags"] = None) -> "aws_sdk_bcm_pricing_calculator.types.create_bill_estimate_response.CreateBillEstimateResponse":
        """<p> Create a Bill estimate from a Bill scenario. In the Bill scenario you can model usage addition, usage changes, and usage removal. You can also model commitment addition and commitment removal. After all changes in a Bill scenario is made satisfactorily, you can call this API with a Bill scenario ID to generate the Bill estimate. Bill estimate calculates the pre-tax cost for your consolidated billing family, incorporating all modeled usage and commitments alongside existing usage and commitments from your most recent completed anniversary bill, with any applicable discounts applied. </p>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to create a Bill estimate. </p>
            name: <p> The name of the Bill estimate that will be created. Names must be unique for an account. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>
            tags: <p> An optional list of tags to associate with the specified BillEstimate. You can use resource tags to control access to your BillEstimate using IAM policies. Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags: </p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services. </p> </li> <li> <p>The maximum length of a key is 128 characters.</p> </li> <li> <p>The maximum length of a value is 256 characters.</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code>.</p> </li> <li> <p>Keys and values are case sensitive.</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services.</p> </li> </ul>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.create_bill_estimate_request.CreateBillEstimateRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.create_bill_estimate_response.CreateBillEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_estimate
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_estimate.async_create_bill_estimate(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.create_bill_estimate_request.CreateBillEstimateRequest = {}  # type: ignore[typeddict-item]
        input["bill_scenario_id"] = bill_scenario_id
        input["name"] = name
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.get_bill_estimate_response.GetBillEstimateResponse":
        """<p> Retrieves details of a specific bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to retrieve. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.get_bill_estimate_request.GetBillEstimateRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.get_bill_estimate_response.GetBillEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_estimate
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_estimate.async_get_bill_estimate(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.get_bill_estimate_request.GetBillEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None, name: Optional["aws_sdk_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"] = None, expires_at: Optional[datetime.datetime] = None) -> "aws_sdk_bcm_pricing_calculator.types.update_bill_estimate_response.UpdateBillEstimateResponse":
        """<p> Updates an existing bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to update. </p>
            name: <p> The new name for the bill estimate. </p>
            expires_at: <p> The new expiration date for the bill estimate. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.update_bill_estimate_request.UpdateBillEstimateRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.update_bill_estimate_response.UpdateBillEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_estimate
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_estimate.async_update_bill_estimate(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.update_bill_estimate_request.UpdateBillEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if name is not None:
            input["name"] = name
        if expires_at is not None:
            input["expires_at"] = expires_at

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.delete_bill_estimate_response.DeleteBillEstimateResponse":
        """<p> Deletes an existing bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to delete. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.delete_bill_estimate_request.DeleteBillEstimateRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.delete_bill_estimate_response.DeleteBillEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_estimate
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_estimate.async_delete_bill_estimate(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.delete_bill_estimate_request.DeleteBillEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None, filters: Optional["aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_filters.ListBillEstimatesFilters"] = None, created_at_filter: Optional["aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"] = None, expires_at_filter: Optional["aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"] = None, next_token: Optional["aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"] = None, max_results: Optional["aws_sdk_bcm_pricing_calculator.types.max_results.MaxResults"] = None) -> "aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_response.ListBillEstimatesResponse":
        """<p> Lists all bill estimates for the account. </p>

        Args:
            filters: <p> Filters to apply to the list of bill estimates. </p>
            created_at_filter: <p> Filter bill estimates based on the creation date. </p>
            expires_at_filter: <p> Filter bill estimates based on the expiration date. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_request.ListBillEstimatesRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_response.ListBillEstimatesResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimates
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimates.async_list_bill_estimates(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.list_bill_estimates_request.ListBillEstimatesRequest = {}  # type: ignore[typeddict-item]
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

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output