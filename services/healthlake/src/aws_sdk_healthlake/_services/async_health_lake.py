"""Generated from Smithy shape ``com.amazonaws.healthlake#HealthLake``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_healthlake._auth._signers
import aws_sdk_healthlake._auth._sigv4
from aws_sdk_healthlake._auth._identity import Credentials
from aws_sdk_healthlake._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_healthlake._auth._zapros_handler import AuthMiddleware
from aws_sdk_healthlake._services._aws_config import aaws_config
from aws_sdk_healthlake._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.amazon_resource_name
    import aws_sdk_healthlake.types.analytics_configuration
    import aws_sdk_healthlake.types.client_token_string
    import aws_sdk_healthlake.types.create_fhir_datastore_request
    import aws_sdk_healthlake.types.create_fhir_datastore_response
    import aws_sdk_healthlake.types.datastore_filter
    import aws_sdk_healthlake.types.datastore_id
    import aws_sdk_healthlake.types.datastore_name
    import aws_sdk_healthlake.types.delete_fhir_datastore_request
    import aws_sdk_healthlake.types.delete_fhir_datastore_response
    import aws_sdk_healthlake.types.describe_fhir_datastore_request
    import aws_sdk_healthlake.types.describe_fhir_datastore_response
    import aws_sdk_healthlake.types.describe_fhir_export_job_request
    import aws_sdk_healthlake.types.describe_fhir_export_job_response
    import aws_sdk_healthlake.types.describe_fhir_import_job_request
    import aws_sdk_healthlake.types.describe_fhir_import_job_response
    import aws_sdk_healthlake.types.fhir_version
    import aws_sdk_healthlake.types.iam_role_arn
    import aws_sdk_healthlake.types.identity_provider_configuration
    import aws_sdk_healthlake.types.input_data_config
    import aws_sdk_healthlake.types.job_id
    import aws_sdk_healthlake.types.job_name
    import aws_sdk_healthlake.types.job_status
    import aws_sdk_healthlake.types.list_fhir_datastores_request
    import aws_sdk_healthlake.types.list_fhir_datastores_response
    import aws_sdk_healthlake.types.list_fhir_export_jobs_request
    import aws_sdk_healthlake.types.list_fhir_export_jobs_response
    import aws_sdk_healthlake.types.list_fhir_import_jobs_request
    import aws_sdk_healthlake.types.list_fhir_import_jobs_response
    import aws_sdk_healthlake.types.list_tags_for_resource_request
    import aws_sdk_healthlake.types.list_tags_for_resource_response
    import aws_sdk_healthlake.types.max_results_integer
    import aws_sdk_healthlake.types.next_token
    import aws_sdk_healthlake.types.nlp_configuration
    import aws_sdk_healthlake.types.output_data_config
    import aws_sdk_healthlake.types.preload_data_config
    import aws_sdk_healthlake.types.profile_configuration
    import aws_sdk_healthlake.types.sse_configuration
    import aws_sdk_healthlake.types.start_fhir_export_job_request
    import aws_sdk_healthlake.types.start_fhir_export_job_response
    import aws_sdk_healthlake.types.start_fhir_import_job_request
    import aws_sdk_healthlake.types.start_fhir_import_job_response
    import aws_sdk_healthlake.types.tag_key_list
    import aws_sdk_healthlake.types.tag_list
    import aws_sdk_healthlake.types.tag_resource_request
    import aws_sdk_healthlake.types.tag_resource_response
    import aws_sdk_healthlake.types.timestamp
    import aws_sdk_healthlake.types.untag_resource_request
    import aws_sdk_healthlake.types.untag_resource_response
    import aws_sdk_healthlake.types.update_fhir_datastore_request
    import aws_sdk_healthlake.types.update_fhir_datastore_response
    import aws_sdk_healthlake.types.validation_level


class AsyncHealthLakeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncHealthLakeClient:
    """A client for the ``HealthLake`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncHealthLakeClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncHealthLakeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncHealthLakeClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def create_fhir_datastore(
        self,
        datastore_type_version: "aws_sdk_healthlake.types.fhir_version.FHIRVersion",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        datastore_name: Optional[
            "aws_sdk_healthlake.types.datastore_name.DatastoreName"
        ] = None,
        sse_configuration: Optional[
            "aws_sdk_healthlake.types.sse_configuration.SseConfiguration"
        ] = None,
        preload_data_config: Optional[
            "aws_sdk_healthlake.types.preload_data_config.PreloadDataConfig"
        ] = None,
        client_token: Optional[
            "aws_sdk_healthlake.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional["aws_sdk_healthlake.types.tag_list.TagList"] = None,
        identity_provider_configuration: Optional[
            "aws_sdk_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
    ) -> "aws_sdk_healthlake.types.create_fhir_datastore_response.CreateFHIRDatastoreResponse":
        """<p>Create a FHIR-enabled data store.</p>

        Args:
            datastore_name: <p>The data store name (user-generated).</p>
            datastore_type_version: <p>The FHIR release version supported by the data store. Current support is for version <code>R4</code>.</p>
            sse_configuration: <p>The server-side encryption key configuration for a customer-provided encryption key specified for creating a data store. </p>
            preload_data_config: <p>An optional parameter to preload (import) open source Synthea FHIR data upon creation of the data store.</p>
            client_token: <p>An optional user-provided token to ensure API idempotency.</p>
            tags: <p>The resource tags applied to a data store when it is created.</p>
            identity_provider_configuration: <p>The identity provider configuration to use for the data store.</p>

        Raises:
            aws_sdk_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.create_fhir_datastore_request.CreateFHIRDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.create_fhir_datastore_response.CreateFHIRDatastoreResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.create_fhir_datastore

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.create_fhir_datastore.async_create_fhir_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.create_fhir_datastore_request.CreateFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
        if datastore_name is not None:
            input_["datastore_name"] = datastore_name
        input_["datastore_type_version"] = datastore_type_version
        if sse_configuration is not None:
            input_["sse_configuration"] = sse_configuration
        if preload_data_config is not None:
            input_["preload_data_config"] = preload_data_config
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_fhir_datastore(
        self,
        datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "aws_sdk_healthlake.types.delete_fhir_datastore_response.DeleteFHIRDatastoreResponse":
        """<p>Delete a FHIR-enabled data store.</p>

        Args:
            datastore_id: <p> The AWS-generated identifier for the data store to be deleted.</p>

        Raises:
            aws_sdk_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            aws_sdk_healthlake.errors.conflict_exception.ConflictException: <p>The data store is in a transition state and the user requested action cannot be performed.</p>
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.delete_fhir_datastore_request.DeleteFHIRDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.delete_fhir_datastore_response.DeleteFHIRDatastoreResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.delete_fhir_datastore

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.delete_fhir_datastore.async_delete_fhir_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.delete_fhir_datastore_request.DeleteFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_fhir_datastore(
        self,
        datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "aws_sdk_healthlake.types.describe_fhir_datastore_response.DescribeFHIRDatastoreResponse":
        """<p>Get properties for a FHIR-enabled data store.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>

        Raises:
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.describe_fhir_datastore_request.DescribeFHIRDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.describe_fhir_datastore_response.DescribeFHIRDatastoreResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.describe_fhir_datastore

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.describe_fhir_datastore.async_describe_fhir_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.describe_fhir_datastore_request.DescribeFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_fhir_export_job(
        self,
        datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId",
        job_id: "aws_sdk_healthlake.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "aws_sdk_healthlake.types.describe_fhir_export_job_response.DescribeFHIRExportJobResponse":
        """<p>Get FHIR export job properties.</p>

        Args:
            datastore_id: <p>The data store identifier from which FHIR data is being exported from.</p>
            job_id: <p>The export job identifier.</p>

        Raises:
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.describe_fhir_export_job_request.DescribeFHIRExportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.describe_fhir_export_job_response.DescribeFHIRExportJobResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.describe_fhir_export_job

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.describe_fhir_export_job.async_describe_fhir_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.describe_fhir_export_job_request.DescribeFHIRExportJobRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_fhir_import_job(
        self,
        datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId",
        job_id: "aws_sdk_healthlake.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "aws_sdk_healthlake.types.describe_fhir_import_job_response.DescribeFHIRImportJobResponse":
        """<p>Get the import job properties to learn more about the job or job progress.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            job_id: <p>The import job identifier.</p>

        Raises:
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.describe_fhir_import_job_request.DescribeFHIRImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.describe_fhir_import_job_response.DescribeFHIRImportJobResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.describe_fhir_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.describe_fhir_import_job.async_describe_fhir_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.describe_fhir_import_job_request.DescribeFHIRImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_fhir_datastores(
        self,
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        filter: Optional[
            "aws_sdk_healthlake.types.datastore_filter.DatastoreFilter"
        ] = None,
        next_token: Optional["aws_sdk_healthlake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_healthlake.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "aws_sdk_healthlake.types.list_fhir_datastores_response.ListFHIRDatastoresResponse":
        """<p>List all FHIR-enabled data stores in a user’s account, regardless of data store status.</p>

        Args:
            filter: <p>List all filters associated with a FHIR data store request.</p>
            next_token: <p>The token used to retrieve the next page of data stores when results are paginated.</p>
            max_results: <p>The maximum number of data stores returned on a page.</p>

        Raises:
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.list_fhir_datastores_request.ListFHIRDatastoresRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.list_fhir_datastores_response.ListFHIRDatastoresResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.list_fhir_datastores

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.list_fhir_datastores.async_list_fhir_datastores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.list_fhir_datastores_request.ListFHIRDatastoresRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_fhir_export_jobs(
        self,
        datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        next_token: Optional["aws_sdk_healthlake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_healthlake.types.max_results_integer.MaxResultsInteger"
        ] = None,
        job_name: Optional["aws_sdk_healthlake.types.job_name.JobName"] = None,
        job_status: Optional["aws_sdk_healthlake.types.job_status.JobStatus"] = None,
        submitted_before: Optional[
            "aws_sdk_healthlake.types.timestamp.Timestamp"
        ] = None,
        submitted_after: Optional[
            "aws_sdk_healthlake.types.timestamp.Timestamp"
        ] = None,
    ) -> "aws_sdk_healthlake.types.list_fhir_export_jobs_response.ListFHIRExportJobsResponse":
        """<p>Lists all FHIR export jobs associated with an account and their statuses.</p>

        Args:
            datastore_id: <p>Limits the response to the export job with the specified data store ID. </p>
            next_token: <p>A pagination token used to identify the next page of results to return.</p>
            max_results: <p>Limits the number of results returned for a ListFHIRExportJobs to a maximum quantity specified by the user.</p>
            job_name: <p>Limits the response to the export job with the specified job name. </p>
            job_status: <p>Limits the response to export jobs with the specified job status. </p>
            submitted_before: <p>Limits the response to FHIR export jobs submitted before a user- specified date.</p>
            submitted_after: <p>Limits the response to FHIR export jobs submitted after a user-specified date.</p>

        Raises:
            aws_sdk_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.list_fhir_export_jobs_request.ListFHIRExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.list_fhir_export_jobs_response.ListFHIRExportJobsResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.list_fhir_export_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.list_fhir_export_jobs.async_list_fhir_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.list_fhir_export_jobs_request.ListFHIRExportJobsRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if job_name is not None:
            input_["job_name"] = job_name
        if job_status is not None:
            input_["job_status"] = job_status
        if submitted_before is not None:
            input_["submitted_before"] = submitted_before
        if submitted_after is not None:
            input_["submitted_after"] = submitted_after

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_fhir_import_jobs(
        self,
        datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        next_token: Optional["aws_sdk_healthlake.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_healthlake.types.max_results_integer.MaxResultsInteger"
        ] = None,
        job_name: Optional["aws_sdk_healthlake.types.job_name.JobName"] = None,
        job_status: Optional["aws_sdk_healthlake.types.job_status.JobStatus"] = None,
        submitted_before: Optional[
            "aws_sdk_healthlake.types.timestamp.Timestamp"
        ] = None,
        submitted_after: Optional[
            "aws_sdk_healthlake.types.timestamp.Timestamp"
        ] = None,
    ) -> "aws_sdk_healthlake.types.list_fhir_import_jobs_response.ListFHIRImportJobsResponse":
        """<p>List all FHIR import jobs associated with an account and their statuses.</p>

        Args:
            datastore_id: <p>Limits the response to the import job with the specified data store ID. </p>
            next_token: <p>The pagination token used to identify the next page of results to return.</p>
            max_results: <p>Limits the number of results returned for <code>ListFHIRImportJobs</code> to a maximum quantity specified by the user.</p>
            job_name: <p>Limits the response to the import job with the specified job name. </p>
            job_status: <p>Limits the response to the import job with the specified job status. </p>
            submitted_before: <p>Limits the response to FHIR import jobs submitted before a user- specified date. </p>
            submitted_after: <p>Limits the response to FHIR import jobs submitted after a user-specified date.</p>

        Raises:
            aws_sdk_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.list_fhir_import_jobs_request.ListFHIRImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.list_fhir_import_jobs_response.ListFHIRImportJobsResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.list_fhir_import_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.list_fhir_import_jobs.async_list_fhir_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.list_fhir_import_jobs_request.ListFHIRImportJobsRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if job_name is not None:
            input_["job_name"] = job_name
        if job_status is not None:
            input_["job_status"] = job_status
        if submitted_before is not None:
            input_["submitted_before"] = submitted_before
        if submitted_after is not None:
            input_["submitted_after"] = submitted_after

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_healthlake.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "aws_sdk_healthlake.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of all existing tags associated with a data store.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the data store to which tags are being added.</p>

        Raises:
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_fhir_export_job(
        self,
        output_data_config: "aws_sdk_healthlake.types.output_data_config.OutputDataConfig",
        datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId",
        data_access_role_arn: "aws_sdk_healthlake.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        job_name: Optional["aws_sdk_healthlake.types.job_name.JobName"] = None,
        client_token: Optional[
            "aws_sdk_healthlake.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "aws_sdk_healthlake.types.start_fhir_export_job_response.StartFHIRExportJobResponse":
        """<p>Start a FHIR export job.</p>

        Args:
            job_name: <p>The export job name.</p>
            output_data_config: <p>The output data configuration supplied when the export job was started.</p>
            datastore_id: <p>The data store identifier from which files are being exported.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) used during initiation of the export job.</p>
            client_token: <p>An optional user provided token used for ensuring API idempotency.</p>

        Raises:
            aws_sdk_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.start_fhir_export_job_request.StartFHIRExportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.start_fhir_export_job_response.StartFHIRExportJobResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.start_fhir_export_job

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.start_fhir_export_job.async_start_fhir_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.start_fhir_export_job_request.StartFHIRExportJobRequest = {}  # type: ignore[typeddict-item]
        if job_name is not None:
            input_["job_name"] = job_name
        input_["output_data_config"] = output_data_config
        input_["datastore_id"] = datastore_id
        input_["data_access_role_arn"] = data_access_role_arn
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_fhir_import_job(
        self,
        input_data_config: "aws_sdk_healthlake.types.input_data_config.InputDataConfig",
        job_output_data_config: "aws_sdk_healthlake.types.output_data_config.OutputDataConfig",
        datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId",
        data_access_role_arn: "aws_sdk_healthlake.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        job_name: Optional["aws_sdk_healthlake.types.job_name.JobName"] = None,
        client_token: Optional[
            "aws_sdk_healthlake.types.client_token_string.ClientTokenString"
        ] = None,
        validation_level: Optional[
            "aws_sdk_healthlake.types.validation_level.ValidationLevel"
        ] = None,
    ) -> "aws_sdk_healthlake.types.start_fhir_import_job_response.StartFHIRImportJobResponse":
        """<p>Start importing bulk FHIR data into an ACTIVE data store. The import job imports FHIR data found in the <code>InputDataConfig</code> object and stores processing results in the <code>JobOutputDataConfig</code> object.</p>

        Args:
            job_name: <p>The import job name.</p>
            input_data_config: <p>The input properties for the import job request.</p>
            datastore_id: <p>The data store identifier.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) that grants access permission to AWS HealthLake.</p>
            client_token: <p>The optional user-provided token used for ensuring API idempotency.</p>
            validation_level: <p>The validation level of the import job.</p>

        Raises:
            aws_sdk_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.start_fhir_import_job_request.StartFHIRImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.start_fhir_import_job_response.StartFHIRImportJobResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.start_fhir_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.start_fhir_import_job.async_start_fhir_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.start_fhir_import_job_request.StartFHIRImportJobRequest = {}  # type: ignore[typeddict-item]
        if job_name is not None:
            input_["job_name"] = job_name
        input_["input_data_config"] = input_data_config
        input_["job_output_data_config"] = job_output_data_config
        input_["datastore_id"] = datastore_id
        input_["data_access_role_arn"] = data_access_role_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if validation_level is not None:
            input_["validation_level"] = validation_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_healthlake.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_healthlake.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "aws_sdk_healthlake.types.tag_resource_response.TagResourceResponse":
        """<p>Add a user-specifed key and value tag to a data store.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that grants access to the data store tags are being added to.</p>
            tags: <p>The user-specified key and value pair tags being added to a data store.</p>

        Raises:
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_healthlake.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_healthlake.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
    ) -> "aws_sdk_healthlake.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove a user-specifed key and value tag from a data store.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the data store from which tags are being removed.</p>
            tag_keys: <p>The keys for the tags to be removed from the data store.</p>

        Raises:
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_fhir_datastore(
        self,
        datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncHealthLakeClientConfig] = None,
        datastore_name: Optional[
            "aws_sdk_healthlake.types.datastore_name.DatastoreName"
        ] = None,
        analytics_configuration: Optional[
            "aws_sdk_healthlake.types.analytics_configuration.AnalyticsConfiguration"
        ] = None,
        nlp_configuration: Optional[
            "aws_sdk_healthlake.types.nlp_configuration.NlpConfiguration"
        ] = None,
        profile_configuration: Optional[
            "aws_sdk_healthlake.types.profile_configuration.ProfileConfiguration"
        ] = None,
        identity_provider_configuration: Optional[
            "aws_sdk_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
    ) -> "aws_sdk_healthlake.types.update_fhir_datastore_response.UpdateFHIRDatastoreResponse":
        """<para>Update the properties of a FHIR-enabled data store.</para>

        Args:
            datastore_id: <para>The data store identifier.</para>
            datastore_name: <para>The data store name.</para>
            analytics_configuration: <para>The analytics configuration for the data store.</para>
            nlp_configuration: <para>The NLP configuration for the data store.</para>
            profile_configuration: <para>The profile configuration for the data store.</para>
            identity_provider_configuration: <para>The identity provider configuration for the data store.</para>

        Raises:
            aws_sdk_healthlake.errors.access_denied_exception.AccessDeniedException: <p>Access is denied. Your account is not authorized to perform this operation.</p>
            aws_sdk_healthlake.errors.conflict_exception.ConflictException: <p>The data store is in a transition state and the user requested action cannot be performed.</p>
            aws_sdk_healthlake.errors.internal_server_exception.InternalServerException: <p>An unknown internal error occurred in the service.</p>
            aws_sdk_healthlake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested data store was not found.</p>
            aws_sdk_healthlake.errors.throttling_exception.ThrottlingException: <p>The user has exceeded their maximum number of allowed calls to the given API. </p>
            aws_sdk_healthlake.errors.validation_exception.ValidationException: <p>The user input parameter was invalid.</p>
            aws_sdk_healthlake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_healthlake.types.update_fhir_datastore_request.UpdateFHIRDatastoreRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_healthlake.types.update_fhir_datastore_response.UpdateFHIRDatastoreResponse"
        ]:
            import aws_sdk_healthlake._operations.health_lake.update_fhir_datastore

            (
                output,
                http_response,
            ) = await aws_sdk_healthlake._operations.health_lake.update_fhir_datastore.async_update_fhir_datastore(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_healthlake.types.update_fhir_datastore_request.UpdateFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        if datastore_name is not None:
            input_["datastore_name"] = datastore_name
        if analytics_configuration is not None:
            input_["analytics_configuration"] = analytics_configuration
        if nlp_configuration is not None:
            input_["nlp_configuration"] = nlp_configuration
        if profile_configuration is not None:
            input_["profile_configuration"] = profile_configuration
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
