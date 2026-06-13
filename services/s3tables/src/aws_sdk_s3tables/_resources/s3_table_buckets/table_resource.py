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
    import aws_sdk_s3tables.types.create_table_request
    import aws_sdk_s3tables.types.create_table_response
    import aws_sdk_s3tables.types.delete_table_request
    import aws_sdk_s3tables.types.encryption_configuration
    import aws_sdk_s3tables.types.get_table_maintenance_configuration_request
    import aws_sdk_s3tables.types.get_table_maintenance_configuration_response
    import aws_sdk_s3tables.types.get_table_maintenance_job_status_request
    import aws_sdk_s3tables.types.get_table_maintenance_job_status_response
    import aws_sdk_s3tables.types.get_table_metadata_location_request
    import aws_sdk_s3tables.types.get_table_metadata_location_response
    import aws_sdk_s3tables.types.get_table_record_expiration_configuration_request
    import aws_sdk_s3tables.types.get_table_record_expiration_configuration_response
    import aws_sdk_s3tables.types.get_table_record_expiration_job_status_request
    import aws_sdk_s3tables.types.get_table_record_expiration_job_status_response
    import aws_sdk_s3tables.types.get_table_request
    import aws_sdk_s3tables.types.get_table_response
    import aws_sdk_s3tables.types.get_table_storage_class_request
    import aws_sdk_s3tables.types.get_table_storage_class_response
    import aws_sdk_s3tables.types.list_tables_limit
    import aws_sdk_s3tables.types.list_tables_request
    import aws_sdk_s3tables.types.list_tables_response
    import aws_sdk_s3tables.types.metadata_location
    import aws_sdk_s3tables.types.namespace_name
    import aws_sdk_s3tables.types.next_token
    import aws_sdk_s3tables.types.open_table_format
    import aws_sdk_s3tables.types.put_table_maintenance_configuration_request
    import aws_sdk_s3tables.types.put_table_record_expiration_configuration_request
    import aws_sdk_s3tables.types.rename_table_request
    import aws_sdk_s3tables.types.storage_class_configuration
    import aws_sdk_s3tables.types.table_arn
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_maintenance_configuration_value
    import aws_sdk_s3tables.types.table_maintenance_type
    import aws_sdk_s3tables.types.table_metadata
    import aws_sdk_s3tables.types.table_name
    import aws_sdk_s3tables.types.table_record_expiration_configuration_value
    import aws_sdk_s3tables.types.table_summary
    import aws_sdk_s3tables.types.tags
    import aws_sdk_s3tables.types.update_table_metadata_location_request
    import aws_sdk_s3tables.types.update_table_metadata_location_response
    import aws_sdk_s3tables.types.version_token
    from aws_sdk_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from aws_sdk_s3tables._services.s3_tables import (
        S3TablesClient,
        S3TablesClientConfig,
    )


class TableResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def create_table(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        format: "aws_sdk_s3tables.types.open_table_format.OpenTableFormat",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        metadata: Optional[
            "aws_sdk_s3tables.types.table_metadata.TableMetadata"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_s3tables.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        storage_class_configuration: Optional[
            "aws_sdk_s3tables.types.storage_class_configuration.StorageClassConfiguration"
        ] = None,
        tags: Optional["aws_sdk_s3tables.types.tags.Tags"] = None,
    ) -> "aws_sdk_s3tables.types.create_table_response.CreateTableResponse":
        """<p>Creates a new table associated with the given namespace in a table bucket. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-create.html\">Creating an Amazon S3 table</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:CreateTable</code> permission to use this operation. </p> </li> <li> <p>If you use this operation with the optional <code>metadata</code> request parameter you must have the <code>s3tables:PutTableData</code> permission. </p> </li> <li> <p>If you use this operation with the optional <code>encryptionConfiguration</code> request parameter you must have the <code>s3tables:PutTableEncryption</code> permission. </p> </li> <li> <p>If you use this operation with the <code>storageClassConfiguration</code> request parameter, you must have the <code>s3tables:PutTableStorageClass</code> permission.</p> </li> <li> <p>To create a table with tags, you must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission.</p> </li> </ul> <note> <p>Additionally, If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html\">Permissions requirements for S3 Tables SSE-KMS encryption</a>. </p> </note> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket to create the table in.</p>
            namespace: <p>The namespace to associated with the table.</p>
            name: <p>The name for the table.</p>
            format: <p>The format for the table.</p>
            metadata: <p>The metadata for the table.</p>
            encryption_configuration: <p>The encryption configuration to use for the table. This configuration specifies the encryption algorithm and, if using SSE-KMS, the KMS key to use for encrypting the table. </p> <note> <p>If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html\">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p> </note>
            storage_class_configuration: <p>The storage class configuration for the table. If not specified, the table inherits the storage class configuration from its table bucket. Specify this parameter to override the bucket's default storage class for this table.</p>
            tags: <p>A map of user-defined tags that you would like to apply to the table that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs for, and control access to resources. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission to create a table with tags.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.create_table_request.CreateTableRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.create_table_response.CreateTableResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.create_table

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.create_table.create_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.create_table_request.CreateTableRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name
        input["format"] = format
        if metadata is not None:
            input["metadata"] = metadata
        if encryption_configuration is not None:
            input["encryption_configuration"] = encryption_configuration
        if storage_class_configuration is not None:
            input["storage_class_configuration"] = storage_class_configuration
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_table(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        version_token: Optional[
            "aws_sdk_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Deletes a table. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-delete.html\">Deleting an Amazon S3 table</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>
            version_token: <p>The version token of the table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.delete_table_request.DeleteTableRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.delete_table

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.delete_table.delete_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.delete_table_request.DeleteTableRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name
        if version_token is not None:
            input["version_token"] = version_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table(
        self,
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        table_bucket_arn: Optional[
            "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
        ] = None,
        namespace: Optional[
            "aws_sdk_s3tables.types.namespace_name.NamespaceName"
        ] = None,
        name: Optional["aws_sdk_s3tables.types.table_name.TableName"] = None,
        table_arn: Optional["aws_sdk_s3tables.types.table_arn.TableARN"] = None,
    ) -> "aws_sdk_s3tables.types.get_table_response.GetTableResponse":
        """<p>Gets details about a table. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html\">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the table.</p>
            namespace: <p>The name of the namespace the table is associated with.</p>
            name: <p>The name of the table.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_request.GetTableRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_response.GetTableResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table.get_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_request.GetTableRequest = {}  # type: ignore[typeddict-item]
        if table_bucket_arn is not None:
            input["table_bucket_arn"] = table_bucket_arn
        if namespace is not None:
            input["namespace"] = namespace
        if name is not None:
            input["name"] = name
        if table_arn is not None:
            input["table_arn"] = table_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table_maintenance_configuration(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_maintenance_configuration_response.GetTableMaintenanceConfigurationResponse":
        """<p>Gets details about the maintenance configuration of a table. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html\">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:GetTableMaintenanceConfiguration</code> permission to use this operation. </p> </li> <li> <p>You must have the <code>s3tables:GetTableData</code> permission to use set the compaction strategy to <code>sort</code> or <code>zorder</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_maintenance_configuration_request.GetTableMaintenanceConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_maintenance_configuration_response.GetTableMaintenanceConfigurationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_maintenance_configuration

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table_maintenance_configuration.get_table_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_maintenance_configuration_request.GetTableMaintenanceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table_maintenance_job_status(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_maintenance_job_status_response.GetTableMaintenanceJobStatusResponse":
        """<p>Gets the status of a maintenance job for a table. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html\">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableMaintenanceJobStatus</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The name of the namespace the table is associated with. </p>
            name: <p>The name of the table containing the maintenance job status you want to check.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_maintenance_job_status_request.GetTableMaintenanceJobStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_maintenance_job_status_response.GetTableMaintenanceJobStatusResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_maintenance_job_status

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table_maintenance_job_status.get_table_maintenance_job_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_maintenance_job_status_request.GetTableMaintenanceJobStatusRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table_metadata_location(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_metadata_location_response.GetTableMetadataLocationResponse":
        """<p>Gets the location of the table metadata.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableMetadataLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_metadata_location_request.GetTableMetadataLocationRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_metadata_location_response.GetTableMetadataLocationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_metadata_location

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table_metadata_location.get_table_metadata_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_metadata_location_request.GetTableMetadataLocationRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table_record_expiration_configuration(
        self,
        table_arn: "aws_sdk_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_record_expiration_configuration_response.GetTableRecordExpirationConfigurationResponse":
        """<p>Retrieves the expiration configuration settings for records in a table, and the status of the configuration. If the status of the configuration is <code>enabled</code>, records expire and are automatically removed from the table after the specified number of days.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableRecordExpirationConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_record_expiration_configuration_request.GetTableRecordExpirationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_record_expiration_configuration_response.GetTableRecordExpirationConfigurationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_record_expiration_configuration

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table_record_expiration_configuration.get_table_record_expiration_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_record_expiration_configuration_request.GetTableRecordExpirationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["table_arn"] = table_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table_record_expiration_job_status(
        self,
        table_arn: "aws_sdk_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_record_expiration_job_status_response.GetTableRecordExpirationJobStatusResponse":
        """<p>Retrieves the status, metrics, and details of the latest record expiration job for a table. This includes when the job ran, and whether it succeeded or failed. If the job ran successfully, this also includes statistics about the records that were removed.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableRecordExpirationJobStatus</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_record_expiration_job_status_request.GetTableRecordExpirationJobStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_record_expiration_job_status_response.GetTableRecordExpirationJobStatusResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_record_expiration_job_status

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table_record_expiration_job_status.get_table_record_expiration_job_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_record_expiration_job_status_request.GetTableRecordExpirationJobStatusRequest = {}  # type: ignore[typeddict-item]
        input["table_arn"] = table_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_table_storage_class(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_storage_class_response.GetTableStorageClassResponse":
        """<p>Retrieves the storage class configuration for a specific table. This allows you to view the storage class settings that apply to an individual table, which may differ from the table bucket's default configuration.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.get_table_storage_class_request.GetTableStorageClassRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.get_table_storage_class_response.GetTableStorageClassResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_storage_class

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.get_table_storage_class.get_table_storage_class(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_storage_class_request.GetTableStorageClassRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tables(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        namespace: Optional[
            "aws_sdk_s3tables.types.namespace_name.NamespaceName"
        ] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional[
            "aws_sdk_s3tables.types.next_token.NextToken"
        ] = None,
        max_tables: Optional[
            "aws_sdk_s3tables.types.list_tables_limit.ListTablesLimit"
        ] = None,
    ) -> "aws_sdk_s3tables.types.list_tables_response.ListTablesResponse":
        """<p>List tables in the given table bucket. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html\">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListTables</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace of the tables.</p>
            prefix: <p>The prefix of the tables.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_tables: <p>The maximum number of tables to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.list_tables_request.ListTablesRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.list_tables_response.ListTablesResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.list_tables

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.list_tables.list_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.list_tables_request.ListTablesRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        if namespace is not None:
            input["namespace"] = namespace
        if prefix is not None:
            input["prefix"] = prefix
        if continuation_token is not None:
            input["continuation_token"] = continuation_token
        if max_tables is not None:
            input["max_tables"] = max_tables

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_table_maintenance_configuration(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        type: "aws_sdk_s3tables.types.table_maintenance_type.TableMaintenanceType",
        value: "aws_sdk_s3tables.types.table_maintenance_configuration_value.TableMaintenanceConfigurationValue",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new maintenance configuration or replaces an existing maintenance configuration for a table. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html\">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table associated with the maintenance configuration.</p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
            type: <p>The type of the maintenance configuration.</p>
            value: <p>Defines the values of the maintenance configuration for the table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.put_table_maintenance_configuration_request.PutTableMaintenanceConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.put_table_maintenance_configuration

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.put_table_maintenance_configuration.put_table_maintenance_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.put_table_maintenance_configuration_request.PutTableMaintenanceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name
        input["type"] = type
        input["value"] = value

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_table_record_expiration_configuration(
        self,
        table_arn: "aws_sdk_s3tables.types.table_arn.TableARN",
        value: "aws_sdk_s3tables.types.table_record_expiration_configuration_value.TableRecordExpirationConfigurationValue",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates or updates the expiration configuration settings for records in a table, including the status of the configuration. If you enable record expiration for a table, records expire and are automatically removed from the table after the number of days that you specify.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableRecordExpirationConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
            value: <p>The record expiration configuration to apply to the table, including the status (<code>enabled</code> or <code>disabled</code>) and retention period in days.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.put_table_record_expiration_configuration_request.PutTableRecordExpirationConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.put_table_record_expiration_configuration

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.put_table_record_expiration_configuration.put_table_record_expiration_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.put_table_record_expiration_configuration_request.PutTableRecordExpirationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["table_arn"] = table_arn
        input["value"] = value

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def rename_table(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        new_namespace_name: Optional[
            "aws_sdk_s3tables.types.namespace_name.NamespaceName"
        ] = None,
        new_name: Optional["aws_sdk_s3tables.types.table_name.TableName"] = None,
        version_token: Optional[
            "aws_sdk_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Renames a table or a namespace. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html\">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:RenameTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket. </p>
            namespace: <p>The namespace associated with the table. </p>
            name: <p>The current name of the table.</p>
            new_namespace_name: <p>The new name for the namespace.</p>
            new_name: <p>The new name for the table.</p>
            version_token: <p>The version token of the table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.rename_table_request.RenameTableRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.rename_table

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.rename_table.rename_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.rename_table_request.RenameTableRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name
        if new_namespace_name is not None:
            input["new_namespace_name"] = new_namespace_name
        if new_name is not None:
            input["new_name"] = new_name
        if version_token is not None:
            input["version_token"] = version_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_table_metadata_location(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        version_token: "aws_sdk_s3tables.types.version_token.VersionToken",
        metadata_location: "aws_sdk_s3tables.types.metadata_location.MetadataLocation",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.update_table_metadata_location_response.UpdateTableMetadataLocationResponse":
        """<p>Updates the metadata location for a table. The metadata location of a table must be an S3 URI that begins with the table's warehouse location. The metadata location for an Apache Iceberg table must end with <code>.metadata.json</code>, or if the metadata file is Gzip-compressed, <code>.metadata.json.gz</code>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:UpdateTableMetadataLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket. </p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
            version_token: <p>The version token of the table. </p>
            metadata_location: <p>The new metadata location for the table. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_s3tables.types.update_table_metadata_location_request.UpdateTableMetadataLocationRequest]",
        ) -> OperationResponse[
            "aws_sdk_s3tables.types.update_table_metadata_location_response.UpdateTableMetadataLocationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.update_table_metadata_location

            output, http_response = (
                aws_sdk_s3tables._operations.s3_table_buckets.update_table_metadata_location.update_table_metadata_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.update_table_metadata_location_request.UpdateTableMetadataLocationRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name
        input["version_token"] = version_token
        input["metadata_location"] = metadata_location

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTableResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def create_table(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        format: "aws_sdk_s3tables.types.open_table_format.OpenTableFormat",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        metadata: Optional[
            "aws_sdk_s3tables.types.table_metadata.TableMetadata"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_s3tables.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        storage_class_configuration: Optional[
            "aws_sdk_s3tables.types.storage_class_configuration.StorageClassConfiguration"
        ] = None,
        tags: Optional["aws_sdk_s3tables.types.tags.Tags"] = None,
    ) -> "aws_sdk_s3tables.types.create_table_response.CreateTableResponse":
        """<p>Creates a new table associated with the given namespace in a table bucket. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-create.html\">Creating an Amazon S3 table</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:CreateTable</code> permission to use this operation. </p> </li> <li> <p>If you use this operation with the optional <code>metadata</code> request parameter you must have the <code>s3tables:PutTableData</code> permission. </p> </li> <li> <p>If you use this operation with the optional <code>encryptionConfiguration</code> request parameter you must have the <code>s3tables:PutTableEncryption</code> permission. </p> </li> <li> <p>If you use this operation with the <code>storageClassConfiguration</code> request parameter, you must have the <code>s3tables:PutTableStorageClass</code> permission.</p> </li> <li> <p>To create a table with tags, you must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission.</p> </li> </ul> <note> <p>Additionally, If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html\">Permissions requirements for S3 Tables SSE-KMS encryption</a>. </p> </note> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket to create the table in.</p>
            namespace: <p>The namespace to associated with the table.</p>
            name: <p>The name for the table.</p>
            format: <p>The format for the table.</p>
            metadata: <p>The metadata for the table.</p>
            encryption_configuration: <p>The encryption configuration to use for the table. This configuration specifies the encryption algorithm and, if using SSE-KMS, the KMS key to use for encrypting the table. </p> <note> <p>If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html\">Permissions requirements for S3 Tables SSE-KMS encryption</a>.</p> </note>
            storage_class_configuration: <p>The storage class configuration for the table. If not specified, the table inherits the storage class configuration from its table bucket. Specify this parameter to override the bucket's default storage class for this table.</p>
            tags: <p>A map of user-defined tags that you would like to apply to the table that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs for, and control access to resources. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3tables:TagResource</code> permission in addition to <code>s3tables:CreateTable</code> permission to create a table with tags.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.create_table_request.CreateTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.create_table_response.CreateTableResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.create_table

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.create_table.async_create_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.create_table_request.CreateTableRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name
        input["format"] = format
        if metadata is not None:
            input["metadata"] = metadata
        if encryption_configuration is not None:
            input["encryption_configuration"] = encryption_configuration
        if storage_class_configuration is not None:
            input["storage_class_configuration"] = storage_class_configuration
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_table(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        version_token: Optional[
            "aws_sdk_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Deletes a table. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-delete.html\">Deleting an Amazon S3 table</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>
            version_token: <p>The version token of the table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.delete_table_request.DeleteTableRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.delete_table

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.delete_table.async_delete_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.delete_table_request.DeleteTableRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name
        if version_token is not None:
            input["version_token"] = version_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table(
        self,
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        table_bucket_arn: Optional[
            "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
        ] = None,
        namespace: Optional[
            "aws_sdk_s3tables.types.namespace_name.NamespaceName"
        ] = None,
        name: Optional["aws_sdk_s3tables.types.table_name.TableName"] = None,
        table_arn: Optional["aws_sdk_s3tables.types.table_arn.TableARN"] = None,
    ) -> "aws_sdk_s3tables.types.get_table_response.GetTableResponse":
        """<p>Gets details about a table. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html\">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the table.</p>
            namespace: <p>The name of the namespace the table is associated with.</p>
            name: <p>The name of the table.</p>
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_request.GetTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_response.GetTableResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table.async_get_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_request.GetTableRequest = {}  # type: ignore[typeddict-item]
        if table_bucket_arn is not None:
            input["table_bucket_arn"] = table_bucket_arn
        if namespace is not None:
            input["namespace"] = namespace
        if name is not None:
            input["name"] = name
        if table_arn is not None:
            input["table_arn"] = table_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_maintenance_configuration(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_maintenance_configuration_response.GetTableMaintenanceConfigurationResponse":
        """<p>Gets details about the maintenance configuration of a table. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html\">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <ul> <li> <p>You must have the <code>s3tables:GetTableMaintenanceConfiguration</code> permission to use this operation. </p> </li> <li> <p>You must have the <code>s3tables:GetTableData</code> permission to use set the compaction strategy to <code>sort</code> or <code>zorder</code>.</p> </li> </ul> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_maintenance_configuration_request.GetTableMaintenanceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_maintenance_configuration_response.GetTableMaintenanceConfigurationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_maintenance_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table_maintenance_configuration.async_get_table_maintenance_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_maintenance_configuration_request.GetTableMaintenanceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_maintenance_job_status(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_maintenance_job_status_response.GetTableMaintenanceJobStatusResponse":
        """<p>Gets the status of a maintenance job for a table. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html\">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableMaintenanceJobStatus</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The name of the namespace the table is associated with. </p>
            name: <p>The name of the table containing the maintenance job status you want to check.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_maintenance_job_status_request.GetTableMaintenanceJobStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_maintenance_job_status_response.GetTableMaintenanceJobStatusResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_maintenance_job_status

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table_maintenance_job_status.async_get_table_maintenance_job_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_maintenance_job_status_request.GetTableMaintenanceJobStatusRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_metadata_location(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_metadata_location_response.GetTableMetadataLocationResponse":
        """<p>Gets the location of the table metadata.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableMetadataLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_metadata_location_request.GetTableMetadataLocationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_metadata_location_response.GetTableMetadataLocationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_metadata_location

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table_metadata_location.async_get_table_metadata_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_metadata_location_request.GetTableMetadataLocationRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_record_expiration_configuration(
        self,
        table_arn: "aws_sdk_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_record_expiration_configuration_response.GetTableRecordExpirationConfigurationResponse":
        """<p>Retrieves the expiration configuration settings for records in a table, and the status of the configuration. If the status of the configuration is <code>enabled</code>, records expire and are automatically removed from the table after the specified number of days.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableRecordExpirationConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_record_expiration_configuration_request.GetTableRecordExpirationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_record_expiration_configuration_response.GetTableRecordExpirationConfigurationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_record_expiration_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table_record_expiration_configuration.async_get_table_record_expiration_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_record_expiration_configuration_request.GetTableRecordExpirationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["table_arn"] = table_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_record_expiration_job_status(
        self,
        table_arn: "aws_sdk_s3tables.types.table_arn.TableARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_record_expiration_job_status_response.GetTableRecordExpirationJobStatusResponse":
        """<p>Retrieves the status, metrics, and details of the latest record expiration job for a table. This includes when the job ran, and whether it succeeded or failed. If the job ran successfully, this also includes statistics about the records that were removed.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableRecordExpirationJobStatus</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_record_expiration_job_status_request.GetTableRecordExpirationJobStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_record_expiration_job_status_response.GetTableRecordExpirationJobStatusResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_record_expiration_job_status

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table_record_expiration_job_status.async_get_table_record_expiration_job_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_record_expiration_job_status_request.GetTableRecordExpirationJobStatusRequest = {}  # type: ignore[typeddict-item]
        input["table_arn"] = table_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_table_storage_class(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.get_table_storage_class_response.GetTableStorageClassResponse":
        """<p>Retrieves the storage class configuration for a specific table. This allows you to view the storage class settings that apply to an individual table, which may differ from the table bucket's default configuration.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetTableStorageClass</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket that contains the table.</p>
            namespace: <p>The namespace associated with the table.</p>
            name: <p>The name of the table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.get_table_storage_class_request.GetTableStorageClassRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.get_table_storage_class_response.GetTableStorageClassResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.get_table_storage_class

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.get_table_storage_class.async_get_table_storage_class(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.get_table_storage_class_request.GetTableStorageClassRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tables(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        namespace: Optional[
            "aws_sdk_s3tables.types.namespace_name.NamespaceName"
        ] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional[
            "aws_sdk_s3tables.types.next_token.NextToken"
        ] = None,
        max_tables: Optional[
            "aws_sdk_s3tables.types.list_tables_limit.ListTablesLimit"
        ] = None,
    ) -> "aws_sdk_s3tables.types.list_tables_response.ListTablesResponse":
        """<p>List tables in the given table bucket. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html\">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListTables</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon resource Name (ARN) of the table bucket.</p>
            namespace: <p>The namespace of the tables.</p>
            prefix: <p>The prefix of the tables.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_tables: <p>The maximum number of tables to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.list_tables_request.ListTablesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.list_tables_response.ListTablesResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.list_tables

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.list_tables.async_list_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.list_tables_request.ListTablesRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        if namespace is not None:
            input["namespace"] = namespace
        if prefix is not None:
            input["prefix"] = prefix
        if continuation_token is not None:
            input["continuation_token"] = continuation_token
        if max_tables is not None:
            input["max_tables"] = max_tables

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_table_maintenance_configuration(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        type: "aws_sdk_s3tables.types.table_maintenance_type.TableMaintenanceType",
        value: "aws_sdk_s3tables.types.table_maintenance_configuration_value.TableMaintenanceConfigurationValue",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates a new maintenance configuration or replaces an existing maintenance configuration for a table. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html\">S3 Tables maintenance</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableMaintenanceConfiguration</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table associated with the maintenance configuration.</p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
            type: <p>The type of the maintenance configuration.</p>
            value: <p>Defines the values of the maintenance configuration for the table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.put_table_maintenance_configuration_request.PutTableMaintenanceConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.put_table_maintenance_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.put_table_maintenance_configuration.async_put_table_maintenance_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.put_table_maintenance_configuration_request.PutTableMaintenanceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name
        input["type"] = type
        input["value"] = value

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_table_record_expiration_configuration(
        self,
        table_arn: "aws_sdk_s3tables.types.table_arn.TableARN",
        value: "aws_sdk_s3tables.types.table_record_expiration_configuration_value.TableRecordExpirationConfigurationValue",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Creates or updates the expiration configuration settings for records in a table, including the status of the configuration. If you enable record expiration for a table, records expire and are automatically removed from the table after the number of days that you specify.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:PutTableRecordExpirationConfiguration</code> permission to use this operation.</p> </dd> </dl>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) of the table.</p>
            value: <p>The record expiration configuration to apply to the table, including the status (<code>enabled</code> or <code>disabled</code>) and retention period in days.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.put_table_record_expiration_configuration_request.PutTableRecordExpirationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.put_table_record_expiration_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.put_table_record_expiration_configuration.async_put_table_record_expiration_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.put_table_record_expiration_configuration_request.PutTableRecordExpirationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["table_arn"] = table_arn
        input["value"] = value

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def rename_table(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        new_namespace_name: Optional[
            "aws_sdk_s3tables.types.namespace_name.NamespaceName"
        ] = None,
        new_name: Optional["aws_sdk_s3tables.types.table_name.TableName"] = None,
        version_token: Optional[
            "aws_sdk_s3tables.types.version_token.VersionToken"
        ] = None,
    ) -> None:
        """<p>Renames a table or a namespace. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-tables.html\">S3 Tables</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:RenameTable</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket. </p>
            namespace: <p>The namespace associated with the table. </p>
            name: <p>The current name of the table.</p>
            new_namespace_name: <p>The new name for the namespace.</p>
            new_name: <p>The new name for the table.</p>
            version_token: <p>The version token of the table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.rename_table_request.RenameTableRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_s3tables._operations.s3_table_buckets.rename_table

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.rename_table.async_rename_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.rename_table_request.RenameTableRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name
        if new_namespace_name is not None:
            input["new_namespace_name"] = new_namespace_name
        if new_name is not None:
            input["new_name"] = new_name
        if version_token is not None:
            input["version_token"] = version_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_table_metadata_location(
        self,
        table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName",
        name: "aws_sdk_s3tables.types.table_name.TableName",
        version_token: "aws_sdk_s3tables.types.version_token.VersionToken",
        metadata_location: "aws_sdk_s3tables.types.metadata_location.MetadataLocation",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "aws_sdk_s3tables.types.update_table_metadata_location_response.UpdateTableMetadataLocationResponse":
        """<p>Updates the metadata location for a table. The metadata location of a table must be an S3 URI that begins with the table's warehouse location. The metadata location for an Apache Iceberg table must end with <code>.metadata.json</code>, or if the metadata file is Gzip-compressed, <code>.metadata.json.gz</code>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:UpdateTableMetadataLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket. </p>
            namespace: <p>The namespace of the table.</p>
            name: <p>The name of the table.</p>
            version_token: <p>The version token of the table. </p>
            metadata_location: <p>The new metadata location for the table. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_s3tables.types.update_table_metadata_location_request.UpdateTableMetadataLocationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_s3tables.types.update_table_metadata_location_response.UpdateTableMetadataLocationResponse"
        ]:
            import aws_sdk_s3tables._operations.s3_table_buckets.update_table_metadata_location

            (
                output,
                http_response,
            ) = await aws_sdk_s3tables._operations.s3_table_buckets.update_table_metadata_location.async_update_table_metadata_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_s3tables.types.update_table_metadata_location_request.UpdateTableMetadataLocationRequest = {}  # type: ignore[typeddict-item]
        input["table_bucket_arn"] = table_bucket_arn
        input["namespace"] = namespace
        input["name"] = name
        input["version_token"] = version_token
        input["metadata_location"] = metadata_location

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
