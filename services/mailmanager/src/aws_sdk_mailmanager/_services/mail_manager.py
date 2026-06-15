"""Generated from Smithy shape ``com.amazonaws.mailmanager#MailManagerSvc``."""

import datetime
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_mailmanager._auth._signers
import aws_sdk_mailmanager._auth._sigv4
from aws_sdk_mailmanager._auth._identity import Credentials
from aws_sdk_mailmanager._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_mailmanager._auth._zapros_handler import AuthMiddleware
from aws_sdk_mailmanager._pagination import resolve_path as _resolve_path
from aws_sdk_mailmanager._resources.mail_manager_svc.addon_instance_resource import (
    AddonInstanceResource,
)
from aws_sdk_mailmanager._resources.mail_manager_svc.addon_subscription_resource import (
    AddonSubscriptionResource,
)
from aws_sdk_mailmanager._resources.mail_manager_svc.address_list_resource import (
    AddressListResource,
)
from aws_sdk_mailmanager._resources.mail_manager_svc.archive_resource import (
    ArchiveResource,
)
from aws_sdk_mailmanager._resources.mail_manager_svc.ingress_point_resource import (
    IngressPointResource,
)
from aws_sdk_mailmanager._resources.mail_manager_svc.relay_resource import RelayResource
from aws_sdk_mailmanager._resources.mail_manager_svc.rule_set_resource import (
    RuleSetResource,
)
from aws_sdk_mailmanager._resources.mail_manager_svc.traffic_policy_resource import (
    TrafficPolicyResource,
)
from aws_sdk_mailmanager._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.address
    import aws_sdk_mailmanager.types.address_filter
    import aws_sdk_mailmanager.types.address_list_id
    import aws_sdk_mailmanager.types.address_page_size
    import aws_sdk_mailmanager.types.archive_filters
    import aws_sdk_mailmanager.types.archive_id
    import aws_sdk_mailmanager.types.archived_message_id
    import aws_sdk_mailmanager.types.create_address_list_import_job_request
    import aws_sdk_mailmanager.types.create_address_list_import_job_response
    import aws_sdk_mailmanager.types.deregister_member_from_address_list_request
    import aws_sdk_mailmanager.types.deregister_member_from_address_list_response
    import aws_sdk_mailmanager.types.export_destination_configuration
    import aws_sdk_mailmanager.types.export_id
    import aws_sdk_mailmanager.types.export_max_results
    import aws_sdk_mailmanager.types.export_summary
    import aws_sdk_mailmanager.types.get_address_list_import_job_request
    import aws_sdk_mailmanager.types.get_address_list_import_job_response
    import aws_sdk_mailmanager.types.get_archive_export_request
    import aws_sdk_mailmanager.types.get_archive_export_response
    import aws_sdk_mailmanager.types.get_archive_message_content_request
    import aws_sdk_mailmanager.types.get_archive_message_content_response
    import aws_sdk_mailmanager.types.get_archive_message_request
    import aws_sdk_mailmanager.types.get_archive_message_response
    import aws_sdk_mailmanager.types.get_archive_search_request
    import aws_sdk_mailmanager.types.get_archive_search_response
    import aws_sdk_mailmanager.types.get_archive_search_results_request
    import aws_sdk_mailmanager.types.get_archive_search_results_response
    import aws_sdk_mailmanager.types.get_member_of_address_list_request
    import aws_sdk_mailmanager.types.get_member_of_address_list_response
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.import_data_format
    import aws_sdk_mailmanager.types.import_job
    import aws_sdk_mailmanager.types.job_id
    import aws_sdk_mailmanager.types.job_name
    import aws_sdk_mailmanager.types.list_address_list_import_jobs_request
    import aws_sdk_mailmanager.types.list_address_list_import_jobs_response
    import aws_sdk_mailmanager.types.list_archive_exports_request
    import aws_sdk_mailmanager.types.list_archive_exports_response
    import aws_sdk_mailmanager.types.list_archive_searches_request
    import aws_sdk_mailmanager.types.list_archive_searches_response
    import aws_sdk_mailmanager.types.list_members_of_address_list_request
    import aws_sdk_mailmanager.types.list_members_of_address_list_response
    import aws_sdk_mailmanager.types.list_tags_for_resource_request
    import aws_sdk_mailmanager.types.list_tags_for_resource_response
    import aws_sdk_mailmanager.types.page_size
    import aws_sdk_mailmanager.types.pagination_token
    import aws_sdk_mailmanager.types.register_member_to_address_list_request
    import aws_sdk_mailmanager.types.register_member_to_address_list_response
    import aws_sdk_mailmanager.types.saved_address
    import aws_sdk_mailmanager.types.search_id
    import aws_sdk_mailmanager.types.search_max_results
    import aws_sdk_mailmanager.types.search_summary
    import aws_sdk_mailmanager.types.start_address_list_import_job_request
    import aws_sdk_mailmanager.types.start_address_list_import_job_response
    import aws_sdk_mailmanager.types.start_archive_export_request
    import aws_sdk_mailmanager.types.start_archive_export_response
    import aws_sdk_mailmanager.types.start_archive_search_request
    import aws_sdk_mailmanager.types.start_archive_search_response
    import aws_sdk_mailmanager.types.stop_address_list_import_job_request
    import aws_sdk_mailmanager.types.stop_address_list_import_job_response
    import aws_sdk_mailmanager.types.stop_archive_export_request
    import aws_sdk_mailmanager.types.stop_archive_export_response
    import aws_sdk_mailmanager.types.stop_archive_search_request
    import aws_sdk_mailmanager.types.stop_archive_search_response
    import aws_sdk_mailmanager.types.tag_key_list
    import aws_sdk_mailmanager.types.tag_list
    import aws_sdk_mailmanager.types.tag_resource_request
    import aws_sdk_mailmanager.types.tag_resource_response
    import aws_sdk_mailmanager.types.taggable_resource_arn
    import aws_sdk_mailmanager.types.untag_resource_request
    import aws_sdk_mailmanager.types.untag_resource_response


class MailManagerClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class MailManagerClient:
    """A client for the ``MailManager`` service.

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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = MailManagerClientConfig(
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

        # resources
        self.addon_instance_resource = AddonInstanceResource(self)
        self.addon_subscription_resource = AddonSubscriptionResource(self)
        self.address_list_resource = AddressListResource(self)
        self.archive_resource = ArchiveResource(self)
        self.ingress_point_resource = IngressPointResource(self)
        self.relay_resource = RelayResource(self)
        self.rule_set_resource = RuleSetResource(self)
        self.traffic_policy_resource = TrafficPolicyResource(self)

    def operation_options(
        self, config_overrides: Optional[MailManagerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MailManagerClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    def create_address_list_import_job(
        self,
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        name: "aws_sdk_mailmanager.types.job_name.JobName",
        import_data_format: "aws_sdk_mailmanager.types.import_data_format.ImportDataFormat",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.create_address_list_import_job_response.CreateAddressListImportJobResponse":
        """<p>Creates an import job for an address list.</p>

        Args:
            client_token: <p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>
            address_list_id: <p>The unique identifier of the address list for importing addresses to.</p>
            name: <p>A user-friendly name for the import job.</p>
            import_data_format: <p>The format of the input for an import job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.create_address_list_import_job_request.CreateAddressListImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.create_address_list_import_job_response.CreateAddressListImportJobResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.create_address_list_import_job

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.create_address_list_import_job.create_address_list_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.create_address_list_import_job_request.CreateAddressListImportJobRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["address_list_id"] = address_list_id
        input_["name"] = name
        input_["import_data_format"] = import_data_format

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_member_from_address_list(
        self,
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        address: "aws_sdk_mailmanager.types.address.Address",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.deregister_member_from_address_list_response.DeregisterMemberFromAddressListResponse":
        """<p>Removes a member from an address list.</p>

        Args:
            address_list_id: <p>The unique identifier of the address list to remove the address from.</p>
            address: <p>The address to be removed from the address list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.deregister_member_from_address_list_request.DeregisterMemberFromAddressListRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.deregister_member_from_address_list_response.DeregisterMemberFromAddressListResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.deregister_member_from_address_list

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.deregister_member_from_address_list.deregister_member_from_address_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.deregister_member_from_address_list_request.DeregisterMemberFromAddressListRequest = {}  # type: ignore[typeddict-item]
        input_["address_list_id"] = address_list_id
        input_["address"] = address

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_address_list_import_job(
        self,
        job_id: "aws_sdk_mailmanager.types.job_id.JobId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_address_list_import_job_response.GetAddressListImportJobResponse":
        """<p>Fetch attributes of an import job.</p>

        Args:
            job_id: <p>The identifier of the import job that needs to be retrieved.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_address_list_import_job_request.GetAddressListImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_address_list_import_job_response.GetAddressListImportJobResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_address_list_import_job

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_address_list_import_job.get_address_list_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_address_list_import_job_request.GetAddressListImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_archive_export(
        self,
        export_id: "aws_sdk_mailmanager.types.export_id.ExportId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> (
        "aws_sdk_mailmanager.types.get_archive_export_response.GetArchiveExportResponse"
    ):
        """<p>Retrieves the details and current status of a specific email archive export job.</p>

        Args:
            export_id: <p>The identifier of the export job to get details for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_archive_export_request.GetArchiveExportRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_archive_export_response.GetArchiveExportResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_archive_export

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_archive_export.get_archive_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_archive_export_request.GetArchiveExportRequest = {}  # type: ignore[typeddict-item]
        input_["export_id"] = export_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_archive_message(
        self,
        archived_message_id: "aws_sdk_mailmanager.types.archived_message_id.ArchivedMessageId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_archive_message_response.GetArchiveMessageResponse":
        """<p>Returns a pre-signed URL that provides temporary download access to the specific email message stored in the archive. </p>

        Args:
            archived_message_id: <p>The unique identifier of the archived email message.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_archive_message_request.GetArchiveMessageRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_archive_message_response.GetArchiveMessageResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_archive_message

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_archive_message.get_archive_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_archive_message_request.GetArchiveMessageRequest = {}  # type: ignore[typeddict-item]
        input_["archived_message_id"] = archived_message_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_archive_message_content(
        self,
        archived_message_id: "aws_sdk_mailmanager.types.archived_message_id.ArchivedMessageId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_archive_message_content_response.GetArchiveMessageContentResponse":
        """<p>Returns the textual content of a specific email message stored in the archive. Attachments are not included. </p>

        Args:
            archived_message_id: <p>The unique identifier of the archived email message.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_archive_message_content_request.GetArchiveMessageContentRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_archive_message_content_response.GetArchiveMessageContentResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_archive_message_content

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_archive_message_content.get_archive_message_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_archive_message_content_request.GetArchiveMessageContentRequest = {}  # type: ignore[typeddict-item]
        input_["archived_message_id"] = archived_message_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_archive_search(
        self,
        search_id: "aws_sdk_mailmanager.types.search_id.SearchId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> (
        "aws_sdk_mailmanager.types.get_archive_search_response.GetArchiveSearchResponse"
    ):
        """<p>Retrieves the details and current status of a specific email archive search job.</p>

        Args:
            search_id: <p>The identifier of the search job to get details for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_archive_search_request.GetArchiveSearchRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_archive_search_response.GetArchiveSearchResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_archive_search

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_archive_search.get_archive_search(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_archive_search_request.GetArchiveSearchRequest = {}  # type: ignore[typeddict-item]
        input_["search_id"] = search_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_archive_search_results(
        self,
        search_id: "aws_sdk_mailmanager.types.search_id.SearchId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_archive_search_results_response.GetArchiveSearchResultsResponse":
        """<p>Returns the results of a completed email archive search job.</p>

        Args:
            search_id: <p>The identifier of the completed search job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_archive_search_results_request.GetArchiveSearchResultsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_archive_search_results_response.GetArchiveSearchResultsResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_archive_search_results

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_archive_search_results.get_archive_search_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_archive_search_results_request.GetArchiveSearchResultsRequest = {}  # type: ignore[typeddict-item]
        input_["search_id"] = search_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_member_of_address_list(
        self,
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        address: "aws_sdk_mailmanager.types.address.Address",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.get_member_of_address_list_response.GetMemberOfAddressListResponse":
        """<p>Fetch attributes of a member in an address list.</p>

        Args:
            address_list_id: <p>The unique identifier of the address list to retrieve the address from.</p>
            address: <p>The address to be retrieved from the address list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.get_member_of_address_list_request.GetMemberOfAddressListRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.get_member_of_address_list_response.GetMemberOfAddressListResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.get_member_of_address_list

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.get_member_of_address_list.get_member_of_address_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.get_member_of_address_list_request.GetMemberOfAddressListRequest = {}  # type: ignore[typeddict-item]
        input_["address_list_id"] = address_list_id
        input_["address"] = address

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_address_list_import_jobs(
        self,
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_mailmanager.types.list_address_list_import_jobs_response.ListAddressListImportJobsResponse":
        """<p>Lists jobs for an address list.</p>

        Args:
            address_list_id: <p>The unique identifier of the address list for listing import jobs.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of import jobs that are returned per call. You can use NextToken to retrieve the next page of jobs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_address_list_import_jobs_request.ListAddressListImportJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_address_list_import_jobs_response.ListAddressListImportJobsResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_address_list_import_jobs

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_address_list_import_jobs.list_address_list_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_address_list_import_jobs_request.ListAddressListImportJobsRequest = {}  # type: ignore[typeddict-item]
        input_["address_list_id"] = address_list_id
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_address_list_import_jobs(
        self,
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
    ) -> "Iterator[aws_sdk_mailmanager.types.import_job.ImportJob]":
        _token = next_token
        while True:
            _response = self.list_address_list_import_jobs(
                address_list_id,
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("import_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_archive_exports(
        self,
        archive_id: "aws_sdk_mailmanager.types.archive_id.ArchiveId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_mailmanager.types.list_archive_exports_response.ListArchiveExportsResponse":
        """<p>Returns a list of email archive export jobs.</p>

        Args:
            archive_id: <p>The identifier of the archive.</p>
            next_token: <p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. </p>
            page_size: <p>The maximum number of archive export jobs that are returned per call. You can use NextToken to obtain further pages of archives. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_archive_exports_request.ListArchiveExportsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_archive_exports_response.ListArchiveExportsResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_archive_exports

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_archive_exports.list_archive_exports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_archive_exports_request.ListArchiveExportsRequest = {}  # type: ignore[typeddict-item]
        input_["archive_id"] = archive_id
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_archive_exports(
        self,
        archive_id: "aws_sdk_mailmanager.types.archive_id.ArchiveId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
    ) -> "Iterator[aws_sdk_mailmanager.types.export_summary.ExportSummary]":
        _token = next_token
        while True:
            _response = self.list_archive_exports(
                archive_id,
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("exports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_archive_searches(
        self,
        archive_id: "aws_sdk_mailmanager.types.archive_id.ArchiveId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
    ) -> "aws_sdk_mailmanager.types.list_archive_searches_response.ListArchiveSearchesResponse":
        """<p>Returns a list of email archive search jobs.</p>

        Args:
            archive_id: <p>The identifier of the archive.</p>
            next_token: <p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. </p>
            page_size: <p>The maximum number of archive search jobs that are returned per call. You can use NextToken to obtain further pages of archives. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_archive_searches_request.ListArchiveSearchesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_archive_searches_response.ListArchiveSearchesResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_archive_searches

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_archive_searches.list_archive_searches(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_archive_searches_request.ListArchiveSearchesRequest = {}  # type: ignore[typeddict-item]
        input_["archive_id"] = archive_id
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_archive_searches(
        self,
        archive_id: "aws_sdk_mailmanager.types.archive_id.ArchiveId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional["aws_sdk_mailmanager.types.page_size.PageSize"] = None,
    ) -> "Iterator[aws_sdk_mailmanager.types.search_summary.SearchSummary]":
        _token = next_token
        while True:
            _response = self.list_archive_searches(
                archive_id,
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("searches",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_members_of_address_list(
        self,
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        filter: Optional[
            "aws_sdk_mailmanager.types.address_filter.AddressFilter"
        ] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional[
            "aws_sdk_mailmanager.types.address_page_size.AddressPageSize"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.list_members_of_address_list_response.ListMembersOfAddressListResponse":
        """<p>Lists members of an address list.</p>

        Args:
            address_list_id: <p>The unique identifier of the address list to list the addresses from.</p>
            filter: <p>Filter to be used to limit the results.</p>
            next_token: <p>If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.</p>
            page_size: <p>The maximum number of address list members that are returned per call. You can use NextToken to retrieve the next page of members.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_members_of_address_list_request.ListMembersOfAddressListRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_members_of_address_list_response.ListMembersOfAddressListResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_members_of_address_list

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_members_of_address_list.list_members_of_address_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_members_of_address_list_request.ListMembersOfAddressListRequest = {}  # type: ignore[typeddict-item]
        input_["address_list_id"] = address_list_id
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_members_of_address_list(
        self,
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        filter: Optional[
            "aws_sdk_mailmanager.types.address_filter.AddressFilter"
        ] = None,
        next_token: Optional[
            "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
        ] = None,
        page_size: Optional[
            "aws_sdk_mailmanager.types.address_page_size.AddressPageSize"
        ] = None,
    ) -> "Iterator[aws_sdk_mailmanager.types.saved_address.SavedAddress]":
        _token = next_token
        while True:
            _response = self.list_members_of_address_list(
                address_list_id,
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("addresses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_mailmanager.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Retrieves the list of tags (keys and values) assigned to the resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to retrieve tags from.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.list_tags_for_resource

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_member_to_address_list(
        self,
        address_list_id: "aws_sdk_mailmanager.types.address_list_id.AddressListId",
        address: "aws_sdk_mailmanager.types.address.Address",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.register_member_to_address_list_response.RegisterMemberToAddressListResponse":
        """<p>Adds a member to an address list.</p>

        Args:
            address_list_id: <p>The unique identifier of the address list where the address should be added.</p>
            address: <p>The address to be added to the address list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.register_member_to_address_list_request.RegisterMemberToAddressListRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.register_member_to_address_list_response.RegisterMemberToAddressListResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.register_member_to_address_list

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.register_member_to_address_list.register_member_to_address_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.register_member_to_address_list_request.RegisterMemberToAddressListRequest = {}  # type: ignore[typeddict-item]
        input_["address_list_id"] = address_list_id
        input_["address"] = address

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_address_list_import_job(
        self,
        job_id: "aws_sdk_mailmanager.types.job_id.JobId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.start_address_list_import_job_response.StartAddressListImportJobResponse":
        """<p>Starts an import job for an address list.</p>

        Args:
            job_id: <p>The identifier of the import job that needs to be started.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.start_address_list_import_job_request.StartAddressListImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.start_address_list_import_job_response.StartAddressListImportJobResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.start_address_list_import_job

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.start_address_list_import_job.start_address_list_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.start_address_list_import_job_request.StartAddressListImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_archive_export(
        self,
        archive_id: "aws_sdk_mailmanager.types.archive_id.ArchiveId",
        from_timestamp: datetime.datetime,
        to_timestamp: datetime.datetime,
        export_destination_configuration: "aws_sdk_mailmanager.types.export_destination_configuration.ExportDestinationConfiguration",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        filters: Optional[
            "aws_sdk_mailmanager.types.archive_filters.ArchiveFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mailmanager.types.export_max_results.ExportMaxResults"
        ] = None,
        include_metadata: Optional[bool] = None,
    ) -> "aws_sdk_mailmanager.types.start_archive_export_response.StartArchiveExportResponse":
        """<p>Initiates an export of emails from the specified archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to export emails from.</p>
            filters: <p>Criteria to filter which emails are included in the export.</p>
            from_timestamp: <p>The start of the timestamp range to include emails from.</p>
            to_timestamp: <p>The end of the timestamp range to include emails from.</p>
            max_results: <p>The maximum number of email items to include in the export.</p>
            export_destination_configuration: <p>Details on where to deliver the exported email data.</p>
            include_metadata: <p>Whether to include message metadata as JSON files in the export.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.start_archive_export_request.StartArchiveExportRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.start_archive_export_response.StartArchiveExportResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.start_archive_export

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.start_archive_export.start_archive_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.start_archive_export_request.StartArchiveExportRequest = {}  # type: ignore[typeddict-item]
        input_["archive_id"] = archive_id
        if filters is not None:
            input_["filters"] = filters
        input_["from_timestamp"] = from_timestamp
        input_["to_timestamp"] = to_timestamp
        if max_results is not None:
            input_["max_results"] = max_results
        input_["export_destination_configuration"] = export_destination_configuration
        if include_metadata is not None:
            input_["include_metadata"] = include_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_archive_search(
        self,
        archive_id: "aws_sdk_mailmanager.types.archive_id.ArchiveId",
        from_timestamp: datetime.datetime,
        to_timestamp: datetime.datetime,
        max_results: "aws_sdk_mailmanager.types.search_max_results.SearchMaxResults",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
        filters: Optional[
            "aws_sdk_mailmanager.types.archive_filters.ArchiveFilters"
        ] = None,
    ) -> "aws_sdk_mailmanager.types.start_archive_search_response.StartArchiveSearchResponse":
        """<p>Initiates a search across emails in the specified archive.</p>

        Args:
            archive_id: <p>The identifier of the archive to search emails in.</p>
            filters: <p>Criteria to filter which emails are included in the search results.</p>
            from_timestamp: <p>The start timestamp of the range to search emails from.</p>
            to_timestamp: <p>The end timestamp of the range to search emails from.</p>
            max_results: <p>The maximum number of search results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.start_archive_search_request.StartArchiveSearchRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.start_archive_search_response.StartArchiveSearchResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.start_archive_search

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.start_archive_search.start_archive_search(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.start_archive_search_request.StartArchiveSearchRequest = {}  # type: ignore[typeddict-item]
        input_["archive_id"] = archive_id
        if filters is not None:
            input_["filters"] = filters
        input_["from_timestamp"] = from_timestamp
        input_["to_timestamp"] = to_timestamp
        input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_address_list_import_job(
        self,
        job_id: "aws_sdk_mailmanager.types.job_id.JobId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.stop_address_list_import_job_response.StopAddressListImportJobResponse":
        """<p>Stops an ongoing import job for an address list.</p>

        Args:
            job_id: <p>The identifier of the import job that needs to be stopped.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.stop_address_list_import_job_request.StopAddressListImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.stop_address_list_import_job_response.StopAddressListImportJobResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.stop_address_list_import_job

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.stop_address_list_import_job.stop_address_list_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.stop_address_list_import_job_request.StopAddressListImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_archive_export(
        self,
        export_id: "aws_sdk_mailmanager.types.export_id.ExportId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.stop_archive_export_response.StopArchiveExportResponse":
        """<p>Stops an in-progress export of emails from an archive.</p>

        Args:
            export_id: <p>The identifier of the export job to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.stop_archive_export_request.StopArchiveExportRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.stop_archive_export_response.StopArchiveExportResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.stop_archive_export

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.stop_archive_export.stop_archive_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.stop_archive_export_request.StopArchiveExportRequest = {}  # type: ignore[typeddict-item]
        input_["export_id"] = export_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_archive_search(
        self,
        search_id: "aws_sdk_mailmanager.types.search_id.SearchId",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.stop_archive_search_response.StopArchiveSearchResponse":
        """<p>Stops an in-progress archive search job.</p>

        Args:
            search_id: <p>The identifier of the search job to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.stop_archive_search_request.StopArchiveSearchRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.stop_archive_search_response.StopArchiveSearchResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.stop_archive_search

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.stop_archive_search.stop_archive_search(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.stop_archive_search_request.StopArchiveSearchRequest = {}  # type: ignore[typeddict-item]
        input_["search_id"] = search_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_mailmanager.types.taggable_resource_arn.TaggableResourceArn",
        tags: "aws_sdk_mailmanager.types.tag_list.TagList",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.tag_resource_response.TagResourceResponse":
        r"""<p> Adds one or more tags (keys and values) to a specified resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that you want to tag. </p>
            tags: <p> The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.tag_resource

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_mailmanager.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "aws_sdk_mailmanager.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[MailManagerClientConfig] = None,
    ) -> "aws_sdk_mailmanager.types.untag_resource_response.UntagResourceResponse":
        """<p> Remove one or more tags (keys and values) from a specified resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that you want to untag. </p>
            tag_keys: <p> The keys of the key-value pairs for the tag or tags you want to remove from the specified resource. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mailmanager.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mailmanager.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_mailmanager._operations.mail_manager_svc.untag_resource

            output, http_response = (
                aws_sdk_mailmanager._operations.mail_manager_svc.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mailmanager.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
