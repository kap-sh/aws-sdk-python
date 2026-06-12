"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ComprehendMedical_20181030``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

from aws_sdk_comprehendmedical._auth._identity import Credentials
from aws_sdk_comprehendmedical._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_comprehendmedical._auth._zapros_handler import AuthMiddleware
from aws_sdk_comprehendmedical._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.bounded_length_string
    import aws_sdk_comprehendmedical.types.client_request_token_string
    import aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter
    import aws_sdk_comprehendmedical.types.describe_entities_detection_v2_job_request
    import aws_sdk_comprehendmedical.types.describe_entities_detection_v2_job_response
    import aws_sdk_comprehendmedical.types.describe_icd10_cm_inference_job_request
    import aws_sdk_comprehendmedical.types.describe_icd10_cm_inference_job_response
    import aws_sdk_comprehendmedical.types.describe_phi_detection_job_request
    import aws_sdk_comprehendmedical.types.describe_phi_detection_job_response
    import aws_sdk_comprehendmedical.types.describe_rx_norm_inference_job_request
    import aws_sdk_comprehendmedical.types.describe_rx_norm_inference_job_response
    import aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_request
    import aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response
    import aws_sdk_comprehendmedical.types.detect_entities_request
    import aws_sdk_comprehendmedical.types.detect_entities_response
    import aws_sdk_comprehendmedical.types.detect_entities_v2_request
    import aws_sdk_comprehendmedical.types.detect_entities_v2_response
    import aws_sdk_comprehendmedical.types.detect_phi_request
    import aws_sdk_comprehendmedical.types.detect_phi_response
    import aws_sdk_comprehendmedical.types.iam_role_arn
    import aws_sdk_comprehendmedical.types.infer_icd10_cm_request
    import aws_sdk_comprehendmedical.types.infer_icd10_cm_response
    import aws_sdk_comprehendmedical.types.infer_rx_norm_request
    import aws_sdk_comprehendmedical.types.infer_rx_norm_response
    import aws_sdk_comprehendmedical.types.infer_snomedct_request
    import aws_sdk_comprehendmedical.types.infer_snomedct_response
    import aws_sdk_comprehendmedical.types.input_data_config
    import aws_sdk_comprehendmedical.types.job_id
    import aws_sdk_comprehendmedical.types.job_name
    import aws_sdk_comprehendmedical.types.kms_key
    import aws_sdk_comprehendmedical.types.language_code
    import aws_sdk_comprehendmedical.types.list_entities_detection_v2_jobs_request
    import aws_sdk_comprehendmedical.types.list_entities_detection_v2_jobs_response
    import aws_sdk_comprehendmedical.types.list_icd10_cm_inference_jobs_request
    import aws_sdk_comprehendmedical.types.list_icd10_cm_inference_jobs_response
    import aws_sdk_comprehendmedical.types.list_phi_detection_jobs_request
    import aws_sdk_comprehendmedical.types.list_phi_detection_jobs_response
    import aws_sdk_comprehendmedical.types.list_rx_norm_inference_jobs_request
    import aws_sdk_comprehendmedical.types.list_rx_norm_inference_jobs_response
    import aws_sdk_comprehendmedical.types.list_snomedct_inference_jobs_request
    import aws_sdk_comprehendmedical.types.list_snomedct_inference_jobs_response
    import aws_sdk_comprehendmedical.types.max_results_integer
    import aws_sdk_comprehendmedical.types.ontology_linking_bounded_length_string
    import aws_sdk_comprehendmedical.types.output_data_config
    import aws_sdk_comprehendmedical.types.start_entities_detection_v2_job_request
    import aws_sdk_comprehendmedical.types.start_entities_detection_v2_job_response
    import aws_sdk_comprehendmedical.types.start_icd10_cm_inference_job_request
    import aws_sdk_comprehendmedical.types.start_icd10_cm_inference_job_response
    import aws_sdk_comprehendmedical.types.start_phi_detection_job_request
    import aws_sdk_comprehendmedical.types.start_phi_detection_job_response
    import aws_sdk_comprehendmedical.types.start_rx_norm_inference_job_request
    import aws_sdk_comprehendmedical.types.start_rx_norm_inference_job_response
    import aws_sdk_comprehendmedical.types.start_snomedct_inference_job_request
    import aws_sdk_comprehendmedical.types.start_snomedct_inference_job_response
    import aws_sdk_comprehendmedical.types.stop_entities_detection_v2_job_request
    import aws_sdk_comprehendmedical.types.stop_entities_detection_v2_job_response
    import aws_sdk_comprehendmedical.types.stop_icd10_cm_inference_job_request
    import aws_sdk_comprehendmedical.types.stop_icd10_cm_inference_job_response
    import aws_sdk_comprehendmedical.types.stop_phi_detection_job_request
    import aws_sdk_comprehendmedical.types.stop_phi_detection_job_response
    import aws_sdk_comprehendmedical.types.stop_rx_norm_inference_job_request
    import aws_sdk_comprehendmedical.types.stop_rx_norm_inference_job_response
    import aws_sdk_comprehendmedical.types.stop_snomedct_inference_job_request
    import aws_sdk_comprehendmedical.types.stop_snomedct_inference_job_response
    import aws_sdk_comprehendmedical.types.string


class ComprehendMedicalClientConfig(TypedDict, total=False):
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


class ComprehendMedicalClient:
    """A client for the ``ComprehendMedical`` service.

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
        self.config = ComprehendMedicalClientConfig(
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
        self, config_overrides: Optional[ComprehendMedicalClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ComprehendMedicalClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def describe_entities_detection_v2_job(
        self,
        job_id: "aws_sdk_comprehendmedical.types.job_id.JobId",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.describe_entities_detection_v2_job_response.DescribeEntitiesDetectionV2JobResponse":
        """<p>Gets the properties associated with a medical entities detection job. Use this operation to get the status of a detection job.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend Medical generated for the job. The <code>StartEntitiesDetectionV2Job</code> operation returns this identifier in its response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.describe_entities_detection_v2_job_request.DescribeEntitiesDetectionV2JobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.describe_entities_detection_v2_job_response.DescribeEntitiesDetectionV2JobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.describe_entities_detection_v2_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.describe_entities_detection_v2_job.describe_entities_detection_v2_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.describe_entities_detection_v2_job_request.DescribeEntitiesDetectionV2JobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_icd10_cm_inference_job(
        self,
        job_id: "aws_sdk_comprehendmedical.types.job_id.JobId",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.describe_icd10_cm_inference_job_response.DescribeICD10CMInferenceJobResponse":
        """<p>Gets the properties associated with an InferICD10CM job. Use this operation to get the status of an inference job.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend Medical generated for the job. <code>The StartICD10CMInferenceJob</code> operation returns this identifier in its response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.describe_icd10_cm_inference_job_request.DescribeICD10CMInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.describe_icd10_cm_inference_job_response.DescribeICD10CMInferenceJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.describe_icd10_cm_inference_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.describe_icd10_cm_inference_job.describe_icd10_cm_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.describe_icd10_cm_inference_job_request.DescribeICD10CMInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_phi_detection_job(
        self,
        job_id: "aws_sdk_comprehendmedical.types.job_id.JobId",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.describe_phi_detection_job_response.DescribePHIDetectionJobResponse":
        """<p>Gets the properties associated with a protected health information (PHI) detection job. Use this operation to get the status of a detection job.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend Medical generated for the job. The <code>StartPHIDetectionJob</code> operation returns this identifier in its response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.describe_phi_detection_job_request.DescribePHIDetectionJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.describe_phi_detection_job_response.DescribePHIDetectionJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.describe_phi_detection_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.describe_phi_detection_job.describe_phi_detection_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.describe_phi_detection_job_request.DescribePHIDetectionJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_rx_norm_inference_job(
        self,
        job_id: "aws_sdk_comprehendmedical.types.job_id.JobId",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.describe_rx_norm_inference_job_response.DescribeRxNormInferenceJobResponse":
        """<p>Gets the properties associated with an InferRxNorm job. Use this operation to get the status of an inference job.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend Medical generated for the job. The StartRxNormInferenceJob operation returns this identifier in its response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.describe_rx_norm_inference_job_request.DescribeRxNormInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.describe_rx_norm_inference_job_response.DescribeRxNormInferenceJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.describe_rx_norm_inference_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.describe_rx_norm_inference_job.describe_rx_norm_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.describe_rx_norm_inference_job_request.DescribeRxNormInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_snomedct_inference_job(
        self,
        job_id: "aws_sdk_comprehendmedical.types.job_id.JobId",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response.DescribeSNOMEDCTInferenceJobResponse":
        """<p> Gets the properties associated with an InferSNOMEDCT job. Use this operation to get the status of an inference job. </p>

        Args:
            job_id: <p> The identifier that Amazon Comprehend Medical generated for the job. The StartSNOMEDCTInferenceJob operation returns this identifier in its response. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_request.DescribeSNOMEDCTInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_response.DescribeSNOMEDCTInferenceJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.describe_snomedct_inference_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.describe_snomedct_inference_job.describe_snomedct_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.describe_snomedct_inference_job_request.DescribeSNOMEDCTInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def detect_entities(
        self,
        text: "aws_sdk_comprehendmedical.types.bounded_length_string.BoundedLengthString",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.detect_entities_response.DetectEntitiesResponse":
        """<p>The <code>DetectEntities</code> operation is deprecated. You should use the <a>DetectEntitiesV2</a> operation instead.</p> <p>Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information.</p>

        Args:
            text: <p> A UTF-8 text string containing the clinical content being examined for entities.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.detect_entities_request.DetectEntitiesRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.detect_entities_response.DetectEntitiesResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.detect_entities

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.detect_entities.detect_entities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.detect_entities_request.DetectEntitiesRequest = {}  # type: ignore[typeddict-item]
        input["text"] = text

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def detect_entities_v2(
        self,
        text: "aws_sdk_comprehendmedical.types.bounded_length_string.BoundedLengthString",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.detect_entities_v2_response.DetectEntitiesV2Response":
        """<p>Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information. Amazon Comprehend Medical only detects medical entities in English language texts.</p> <p>The <code>DetectEntitiesV2</code> operation replaces the <a>DetectEntities</a> operation. This new action uses a different model for determining the entities in your medical text and changes the way that some entities are returned in the output. You should use the <code>DetectEntitiesV2</code> operation in all new applications.</p> <p>The <code>DetectEntitiesV2</code> operation returns the <code>Acuity</code> and <code>Direction</code> entities as attributes instead of types. </p>

        Args:
            text: <p>A UTF-8 string containing the clinical content being examined for entities.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.detect_entities_v2_request.DetectEntitiesV2Request]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.detect_entities_v2_response.DetectEntitiesV2Response"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.detect_entities_v2

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.detect_entities_v2.detect_entities_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.detect_entities_v2_request.DetectEntitiesV2Request = {}  # type: ignore[typeddict-item]
        input["text"] = text

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def detect_phi(
        self,
        text: "aws_sdk_comprehendmedical.types.bounded_length_string.BoundedLengthString",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.detect_phi_response.DetectPHIResponse":
        """<p>Inspects the clinical text for protected health information (PHI) entities and returns the entity category, location, and confidence score for each entity. Amazon Comprehend Medical only detects entities in English language texts.</p>

        Args:
            text: <p>A UTF-8 text string containing the clinical content being examined for PHI entities.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.detect_phi_request.DetectPHIRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.detect_phi_response.DetectPHIResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.detect_phi

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.detect_phi.detect_phi(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.detect_phi_request.DetectPHIRequest = {}  # type: ignore[typeddict-item]
        input["text"] = text

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def infer_icd10_cm(
        self,
        text: "aws_sdk_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.infer_icd10_cm_response.InferICD10CMResponse":
        """<p>InferICD10CM detects medical conditions as entities listed in a patient record and links those entities to normalized concept identifiers in the ICD-10-CM knowledge base from the Centers for Disease Control. Amazon Comprehend Medical only detects medical entities in English language texts. </p>

        Args:
            text: <p>The input text used for analysis.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.infer_icd10_cm_request.InferICD10CMRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.infer_icd10_cm_response.InferICD10CMResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.infer_icd10_cm

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.infer_icd10_cm.infer_icd10_cm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.infer_icd10_cm_request.InferICD10CMRequest = {}  # type: ignore[typeddict-item]
        input["text"] = text

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def infer_rx_norm(
        self,
        text: "aws_sdk_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.infer_rx_norm_response.InferRxNormResponse":
        """<p>InferRxNorm detects medications as entities listed in a patient record and links to the normalized concept identifiers in the RxNorm database from the National Library of Medicine. Amazon Comprehend Medical only detects medical entities in English language texts. </p>

        Args:
            text: <p>The input text used for analysis.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.infer_rx_norm_request.InferRxNormRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.infer_rx_norm_response.InferRxNormResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.infer_rx_norm

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.infer_rx_norm.infer_rx_norm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.infer_rx_norm_request.InferRxNormRequest = {}  # type: ignore[typeddict-item]
        input["text"] = text

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def infer_snomedct(
        self,
        text: "aws_sdk_comprehendmedical.types.ontology_linking_bounded_length_string.OntologyLinkingBoundedLengthString",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> (
        "aws_sdk_comprehendmedical.types.infer_snomedct_response.InferSNOMEDCTResponse"
    ):
        """<p> InferSNOMEDCT detects possible medical concepts as entities and links them to codes from the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED-CT) ontology</p>

        Args:
            text: <p>The input text to be analyzed using InferSNOMEDCT.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.infer_snomedct_request.InferSNOMEDCTRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.infer_snomedct_response.InferSNOMEDCTResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.infer_snomedct

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.infer_snomedct.infer_snomedct(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.infer_snomedct_request.InferSNOMEDCTRequest = {}  # type: ignore[typeddict-item]
        input["text"] = text

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_entities_detection_v2_jobs(
        self,
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
        filter: Optional[
            "aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter.ComprehendMedicalAsyncJobFilter"
        ] = None,
        next_token: Optional["aws_sdk_comprehendmedical.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_comprehendmedical.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "aws_sdk_comprehendmedical.types.list_entities_detection_v2_jobs_response.ListEntitiesDetectionV2JobsResponse":
        """<p>Gets a list of medical entity detection jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.list_entities_detection_v2_jobs_request.ListEntitiesDetectionV2JobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.list_entities_detection_v2_jobs_response.ListEntitiesDetectionV2JobsResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.list_entities_detection_v2_jobs

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.list_entities_detection_v2_jobs.list_entities_detection_v2_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.list_entities_detection_v2_jobs_request.ListEntitiesDetectionV2JobsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input["filter"] = filter
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_icd10_cm_inference_jobs(
        self,
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
        filter: Optional[
            "aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter.ComprehendMedicalAsyncJobFilter"
        ] = None,
        next_token: Optional["aws_sdk_comprehendmedical.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_comprehendmedical.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "aws_sdk_comprehendmedical.types.list_icd10_cm_inference_jobs_response.ListICD10CMInferenceJobsResponse":
        """<p>Gets a list of InferICD10CM jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.list_icd10_cm_inference_jobs_request.ListICD10CMInferenceJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.list_icd10_cm_inference_jobs_response.ListICD10CMInferenceJobsResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.list_icd10_cm_inference_jobs

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.list_icd10_cm_inference_jobs.list_icd10_cm_inference_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.list_icd10_cm_inference_jobs_request.ListICD10CMInferenceJobsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input["filter"] = filter
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_phi_detection_jobs(
        self,
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
        filter: Optional[
            "aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter.ComprehendMedicalAsyncJobFilter"
        ] = None,
        next_token: Optional["aws_sdk_comprehendmedical.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_comprehendmedical.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "aws_sdk_comprehendmedical.types.list_phi_detection_jobs_response.ListPHIDetectionJobsResponse":
        """<p>Gets a list of protected health information (PHI) detection jobs you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.list_phi_detection_jobs_request.ListPHIDetectionJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.list_phi_detection_jobs_response.ListPHIDetectionJobsResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.list_phi_detection_jobs

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.list_phi_detection_jobs.list_phi_detection_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.list_phi_detection_jobs_request.ListPHIDetectionJobsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input["filter"] = filter
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_rx_norm_inference_jobs(
        self,
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
        filter: Optional[
            "aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter.ComprehendMedicalAsyncJobFilter"
        ] = None,
        next_token: Optional["aws_sdk_comprehendmedical.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_comprehendmedical.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "aws_sdk_comprehendmedical.types.list_rx_norm_inference_jobs_response.ListRxNormInferenceJobsResponse":
        """<p>Gets a list of InferRxNorm jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>Identifies the next page of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.list_rx_norm_inference_jobs_request.ListRxNormInferenceJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.list_rx_norm_inference_jobs_response.ListRxNormInferenceJobsResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.list_rx_norm_inference_jobs

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.list_rx_norm_inference_jobs.list_rx_norm_inference_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.list_rx_norm_inference_jobs_request.ListRxNormInferenceJobsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input["filter"] = filter
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_snomedct_inference_jobs(
        self,
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
        filter: Optional[
            "aws_sdk_comprehendmedical.types.comprehend_medical_async_job_filter.ComprehendMedicalAsyncJobFilter"
        ] = None,
        next_token: Optional["aws_sdk_comprehendmedical.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_comprehendmedical.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "aws_sdk_comprehendmedical.types.list_snomedct_inference_jobs_response.ListSNOMEDCTInferenceJobsResponse":
        """<p> Gets a list of InferSNOMEDCT jobs a user has submitted. </p>

        Args:
            next_token: <p> Identifies the next page of InferSNOMEDCT results to return. </p>
            max_results: <p> The maximum number of results to return in each page. The default is 100. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.list_snomedct_inference_jobs_request.ListSNOMEDCTInferenceJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.list_snomedct_inference_jobs_response.ListSNOMEDCTInferenceJobsResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.list_snomedct_inference_jobs

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.list_snomedct_inference_jobs.list_snomedct_inference_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.list_snomedct_inference_jobs_request.ListSNOMEDCTInferenceJobsRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input["filter"] = filter
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_entities_detection_v2_job(
        self,
        input_data_config: "aws_sdk_comprehendmedical.types.input_data_config.InputDataConfig",
        output_data_config: "aws_sdk_comprehendmedical.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "aws_sdk_comprehendmedical.types.iam_role_arn.IamRoleArn",
        language_code: "aws_sdk_comprehendmedical.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
        job_name: Optional["aws_sdk_comprehendmedical.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "aws_sdk_comprehendmedical.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        kms_key: Optional["aws_sdk_comprehendmedical.types.kms_key.KMSKey"] = None,
    ) -> "aws_sdk_comprehendmedical.types.start_entities_detection_v2_job_response.StartEntitiesDetectionV2JobResponse":
        """<p>Starts an asynchronous medical entity detection job for a collection of documents. Use the <code>DescribeEntitiesDetectionV2Job</code> operation to track the status of a job.</p>

        Args:
            input_data_config: <p>The input configuration that specifies the format and location of the input data for the job.</p>
            output_data_config: <p>The output configuration that specifies where to send the output files.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions-med.html#auth-role-permissions-med\">Role-Based Permissions Required for Asynchronous Operations</a>.</p>
            job_name: <p>The identifier of the job.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend Medical generates one for you.</p>
            kms_key: <p>An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.</p>
            language_code: <p>The language of the input documents. All documents must be in the same language. Amazon Comprehend Medical processes files in US English (en).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.start_entities_detection_v2_job_request.StartEntitiesDetectionV2JobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.start_entities_detection_v2_job_response.StartEntitiesDetectionV2JobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.start_entities_detection_v2_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.start_entities_detection_v2_job.start_entities_detection_v2_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.start_entities_detection_v2_job_request.StartEntitiesDetectionV2JobRequest = {}  # type: ignore[typeddict-item]
        input["input_data_config"] = input_data_config
        input["output_data_config"] = output_data_config
        input["data_access_role_arn"] = data_access_role_arn
        if job_name is not None:
            input["job_name"] = job_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if kms_key is not None:
            input["kms_key"] = kms_key
        input["language_code"] = language_code

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_icd10_cm_inference_job(
        self,
        input_data_config: "aws_sdk_comprehendmedical.types.input_data_config.InputDataConfig",
        output_data_config: "aws_sdk_comprehendmedical.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "aws_sdk_comprehendmedical.types.iam_role_arn.IamRoleArn",
        language_code: "aws_sdk_comprehendmedical.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
        job_name: Optional["aws_sdk_comprehendmedical.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "aws_sdk_comprehendmedical.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        kms_key: Optional["aws_sdk_comprehendmedical.types.kms_key.KMSKey"] = None,
    ) -> "aws_sdk_comprehendmedical.types.start_icd10_cm_inference_job_response.StartICD10CMInferenceJobResponse":
        """<p>Starts an asynchronous job to detect medical conditions and link them to the ICD-10-CM ontology. Use the <code>DescribeICD10CMInferenceJob</code> operation to track the status of a job.</p>

        Args:
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies where to send the output files.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions-med.html#auth-role-permissions-med\"> Role-Based Permissions Required for Asynchronous Operations</a>.</p>
            job_name: <p>The identifier of the job.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend Medical generates one.</p>
            kms_key: <p>An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.</p>
            language_code: <p>The language of the input documents. All documents must be in the same language.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.start_icd10_cm_inference_job_request.StartICD10CMInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.start_icd10_cm_inference_job_response.StartICD10CMInferenceJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.start_icd10_cm_inference_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.start_icd10_cm_inference_job.start_icd10_cm_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.start_icd10_cm_inference_job_request.StartICD10CMInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input["input_data_config"] = input_data_config
        input["output_data_config"] = output_data_config
        input["data_access_role_arn"] = data_access_role_arn
        if job_name is not None:
            input["job_name"] = job_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if kms_key is not None:
            input["kms_key"] = kms_key
        input["language_code"] = language_code

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_phi_detection_job(
        self,
        input_data_config: "aws_sdk_comprehendmedical.types.input_data_config.InputDataConfig",
        output_data_config: "aws_sdk_comprehendmedical.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "aws_sdk_comprehendmedical.types.iam_role_arn.IamRoleArn",
        language_code: "aws_sdk_comprehendmedical.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
        job_name: Optional["aws_sdk_comprehendmedical.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "aws_sdk_comprehendmedical.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        kms_key: Optional["aws_sdk_comprehendmedical.types.kms_key.KMSKey"] = None,
    ) -> "aws_sdk_comprehendmedical.types.start_phi_detection_job_response.StartPHIDetectionJobResponse":
        """<p>Starts an asynchronous job to detect protected health information (PHI). Use the <code>DescribePHIDetectionJob</code> operation to track the status of a job.</p>

        Args:
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies where to send the output files.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions-med.html#auth-role-permissions-med\"> Role-Based Permissions Required for Asynchronous Operations</a>.</p>
            job_name: <p>The identifier of the job.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend Medical generates one.</p>
            kms_key: <p>An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.</p>
            language_code: <p>The language of the input documents. All documents must be in the same language.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.start_phi_detection_job_request.StartPHIDetectionJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.start_phi_detection_job_response.StartPHIDetectionJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.start_phi_detection_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.start_phi_detection_job.start_phi_detection_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.start_phi_detection_job_request.StartPHIDetectionJobRequest = {}  # type: ignore[typeddict-item]
        input["input_data_config"] = input_data_config
        input["output_data_config"] = output_data_config
        input["data_access_role_arn"] = data_access_role_arn
        if job_name is not None:
            input["job_name"] = job_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if kms_key is not None:
            input["kms_key"] = kms_key
        input["language_code"] = language_code

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_rx_norm_inference_job(
        self,
        input_data_config: "aws_sdk_comprehendmedical.types.input_data_config.InputDataConfig",
        output_data_config: "aws_sdk_comprehendmedical.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "aws_sdk_comprehendmedical.types.iam_role_arn.IamRoleArn",
        language_code: "aws_sdk_comprehendmedical.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
        job_name: Optional["aws_sdk_comprehendmedical.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "aws_sdk_comprehendmedical.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        kms_key: Optional["aws_sdk_comprehendmedical.types.kms_key.KMSKey"] = None,
    ) -> "aws_sdk_comprehendmedical.types.start_rx_norm_inference_job_response.StartRxNormInferenceJobResponse":
        """<p>Starts an asynchronous job to detect medication entities and link them to the RxNorm ontology. Use the <code>DescribeRxNormInferenceJob</code> operation to track the status of a job.</p>

        Args:
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies where to send the output files.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/access-control-managing-permissions-med.html#auth-role-permissions-med\"> Role-Based Permissions Required for Asynchronous Operations</a>.</p>
            job_name: <p>The identifier of the job.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend Medical generates one.</p>
            kms_key: <p>An AWS Key Management Service key to encrypt your output files. If you do not specify a key, the files are written in plain text.</p>
            language_code: <p>The language of the input documents. All documents must be in the same language.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.start_rx_norm_inference_job_request.StartRxNormInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.start_rx_norm_inference_job_response.StartRxNormInferenceJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.start_rx_norm_inference_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.start_rx_norm_inference_job.start_rx_norm_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.start_rx_norm_inference_job_request.StartRxNormInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input["input_data_config"] = input_data_config
        input["output_data_config"] = output_data_config
        input["data_access_role_arn"] = data_access_role_arn
        if job_name is not None:
            input["job_name"] = job_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if kms_key is not None:
            input["kms_key"] = kms_key
        input["language_code"] = language_code

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_snomedct_inference_job(
        self,
        input_data_config: "aws_sdk_comprehendmedical.types.input_data_config.InputDataConfig",
        output_data_config: "aws_sdk_comprehendmedical.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "aws_sdk_comprehendmedical.types.iam_role_arn.IamRoleArn",
        language_code: "aws_sdk_comprehendmedical.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
        job_name: Optional["aws_sdk_comprehendmedical.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "aws_sdk_comprehendmedical.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        kms_key: Optional["aws_sdk_comprehendmedical.types.kms_key.KMSKey"] = None,
    ) -> "aws_sdk_comprehendmedical.types.start_snomedct_inference_job_response.StartSNOMEDCTInferenceJobResponse":
        """<p> Starts an asynchronous job to detect medical concepts and link them to the SNOMED-CT ontology. Use the DescribeSNOMEDCTInferenceJob operation to track the status of a job. </p>

        Args:
            data_access_role_arn: <p> The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend Medical read access to your input data. </p>
            job_name: <p> The user generated name the asynchronous InferSNOMEDCT job. </p>
            client_request_token: <p> A unique identifier for the request. If you don't set the client request token, Amazon Comprehend Medical generates one. </p>
            kms_key: <p> An AWS Key Management Service key used to encrypt your output files. If you do not specify a key, the files are written in plain text. </p>
            language_code: <p> The language of the input documents. All documents must be in the same language. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.start_snomedct_inference_job_request.StartSNOMEDCTInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.start_snomedct_inference_job_response.StartSNOMEDCTInferenceJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.start_snomedct_inference_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.start_snomedct_inference_job.start_snomedct_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.start_snomedct_inference_job_request.StartSNOMEDCTInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input["input_data_config"] = input_data_config
        input["output_data_config"] = output_data_config
        input["data_access_role_arn"] = data_access_role_arn
        if job_name is not None:
            input["job_name"] = job_name
        if client_request_token is not None:
            input["client_request_token"] = client_request_token
        if kms_key is not None:
            input["kms_key"] = kms_key
        input["language_code"] = language_code

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_entities_detection_v2_job(
        self,
        job_id: "aws_sdk_comprehendmedical.types.job_id.JobId",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.stop_entities_detection_v2_job_response.StopEntitiesDetectionV2JobResponse":
        """<p>Stops a medical entities detection job in progress.</p>

        Args:
            job_id: <p>The identifier of the medical entities job to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.stop_entities_detection_v2_job_request.StopEntitiesDetectionV2JobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.stop_entities_detection_v2_job_response.StopEntitiesDetectionV2JobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.stop_entities_detection_v2_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.stop_entities_detection_v2_job.stop_entities_detection_v2_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.stop_entities_detection_v2_job_request.StopEntitiesDetectionV2JobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_icd10_cm_inference_job(
        self,
        job_id: "aws_sdk_comprehendmedical.types.job_id.JobId",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.stop_icd10_cm_inference_job_response.StopICD10CMInferenceJobResponse":
        """<p>Stops an InferICD10CM inference job in progress.</p>

        Args:
            job_id: <p>The identifier of the job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.stop_icd10_cm_inference_job_request.StopICD10CMInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.stop_icd10_cm_inference_job_response.StopICD10CMInferenceJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.stop_icd10_cm_inference_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.stop_icd10_cm_inference_job.stop_icd10_cm_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.stop_icd10_cm_inference_job_request.StopICD10CMInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_phi_detection_job(
        self,
        job_id: "aws_sdk_comprehendmedical.types.job_id.JobId",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.stop_phi_detection_job_response.StopPHIDetectionJobResponse":
        """<p>Stops a protected health information (PHI) detection job in progress.</p>

        Args:
            job_id: <p>The identifier of the PHI detection job to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.stop_phi_detection_job_request.StopPHIDetectionJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.stop_phi_detection_job_response.StopPHIDetectionJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.stop_phi_detection_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.stop_phi_detection_job.stop_phi_detection_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.stop_phi_detection_job_request.StopPHIDetectionJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_rx_norm_inference_job(
        self,
        job_id: "aws_sdk_comprehendmedical.types.job_id.JobId",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.stop_rx_norm_inference_job_response.StopRxNormInferenceJobResponse":
        """<p>Stops an InferRxNorm inference job in progress.</p>

        Args:
            job_id: <p>The identifier of the job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.stop_rx_norm_inference_job_request.StopRxNormInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.stop_rx_norm_inference_job_response.StopRxNormInferenceJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.stop_rx_norm_inference_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.stop_rx_norm_inference_job.stop_rx_norm_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.stop_rx_norm_inference_job_request.StopRxNormInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_snomedct_inference_job(
        self,
        job_id: "aws_sdk_comprehendmedical.types.job_id.JobId",
        *,
        config_overrides: Optional[ComprehendMedicalClientConfig] = None,
    ) -> "aws_sdk_comprehendmedical.types.stop_snomedct_inference_job_response.StopSNOMEDCTInferenceJobResponse":
        """<p> Stops an InferSNOMEDCT inference job in progress. </p>

        Args:
            job_id: <p> The job id of the asynchronous InferSNOMEDCT job to be stopped. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_comprehendmedical.types.stop_snomedct_inference_job_request.StopSNOMEDCTInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_comprehendmedical.types.stop_snomedct_inference_job_response.StopSNOMEDCTInferenceJobResponse"
        ]:
            import aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.stop_snomedct_inference_job

            output, http_response = (
                aws_sdk_comprehendmedical._operations.comprehend_medical_20181030.stop_snomedct_inference_job.stop_snomedct_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_comprehendmedical.types.stop_snomedct_inference_job_request.StopSNOMEDCTInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
