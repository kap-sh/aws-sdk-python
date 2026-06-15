"""Generated from Smithy shape ``com.amazonaws.billingconductor#AWSBillingConductor``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_billingconductor._auth._signers
import aws_sdk_billingconductor._auth._sigv4
from aws_sdk_billingconductor._auth._identity import Credentials
from aws_sdk_billingconductor._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_billingconductor._auth._zapros_handler import AuthMiddleware
from aws_sdk_billingconductor._pagination import resolve_path as _resolve_path
from aws_sdk_billingconductor._resources.aws_billing_conductor.billing_group import (
    AsyncBillingGroup,
)
from aws_sdk_billingconductor._resources.aws_billing_conductor.custom_line_item import (
    AsyncCustomLineItem,
)
from aws_sdk_billingconductor._resources.aws_billing_conductor.pricing_plan import (
    AsyncPricingPlan,
)
from aws_sdk_billingconductor._resources.aws_billing_conductor.pricing_rule import (
    AsyncPricingRule,
)
from aws_sdk_billingconductor._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_associations_list_element
    import aws_sdk_billingconductor.types.arn
    import aws_sdk_billingconductor.types.billing_group_arn
    import aws_sdk_billingconductor.types.billing_group_cost_report_element
    import aws_sdk_billingconductor.types.billing_group_cost_report_result_element
    import aws_sdk_billingconductor.types.billing_period
    import aws_sdk_billingconductor.types.billing_period_range
    import aws_sdk_billingconductor.types.get_billing_group_cost_report_input
    import aws_sdk_billingconductor.types.get_billing_group_cost_report_output
    import aws_sdk_billingconductor.types.group_by_attributes_list
    import aws_sdk_billingconductor.types.list_account_associations_filter
    import aws_sdk_billingconductor.types.list_account_associations_input
    import aws_sdk_billingconductor.types.list_account_associations_output
    import aws_sdk_billingconductor.types.list_billing_group_cost_reports_filter
    import aws_sdk_billingconductor.types.list_billing_group_cost_reports_input
    import aws_sdk_billingconductor.types.list_billing_group_cost_reports_output
    import aws_sdk_billingconductor.types.list_tags_for_resource_request
    import aws_sdk_billingconductor.types.list_tags_for_resource_response
    import aws_sdk_billingconductor.types.max_billing_group_cost_report_results
    import aws_sdk_billingconductor.types.max_billing_group_results
    import aws_sdk_billingconductor.types.tag_key_list
    import aws_sdk_billingconductor.types.tag_map
    import aws_sdk_billingconductor.types.tag_resource_request
    import aws_sdk_billingconductor.types.tag_resource_response
    import aws_sdk_billingconductor.types.token
    import aws_sdk_billingconductor.types.untag_resource_request
    import aws_sdk_billingconductor.types.untag_resource_response


class AsyncbillingconductorClientConfig(TypedDict, total=False):
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


class AsyncbillingconductorClient:
    """A client for the ``billingconductor`` service.

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
        self._config = AsyncbillingconductorClientConfig(
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

        # resources
        self.billing_group = AsyncBillingGroup(self)
        self.custom_line_item = AsyncCustomLineItem(self)
        self.pricing_plan = AsyncPricingPlan(self)
        self.pricing_rule = AsyncPricingRule(self)

    def operation_options(
        self, config_overrides: Optional[AsyncbillingconductorClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncbillingconductorClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def get_billing_group_cost_report(
        self,
        arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.billing_period_range.BillingPeriodRange"
        ] = None,
        group_by: Optional[
            "aws_sdk_billingconductor.types.group_by_attributes_list.GroupByAttributesList"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_billing_group_cost_report_results.MaxBillingGroupCostReportResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
    ) -> "aws_sdk_billingconductor.types.get_billing_group_cost_report_output.GetBillingGroupCostReportOutput":
        """<p>Retrieves the margin summary report, which includes the Amazon Web Services cost and charged amount (pro forma cost) by Amazon Web Services service for a specific billing group.</p>

        Args:
            arn: <p>The Amazon Resource Number (ARN) that uniquely identifies the billing group.</p>
            billing_period_range: <p>A time range for which the margin summary is effective. You can specify up to 12 months.</p>
            group_by: <p>A list of strings that specify the attributes that are used to break down costs in the margin summary reports for the billing group. For example, you can view your costs by the Amazon Web Services service name or the billing period.</p>
            max_results: <p>The maximum number of margin summary reports to retrieve.</p>
            next_token: <p>The pagination token used on subsequent calls to get reports.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.get_billing_group_cost_report_input.GetBillingGroupCostReportInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.get_billing_group_cost_report_output.GetBillingGroupCostReportOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.get_billing_group_cost_report

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.get_billing_group_cost_report.async_get_billing_group_cost_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.get_billing_group_cost_report_input.GetBillingGroupCostReportInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range
        if group_by is not None:
            input_["group_by"] = group_by
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

    async def iter_get_billing_group_cost_report(
        self,
        arn: "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period_range: Optional[
            "aws_sdk_billingconductor.types.billing_period_range.BillingPeriodRange"
        ] = None,
        group_by: Optional[
            "aws_sdk_billingconductor.types.group_by_attributes_list.GroupByAttributesList"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_billing_group_cost_report_results.MaxBillingGroupCostReportResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
    ) -> "AsyncIterator[aws_sdk_billingconductor.types.billing_group_cost_report_result_element.BillingGroupCostReportResultElement]":
        _token = next_token
        while True:
            _response = await self.get_billing_group_cost_report(
                arn,
                config_overrides=config_overrides,
                billing_period_range=billing_period_range,
                group_by=group_by,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("billing_group_cost_report_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_account_associations(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_account_associations_filter.ListAccountAssociationsFilter"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
    ) -> "aws_sdk_billingconductor.types.list_account_associations_output.ListAccountAssociationsOutput":
        """<p> This is a paginated call to list linked accounts that are linked to the payer account for the specified time period. If no information is provided, the current billing period is used. The response will optionally include the billing group that's associated with the linked account.</p>

        Args:
            billing_period: <p> The preferred billing period to get account associations. </p>
            filters: <p>The filter on the account ID of the linked account, or any of the following:</p> <p> <code>MONITORED</code>: linked accounts that are associated to billing groups.</p> <p> <code>UNMONITORED</code>: linked accounts that aren't associated to billing groups.</p> <p> <code>Billing Group Arn</code>: linked accounts that are associated to the provided billing group Arn. </p>
            next_token: <p> The pagination token that's used on subsequent calls to retrieve accounts. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.list_account_associations_input.ListAccountAssociationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.list_account_associations_output.ListAccountAssociationsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_account_associations

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.list_account_associations.async_list_account_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_account_associations_input.ListAccountAssociationsInput = {}  # type: ignore[typeddict-item]
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_account_associations(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_account_associations_filter.ListAccountAssociationsFilter"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
    ) -> "AsyncIterator[aws_sdk_billingconductor.types.account_associations_list_element.AccountAssociationsListElement]":
        _token = next_token
        while True:
            _response = await self.list_account_associations(
                config_overrides=config_overrides,
                billing_period=billing_period,
                filters=filters,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("linked_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_billing_group_cost_reports(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_billing_group_cost_reports_filter.ListBillingGroupCostReportsFilter"
        ] = None,
    ) -> "aws_sdk_billingconductor.types.list_billing_group_cost_reports_output.ListBillingGroupCostReportsOutput":
        """<p>A paginated call to retrieve a summary report of actual Amazon Web Services charges and the calculated Amazon Web Services charges based on the associated pricing plan of a billing group.</p>

        Args:
            billing_period: <p>The preferred billing period for your report. </p>
            max_results: <p>The maximum number of reports to retrieve. </p>
            next_token: <p>The pagination token that's used on subsequent calls to get reports. </p>
            filters: <p>A <code>ListBillingGroupCostReportsFilter</code> to specify billing groups to retrieve reports from. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.list_billing_group_cost_reports_input.ListBillingGroupCostReportsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.list_billing_group_cost_reports_output.ListBillingGroupCostReportsOutput"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_billing_group_cost_reports

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.list_billing_group_cost_reports.async_list_billing_group_cost_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_billing_group_cost_reports_input.ListBillingGroupCostReportsInput = {}  # type: ignore[typeddict-item]
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

    async def iter_list_billing_group_cost_reports(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "aws_sdk_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
        ] = None,
        next_token: Optional["aws_sdk_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "aws_sdk_billingconductor.types.list_billing_group_cost_reports_filter.ListBillingGroupCostReportsFilter"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_billingconductor.types.billing_group_cost_report_element.BillingGroupCostReportElement]":
        _token = next_token
        while True:
            _response = await self.list_billing_group_cost_reports(
                config_overrides=config_overrides,
                billing_period=billing_period,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("billing_group_cost_reports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_billingconductor.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> A list the tags for a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) that identifies the resource to list the tags. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_billingconductor.types.arn.Arn",
        tags: "aws_sdk_billingconductor.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.tag_resource_response.TagResourceResponse":
        """<p> Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource are not specified in the request parameters, they are not changed. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource to which to add tags. </p>
            tags: <p> The tags to add to the resource as a list of key-value pairs. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_billingconductor.types.arn.Arn",
        tag_keys: "aws_sdk_billingconductor.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "aws_sdk_billingconductor.types.untag_resource_response.UntagResourceResponse":
        """<p> Deletes specified tags from a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource to which to delete tags. </p>
            tag_keys: <p> The tags to delete from the resource as a list of key-value pairs. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_billingconductor.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_billingconductor.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_billingconductor._operations.aws_billing_conductor.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_billingconductor._operations.aws_billing_conductor.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_billingconductor.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
