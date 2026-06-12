from typing import Optional, TYPE_CHECKING
from aws_sdk_bcm_pricing_calculator._services.async_bcm_pricing_calculator import ensure_async_iterator
from aws_sdk_bcm_pricing_calculator._services.bcm_pricing_calculator import ensure_sync_iterator
from aws_sdk_bcm_pricing_calculator._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
if TYPE_CHECKING:
    from aws_sdk_bcm_pricing_calculator._services.bcm_pricing_calculator import BCMPricingCalculatorClient, BCMPricingCalculatorClientConfig
    from aws_sdk_bcm_pricing_calculator._services.async_bcm_pricing_calculator import AsyncBCMPricingCalculatorClient, AsyncBCMPricingCalculatorClientConfig
    import aws_sdk_bcm_pricing_calculator.types.client_token
    import aws_sdk_bcm_pricing_calculator.types.create_workload_estimate_request
    import aws_sdk_bcm_pricing_calculator.types.create_workload_estimate_response
    import aws_sdk_bcm_pricing_calculator.types.delete_workload_estimate_request
    import aws_sdk_bcm_pricing_calculator.types.delete_workload_estimate_response
    import aws_sdk_bcm_pricing_calculator.types.filter_timestamp
    import aws_sdk_bcm_pricing_calculator.types.get_workload_estimate_request
    import aws_sdk_bcm_pricing_calculator.types.get_workload_estimate_response
    import aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_filters
    import aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_request
    import aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_response
    import aws_sdk_bcm_pricing_calculator.types.max_results
    import aws_sdk_bcm_pricing_calculator.types.next_page_token
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.tags
    import aws_sdk_bcm_pricing_calculator.types.update_workload_estimate_request
    import aws_sdk_bcm_pricing_calculator.types.update_workload_estimate_response
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_name
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_summary

class WorkloadEstimate:
    def __init__(self, service: BCMPricingCalculatorClient) -> None:
        self._service = service
    def create(self, name: "aws_sdk_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName", *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None, client_token: Optional["aws_sdk_bcm_pricing_calculator.types.client_token.ClientToken"] = None, rate_type: Optional["aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type.WorkloadEstimateRateType"] = None, tags: Optional["aws_sdk_bcm_pricing_calculator.types.tags.Tags"] = None) -> "aws_sdk_bcm_pricing_calculator.types.create_workload_estimate_response.CreateWorkloadEstimateResponse":
        """<p> Creates a new workload estimate to model costs for a specific workload. </p>

        Args:
            name: <p> A descriptive name for the workload estimate. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            rate_type: <p> The type of pricing rates to use for the estimate. </p>
            tags: <p> The tags to apply to the workload estimate. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_pricing_calculator.types.create_workload_estimate_request.CreateWorkloadEstimateRequest]') -> OperationResponse["aws_sdk_bcm_pricing_calculator.types.create_workload_estimate_response.CreateWorkloadEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_workload_estimate
            output, http_response = aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_workload_estimate.create_workload_estimate(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.create_workload_estimate_request.CreateWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if client_token is not None:
            input["client_token"] = client_token
        if rate_type is not None:
            input["rate_type"] = rate_type
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.get_workload_estimate_response.GetWorkloadEstimateResponse":
        """<p> Retrieves details of a specific workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to retrieve. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_pricing_calculator.types.get_workload_estimate_request.GetWorkloadEstimateRequest]') -> OperationResponse["aws_sdk_bcm_pricing_calculator.types.get_workload_estimate_response.GetWorkloadEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_workload_estimate
            output, http_response = aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_workload_estimate.get_workload_estimate(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.get_workload_estimate_request.GetWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None, name: Optional["aws_sdk_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName"] = None, expires_at: Optional[datetime.datetime] = None) -> "aws_sdk_bcm_pricing_calculator.types.update_workload_estimate_response.UpdateWorkloadEstimateResponse":
        """<p> Updates an existing workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to update. </p>
            name: <p> The new name for the workload estimate. </p>
            expires_at: <p> The new expiration date for the workload estimate. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_pricing_calculator.types.update_workload_estimate_request.UpdateWorkloadEstimateRequest]') -> OperationResponse["aws_sdk_bcm_pricing_calculator.types.update_workload_estimate_response.UpdateWorkloadEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_workload_estimate
            output, http_response = aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_workload_estimate.update_workload_estimate(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.update_workload_estimate_request.UpdateWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if name is not None:
            input["name"] = name
        if expires_at is not None:
            input["expires_at"] = expires_at

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.delete_workload_estimate_response.DeleteWorkloadEstimateResponse":
        """<p> Deletes an existing workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to delete. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_pricing_calculator.types.delete_workload_estimate_request.DeleteWorkloadEstimateRequest]') -> OperationResponse["aws_sdk_bcm_pricing_calculator.types.delete_workload_estimate_response.DeleteWorkloadEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_workload_estimate
            output, http_response = aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_workload_estimate.delete_workload_estimate(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.delete_workload_estimate_request.DeleteWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[BCMPricingCalculatorClientConfig] = None, created_at_filter: Optional["aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"] = None, expires_at_filter: Optional["aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"] = None, filters: Optional["aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_filters.ListWorkloadEstimatesFilters"] = None, next_token: Optional["aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"] = None, max_results: Optional["aws_sdk_bcm_pricing_calculator.types.max_results.MaxResults"] = None) -> "aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_response.ListWorkloadEstimatesResponse":
        """<p> Lists all workload estimates for the account. </p>

        Args:
            created_at_filter: <p> Filter workload estimates based on the creation date. </p>
            expires_at_filter: <p> Filter workload estimates based on the expiration date. </p>
            filters: <p> Filters to apply to the list of workload estimates. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_request.ListWorkloadEstimatesRequest]') -> OperationResponse["aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_response.ListWorkloadEstimatesResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimates
            output, http_response = aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimates.list_workload_estimates(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_request.ListWorkloadEstimatesRequest = {}  # type: ignore[typeddict-item]
        if created_at_filter is not None:
            input["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input["expires_at_filter"] = expires_at_filter
        if filters is not None:
            input["filters"] = filters
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncWorkloadEstimate:
    def __init__(self, service: AsyncBCMPricingCalculatorClient) -> None:
        self._service = service
    async def create(self, name: "aws_sdk_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None, client_token: Optional["aws_sdk_bcm_pricing_calculator.types.client_token.ClientToken"] = None, rate_type: Optional["aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type.WorkloadEstimateRateType"] = None, tags: Optional["aws_sdk_bcm_pricing_calculator.types.tags.Tags"] = None) -> "aws_sdk_bcm_pricing_calculator.types.create_workload_estimate_response.CreateWorkloadEstimateResponse":
        """<p> Creates a new workload estimate to model costs for a specific workload. </p>

        Args:
            name: <p> A descriptive name for the workload estimate. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            rate_type: <p> The type of pricing rates to use for the estimate. </p>
            tags: <p> The tags to apply to the workload estimate. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.create_workload_estimate_request.CreateWorkloadEstimateRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.create_workload_estimate_response.CreateWorkloadEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_workload_estimate
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_workload_estimate.async_create_workload_estimate(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.create_workload_estimate_request.CreateWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if client_token is not None:
            input["client_token"] = client_token
        if rate_type is not None:
            input["rate_type"] = rate_type
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.get_workload_estimate_response.GetWorkloadEstimateResponse":
        """<p> Retrieves details of a specific workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to retrieve. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.get_workload_estimate_request.GetWorkloadEstimateRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.get_workload_estimate_response.GetWorkloadEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_workload_estimate
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_workload_estimate.async_get_workload_estimate(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.get_workload_estimate_request.GetWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None, name: Optional["aws_sdk_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName"] = None, expires_at: Optional[datetime.datetime] = None) -> "aws_sdk_bcm_pricing_calculator.types.update_workload_estimate_response.UpdateWorkloadEstimateResponse":
        """<p> Updates an existing workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to update. </p>
            name: <p> The new name for the workload estimate. </p>
            expires_at: <p> The new expiration date for the workload estimate. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.update_workload_estimate_request.UpdateWorkloadEstimateRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.update_workload_estimate_response.UpdateWorkloadEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_workload_estimate
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_workload_estimate.async_update_workload_estimate(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.update_workload_estimate_request.UpdateWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if name is not None:
            input["name"] = name
        if expires_at is not None:
            input["expires_at"] = expires_at

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.delete_workload_estimate_response.DeleteWorkloadEstimateResponse":
        """<p> Deletes an existing workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to delete. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.delete_workload_estimate_request.DeleteWorkloadEstimateRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.delete_workload_estimate_response.DeleteWorkloadEstimateResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_workload_estimate
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_workload_estimate.async_delete_workload_estimate(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.delete_workload_estimate_request.DeleteWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None, created_at_filter: Optional["aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"] = None, expires_at_filter: Optional["aws_sdk_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"] = None, filters: Optional["aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_filters.ListWorkloadEstimatesFilters"] = None, next_token: Optional["aws_sdk_bcm_pricing_calculator.types.next_page_token.NextPageToken"] = None, max_results: Optional["aws_sdk_bcm_pricing_calculator.types.max_results.MaxResults"] = None) -> "aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_response.ListWorkloadEstimatesResponse":
        """<p> Lists all workload estimates for the account. </p>

        Args:
            created_at_filter: <p> Filter workload estimates based on the creation date. </p>
            expires_at_filter: <p> Filter workload estimates based on the expiration date. </p>
            filters: <p> Filters to apply to the list of workload estimates. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_request.ListWorkloadEstimatesRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_response.ListWorkloadEstimatesResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimates
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimates.async_list_workload_estimates(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.list_workload_estimates_request.ListWorkloadEstimatesRequest = {}  # type: ignore[typeddict-item]
        if created_at_filter is not None:
            input["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input["expires_at_filter"] = expires_at_filter
        if filters is not None:
            input["filters"] = filters
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output