"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#AWSApplicationCostProfiler``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_applicationcostprofiler._auth._signers
import aws_sdk_applicationcostprofiler._auth._sigv4
from aws_sdk_applicationcostprofiler._auth._identity import Credentials
from aws_sdk_applicationcostprofiler._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_applicationcostprofiler._auth._zapros_handler import AuthMiddleware
from aws_sdk_applicationcostprofiler._pagination import resolve_path as _resolve_path
from aws_sdk_applicationcostprofiler._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.delete_report_definition_request
    import aws_sdk_applicationcostprofiler.types.delete_report_definition_result
    import aws_sdk_applicationcostprofiler.types.format
    import aws_sdk_applicationcostprofiler.types.get_report_definition_request
    import aws_sdk_applicationcostprofiler.types.get_report_definition_result
    import aws_sdk_applicationcostprofiler.types.import_application_usage_request
    import aws_sdk_applicationcostprofiler.types.import_application_usage_result
    import aws_sdk_applicationcostprofiler.types.integer
    import aws_sdk_applicationcostprofiler.types.list_report_definitions_request
    import aws_sdk_applicationcostprofiler.types.list_report_definitions_result
    import aws_sdk_applicationcostprofiler.types.put_report_definition_request
    import aws_sdk_applicationcostprofiler.types.put_report_definition_result
    import aws_sdk_applicationcostprofiler.types.report_definition
    import aws_sdk_applicationcostprofiler.types.report_description
    import aws_sdk_applicationcostprofiler.types.report_frequency
    import aws_sdk_applicationcostprofiler.types.report_id
    import aws_sdk_applicationcostprofiler.types.s3_location
    import aws_sdk_applicationcostprofiler.types.source_s3_location
    import aws_sdk_applicationcostprofiler.types.token
    import aws_sdk_applicationcostprofiler.types.update_report_definition_request
    import aws_sdk_applicationcostprofiler.types.update_report_definition_result


class ApplicationCostProfilerClientConfig(TypedDict, total=False):
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


class ApplicationCostProfilerClient:
    """A client for the ``ApplicationCostProfiler`` service.

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
        self._config = ApplicationCostProfilerClientConfig(
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
        self, config_overrides: Optional[ApplicationCostProfilerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ApplicationCostProfilerClientConfig = config_overrides or {}
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

    def delete_report_definition(
        self,
        report_id: "aws_sdk_applicationcostprofiler.types.report_id.ReportId",
        *,
        config_overrides: Optional[ApplicationCostProfilerClientConfig] = None,
    ) -> "aws_sdk_applicationcostprofiler.types.delete_report_definition_result.DeleteReportDefinitionResult":
        """<p>Deletes the specified report definition in AWS Application Cost Profiler. This stops the report from being generated.</p>

        Args:
            report_id: <p>Required. ID of the report to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_applicationcostprofiler.types.delete_report_definition_request.DeleteReportDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_applicationcostprofiler.types.delete_report_definition_result.DeleteReportDefinitionResult"
        ]:
            import aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.delete_report_definition

            output, http_response = (
                aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.delete_report_definition.delete_report_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_applicationcostprofiler.types.delete_report_definition_request.DeleteReportDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["report_id"] = report_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_report_definition(
        self,
        report_id: "aws_sdk_applicationcostprofiler.types.report_id.ReportId",
        *,
        config_overrides: Optional[ApplicationCostProfilerClientConfig] = None,
    ) -> "aws_sdk_applicationcostprofiler.types.get_report_definition_result.GetReportDefinitionResult":
        """<p>Retrieves the definition of a report already configured in AWS Application Cost Profiler.</p>

        Args:
            report_id: <p>ID of the report to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_applicationcostprofiler.types.get_report_definition_request.GetReportDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_applicationcostprofiler.types.get_report_definition_result.GetReportDefinitionResult"
        ]:
            import aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.get_report_definition

            output, http_response = (
                aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.get_report_definition.get_report_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_applicationcostprofiler.types.get_report_definition_request.GetReportDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["report_id"] = report_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_application_usage(
        self,
        source_s3_location: "aws_sdk_applicationcostprofiler.types.source_s3_location.SourceS3Location",
        *,
        config_overrides: Optional[ApplicationCostProfilerClientConfig] = None,
    ) -> "aws_sdk_applicationcostprofiler.types.import_application_usage_result.ImportApplicationUsageResult":
        """<p>Ingests application usage data from Amazon Simple Storage Service (Amazon S3).</p> <p>The data must already exist in the S3 location. As part of the action, AWS Application Cost Profiler copies the object from your S3 bucket to an S3 bucket owned by Amazon for processing asynchronously.</p>

        Args:
            source_s3_location: <p>Amazon S3 location to import application usage data from.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_applicationcostprofiler.types.import_application_usage_request.ImportApplicationUsageRequest]",
        ) -> OperationResponse[
            "aws_sdk_applicationcostprofiler.types.import_application_usage_result.ImportApplicationUsageResult"
        ]:
            import aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.import_application_usage

            output, http_response = (
                aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.import_application_usage.import_application_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_applicationcostprofiler.types.import_application_usage_request.ImportApplicationUsageRequest = {}  # type: ignore[typeddict-item]
        input_["source_s3_location"] = source_s3_location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_report_definitions(
        self,
        *,
        config_overrides: Optional[ApplicationCostProfilerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_applicationcostprofiler.types.token.Token"
        ] = None,
        max_results: Optional[
            "aws_sdk_applicationcostprofiler.types.integer.Integer"
        ] = None,
    ) -> "aws_sdk_applicationcostprofiler.types.list_report_definitions_result.ListReportDefinitionsResult":
        """<p>Retrieves a list of all reports and their configurations for your AWS account.</p> <p>The maximum number of reports is one.</p>

        Args:
            next_token: <p>The token value from a previous call to access the next page of results.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_applicationcostprofiler.types.list_report_definitions_request.ListReportDefinitionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_applicationcostprofiler.types.list_report_definitions_result.ListReportDefinitionsResult"
        ]:
            import aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.list_report_definitions

            output, http_response = (
                aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.list_report_definitions.list_report_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_applicationcostprofiler.types.list_report_definitions_request.ListReportDefinitionsRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_report_definitions(
        self,
        *,
        config_overrides: Optional[ApplicationCostProfilerClientConfig] = None,
        next_token: Optional[
            "aws_sdk_applicationcostprofiler.types.token.Token"
        ] = None,
        max_results: Optional[
            "aws_sdk_applicationcostprofiler.types.integer.Integer"
        ] = None,
    ) -> "Iterator[aws_sdk_applicationcostprofiler.types.report_definition.ReportDefinition]":
        _token = next_token
        while True:
            _response = self.list_report_definitions(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("report_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_report_definition(
        self,
        report_id: "aws_sdk_applicationcostprofiler.types.report_id.ReportId",
        report_description: "aws_sdk_applicationcostprofiler.types.report_description.ReportDescription",
        report_frequency: "aws_sdk_applicationcostprofiler.types.report_frequency.ReportFrequency",
        format: "aws_sdk_applicationcostprofiler.types.format.Format",
        destination_s3_location: "aws_sdk_applicationcostprofiler.types.s3_location.S3Location",
        *,
        config_overrides: Optional[ApplicationCostProfilerClientConfig] = None,
    ) -> "aws_sdk_applicationcostprofiler.types.put_report_definition_result.PutReportDefinitionResult":
        """<p>Creates the report definition for a report in Application Cost Profiler.</p>

        Args:
            report_id: <p>Required. ID of the report. You can choose any valid string matching the pattern for the ID.</p>
            report_description: <p>Required. Description of the report.</p>
            report_frequency: <p>Required. The cadence to generate the report.</p>
            format: <p>Required. The format to use for the generated report.</p>
            destination_s3_location: <p>Required. Amazon Simple Storage Service (Amazon S3) location where Application Cost Profiler uploads the report.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_applicationcostprofiler.types.put_report_definition_request.PutReportDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_applicationcostprofiler.types.put_report_definition_result.PutReportDefinitionResult"
        ]:
            import aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.put_report_definition

            output, http_response = (
                aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.put_report_definition.put_report_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_applicationcostprofiler.types.put_report_definition_request.PutReportDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["report_id"] = report_id
        input_["report_description"] = report_description
        input_["report_frequency"] = report_frequency
        input_["format"] = format
        input_["destination_s3_location"] = destination_s3_location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_report_definition(
        self,
        report_id: "aws_sdk_applicationcostprofiler.types.report_id.ReportId",
        report_description: "aws_sdk_applicationcostprofiler.types.report_description.ReportDescription",
        report_frequency: "aws_sdk_applicationcostprofiler.types.report_frequency.ReportFrequency",
        format: "aws_sdk_applicationcostprofiler.types.format.Format",
        destination_s3_location: "aws_sdk_applicationcostprofiler.types.s3_location.S3Location",
        *,
        config_overrides: Optional[ApplicationCostProfilerClientConfig] = None,
    ) -> "aws_sdk_applicationcostprofiler.types.update_report_definition_result.UpdateReportDefinitionResult":
        """<p>Updates existing report in AWS Application Cost Profiler.</p>

        Args:
            report_id: <p>Required. ID of the report to update.</p>
            report_description: <p>Required. Description of the report.</p>
            report_frequency: <p>Required. The cadence to generate the report.</p>
            format: <p>Required. The format to use for the generated report.</p>
            destination_s3_location: <p>Required. Amazon Simple Storage Service (Amazon S3) location where Application Cost Profiler uploads the report.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_applicationcostprofiler.types.update_report_definition_request.UpdateReportDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_applicationcostprofiler.types.update_report_definition_result.UpdateReportDefinitionResult"
        ]:
            import aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.update_report_definition

            output, http_response = (
                aws_sdk_applicationcostprofiler._operations.aws_application_cost_profiler.update_report_definition.update_report_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_applicationcostprofiler.types.update_report_definition_request.UpdateReportDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["report_id"] = report_id
        input_["report_description"] = report_description
        input_["report_frequency"] = report_frequency
        input_["format"] = format
        input_["destination_s3_location"] = destination_s3_location

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
