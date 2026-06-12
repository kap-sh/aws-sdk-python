from typing import TYPE_CHECKING, Optional

import aws_sdk_artifact._auth._signers
import aws_sdk_artifact._auth._sigv4
from aws_sdk_artifact._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_artifact.types.get_report_metadata_request
    import aws_sdk_artifact.types.get_report_metadata_response
    import aws_sdk_artifact.types.get_report_request
    import aws_sdk_artifact.types.get_report_response
    import aws_sdk_artifact.types.get_term_for_report_request
    import aws_sdk_artifact.types.get_term_for_report_response
    import aws_sdk_artifact.types.list_report_versions_request
    import aws_sdk_artifact.types.list_report_versions_response
    import aws_sdk_artifact.types.list_reports_request
    import aws_sdk_artifact.types.list_reports_response
    import aws_sdk_artifact.types.max_results_attribute
    import aws_sdk_artifact.types.next_token_attribute
    import aws_sdk_artifact.types.report_id
    import aws_sdk_artifact.types.report_summary
    import aws_sdk_artifact.types.short_string_attribute
    import aws_sdk_artifact.types.version_attribute
    from aws_sdk_artifact._services.artifact import ArtifactClient, ArtifactClientConfig
    from aws_sdk_artifact._services.async_artifact import (
        AsyncArtifactClient,
        AsyncArtifactClientConfig,
    )


class ReportResource:
    def __init__(self, service: ArtifactClient) -> None:
        self._service = service

    def read(
        self,
        report_id: "aws_sdk_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        report_version: Optional[
            "aws_sdk_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> (
        "aws_sdk_artifact.types.get_report_metadata_response.GetReportMetadataResponse"
    ):
        """<p>Get the metadata for a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>

        Examples:
            Invoke GetReportMetadata operation on the latest version of a specific report
            The GetReportMetadata operation is invoked on a reportId and on a optional version.
                        If callers do not provide a version, it will default to the report's latest version.

            >>> client.read(report_id='report-bqhUJF3FrQZsMJpb')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_artifact.types.get_report_metadata_request.GetReportMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_artifact.types.get_report_metadata_response.GetReportMetadataResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.get_report_metadata

            output, http_response = (
                aws_sdk_artifact._operations.artifact.get_report_metadata.get_report_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.get_report_metadata_request.GetReportMetadataRequest = {}  # type: ignore[typeddict-item]
        input["report_id"] = report_id
        if report_version is not None:
            input["report_version"] = report_version

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "aws_sdk_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "aws_sdk_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "aws_sdk_artifact.types.list_reports_response.ListReportsResponse":
        """<p>List available reports.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Examples:
            Invoke ListReports operation
            The ListReports operation returns a collection of report resources.

            >>> client.list()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_artifact.types.list_reports_request.ListReportsRequest]",
        ) -> OperationResponse[
            "aws_sdk_artifact.types.list_reports_response.ListReportsResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.list_reports

            output, http_response = (
                aws_sdk_artifact._operations.artifact.list_reports.list_reports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.list_reports_request.ListReportsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_report(
        self,
        report_id: "aws_sdk_artifact.types.report_id.ReportId",
        term_token: "aws_sdk_artifact.types.short_string_attribute.ShortStringAttribute",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        report_version: Optional[
            "aws_sdk_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "aws_sdk_artifact.types.get_report_response.GetReportResponse":
        """<p>Get the content for a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>
            term_token: <p>Unique download token provided by GetTermForReport API.</p>

        Examples:
            Invoke GetReport operation on the latest version of a specific report
            The GetReport operation is invoked on a reportId and on a optional version.
                        Callers must provide a termToken, which is provided by the GetTermForReport
                        operation. If callers do not provide a version, it will default to the
                        report's latest version

            >>> client.get_report(report_id='report-abcdef0123456789', term_token='term-token-abcdefghijklm01234567890')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_artifact.types.get_report_request.GetReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_artifact.types.get_report_response.GetReportResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.get_report

            output, http_response = (
                aws_sdk_artifact._operations.artifact.get_report.get_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.get_report_request.GetReportRequest = {}  # type: ignore[typeddict-item]
        input["report_id"] = report_id
        if report_version is not None:
            input["report_version"] = report_version
        input["term_token"] = term_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_term_for_report(
        self,
        report_id: "aws_sdk_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        report_version: Optional[
            "aws_sdk_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "aws_sdk_artifact.types.get_term_for_report_response.GetTermForReportResponse":
        """<p>Get the Term content associated with a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>

        Examples:
            Invoke GetTermForReport operation on the latest version of a specific report
            The GetTermForReport operation is invoked on a reportId and on a optional version.
                        If callers do not provide a version, it will default to the report's latest version.

            >>> client.get_term_for_report(report_id='report-abcdef0123456789')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_artifact.types.get_term_for_report_request.GetTermForReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_artifact.types.get_term_for_report_response.GetTermForReportResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.get_term_for_report

            output, http_response = (
                aws_sdk_artifact._operations.artifact.get_term_for_report.get_term_for_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.get_term_for_report_request.GetTermForReportRequest = {}  # type: ignore[typeddict-item]
        input["report_id"] = report_id
        if report_version is not None:
            input["report_version"] = report_version

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_report_versions(
        self,
        report_id: "aws_sdk_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "aws_sdk_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "aws_sdk_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "aws_sdk_artifact.types.list_report_versions_response.ListReportVersionsResponse":
        """<p>List available report versions for a given report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Examples:
            Invoke ListReportVersions operation
            The ListReportVersions operation returns a collection of report versions
                        for a given resource.

            >>> client.list_report_versions(report_id='report-abcdef0123456789')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_artifact.types.list_report_versions_request.ListReportVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_artifact.types.list_report_versions_response.ListReportVersionsResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.list_report_versions

            output, http_response = (
                aws_sdk_artifact._operations.artifact.list_report_versions.list_report_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.list_report_versions_request.ListReportVersionsRequest = {}  # type: ignore[typeddict-item]
        input["report_id"] = report_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncReportResource:
    def __init__(self, service: AsyncArtifactClient) -> None:
        self._service = service

    async def read(
        self,
        report_id: "aws_sdk_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        report_version: Optional[
            "aws_sdk_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> (
        "aws_sdk_artifact.types.get_report_metadata_response.GetReportMetadataResponse"
    ):
        """<p>Get the metadata for a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>

        Examples:
            Invoke GetReportMetadata operation on the latest version of a specific report
            The GetReportMetadata operation is invoked on a reportId and on a optional version.
                        If callers do not provide a version, it will default to the report's latest version.

            >>> await client.read(report_id='report-bqhUJF3FrQZsMJpb')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_artifact.types.get_report_metadata_request.GetReportMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_artifact.types.get_report_metadata_response.GetReportMetadataResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.get_report_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_artifact._operations.artifact.get_report_metadata.async_get_report_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.get_report_metadata_request.GetReportMetadataRequest = {}  # type: ignore[typeddict-item]
        input["report_id"] = report_id
        if report_version is not None:
            input["report_version"] = report_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        max_results: Optional[
            "aws_sdk_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "aws_sdk_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "aws_sdk_artifact.types.list_reports_response.ListReportsResponse":
        """<p>List available reports.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Examples:
            Invoke ListReports operation
            The ListReports operation returns a collection of report resources.

            >>> await client.list()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_artifact.types.list_reports_request.ListReportsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_artifact.types.list_reports_response.ListReportsResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.list_reports

            (
                output,
                http_response,
            ) = await aws_sdk_artifact._operations.artifact.list_reports.async_list_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.list_reports_request.ListReportsRequest = {}  # type: ignore[typeddict-item]
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

    async def get_report(
        self,
        report_id: "aws_sdk_artifact.types.report_id.ReportId",
        term_token: "aws_sdk_artifact.types.short_string_attribute.ShortStringAttribute",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        report_version: Optional[
            "aws_sdk_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "aws_sdk_artifact.types.get_report_response.GetReportResponse":
        """<p>Get the content for a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>
            term_token: <p>Unique download token provided by GetTermForReport API.</p>

        Examples:
            Invoke GetReport operation on the latest version of a specific report
            The GetReport operation is invoked on a reportId and on a optional version.
                        Callers must provide a termToken, which is provided by the GetTermForReport
                        operation. If callers do not provide a version, it will default to the
                        report's latest version

            >>> await client.get_report(report_id='report-abcdef0123456789', term_token='term-token-abcdefghijklm01234567890')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_artifact.types.get_report_request.GetReportRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_artifact.types.get_report_response.GetReportResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.get_report

            (
                output,
                http_response,
            ) = await aws_sdk_artifact._operations.artifact.get_report.async_get_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.get_report_request.GetReportRequest = {}  # type: ignore[typeddict-item]
        input["report_id"] = report_id
        if report_version is not None:
            input["report_version"] = report_version
        input["term_token"] = term_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_term_for_report(
        self,
        report_id: "aws_sdk_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        report_version: Optional[
            "aws_sdk_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "aws_sdk_artifact.types.get_term_for_report_response.GetTermForReportResponse":
        """<p>Get the Term content associated with a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>

        Examples:
            Invoke GetTermForReport operation on the latest version of a specific report
            The GetTermForReport operation is invoked on a reportId and on a optional version.
                        If callers do not provide a version, it will default to the report's latest version.

            >>> await client.get_term_for_report(report_id='report-abcdef0123456789')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_artifact.types.get_term_for_report_request.GetTermForReportRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_artifact.types.get_term_for_report_response.GetTermForReportResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.get_term_for_report

            (
                output,
                http_response,
            ) = await aws_sdk_artifact._operations.artifact.get_term_for_report.async_get_term_for_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.get_term_for_report_request.GetTermForReportRequest = {}  # type: ignore[typeddict-item]
        input["report_id"] = report_id
        if report_version is not None:
            input["report_version"] = report_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_report_versions(
        self,
        report_id: "aws_sdk_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        max_results: Optional[
            "aws_sdk_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "aws_sdk_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "aws_sdk_artifact.types.list_report_versions_response.ListReportVersionsResponse":
        """<p>List available report versions for a given report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Examples:
            Invoke ListReportVersions operation
            The ListReportVersions operation returns a collection of report versions
                        for a given resource.

            >>> await client.list_report_versions(report_id='report-abcdef0123456789')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_artifact.types.list_report_versions_request.ListReportVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_artifact.types.list_report_versions_response.ListReportVersionsResponse"
        ]:
            import aws_sdk_artifact._operations.artifact.list_report_versions

            (
                output,
                http_response,
            ) = await aws_sdk_artifact._operations.artifact.list_report_versions.async_list_report_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_artifact.types.list_report_versions_request.ListReportVersionsRequest = {}  # type: ignore[typeddict-item]
        input["report_id"] = report_id
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
