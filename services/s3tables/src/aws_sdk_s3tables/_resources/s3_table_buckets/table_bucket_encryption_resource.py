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
    import aws_sdk_s3tables.types.delete_table_bucket_encryption_request
    import aws_sdk_s3tables.types.encryption_configuration
    import aws_sdk_s3tables.types.get_table_bucket_encryption_request
    import aws_sdk_s3tables.types.get_table_bucket_encryption_response
    import aws_sdk_s3tables.types.put_table_bucket_encryption_request
    import aws_sdk_s3tables.types.table_bucket_arn
    from aws_sdk_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from aws_sdk_s3tables._services.s3_tables import (
        S3TablesClient,
        S3TablesClientConfig,
    )


class TableBucketEncryptionResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def delete_table_bucket_encryption(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes the encryption configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.delete_table_bucket_encryption_request.DeleteTableBucketEncryptionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_encryption

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_encryption.delete_table_bucket_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.delete_table_bucket_encryption_request.DeleteTableBucketEncryptionRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table_bucket_encryption(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_bucket_encryption_response.GetTableBucketEncryptionResponse":
        """<p>Gets the encryption configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_bucket_encryption_request.GetTableBucketEncryptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_bucket_encryption_response.GetTableBucketEncryptionResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_encryption

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_encryption.get_table_bucket_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_bucket_encryption_request.GetTableBucketEncryptionRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_table_bucket_encryption(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        encryption_configuration: "aws_sdk_s3tables.types.encryption_configuration.EncryptionConfiguration",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets the encryption configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketEncryption</code> permission to use this operation.</p> <note> <p>If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html\">Permissions requirements for S3 Tables SSE-KMS encryption</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> </note> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            encryption_configuration: <p>The encryption configuration to apply to the table bucket.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.put_table_bucket_encryption_request.PutTableBucketEncryptionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_encryption

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_encryption.put_table_bucket_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.put_table_bucket_encryption_request.PutTableBucketEncryptionRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["encryption_configuration"] = encryption_configuration

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTableBucketEncryptionResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def delete_table_bucket_encryption(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes the encryption configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.delete_table_bucket_encryption_request.DeleteTableBucketEncryptionRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_encryption

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_encryption.async_delete_table_bucket_encryption(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.delete_table_bucket_encryption_request.DeleteTableBucketEncryptionRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_bucket_encryption(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_bucket_encryption_response.GetTableBucketEncryptionResponse":
        """<p>Gets the encryption configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_bucket_encryption_request.GetTableBucketEncryptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_bucket_encryption_response.GetTableBucketEncryptionResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_encryption

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_encryption.async_get_table_bucket_encryption(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_bucket_encryption_request.GetTableBucketEncryptionRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_table_bucket_encryption(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        encryption_configuration: "aws_sdk_s3tables.types.encryption_configuration.EncryptionConfiguration",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Sets the encryption configuration for a table bucket.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableBucketEncryption</code> permission to use this operation.</p> <note> <p>If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html\">Permissions requirements for S3 Tables SSE-KMS encryption</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> </note> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            encryption_configuration: <p>The encryption configuration to apply to the table bucket.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.put_table_bucket_encryption_request.PutTableBucketEncryptionRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_encryption

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_encryption.async_put_table_bucket_encryption(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.put_table_bucket_encryption_request.PutTableBucketEncryptionRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
