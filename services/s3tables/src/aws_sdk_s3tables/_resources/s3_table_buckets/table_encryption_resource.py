from __future__ import annotations

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
    import aws_sdk_s3tables.types.get_table_encryption_request
    import aws_sdk_s3tables.types.get_table_encryption_response
    import aws_sdk_s3tables.types.namespace_name
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_name
    from aws_sdk_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from aws_sdk_s3tables._services.s3_tables import (
        S3TablesClient,
        S3TablesClientConfig,
    )


class TableEncryptionResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def get_table_encryption(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_encryption_response.GetTableEncryptionResponse":
        """<p>Gets the encryption configuration for a table.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket containing the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>

        Raises:
            aws_sdk_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            aws_sdk_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            aws_sdk_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            aws_sdk_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            aws_sdk_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            aws_sdk_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_encryption_request.GetTableEncryptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_encryption_response.GetTableEncryptionResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_encryption

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table_encryption.get_table_encryption(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.get_table_encryption_request.GetTableEncryptionRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn
        input_["namespace"] = namespace
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTableEncryptionResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def get_table_encryption(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_encryption_response.GetTableEncryptionResponse":
        """<p>Gets the encryption configuration for a table.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableEncryption</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket containing the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>

        Raises:
            aws_sdk_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            aws_sdk_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            aws_sdk_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            aws_sdk_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            aws_sdk_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            aws_sdk_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_encryption_request.GetTableEncryptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_encryption_response.GetTableEncryptionResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_encryption

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table_encryption.async_get_table_encryption(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.get_table_encryption_request.GetTableEncryptionRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn
        input_["namespace"] = namespace
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
