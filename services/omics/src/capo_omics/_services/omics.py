"""Generated from Smithy shape ``com.amazonaws.omics#Omics``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_omics._auth._signers
import capo_omics._auth._sigv4
from capo_omics._auth._identity import Credentials
from capo_omics._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_omics._auth._zapros_handler import AuthMiddleware
from capo_omics._resources.omics.annotation_import_job import AnnotationImportJob
from capo_omics._resources.omics.annotation_store import AnnotationStore
from capo_omics._resources.omics.annotation_store_version import AnnotationStoreVersion
from capo_omics._resources.omics.configuration_resource import ConfigurationResource
from capo_omics._resources.omics.reference_store_resource import ReferenceStoreResource
from capo_omics._resources.omics.run_batch_resource import RunBatchResource
from capo_omics._resources.omics.run_cache_resource import RunCacheResource
from capo_omics._resources.omics.run_group_resource import RunGroupResource
from capo_omics._resources.omics.run_resource import RunResource
from capo_omics._resources.omics.sequence_store_resource import SequenceStoreResource
from capo_omics._resources.omics.share import Share
from capo_omics._resources.omics.tagging_resource import TaggingResource
from capo_omics._resources.omics.variant_import_job import VariantImportJob
from capo_omics._resources.omics.variant_store import VariantStore
from capo_omics._resources.omics.workflow_resource import WorkflowResource
from capo_omics._services._aws_config import aws_config
from capo_omics._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_omics.types.delete_s3_access_policy_request
    import capo_omics.types.delete_s3_access_policy_response
    import capo_omics.types.get_s3_access_policy_request
    import capo_omics.types.get_s3_access_policy_response
    import capo_omics.types.put_s3_access_policy_request
    import capo_omics.types.put_s3_access_policy_response
    import capo_omics.types.s3_access_point_arn
    import capo_omics.types.s3_access_policy


class OmicsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = OmicsClientConfig(
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
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def delete_s3_access_policy(
        self,
        s3_access_point_arn: "capo_omics.types.s3_access_point_arn.S3AccessPointArn",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.delete_s3_access_policy_response.DeleteS3AccessPolicyResponse"
    ):
        """<p>Deletes an access policy for the specified store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN that has the access policy.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.delete_s3_access_policy_request.DeleteS3AccessPolicyRequest]",
        ) -> OperationResponse[
            "capo_omics.types.delete_s3_access_policy_response.DeleteS3AccessPolicyResponse"
        ]:
            import capo_omics._operations.omics.delete_s3_access_policy

            output, http_response = (
                capo_omics._operations.omics.delete_s3_access_policy.delete_s3_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.delete_s3_access_policy_request.DeleteS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["s3_access_point_arn"] = s3_access_point_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_s3_access_policy(
        self,
        s3_access_point_arn: "capo_omics.types.s3_access_point_arn.S3AccessPointArn",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.get_s3_access_policy_response.GetS3AccessPolicyResponse":
        """<p>Retrieves details about an access policy on a given store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN that has the access policy.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.get_s3_access_policy_request.GetS3AccessPolicyRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_s3_access_policy_response.GetS3AccessPolicyResponse"
        ]:
            import capo_omics._operations.omics.get_s3_access_policy

            output, http_response = (
                capo_omics._operations.omics.get_s3_access_policy.get_s3_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.get_s3_access_policy_request.GetS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["s3_access_point_arn"] = s3_access_point_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_s3_access_policy(
        self,
        s3_access_point_arn: "capo_omics.types.s3_access_point_arn.S3AccessPointArn",
        s3_access_policy: "capo_omics.types.s3_access_policy.S3AccessPolicy",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.put_s3_access_policy_response.PutS3AccessPolicyResponse":
        """<p>Adds an access policy to the specified store.</p>

        Args:
            s3_access_point_arn: <p>The S3 access point ARN where you want to put the access policy.</p>
            s3_access_policy: <p>The resource policy that controls S3 access to the store.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.put_s3_access_policy_request.PutS3AccessPolicyRequest]",
        ) -> OperationResponse[
            "capo_omics.types.put_s3_access_policy_response.PutS3AccessPolicyResponse"
        ]:
            import capo_omics._operations.omics.put_s3_access_policy

            output, http_response = (
                capo_omics._operations.omics.put_s3_access_policy.put_s3_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_omics.types.put_s3_access_policy_request.PutS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
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
