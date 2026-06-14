"""Generated from Smithy shape ``com.amazonaws.omics#Omics``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_omics._auth._signers
import aws_sdk_omics._auth._sigv4
from aws_sdk_omics._auth._identity import Credentials
from aws_sdk_omics._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_omics._auth._zapros_handler import AuthMiddleware
from aws_sdk_omics._resources.omics.annotation_import_job import (
    AsyncAnnotationImportJob,
)
from aws_sdk_omics._resources.omics.annotation_store import AsyncAnnotationStore
from aws_sdk_omics._resources.omics.annotation_store_version import (
    AsyncAnnotationStoreVersion,
)
from aws_sdk_omics._resources.omics.configuration_resource import (
    AsyncConfigurationResource,
)
from aws_sdk_omics._resources.omics.reference_store_resource import (
    AsyncReferenceStoreResource,
)
from aws_sdk_omics._resources.omics.run_batch_resource import AsyncRunBatchResource
from aws_sdk_omics._resources.omics.run_cache_resource import AsyncRunCacheResource
from aws_sdk_omics._resources.omics.run_group_resource import AsyncRunGroupResource
from aws_sdk_omics._resources.omics.run_resource import AsyncRunResource
from aws_sdk_omics._resources.omics.sequence_store_resource import (
    AsyncSequenceStoreResource,
)
from aws_sdk_omics._resources.omics.share import AsyncShare
from aws_sdk_omics._resources.omics.tagging_resource import AsyncTaggingResource
from aws_sdk_omics._resources.omics.variant_import_job import AsyncVariantImportJob
from aws_sdk_omics._resources.omics.variant_store import AsyncVariantStore
from aws_sdk_omics._resources.omics.workflow_resource import AsyncWorkflowResource
from aws_sdk_omics._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_omics.types.delete_s3_access_policy_request
    import aws_sdk_omics.types.delete_s3_access_policy_response
    import aws_sdk_omics.types.get_s3_access_policy_request
    import aws_sdk_omics.types.get_s3_access_policy_response
    import aws_sdk_omics.types.put_s3_access_policy_request
    import aws_sdk_omics.types.put_s3_access_policy_response
    import aws_sdk_omics.types.s3_access_point_arn
    import aws_sdk_omics.types.s3_access_policy


class AsyncOmicsClientConfig(TypedDict, total=False):
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


class AsyncOmicsClient:
    """A client for the ``Omics`` service.

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
        self.config = AsyncOmicsClientConfig(
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
        self.annotation_import_job = AsyncAnnotationImportJob(self)
        self.annotation_store = AsyncAnnotationStore(self)
        self.annotation_store_version = AsyncAnnotationStoreVersion(self)
        self.configuration_resource = AsyncConfigurationResource(self)
        self.reference_store_resource = AsyncReferenceStoreResource(self)
        self.run_batch_resource = AsyncRunBatchResource(self)
        self.run_cache_resource = AsyncRunCacheResource(self)
        self.run_group_resource = AsyncRunGroupResource(self)
        self.run_resource = AsyncRunResource(self)
        self.sequence_store_resource = AsyncSequenceStoreResource(self)
        self.share = AsyncShare(self)
        self.tagging_resource = AsyncTaggingResource(self)
        self.variant_import_job = AsyncVariantImportJob(self)
        self.variant_store = AsyncVariantStore(self)
        self.workflow_resource = AsyncWorkflowResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncOmicsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncOmicsClientConfig = config_overrides or {}
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

    async def delete_s3_access_policy(
        self,
        s3_access_point_arn: "aws_sdk_omics.types.s3_access_point_arn.S3AccessPointArn",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.delete_s3_access_policy_response.DeleteS3AccessPolicyResponse":
        """<p>Deletes an access policy for the specified store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN that has the access policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.delete_s3_access_policy_request.DeleteS3AccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.delete_s3_access_policy_response.DeleteS3AccessPolicyResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_s3_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.delete_s3_access_policy.async_delete_s3_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_s3_access_policy_request.DeleteS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["s3_access_point_arn"] = s3_access_point_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_s3_access_policy(
        self,
        s3_access_point_arn: "aws_sdk_omics.types.s3_access_point_arn.S3AccessPointArn",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_s3_access_policy_response.GetS3AccessPolicyResponse":
        """<p>Retrieves details about an access policy on a given store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN that has the access policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.get_s3_access_policy_request.GetS3AccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.get_s3_access_policy_response.GetS3AccessPolicyResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_s3_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.get_s3_access_policy.async_get_s3_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_s3_access_policy_request.GetS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["s3_access_point_arn"] = s3_access_point_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_s3_access_policy(
        self,
        s3_access_point_arn: "aws_sdk_omics.types.s3_access_point_arn.S3AccessPointArn",
        s3_access_policy: "aws_sdk_omics.types.s3_access_policy.S3AccessPolicy",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.put_s3_access_policy_response.PutS3AccessPolicyResponse":
        """<p>Adds an access policy to the specified store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN where you want to put the access policy.</p>
            s3_access_policy: <p>The resource policy that controls S3 access to the store.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.put_s3_access_policy_request.PutS3AccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.put_s3_access_policy_response.PutS3AccessPolicyResponse"
        ]:
            import aws_sdk_omics._operations.omics.put_s3_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.put_s3_access_policy.async_put_s3_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_omics.types.put_s3_access_policy_request.PutS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["s3_access_point_arn"] = s3_access_point_arn
        input_["s3_access_policy"] = s3_access_policy

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
