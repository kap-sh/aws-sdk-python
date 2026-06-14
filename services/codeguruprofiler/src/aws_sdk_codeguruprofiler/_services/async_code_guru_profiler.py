"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#CodeGuruProfiler``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_codeguruprofiler._auth._signers
import aws_sdk_codeguruprofiler._auth._sigv4
from aws_sdk_codeguruprofiler._auth._identity import Credentials
from aws_sdk_codeguruprofiler._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_codeguruprofiler._auth._zapros_handler import AuthMiddleware
from aws_sdk_codeguruprofiler._resources.code_guru_profiler.profiling_group import (
    AsyncProfilingGroup,
)
from aws_sdk_codeguruprofiler._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.get_findings_report_account_summary_request
    import aws_sdk_codeguruprofiler.types.get_findings_report_account_summary_response
    import aws_sdk_codeguruprofiler.types.list_tags_for_resource_request
    import aws_sdk_codeguruprofiler.types.list_tags_for_resource_response
    import aws_sdk_codeguruprofiler.types.max_results
    import aws_sdk_codeguruprofiler.types.pagination_token
    import aws_sdk_codeguruprofiler.types.profiling_group_arn
    import aws_sdk_codeguruprofiler.types.tag_keys
    import aws_sdk_codeguruprofiler.types.tag_resource_request
    import aws_sdk_codeguruprofiler.types.tag_resource_response
    import aws_sdk_codeguruprofiler.types.tags_map
    import aws_sdk_codeguruprofiler.types.untag_resource_request
    import aws_sdk_codeguruprofiler.types.untag_resource_response


class AsyncCodeGuruProfilerClientConfig(TypedDict, total=False):
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


class AsyncCodeGuruProfilerClient:
    """A client for the ``CodeGuruProfiler`` service.

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
        self.config = AsyncCodeGuruProfilerClientConfig(
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
        self.profiling_group = AsyncProfilingGroup(self)

    def operation_options(
        self, config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCodeGuruProfilerClientConfig = config_overrides or {}
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

    async def get_findings_report_account_summary(
        self,
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_codeguruprofiler.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_codeguruprofiler.types.max_results.MaxResults"
        ] = None,
        daily_reports_only: Optional[bool] = None,
    ) -> "aws_sdk_codeguruprofiler.types.get_findings_report_account_summary_response.GetFindingsReportAccountSummaryResponse":
        """<p> Returns a list of <a href=\"https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FindingsReportSummary.html\"> <code>FindingsReportSummary</code> </a> objects that contain analysis results for all profiling groups in your AWS account. </p>

        Args:
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>GetFindingsReportAccountSummary</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of results returned by <code> GetFindingsReportAccountSummary</code> in paginated output. When this parameter is used, <code>GetFindingsReportAccountSummary</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>GetFindingsReportAccountSummary</code> request with the returned <code>nextToken</code> value.</p>
            daily_reports_only: <p>A <code>Boolean</code> value indicating whether to only return reports from daily profiles. If set to <code>True</code>, only analysis data from daily profiles is returned. If set to <code>False</code>, analysis data is returned from smaller time windows (for example, one hour).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codeguruprofiler.types.get_findings_report_account_summary_request.GetFindingsReportAccountSummaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codeguruprofiler.types.get_findings_report_account_summary_response.GetFindingsReportAccountSummaryResponse"
        ]:
            import aws_sdk_codeguruprofiler._operations.code_guru_profiler.get_findings_report_account_summary

            (
                output,
                http_response,
            ) = await aws_sdk_codeguruprofiler._operations.code_guru_profiler.get_findings_report_account_summary.async_get_findings_report_account_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codeguruprofiler.types.get_findings_report_account_summary_request.GetFindingsReportAccountSummaryRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if daily_reports_only is not None:
            input_["daily_reports_only"] = daily_reports_only

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "aws_sdk_codeguruprofiler.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Returns a list of the tags that are assigned to a specified resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that contains the tags to return. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codeguruprofiler.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codeguruprofiler.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_codeguruprofiler._operations.code_guru_profiler.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_codeguruprofiler._operations.code_guru_profiler.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codeguruprofiler.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn",
        tags: "aws_sdk_codeguruprofiler.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "aws_sdk_codeguruprofiler.types.tag_resource_response.TagResourceResponse":
        """<p> Use to assign one or more tags to a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that the tags are added to. </p>
            tags: <p> The list of tags that are added to the specified resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codeguruprofiler.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codeguruprofiler.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_codeguruprofiler._operations.code_guru_profiler.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_codeguruprofiler._operations.code_guru_profiler.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codeguruprofiler.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn",
        tag_keys: "aws_sdk_codeguruprofiler.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "aws_sdk_codeguruprofiler.types.untag_resource_response.UntagResourceResponse":
        """<p> Use to remove one or more tags from a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that contains the tags to remove. </p>
            tag_keys: <p> A list of tag keys. Existing tags of resources with keys in this list are removed from the specified resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codeguruprofiler.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codeguruprofiler.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_codeguruprofiler._operations.code_guru_profiler.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_codeguruprofiler._operations.code_guru_profiler.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codeguruprofiler.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
