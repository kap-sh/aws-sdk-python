"""Generated from Smithy shape ``com.amazonaws.s3tables#S3TableBuckets``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_s3tables._auth._signers
import aws_sdk_s3tables._auth._sigv4
from aws_sdk_s3tables._auth._identity import Credentials
from aws_sdk_s3tables._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_s3tables._auth._zapros_handler import AuthMiddleware
from aws_sdk_s3tables._resources.s3_table_buckets.namespace_resource import (
    NamespaceResource,
)
from aws_sdk_s3tables._resources.s3_table_buckets.table_bucket_encryption_resource import (
    TableBucketEncryptionResource,
)
from aws_sdk_s3tables._resources.s3_table_buckets.table_bucket_policy_resource import (
    TableBucketPolicyResource,
)
from aws_sdk_s3tables._resources.s3_table_buckets.table_bucket_replication_resource import (
    TableBucketReplicationResource,
)
from aws_sdk_s3tables._resources.s3_table_buckets.table_bucket_resource import (
    TableBucketResource,
)
from aws_sdk_s3tables._resources.s3_table_buckets.table_encryption_resource import (
    TableEncryptionResource,
)
from aws_sdk_s3tables._resources.s3_table_buckets.table_policy_resource import (
    TablePolicyResource,
)
from aws_sdk_s3tables._resources.s3_table_buckets.table_replication_resource import (
    TableReplicationResource,
)
from aws_sdk_s3tables._resources.s3_table_buckets.table_resource import TableResource
from aws_sdk_s3tables._services._aws_config import aws_config
from aws_sdk_s3tables._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.list_tags_for_resource_request
    import aws_sdk_s3tables.types.list_tags_for_resource_response
    import aws_sdk_s3tables.types.resource_arn
    import aws_sdk_s3tables.types.tag_key_list
    import aws_sdk_s3tables.types.tag_resource_request
    import aws_sdk_s3tables.types.tag_resource_response
    import aws_sdk_s3tables.types.tags
    import aws_sdk_s3tables.types.untag_resource_request
    import aws_sdk_s3tables.types.untag_resource_response


class S3TablesClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class S3TablesClient:
    """A client for the ``S3Tables`` service.

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
        self._config = S3TablesClientConfig(
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
        self.namespace_resource = NamespaceResource(self)
        self.table_bucket_encryption_resource = TableBucketEncryptionResource(self)
        self.table_bucket_policy_resource = TableBucketPolicyResource(self)
        self.table_bucket_replication_resource = TableBucketReplicationResource(self)
        self.table_bucket_resource = TableBucketResource(self)
        self.table_encryption_resource = TableEncryptionResource(self)
        self.table_policy_resource = TablePolicyResource(self)
        self.table_replication_resource = TableReplicationResource(self)
        self.table_resource = TableResource(self)

    def operation_options(
        self, config_overrides: Optional[S3TablesClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: S3TablesClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_s3tables.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        r"""<p>Lists all of the tags applied to a specified Amazon S3 Tables resource. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to resources. </p> <note> <p>For a list of S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For tables and table buckets, you must have the <code>s3tables:ListTagsForResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Tables resource that you want to list tags for. The tagged resource can be a table bucket or a table. For a list of all S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.list_tags_for_resource

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_s3tables.types.resource_arn.ResourceArn",
        tags: "aws_sdk_s3tables.types.tags.Tags",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.tag_resource_response.TagResourceResponse":
        r"""<p>Applies one or more user-defined tags to an Amazon S3 Tables resource or updates existing tags. Each tag is a label consisting of a key and value pair. Tags can help you organize, track costs for, and control access to your resources. You can add up to 50 tags for each S3 resource. </p> <note> <p>For a list of S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For tables and table buckets, you must have the <code>s3tables:TagResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Tables resource that you're applying tags to. The tagged resource can be a table bucket or a table. For a list of all S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p>
            tags: <p>The user-defined tag that you want to add to the specified S3 Tables resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.tag_resource

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_s3tables.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_s3tables.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.untag_resource_response.UntagResourceResponse":
        r"""<p>Removes the specified user-defined tags from an Amazon S3 Tables resource. You can pass one or more tag keys. </p> <note> <p>For a list of S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p> </note> <dl> <dt>Permissions</dt> <dd> <p>For tables and table buckets, you must have the <code>s3tables:UntagResource</code> permission to use this operation.</p> </dd> </dl>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon S3 Tables resource that you're removing tags from. The tagged resource can be a table bucket or a table. For a list of all S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p>
            tag_keys: <p>The array of tag keys that you're removing from the S3 Tables resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.untag_resource

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
