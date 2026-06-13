"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#AWSMarketplaceDiscovery``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_marketplace_discovery._auth._signers
import aws_sdk_marketplace_discovery._auth._sigv4
from aws_sdk_marketplace_discovery._auth._identity import Credentials
from aws_sdk_marketplace_discovery._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_marketplace_discovery._auth._zapros_handler import AuthMiddleware
from aws_sdk_marketplace_discovery._pagination import resolve_path as _resolve_path
from aws_sdk_marketplace_discovery._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.facet_type_list
    import aws_sdk_marketplace_discovery.types.fulfillment_option
    import aws_sdk_marketplace_discovery.types.get_listing_input
    import aws_sdk_marketplace_discovery.types.get_listing_output
    import aws_sdk_marketplace_discovery.types.get_offer_input
    import aws_sdk_marketplace_discovery.types.get_offer_output
    import aws_sdk_marketplace_discovery.types.get_offer_set_input
    import aws_sdk_marketplace_discovery.types.get_offer_set_output
    import aws_sdk_marketplace_discovery.types.get_offer_terms_input
    import aws_sdk_marketplace_discovery.types.get_offer_terms_output
    import aws_sdk_marketplace_discovery.types.get_product_input
    import aws_sdk_marketplace_discovery.types.get_product_output
    import aws_sdk_marketplace_discovery.types.list_fulfillment_options_input
    import aws_sdk_marketplace_discovery.types.list_fulfillment_options_output
    import aws_sdk_marketplace_discovery.types.list_purchase_options_input
    import aws_sdk_marketplace_discovery.types.list_purchase_options_output
    import aws_sdk_marketplace_discovery.types.listing_facet_list
    import aws_sdk_marketplace_discovery.types.listing_id
    import aws_sdk_marketplace_discovery.types.listing_summary
    import aws_sdk_marketplace_discovery.types.max_results
    import aws_sdk_marketplace_discovery.types.next_token
    import aws_sdk_marketplace_discovery.types.offer_id
    import aws_sdk_marketplace_discovery.types.offer_set_id
    import aws_sdk_marketplace_discovery.types.offer_term
    import aws_sdk_marketplace_discovery.types.product_id
    import aws_sdk_marketplace_discovery.types.purchase_option_filter_list
    import aws_sdk_marketplace_discovery.types.purchase_option_summary
    import aws_sdk_marketplace_discovery.types.search_facet_type
    import aws_sdk_marketplace_discovery.types.search_facets_input
    import aws_sdk_marketplace_discovery.types.search_facets_output
    import aws_sdk_marketplace_discovery.types.search_filter_list
    import aws_sdk_marketplace_discovery.types.search_listings_input
    import aws_sdk_marketplace_discovery.types.search_listings_output
    import aws_sdk_marketplace_discovery.types.search_listings_sort_by
    import aws_sdk_marketplace_discovery.types.search_listings_sort_order
    import aws_sdk_marketplace_discovery.types.search_text


class MarketplaceDiscoveryClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class MarketplaceDiscoveryClient:
    """A client for the ``MarketplaceDiscovery`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = MarketplaceDiscoveryClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MarketplaceDiscoveryClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def get_listing(
        self,
        listing_id: "aws_sdk_marketplace_discovery.types.listing_id.ListingId",
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
    ) -> "aws_sdk_marketplace_discovery.types.get_listing_output.GetListingOutput":
        """<p>Provides details about a listing, such as descriptions, badges, categories, pricing model summaries, reviews, and associated products and offers.</p>

        Args:
            listing_id: <p>The unique identifier of the listing to retrieve.</p>

        Examples:
            GetListing for SaaS listing

            >>> client.get_listing(listing_id='prodview-sampleSaasId')
            GetListing for AMI listing with video

            >>> client.get_listing(listing_id='prodview-sampleAmiId')
            GetListing for multi-product listing

            >>> client.get_listing(listing_id='prodview-sampleMultiProductId')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_discovery.types.get_listing_input.GetListingInput]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_discovery.types.get_listing_output.GetListingOutput"
        ]:
            import aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.get_listing

            output, http_response = (
                aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.get_listing.get_listing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_discovery.types.get_listing_input.GetListingInput = {}  # type: ignore[typeddict-item]
        input["listing_id"] = listing_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_offer(
        self,
        offer_id: "aws_sdk_marketplace_discovery.types.offer_id.OfferId",
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
    ) -> "aws_sdk_marketplace_discovery.types.get_offer_output.GetOfferOutput":
        """<p>Provides details about an offer, such as the pricing model, seller of record, availability dates, badges, and associated products.</p>

        Args:
            offer_id: <p>The unique identifier of the offer to retrieve.</p>

        Examples:
            Invoke GetOffer for Contract Pricing offer

            >>> client.get_offer(offer_id='offer-sampleContractId')
            Invoke GetOffer for Usage Pricing offer

            >>> client.get_offer(offer_id='offer-sampleUsageId')
            Invoke GetOffer for BYOL Pricing offer

            >>> client.get_offer(offer_id='offer-sampleByolId')
            Invoke GetOffer for FREE Pricing offer

            >>> client.get_offer(offer_id='offer-sampleFreeId')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_discovery.types.get_offer_input.GetOfferInput]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_discovery.types.get_offer_output.GetOfferOutput"
        ]:
            import aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.get_offer

            output, http_response = (
                aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.get_offer.get_offer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_discovery.types.get_offer_input.GetOfferInput = {}  # type: ignore[typeddict-item]
        input["offer_id"] = offer_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_offer_set(
        self,
        offer_set_id: "aws_sdk_marketplace_discovery.types.offer_set_id.OfferSetId",
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
    ) -> "aws_sdk_marketplace_discovery.types.get_offer_set_output.GetOfferSetOutput":
        """<p>Provides details about an offer set, which is a bundle of offers across multiple products. Includes the seller, availability dates, buyer notes, and associated product-offer pairs.</p>

        Args:
            offer_set_id: <p>The unique identifier of the offer set to retrieve.</p>

        Examples:
            Get offer set with multiple products

            >>> client.get_offer_set(offer_set_id='offerset-sampleId')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_discovery.types.get_offer_set_input.GetOfferSetInput]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_discovery.types.get_offer_set_output.GetOfferSetOutput"
        ]:
            import aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.get_offer_set

            output, http_response = (
                aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.get_offer_set.get_offer_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_discovery.types.get_offer_set_input.GetOfferSetInput = {}  # type: ignore[typeddict-item]
        input["offer_set_id"] = offer_set_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_offer_terms(
        self,
        offer_id: "aws_sdk_marketplace_discovery.types.offer_id.OfferId",
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> (
        "aws_sdk_marketplace_discovery.types.get_offer_terms_output.GetOfferTermsOutput"
    ):
        """<p>Returns the terms attached to an offer, such as pricing terms (usage-based, contract, BYOL, free trial), legal terms, payment schedules, validity terms, support terms, and renewal terms.</p>

        Args:
            offer_id: <p>The unique identifier of the offer whose terms to retrieve.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>

        Examples:
            GetOfferTerms for Usage-based ML Model offer

            >>> client.get_offer_terms(offer_id='offer-sampleUsageBasedId')
            GetOfferTerms for BYOL offer

            >>> client.get_offer_terms(offer_id='offer-sampleByolId')
            GetOfferTerms for configurable upfront pricing

            >>> client.get_offer_terms(offer_id='offer-sampleConfigUpfrontId')
            GetOfferTerms for free trial offer

            >>> client.get_offer_terms(offer_id='offer-sampleFreeTrialId')
            GetOfferTerms for recurring payment

            >>> client.get_offer_terms(offer_id='offer-sampleRecurringId')
            GetOfferTerms for variable payment

            >>> client.get_offer_terms(offer_id='offer-sampleVariableId')
            GetOfferTerms for renewal term

            >>> client.get_offer_terms(offer_id='offer-sampleRenewalId')
            GetOfferTerms for support term

            >>> client.get_offer_terms(offer_id='offer-sampleSupportId')
            GetOfferTerms for validity term with dates

            >>> client.get_offer_terms(offer_id='offer-sampleValidityId')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_discovery.types.get_offer_terms_input.GetOfferTermsInput]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_discovery.types.get_offer_terms_output.GetOfferTermsOutput"
        ]:
            import aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.get_offer_terms

            output, http_response = (
                aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.get_offer_terms.get_offer_terms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_discovery.types.get_offer_terms_input.GetOfferTermsInput = {}  # type: ignore[typeddict-item]
        input["offer_id"] = offer_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_offer_terms(
        self,
        offer_id: "aws_sdk_marketplace_discovery.types.offer_id.OfferId",
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_marketplace_discovery.types.offer_term.OfferTerm]":
        _token = next_token
        while True:
            _response = self.get_offer_terms(
                offer_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("offer_terms",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_product(
        self,
        product_id: "aws_sdk_marketplace_discovery.types.product_id.ProductId",
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
    ) -> "aws_sdk_marketplace_discovery.types.get_product_output.GetProductOutput":
        """<p>Provides details about a product, such as descriptions, highlights, categories, fulfillment option summaries, promotional media, and seller engagement options.</p>

        Args:
            product_id: <p>The unique identifier of the product to retrieve.</p>

        Examples:
            GetProduct for SaaS product with DEPLOYED status

            >>> client.get_product(product_id='prod-sampleSaasId')
            GetProduct for AMI product with NOT_DEPLOYED status

            >>> client.get_product(product_id='prod-sampleAmiId')
            GetProduct for professional services with NOT_APPLICABLE status

            >>> client.get_product(product_id='prod-sampleProServId')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_discovery.types.get_product_input.GetProductInput]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_discovery.types.get_product_output.GetProductOutput"
        ]:
            import aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.get_product

            output, http_response = (
                aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.get_product.get_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_discovery.types.get_product_input.GetProductInput = {}  # type: ignore[typeddict-item]
        input["product_id"] = product_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_fulfillment_options(
        self,
        product_id: "aws_sdk_marketplace_discovery.types.product_id.ProductId",
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_marketplace_discovery.types.list_fulfillment_options_output.ListFulfillmentOptionsOutput":
        """<p>Returns the fulfillment options available for a product, including deployment details such as version information, operating systems, usage instructions, and release notes.</p>

        Args:
            product_id: <p>The unique identifier of the product for which to list fulfillment options.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>

        Examples:
            List AMI Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleAmiId')
            List API Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleApiId')
            List CloudFormation Template Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleCftId')
            List Container Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleContainerId')
            List Helm Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleHelmId')
            List EKS Add-On Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleEksId')
            List EC2 Image Builder Component Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleImageBuilderId')
            List Data Exchange Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleDataExchangeId')
            List Professional Services Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleProServId')
            List SaaS Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleSaasId')
            List SageMaker Algorithm Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleSmAlgoId')
            List SageMaker Model Fulfillment Options

            >>> client.list_fulfillment_options(product_id='prod-sampleSmModelId')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_discovery.types.list_fulfillment_options_input.ListFulfillmentOptionsInput]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_discovery.types.list_fulfillment_options_output.ListFulfillmentOptionsOutput"
        ]:
            import aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.list_fulfillment_options

            output, http_response = (
                aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.list_fulfillment_options.list_fulfillment_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_discovery.types.list_fulfillment_options_input.ListFulfillmentOptionsInput = {}  # type: ignore[typeddict-item]
        input["product_id"] = product_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_fulfillment_options(
        self,
        product_id: "aws_sdk_marketplace_discovery.types.product_id.ProductId",
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_marketplace_discovery.types.fulfillment_option.FulfillmentOption]":
        _token = next_token
        while True:
            _response = self.list_fulfillment_options(
                product_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fulfillment_options",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_purchase_options(
        self,
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
        filters: Optional[
            "aws_sdk_marketplace_discovery.types.purchase_option_filter_list.PurchaseOptionFilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_marketplace_discovery.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_marketplace_discovery.types.list_purchase_options_output.ListPurchaseOptionsOutput":
        """<p>Returns the purchase options (offers and offer sets) available to the buyer. You can filter results by product, seller, purchase option type, visibility scope, and availability status.</p> <note> <p>You must include at least one of the following filters in the request: a <code>PRODUCT_ID</code> filter to specify the product for which to retrieve purchase options, or a <code>VISIBILITY_SCOPE</code> filter to retrieve purchase options by visibility.</p> </note>

        Args:
            filters: <p>Filters to narrow the results. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>

        Examples:
            Filter by Product ID

            >>> client.list_purchase_options(filters=[{'filterType': 'PRODUCT_ID', 'filterValues': ['prod-sampleOfferId']}])
            Filter by Seller with Private Offerset

            >>> client.list_purchase_options(filters=[{'filterType': 'SELLER_OF_RECORD_PROFILE_ID', 'filterValues': ['seller-sampleResellerId']}, {'filterType': 'PURCHASE_OPTION_TYPE', 'filterValues': ['OFFERSET']}, {'filterType': 'VISIBILITY_SCOPE', 'filterValues': ['PRIVATE']}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_discovery.types.list_purchase_options_input.ListPurchaseOptionsInput]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_discovery.types.list_purchase_options_output.ListPurchaseOptionsOutput"
        ]:
            import aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.list_purchase_options

            output, http_response = (
                aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.list_purchase_options.list_purchase_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_discovery.types.list_purchase_options_input.ListPurchaseOptionsInput = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_purchase_options(
        self,
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
        filters: Optional[
            "aws_sdk_marketplace_discovery.types.purchase_option_filter_list.PurchaseOptionFilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_marketplace_discovery.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_marketplace_discovery.types.purchase_option_summary.PurchaseOptionSummary]":
        _token = next_token
        while True:
            _response = self.list_purchase_options(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("purchase_options",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_facets(
        self,
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
        search_text: Optional[
            "aws_sdk_marketplace_discovery.types.search_text.SearchText"
        ] = None,
        filters: Optional[
            "aws_sdk_marketplace_discovery.types.search_filter_list.SearchFilterList"
        ] = None,
        facet_types: Optional[
            "aws_sdk_marketplace_discovery.types.facet_type_list.FacetTypeList"
        ] = None,
        next_token: Optional[
            "aws_sdk_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_marketplace_discovery.types.search_facets_output.SearchFacetsOutput":
        """<p>Returns available facet values for filtering listings, such as categories, pricing models, fulfillment option types, publishers, and customer ratings. Each facet value includes a count of matching listings.</p>

        Args:
            search_text: <p>The search query text to filter listings before retrieving facets.</p>
            filters: <p>Filters to apply before retrieving facets. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.</p>
            facet_types: <p>A list of specific facet types to retrieve. If empty or null, all available facets are returned.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>

        Examples:
            Get facets for machine learning category
            Retrieve available facet values for listings in the machine learning category

            >>> client.search_facets(search_text='analytics', filters=[{'filterType': 'CATEGORY', 'filterValues': ['machine-learning']}], facet_types=['FULFILLMENT_OPTION_TYPE', 'PRICING_MODEL'])
            Get facets with term and rating range filters
            Retrieve facets for security listings with ratings between 3.0 and 5.0 stars

            >>> client.search_facets(filters=[{'filterType': 'CATEGORY', 'filterValues': ['security']}, {'filterType': 'MIN_AVERAGE_CUSTOMER_RATING', 'filterValues': ['3.0']}, {'filterType': 'MAX_AVERAGE_CUSTOMER_RATING', 'filterValues': ['5.0']}], facet_types=['PRICING_MODEL', 'AVERAGE_CUSTOMER_RATING'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_discovery.types.search_facets_input.SearchFacetsInput]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_discovery.types.search_facets_output.SearchFacetsOutput"
        ]:
            import aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.search_facets

            output, http_response = (
                aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.search_facets.search_facets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_discovery.types.search_facets_input.SearchFacetsInput = {}  # type: ignore[typeddict-item]
        if search_text is not None:
            input["search_text"] = search_text
        if filters is not None:
            input["filters"] = filters
        if facet_types is not None:
            input["facet_types"] = facet_types
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_search_facets(
        self,
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
        search_text: Optional[
            "aws_sdk_marketplace_discovery.types.search_text.SearchText"
        ] = None,
        filters: Optional[
            "aws_sdk_marketplace_discovery.types.search_filter_list.SearchFilterList"
        ] = None,
        facet_types: Optional[
            "aws_sdk_marketplace_discovery.types.facet_type_list.FacetTypeList"
        ] = None,
        next_token: Optional[
            "aws_sdk_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[tuple[aws_sdk_marketplace_discovery.types.search_facet_type.SearchFacetType, aws_sdk_marketplace_discovery.types.listing_facet_list.ListingFacetList]]":
        _token = next_token
        while True:
            _response = self.search_facets(
                config_overrides=config_overrides,
                search_text=search_text,
                filters=filters,
                facet_types=facet_types,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("listing_facets",))
            for _k, _v in (_page or {}).items():
                yield (_k, _v)
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_listings(
        self,
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
        search_text: Optional[
            "aws_sdk_marketplace_discovery.types.search_text.SearchText"
        ] = None,
        filters: Optional[
            "aws_sdk_marketplace_discovery.types.search_filter_list.SearchFilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_marketplace_discovery.types.max_results.MaxResults"
        ] = None,
        sort_by: Optional[
            "aws_sdk_marketplace_discovery.types.search_listings_sort_by.SearchListingsSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_marketplace_discovery.types.search_listings_sort_order.SearchListingsSortOrder"
        ] = None,
        next_token: Optional[
            "aws_sdk_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_marketplace_discovery.types.search_listings_output.SearchListingsOutput":
        """<p>Returns a list of product listings based on search criteria and filters. You can search by keyword, filter by category, pricing model, fulfillment type, and other attributes, and sort results by relevance or customer rating.</p>

        Args:
            search_text: <p>The search query text to find relevant listings.</p>
            filters: <p>Filters to narrow search results. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>
            sort_by: <p>The field to sort results by. Valid values are <code>RELEVANCE</code> and <code>AVERAGE_CUSTOMER_RATING</code>.</p>
            sort_order: <p>The sort direction. Valid values are <code>DESCENDING</code> and <code>ASCENDING</code>.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>

        Examples:
            Search for machine learning listings
            Search for SaaS listings in the machine learning category with sorting by relevance

            >>> client.search_listings(search_text='computer vision', filters=[{'filterType': 'CATEGORY', 'filterValues': ['machine-learning']}, {'filterType': 'FULFILLMENT_OPTION_TYPE', 'filterValues': ['SAAS']}], max_results=25, sort_by='RELEVANCE', sort_order='DESCENDING')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_discovery.types.search_listings_input.SearchListingsInput]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_discovery.types.search_listings_output.SearchListingsOutput"
        ]:
            import aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.search_listings

            output, http_response = (
                aws_sdk_marketplace_discovery._operations.aws_marketplace_discovery.search_listings.search_listings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_discovery.types.search_listings_input.SearchListingsInput = {}  # type: ignore[typeddict-item]
        if search_text is not None:
            input["search_text"] = search_text
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if sort_by is not None:
            input["sort_by"] = sort_by
        if sort_order is not None:
            input["sort_order"] = sort_order
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_search_listings(
        self,
        *,
        config_overrides: Optional[MarketplaceDiscoveryClientConfig] = None,
        search_text: Optional[
            "aws_sdk_marketplace_discovery.types.search_text.SearchText"
        ] = None,
        filters: Optional[
            "aws_sdk_marketplace_discovery.types.search_filter_list.SearchFilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_marketplace_discovery.types.max_results.MaxResults"
        ] = None,
        sort_by: Optional[
            "aws_sdk_marketplace_discovery.types.search_listings_sort_by.SearchListingsSortBy"
        ] = None,
        sort_order: Optional[
            "aws_sdk_marketplace_discovery.types.search_listings_sort_order.SearchListingsSortOrder"
        ] = None,
        next_token: Optional[
            "aws_sdk_marketplace_discovery.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_marketplace_discovery.types.listing_summary.ListingSummary]":
        _token = next_token
        while True:
            _response = self.search_listings(
                config_overrides=config_overrides,
                search_text=search_text,
                filters=filters,
                max_results=max_results,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("listing_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
