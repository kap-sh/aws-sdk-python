"""Generated from Smithy shape ``com.amazonaws.savingsplans#AWSSavingsPlan``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_savingsplans._auth._signers
import aws_sdk_savingsplans._auth._sigv4
from aws_sdk_savingsplans._auth._identity import Credentials
from aws_sdk_savingsplans._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_savingsplans._auth._zapros_handler import AuthMiddleware
from aws_sdk_savingsplans._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.amount
    import aws_sdk_savingsplans.types.client_token
    import aws_sdk_savingsplans.types.create_savings_plan_request
    import aws_sdk_savingsplans.types.create_savings_plan_response
    import aws_sdk_savingsplans.types.currency_list
    import aws_sdk_savingsplans.types.date_time
    import aws_sdk_savingsplans.types.delete_queued_savings_plan_request
    import aws_sdk_savingsplans.types.delete_queued_savings_plan_response
    import aws_sdk_savingsplans.types.describe_savings_plan_rates_request
    import aws_sdk_savingsplans.types.describe_savings_plan_rates_response
    import aws_sdk_savingsplans.types.describe_savings_plans_offering_rates_request
    import aws_sdk_savingsplans.types.describe_savings_plans_offering_rates_response
    import aws_sdk_savingsplans.types.describe_savings_plans_offerings_request
    import aws_sdk_savingsplans.types.describe_savings_plans_offerings_response
    import aws_sdk_savingsplans.types.describe_savings_plans_request
    import aws_sdk_savingsplans.types.describe_savings_plans_response
    import aws_sdk_savingsplans.types.durations_list
    import aws_sdk_savingsplans.types.list_tags_for_resource_request
    import aws_sdk_savingsplans.types.list_tags_for_resource_response
    import aws_sdk_savingsplans.types.max_results
    import aws_sdk_savingsplans.types.page_size
    import aws_sdk_savingsplans.types.pagination_token
    import aws_sdk_savingsplans.types.return_savings_plan_request
    import aws_sdk_savingsplans.types.return_savings_plan_response
    import aws_sdk_savingsplans.types.savings_plan_arn
    import aws_sdk_savingsplans.types.savings_plan_arn_list
    import aws_sdk_savingsplans.types.savings_plan_descriptions_list
    import aws_sdk_savingsplans.types.savings_plan_filter_list
    import aws_sdk_savingsplans.types.savings_plan_id
    import aws_sdk_savingsplans.types.savings_plan_id_list
    import aws_sdk_savingsplans.types.savings_plan_offering_filters_list
    import aws_sdk_savingsplans.types.savings_plan_offering_id
    import aws_sdk_savingsplans.types.savings_plan_offering_rate_filters_list
    import aws_sdk_savingsplans.types.savings_plan_operation_list
    import aws_sdk_savingsplans.types.savings_plan_payment_option_list
    import aws_sdk_savingsplans.types.savings_plan_product_type
    import aws_sdk_savingsplans.types.savings_plan_product_type_list
    import aws_sdk_savingsplans.types.savings_plan_rate_filter_list
    import aws_sdk_savingsplans.types.savings_plan_rate_operation_list
    import aws_sdk_savingsplans.types.savings_plan_rate_service_code_list
    import aws_sdk_savingsplans.types.savings_plan_rate_usage_type_list
    import aws_sdk_savingsplans.types.savings_plan_service_code_list
    import aws_sdk_savingsplans.types.savings_plan_state_list
    import aws_sdk_savingsplans.types.savings_plan_type_list
    import aws_sdk_savingsplans.types.savings_plan_usage_type_list
    import aws_sdk_savingsplans.types.tag_key_list
    import aws_sdk_savingsplans.types.tag_map
    import aws_sdk_savingsplans.types.tag_resource_request
    import aws_sdk_savingsplans.types.tag_resource_response
    import aws_sdk_savingsplans.types.untag_resource_request
    import aws_sdk_savingsplans.types.untag_resource_response
    import aws_sdk_savingsplans.types.uui_ds


class AsyncsavingsplansClientConfig(TypedDict, total=False):
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


class AsyncsavingsplansClient:
    """A client for the ``savingsplans`` service.

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
        self.config = AsyncsavingsplansClientConfig(
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
        self, config_overrides: Optional[AsyncsavingsplansClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncsavingsplansClientConfig = config_overrides or {}
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

    async def create_savings_plan(
        self,
        savings_plan_offering_id: "aws_sdk_savingsplans.types.savings_plan_offering_id.SavingsPlanOfferingId",
        commitment: "aws_sdk_savingsplans.types.amount.Amount",
        *,
        config_overrides: Optional[AsyncsavingsplansClientConfig] = None,
        upfront_payment_amount: Optional[
            "aws_sdk_savingsplans.types.amount.Amount"
        ] = None,
        purchase_time: Optional["aws_sdk_savingsplans.types.date_time.DateTime"] = None,
        client_token: Optional[
            "aws_sdk_savingsplans.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_savingsplans.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_savingsplans.types.create_savings_plan_response.CreateSavingsPlanResponse":
        """<p>Creates a Savings Plan.</p>

        Args:
            savings_plan_offering_id: <p>The ID of the offering.</p>
            commitment: <p>The hourly commitment, in the same currency of the <code>savingsPlanOfferingId</code>. This is a value between 0.001 and 1 million. You cannot specify more than five digits after the decimal point.</p>
            upfront_payment_amount: <p>The up-front payment amount. This is a whole number between 50 and 99 percent of the total value of the Savings Plan. This parameter is only supported if the payment option is <code>Partial Upfront</code>.</p>
            purchase_time: <p>The purchase time of the Savings Plan in UTC format (YYYY-MM-DDTHH:MM:SSZ).</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>One or more tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_savingsplans.types.create_savings_plan_request.CreateSavingsPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_savingsplans.types.create_savings_plan_response.CreateSavingsPlanResponse"
        ]:
            import aws_sdk_savingsplans._operations.aws_savings_plan.create_savings_plan

            (
                output,
                http_response,
            ) = await aws_sdk_savingsplans._operations.aws_savings_plan.create_savings_plan.async_create_savings_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_savingsplans.types.create_savings_plan_request.CreateSavingsPlanRequest = {}  # type: ignore[typeddict-item]
        input["savings_plan_offering_id"] = savings_plan_offering_id
        input["commitment"] = commitment
        if upfront_payment_amount is not None:
            input["upfront_payment_amount"] = upfront_payment_amount
        if purchase_time is not None:
            input["purchase_time"] = purchase_time
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_queued_savings_plan(
        self,
        savings_plan_id: "aws_sdk_savingsplans.types.savings_plan_id.SavingsPlanId",
        *,
        config_overrides: Optional[AsyncsavingsplansClientConfig] = None,
    ) -> "aws_sdk_savingsplans.types.delete_queued_savings_plan_response.DeleteQueuedSavingsPlanResponse":
        """<p>Deletes the queued purchase for the specified Savings Plan.</p>

        Args:
            savings_plan_id: <p>The ID of the Savings Plan.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_savingsplans.types.delete_queued_savings_plan_request.DeleteQueuedSavingsPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_savingsplans.types.delete_queued_savings_plan_response.DeleteQueuedSavingsPlanResponse"
        ]:
            import aws_sdk_savingsplans._operations.aws_savings_plan.delete_queued_savings_plan

            (
                output,
                http_response,
            ) = await aws_sdk_savingsplans._operations.aws_savings_plan.delete_queued_savings_plan.async_delete_queued_savings_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_savingsplans.types.delete_queued_savings_plan_request.DeleteQueuedSavingsPlanRequest = {}  # type: ignore[typeddict-item]
        input["savings_plan_id"] = savings_plan_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_savings_plan_rates(
        self,
        savings_plan_id: "aws_sdk_savingsplans.types.savings_plan_id.SavingsPlanId",
        *,
        config_overrides: Optional[AsyncsavingsplansClientConfig] = None,
        filters: Optional[
            "aws_sdk_savingsplans.types.savings_plan_rate_filter_list.SavingsPlanRateFilterList"
        ] = None,
        next_token: Optional[
            "aws_sdk_savingsplans.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_savingsplans.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_savingsplans.types.describe_savings_plan_rates_response.DescribeSavingsPlanRatesResponse":
        """<p>Describes the rates for a specific, existing Savings Plan.</p>

        Args:
            savings_plan_id: <p>The ID of the Savings Plan.</p>
            filters: <p>The filters.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_savingsplans.types.describe_savings_plan_rates_request.DescribeSavingsPlanRatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_savingsplans.types.describe_savings_plan_rates_response.DescribeSavingsPlanRatesResponse"
        ]:
            import aws_sdk_savingsplans._operations.aws_savings_plan.describe_savings_plan_rates

            (
                output,
                http_response,
            ) = await aws_sdk_savingsplans._operations.aws_savings_plan.describe_savings_plan_rates.async_describe_savings_plan_rates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_savingsplans.types.describe_savings_plan_rates_request.DescribeSavingsPlanRatesRequest = {}  # type: ignore[typeddict-item]
        input["savings_plan_id"] = savings_plan_id
        if filters is not None:
            input["filters"] = filters
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

    async def describe_savings_plans(
        self,
        *,
        config_overrides: Optional[AsyncsavingsplansClientConfig] = None,
        savings_plan_arns: Optional[
            "aws_sdk_savingsplans.types.savings_plan_arn_list.SavingsPlanArnList"
        ] = None,
        savings_plan_ids: Optional[
            "aws_sdk_savingsplans.types.savings_plan_id_list.SavingsPlanIdList"
        ] = None,
        next_token: Optional[
            "aws_sdk_savingsplans.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_savingsplans.types.max_results.MaxResults"
        ] = None,
        states: Optional[
            "aws_sdk_savingsplans.types.savings_plan_state_list.SavingsPlanStateList"
        ] = None,
        filters: Optional[
            "aws_sdk_savingsplans.types.savings_plan_filter_list.SavingsPlanFilterList"
        ] = None,
    ) -> "aws_sdk_savingsplans.types.describe_savings_plans_response.DescribeSavingsPlansResponse":
        """<p>Describes the specified Savings Plans.</p>

        Args:
            savings_plan_arns: <p>The Amazon Resource Names (ARN) of the Savings Plans.</p>
            savings_plan_ids: <p>The IDs of the Savings Plans.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>
            states: <p>The current states of the Savings Plans.</p>
            filters: <p>The filters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_savingsplans.types.describe_savings_plans_request.DescribeSavingsPlansRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_savingsplans.types.describe_savings_plans_response.DescribeSavingsPlansResponse"
        ]:
            import aws_sdk_savingsplans._operations.aws_savings_plan.describe_savings_plans

            (
                output,
                http_response,
            ) = await aws_sdk_savingsplans._operations.aws_savings_plan.describe_savings_plans.async_describe_savings_plans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_savingsplans.types.describe_savings_plans_request.DescribeSavingsPlansRequest = {}  # type: ignore[typeddict-item]
        if savings_plan_arns is not None:
            input["savings_plan_arns"] = savings_plan_arns
        if savings_plan_ids is not None:
            input["savings_plan_ids"] = savings_plan_ids
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if states is not None:
            input["states"] = states
        if filters is not None:
            input["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_savings_plans_offering_rates(
        self,
        *,
        config_overrides: Optional[AsyncsavingsplansClientConfig] = None,
        savings_plan_offering_ids: Optional[
            "aws_sdk_savingsplans.types.uui_ds.UUIDs"
        ] = None,
        savings_plan_payment_options: Optional[
            "aws_sdk_savingsplans.types.savings_plan_payment_option_list.SavingsPlanPaymentOptionList"
        ] = None,
        savings_plan_types: Optional[
            "aws_sdk_savingsplans.types.savings_plan_type_list.SavingsPlanTypeList"
        ] = None,
        products: Optional[
            "aws_sdk_savingsplans.types.savings_plan_product_type_list.SavingsPlanProductTypeList"
        ] = None,
        service_codes: Optional[
            "aws_sdk_savingsplans.types.savings_plan_rate_service_code_list.SavingsPlanRateServiceCodeList"
        ] = None,
        usage_types: Optional[
            "aws_sdk_savingsplans.types.savings_plan_rate_usage_type_list.SavingsPlanRateUsageTypeList"
        ] = None,
        operations: Optional[
            "aws_sdk_savingsplans.types.savings_plan_rate_operation_list.SavingsPlanRateOperationList"
        ] = None,
        filters: Optional[
            "aws_sdk_savingsplans.types.savings_plan_offering_rate_filters_list.SavingsPlanOfferingRateFiltersList"
        ] = None,
        next_token: Optional[
            "aws_sdk_savingsplans.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_savingsplans.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_savingsplans.types.describe_savings_plans_offering_rates_response.DescribeSavingsPlansOfferingRatesResponse":
        """<p>Describes the offering rates for Savings Plans you might want to purchase.</p>

        Args:
            savings_plan_offering_ids: <p>The IDs of the offerings.</p>
            savings_plan_payment_options: <p>The payment options.</p>
            savings_plan_types: <p>The plan types.</p>
            products: <p>The Amazon Web Services products.</p>
            service_codes: <p>The services.</p>
            usage_types: <p>The usage details of the line item in the billing report.</p>
            operations: <p>The specific Amazon Web Services operation for the line item in the billing report.</p>
            filters: <p>The filters.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_savingsplans.types.describe_savings_plans_offering_rates_request.DescribeSavingsPlansOfferingRatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_savingsplans.types.describe_savings_plans_offering_rates_response.DescribeSavingsPlansOfferingRatesResponse"
        ]:
            import aws_sdk_savingsplans._operations.aws_savings_plan.describe_savings_plans_offering_rates

            (
                output,
                http_response,
            ) = await aws_sdk_savingsplans._operations.aws_savings_plan.describe_savings_plans_offering_rates.async_describe_savings_plans_offering_rates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_savingsplans.types.describe_savings_plans_offering_rates_request.DescribeSavingsPlansOfferingRatesRequest = {}  # type: ignore[typeddict-item]
        if savings_plan_offering_ids is not None:
            input["savings_plan_offering_ids"] = savings_plan_offering_ids
        if savings_plan_payment_options is not None:
            input["savings_plan_payment_options"] = savings_plan_payment_options
        if savings_plan_types is not None:
            input["savings_plan_types"] = savings_plan_types
        if products is not None:
            input["products"] = products
        if service_codes is not None:
            input["service_codes"] = service_codes
        if usage_types is not None:
            input["usage_types"] = usage_types
        if operations is not None:
            input["operations"] = operations
        if filters is not None:
            input["filters"] = filters
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

    async def describe_savings_plans_offerings(
        self,
        *,
        config_overrides: Optional[AsyncsavingsplansClientConfig] = None,
        offering_ids: Optional["aws_sdk_savingsplans.types.uui_ds.UUIDs"] = None,
        payment_options: Optional[
            "aws_sdk_savingsplans.types.savings_plan_payment_option_list.SavingsPlanPaymentOptionList"
        ] = None,
        product_type: Optional[
            "aws_sdk_savingsplans.types.savings_plan_product_type.SavingsPlanProductType"
        ] = None,
        plan_types: Optional[
            "aws_sdk_savingsplans.types.savings_plan_type_list.SavingsPlanTypeList"
        ] = None,
        durations: Optional[
            "aws_sdk_savingsplans.types.durations_list.DurationsList"
        ] = None,
        currencies: Optional[
            "aws_sdk_savingsplans.types.currency_list.CurrencyList"
        ] = None,
        descriptions: Optional[
            "aws_sdk_savingsplans.types.savings_plan_descriptions_list.SavingsPlanDescriptionsList"
        ] = None,
        service_codes: Optional[
            "aws_sdk_savingsplans.types.savings_plan_service_code_list.SavingsPlanServiceCodeList"
        ] = None,
        usage_types: Optional[
            "aws_sdk_savingsplans.types.savings_plan_usage_type_list.SavingsPlanUsageTypeList"
        ] = None,
        operations: Optional[
            "aws_sdk_savingsplans.types.savings_plan_operation_list.SavingsPlanOperationList"
        ] = None,
        filters: Optional[
            "aws_sdk_savingsplans.types.savings_plan_offering_filters_list.SavingsPlanOfferingFiltersList"
        ] = None,
        next_token: Optional[
            "aws_sdk_savingsplans.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_savingsplans.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_savingsplans.types.describe_savings_plans_offerings_response.DescribeSavingsPlansOfferingsResponse":
        """<p>Describes the offerings for the specified Savings Plans.</p>

        Args:
            offering_ids: <p>The IDs of the offerings.</p>
            payment_options: <p>The payment options.</p>
            product_type: <p>The product type.</p>
            plan_types: <p>The plan types.</p>
            durations: <p>The duration, in seconds.</p>
            currencies: <p>The currencies.</p>
            descriptions: <p>The descriptions.</p>
            service_codes: <p>The services.</p>
            usage_types: <p>The usage details of the line item in the billing report.</p>
            operations: <p>The specific Amazon Web Services operation for the line item in the billing report.</p>
            filters: <p>The filters.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_savingsplans.types.describe_savings_plans_offerings_request.DescribeSavingsPlansOfferingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_savingsplans.types.describe_savings_plans_offerings_response.DescribeSavingsPlansOfferingsResponse"
        ]:
            import aws_sdk_savingsplans._operations.aws_savings_plan.describe_savings_plans_offerings

            (
                output,
                http_response,
            ) = await aws_sdk_savingsplans._operations.aws_savings_plan.describe_savings_plans_offerings.async_describe_savings_plans_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_savingsplans.types.describe_savings_plans_offerings_request.DescribeSavingsPlansOfferingsRequest = {}  # type: ignore[typeddict-item]
        if offering_ids is not None:
            input["offering_ids"] = offering_ids
        if payment_options is not None:
            input["payment_options"] = payment_options
        if product_type is not None:
            input["product_type"] = product_type
        if plan_types is not None:
            input["plan_types"] = plan_types
        if durations is not None:
            input["durations"] = durations
        if currencies is not None:
            input["currencies"] = currencies
        if descriptions is not None:
            input["descriptions"] = descriptions
        if service_codes is not None:
            input["service_codes"] = service_codes
        if usage_types is not None:
            input["usage_types"] = usage_types
        if operations is not None:
            input["operations"] = operations
        if filters is not None:
            input["filters"] = filters
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_savingsplans.types.savings_plan_arn.SavingsPlanArn",
        *,
        config_overrides: Optional[AsyncsavingsplansClientConfig] = None,
    ) -> "aws_sdk_savingsplans.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_savingsplans.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_savingsplans.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_savingsplans._operations.aws_savings_plan.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_savingsplans._operations.aws_savings_plan.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_savingsplans.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def return_savings_plan(
        self,
        savings_plan_id: "aws_sdk_savingsplans.types.savings_plan_id.SavingsPlanId",
        *,
        config_overrides: Optional[AsyncsavingsplansClientConfig] = None,
        client_token: Optional[
            "aws_sdk_savingsplans.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_savingsplans.types.return_savings_plan_response.ReturnSavingsPlanResponse":
        """<p>Returns the specified Savings Plan.</p>

        Args:
            savings_plan_id: <p>The ID of the Savings Plan.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_savingsplans.types.return_savings_plan_request.ReturnSavingsPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_savingsplans.types.return_savings_plan_response.ReturnSavingsPlanResponse"
        ]:
            import aws_sdk_savingsplans._operations.aws_savings_plan.return_savings_plan

            (
                output,
                http_response,
            ) = await aws_sdk_savingsplans._operations.aws_savings_plan.return_savings_plan.async_return_savings_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_savingsplans.types.return_savings_plan_request.ReturnSavingsPlanRequest = {}  # type: ignore[typeddict-item]
        input["savings_plan_id"] = savings_plan_id
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
        resource_arn: "aws_sdk_savingsplans.types.savings_plan_arn.SavingsPlanArn",
        tags: "aws_sdk_savingsplans.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncsavingsplansClientConfig] = None,
    ) -> "aws_sdk_savingsplans.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>One or more tags. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_savingsplans.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_savingsplans.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_savingsplans._operations.aws_savings_plan.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_savingsplans._operations.aws_savings_plan.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_savingsplans.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_savingsplans.types.savings_plan_arn.SavingsPlanArn",
        tag_keys: "aws_sdk_savingsplans.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncsavingsplansClientConfig] = None,
    ) -> "aws_sdk_savingsplans.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_savingsplans.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_savingsplans.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_savingsplans._operations.aws_savings_plan.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_savingsplans._operations.aws_savings_plan.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_savingsplans.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

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
