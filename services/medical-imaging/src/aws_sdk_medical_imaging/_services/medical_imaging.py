"""Generated from Smithy shape ``com.amazonaws.medicalimaging#AHIGatewayService``."""

import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_medical_imaging._auth._signers
import aws_sdk_medical_imaging._auth._sigv4
from aws_sdk_medical_imaging._auth._identity import Credentials
from aws_sdk_medical_imaging._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_medical_imaging._auth._zapros_handler import AuthMiddleware
from aws_sdk_medical_imaging._pagination import resolve_path as _resolve_path
from aws_sdk_medical_imaging._resources.ahi_gateway_service.datastore_resource import (
    DatastoreResource,
)
from aws_sdk_medical_imaging._resources.ahi_gateway_service.image_set_resource import (
    ImageSetResource,
)
from aws_sdk_medical_imaging._services._aws_config import aws_config
from aws_sdk_medical_imaging._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.arn
    import aws_sdk_medical_imaging.types.aws_account_id
    import aws_sdk_medical_imaging.types.client_token
    import aws_sdk_medical_imaging.types.copy_image_set_information
    import aws_sdk_medical_imaging.types.copy_image_set_request
    import aws_sdk_medical_imaging.types.copy_image_set_response
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.delete_image_set_request
    import aws_sdk_medical_imaging.types.delete_image_set_response
    import aws_sdk_medical_imaging.types.dicom_import_job_summary
    import aws_sdk_medical_imaging.types.get_dicom_import_job_request
    import aws_sdk_medical_imaging.types.get_dicom_import_job_response
    import aws_sdk_medical_imaging.types.get_image_frame_request
    import aws_sdk_medical_imaging.types.get_image_frame_response
    import aws_sdk_medical_imaging.types.get_image_set_metadata_request
    import aws_sdk_medical_imaging.types.get_image_set_metadata_response
    import aws_sdk_medical_imaging.types.get_image_set_request
    import aws_sdk_medical_imaging.types.get_image_set_response
    import aws_sdk_medical_imaging.types.image_frame_information
    import aws_sdk_medical_imaging.types.image_set_external_version_id
    import aws_sdk_medical_imaging.types.image_set_id
    import aws_sdk_medical_imaging.types.image_set_properties
    import aws_sdk_medical_imaging.types.image_sets_metadata_summary
    import aws_sdk_medical_imaging.types.import_configuration
    import aws_sdk_medical_imaging.types.job_id
    import aws_sdk_medical_imaging.types.job_name
    import aws_sdk_medical_imaging.types.job_status
    import aws_sdk_medical_imaging.types.list_dicom_import_jobs_request
    import aws_sdk_medical_imaging.types.list_dicom_import_jobs_response
    import aws_sdk_medical_imaging.types.list_image_set_versions_request
    import aws_sdk_medical_imaging.types.list_image_set_versions_response
    import aws_sdk_medical_imaging.types.list_tags_for_resource_request
    import aws_sdk_medical_imaging.types.list_tags_for_resource_response
    import aws_sdk_medical_imaging.types.metadata_updates
    import aws_sdk_medical_imaging.types.next_token
    import aws_sdk_medical_imaging.types.role_arn
    import aws_sdk_medical_imaging.types.s3_uri
    import aws_sdk_medical_imaging.types.search_criteria
    import aws_sdk_medical_imaging.types.search_image_sets_request
    import aws_sdk_medical_imaging.types.search_image_sets_response
    import aws_sdk_medical_imaging.types.start_dicom_import_job_request
    import aws_sdk_medical_imaging.types.start_dicom_import_job_response
    import aws_sdk_medical_imaging.types.tag_key_list
    import aws_sdk_medical_imaging.types.tag_map
    import aws_sdk_medical_imaging.types.tag_resource_request
    import aws_sdk_medical_imaging.types.tag_resource_response
    import aws_sdk_medical_imaging.types.untag_resource_request
    import aws_sdk_medical_imaging.types.untag_resource_response
    import aws_sdk_medical_imaging.types.update_image_set_metadata_request
    import aws_sdk_medical_imaging.types.update_image_set_metadata_response


class MedicalImagingClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class MedicalImagingClient:
    """A client for the ``MedicalImaging`` service.

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
        self._config = MedicalImagingClientConfig(
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
        self.datastore_resource = DatastoreResource(self)
        self.image_set_resource = ImageSetResource(self)

    def operation_options(
        self, config_overrides: Optional[MedicalImagingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MedicalImagingClientConfig = config_overrides or {}
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

    def copy_image_set(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        source_image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        copy_image_set_information: "aws_sdk_medical_imaging.types.copy_image_set_information.CopyImageSetInformation",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        force: Optional[bool] = None,
        promote_to_primary: Optional[bool] = None,
    ) -> "aws_sdk_medical_imaging.types.copy_image_set_response.CopyImageSetResponse":
        """<p>Copy an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            source_image_set_id: <p>The source image set identifier.</p>
            copy_image_set_information: <p>Copy image set information.</p>
            force: <p>Providing this parameter will force completion of the <code>CopyImageSet</code> operation, even if there are inconsistent Patient, Study, and/or Series level metadata elements between the <code>sourceImageSet</code> and <code>destinationImageSet</code>.</p>
            promote_to_primary: <p>Providing this parameter will configure the <code>CopyImageSet</code> operation to promote the given image set to the primary DICOM hierarchy. If successful, a new primary image set ID will be returned as the destination image set.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request caused a service quota to be exceeded.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.copy_image_set_request.CopyImageSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.copy_image_set_response.CopyImageSetResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.copy_image_set

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.copy_image_set.copy_image_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.copy_image_set_request.CopyImageSetRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        input_["source_image_set_id"] = source_image_set_id
        input_["copy_image_set_information"] = copy_image_set_information
        if force is not None:
            input_["force"] = force
        if promote_to_primary is not None:
            input_["promote_to_primary"] = promote_to_primary

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_image_set(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> (
        "aws_sdk_medical_imaging.types.delete_image_set_response.DeleteImageSetResponse"
    ):
        """<p>Delete an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.delete_image_set_request.DeleteImageSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.delete_image_set_response.DeleteImageSetResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.delete_image_set

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.delete_image_set.delete_image_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.delete_image_set_request.DeleteImageSetRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        input_["image_set_id"] = image_set_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_dicom_import_job(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        job_id: "aws_sdk_medical_imaging.types.job_id.JobId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.get_dicom_import_job_response.GetDICOMImportJobResponse":
        """<p>Get the import job properties to learn more about the job or job progress.</p> <note> <p>The <code>jobStatus</code> refers to the execution of the import job. Therefore, an import job can return a <code>jobStatus</code> as <code>COMPLETED</code> even if validation issues are discovered during the import process. If a <code>jobStatus</code> returns as <code>COMPLETED</code>, we still recommend you review the output manifests written to S3, as they provide details on the success or failure of individual P10 object imports.</p> </note>

        Args:
            datastore_id: <p>The data store identifier.</p>
            job_id: <p>The import job identifier.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.get_dicom_import_job_request.GetDICOMImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.get_dicom_import_job_response.GetDICOMImportJobResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.get_dicom_import_job

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.get_dicom_import_job.get_dicom_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.get_dicom_import_job_request.GetDICOMImportJobRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    @contextmanager
    def get_image_frame(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        image_frame_information: "aws_sdk_medical_imaging.types.image_frame_information.ImageFrameInformation",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "Generator[aws_sdk_medical_imaging.types.get_image_frame_response.GetImageFrameResponse]":
        """<p>Get an image frame (pixel data) for an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            image_frame_information: <p>Information about the image frame (pixel data) identifier.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.not_acceptable_exception.NotAcceptableException: <p>The request content type or accept header is not supported.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.get_image_frame_request.GetImageFrameRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.get_image_frame_response.GetImageFrameResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_frame

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_frame.get_image_frame(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.get_image_frame_request.GetImageFrameRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        input_["image_set_id"] = image_set_id
        input_["image_frame_information"] = image_frame_information

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    def get_image_set(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        version_id: Optional[
            "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
        ] = None,
    ) -> "aws_sdk_medical_imaging.types.get_image_set_response.GetImageSetResponse":
        """<p>Get image set properties.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            version_id: <p>The image set version identifier.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.get_image_set_request.GetImageSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.get_image_set_response.GetImageSetResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_set

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_set.get_image_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.get_image_set_request.GetImageSetRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        input_["image_set_id"] = image_set_id
        if version_id is not None:
            input_["version_id"] = version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    @contextmanager
    def get_image_set_metadata(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        version_id: Optional[
            "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
        ] = None,
    ) -> "Generator[aws_sdk_medical_imaging.types.get_image_set_metadata_response.GetImageSetMetadataResponse]":
        """<p>Get metadata attributes for an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            version_id: <p>The image set version identifier.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.get_image_set_metadata_request.GetImageSetMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.get_image_set_metadata_response.GetImageSetMetadataResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_set_metadata

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_set_metadata.get_image_set_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.get_image_set_metadata_request.GetImageSetMetadataRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        input_["image_set_id"] = image_set_id
        if version_id is not None:
            input_["version_id"] = version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    def list_dicom_import_jobs(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        job_status: Optional[
            "aws_sdk_medical_imaging.types.job_status.JobStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_medical_imaging.types.list_dicom_import_jobs_response.ListDICOMImportJobsResponse":
        """<p>List import jobs created for a specific data store.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            job_status: <p>The filters for listing import jobs based on status.</p>
            next_token: <p>The pagination token used to request the list of import jobs on the next page.</p>
            max_results: <p>The max results count. The upper bound is determined by load testing.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.list_dicom_import_jobs_request.ListDICOMImportJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.list_dicom_import_jobs_response.ListDICOMImportJobsResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.list_dicom_import_jobs

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.list_dicom_import_jobs.list_dicom_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.list_dicom_import_jobs_request.ListDICOMImportJobsRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        if job_status is not None:
            input_["job_status"] = job_status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_dicom_import_jobs(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        job_status: Optional[
            "aws_sdk_medical_imaging.types.job_status.JobStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[aws_sdk_medical_imaging.types.dicom_import_job_summary.DICOMImportJobSummary]":
        _token = next_token
        while True:
            _response = self.list_dicom_import_jobs(
                datastore_id,
                config_overrides=config_overrides,
                job_status=job_status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_image_set_versions(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_medical_imaging.types.list_image_set_versions_response.ListImageSetVersionsResponse":
        """<p>List image set versions.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            next_token: <p>The pagination token used to request the list of image set versions on the next page.</p>
            max_results: <p>The max results count.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.list_image_set_versions_request.ListImageSetVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.list_image_set_versions_response.ListImageSetVersionsResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.list_image_set_versions

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.list_image_set_versions.list_image_set_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.list_image_set_versions_request.ListImageSetVersionsRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        input_["image_set_id"] = image_set_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_image_set_versions(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[aws_sdk_medical_imaging.types.image_set_properties.ImageSetProperties]":
        _token = next_token
        while True:
            _response = self.list_image_set_versions(
                datastore_id,
                image_set_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("image_set_properties_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_medical_imaging.types.arn.Arn",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a medical imaging resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the medical imaging resource to list tags for.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_image_sets(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        search_criteria: Optional[
            "aws_sdk_medical_imaging.types.search_criteria.SearchCriteria"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_medical_imaging.types.search_image_sets_response.SearchImageSetsResponse":
        """<p>Search image sets based on defined input attributes.</p> <note> <p> <code>SearchImageSets</code> accepts a single search query parameter and returns a paginated response of all image sets that have the matching criteria. All date range queries must be input as <code>(lowerBound, upperBound)</code>.</p> <p>By default, <code>SearchImageSets</code> uses the <code>updatedAt</code> field for sorting in descending order from newest to oldest.</p> </note>

        Args:
            datastore_id: <p>The identifier of the data store where the image sets reside.</p>
            search_criteria: <p>The search criteria that filters by applying a maximum of 1 item to <code>SearchByAttribute</code>.</p>
            max_results: <p>The maximum number of results that can be returned in a search.</p>
            next_token: <p>The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.search_image_sets_request.SearchImageSetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.search_image_sets_response.SearchImageSetsResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.search_image_sets

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.search_image_sets.search_image_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.search_image_sets_request.SearchImageSetsRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        if search_criteria is not None:
            input_["search_criteria"] = search_criteria
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

    def iter_search_image_sets(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        search_criteria: Optional[
            "aws_sdk_medical_imaging.types.search_criteria.SearchCriteria"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_medical_imaging.types.image_sets_metadata_summary.ImageSetsMetadataSummary]":
        _token = next_token
        while True:
            _response = self.search_image_sets(
                datastore_id,
                config_overrides=config_overrides,
                search_criteria=search_criteria,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("image_sets_metadata_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_dicom_import_job(
        self,
        data_access_role_arn: "aws_sdk_medical_imaging.types.role_arn.RoleArn",
        client_token: "aws_sdk_medical_imaging.types.client_token.ClientToken",
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        input_s3_uri: "aws_sdk_medical_imaging.types.s3_uri.S3Uri",
        output_s3_uri: "aws_sdk_medical_imaging.types.s3_uri.S3Uri",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        job_name: Optional["aws_sdk_medical_imaging.types.job_name.JobName"] = None,
        input_owner_account_id: Optional[
            "aws_sdk_medical_imaging.types.aws_account_id.AwsAccountId"
        ] = None,
        import_configuration: Optional[
            "aws_sdk_medical_imaging.types.import_configuration.ImportConfiguration"
        ] = None,
    ) -> "aws_sdk_medical_imaging.types.start_dicom_import_job_response.StartDICOMImportJobResponse":
        """<p>Start importing bulk data into an <code>ACTIVE</code> data store. The import job imports DICOM P10 files or enhances existing DICOM files with JSON metadata. The <code>importConfiguration</code> parameter specifies the import type. The data is found in the S3 prefix specified by the <code>inputS3Uri</code> parameter. The import job stores processing results in the file specified by the <code>outputS3Uri</code> parameter.</p>

        Args:
            job_name: <p>The import job name.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants permission to access medical imaging resources.</p>
            client_token: <p>A unique identifier for API idempotency.</p>
            datastore_id: <p>The data store identifier.</p>
            input_s3_uri: <p>The input prefix path for the S3 bucket that contains the DICOM files to be imported.</p>
            output_s3_uri: <p>The output prefix of the S3 bucket to upload the results of the DICOM import job.</p>
            input_owner_account_id: <p>The account ID of the source S3 bucket owner.</p>
            import_configuration: <p>The import configuration for the import job.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request caused a service quota to be exceeded.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.start_dicom_import_job_request.StartDICOMImportJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.start_dicom_import_job_response.StartDICOMImportJobResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.start_dicom_import_job

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.start_dicom_import_job.start_dicom_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.start_dicom_import_job_request.StartDICOMImportJobRequest = {}  # type: ignore[typeddict-item]
        if job_name is not None:
            input_["job_name"] = job_name
        input_["data_access_role_arn"] = data_access_role_arn
        input_["client_token"] = client_token
        input_["datastore_id"] = datastore_id
        input_["input_s3_uri"] = input_s3_uri
        input_["output_s3_uri"] = output_s3_uri
        if input_owner_account_id is not None:
            input_["input_owner_account_id"] = input_owner_account_id
        if import_configuration is not None:
            input_["import_configuration"] = import_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_medical_imaging.types.arn.Arn",
        tags: "aws_sdk_medical_imaging.types.tag_map.TagMap",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a user-specifed key and value tag to a medical imaging resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to.</p>
            tags: <p>The user-specified key and value tag pairs added to a medical imaging resource.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.tag_resource

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_medical_imaging.types.arn.Arn",
        tag_keys: "aws_sdk_medical_imaging.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a medical imaging resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from.</p>
            tag_keys: <p>The keys for the tags to be removed from the medical imaging resource.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.untag_resource

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_image_set_metadata(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        latest_version_id: "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId",
        update_image_set_metadata_updates: "aws_sdk_medical_imaging.types.metadata_updates.MetadataUpdates",
        *,
        config_overrides: Optional[MedicalImagingClientConfig] = None,
        force: Optional[bool] = None,
        include_study_image_sets: Optional[bool] = None,
    ) -> "aws_sdk_medical_imaging.types.update_image_set_metadata_response.UpdateImageSetMetadataResponse":
        """<p>Update image set metadata attributes.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            latest_version_id: <p>The latest image set version identifier.</p>
            force: <p>Setting this flag will force the <code>UpdateImageSetMetadata</code> operation for the following attributes:</p> <ul> <li> <p> <code>Tag.StudyInstanceUID</code>, <code>Tag.SeriesInstanceUID</code>, <code>Tag.SOPInstanceUID</code>, and <code>Tag.StudyID</code> </p> </li> <li> <p>Adding, removing, or updating private tags for an individual SOP Instance</p> </li> </ul>
            include_study_image_sets: <p>Flag to apply the metadata updates to all image sets in the same Study as the requested image set ID.</p>
            update_image_set_metadata_updates: <p>Update image set metadata updates.</p>

        Raises:
            aws_sdk_medical_imaging.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_medical_imaging.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_medical_imaging.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of the request.</p>
            aws_sdk_medical_imaging.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_medical_imaging.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request caused a service quota to be exceeded.</p>
            aws_sdk_medical_imaging.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling.</p>
            aws_sdk_medical_imaging.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints set by the service.</p>
            aws_sdk_medical_imaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_medical_imaging.types.update_image_set_metadata_request.UpdateImageSetMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_medical_imaging.types.update_image_set_metadata_response.UpdateImageSetMetadataResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.update_image_set_metadata

            output, http_response = (
                aws_sdk_medical_imaging._operations.ahi_gateway_service.update_image_set_metadata.update_image_set_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_medical_imaging.types.update_image_set_metadata_request.UpdateImageSetMetadataRequest = {}  # type: ignore[typeddict-item]
        input_["datastore_id"] = datastore_id
        input_["image_set_id"] = image_set_id
        input_["latest_version_id"] = latest_version_id
        if force is not None:
            input_["force"] = force
        if include_study_image_sets is not None:
            input_["include_study_image_sets"] = include_study_image_sets
        input_["update_image_set_metadata_updates"] = update_image_set_metadata_updates

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
