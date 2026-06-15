"""Generated from Smithy shape ``com.amazonaws.kendraranking#AWSKendraRerankingFrontendService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_kendra_ranking._auth._signers
import aws_sdk_kendra_ranking._auth._sigv4
from aws_sdk_kendra_ranking._auth._identity import Credentials
from aws_sdk_kendra_ranking._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_kendra_ranking._auth._zapros_handler import AuthMiddleware
from aws_sdk_kendra_ranking._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.amazon_resource_name
    import aws_sdk_kendra_ranking.types.capacity_units_configuration
    import aws_sdk_kendra_ranking.types.client_token_name
    import aws_sdk_kendra_ranking.types.create_rescore_execution_plan_request
    import aws_sdk_kendra_ranking.types.create_rescore_execution_plan_response
    import aws_sdk_kendra_ranking.types.delete_rescore_execution_plan_request
    import aws_sdk_kendra_ranking.types.describe_rescore_execution_plan_request
    import aws_sdk_kendra_ranking.types.describe_rescore_execution_plan_response
    import aws_sdk_kendra_ranking.types.description
    import aws_sdk_kendra_ranking.types.document_list
    import aws_sdk_kendra_ranking.types.list_rescore_execution_plans_request
    import aws_sdk_kendra_ranking.types.list_rescore_execution_plans_response
    import aws_sdk_kendra_ranking.types.list_tags_for_resource_request
    import aws_sdk_kendra_ranking.types.list_tags_for_resource_response
    import aws_sdk_kendra_ranking.types.max_results_integer_for_list_rescore_execution_plans_request
    import aws_sdk_kendra_ranking.types.next_token
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_id
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_name
    import aws_sdk_kendra_ranking.types.rescore_request
    import aws_sdk_kendra_ranking.types.rescore_result
    import aws_sdk_kendra_ranking.types.search_query
    import aws_sdk_kendra_ranking.types.tag_key_list
    import aws_sdk_kendra_ranking.types.tag_list
    import aws_sdk_kendra_ranking.types.tag_resource_request
    import aws_sdk_kendra_ranking.types.tag_resource_response
    import aws_sdk_kendra_ranking.types.untag_resource_request
    import aws_sdk_kendra_ranking.types.untag_resource_response
    import aws_sdk_kendra_ranking.types.update_rescore_execution_plan_request


class KendraRankingClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class KendraRankingClient:
    """A client for the ``KendraRanking`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = KendraRankingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[KendraRankingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: KendraRankingClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self._config.get("region")),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def create_rescore_execution_plan(
        self,
        name: "aws_sdk_kendra_ranking.types.rescore_execution_plan_name.RescoreExecutionPlanName",
        *,
        config_overrides: Optional[KendraRankingClientConfig] = None,
        description: Optional[
            "aws_sdk_kendra_ranking.types.description.Description"
        ] = None,
        capacity_units: Optional[
            "aws_sdk_kendra_ranking.types.capacity_units_configuration.CapacityUnitsConfiguration"
        ] = None,
        tags: Optional["aws_sdk_kendra_ranking.types.tag_list.TagList"] = None,
        client_token: Optional[
            "aws_sdk_kendra_ranking.types.client_token_name.ClientTokenName"
        ] = None,
    ) -> "aws_sdk_kendra_ranking.types.create_rescore_execution_plan_response.CreateRescoreExecutionPlanResponse":
        r"""<p>Creates a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API. You set the number of capacity units that you require for Amazon Kendra Intelligent Ranking to rescore or re-rank a search service's results.</p> <p>For an example of using the <code>CreateRescoreExecutionPlan</code> API, including using the Python and Java SDKs, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/search-service-rerank.html\">Semantically ranking a search service's results</a>.</p>

        Args:
            name: <p>A name for the rescore execution plan.</p>
            description: <p>A description for the rescore execution plan.</p>
            capacity_units: <p>You can set additional capacity units to meet the needs of your rescore execution plan. You are given a single capacity unit by default. If you want to use the default capacity, you don't set additional capacity units. For more information on the default capacity and additional capacity units, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html\">Adjusting capacity</a>.</p>
            tags: <p>A list of key-value pairs that identify or categorize your rescore execution plan. You can also use tags to help control access to the rescore execution plan. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            client_token: <p>A token that you provide to identify the request to create a rescore execution plan. Multiple calls to the <code>CreateRescoreExecutionPlanRequest</code> API with the same client token will create only one rescore execution plan.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_kendra_ranking.types.create_rescore_execution_plan_request.CreateRescoreExecutionPlanRequest]",
        ) -> OperationResponse[
            "aws_sdk_kendra_ranking.types.create_rescore_execution_plan_response.CreateRescoreExecutionPlanResponse"
        ]:
            import aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.create_rescore_execution_plan

            output, http_response = (
                aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.create_rescore_execution_plan.create_rescore_execution_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kendra_ranking.types.create_rescore_execution_plan_request.CreateRescoreExecutionPlanRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if capacity_units is not None:
            input_["capacity_units"] = capacity_units
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_rescore_execution_plan(
        self,
        id: "aws_sdk_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId",
        *,
        config_overrides: Optional[KendraRankingClientConfig] = None,
    ) -> None:
        """<p>Deletes a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API.</p>

        Args:
            id: <p>The identifier of the rescore execution plan that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_kendra_ranking.types.delete_rescore_execution_plan_request.DeleteRescoreExecutionPlanRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.delete_rescore_execution_plan

            output, http_response = (
                aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.delete_rescore_execution_plan.delete_rescore_execution_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kendra_ranking.types.delete_rescore_execution_plan_request.DeleteRescoreExecutionPlanRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_rescore_execution_plan(
        self,
        id: "aws_sdk_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId",
        *,
        config_overrides: Optional[KendraRankingClientConfig] = None,
    ) -> "aws_sdk_kendra_ranking.types.describe_rescore_execution_plan_response.DescribeRescoreExecutionPlanResponse":
        """<p>Gets information about a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API.</p>

        Args:
            id: <p>The identifier of the rescore execution plan that you want to get information on.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_kendra_ranking.types.describe_rescore_execution_plan_request.DescribeRescoreExecutionPlanRequest]",
        ) -> OperationResponse[
            "aws_sdk_kendra_ranking.types.describe_rescore_execution_plan_response.DescribeRescoreExecutionPlanResponse"
        ]:
            import aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.describe_rescore_execution_plan

            output, http_response = (
                aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.describe_rescore_execution_plan.describe_rescore_execution_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kendra_ranking.types.describe_rescore_execution_plan_request.DescribeRescoreExecutionPlanRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_rescore_execution_plans(
        self,
        *,
        config_overrides: Optional[KendraRankingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_kendra_ranking.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_kendra_ranking.types.max_results_integer_for_list_rescore_execution_plans_request.MaxResultsIntegerForListRescoreExecutionPlansRequest"
        ] = None,
    ) -> "aws_sdk_kendra_ranking.types.list_rescore_execution_plans_response.ListRescoreExecutionPlansResponse":
        """<p>Lists your rescore execution plans. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API.</p>

        Args:
            next_token: <p>If the response is truncated, Amazon Kendra Intelligent Ranking returns a pagination token in the response. You can use this pagination token to retrieve the next set of rescore execution plans.</p>
            max_results: <p>The maximum number of rescore execution plans to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_kendra_ranking.types.list_rescore_execution_plans_request.ListRescoreExecutionPlansRequest]",
        ) -> OperationResponse[
            "aws_sdk_kendra_ranking.types.list_rescore_execution_plans_response.ListRescoreExecutionPlansResponse"
        ]:
            import aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.list_rescore_execution_plans

            output, http_response = (
                aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.list_rescore_execution_plans.list_rescore_execution_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kendra_ranking.types.list_rescore_execution_plans_request.ListRescoreExecutionPlansRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_kendra_ranking.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[KendraRankingClientConfig] = None,
    ) -> "aws_sdk_kendra_ranking.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Gets a list of tags associated with a specified resource. A rescore execution plan is an example of a resource that can have tags associated with it.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the rescore execution plan to get a list of tags for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_kendra_ranking.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_kendra_ranking.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kendra_ranking.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def rescore(
        self,
        rescore_execution_plan_id: "aws_sdk_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId",
        search_query: "aws_sdk_kendra_ranking.types.search_query.SearchQuery",
        documents: "aws_sdk_kendra_ranking.types.document_list.DocumentList",
        *,
        config_overrides: Optional[KendraRankingClientConfig] = None,
    ) -> "aws_sdk_kendra_ranking.types.rescore_result.RescoreResult":
        """<p>Rescores or re-ranks search results from a search service such as OpenSearch (self managed). You use the semantic search capabilities of Amazon Kendra Intelligent Ranking to improve the search service's results.</p>

        Args:
            rescore_execution_plan_id: <p>The identifier of the rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API.</p>
            search_query: <p>The input query from the search service.</p>
            documents: <p>The list of documents for Amazon Kendra Intelligent Ranking to rescore or rank on.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_kendra_ranking.types.rescore_request.RescoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_kendra_ranking.types.rescore_result.RescoreResult"
        ]:
            import aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.rescore

            output, http_response = (
                aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.rescore.rescore(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kendra_ranking.types.rescore_request.RescoreRequest = {}  # type: ignore[typeddict-item]
        input_["rescore_execution_plan_id"] = rescore_execution_plan_id
        input_["search_query"] = search_query
        input_["documents"] = documents

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_kendra_ranking.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_kendra_ranking.types.tag_list.TagList",
        *,
        config_overrides: Optional[KendraRankingClientConfig] = None,
    ) -> "aws_sdk_kendra_ranking.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a specified tag to a specified rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API. If the tag already exists, the existing value is replaced with the new value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the rescore execution plan to tag.</p>
            tags: <p>A list of tag keys to add to a rescore execution plan. If a tag already exists, the existing value is replaced with the new value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_kendra_ranking.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_kendra_ranking.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.tag_resource

            output, http_response = (
                aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kendra_ranking.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_kendra_ranking.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_kendra_ranking.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[KendraRankingClientConfig] = None,
    ) -> "aws_sdk_kendra_ranking.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> operation.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the rescore execution plan to remove the tag.</p>
            tag_keys: <p>A list of tag keys to remove from the rescore execution plan. If a tag key does not exist on the resource, it is ignored.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_kendra_ranking.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_kendra_ranking.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.untag_resource

            output, http_response = (
                aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kendra_ranking.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_rescore_execution_plan(
        self,
        id: "aws_sdk_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId",
        *,
        config_overrides: Optional[KendraRankingClientConfig] = None,
        name: Optional[
            "aws_sdk_kendra_ranking.types.rescore_execution_plan_name.RescoreExecutionPlanName"
        ] = None,
        description: Optional[
            "aws_sdk_kendra_ranking.types.description.Description"
        ] = None,
        capacity_units: Optional[
            "aws_sdk_kendra_ranking.types.capacity_units_configuration.CapacityUnitsConfiguration"
        ] = None,
    ) -> None:
        r"""<p>Updates a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API. You can update the number of capacity units you require for Amazon Kendra Intelligent Ranking to rescore or re-rank a search service's results.</p>

        Args:
            id: <p>The identifier of the rescore execution plan that you want to update.</p>
            name: <p>A new name for the rescore execution plan.</p>
            description: <p>A new description for the rescore execution plan.</p>
            capacity_units: <p>You can set additional capacity units to meet the needs of your rescore execution plan. You are given a single capacity unit by default. If you want to use the default capacity, you don't set additional capacity units. For more information on the default capacity and additional capacity units, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html\">Adjusting capacity</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_kendra_ranking.types.update_rescore_execution_plan_request.UpdateRescoreExecutionPlanRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.update_rescore_execution_plan

            output, http_response = (
                aws_sdk_kendra_ranking._operations.aws_kendra_reranking_frontend_service.update_rescore_execution_plan.update_rescore_execution_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kendra_ranking.types.update_rescore_execution_plan_request.UpdateRescoreExecutionPlanRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if capacity_units is not None:
            input_["capacity_units"] = capacity_units

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
