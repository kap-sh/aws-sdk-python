from typing import TYPE_CHECKING, Optional

import aws_sdk_s3tables._auth._signers
import aws_sdk_s3tables._auth._sigv4
from aws_sdk_s3tables._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.delete_table_bucket_policy_request
    import aws_sdk_s3tables.types.get_table_bucket_policy_request
    import aws_sdk_s3tables.types.get_table_bucket_policy_response
    import aws_sdk_s3tables.types.put_table_bucket_policy_request
    import aws_sdk_s3tables.types.resource_policy
    import aws_sdk_s3tables.types.table_bucket_arn
    from aws_sdk_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from aws_sdk_s3tables._services.s3_tables import (
        S3TablesClient,
        S3TablesClientConfig,
    )


class TableBucketPolicyResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def delete_table_bucket_policy(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes a table bucket policy. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-delete\">Deleting a table bucket policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.delete_table_bucket_policy_request.DeleteTableBucketPolicyRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_policy

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_policy.delete_table_bucket_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.delete_table_bucket_policy_request.DeleteTableBucketPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table_bucket_policy(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_bucket_policy_response.GetTableBucketPolicyResponse":
        """<p>Gets details about a table bucket policy. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-get\">Viewing a table bucket policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_bucket_policy_request.GetTableBucketPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_bucket_policy_response.GetTableBucketPolicyResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_policy

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_policy.get_table_bucket_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.get_table_bucket_policy_request.GetTableBucketPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_table_bucket_policy(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        resource_policy: "aws_sdk_s3tables.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new table bucket policy or replaces an existing table bucket policy for a table bucket. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-add\">Adding a table bucket policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            resource_policy: <p>The <code>JSON</code> that defines the policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.put_table_bucket_policy_request.PutTableBucketPolicyRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_policy

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_policy.put_table_bucket_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.put_table_bucket_policy_request.PutTableBucketPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn
        input_["resource_policy"] = resource_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTableBucketPolicyResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def delete_table_bucket_policy(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes a table bucket policy. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-delete\">Deleting a table bucket policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.delete_table_bucket_policy_request.DeleteTableBucketPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_policy

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_policy.async_delete_table_bucket_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.delete_table_bucket_policy_request.DeleteTableBucketPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_bucket_policy(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_bucket_policy_response.GetTableBucketPolicyResponse":
        """<p>Gets details about a table bucket policy. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-get\">Viewing a table bucket policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_bucket_policy_request.GetTableBucketPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_bucket_policy_response.GetTableBucketPolicyResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_policy

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_policy.async_get_table_bucket_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.get_table_bucket_policy_request.GetTableBucketPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_table_bucket_policy(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        resource_policy: "aws_sdk_s3tables.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new table bucket policy or replaces an existing table bucket policy for a table bucket. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-add\">Adding a table bucket policy</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketPolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            resource_policy: <p>The <code>JSON</code> that defines the policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.put_table_bucket_policy_request.PutTableBucketPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_policy

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_policy.async_put_table_bucket_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.put_table_bucket_policy_request.PutTableBucketPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn
        input_["resource_policy"] = resource_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
