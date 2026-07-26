"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#AmazonMWAAServerless``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_mwaa_serverless._auth._signers
import capo_mwaa_serverless._auth._sigv4
from capo_mwaa_serverless._auth._identity import Credentials
from capo_mwaa_serverless._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mwaa_serverless._auth._zapros_handler import AuthMiddleware
from capo_mwaa_serverless._resources.amazon_mwaa_serverless.task_instance_resource import (
    AsyncTaskInstanceResource,
)
from capo_mwaa_serverless._resources.amazon_mwaa_serverless.workflow_resource import (
    AsyncWorkflowResource,
)
from capo_mwaa_serverless._resources.amazon_mwaa_serverless.workflow_run_resource import (
    AsyncWorkflowRunResource,
)
from capo_mwaa_serverless._resources.amazon_mwaa_serverless.workflow_version_resource import (
    AsyncWorkflowVersionResource,
)
from capo_mwaa_serverless._services._aws_config import aaws_config
from capo_mwaa_serverless._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.list_tags_for_resource_request
    import capo_mwaa_serverless.types.list_tags_for_resource_response
    import capo_mwaa_serverless.types.tag_keys
    import capo_mwaa_serverless.types.tag_resource_request
    import capo_mwaa_serverless.types.tag_resource_response
    import capo_mwaa_serverless.types.taggable_resource_arn
    import capo_mwaa_serverless.types.tags
    import capo_mwaa_serverless.types.untag_resource_request
    import capo_mwaa_serverless.types.untag_resource_response


class AsyncMWAAServerlessClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncMWAAServerlessClientConfig(
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

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> "capo_mwaa_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags that are associated with a specified Amazon Managed Workflows for Apache Airflow Serverless resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_mwaa_serverless.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> "capo_mwaa_serverless.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to an Amazon Managed Workflows for Apache Airflow Serverless resource. Tags are key-value pairs that help you organize and categorize your resources.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which to add tags.</p>
            tags: <p>A map of tags to add to the resource. Each tag consists of a key-value pair.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.tag_resource

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "capo_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_mwaa_serverless.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> "capo_mwaa_serverless.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from an Amazon Managed Workflows for Apache Airflow Serverless resource. This operation removes the specified tags from the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of tag keys to remove from the resource. Only the keys are required; the values are ignored.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.untag_resource

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mwaa_serverless.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
