"""Generated from Smithy shape ``com.amazonaws.s3vectors#S3Vectors``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_s3vectors._auth._signers
import capo_s3vectors._auth._sigv4
from capo_s3vectors._auth._identity import Credentials
from capo_s3vectors._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_s3vectors._auth._zapros_handler import AuthMiddleware
from capo_s3vectors._resources.s3_vectors.vector_bucket_resource import (
    VectorBucketResource,
)
from capo_s3vectors._services._aws_config import aws_config
from capo_s3vectors._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_s3vectors.types.list_tags_for_resource_input
    import capo_s3vectors.types.list_tags_for_resource_output
    import capo_s3vectors.types.resource_arn
    import capo_s3vectors.types.tag_key_list
    import capo_s3vectors.types.tag_resource_input
    import capo_s3vectors.types.tag_resource_output
    import capo_s3vectors.types.tags_map
    import capo_s3vectors.types.untag_resource_input
    import capo_s3vectors.types.untag_resource_output


class S3VectorsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class S3VectorsClient:
    """A client for the ``S3Vectors`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = S3VectorsClientConfig(
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
        self.vector_bucket_resource = VectorBucketResource(self)

    def operation_options(
        self, config_overrides: Optional[S3VectorsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: S3VectorsClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_s3vectors.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
    ) -> "capo_s3vectors.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        r"""<p>Lists all of the tags applied to a specified Amazon S3 Vectors resource. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to resources. </p> <note> <p>For a list of S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For vector buckets and vector indexes, you must have the <code>s3vectors:ListTagsForResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you want to list tags for. The tagged resource can be a vector bucket or a vector index. </p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.list_tags_for_resource

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_s3vectors.types.resource_arn.ResourceARN",
        tags: "capo_s3vectors.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
    ) -> "capo_s3vectors.types.tag_resource_output.TagResourceOutput":
        r"""<p>Applies one or more user-defined tags to an Amazon S3 Vectors resource or updates existing tags. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to your resources. You can add up to 50 tags for each resource.</p> <note> <p>For a list of S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For vector buckets and vector indexes, you must have the <code>s3vectors:TagResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you're applying tags to. The tagged resource can be a vector bucket or a vector index. </p>
            tags: <p>The user-defined tag that you want to add to the specified S3 Vectors resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.conflict_exception.ConflictException: <p>The request failed because a vector bucket name or a vector index name already exists. Vector bucket names must be unique within your Amazon Web Services account for each Amazon Web Services Region. Vector index names must be unique within your vector bucket. Choose a different vector bucket name or vector index name, and try again.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.tag_resource

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_s3vectors.types.resource_arn.ResourceARN",
        tag_keys: "capo_s3vectors.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
    ) -> "capo_s3vectors.types.untag_resource_output.UntagResourceOutput":
        r"""<p>Removes the specified user-defined tags from an Amazon S3 Vectors resource. You can pass one or more tag keys. </p> <note> <p>For a list of S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For vector buckets and vector indexes, you must have the <code>s3vectors:UntagResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you're removing tags from. The tagged resource can be a vector bucket or a vector index. </p>
            tag_keys: <p>The array of tag keys that you're removing from the S3 Vectors resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>

        Raises:
            capo_s3vectors.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_s3vectors.errors.internal_server_exception.InternalServerException: <p>The request failed due to an internal server error.</p>
            capo_s3vectors.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out. Retry your request.</p>
            capo_s3vectors.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling.</p>
            capo_s3vectors.errors.validation_exception.ValidationException: <p>The requested action isn't valid.</p>
            capo_s3vectors.errors.conflict_exception.ConflictException: <p>The request failed because a vector bucket name or a vector index name already exists. Vector bucket names must be unique within your Amazon Web Services account for each Amazon Web Services Region. Vector index names must be unique within your vector bucket. Choose a different vector bucket name or vector index name, and try again.</p>
            capo_s3vectors.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource can't be found.</p>
            capo_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Wait briefly and retry your request. If it continues to fail, increase your waiting time between retries.</p>
            capo_s3vectors.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3vectors.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_s3vectors.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_s3vectors._operations.s3_vectors.untag_resource

            output, http_response = (
                capo_s3vectors._operations.s3_vectors.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3vectors.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
