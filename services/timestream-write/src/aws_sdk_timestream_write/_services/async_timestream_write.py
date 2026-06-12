"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#Timestream_20181101``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

from aws_sdk_timestream_write._auth._identity import Credentials
from aws_sdk_timestream_write._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_timestream_write._auth._zapros_handler import AuthMiddleware
from aws_sdk_timestream_write._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.amazon_resource_name
    import aws_sdk_timestream_write.types.batch_load_status
    import aws_sdk_timestream_write.types.batch_load_task_id
    import aws_sdk_timestream_write.types.client_request_token
    import aws_sdk_timestream_write.types.create_batch_load_task_request
    import aws_sdk_timestream_write.types.create_batch_load_task_response
    import aws_sdk_timestream_write.types.create_database_request
    import aws_sdk_timestream_write.types.create_database_response
    import aws_sdk_timestream_write.types.create_table_request
    import aws_sdk_timestream_write.types.create_table_response
    import aws_sdk_timestream_write.types.data_model_configuration
    import aws_sdk_timestream_write.types.data_source_configuration
    import aws_sdk_timestream_write.types.delete_database_request
    import aws_sdk_timestream_write.types.delete_table_request
    import aws_sdk_timestream_write.types.describe_batch_load_task_request
    import aws_sdk_timestream_write.types.describe_batch_load_task_response
    import aws_sdk_timestream_write.types.describe_database_request
    import aws_sdk_timestream_write.types.describe_database_response
    import aws_sdk_timestream_write.types.describe_endpoints_request
    import aws_sdk_timestream_write.types.describe_endpoints_response
    import aws_sdk_timestream_write.types.describe_table_request
    import aws_sdk_timestream_write.types.describe_table_response
    import aws_sdk_timestream_write.types.list_batch_load_tasks_request
    import aws_sdk_timestream_write.types.list_batch_load_tasks_response
    import aws_sdk_timestream_write.types.list_databases_request
    import aws_sdk_timestream_write.types.list_databases_response
    import aws_sdk_timestream_write.types.list_tables_request
    import aws_sdk_timestream_write.types.list_tables_response
    import aws_sdk_timestream_write.types.list_tags_for_resource_request
    import aws_sdk_timestream_write.types.list_tags_for_resource_response
    import aws_sdk_timestream_write.types.magnetic_store_write_properties
    import aws_sdk_timestream_write.types.page_limit
    import aws_sdk_timestream_write.types.pagination_limit
    import aws_sdk_timestream_write.types.record
    import aws_sdk_timestream_write.types.record_version
    import aws_sdk_timestream_write.types.records
    import aws_sdk_timestream_write.types.report_configuration
    import aws_sdk_timestream_write.types.resource_create_api_name
    import aws_sdk_timestream_write.types.resource_name
    import aws_sdk_timestream_write.types.resume_batch_load_task_request
    import aws_sdk_timestream_write.types.resume_batch_load_task_response
    import aws_sdk_timestream_write.types.retention_properties
    import aws_sdk_timestream_write.types.schema
    import aws_sdk_timestream_write.types.string
    import aws_sdk_timestream_write.types.string_value2048
    import aws_sdk_timestream_write.types.tag_key_list
    import aws_sdk_timestream_write.types.tag_list
    import aws_sdk_timestream_write.types.tag_resource_request
    import aws_sdk_timestream_write.types.tag_resource_response
    import aws_sdk_timestream_write.types.untag_resource_request
    import aws_sdk_timestream_write.types.untag_resource_response
    import aws_sdk_timestream_write.types.update_database_request
    import aws_sdk_timestream_write.types.update_database_response
    import aws_sdk_timestream_write.types.update_table_request
    import aws_sdk_timestream_write.types.update_table_response
    import aws_sdk_timestream_write.types.write_records_request
    import aws_sdk_timestream_write.types.write_records_response


class AsyncTimestreamWriteClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncTimestreamWriteClient:
    """A client for the ``TimestreamWrite`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncTimestreamWriteClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTimestreamWriteClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def create_batch_load_task(
        self,
        data_source_configuration: "aws_sdk_timestream_write.types.data_source_configuration.DataSourceConfiguration",
        report_configuration: "aws_sdk_timestream_write.types.report_configuration.ReportConfiguration",
        target_database_name: "aws_sdk_timestream_write.types.resource_create_api_name.ResourceCreateAPIName",
        target_table_name: "aws_sdk_timestream_write.types.resource_create_api_name.ResourceCreateAPIName",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
        client_token: Optional[
            "aws_sdk_timestream_write.types.client_request_token.ClientRequestToken"
        ] = None,
        data_model_configuration: Optional[
            "aws_sdk_timestream_write.types.data_model_configuration.DataModelConfiguration"
        ] = None,
        record_version: Optional[
            "aws_sdk_timestream_write.types.record_version.RecordVersion"
        ] = None,
    ) -> "aws_sdk_timestream_write.types.create_batch_load_task_response.CreateBatchLoadTaskResponse":
        """<p>Creates a new Timestream batch load task. A batch load task processes data from a CSV source in an S3 location and writes to a Timestream table. A mapping from source to target is defined in a batch load task. Errors and events are written to a report at an S3 location. For the report, if the KMS key is not specified, the report will be encrypted with an S3 managed key when <code>SSE_S3</code> is the option. Otherwise an error is thrown. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed keys</a>. <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html\">Service quotas apply</a>. For details, see <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.create-batch-load.html\">code sample</a>.</p>

        Args:
            client_token: <p></p>
            data_source_configuration: <p>Defines configuration details about the data source for a batch load task.</p>
            target_database_name: <p>Target Timestream database for a batch load task.</p>
            target_table_name: <p>Target Timestream table for a batch load task.</p>
            record_version: <p></p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.create_batch_load_task_request.CreateBatchLoadTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.create_batch_load_task_response.CreateBatchLoadTaskResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.create_batch_load_task

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.create_batch_load_task.async_create_batch_load_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.create_batch_load_task_request.CreateBatchLoadTaskRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        if data_model_configuration is not None:
            input["data_model_configuration"] = data_model_configuration
        input["data_source_configuration"] = data_source_configuration
        input["report_configuration"] = report_configuration
        input["target_database_name"] = target_database_name
        input["target_table_name"] = target_table_name
        if record_version is not None:
            input["record_version"] = record_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_database(
        self,
        database_name: "aws_sdk_timestream_write.types.resource_create_api_name.ResourceCreateAPIName",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
        kms_key_id: Optional[
            "aws_sdk_timestream_write.types.string_value2048.StringValue2048"
        ] = None,
        tags: Optional["aws_sdk_timestream_write.types.tag_list.TagList"] = None,
    ) -> (
        "aws_sdk_timestream_write.types.create_database_response.CreateDatabaseResponse"
    ):
        """<p>Creates a new Timestream database. If the KMS key is not specified, the database will be encrypted with a Timestream managed KMS key located in your account. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed keys</a>. <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html\">Service quotas apply</a>. For details, see <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.create-db.html\">code sample</a>. </p>

        Args:
            database_name: <p>The name of the Timestream database.</p>
            kms_key_id: <p>The KMS key for the database. If the KMS key is not specified, the database will be encrypted with a Timestream managed KMS key located in your account. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed keys</a>.</p>
            tags: <p> A list of key-value pairs to label the table. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.create_database_request.CreateDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.create_database_response.CreateDatabaseResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.create_database

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.create_database.async_create_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.create_database_request.CreateDatabaseRequest = {}  # type: ignore[typeddict-item]
        input["database_name"] = database_name
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_table(
        self,
        database_name: "aws_sdk_timestream_write.types.resource_create_api_name.ResourceCreateAPIName",
        table_name: "aws_sdk_timestream_write.types.resource_create_api_name.ResourceCreateAPIName",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
        retention_properties: Optional[
            "aws_sdk_timestream_write.types.retention_properties.RetentionProperties"
        ] = None,
        tags: Optional["aws_sdk_timestream_write.types.tag_list.TagList"] = None,
        magnetic_store_write_properties: Optional[
            "aws_sdk_timestream_write.types.magnetic_store_write_properties.MagneticStoreWriteProperties"
        ] = None,
        schema: Optional["aws_sdk_timestream_write.types.schema.Schema"] = None,
    ) -> "aws_sdk_timestream_write.types.create_table_response.CreateTableResponse":
        """<p>Adds a new table to an existing database in your account. In an Amazon Web Services account, table names must be at least unique within each Region if they are in the same database. You might have identical table names in the same Region if the tables are in separate databases. While creating the table, you must specify the table name, database name, and the retention properties. <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html\">Service quotas apply</a>. See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.create-table.html\">code sample</a> for details. </p>

        Args:
            database_name: <p>The name of the Timestream database.</p>
            table_name: <p>The name of the Timestream table.</p>
            retention_properties: <p>The duration for which your time-series data must be stored in the memory store and the magnetic store.</p>
            tags: <p> A list of key-value pairs to label the table. </p>
            magnetic_store_write_properties: <p>Contains properties to set on the table when enabling magnetic store writes.</p>
            schema: <p> The schema of the table. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.create_table_request.CreateTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.create_table_response.CreateTableResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.create_table

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.create_table.async_create_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.create_table_request.CreateTableRequest = {}  # type: ignore[typeddict-item]
        input["database_name"] = database_name
        input["table_name"] = table_name
        if retention_properties is not None:
            input["retention_properties"] = retention_properties
        if tags is not None:
            input["tags"] = tags
        if magnetic_store_write_properties is not None:
            input["magnetic_store_write_properties"] = magnetic_store_write_properties
        if schema is not None:
            input["schema"] = schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_database(
        self,
        database_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
    ) -> None:
        """<p>Deletes a given Timestream database. <i>This is an irreversible operation. After a database is deleted, the time-series data from its tables cannot be recovered.</i> </p> <note> <p>All tables in the database must be deleted first, or a ValidationException error will be thrown. </p> <p>Due to the nature of distributed retries, the operation can return either success or a ResourceNotFoundException. Clients should consider them equivalent.</p> </note> <p>See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.delete-db.html\">code sample</a> for details.</p>

        Args:
            database_name: <p>The name of the Timestream database to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.delete_database_request.DeleteDatabaseRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_timestream_write._operations.timestream_20181101.delete_database

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.delete_database.async_delete_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.delete_database_request.DeleteDatabaseRequest = {}  # type: ignore[typeddict-item]
        input["database_name"] = database_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_table(
        self,
        database_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        table_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
    ) -> None:
        """<p>Deletes a given Timestream table. This is an irreversible operation. After a Timestream database table is deleted, the time-series data stored in the table cannot be recovered. </p> <note> <p>Due to the nature of distributed retries, the operation can return either success or a ResourceNotFoundException. Clients should consider them equivalent.</p> </note> <p>See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.delete-table.html\">code sample</a> for details.</p>

        Args:
            database_name: <p>The name of the database where the Timestream database is to be deleted.</p>
            table_name: <p>The name of the Timestream table to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.delete_table_request.DeleteTableRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_timestream_write._operations.timestream_20181101.delete_table

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.delete_table.async_delete_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.delete_table_request.DeleteTableRequest = {}  # type: ignore[typeddict-item]
        input["database_name"] = database_name
        input["table_name"] = table_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_batch_load_task(
        self,
        task_id: "aws_sdk_timestream_write.types.batch_load_task_id.BatchLoadTaskId",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
    ) -> "aws_sdk_timestream_write.types.describe_batch_load_task_response.DescribeBatchLoadTaskResponse":
        """<p>Returns information about the batch load task, including configurations, mappings, progress, and other details. <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html\">Service quotas apply</a>. See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.describe-batch-load.html\">code sample</a> for details.</p>

        Args:
            task_id: <p>The ID of the batch load task.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.describe_batch_load_task_request.DescribeBatchLoadTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.describe_batch_load_task_response.DescribeBatchLoadTaskResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.describe_batch_load_task

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.describe_batch_load_task.async_describe_batch_load_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.describe_batch_load_task_request.DescribeBatchLoadTaskRequest = {}  # type: ignore[typeddict-item]
        input["task_id"] = task_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_database(
        self,
        database_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
    ) -> "aws_sdk_timestream_write.types.describe_database_response.DescribeDatabaseResponse":
        """<p>Returns information about the database, including the database name, time that the database was created, and the total number of tables found within the database. <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html\">Service quotas apply</a>. See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.describe-db.html\">code sample</a> for details.</p>

        Args:
            database_name: <p>The name of the Timestream database.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.describe_database_request.DescribeDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.describe_database_response.DescribeDatabaseResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.describe_database

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.describe_database.async_describe_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.describe_database_request.DescribeDatabaseRequest = {}  # type: ignore[typeddict-item]
        input["database_name"] = database_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_endpoints(
        self, *, config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None
    ) -> "aws_sdk_timestream_write.types.describe_endpoints_response.DescribeEndpointsResponse":
        """<p>Returns a list of available endpoints to make Timestream API calls against. This API operation is available through both the Write and Query APIs.</p> <p>Because the Timestream SDKs are designed to transparently work with the service’s architecture, including the management and mapping of the service endpoints, <i>we don't recommend that you use this API operation unless</i>:</p> <ul> <li> <p>You are using <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/VPCEndpoints\">VPC endpoints (Amazon Web Services PrivateLink) with Timestream</a> </p> </li> <li> <p>Your application uses a programming language that does not yet have SDK support</p> </li> <li> <p>You require better control over the client-side implementation</p> </li> </ul> <p>For detailed information on how and when to use and implement DescribeEndpoints, see <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/Using.API.html#Using-API.endpoint-discovery\">The Endpoint Discovery Pattern</a>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.describe_endpoints_request.DescribeEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.describe_endpoints_response.DescribeEndpointsResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.describe_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.describe_endpoints.async_describe_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.describe_endpoints_request.DescribeEndpointsRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_table(
        self,
        database_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        table_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
    ) -> "aws_sdk_timestream_write.types.describe_table_response.DescribeTableResponse":
        """<p>Returns information about the table, including the table name, database name, retention duration of the memory store and the magnetic store. <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html\">Service quotas apply</a>. See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.describe-table.html\">code sample</a> for details. </p>

        Args:
            database_name: <p>The name of the Timestream database.</p>
            table_name: <p>The name of the Timestream table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.describe_table_request.DescribeTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.describe_table_response.DescribeTableResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.describe_table

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.describe_table.async_describe_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.describe_table_request.DescribeTableRequest = {}  # type: ignore[typeddict-item]
        input["database_name"] = database_name
        input["table_name"] = table_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_batch_load_tasks(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
        next_token: Optional["aws_sdk_timestream_write.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_timestream_write.types.page_limit.PageLimit"
        ] = None,
        task_status: Optional[
            "aws_sdk_timestream_write.types.batch_load_status.BatchLoadStatus"
        ] = None,
    ) -> "aws_sdk_timestream_write.types.list_batch_load_tasks_response.ListBatchLoadTasksResponse":
        """<p>Provides a list of batch load tasks, along with the name, status, when the task is resumable until, and other details. See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.list-batch-load-tasks.html\">code sample</a> for details.</p>

        Args:
            next_token: <p>A token to specify where to start paginating. This is the NextToken from a previously truncated response.</p>
            max_results: <p>The total number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
            task_status: <p>Status of the batch load task.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.list_batch_load_tasks_request.ListBatchLoadTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.list_batch_load_tasks_response.ListBatchLoadTasksResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.list_batch_load_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.list_batch_load_tasks.async_list_batch_load_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.list_batch_load_tasks_request.ListBatchLoadTasksRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if task_status is not None:
            input["task_status"] = task_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_databases(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
        next_token: Optional["aws_sdk_timestream_write.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_timestream_write.types.pagination_limit.PaginationLimit"
        ] = None,
    ) -> "aws_sdk_timestream_write.types.list_databases_response.ListDatabasesResponse":
        """<p>Returns a list of your Timestream databases. <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html\">Service quotas apply</a>. See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.list-db.html\">code sample</a> for details. </p>

        Args:
            next_token: <p>The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
            max_results: <p>The total number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.list_databases_request.ListDatabasesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.list_databases_response.ListDatabasesResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.list_databases

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.list_databases.async_list_databases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.list_databases_request.ListDatabasesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tables(
        self,
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
        database_name: Optional[
            "aws_sdk_timestream_write.types.resource_name.ResourceName"
        ] = None,
        next_token: Optional["aws_sdk_timestream_write.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_timestream_write.types.pagination_limit.PaginationLimit"
        ] = None,
    ) -> "aws_sdk_timestream_write.types.list_tables_response.ListTablesResponse":
        """<p>Provides a list of tables, along with the name, status, and retention properties of each table. See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.list-table.html\">code sample</a> for details. </p>

        Args:
            database_name: <p>The name of the Timestream database.</p>
            next_token: <p>The pagination token. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
            max_results: <p>The total number of items to return in the output. If the total number of items available is more than the value specified, a NextToken is provided in the output. To resume pagination, provide the NextToken value as argument of a subsequent API invocation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.list_tables_request.ListTablesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.list_tables_response.ListTablesResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.list_tables

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.list_tables.async_list_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.list_tables_request.ListTablesRequest = {}  # type: ignore[typeddict-item]
        if database_name is not None:
            input["database_name"] = database_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_timestream_write.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
    ) -> "aws_sdk_timestream_write.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Lists all tags on a Timestream resource. </p>

        Args:
            resource_arn: <p> The Timestream resource with tags to be listed. This value is an Amazon Resource Name (ARN). </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def resume_batch_load_task(
        self,
        task_id: "aws_sdk_timestream_write.types.batch_load_task_id.BatchLoadTaskId",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
    ) -> "aws_sdk_timestream_write.types.resume_batch_load_task_response.ResumeBatchLoadTaskResponse":
        """<p> </p>

        Args:
            task_id: <p>The ID of the batch load task to resume.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.resume_batch_load_task_request.ResumeBatchLoadTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.resume_batch_load_task_response.ResumeBatchLoadTaskResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.resume_batch_load_task

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.resume_batch_load_task.async_resume_batch_load_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.resume_batch_load_task_request.ResumeBatchLoadTaskRequest = {}  # type: ignore[typeddict-item]
        input["task_id"] = task_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_timestream_write.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_timestream_write.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
    ) -> "aws_sdk_timestream_write.types.tag_resource_response.TagResourceResponse":
        """<p> Associates a set of tags with a Timestream resource. You can then activate these user-defined tags so that they appear on the Billing and Cost Management console for cost allocation tracking. </p>

        Args:
            resource_arn: <p> Identifies the Timestream resource to which tags should be added. This value is an Amazon Resource Name (ARN). </p>
            tags: <p> The tags to be assigned to the Timestream resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_timestream_write.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_timestream_write.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
    ) -> "aws_sdk_timestream_write.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes the association of tags from a Timestream resource. </p>

        Args:
            resource_arn: <p> The Timestream resource that the tags will be removed from. This value is an Amazon Resource Name (ARN). </p>
            tag_keys: <p> A list of tags keys. Existing tags of the resource whose keys are members of this list will be removed from the Timestream resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_database(
        self,
        database_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        kms_key_id: "aws_sdk_timestream_write.types.string_value2048.StringValue2048",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
    ) -> (
        "aws_sdk_timestream_write.types.update_database_response.UpdateDatabaseResponse"
    ):
        """<p> Modifies the KMS key for an existing database. While updating the database, you must specify the database name and the identifier of the new KMS key to be used (<code>KmsKeyId</code>). If there are any concurrent <code>UpdateDatabase</code> requests, first writer wins. </p> <p>See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.update-db.html\">code sample</a> for details.</p>

        Args:
            database_name: <p> The name of the database. </p>
            kms_key_id: <p> The identifier of the new KMS key (<code>KmsKeyId</code>) to be used to encrypt the data stored in the database. If the <code>KmsKeyId</code> currently registered with the database is the same as the <code>KmsKeyId</code> in the request, there will not be any update. </p> <p>You can specify the <code>KmsKeyId</code> using any of the following:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias ARN: <code>arn:aws:kms:us-east-1:111122223333:alias/ExampleAlias</code> </p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.update_database_request.UpdateDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.update_database_response.UpdateDatabaseResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.update_database

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.update_database.async_update_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.update_database_request.UpdateDatabaseRequest = {}  # type: ignore[typeddict-item]
        input["database_name"] = database_name
        input["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_table(
        self,
        database_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        table_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
        retention_properties: Optional[
            "aws_sdk_timestream_write.types.retention_properties.RetentionProperties"
        ] = None,
        magnetic_store_write_properties: Optional[
            "aws_sdk_timestream_write.types.magnetic_store_write_properties.MagneticStoreWriteProperties"
        ] = None,
        schema: Optional["aws_sdk_timestream_write.types.schema.Schema"] = None,
    ) -> "aws_sdk_timestream_write.types.update_table_response.UpdateTableResponse":
        """<p>Modifies the retention duration of the memory store and magnetic store for your Timestream table. Note that the change in retention duration takes effect immediately. For example, if the retention period of the memory store was initially set to 2 hours and then changed to 24 hours, the memory store will be capable of holding 24 hours of data, but will be populated with 24 hours of data 22 hours after this change was made. Timestream does not retrieve data from the magnetic store to populate the memory store. </p> <p>See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.update-table.html\">code sample</a> for details.</p>

        Args:
            database_name: <p>The name of the Timestream database.</p>
            table_name: <p>The name of the Timestream table.</p>
            retention_properties: <p>The retention duration of the memory store and the magnetic store.</p>
            magnetic_store_write_properties: <p>Contains properties to set on the table when enabling magnetic store writes.</p>
            schema: <p> The schema of the table. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.update_table_request.UpdateTableRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.update_table_response.UpdateTableResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.update_table

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.update_table.async_update_table(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.update_table_request.UpdateTableRequest = {}  # type: ignore[typeddict-item]
        input["database_name"] = database_name
        input["table_name"] = table_name
        if retention_properties is not None:
            input["retention_properties"] = retention_properties
        if magnetic_store_write_properties is not None:
            input["magnetic_store_write_properties"] = magnetic_store_write_properties
        if schema is not None:
            input["schema"] = schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def write_records(
        self,
        database_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        table_name: "aws_sdk_timestream_write.types.resource_name.ResourceName",
        records: "aws_sdk_timestream_write.types.records.Records",
        *,
        config_overrides: Optional[AsyncTimestreamWriteClientConfig] = None,
        common_attributes: Optional[
            "aws_sdk_timestream_write.types.record.Record"
        ] = None,
    ) -> "aws_sdk_timestream_write.types.write_records_response.WriteRecordsResponse":
        """<p>Enables you to write your time-series data into Timestream. You can specify a single data point or a batch of data points to be inserted into the system. Timestream offers you a flexible schema that auto detects the column names and data types for your Timestream tables based on the dimension names and data types of the data points you specify when invoking writes into the database. </p> <p>Timestream supports eventual consistency read semantics. This means that when you query data immediately after writing a batch of data into Timestream, the query results might not reflect the results of a recently completed write operation. The results may also include some stale data. If you repeat the query request after a short time, the results should return the latest data. <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/ts-limits.html\">Service quotas apply</a>. </p> <p>See <a href=\"https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.write.html\">code sample</a> for details.</p> <p> <b>Upserts</b> </p> <p>You can use the <code>Version</code> parameter in a <code>WriteRecords</code> request to update data points. Timestream tracks a version number with each record. <code>Version</code> defaults to <code>1</code> when it's not specified for the record in the request. Timestream updates an existing record’s measure value along with its <code>Version</code> when it receives a write request with a higher <code>Version</code> number for that record. When it receives an update request where the measure value is the same as that of the existing record, Timestream still updates <code>Version</code>, if it is greater than the existing value of <code>Version</code>. You can update a data point as many times as desired, as long as the value of <code>Version</code> continuously increases. </p> <p> For example, suppose you write a new record without indicating <code>Version</code> in the request. Timestream stores this record, and set <code>Version</code> to <code>1</code>. Now, suppose you try to update this record with a <code>WriteRecords</code> request of the same record with a different measure value but, like before, do not provide <code>Version</code>. In this case, Timestream will reject this update with a <code>RejectedRecordsException</code> since the updated record’s version is not greater than the existing value of Version. </p> <p>However, if you were to resend the update request with <code>Version</code> set to <code>2</code>, Timestream would then succeed in updating the record’s value, and the <code>Version</code> would be set to <code>2</code>. Next, suppose you sent a <code>WriteRecords</code> request with this same record and an identical measure value, but with <code>Version</code> set to <code>3</code>. In this case, Timestream would only update <code>Version</code> to <code>3</code>. Any further updates would need to send a version number greater than <code>3</code>, or the update requests would receive a <code>RejectedRecordsException</code>. </p>

        Args:
            database_name: <p>The name of the Timestream database.</p>
            table_name: <p>The name of the Timestream table.</p>
            common_attributes: <p>A record that contains the common measure, dimension, time, and version attributes shared across all the records in the request. The measure and dimension attributes specified will be merged with the measure and dimension attributes in the records object when the data is written into Timestream. Dimensions may not overlap, or a <code>ValidationException</code> will be thrown. In other words, a record must contain dimensions with unique names. </p>
            records: <p>An array of records that contain the unique measure, dimension, time, and version attributes for each time-series data point. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_timestream_write.types.write_records_request.WriteRecordsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_timestream_write.types.write_records_response.WriteRecordsResponse"
        ]:
            import aws_sdk_timestream_write._operations.timestream_20181101.write_records

            (
                output,
                http_response,
            ) = await aws_sdk_timestream_write._operations.timestream_20181101.write_records.async_write_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_timestream_write.types.write_records_request.WriteRecordsRequest = {}  # type: ignore[typeddict-item]
        input["database_name"] = database_name
        input["table_name"] = table_name
        if common_attributes is not None:
            input["common_attributes"] = common_attributes
        input["records"] = records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
