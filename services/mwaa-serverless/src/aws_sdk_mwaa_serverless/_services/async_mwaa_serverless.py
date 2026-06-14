"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#AmazonMWAAServerless``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_mwaa_serverless._auth._signers
import aws_sdk_mwaa_serverless._auth._sigv4
from aws_sdk_mwaa_serverless._auth._identity import Credentials
from aws_sdk_mwaa_serverless._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_mwaa_serverless._auth._zapros_handler import AuthMiddleware
from aws_sdk_mwaa_serverless._resources.amazon_mwaa_serverless.task_instance_resource import (
    AsyncTaskInstanceResource,
)
from aws_sdk_mwaa_serverless._resources.amazon_mwaa_serverless.workflow_resource import (
    AsyncWorkflowResource,
)
from aws_sdk_mwaa_serverless._resources.amazon_mwaa_serverless.workflow_run_resource import (
    AsyncWorkflowRunResource,
)
from aws_sdk_mwaa_serverless._resources.amazon_mwaa_serverless.workflow_version_resource import (
    AsyncWorkflowVersionResource,
)
from aws_sdk_mwaa_serverless._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.list_tags_for_resource_request
    import aws_sdk_mwaa_serverless.types.list_tags_for_resource_response
    import aws_sdk_mwaa_serverless.types.tag_keys
    import aws_sdk_mwaa_serverless.types.tag_resource_request
    import aws_sdk_mwaa_serverless.types.tag_resource_response
    import aws_sdk_mwaa_serverless.types.taggable_resource_arn
    import aws_sdk_mwaa_serverless.types.tags
    import aws_sdk_mwaa_serverless.types.untag_resource_request
    import aws_sdk_mwaa_serverless.types.untag_resource_response


class AsyncMWAAServerlessClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
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


class AsyncMWAAServerlessClient:
    """A client for the ``MWAAServerless`` service.

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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncMWAAServerlessClientConfig(
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
        self.task_instance_resource = AsyncTaskInstanceResource(self)
        self.workflow_resource = AsyncWorkflowResource(self)
        self.workflow_run_resource = AsyncWorkflowRunResource(self)
        self.workflow_version_resource = AsyncWorkflowVersionResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMWAAServerlessClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> "aws_sdk_mwaa_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags that are associated with a specified Amazon Managed Workflows for Apache Airflow Serverless resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mwaa_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mwaa_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn",
        tags: "aws_sdk_mwaa_serverless.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> "aws_sdk_mwaa_serverless.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to an Amazon Managed Workflows for Apache Airflow Serverless resource. Tags are key-value pairs that help you organize and categorize your resources.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which to add tags.</p>
            tags: <p>A map of tags to add to the resource. Each tag consists of a key-value pair.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mwaa_serverless.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mwaa_serverless.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "aws_sdk_mwaa_serverless.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> "aws_sdk_mwaa_serverless.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from an Amazon Managed Workflows for Apache Airflow Serverless resource. This operation removes the specified tags from the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of tag keys to remove from the resource. Only the keys are required; the values are ignored.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mwaa_serverless.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mwaa_serverless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mwaa_serverless._operations.amazon_mwaa_serverless.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mwaa_serverless.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
