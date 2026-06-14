"""Generated from Smithy shape ``com.amazonaws.omics#Omics``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_omics._auth._signers
import aws_sdk_omics._auth._sigv4
from aws_sdk_omics._auth._identity import Credentials
from aws_sdk_omics._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_omics._auth._zapros_handler import AuthMiddleware
from aws_sdk_omics._resources.omics.annotation_import_job import AnnotationImportJob
from aws_sdk_omics._resources.omics.annotation_store import AnnotationStore
from aws_sdk_omics._resources.omics.annotation_store_version import (
    AnnotationStoreVersion,
)
from aws_sdk_omics._resources.omics.configuration_resource import ConfigurationResource
from aws_sdk_omics._resources.omics.reference_store_resource import (
    ReferenceStoreResource,
)
from aws_sdk_omics._resources.omics.run_batch_resource import RunBatchResource
from aws_sdk_omics._resources.omics.run_cache_resource import RunCacheResource
from aws_sdk_omics._resources.omics.run_group_resource import RunGroupResource
from aws_sdk_omics._resources.omics.run_resource import RunResource
from aws_sdk_omics._resources.omics.sequence_store_resource import SequenceStoreResource
from aws_sdk_omics._resources.omics.share import Share
from aws_sdk_omics._resources.omics.tagging_resource import TaggingResource
from aws_sdk_omics._resources.omics.variant_import_job import VariantImportJob
from aws_sdk_omics._resources.omics.variant_store import VariantStore
from aws_sdk_omics._resources.omics.workflow_resource import WorkflowResource
from aws_sdk_omics._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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


class OmicsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class OmicsClient:
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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
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
        self._config = OmicsClientConfig(
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
        self.annotation_import_job = AnnotationImportJob(self)
        self.annotation_store = AnnotationStore(self)
        self.annotation_store_version = AnnotationStoreVersion(self)
        self.configuration_resource = ConfigurationResource(self)
        self.reference_store_resource = ReferenceStoreResource(self)
        self.run_batch_resource = RunBatchResource(self)
        self.run_cache_resource = RunCacheResource(self)
        self.run_group_resource = RunGroupResource(self)
        self.run_resource = RunResource(self)
        self.sequence_store_resource = SequenceStoreResource(self)
        self.share = Share(self)
        self.tagging_resource = TaggingResource(self)
        self.variant_import_job = VariantImportJob(self)
        self.variant_store = VariantStore(self)
        self.workflow_resource = WorkflowResource(self)

    def operation_options(
        self, config_overrides: Optional[OmicsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: OmicsClientConfig = config_overrides or {}
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

    def delete_s3_access_policy(
        self,
        s3_access_point_arn: "aws_sdk_omics.types.s3_access_point_arn.S3AccessPointArn",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.delete_s3_access_policy_response.DeleteS3AccessPolicyResponse":
        """<p>Deletes an access policy for the specified store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN that has the access policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.delete_s3_access_policy_request.DeleteS3AccessPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.delete_s3_access_policy_response.DeleteS3AccessPolicyResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_s3_access_policy

            output, http_response = (
                aws_sdk_omics._operations.omics.delete_s3_access_policy.delete_s3_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_s3_access_policy_request.DeleteS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["s3_access_point_arn"] = s3_access_point_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_s3_access_policy(
        self,
        s3_access_point_arn: "aws_sdk_omics.types.s3_access_point_arn.S3AccessPointArn",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_s3_access_policy_response.GetS3AccessPolicyResponse":
        """<p>Retrieves details about an access policy on a given store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN that has the access policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.get_s3_access_policy_request.GetS3AccessPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.get_s3_access_policy_response.GetS3AccessPolicyResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_s3_access_policy

            output, http_response = (
                aws_sdk_omics._operations.omics.get_s3_access_policy.get_s3_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_s3_access_policy_request.GetS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["s3_access_point_arn"] = s3_access_point_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_s3_access_policy(
        self,
        s3_access_point_arn: "aws_sdk_omics.types.s3_access_point_arn.S3AccessPointArn",
        s3_access_policy: "aws_sdk_omics.types.s3_access_policy.S3AccessPolicy",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.put_s3_access_policy_response.PutS3AccessPolicyResponse":
        """<p>Adds an access policy to the specified store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN where you want to put the access policy.</p>
            s3_access_policy: <p>The resource policy that controls S3 access to the store.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.put_s3_access_policy_request.PutS3AccessPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.put_s3_access_policy_response.PutS3AccessPolicyResponse"
        ]:
            import aws_sdk_omics._operations.omics.put_s3_access_policy

            output, http_response = (
                aws_sdk_omics._operations.omics.put_s3_access_policy.put_s3_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_omics.types.put_s3_access_policy_request.PutS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["s3_access_point_arn"] = s3_access_point_arn
        input_["s3_access_policy"] = s3_access_policy

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
