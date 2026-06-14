"""Generated from Smithy shape ``com.amazonaws.backupsearch#CryoBackupSearchService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_backupsearch._auth._signers
import aws_sdk_backupsearch._auth._sigv4
from aws_sdk_backupsearch._auth._identity import Credentials
from aws_sdk_backupsearch._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_backupsearch._auth._zapros_handler import AuthMiddleware
from aws_sdk_backupsearch._pagination import resolve_path as _resolve_path
from aws_sdk_backupsearch._resources.cryo_backup_search_service.search_job import (
    SearchJob,
)
from aws_sdk_backupsearch._resources.cryo_backup_search_service.search_result_export_job import (
    SearchResultExportJob,
)
from aws_sdk_backupsearch._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.generic_id
    import aws_sdk_backupsearch.types.list_search_job_backups_input
    import aws_sdk_backupsearch.types.list_search_job_backups_output
    import aws_sdk_backupsearch.types.list_search_job_results_input
    import aws_sdk_backupsearch.types.list_search_job_results_output
    import aws_sdk_backupsearch.types.list_tags_for_resource_request
    import aws_sdk_backupsearch.types.list_tags_for_resource_response
    import aws_sdk_backupsearch.types.search_job_backups_result
    import aws_sdk_backupsearch.types.tag_keys
    import aws_sdk_backupsearch.types.tag_map
    import aws_sdk_backupsearch.types.tag_resource_request
    import aws_sdk_backupsearch.types.tag_resource_response
    import aws_sdk_backupsearch.types.untag_resource_request
    import aws_sdk_backupsearch.types.untag_resource_response


class BackupSearchClientConfig(TypedDict, total=False):
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


class BackupSearchClient:
    """A client for the ``BackupSearch`` service.

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
        self.config = BackupSearchClientConfig(
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
        # resources
        self.search_job = SearchJob(self)
        self.search_result_export_job = SearchResultExportJob(self)

    def operation_options(
        self, config_overrides: Optional[BackupSearchClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BackupSearchClientConfig = config_overrides or {}
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

    def list_search_job_backups(
        self,
        search_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_backupsearch.types.list_search_job_backups_output.ListSearchJobBackupsOutput":
        """<p>This operation returns a list of all backups (recovery points) in a paginated format that were included in the search job.</p> <p>If a search does not display an expected backup in the results, you can call this operation to display each backup included in the search. Any backups that were not included because they have a <code>FAILED</code> status from a permissions issue will be displayed, along with a status message.</p> <p>Only recovery points with a backup index that has a status of <code>ACTIVE</code> will be included in search results. If the index has any other status, its status will be displayed along with a status message.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            next_token: <p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backupsearch.types.list_search_job_backups_input.ListSearchJobBackupsInput]",
        ) -> OperationResponse[
            "aws_sdk_backupsearch.types.list_search_job_backups_output.ListSearchJobBackupsOutput"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.list_search_job_backups

            output, http_response = (
                aws_sdk_backupsearch._operations.cryo_backup_search_service.list_search_job_backups.list_search_job_backups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_backupsearch.types.list_search_job_backups_input.ListSearchJobBackupsInput = {}  # type: ignore[typeddict-item]
        input["search_job_identifier"] = search_job_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_search_job_backups(
        self,
        search_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[aws_sdk_backupsearch.types.search_job_backups_result.SearchJobBackupsResult]":
        _token = next_token
        while True:
            _response = self.list_search_job_backups(
                search_job_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_search_job_results(
        self,
        search_job_identifier: "aws_sdk_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_backupsearch.types.list_search_job_results_output.ListSearchJobResultsOutput":
        """<p>This operation returns a list of a specified search job.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            next_token: <p>The next item following a partial list of returned search job results.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of search job results, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backupsearch.types.list_search_job_results_input.ListSearchJobResultsInput]",
        ) -> OperationResponse[
            "aws_sdk_backupsearch.types.list_search_job_results_output.ListSearchJobResultsOutput"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.list_search_job_results

            output, http_response = (
                aws_sdk_backupsearch._operations.cryo_backup_search_service.list_search_job_results.list_search_job_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_backupsearch.types.list_search_job_results_input.ListSearchJobResultsInput = {}  # type: ignore[typeddict-item]
        input["search_job_identifier"] = search_job_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
    ) -> "aws_sdk_backupsearch.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>This operation returns the tags for a resource type.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource.&gt;</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backupsearch.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_backupsearch.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_backupsearch._operations.cryo_backup_search_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_backupsearch.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: str,
        tags: "aws_sdk_backupsearch.types.tag_map.TagMap",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
    ) -> "aws_sdk_backupsearch.types.tag_resource_response.TagResourceResponse":
        """<p>This operation puts tags on the resource you indicate.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource.</p> <p>This is the resource that will have the indicated tags.</p>
            tags: <p>Required tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - = . _ : /. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backupsearch.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_backupsearch.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.tag_resource

            output, http_response = (
                aws_sdk_backupsearch._operations.cryo_backup_search_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_backupsearch.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: str,
        tag_keys: "aws_sdk_backupsearch.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
    ) -> "aws_sdk_backupsearch.types.untag_resource_response.UntagResourceResponse":
        """<p>This operation removes tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource where you want to remove tags.</p>
            tag_keys: <p>This required parameter contains the tag keys you want to remove from the source.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backupsearch.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_backupsearch.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_backupsearch._operations.cryo_backup_search_service.untag_resource

            output, http_response = (
                aws_sdk_backupsearch._operations.cryo_backup_search_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_backupsearch.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
