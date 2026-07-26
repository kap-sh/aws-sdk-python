"""Generated from Smithy shape ``com.amazonaws.backupsearch#CryoBackupSearchService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_backupsearch._auth._signers
import capo_backupsearch._auth._sigv4
from capo_backupsearch._auth._identity import Credentials
from capo_backupsearch._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_backupsearch._auth._zapros_handler import AuthMiddleware
from capo_backupsearch._pagination import resolve_path as _resolve_path
from capo_backupsearch._resources.cryo_backup_search_service.search_job import (
    AsyncSearchJob,
)
from capo_backupsearch._resources.cryo_backup_search_service.search_result_export_job import (
    AsyncSearchResultExportJob,
)
from capo_backupsearch._services._aws_config import aaws_config
from capo_backupsearch._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_backupsearch.types.generic_id
    import capo_backupsearch.types.list_search_job_backups_input
    import capo_backupsearch.types.list_search_job_backups_output
    import capo_backupsearch.types.list_search_job_results_input
    import capo_backupsearch.types.list_search_job_results_output
    import capo_backupsearch.types.list_tags_for_resource_request
    import capo_backupsearch.types.list_tags_for_resource_response
    import capo_backupsearch.types.search_job_backups_result
    import capo_backupsearch.types.tag_keys
    import capo_backupsearch.types.tag_map
    import capo_backupsearch.types.tag_resource_request
    import capo_backupsearch.types.tag_resource_response
    import capo_backupsearch.types.untag_resource_request
    import capo_backupsearch.types.untag_resource_response


class AsyncBackupSearchClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncBackupSearchClient:
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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncBackupSearchClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.search_job = AsyncSearchJob(self)
        self.search_result_export_job = AsyncSearchResultExportJob(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBackupSearchClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBackupSearchClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def list_search_job_backups(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_backupsearch.types.list_search_job_backups_output.ListSearchJobBackupsOutput":
        """<p>This operation returns a list of all backups (recovery points) in a paginated format that were included in the search job.</p> <p>If a search does not display an expected backup in the results, you can call this operation to display each backup included in the search. Any backups that were not included because they have a <code>FAILED</code> status from a permissions issue will be displayed, along with a status message.</p> <p>Only recovery points with a backup index that has a status of <code>ACTIVE</code> will be included in search results. If the index has any other status, its status will be displayed along with a status message.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            next_token: <p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.list_search_job_backups_input.ListSearchJobBackupsInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.list_search_job_backups_output.ListSearchJobBackupsOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_search_job_backups

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.list_search_job_backups.async_list_search_job_backups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.list_search_job_backups_input.ListSearchJobBackupsInput = {}  # type: ignore[typeddict-item]
        input_["search_job_identifier"] = search_job_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_search_job_backups(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_backupsearch.types.search_job_backups_result.SearchJobBackupsResult]":
        _token = next_token
        while True:
            _response = await self.list_search_job_backups(
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

    async def list_search_job_results(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_backupsearch.types.list_search_job_results_output.ListSearchJobResultsOutput":
        """<p>This operation returns a list of a specified search job.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            next_token: <p>The next item following a partial list of returned search job results.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of search job results, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.list_search_job_results_input.ListSearchJobResultsInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.list_search_job_results_output.ListSearchJobResultsOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_search_job_results

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.list_search_job_results.async_list_search_job_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.list_search_job_results_input.ListSearchJobResultsInput = {}  # type: ignore[typeddict-item]
        input_["search_job_identifier"] = search_job_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>This operation returns the tags for a resource type.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource.&gt;</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_backupsearch.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.tag_resource_response.TagResourceResponse":
        """<p>This operation puts tags on the resource you indicate.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource.</p> <p>This is the resource that will have the indicated tags.</p>
            tags: <p>Required tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - = . _ : /. </p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: str,
        tag_keys: "capo_backupsearch.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.untag_resource_response.UntagResourceResponse":
        """<p>This operation removes tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource where you want to remove tags.</p>
            tag_keys: <p>This required parameter contains the tag keys you want to remove from the source.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
