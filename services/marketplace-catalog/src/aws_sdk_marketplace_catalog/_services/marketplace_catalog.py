"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AWSMPSeymour``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_marketplace_catalog._auth._signers
import aws_sdk_marketplace_catalog._auth._sigv4
from aws_sdk_marketplace_catalog._auth._identity import Credentials
from aws_sdk_marketplace_catalog._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_marketplace_catalog._auth._zapros_handler import AuthMiddleware
from aws_sdk_marketplace_catalog._pagination import resolve_path as _resolve_path
from aws_sdk_marketplace_catalog._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.batch_describe_entities_request
    import aws_sdk_marketplace_catalog.types.batch_describe_entities_response
    import aws_sdk_marketplace_catalog.types.cancel_change_set_request
    import aws_sdk_marketplace_catalog.types.cancel_change_set_response
    import aws_sdk_marketplace_catalog.types.catalog
    import aws_sdk_marketplace_catalog.types.change_set_name
    import aws_sdk_marketplace_catalog.types.change_set_summary_list_item
    import aws_sdk_marketplace_catalog.types.client_request_token
    import aws_sdk_marketplace_catalog.types.delete_resource_policy_request
    import aws_sdk_marketplace_catalog.types.delete_resource_policy_response
    import aws_sdk_marketplace_catalog.types.describe_change_set_request
    import aws_sdk_marketplace_catalog.types.describe_change_set_response
    import aws_sdk_marketplace_catalog.types.describe_entity_request
    import aws_sdk_marketplace_catalog.types.describe_entity_response
    import aws_sdk_marketplace_catalog.types.entity_request_list
    import aws_sdk_marketplace_catalog.types.entity_summary
    import aws_sdk_marketplace_catalog.types.entity_type
    import aws_sdk_marketplace_catalog.types.entity_type_filters
    import aws_sdk_marketplace_catalog.types.entity_type_sort
    import aws_sdk_marketplace_catalog.types.filter_list
    import aws_sdk_marketplace_catalog.types.get_resource_policy_request
    import aws_sdk_marketplace_catalog.types.get_resource_policy_response
    import aws_sdk_marketplace_catalog.types.intent
    import aws_sdk_marketplace_catalog.types.list_change_sets_max_result_integer
    import aws_sdk_marketplace_catalog.types.list_change_sets_request
    import aws_sdk_marketplace_catalog.types.list_change_sets_response
    import aws_sdk_marketplace_catalog.types.list_entities_max_result_integer
    import aws_sdk_marketplace_catalog.types.list_entities_request
    import aws_sdk_marketplace_catalog.types.list_entities_response
    import aws_sdk_marketplace_catalog.types.list_tags_for_resource_request
    import aws_sdk_marketplace_catalog.types.list_tags_for_resource_response
    import aws_sdk_marketplace_catalog.types.next_token
    import aws_sdk_marketplace_catalog.types.ownership_type
    import aws_sdk_marketplace_catalog.types.put_resource_policy_request
    import aws_sdk_marketplace_catalog.types.put_resource_policy_response
    import aws_sdk_marketplace_catalog.types.requested_change_list
    import aws_sdk_marketplace_catalog.types.resource_arn
    import aws_sdk_marketplace_catalog.types.resource_id
    import aws_sdk_marketplace_catalog.types.resource_policy_json
    import aws_sdk_marketplace_catalog.types.sort
    import aws_sdk_marketplace_catalog.types.start_change_set_request
    import aws_sdk_marketplace_catalog.types.start_change_set_response
    import aws_sdk_marketplace_catalog.types.tag_key_list
    import aws_sdk_marketplace_catalog.types.tag_list
    import aws_sdk_marketplace_catalog.types.tag_resource_request
    import aws_sdk_marketplace_catalog.types.tag_resource_response
    import aws_sdk_marketplace_catalog.types.untag_resource_request
    import aws_sdk_marketplace_catalog.types.untag_resource_response


class MarketplaceCatalogClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_dual_stack: bool | None
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


class MarketplaceCatalogClient:
    """A client for the ``MarketplaceCatalog`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
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
        use_dual_stack: bool | None = None,
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
        self.config = MarketplaceCatalogClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[MarketplaceCatalogClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MarketplaceCatalogClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def batch_describe_entities(
        self,
        entity_request_list: "aws_sdk_marketplace_catalog.types.entity_request_list.EntityRequestList",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
    ) -> "aws_sdk_marketplace_catalog.types.batch_describe_entities_response.BatchDescribeEntitiesResponse":
        """<p>Returns metadata and content for multiple entities. This is the Batch version of the <code>DescribeEntity</code> API and uses the same IAM permission action as <code>DescribeEntity</code> API.</p>

        Args:
            entity_request_list: <p>List of entity IDs and the catalogs the entities are present in.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.batch_describe_entities_request.BatchDescribeEntitiesRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.batch_describe_entities_response.BatchDescribeEntitiesResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.batch_describe_entities

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.batch_describe_entities.batch_describe_entities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.batch_describe_entities_request.BatchDescribeEntitiesRequest = {}  # type: ignore[typeddict-item]
        input["entity_request_list"] = entity_request_list

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_change_set(
        self,
        catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog",
        change_set_id: "aws_sdk_marketplace_catalog.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
    ) -> "aws_sdk_marketplace_catalog.types.cancel_change_set_response.CancelChangeSetResponse":
        """<p>Used to cancel an open change request. Must be sent before the status of the request changes to <code>APPLYING</code>, the final stage of completing your change request. You can describe a change during the 60-day request history retention period for API calls.</p>

        Args:
            catalog: <p>Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code>.</p>
            change_set_id: <p>Required. The unique identifier of the <code>StartChangeSet</code> request that you want to cancel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.cancel_change_set_request.CancelChangeSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.cancel_change_set_response.CancelChangeSetResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.cancel_change_set

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.cancel_change_set.cancel_change_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.cancel_change_set_request.CancelChangeSetRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["change_set_id"] = change_set_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_marketplace_catalog.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
    ) -> "aws_sdk_marketplace_catalog.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a resource-based policy on an entity that is identified by its resource ARN.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the entity resource that is associated with the resource policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.delete_resource_policy

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_change_set(
        self,
        catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog",
        change_set_id: "aws_sdk_marketplace_catalog.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
    ) -> "aws_sdk_marketplace_catalog.types.describe_change_set_response.DescribeChangeSetResponse":
        """<p>Provides information about a given change set.</p>

        Args:
            catalog: <p>Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            change_set_id: <p>Required. The unique identifier for the <code>StartChangeSet</code> request that you want to describe the details for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.describe_change_set_request.DescribeChangeSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.describe_change_set_response.DescribeChangeSetResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.describe_change_set

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.describe_change_set.describe_change_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.describe_change_set_request.DescribeChangeSetRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["change_set_id"] = change_set_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_entity(
        self,
        catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog",
        entity_id: "aws_sdk_marketplace_catalog.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
    ) -> "aws_sdk_marketplace_catalog.types.describe_entity_response.DescribeEntityResponse":
        """<p>Returns the metadata and content of the entity.</p>

        Args:
            catalog: <p>Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            entity_id: <p>Required. The unique ID of the entity to describe.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.describe_entity_request.DescribeEntityRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.describe_entity_response.DescribeEntityResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.describe_entity

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.describe_entity.describe_entity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.describe_entity_request.DescribeEntityRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["entity_id"] = entity_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "aws_sdk_marketplace_catalog.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
    ) -> "aws_sdk_marketplace_catalog.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Gets a resource-based policy of an entity that is identified by its resource ARN.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the entity resource that is associated with the resource policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.get_resource_policy

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_change_sets(
        self,
        catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
        filter_list: Optional[
            "aws_sdk_marketplace_catalog.types.filter_list.FilterList"
        ] = None,
        sort: Optional["aws_sdk_marketplace_catalog.types.sort.Sort"] = None,
        max_results: Optional[
            "aws_sdk_marketplace_catalog.types.list_change_sets_max_result_integer.ListChangeSetsMaxResultInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_marketplace_catalog.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_marketplace_catalog.types.list_change_sets_response.ListChangeSetsResponse":
        """<p>Returns the list of change sets owned by the account being used to make the call. You can filter this list by providing any combination of <code>entityId</code>, <code>ChangeSetName</code>, and status. If you provide more than one filter, the API operation applies a logical AND between the filters.</p> <p>You can describe a change during the 60-day request history retention period for API calls.</p>

        Args:
            catalog: <p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            filter_list: <p>An array of filter objects.</p>
            sort: <p>An object that contains two attributes, <code>SortBy</code> and <code>SortOrder</code>.</p>
            max_results: <p>The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results. By default, this value is 20.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.list_change_sets_request.ListChangeSetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.list_change_sets_response.ListChangeSetsResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.list_change_sets

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.list_change_sets.list_change_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.list_change_sets_request.ListChangeSetsRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if filter_list is not None:
            input["filter_list"] = filter_list
        if sort is not None:
            input["sort"] = sort
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

    def iter_list_change_sets(
        self,
        catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
        filter_list: Optional[
            "aws_sdk_marketplace_catalog.types.filter_list.FilterList"
        ] = None,
        sort: Optional["aws_sdk_marketplace_catalog.types.sort.Sort"] = None,
        max_results: Optional[
            "aws_sdk_marketplace_catalog.types.list_change_sets_max_result_integer.ListChangeSetsMaxResultInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_marketplace_catalog.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_marketplace_catalog.types.change_set_summary_list_item.ChangeSetSummaryListItem]":
        _token = next_token
        while True:
            _response = self.list_change_sets(
                catalog,
                config_overrides=config_overrides,
                filter_list=filter_list,
                sort=sort,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("change_set_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_entities(
        self,
        catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog",
        entity_type: "aws_sdk_marketplace_catalog.types.entity_type.EntityType",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
        filter_list: Optional[
            "aws_sdk_marketplace_catalog.types.filter_list.FilterList"
        ] = None,
        sort: Optional["aws_sdk_marketplace_catalog.types.sort.Sort"] = None,
        next_token: Optional[
            "aws_sdk_marketplace_catalog.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_marketplace_catalog.types.list_entities_max_result_integer.ListEntitiesMaxResultInteger"
        ] = None,
        ownership_type: Optional[
            "aws_sdk_marketplace_catalog.types.ownership_type.OwnershipType"
        ] = None,
        entity_type_filters: Optional[
            "aws_sdk_marketplace_catalog.types.entity_type_filters.EntityTypeFilters"
        ] = None,
        entity_type_sort: Optional[
            "aws_sdk_marketplace_catalog.types.entity_type_sort.EntityTypeSort"
        ] = None,
    ) -> (
        "aws_sdk_marketplace_catalog.types.list_entities_response.ListEntitiesResponse"
    ):
        """<p>Provides the list of entities of a given type.</p>

        Args:
            catalog: <p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            entity_type: <p>The type of entities to retrieve. Valid values are: <code>AmiProduct</code>, <code>ContainerProduct</code>, <code>DataProduct</code>, <code>SaaSProduct</code>, <code>ProcurementPolicy</code>, <code>Experience</code>, <code>Audience</code>, <code>BrandingSettings</code>, <code>Offer</code>, <code>OfferSet</code>, <code>Seller</code>, <code>ResaleAuthorization</code>, <code>Solution</code>.</p>
            filter_list: <p>An array of filter objects. Each filter object contains two attributes, <code>filterName</code> and <code>filterValues</code>.</p>
            sort: <p>An object that contains two attributes, <code>SortBy</code> and <code>SortOrder</code>.</p>
            next_token: <p>The value of the next token, if it exists. Null if there are no more results.</p>
            max_results: <p>Specifies the upper limit of the elements on a single page. If a value isn't provided, the default value is 20.</p>
            ownership_type: <p>Filters the returned set of entities based on their owner. The default is <code>SELF</code>. To list entities shared with you through AWS Resource Access Manager (AWS RAM), set to <code>SHARED</code>. Entities shared through the AWS Marketplace Catalog API <code>PutResourcePolicy</code> operation can't be discovered through the <code>SHARED</code> parameter.</p>
            entity_type_filters: <p>A Union object containing filter shapes for all <code>EntityType</code>s. Each <code>EntityTypeFilter</code> shape will have filters applicable for that <code>EntityType</code> that can be used to search or filter entities.</p>
            entity_type_sort: <p>A Union object containing <code>Sort</code> shapes for all <code>EntityType</code>s. Each <code>EntityTypeSort</code> shape will have <code>SortBy</code> and <code>SortOrder</code> applicable for fields on that <code>EntityType</code>. This can be used to sort the results of the filter query.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.list_entities_request.ListEntitiesRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.list_entities_response.ListEntitiesResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.list_entities

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.list_entities.list_entities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.list_entities_request.ListEntitiesRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["entity_type"] = entity_type
        if filter_list is not None:
            input["filter_list"] = filter_list
        if sort is not None:
            input["sort"] = sort
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if ownership_type is not None:
            input["ownership_type"] = ownership_type
        if entity_type_filters is not None:
            input["entity_type_filters"] = entity_type_filters
        if entity_type_sort is not None:
            input["entity_type_sort"] = entity_type_sort

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_entities(
        self,
        catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog",
        entity_type: "aws_sdk_marketplace_catalog.types.entity_type.EntityType",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
        filter_list: Optional[
            "aws_sdk_marketplace_catalog.types.filter_list.FilterList"
        ] = None,
        sort: Optional["aws_sdk_marketplace_catalog.types.sort.Sort"] = None,
        next_token: Optional[
            "aws_sdk_marketplace_catalog.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_marketplace_catalog.types.list_entities_max_result_integer.ListEntitiesMaxResultInteger"
        ] = None,
        ownership_type: Optional[
            "aws_sdk_marketplace_catalog.types.ownership_type.OwnershipType"
        ] = None,
        entity_type_filters: Optional[
            "aws_sdk_marketplace_catalog.types.entity_type_filters.EntityTypeFilters"
        ] = None,
        entity_type_sort: Optional[
            "aws_sdk_marketplace_catalog.types.entity_type_sort.EntityTypeSort"
        ] = None,
    ) -> "Iterator[aws_sdk_marketplace_catalog.types.entity_summary.EntitySummary]":
        _token = next_token
        while True:
            _response = self.list_entities(
                catalog,
                entity_type,
                config_overrides=config_overrides,
                filter_list=filter_list,
                sort=sort,
                next_token=_token,
                max_results=max_results,
                ownership_type=ownership_type,
                entity_type_filters=entity_type_filters,
                entity_type_sort=entity_type_sort,
            )
            _page = _resolve_path(_response, ("entity_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_marketplace_catalog.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
    ) -> "aws_sdk_marketplace_catalog.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags that have been added to a resource (either an <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities\">entity</a> or <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\">change set</a>).</p>

        Args:
            resource_arn: <p>Required. The Amazon Resource Name (ARN) associated with the resource you want to list tags on.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.list_tags_for_resource

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "aws_sdk_marketplace_catalog.types.resource_arn.ResourceARN",
        policy: "aws_sdk_marketplace_catalog.types.resource_policy_json.ResourcePolicyJson",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
    ) -> "aws_sdk_marketplace_catalog.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Attaches a resource-based policy to an entity. Examples of an entity include: <code>AmiProduct</code> and <code>ContainerProduct</code>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the entity resource you want to associate with a resource policy.</p>
            policy: <p>The policy document to set; formatted in JSON.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.put_resource_policy

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_change_set(
        self,
        catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog",
        change_set: "aws_sdk_marketplace_catalog.types.requested_change_list.RequestedChangeList",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
        change_set_name: Optional[
            "aws_sdk_marketplace_catalog.types.change_set_name.ChangeSetName"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_marketplace_catalog.types.client_request_token.ClientRequestToken"
        ] = None,
        change_set_tags: Optional[
            "aws_sdk_marketplace_catalog.types.tag_list.TagList"
        ] = None,
        intent: Optional["aws_sdk_marketplace_catalog.types.intent.Intent"] = None,
    ) -> "aws_sdk_marketplace_catalog.types.start_change_set_response.StartChangeSetResponse":
        """<p>Allows you to request changes for your entities. Within a single <code>ChangeSet</code>, you can't start the same change type against the same entity multiple times. Additionally, when a <code>ChangeSet</code> is running, all the entities targeted by the different changes are locked until the change set has completed (either succeeded, cancelled, or failed). If you try to start a change set containing a change against an entity that is already locked, you will receive a <code>ResourceInUseException</code> error.</p> <p>For example, you can't start the <code>ChangeSet</code> described in the <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html#API_StartChangeSet_Examples\">example</a> later in this topic because it contains two changes to run the same change type (<code>AddRevisions</code>) against the same entity (<code>entity-id@1</code>).</p> <p>For more information about working with change sets, see <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\"> Working with change sets</a>. For information about change types for single-AMI products, see <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products\">Working with single-AMI products</a>. Also, for more information about change types available for container-based products, see <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products\">Working with container products</a>.</p> <p>To download \"DetailsDocument\" shapes, see <a href=\"https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python\">Python</a> and <a href=\"https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-java/tree/main\">Java</a> shapes on GitHub.</p>

        Args:
            catalog: <p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            change_set: <p>Array of <code>change</code> object.</p>
            change_set_name: <p>Optional case sensitive string of up to 100 ASCII characters. The change set name can be used to filter the list of change sets. </p>
            client_request_token: <p>A unique token to identify the request to ensure idempotency.</p>
            change_set_tags: <p>A list of objects specifying each key name and value for the <code>ChangeSetTags</code> property.</p>
            intent: <p>The intent related to the request. The default is <code>APPLY</code>. To test your request before applying changes to your entities, use <code>VALIDATE</code>. This feature is currently available for adding versions to single-AMI products. For more information, see <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#ami-add-version\">Add a new version</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.start_change_set_request.StartChangeSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.start_change_set_response.StartChangeSetResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.start_change_set

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.start_change_set.start_change_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.start_change_set_request.StartChangeSetRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["change_set"] = change_set
        if change_set_name is not None:
            input["change_set_name"] = change_set_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if change_set_tags is not None:
            input["change_set_tags"] = change_set_tags
        if intent is not None:
            input["intent"] = intent

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_marketplace_catalog.types.resource_arn.ResourceARN",
        tags: "aws_sdk_marketplace_catalog.types.tag_list.TagList",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
    ) -> "aws_sdk_marketplace_catalog.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource (either an <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities\">entity</a> or <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\">change set</a>).</p>

        Args:
            resource_arn: <p>Required. The Amazon Resource Name (ARN) associated with the resource you want to tag.</p>
            tags: <p>Required. A list of objects specifying each key name and value. Number of objects allowed: 1-50.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.tag_resource

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_marketplace_catalog.types.resource_arn.ResourceARN",
        tag_keys: "aws_sdk_marketplace_catalog.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[MarketplaceCatalogClientConfig] = None,
    ) -> "aws_sdk_marketplace_catalog.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or list of tags from a resource (either an <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities\">entity</a> or <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\">change set</a>).</p>

        Args:
            resource_arn: <p>Required. The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from.</p>
            tag_keys: <p>Required. A list of key names of tags to be removed. Number of strings allowed: 0-256.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_marketplace_catalog.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_marketplace_catalog.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_marketplace_catalog._operations.awsmp_seymour.untag_resource

            output, http_response = (
                aws_sdk_marketplace_catalog._operations.awsmp_seymour.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_marketplace_catalog.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
