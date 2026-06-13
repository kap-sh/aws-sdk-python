from typing import TYPE_CHECKING, Optional

import aws_sdk_braket._auth._signers
import aws_sdk_braket._auth._sigv4
from aws_sdk_braket._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_braket.types.create_spending_limit_request
    import aws_sdk_braket.types.create_spending_limit_response
    import aws_sdk_braket.types.delete_spending_limit_request
    import aws_sdk_braket.types.delete_spending_limit_response
    import aws_sdk_braket.types.device_arn
    import aws_sdk_braket.types.search_spending_limits_filter_list
    import aws_sdk_braket.types.search_spending_limits_request
    import aws_sdk_braket.types.search_spending_limits_response
    import aws_sdk_braket.types.spending_limit_arn
    import aws_sdk_braket.types.spending_limit_summary
    import aws_sdk_braket.types.string64
    import aws_sdk_braket.types.tags_map
    import aws_sdk_braket.types.time_period
    import aws_sdk_braket.types.update_spending_limit_request
    import aws_sdk_braket.types.update_spending_limit_response
    from aws_sdk_braket._services.async_braket import (
        AsyncBraketClient,
        AsyncBraketClientConfig,
    )
    from aws_sdk_braket._services.braket import BraketClient, BraketClientConfig


class SpendingLimitResource:
    def __init__(self, service: BraketClient) -> None:
        self._service = service

    def create(
        self,
        client_token: "aws_sdk_braket.types.string64.String64",
        device_arn: "aws_sdk_braket.types.device_arn.DeviceArn",
        spending_limit: str,
        *,
        config_overrides: Optional[BraketClientConfig] = None,
        time_period: Optional["aws_sdk_braket.types.time_period.TimePeriod"] = None,
        tags: Optional["aws_sdk_braket.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_braket.types.create_spending_limit_response.CreateSpendingLimitResponse":
        """<p>Creates a spending limit for a specified quantum device. Spending limits help you control costs by setting maximum amounts that can be spent on quantum computing tasks within a specified time period. Simulators do not support spending limits.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.</p>
            device_arn: <p>The Amazon Resource Name (ARN) of the quantum device to apply the spending limit to.</p>
            spending_limit: <p>The maximum amount that can be spent on the specified device, in USD.</p>
            time_period: <p>The time period during which the spending limit is active, including start and end dates.</p>
            tags: <p>The tags to apply to the spending limit. Each tag consists of a key and an optional value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.create_spending_limit_request.CreateSpendingLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.create_spending_limit_response.CreateSpendingLimitResponse"
        ]:
            import aws_sdk_braket._operations.braket.create_spending_limit

            output, http_response = (
                aws_sdk_braket._operations.braket.create_spending_limit.create_spending_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.create_spending_limit_request.CreateSpendingLimitRequest = {}  # type: ignore[typeddict-item]
        input["client_token"] = client_token
        input["device_arn"] = device_arn
        input["spending_limit"] = spending_limit
        if time_period is not None:
            input["time_period"] = time_period
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        spending_limit_arn: "aws_sdk_braket.types.spending_limit_arn.SpendingLimitArn",
        client_token: "aws_sdk_braket.types.string64.String64",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
        spending_limit: Optional[str] = None,
        time_period: Optional["aws_sdk_braket.types.time_period.TimePeriod"] = None,
    ) -> "aws_sdk_braket.types.update_spending_limit_response.UpdateSpendingLimitResponse":
        """<p>Updates an existing spending limit. You can modify the spending amount or time period. Changes take effect immediately.</p>

        Args:
            spending_limit_arn: <p>The Amazon Resource Name (ARN) of the spending limit to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.</p>
            spending_limit: <p>The new maximum amount that can be spent on the specified device, in USD.</p>
            time_period: <p>The new time period during which the spending limit is active, including start and end dates.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.update_spending_limit_request.UpdateSpendingLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.update_spending_limit_response.UpdateSpendingLimitResponse"
        ]:
            import aws_sdk_braket._operations.braket.update_spending_limit

            output, http_response = (
                aws_sdk_braket._operations.braket.update_spending_limit.update_spending_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.update_spending_limit_request.UpdateSpendingLimitRequest = {}  # type: ignore[typeddict-item]
        input["spending_limit_arn"] = spending_limit_arn
        input["client_token"] = client_token
        if spending_limit is not None:
            input["spending_limit"] = spending_limit
        if time_period is not None:
            input["time_period"] = time_period

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        spending_limit_arn: "aws_sdk_braket.types.spending_limit_arn.SpendingLimitArn",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
    ) -> "aws_sdk_braket.types.delete_spending_limit_response.DeleteSpendingLimitResponse":
        """<p>Deletes an existing spending limit. This operation permanently removes the spending limit and cannot be undone. After deletion, the associated device becomes unrestricted for spending.</p>

        Args:
            spending_limit_arn: <p>The Amazon Resource Name (ARN) of the spending limit to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.delete_spending_limit_request.DeleteSpendingLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.delete_spending_limit_response.DeleteSpendingLimitResponse"
        ]:
            import aws_sdk_braket._operations.braket.delete_spending_limit

            output, http_response = (
                aws_sdk_braket._operations.braket.delete_spending_limit.delete_spending_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.delete_spending_limit_request.DeleteSpendingLimitRequest = {}  # type: ignore[typeddict-item]
        input["spending_limit_arn"] = spending_limit_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "aws_sdk_braket.types.search_spending_limits_filter_list.SearchSpendingLimitsFilterList"
        ] = None,
    ) -> "aws_sdk_braket.types.search_spending_limits_response.SearchSpendingLimitsResponse":
        """<p>Searches and lists spending limits based on specified filters. This operation supports pagination and allows filtering by various criteria to find specific spending limits. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            next_token: <p>The token to retrieve the next page of results. This value is returned from a previous call to SearchSpendingLimits when there are more results available.</p>
            max_results: <p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 100. Default is 20.</p>
            filters: <p>The filters to apply when searching for spending limits. Use filters to narrow down the results based on specific criteria.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.search_spending_limits_request.SearchSpendingLimitsRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.search_spending_limits_response.SearchSpendingLimitsResponse"
        ]:
            import aws_sdk_braket._operations.braket.search_spending_limits

            output, http_response = (
                aws_sdk_braket._operations.braket.search_spending_limits.search_spending_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.search_spending_limits_request.SearchSpendingLimitsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSpendingLimitResource:
    def __init__(self, service: AsyncBraketClient) -> None:
        self._service = service

    async def create(
        self,
        client_token: "aws_sdk_braket.types.string64.String64",
        device_arn: "aws_sdk_braket.types.device_arn.DeviceArn",
        spending_limit: str,
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        time_period: Optional["aws_sdk_braket.types.time_period.TimePeriod"] = None,
        tags: Optional["aws_sdk_braket.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_braket.types.create_spending_limit_response.CreateSpendingLimitResponse":
        """<p>Creates a spending limit for a specified quantum device. Spending limits help you control costs by setting maximum amounts that can be spent on quantum computing tasks within a specified time period. Simulators do not support spending limits.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.</p>
            device_arn: <p>The Amazon Resource Name (ARN) of the quantum device to apply the spending limit to.</p>
            spending_limit: <p>The maximum amount that can be spent on the specified device, in USD.</p>
            time_period: <p>The time period during which the spending limit is active, including start and end dates.</p>
            tags: <p>The tags to apply to the spending limit. Each tag consists of a key and an optional value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_braket.types.create_spending_limit_request.CreateSpendingLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_braket.types.create_spending_limit_response.CreateSpendingLimitResponse"
        ]:
            import aws_sdk_braket._operations.braket.create_spending_limit

            (
                output,
                http_response,
            ) = await aws_sdk_braket._operations.braket.create_spending_limit.async_create_spending_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.create_spending_limit_request.CreateSpendingLimitRequest = {}  # type: ignore[typeddict-item]
        input["client_token"] = client_token
        input["device_arn"] = device_arn
        input["spending_limit"] = spending_limit
        if time_period is not None:
            input["time_period"] = time_period
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        spending_limit_arn: "aws_sdk_braket.types.spending_limit_arn.SpendingLimitArn",
        client_token: "aws_sdk_braket.types.string64.String64",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        spending_limit: Optional[str] = None,
        time_period: Optional["aws_sdk_braket.types.time_period.TimePeriod"] = None,
    ) -> "aws_sdk_braket.types.update_spending_limit_response.UpdateSpendingLimitResponse":
        """<p>Updates an existing spending limit. You can modify the spending amount or time period. Changes take effect immediately.</p>

        Args:
            spending_limit_arn: <p>The Amazon Resource Name (ARN) of the spending limit to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.</p>
            spending_limit: <p>The new maximum amount that can be spent on the specified device, in USD.</p>
            time_period: <p>The new time period during which the spending limit is active, including start and end dates.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_braket.types.update_spending_limit_request.UpdateSpendingLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_braket.types.update_spending_limit_response.UpdateSpendingLimitResponse"
        ]:
            import aws_sdk_braket._operations.braket.update_spending_limit

            (
                output,
                http_response,
            ) = await aws_sdk_braket._operations.braket.update_spending_limit.async_update_spending_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.update_spending_limit_request.UpdateSpendingLimitRequest = {}  # type: ignore[typeddict-item]
        input["spending_limit_arn"] = spending_limit_arn
        input["client_token"] = client_token
        if spending_limit is not None:
            input["spending_limit"] = spending_limit
        if time_period is not None:
            input["time_period"] = time_period

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        spending_limit_arn: "aws_sdk_braket.types.spending_limit_arn.SpendingLimitArn",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "aws_sdk_braket.types.delete_spending_limit_response.DeleteSpendingLimitResponse":
        """<p>Deletes an existing spending limit. This operation permanently removes the spending limit and cannot be undone. After deletion, the associated device becomes unrestricted for spending.</p>

        Args:
            spending_limit_arn: <p>The Amazon Resource Name (ARN) of the spending limit to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_braket.types.delete_spending_limit_request.DeleteSpendingLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_braket.types.delete_spending_limit_response.DeleteSpendingLimitResponse"
        ]:
            import aws_sdk_braket._operations.braket.delete_spending_limit

            (
                output,
                http_response,
            ) = await aws_sdk_braket._operations.braket.delete_spending_limit.async_delete_spending_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.delete_spending_limit_request.DeleteSpendingLimitRequest = {}  # type: ignore[typeddict-item]
        input["spending_limit_arn"] = spending_limit_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "aws_sdk_braket.types.search_spending_limits_filter_list.SearchSpendingLimitsFilterList"
        ] = None,
    ) -> "aws_sdk_braket.types.search_spending_limits_response.SearchSpendingLimitsResponse":
        """<p>Searches and lists spending limits based on specified filters. This operation supports pagination and allows filtering by various criteria to find specific spending limits. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            next_token: <p>The token to retrieve the next page of results. This value is returned from a previous call to SearchSpendingLimits when there are more results available.</p>
            max_results: <p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 100. Default is 20.</p>
            filters: <p>The filters to apply when searching for spending limits. Use filters to narrow down the results based on specific criteria.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_braket.types.search_spending_limits_request.SearchSpendingLimitsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_braket.types.search_spending_limits_response.SearchSpendingLimitsResponse"
        ]:
            import aws_sdk_braket._operations.braket.search_spending_limits

            (
                output,
                http_response,
            ) = await aws_sdk_braket._operations.braket.search_spending_limits.async_search_spending_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.search_spending_limits_request.SearchSpendingLimitsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if filters is not None:
            input["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
