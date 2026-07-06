"""Generated from Smithy shape ``com.amazonaws.mgn#ApplicationMigrationService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_mgn._auth._signers
import aws_sdk_mgn._auth._sigv4
from aws_sdk_mgn._auth._identity import Credentials
from aws_sdk_mgn._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_mgn._auth._zapros_handler import AuthMiddleware
from aws_sdk_mgn._pagination import resolve_path as _resolve_path
from aws_sdk_mgn._resources.application_migration_service.account_resource import (
    AccountResource,
)
from aws_sdk_mgn._resources.application_migration_service.appliance_resource import (
    ApplianceResource,
)
from aws_sdk_mgn._resources.application_migration_service.application_resource import (
    ApplicationResource,
)
from aws_sdk_mgn._resources.application_migration_service.connector_resource import (
    ConnectorResource,
)
from aws_sdk_mgn._resources.application_migration_service.export_resource import (
    ExportResource,
)
from aws_sdk_mgn._resources.application_migration_service.import_resource import (
    ImportResource,
)
from aws_sdk_mgn._resources.application_migration_service.job_resource import (
    JobResource,
)
from aws_sdk_mgn._resources.application_migration_service.launch_configuration_template_resource import (
    LaunchConfigurationTemplateResource,
)
from aws_sdk_mgn._resources.application_migration_service.network_migration_definition_resource import (
    NetworkMigrationDefinitionResource,
)
from aws_sdk_mgn._resources.application_migration_service.replication_configuration_template_resource import (
    ReplicationConfigurationTemplateResource,
)
from aws_sdk_mgn._resources.application_migration_service.source_server_resource import (
    SourceServerResource,
)
from aws_sdk_mgn._resources.application_migration_service.vcenter_client_resource import (
    VcenterClientResource,
)
from aws_sdk_mgn._resources.application_migration_service.wave_resource import (
    WaveResource,
)
from aws_sdk_mgn._services._aws_config import aws_config
from aws_sdk_mgn._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.client_idempotency_token
    import aws_sdk_mgn.types.enrichment_source_s3_configuration
    import aws_sdk_mgn.types.enrichment_target_s3_configuration
    import aws_sdk_mgn.types.import_file_enrichment
    import aws_sdk_mgn.types.initialize_service_request
    import aws_sdk_mgn.types.initialize_service_response
    import aws_sdk_mgn.types.ip_assignment_strategy
    import aws_sdk_mgn.types.list_import_file_enrichments_filters
    import aws_sdk_mgn.types.list_import_file_enrichments_request
    import aws_sdk_mgn.types.list_import_file_enrichments_response
    import aws_sdk_mgn.types.list_managed_accounts_request
    import aws_sdk_mgn.types.list_managed_accounts_response
    import aws_sdk_mgn.types.list_tags_for_resource_request
    import aws_sdk_mgn.types.list_tags_for_resource_response
    import aws_sdk_mgn.types.managed_account
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.start_import_file_enrichment_request
    import aws_sdk_mgn.types.start_import_file_enrichment_response
    import aws_sdk_mgn.types.tag_keys
    import aws_sdk_mgn.types.tag_resource_request
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.untag_resource_request


class mgnClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class mgnClient:
    """A client for the ``mgn`` service.

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
        self._config = mgnClientConfig(
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
        self.account_resource = AccountResource(self)
        self.appliance_resource = ApplianceResource(self)
        self.application_resource = ApplicationResource(self)
        self.connector_resource = ConnectorResource(self)
        self.export_resource = ExportResource(self)
        self.import_resource = ImportResource(self)
        self.job_resource = JobResource(self)
        self.launch_configuration_template_resource = (
            LaunchConfigurationTemplateResource(self)
        )
        self.network_migration_definition_resource = NetworkMigrationDefinitionResource(
            self
        )
        self.replication_configuration_template_resource = (
            ReplicationConfigurationTemplateResource(self)
        )
        self.source_server_resource = SourceServerResource(self)
        self.vcenter_client_resource = VcenterClientResource(self)
        self.wave_resource = WaveResource(self)

    def operation_options(
        self, config_overrides: Optional[mgnClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: mgnClientConfig = config_overrides or {}
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

    def initialize_service(
        self, *, config_overrides: Optional[mgnClientConfig] = None
    ) -> "aws_sdk_mgn.types.initialize_service_response.InitializeServiceResponse":
        """<p>Initialize Application Migration Service.</p>

        Raises:
            aws_sdk_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operating denied due to a file permission or access check error.</p>
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.initialize_service_request.InitializeServiceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.initialize_service_response.InitializeServiceResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.initialize_service

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.initialize_service.initialize_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.initialize_service_request.InitializeServiceRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_import_file_enrichments(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_import_file_enrichments_filters.ListImportFileEnrichmentsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_import_file_enrichments_response.ListImportFileEnrichmentsResponse":
        """<p>Lists import file enrichment jobs with optional filtering by job IDs.</p>

        Args:
            filters: <p>Filters to apply when listing import file enrichment jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListImportFileEnrichments call

            >>> client.list_import_file_enrichments(filters={'jobIDs': ['01234567-abcd-abcd-efab-0123456789ab']}, max_results=10)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_import_file_enrichments_request.ListImportFileEnrichmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_import_file_enrichments_response.ListImportFileEnrichmentsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_import_file_enrichments

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_import_file_enrichments.list_import_file_enrichments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_import_file_enrichments_request.ListImportFileEnrichmentsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_import_file_enrichments(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.list_import_file_enrichments_filters.ListImportFileEnrichmentsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_mgn.types.import_file_enrichment.ImportFileEnrichment]":
        _token = next_token
        while True:
            _response = self.list_import_file_enrichments(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_managed_accounts(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.list_managed_accounts_response.ListManagedAccountsResponse":
        """<p>List Managed Accounts.</p>

        Args:
            max_results: <p>List managed accounts request max results.</p>
            next_token: <p>List managed accounts request next token.</p>

        Raises:
            aws_sdk_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_managed_accounts_request.ListManagedAccountsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_managed_accounts_response.ListManagedAccountsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_managed_accounts

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_managed_accounts.list_managed_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_managed_accounts_request.ListManagedAccountsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_managed_accounts(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_mgn.types.managed_account.ManagedAccount]":
        _token = next_token
        while True:
            _response = self.list_managed_accounts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_mgn.types.arn.ARN",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> (
        "aws_sdk_mgn.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>List all tags for your Application Migration Service resources.</p>

        Args:
            resource_arn: <p>List tags for resource request by ARN.</p>

        Raises:
            aws_sdk_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operating denied due to a file permission or access check error.</p>
            aws_sdk_mgn.errors.internal_server_exception.InternalServerException: <p>The server encountered an unexpected condition that prevented it from fulfilling the request.</p>
            aws_sdk_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            aws_sdk_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_import_file_enrichment(
        self,
        s3_bucket_source: "aws_sdk_mgn.types.enrichment_source_s3_configuration.EnrichmentSourceS3Configuration",
        s3_bucket_target: "aws_sdk_mgn.types.enrichment_target_s3_configuration.EnrichmentTargetS3Configuration",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mgn.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        ip_assignment_strategy: Optional[
            "aws_sdk_mgn.types.ip_assignment_strategy.IpAssignmentStrategy"
        ] = None,
    ) -> "aws_sdk_mgn.types.start_import_file_enrichment_response.StartImportFileEnrichmentResponse":
        """<p>Starts an import file enrichment job to process and enrich network migration import files with additional metadata and IP assignment strategies.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            s3_bucket_source: <p>The S3 configuration specifying the source location of the import file to be enriched.</p>
            s3_bucket_target: <p>The S3 configuration specifying the target location where the enriched import file will be stored.</p>
            ip_assignment_strategy: <p>The IP assignment strategy to use when enriching the import file. Can be STATIC or DYNAMIC.</p>

        Raises:
            aws_sdk_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operating denied due to a file permission or access check error.</p>
            aws_sdk_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            aws_sdk_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because its exceeded the service quota.</p>
            aws_sdk_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample StartImportFileEnrichment call

            >>> client.start_import_file_enrichment(s3_bucket_source={'s3Bucket': 'my-source-bucket', 's3BucketOwner': '123456789012', 's3Key': 'imports/source-file.csv'}, s3_bucket_target={'s3Bucket': 'my-target-bucket', 's3BucketOwner': '123456789012', 's3Key': 'enriched/output.csv'}, ip_assignment_strategy='STATIC')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.start_import_file_enrichment_request.StartImportFileEnrichmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.start_import_file_enrichment_response.StartImportFileEnrichmentResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_import_file_enrichment

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.start_import_file_enrichment.start_import_file_enrichment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.start_import_file_enrichment_request.StartImportFileEnrichmentRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["s3_bucket_source"] = s3_bucket_source
        input_["s3_bucket_target"] = s3_bucket_target
        if ip_assignment_strategy is not None:
            input_["ip_assignment_strategy"] = ip_assignment_strategy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_mgn.types.arn.ARN",
        tags: "aws_sdk_mgn.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> None:
        """<p>Adds or overwrites only the specified tags for the specified Application Migration Service resource or resources. When you specify an existing tag key, the value is overwritten with the new value. Each resource can have a maximum of 50 tags. Each tag consists of a key and optional value.</p>

        Args:
            resource_arn: <p>Tag resource by ARN.</p>
            tags: <p>Tag resource by Tags.</p>

        Raises:
            aws_sdk_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operating denied due to a file permission or access check error.</p>
            aws_sdk_mgn.errors.internal_server_exception.InternalServerException: <p>The server encountered an unexpected condition that prevented it from fulfilling the request.</p>
            aws_sdk_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            aws_sdk_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_mgn._operations.application_migration_service.tag_resource

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_mgn.types.arn.ARN",
        tag_keys: "aws_sdk_mgn.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified set of tags from the specified set of Application Migration Service resources.</p>

        Args:
            resource_arn: <p>Untag resource by ARN.</p>
            tag_keys: <p>Untag resource by Keys.</p>

        Raises:
            aws_sdk_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operating denied due to a file permission or access check error.</p>
            aws_sdk_mgn.errors.internal_server_exception.InternalServerException: <p>The server encountered an unexpected condition that prevented it from fulfilling the request.</p>
            aws_sdk_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            aws_sdk_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_mgn._operations.application_migration_service.untag_resource

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
