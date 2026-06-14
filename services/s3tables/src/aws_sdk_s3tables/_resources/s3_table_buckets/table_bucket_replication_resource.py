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
    import aws_sdk_s3tables.types.delete_table_bucket_replication_request
    import aws_sdk_s3tables.types.get_table_bucket_replication_request
    import aws_sdk_s3tables.types.get_table_bucket_replication_response
    import aws_sdk_s3tables.types.put_table_bucket_replication_request
    import aws_sdk_s3tables.types.put_table_bucket_replication_response
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_bucket_replication_configuration
    import aws_sdk_s3tables.types.version_token
    from aws_sdk_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from aws_sdk_s3tables._services.s3_tables import (
        S3TablesClient,
        S3TablesClientConfig,
    )


class TableBucketReplicationResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def delete_table_bucket_replication(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        version_token: Optional[
            "aws_sdk_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Deletes the replication configuration for a table bucket. After deletion, new table updates will no longer be replicated to destination buckets, though existing replicated tables will remain in destination buckets.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            version_token: <p>A version token from a previous GetTableBucketReplication call. Use this token to ensure you're deleting the expected version of the configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.delete_table_bucket_replication_request.DeleteTableBucketReplicationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_replication

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_replication.delete_table_bucket_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.delete_table_bucket_replication_request.DeleteTableBucketReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn
        if version_token is not None:
            input_["version_token"] = version_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table_bucket_replication(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_bucket_replication_response.GetTableBucketReplicationResponse":
        """<p>Retrieves the replication configuration for a table bucket.This operation returns the IAM role, <code>versionToken</code>, and replication rules that define how tables in this bucket are replicated to other buckets.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_bucket_replication_request.GetTableBucketReplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_bucket_replication_response.GetTableBucketReplicationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_replication

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_replication.get_table_bucket_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.get_table_bucket_replication_request.GetTableBucketReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_table_bucket_replication(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        configuration: "aws_sdk_s3tables.types.table_bucket_replication_configuration.TableBucketReplicationConfiguration",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        version_token: Optional[
            "aws_sdk_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> "aws_sdk_s3tables.types.put_table_bucket_replication_response.PutTableBucketReplicationResponse":
        """<p>Creates or updates the replication configuration for a table bucket. This operation defines how tables in the source bucket are replicated to destination buckets. Replication helps ensure data availability and disaster recovery across regions or accounts.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:PutTableBucketReplication</code> permission to use this operation. The IAM role specified in the configuration must have permissions to read from the source bucket and write permissions to all destination buckets.</p> </li> <li> <p>You must also have the following permissions:</p> <ul> <li> <p> <code>s3tables:GetTable</code> permission on the source table.</p> </li> <li> <p> <code>s3tables:ListTables</code> permission on the bucket containing the table.</p> </li> <li> <p> <code>s3tables:CreateTable</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:CreateNamespace</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:GetTableMaintenanceConfig</code> permission for the source bucket.</p> </li> <li> <p> <code>s3tables:PutTableMaintenanceConfig</code> permission for the destination bucket.</p> </li> </ul> </li> <li> <p>You must have <code>iam:PassRole</code> permission with condition allowing roles to be passed to <code>replication.s3tables.amazonaws.com</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the source table bucket.</p>
            version_token: <p>A version token from a previous GetTableBucketReplication call. Use this token to ensure you're updating the expected version of the configuration.</p>
            configuration: <p>The replication configuration to apply, including the IAM role and replication rules.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.put_table_bucket_replication_request.PutTableBucketReplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.put_table_bucket_replication_response.PutTableBucketReplicationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_replication

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_replication.put_table_bucket_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.put_table_bucket_replication_request.PutTableBucketReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn
        if version_token is not None:
            input_["version_token"] = version_token
        input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTableBucketReplicationResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def delete_table_bucket_replication(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        version_token: Optional[
            "aws_sdk_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Deletes the replication configuration for a table bucket. After deletion, new table updates will no longer be replicated to destination buckets, though existing replicated tables will remain in destination buckets.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTableBucketReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            version_token: <p>A version token from a previous GetTableBucketReplication call. Use this token to ensure you're deleting the expected version of the configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.delete_table_bucket_replication_request.DeleteTableBucketReplicationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_replication

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.delete_table_bucket_replication.async_delete_table_bucket_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.delete_table_bucket_replication_request.DeleteTableBucketReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn
        if version_token is not None:
            input_["version_token"] = version_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_bucket_replication(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_bucket_replication_response.GetTableBucketReplicationResponse":
        """<p>Retrieves the replication configuration for a table bucket.This operation returns the IAM role, <code>versionToken</code>, and replication rules that define how tables in this bucket are replicated to other buckets.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableBucketReplication</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_bucket_replication_request.GetTableBucketReplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_bucket_replication_response.GetTableBucketReplicationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_replication

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table_bucket_replication.async_get_table_bucket_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.get_table_bucket_replication_request.GetTableBucketReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_table_bucket_replication(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        configuration: "aws_sdk_s3tables.types.table_bucket_replication_configuration.TableBucketReplicationConfiguration",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        version_token: Optional[
            "aws_sdk_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> "aws_sdk_s3tables.types.put_table_bucket_replication_response.PutTableBucketReplicationResponse":
        """<p>Creates or updates the replication configuration for a table bucket. This operation defines how tables in the source bucket are replicated to destination buckets. Replication helps ensure data availability and disaster recovery across regions or accounts.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:PutTableBucketReplication</code> permission to use this operation. The IAM role specified in the configuration must have permissions to read from the source bucket and write permissions to all destination buckets.</p> </li> <li> <p>You must also have the following permissions:</p> <ul> <li> <p> <code>s3tables:GetTable</code> permission on the source table.</p> </li> <li> <p> <code>s3tables:ListTables</code> permission on the bucket containing the table.</p> </li> <li> <p> <code>s3tables:CreateTable</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:CreateNamespace</code> permission for the destination.</p> </li> <li> <p> <code>s3tables:GetTableMaintenanceConfig</code> permission for the source bucket.</p> </li> <li> <p> <code>s3tables:PutTableMaintenanceConfig</code> permission for the destination bucket.</p> </li> </ul> </li> <li> <p>You must have <code>iam:PassRole</code> permission with condition allowing roles to be passed to <code>replication.s3tables.amazonaws.com</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the source table bucket.</p>
            version_token: <p>A version token from a previous GetTableBucketReplication call. Use this token to ensure you're updating the expected version of the configuration.</p>
            configuration: <p>The replication configuration to apply, including the IAM role and replication rules.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.put_table_bucket_replication_request.PutTableBucketReplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.put_table_bucket_replication_response.PutTableBucketReplicationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_replication

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.put_table_bucket_replication.async_put_table_bucket_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_s3tables.types.put_table_bucket_replication_request.PutTableBucketReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["table_bucket_arn"] = table_bucket_arn
        if version_token is not None:
            input_["version_token"] = version_token
        input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
