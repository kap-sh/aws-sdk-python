"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#AWSBillingAndCostManagementDataExports``."""

from aws_sdk_bcm_data_exports._auth._signers import SigV4Signer
from aws_sdk_bcm_data_exports._auth._sigv4 import presign_sigv4
from collections.abc import Iterator
from aws_sdk_bcm_data_exports._pagination import resolve_path as _resolve_path
from typing import Any, Iterable, TypedDict, Unpack, TYPE_CHECKING
from typing_extensions import Self
from typing import Optional
from zapros import URL, BaseHandler, Client
from aws_sdk_bcm_data_exports._auth._zapros_handler import AuthMiddleware
from aws_sdk_bcm_data_exports._services._pipeline import Interceptor, OperationOptions, OperationRequest, OperationResponse, execute_pipeline, retry
import time
from aws_sdk_bcm_data_exports.errors import ServiceError, WaiterFailedError, WaiterTimeoutError
import warnings
from aws_sdk_bcm_data_exports._auth._identity import Credentials
from aws_sdk_bcm_data_exports._auth._providers import CredentialsProvider, StaticAwsCredentialsProvider
if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.arn
    import aws_sdk_bcm_data_exports.types.execution_reference
    import aws_sdk_bcm_data_exports.types.generic_string
    import aws_sdk_bcm_data_exports.types.get_execution_request
    import aws_sdk_bcm_data_exports.types.get_execution_response
    import aws_sdk_bcm_data_exports.types.get_table_request
    import aws_sdk_bcm_data_exports.types.get_table_response
    import aws_sdk_bcm_data_exports.types.list_executions_request
    import aws_sdk_bcm_data_exports.types.list_executions_response
    import aws_sdk_bcm_data_exports.types.list_tables_request
    import aws_sdk_bcm_data_exports.types.list_tables_response
    import aws_sdk_bcm_data_exports.types.list_tags_for_resource_request
    import aws_sdk_bcm_data_exports.types.list_tags_for_resource_response
    import aws_sdk_bcm_data_exports.types.max_results
    import aws_sdk_bcm_data_exports.types.next_page_token
    import aws_sdk_bcm_data_exports.types.resource_tag_key_list
    import aws_sdk_bcm_data_exports.types.resource_tag_list
    import aws_sdk_bcm_data_exports.types.table
    import aws_sdk_bcm_data_exports.types.table_name
    import aws_sdk_bcm_data_exports.types.table_properties
    import aws_sdk_bcm_data_exports.types.tag_resource_request
    import aws_sdk_bcm_data_exports.types.tag_resource_response
    import aws_sdk_bcm_data_exports.types.untag_resource_request
    import aws_sdk_bcm_data_exports.types.untag_resource_response

class BCMDataExportsClientConfig(TypedDict, total=False):
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

class BCMDataExportsClient:
    """A client for the ``BCMDataExports`` service.

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
    def __init__(self, http_handler: BaseHandler | None = None, operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None, retry_max_attempts: int | None = None, use_fips: bool | None = None, endpoint: str | None = None, region: str | None = None, credentials: Credentials | None = None, credentials_provider: CredentialsProvider | None = None):
        self._client = Client(http_handler).wrap_with_middleware(lambda next: AuthMiddleware(next))
        if credentials is not None and credentials_provider is not None:
            warnings.warn("Both credentials and credentials_provider given; provider takes precedence")
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = BCMDataExportsClientConfig({"operation_interceptors": operation_interceptors or [], "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS if retry_max_attempts is None else retry_max_attempts, "use_fips": use_fips, "endpoint": endpoint, "region": region, "credentials_provider": credentials_provider})
    def operation_options(self, config_overrides: Optional[BCMDataExportsClientConfig] = None) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BCMDataExportsClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [*overrides.get("operation_interceptors", self.config.get("operation_interceptors", [])), retry()]
        options_: OperationOptions = OperationOptions(client=self._client, retry_max_attempts=overrides.get("retry_max_attempts", self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS)), use_fips=overrides.get("use_fips", self.config.get("use_fips")), endpoint=overrides.get("endpoint", self.config.get("endpoint")), region=overrides.get("region", self.config.get("region")), credentials_provider=overrides.get("credentials_provider", self.config.get("credentials_provider")))
        return interceptors_, options_
    def get_execution(self, export_arn: "aws_sdk_bcm_data_exports.types.arn.Arn", execution_id: "aws_sdk_bcm_data_exports.types.generic_string.GenericString", *, config_overrides: Optional[BCMDataExportsClientConfig] = None) -> "aws_sdk_bcm_data_exports.types.get_execution_response.GetExecutionResponse":
        """<p>Exports data based on the source data update.</p>

        Args:
            export_arn: <p>The Amazon Resource Name (ARN) of the Export object that generated this specific execution.</p>
            execution_id: <p>The ID for this specific execution.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_data_exports.types.get_execution_request.GetExecutionRequest]') -> OperationResponse["aws_sdk_bcm_data_exports.types.get_execution_response.GetExecutionResponse"]:
            import aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_execution
            output, http_response = aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_execution.get_execution(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_data_exports.types.get_execution_request.GetExecutionRequest = {}  # type: ignore[typeddict-item]
        input["export_arn"] = export_arn
        input["execution_id"] = execution_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_table(self, table_name: "aws_sdk_bcm_data_exports.types.table_name.TableName", *, config_overrides: Optional[BCMDataExportsClientConfig] = None, table_properties: Optional["aws_sdk_bcm_data_exports.types.table_properties.TableProperties"] = None) -> "aws_sdk_bcm_data_exports.types.get_table_response.GetTableResponse":
        """<p>Returns the metadata for the specified table and table properties. This includes the list of columns in the table schema, their data types, and column descriptions.</p>

        Args:
            table_name: <p>The name of the table.</p>
            table_properties: <p>TableProperties are additional configurations you can provide to change the data and schema of a table. Each table can have different TableProperties. Tables are not required to have any TableProperties. Each table property has a default value that it assumes if not specified.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_data_exports.types.get_table_request.GetTableRequest]') -> OperationResponse["aws_sdk_bcm_data_exports.types.get_table_response.GetTableResponse"]:
            import aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_table
            output, http_response = aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.get_table.get_table(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_data_exports.types.get_table_request.GetTableRequest = {}  # type: ignore[typeddict-item]
        input["table_name"] = table_name
        if table_properties is not None:
            input["table_properties"] = table_properties

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_executions(self, export_arn: "aws_sdk_bcm_data_exports.types.arn.Arn", *, config_overrides: Optional[BCMDataExportsClientConfig] = None, max_results: Optional["aws_sdk_bcm_data_exports.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bcm_data_exports.types.next_page_token.NextPageToken"] = None) -> "aws_sdk_bcm_data_exports.types.list_executions_response.ListExecutionsResponse":
        """<p>Lists the historical executions for the export.</p>

        Args:
            export_arn: <p>The Amazon Resource Name (ARN) for this export.</p>
            max_results: <p>The maximum number of objects that are returned for the request.</p>
            next_token: <p>The token to retrieve the next set of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_data_exports.types.list_executions_request.ListExecutionsRequest]') -> OperationResponse["aws_sdk_bcm_data_exports.types.list_executions_response.ListExecutionsResponse"]:
            import aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_executions
            output, http_response = aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_executions.list_executions(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_data_exports.types.list_executions_request.ListExecutionsRequest = {}  # type: ignore[typeddict-item]
        input["export_arn"] = export_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def iter_list_executions(self, export_arn: "aws_sdk_bcm_data_exports.types.arn.Arn", *, config_overrides: Optional[BCMDataExportsClientConfig] = None, max_results: Optional["aws_sdk_bcm_data_exports.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bcm_data_exports.types.next_page_token.NextPageToken"] = None) -> "Iterator[aws_sdk_bcm_data_exports.types.execution_reference.ExecutionReference]":
        _token = next_token
        while True:
            _response = self.list_executions(
                export_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ('executions',))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ('next_token',))
            if not _token:
                break
    def list_tables(self, *, config_overrides: Optional[BCMDataExportsClientConfig] = None, next_token: Optional["aws_sdk_bcm_data_exports.types.next_page_token.NextPageToken"] = None, max_results: Optional["aws_sdk_bcm_data_exports.types.max_results.MaxResults"] = None) -> "aws_sdk_bcm_data_exports.types.list_tables_response.ListTablesResponse":
        """<p>Lists all available tables in data exports.</p>

        Args:
            next_token: <p>The token to retrieve the next set of results.</p>
            max_results: <p>The maximum number of objects that are returned for the request.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_data_exports.types.list_tables_request.ListTablesRequest]') -> OperationResponse["aws_sdk_bcm_data_exports.types.list_tables_response.ListTablesResponse"]:
            import aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_tables
            output, http_response = aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_tables.list_tables(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_data_exports.types.list_tables_request.ListTablesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def iter_list_tables(self, *, config_overrides: Optional[BCMDataExportsClientConfig] = None, next_token: Optional["aws_sdk_bcm_data_exports.types.next_page_token.NextPageToken"] = None, max_results: Optional["aws_sdk_bcm_data_exports.types.max_results.MaxResults"] = None) -> "Iterator[aws_sdk_bcm_data_exports.types.table.Table]":
        _token = next_token
        while True:
            _response = self.list_tables(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ('tables',))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ('next_token',))
            if not _token:
                break
    def list_tags_for_resource(self, resource_arn: "aws_sdk_bcm_data_exports.types.arn.Arn", *, config_overrides: Optional[BCMDataExportsClientConfig] = None, max_results: Optional["aws_sdk_bcm_data_exports.types.max_results.MaxResults"] = None, next_token: Optional["aws_sdk_bcm_data_exports.types.next_page_token.NextPageToken"] = None) -> "aws_sdk_bcm_data_exports.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List tags associated with an existing data export.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
            max_results: <p>The maximum number of objects that are returned for the request.</p>
            next_token: <p>The token to retrieve the next set of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_data_exports.types.list_tags_for_resource_request.ListTagsForResourceRequest]') -> OperationResponse["aws_sdk_bcm_data_exports.types.list_tags_for_resource_response.ListTagsForResourceResponse"]:
            import aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_tags_for_resource
            output, http_response = aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.list_tags_for_resource.list_tags_for_resource(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_data_exports.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def tag_resource(self, resource_arn: "aws_sdk_bcm_data_exports.types.arn.Arn", resource_tags: "aws_sdk_bcm_data_exports.types.resource_tag_list.ResourceTagList", *, config_overrides: Optional[BCMDataExportsClientConfig] = None) -> "aws_sdk_bcm_data_exports.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags for an existing data export definition.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
            resource_tags: <p>The tags to associate with the resource. Each tag consists of a key and a value, and each key must be unique for the resource.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_data_exports.types.tag_resource_request.TagResourceRequest]') -> OperationResponse["aws_sdk_bcm_data_exports.types.tag_resource_response.TagResourceResponse"]:
            import aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.tag_resource
            output, http_response = aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.tag_resource.tag_resource(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_data_exports.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["resource_tags"] = resource_tags

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def untag_resource(self, resource_arn: "aws_sdk_bcm_data_exports.types.arn.Arn", resource_tag_keys: "aws_sdk_bcm_data_exports.types.resource_tag_key_list.ResourceTagKeyList", *, config_overrides: Optional[BCMDataExportsClientConfig] = None) -> "aws_sdk_bcm_data_exports.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes tags associated with an existing data export definition.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
            resource_tag_keys: <p>The tag keys that are associated with the resource ARN.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bcm_data_exports.types.untag_resource_request.UntagResourceRequest]') -> OperationResponse["aws_sdk_bcm_data_exports.types.untag_resource_response.UntagResourceResponse"]:
            import aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.untag_resource
            output, http_response = aws_sdk_bcm_data_exports._operations.aws_billing_and_cost_management_data_exports.untag_resource.untag_resource(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_data_exports.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["resource_tag_keys"] = resource_tag_keys

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def __enter__(self) -> Self:
        return self
    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()