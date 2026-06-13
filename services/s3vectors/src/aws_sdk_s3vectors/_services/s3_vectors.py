"""Generated from Smithy shape ``com.amazonaws.s3vectors#S3Vectors``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_s3vectors._auth._signers
import aws_sdk_s3vectors._auth._sigv4
from aws_sdk_s3vectors._auth._identity import Credentials
from aws_sdk_s3vectors._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_s3vectors._auth._zapros_handler import AuthMiddleware
from aws_sdk_s3vectors._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.list_tags_for_resource_input
    import aws_sdk_s3vectors.types.list_tags_for_resource_output
    import aws_sdk_s3vectors.types.resource_arn
    import aws_sdk_s3vectors.types.tag_key_list
    import aws_sdk_s3vectors.types.tag_resource_input
    import aws_sdk_s3vectors.types.tag_resource_output
    import aws_sdk_s3vectors.types.tags_map
    import aws_sdk_s3vectors.types.untag_resource_input
    import aws_sdk_s3vectors.types.untag_resource_output


class S3VectorsClientConfig(TypedDict, total=False):
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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = S3VectorsClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[S3VectorsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: S3VectorsClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_s3vectors.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
    ) -> "aws_sdk_s3vectors.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists all of the tags applied to a specified Amazon S3 Vectors resource. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to resources. </p> <note> <p>For a list of S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For vector buckets and vector indexes, you must have the <code>s3vectors:ListTagsForResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you want to list tags for. The tagged resource can be a vector bucket or a vector index. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3vectors.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_s3vectors.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_s3vectors._operations.s3_vectors.list_tags_for_resource

            output, http_response = (
                aws_sdk_s3vectors._operations.s3_vectors.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_s3vectors.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_s3vectors.types.resource_arn.ResourceARN",
        tags: "aws_sdk_s3vectors.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
    ) -> "aws_sdk_s3vectors.types.tag_resource_output.TagResourceOutput":
        """<p>Applies one or more user-defined tags to an Amazon S3 Vectors resource or updates existing tags. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to your resources. You can add up to 50 tags for each resource.</p> <note> <p>For a list of S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For vector buckets and vector indexes, you must have the <code>s3vectors:TagResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you're applying tags to. The tagged resource can be a vector bucket or a vector index. </p>
            tags: <p>The user-defined tag that you want to add to the specified S3 Vectors resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3vectors.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_s3vectors.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_s3vectors._operations.s3_vectors.tag_resource

            output, http_response = (
                aws_sdk_s3vectors._operations.s3_vectors.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_s3vectors.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_s3vectors.types.resource_arn.ResourceARN",
        tag_keys: "aws_sdk_s3vectors.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[S3VectorsClientConfig] = None,
    ) -> "aws_sdk_s3vectors.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes the specified user-defined tags from an Amazon S3 Vectors resource. You can pass one or more tag keys. </p> <note> <p>For a list of S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For vector buckets and vector indexes, you must have the <code>s3vectors:UntagResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Vectors resource that you're removing tags from. The tagged resource can be a vector bucket or a vector index. </p>
            tag_keys: <p>The array of tag keys that you're removing from the S3 Vectors resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3vectors.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_s3vectors.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_s3vectors._operations.s3_vectors.untag_resource

            output, http_response = (
                aws_sdk_s3vectors._operations.s3_vectors.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_s3vectors.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
