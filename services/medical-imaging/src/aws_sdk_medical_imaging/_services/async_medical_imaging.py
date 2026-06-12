"""Generated from Smithy shape ``com.amazonaws.medicalimaging#AHIGatewayService``."""

import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_medical_imaging._auth._signers
import aws_sdk_medical_imaging._auth._sigv4
from aws_sdk_medical_imaging._auth._identity import Credentials
from aws_sdk_medical_imaging._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_medical_imaging._auth._zapros_handler import AuthMiddleware
from aws_sdk_medical_imaging._pagination import resolve_path as _resolve_path
from aws_sdk_medical_imaging._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
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


class AsyncMedicalImagingClientConfig(TypedDict, total=False):
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


class AsyncMedicalImagingClient:
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
        self.config = AsyncMedicalImagingClientConfig(
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
        self, config_overrides: Optional[AsyncMedicalImagingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMedicalImagingClientConfig = config_overrides or {}
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

    async def copy_image_set(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        source_image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        copy_image_set_information: "aws_sdk_medical_imaging.types.copy_image_set_information.CopyImageSetInformation",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
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
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.copy_image_set_request.CopyImageSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.copy_image_set_response.CopyImageSetResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.copy_image_set

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.copy_image_set.async_copy_image_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.copy_image_set_request.CopyImageSetRequest = {}  # type: ignore[typeddict-item]
        input["datastore_id"] = datastore_id
        input["source_image_set_id"] = source_image_set_id
        input["copy_image_set_information"] = copy_image_set_information
        if force is not None:
            input["force"] = force
        if promote_to_primary is not None:
            input["promote_to_primary"] = promote_to_primary

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_image_set(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
    ) -> (
        "aws_sdk_medical_imaging.types.delete_image_set_response.DeleteImageSetResponse"
    ):
        """<p>Delete an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.delete_image_set_request.DeleteImageSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.delete_image_set_response.DeleteImageSetResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.delete_image_set

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.delete_image_set.async_delete_image_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.delete_image_set_request.DeleteImageSetRequest = {}  # type: ignore[typeddict-item]
        input["datastore_id"] = datastore_id
        input["image_set_id"] = image_set_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_dicom_import_job(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        job_id: "aws_sdk_medical_imaging.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.get_dicom_import_job_response.GetDICOMImportJobResponse":
        """<p>Get the import job properties to learn more about the job or job progress.</p> <note> <p>The <code>jobStatus</code> refers to the execution of the import job. Therefore, an import job can return a <code>jobStatus</code> as <code>COMPLETED</code> even if validation issues are discovered during the import process. If a <code>jobStatus</code> returns as <code>COMPLETED</code>, we still recommend you review the output manifests written to S3, as they provide details on the success or failure of individual P10 object imports.</p> </note>

        Args:
            datastore_id: <p>The data store identifier.</p>
            job_id: <p>The import job identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.get_dicom_import_job_request.GetDICOMImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.get_dicom_import_job_response.GetDICOMImportJobResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.get_dicom_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.get_dicom_import_job.async_get_dicom_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.get_dicom_import_job_request.GetDICOMImportJobRequest = {}  # type: ignore[typeddict-item]
        input["datastore_id"] = datastore_id
        input["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    @asynccontextmanager
    async def get_image_frame(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        image_frame_information: "aws_sdk_medical_imaging.types.image_frame_information.ImageFrameInformation",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
    ) -> "AsyncGenerator[aws_sdk_medical_imaging.types.get_image_frame_response.GetImageFrameResponse]":
        """<p>Get an image frame (pixel data) for an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            image_frame_information: <p>Information about the image frame (pixel data) identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.get_image_frame_request.GetImageFrameRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.get_image_frame_response.GetImageFrameResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_frame

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_frame.async_get_image_frame(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.get_image_frame_request.GetImageFrameRequest = {}  # type: ignore[typeddict-item]
        input["datastore_id"] = datastore_id
        input["image_set_id"] = image_set_id
        input["image_frame_information"] = image_frame_information

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    async def get_image_set(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
        version_id: Optional[
            "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
        ] = None,
    ) -> "aws_sdk_medical_imaging.types.get_image_set_response.GetImageSetResponse":
        """<p>Get image set properties.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            version_id: <p>The image set version identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.get_image_set_request.GetImageSetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.get_image_set_response.GetImageSetResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_set

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_set.async_get_image_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.get_image_set_request.GetImageSetRequest = {}  # type: ignore[typeddict-item]
        input["datastore_id"] = datastore_id
        input["image_set_id"] = image_set_id
        if version_id is not None:
            input["version_id"] = version_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    @asynccontextmanager
    async def get_image_set_metadata(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
        version_id: Optional[
            "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
        ] = None,
    ) -> "AsyncGenerator[aws_sdk_medical_imaging.types.get_image_set_metadata_response.GetImageSetMetadataResponse]":
        """<p>Get metadata attributes for an image set.</p>

        Args:
            datastore_id: <p>The data store identifier.</p>
            image_set_id: <p>The image set identifier.</p>
            version_id: <p>The image set version identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.get_image_set_metadata_request.GetImageSetMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.get_image_set_metadata_response.GetImageSetMetadataResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_set_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.get_image_set_metadata.async_get_image_set_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.get_image_set_metadata_request.GetImageSetMetadataRequest = {}  # type: ignore[typeddict-item]
        input["datastore_id"] = datastore_id
        input["image_set_id"] = image_set_id
        if version_id is not None:
            input["version_id"] = version_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    async def list_dicom_import_jobs(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
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
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.list_dicom_import_jobs_request.ListDICOMImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.list_dicom_import_jobs_response.ListDICOMImportJobsResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.list_dicom_import_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.list_dicom_import_jobs.async_list_dicom_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.list_dicom_import_jobs_request.ListDICOMImportJobsRequest = {}  # type: ignore[typeddict-item]
        input["datastore_id"] = datastore_id
        if job_status is not None:
            input["job_status"] = job_status
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

    async def iter_list_dicom_import_jobs(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
        job_status: Optional[
            "aws_sdk_medical_imaging.types.job_status.JobStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[aws_sdk_medical_imaging.types.dicom_import_job_summary.DICOMImportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_dicom_import_jobs(
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

    async def list_image_set_versions(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
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
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.list_image_set_versions_request.ListImageSetVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.list_image_set_versions_response.ListImageSetVersionsResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.list_image_set_versions

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.list_image_set_versions.async_list_image_set_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.list_image_set_versions_request.ListImageSetVersionsRequest = {}  # type: ignore[typeddict-item]
        input["datastore_id"] = datastore_id
        input["image_set_id"] = image_set_id
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

    async def iter_list_image_set_versions(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[aws_sdk_medical_imaging.types.image_set_properties.ImageSetProperties]":
        _token = next_token
        while True:
            _response = await self.list_image_set_versions(
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_medical_imaging.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a medical imaging resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the medical imaging resource to list tags for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def search_image_sets(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
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
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.search_image_sets_request.SearchImageSetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.search_image_sets_response.SearchImageSetsResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.search_image_sets

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.search_image_sets.async_search_image_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.search_image_sets_request.SearchImageSetsRequest = {}  # type: ignore[typeddict-item]
        input["datastore_id"] = datastore_id
        if search_criteria is not None:
            input["search_criteria"] = search_criteria
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_search_image_sets(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
        search_criteria: Optional[
            "aws_sdk_medical_imaging.types.search_criteria.SearchCriteria"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_medical_imaging.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_medical_imaging.types.image_sets_metadata_summary.ImageSetsMetadataSummary]":
        _token = next_token
        while True:
            _response = await self.search_image_sets(
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

    async def start_dicom_import_job(
        self,
        data_access_role_arn: "aws_sdk_medical_imaging.types.role_arn.RoleArn",
        client_token: "aws_sdk_medical_imaging.types.client_token.ClientToken",
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        input_s3_uri: "aws_sdk_medical_imaging.types.s3_uri.S3Uri",
        output_s3_uri: "aws_sdk_medical_imaging.types.s3_uri.S3Uri",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
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
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.start_dicom_import_job_request.StartDICOMImportJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.start_dicom_import_job_response.StartDICOMImportJobResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.start_dicom_import_job

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.start_dicom_import_job.async_start_dicom_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.start_dicom_import_job_request.StartDICOMImportJobRequest = {}  # type: ignore[typeddict-item]
        if job_name is not None:
            input["job_name"] = job_name
        input["data_access_role_arn"] = data_access_role_arn
        input["client_token"] = client_token
        input["datastore_id"] = datastore_id
        input["input_s3_uri"] = input_s3_uri
        input["output_s3_uri"] = output_s3_uri
        if input_owner_account_id is not None:
            input["input_owner_account_id"] = input_owner_account_id
        if import_configuration is not None:
            input["import_configuration"] = import_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_medical_imaging.types.arn.Arn",
        tags: "aws_sdk_medical_imaging.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a user-specifed key and value tag to a medical imaging resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to.</p>
            tags: <p>The user-specified key and value tag pairs added to a medical imaging resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_medical_imaging.types.arn.Arn",
        tag_keys: "aws_sdk_medical_imaging.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
    ) -> "aws_sdk_medical_imaging.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a medical imaging resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from.</p>
            tag_keys: <p>The keys for the tags to be removed from the medical imaging resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_image_set_metadata(
        self,
        datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId",
        image_set_id: "aws_sdk_medical_imaging.types.image_set_id.ImageSetId",
        latest_version_id: "aws_sdk_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId",
        update_image_set_metadata_updates: "aws_sdk_medical_imaging.types.metadata_updates.MetadataUpdates",
        *,
        config_overrides: Optional[AsyncMedicalImagingClientConfig] = None,
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
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_medical_imaging.types.update_image_set_metadata_request.UpdateImageSetMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_medical_imaging.types.update_image_set_metadata_response.UpdateImageSetMetadataResponse"
        ]:
            import aws_sdk_medical_imaging._operations.ahi_gateway_service.update_image_set_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_medical_imaging._operations.ahi_gateway_service.update_image_set_metadata.async_update_image_set_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_medical_imaging.types.update_image_set_metadata_request.UpdateImageSetMetadataRequest = {}  # type: ignore[typeddict-item]
        input["datastore_id"] = datastore_id
        input["image_set_id"] = image_set_id
        input["latest_version_id"] = latest_version_id
        if force is not None:
            input["force"] = force
        if include_study_image_sets is not None:
            input["include_study_image_sets"] = include_study_image_sets
        input["update_image_set_metadata_updates"] = update_image_set_metadata_updates

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
