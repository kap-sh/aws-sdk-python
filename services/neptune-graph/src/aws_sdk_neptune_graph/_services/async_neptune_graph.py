"""Generated from Smithy shape ``com.amazonaws.neptunegraph#AmazonNeptuneGraph``."""

from aws_sdk_neptune_graph._auth._signers import SigV4Signer
from aws_sdk_neptune_graph._auth._sigv4 import presign_sigv4
from collections.abc import AsyncIterator
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any, Iterable, TypedDict, Unpack, TYPE_CHECKING
from typing_extensions import Self
from typing import Optional
from zapros import URL, AsyncBaseHandler, AsyncClient
from aws_sdk_neptune_graph._auth._zapros_handler import AuthMiddleware
from aws_sdk_neptune_graph._services._pipeline import AsyncInterceptor, AsyncOperationOptions, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline, aretry
from aws_sdk_neptune_graph._async import anysleep
import time
from aws_sdk_neptune_graph.errors import ServiceError, WaiterFailedError, WaiterTimeoutError
import warnings
import aws_sdk_neptune_graph._auth._signers
import aws_sdk_neptune_graph._auth._sigv4
from aws_sdk_neptune_graph._auth._identity import Credentials
from aws_sdk_neptune_graph._auth._providers import CredentialsProvider, StaticAwsCredentialsProvider
if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.arn
    import aws_sdk_neptune_graph.types.cancel_query_input
    import aws_sdk_neptune_graph.types.document_valued_map
    import aws_sdk_neptune_graph.types.execute_query_input
    import aws_sdk_neptune_graph.types.execute_query_output
    import aws_sdk_neptune_graph.types.explain_mode
    import aws_sdk_neptune_graph.types.get_graph_summary_input
    import aws_sdk_neptune_graph.types.get_graph_summary_output
    import aws_sdk_neptune_graph.types.get_query_input
    import aws_sdk_neptune_graph.types.get_query_output
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.graph_summary_mode
    import aws_sdk_neptune_graph.types.list_queries_input
    import aws_sdk_neptune_graph.types.list_queries_output
    import aws_sdk_neptune_graph.types.list_tags_for_resource_input
    import aws_sdk_neptune_graph.types.list_tags_for_resource_output
    import aws_sdk_neptune_graph.types.plan_cache_type
    import aws_sdk_neptune_graph.types.query_language
    import aws_sdk_neptune_graph.types.query_state_input
    import aws_sdk_neptune_graph.types.tag_key_list
    import aws_sdk_neptune_graph.types.tag_map
    import aws_sdk_neptune_graph.types.tag_resource_input
    import aws_sdk_neptune_graph.types.tag_resource_output
    import aws_sdk_neptune_graph.types.untag_resource_input
    import aws_sdk_neptune_graph.types.untag_resource_output

class AsyncNeptuneGraphClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_fips: bool | None
    use_dual_stack: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None

DEFAULT_RETRY_MAX_ATTEMPTS = 3

async def ensure_async_iterator(it: AsyncIterator[bytes] | bytes) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk

class AsyncNeptuneGraphClient:
    """A client for the ``NeptuneGraph`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """
    def __init__(self, http_handler: AsyncBaseHandler | None = None, operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None, retry_max_attempts: int | None = None, region: str | None = None, use_fips: bool | None = None, use_dual_stack: bool | None = None, endpoint: str | None = None, credentials: Credentials | None = None, credentials_provider: CredentialsProvider | None = None):
        self._client = AsyncClient(http_handler).wrap_with_middleware(lambda next: AuthMiddleware(next))
        if credentials is not None and credentials_provider is not None:
            warnings.warn("Both credentials and credentials_provider given; provider takes precedence")
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncNeptuneGraphClientConfig({"operation_interceptors": operation_interceptors or [], "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS if retry_max_attempts is None else retry_max_attempts, "region": region, "use_fips": use_fips, "use_dual_stack": use_dual_stack, "endpoint": endpoint, "credentials_provider": credentials_provider})
    def operation_options(self, config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncNeptuneGraphClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [*overrides.get("operation_interceptors", self.config.get("operation_interceptors", [])), aretry()]
        options_: AsyncOperationOptions = AsyncOperationOptions(client=self._client, retry_max_attempts=overrides.get("retry_max_attempts", self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS)), region=overrides.get("region", self.config.get("region")), use_fips=overrides.get("use_fips", self.config.get("use_fips")), use_dual_stack=overrides.get("use_dual_stack", self.config.get("use_dual_stack")), endpoint=overrides.get("endpoint", self.config.get("endpoint")), credentials_provider=overrides.get("credentials_provider", self.config.get("credentials_provider")))
        return interceptors_, options_
    async def cancel_query(self, graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier", query_id: str, *, config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None) -> None:
        """<p>Cancels a specified query.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            query_id: <p>The unique identifier of the query to cancel.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_neptune_graph.types.cancel_query_input.CancelQueryInput]') -> AsyncOperationResponse[None]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.cancel_query
            output, http_response = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.cancel_query.async_cancel_query(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.cancel_query_input.CancelQueryInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        input["query_id"] = query_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    @asynccontextmanager
    async def execute_query(self, graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier", query_string: str, language: "aws_sdk_neptune_graph.types.query_language.QueryLanguage", *, config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None, parameters: Optional["aws_sdk_neptune_graph.types.document_valued_map.DocumentValuedMap"] = None, plan_cache: Optional["aws_sdk_neptune_graph.types.plan_cache_type.PlanCacheType"] = None, explain_mode: Optional["aws_sdk_neptune_graph.types.explain_mode.ExplainMode"] = None, query_timeout_milliseconds: Optional[int] = None) -> "AsyncGenerator[aws_sdk_neptune_graph.types.execute_query_output.ExecuteQueryOutput]":
        """<p>Execute an openCypher query.</p> <p> When invoking this operation in a Neptune Analytics cluster, the IAM user or role making the request must have a policy attached that allows one of the following IAM actions in that cluster, depending on the query: </p> <ul> <li> <p>neptune-graph:ReadDataViaQuery</p> </li> <li> <p>neptune-graph:WriteDataViaQuery</p> </li> <li> <p>neptune-graph:DeleteDataViaQuery</p> </li> </ul>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            query_string: <p>The query string to be executed.</p>
            language: <p>The query language the query is written in. Currently only openCypher is supported.</p>
            parameters: <p>The data parameters the query can use in JSON format. For example: {\"name\": \"john\", \"age\": 20}. (optional) </p>
            plan_cache: <p>Query plan cache is a feature that saves the query plan and reuses it on successive executions of the same query. This reduces query latency, and works for both <code>READ</code> and <code>UPDATE</code> queries. The plan cache is an LRU cache with a 5 minute TTL and a capacity of 1000.</p>
            explain_mode: <p>The explain mode parameter returns a query explain instead of the actual query results. A query explain can be used to gather insights about the query execution such as planning decisions, time spent on each operator, solutions flowing etc.</p>
            query_timeout_milliseconds: <p>Specifies the query timeout duration, in milliseconds. (optional)</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_neptune_graph.types.execute_query_input.ExecuteQueryInput]') -> AsyncOperationResponse["aws_sdk_neptune_graph.types.execute_query_output.ExecuteQueryOutput"]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.execute_query
            output, http_response = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.execute_query.async_execute_query(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.execute_query_input.ExecuteQueryInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        input["query_string"] = query_string
        input["language"] = language
        if parameters is not None:
            input["parameters"] = parameters
        if plan_cache is not None:
            input["plan_cache"] = plan_cache
        if explain_mode is not None:
            input["explain_mode"] = explain_mode
        if query_timeout_milliseconds is not None:
            input["query_timeout_milliseconds"] = query_timeout_milliseconds

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        yield response.output
    async def get_graph_summary(self, graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier", *, config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None, mode: Optional["aws_sdk_neptune_graph.types.graph_summary_mode.GraphSummaryMode"] = None) -> "aws_sdk_neptune_graph.types.get_graph_summary_output.GetGraphSummaryOutput":
        """<p>Gets a graph summary for a property graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            mode: <p>The summary mode can take one of two values: <code>basic</code> (the default), and <code>detailed</code>.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_neptune_graph.types.get_graph_summary_input.GetGraphSummaryInput]') -> AsyncOperationResponse["aws_sdk_neptune_graph.types.get_graph_summary_output.GetGraphSummaryOutput"]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_graph_summary
            output, http_response = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_graph_summary.async_get_graph_summary(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.get_graph_summary_input.GetGraphSummaryInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        if mode is not None:
            input["mode"] = mode

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_query(self, graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier", query_id: str, *, config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None) -> "aws_sdk_neptune_graph.types.get_query_output.GetQueryOutput":
        """<p>Retrieves the status of a specified query.</p> <note> <p> When invoking this operation in a Neptune Analytics cluster, the IAM user or role making the request must have the <code>neptune-graph:GetQueryStatus</code> IAM action attached. </p> </note>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            query_id: <p>The ID of the query in question.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_neptune_graph.types.get_query_input.GetQueryInput]') -> AsyncOperationResponse["aws_sdk_neptune_graph.types.get_query_output.GetQueryOutput"]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_query
            output, http_response = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_query.async_get_query(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.get_query_input.GetQueryInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        input["query_id"] = query_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_queries(self, graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier", max_results: int, *, config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None, state: Optional["aws_sdk_neptune_graph.types.query_state_input.QueryStateInput"] = None) -> "aws_sdk_neptune_graph.types.list_queries_output.ListQueriesOutput":
        """<p>Lists active openCypher queries.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            max_results: <p>The maximum number of results to be fetched by the API.</p>
            state: <p>Filtered list of queries based on state.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_neptune_graph.types.list_queries_input.ListQueriesInput]') -> AsyncOperationResponse["aws_sdk_neptune_graph.types.list_queries_output.ListQueriesOutput"]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_queries
            output, http_response = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_queries.async_list_queries(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.list_queries_input.ListQueriesInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        input["max_results"] = max_results
        if state is not None:
            input["state"] = state

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_tags_for_resource(self, resource_arn: "aws_sdk_neptune_graph.types.arn.Arn", *, config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None) -> "aws_sdk_neptune_graph.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists tags associated with a specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_neptune_graph.types.list_tags_for_resource_input.ListTagsForResourceInput]') -> AsyncOperationResponse["aws_sdk_neptune_graph.types.list_tags_for_resource_output.ListTagsForResourceOutput"]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_tags_for_resource
            output, http_response = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_tags_for_resource.async_list_tags_for_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def tag_resource(self, resource_arn: "aws_sdk_neptune_graph.types.arn.Arn", tags: "aws_sdk_neptune_graph.types.tag_map.TagMap", *, config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None) -> "aws_sdk_neptune_graph.types.tag_resource_output.TagResourceOutput":
        """<p>Adds tags to the specified resource.</p>

        Args:
            resource_arn: <p>ARN of the resource for which tags need to be added.</p>
            tags: <p>The tags to be assigned to the Neptune Analytics resource.</p> <p>The tags are metadata that are specified as a list of key-value pairs:</p> <p> <b>Key</b> (string) – A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length. It can't be prefixed with <code>aws:</code> and can only contain the set of Unicode characters specified by this Java regular expression: <code>\"^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$\")</code>.</p> <p> <b>Value</b> (string) – A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length. It can't be prefixed with <code>aws:</code> and can only contain the set of Unicode characters specified by this Java regular expression: <code>\"^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$\")</code>.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_neptune_graph.types.tag_resource_input.TagResourceInput]') -> AsyncOperationResponse["aws_sdk_neptune_graph.types.tag_resource_output.TagResourceOutput"]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.tag_resource
            output, http_response = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.tag_resource.async_tag_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def untag_resource(self, resource_arn: "aws_sdk_neptune_graph.types.arn.Arn", tag_keys: "aws_sdk_neptune_graph.types.tag_key_list.TagKeyList", *, config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None) -> "aws_sdk_neptune_graph.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>ARN of the resource whose tag needs to be removed.</p>
            tag_keys: <p>Tag keys for the tags to be removed.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_neptune_graph.types.untag_resource_input.UntagResourceInput]') -> AsyncOperationResponse["aws_sdk_neptune_graph.types.untag_resource_output.UntagResourceOutput"]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.untag_resource
            output, http_response = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.untag_resource.async_untag_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def __aenter__(self) -> Self:
        return self
    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()