"""Generated from Smithy shape ``com.amazonaws.evs#AmazonElasticVMwareService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_evs._auth._signers
import aws_sdk_evs._auth._sigv4
from aws_sdk_evs._auth._identity import Credentials
from aws_sdk_evs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_evs._auth._zapros_handler import AuthMiddleware
from aws_sdk_evs._resources.amazon_elastic_v_mware_service.environment_resource import (
    AsyncEnvironmentResource,
)
from aws_sdk_evs._services._aws_config import aaws_config
from aws_sdk_evs._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_evs.types.arn
    import aws_sdk_evs.types.get_versions_request
    import aws_sdk_evs.types.get_versions_response
    import aws_sdk_evs.types.list_tags_for_resource_request
    import aws_sdk_evs.types.list_tags_for_resource_response
    import aws_sdk_evs.types.request_tag_map
    import aws_sdk_evs.types.tag_keys
    import aws_sdk_evs.types.tag_resource_request
    import aws_sdk_evs.types.tag_resource_response
    import aws_sdk_evs.types.untag_resource_request
    import aws_sdk_evs.types.untag_resource_response


class AsyncevsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncevsClient:
    """A client for the ``evs`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncevsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.environment_resource = AsyncEnvironmentResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncevsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncevsClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def get_versions(
        self, *, config_overrides: Optional[AsyncevsClientConfig] = None
    ) -> "aws_sdk_evs.types.get_versions_response.GetVersionsResponse":
        """<p>Returns information about VCF versions, ESX versions and EC2 instance types provided by Amazon EVS. For each VCF version, the response also includes the default ESX version and provided EC2 instance types.</p>

        Raises:
            aws_sdk_evs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_evs.errors.throttling_exception.ThrottlingException: <p>The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.</p>
            aws_sdk_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.get_versions_request.GetVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.get_versions_response.GetVersionsResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_versions

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.get_versions.async_get_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_evs.types.get_versions_request.GetVersionsRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_evs.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
    ) -> (
        "aws_sdk_evs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Lists the tags for an Amazon EVS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list tags for.</p>

        Raises:
            aws_sdk_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            aws_sdk_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_evs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_evs.types.arn.Arn",
        tags: "aws_sdk_evs.types.request_tag_map.RequestTagMap",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
    ) -> "aws_sdk_evs.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to an Amazon EVS resource with the specified <code>resourceArn</code>. If existing tags on a resource are not specified in the request parameters, they aren't changed. When a resource is deleted, the tags associated with that resource are also deleted. Tags that you create for Amazon EVS resources don't propagate to any other resources associated with the environment. For example, if you tag an environment with this operation, that tag doesn't automatically propagate to the VLAN subnets and hosts associated with the environment.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>
            tags: <p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other environment or Amazon Web Services resources.</p>

        Raises:
            aws_sdk_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            aws_sdk_evs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of one or more Amazon EVS resources exceeds the maximum allowed. For a list of Amazon EVS quotas, see <a href=\"https://docs.aws.amazon.com/evs/latest/userguide/service-quotas-evs.html\">Amazon EVS endpoints and quotas</a> in the <i>Amazon EVS User Guide</i>. Delete some resources or request an increase in your service quota. To request an increase, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html\">Amazon Web Services Service Quotas</a> in the <i>Amazon Web Services General Reference Guide</i>. </p>
            aws_sdk_evs.errors.tag_policy_exception.TagPolicyException: <note> <p> <code>TagPolicyException</code> is deprecated. See <a href=\"https://docs.aws.amazon.com/evs/latest/APIReference/API_ValidationException.html\"> <code>ValidationException</code> </a> instead.</p> </note> <p>The request doesn't comply with IAM tag policy. Correct your request and then retry it.</p>
            aws_sdk_evs.errors.too_many_tags_exception.TooManyTagsException: <note> <p> <code>TooManyTagsException</code> is deprecated. See <a href=\"https://docs.aws.amazon.com/evs/latest/APIReference/API_ServiceQuotaExceededException.html\"> <code>ServiceQuotaExceededException</code> </a> instead.</p> </note> <p>A service resource associated with the request has more than 200 tags.</p>
            aws_sdk_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_evs.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_evs.types.arn.Arn",
        tag_keys: "aws_sdk_evs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncevsClientConfig] = None,
    ) -> "aws_sdk_evs.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes specified tags from an Amazon EVS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to delete tags from.</p>
            tag_keys: <p>The keys of the tags to delete.</p>

        Raises:
            aws_sdk_evs.errors.resource_not_found_exception.ResourceNotFoundException: <p>A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a <code>state</code> of <code>DELETED</code>.</p>
            aws_sdk_evs.errors.tag_policy_exception.TagPolicyException: <note> <p> <code>TagPolicyException</code> is deprecated. See <a href=\"https://docs.aws.amazon.com/evs/latest/APIReference/API_ValidationException.html\"> <code>ValidationException</code> </a> instead.</p> </note> <p>The request doesn't comply with IAM tag policy. Correct your request and then retry it.</p>
            aws_sdk_evs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_evs.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_evs.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_evs._operations.amazon_elastic_v_mware_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_evs._operations.amazon_elastic_v_mware_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_evs.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
