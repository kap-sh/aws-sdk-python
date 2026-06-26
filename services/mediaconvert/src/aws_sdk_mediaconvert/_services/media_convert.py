"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MediaConvert``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_mediaconvert._auth._signers
import aws_sdk_mediaconvert._auth._sigv4
from aws_sdk_mediaconvert._auth._identity import Credentials
from aws_sdk_mediaconvert._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_mediaconvert._auth._zapros_handler import AuthMiddleware
from aws_sdk_mediaconvert._pagination import resolve_path as _resolve_path
from aws_sdk_mediaconvert._services._aws_config import aws_config
from aws_sdk_mediaconvert._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.__integer_min0
    import aws_sdk_mediaconvert.types.__integer_min1_max20
    import aws_sdk_mediaconvert.types.__integer_min_negative50_max50
    import aws_sdk_mediaconvert.types.__list_of__string
    import aws_sdk_mediaconvert.types.__list_of_hop_destination
    import aws_sdk_mediaconvert.types.__list_of_jobs_query_filter
    import aws_sdk_mediaconvert.types.__list_of_probe_input_file
    import aws_sdk_mediaconvert.types.__map_of__string
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.acceleration_settings
    import aws_sdk_mediaconvert.types.associate_certificate_request
    import aws_sdk_mediaconvert.types.associate_certificate_response
    import aws_sdk_mediaconvert.types.billing_tags_source
    import aws_sdk_mediaconvert.types.cancel_job_request
    import aws_sdk_mediaconvert.types.cancel_job_response
    import aws_sdk_mediaconvert.types.create_job_request
    import aws_sdk_mediaconvert.types.create_job_response
    import aws_sdk_mediaconvert.types.create_job_template_request
    import aws_sdk_mediaconvert.types.create_job_template_response
    import aws_sdk_mediaconvert.types.create_preset_request
    import aws_sdk_mediaconvert.types.create_preset_response
    import aws_sdk_mediaconvert.types.create_queue_request
    import aws_sdk_mediaconvert.types.create_queue_response
    import aws_sdk_mediaconvert.types.create_resource_share_request
    import aws_sdk_mediaconvert.types.create_resource_share_response
    import aws_sdk_mediaconvert.types.delete_job_template_request
    import aws_sdk_mediaconvert.types.delete_job_template_response
    import aws_sdk_mediaconvert.types.delete_policy_request
    import aws_sdk_mediaconvert.types.delete_policy_response
    import aws_sdk_mediaconvert.types.delete_preset_request
    import aws_sdk_mediaconvert.types.delete_preset_response
    import aws_sdk_mediaconvert.types.delete_queue_request
    import aws_sdk_mediaconvert.types.delete_queue_response
    import aws_sdk_mediaconvert.types.describe_endpoints_mode
    import aws_sdk_mediaconvert.types.describe_endpoints_request
    import aws_sdk_mediaconvert.types.describe_endpoints_response
    import aws_sdk_mediaconvert.types.disassociate_certificate_request
    import aws_sdk_mediaconvert.types.disassociate_certificate_response
    import aws_sdk_mediaconvert.types.endpoint
    import aws_sdk_mediaconvert.types.get_job_request
    import aws_sdk_mediaconvert.types.get_job_response
    import aws_sdk_mediaconvert.types.get_job_template_request
    import aws_sdk_mediaconvert.types.get_job_template_response
    import aws_sdk_mediaconvert.types.get_jobs_query_results_request
    import aws_sdk_mediaconvert.types.get_jobs_query_results_response
    import aws_sdk_mediaconvert.types.get_policy_request
    import aws_sdk_mediaconvert.types.get_policy_response
    import aws_sdk_mediaconvert.types.get_preset_request
    import aws_sdk_mediaconvert.types.get_preset_response
    import aws_sdk_mediaconvert.types.get_queue_request
    import aws_sdk_mediaconvert.types.get_queue_response
    import aws_sdk_mediaconvert.types.job
    import aws_sdk_mediaconvert.types.job_engine_version
    import aws_sdk_mediaconvert.types.job_settings
    import aws_sdk_mediaconvert.types.job_status
    import aws_sdk_mediaconvert.types.job_template
    import aws_sdk_mediaconvert.types.job_template_list_by
    import aws_sdk_mediaconvert.types.job_template_settings
    import aws_sdk_mediaconvert.types.list_job_templates_request
    import aws_sdk_mediaconvert.types.list_job_templates_response
    import aws_sdk_mediaconvert.types.list_jobs_request
    import aws_sdk_mediaconvert.types.list_jobs_response
    import aws_sdk_mediaconvert.types.list_presets_request
    import aws_sdk_mediaconvert.types.list_presets_response
    import aws_sdk_mediaconvert.types.list_queues_request
    import aws_sdk_mediaconvert.types.list_queues_response
    import aws_sdk_mediaconvert.types.list_tags_for_resource_request
    import aws_sdk_mediaconvert.types.list_tags_for_resource_response
    import aws_sdk_mediaconvert.types.list_versions_request
    import aws_sdk_mediaconvert.types.list_versions_response
    import aws_sdk_mediaconvert.types.order
    import aws_sdk_mediaconvert.types.policy
    import aws_sdk_mediaconvert.types.preset
    import aws_sdk_mediaconvert.types.preset_list_by
    import aws_sdk_mediaconvert.types.preset_settings
    import aws_sdk_mediaconvert.types.pricing_plan
    import aws_sdk_mediaconvert.types.probe_request
    import aws_sdk_mediaconvert.types.probe_response
    import aws_sdk_mediaconvert.types.put_policy_request
    import aws_sdk_mediaconvert.types.put_policy_response
    import aws_sdk_mediaconvert.types.queue
    import aws_sdk_mediaconvert.types.queue_list_by
    import aws_sdk_mediaconvert.types.queue_status
    import aws_sdk_mediaconvert.types.reservation_plan_settings
    import aws_sdk_mediaconvert.types.search_jobs_request
    import aws_sdk_mediaconvert.types.search_jobs_response
    import aws_sdk_mediaconvert.types.simulate_reserved_queue
    import aws_sdk_mediaconvert.types.start_jobs_query_request
    import aws_sdk_mediaconvert.types.start_jobs_query_response
    import aws_sdk_mediaconvert.types.status_update_interval
    import aws_sdk_mediaconvert.types.tag_resource_request
    import aws_sdk_mediaconvert.types.tag_resource_response
    import aws_sdk_mediaconvert.types.untag_resource_request
    import aws_sdk_mediaconvert.types.untag_resource_response
    import aws_sdk_mediaconvert.types.update_job_template_request
    import aws_sdk_mediaconvert.types.update_job_template_response
    import aws_sdk_mediaconvert.types.update_preset_request
    import aws_sdk_mediaconvert.types.update_preset_response
    import aws_sdk_mediaconvert.types.update_queue_request
    import aws_sdk_mediaconvert.types.update_queue_response


class MediaConvertClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class MediaConvertClient:
    """A client for the ``MediaConvert`` service.

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
        self._config = MediaConvertClientConfig(
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
        self, config_overrides: Optional[MediaConvertClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MediaConvertClientConfig = config_overrides or {}
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

    def associate_certificate(
        self,
        arn: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.associate_certificate_response.AssociateCertificateResponse":
        """Associates an AWS Certificate Manager (ACM) Amazon Resource Name (ARN) with AWS Elemental MediaConvert.

        Args:
            arn: The ARN of the ACM certificate that you want to associate with your MediaConvert resource.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.associate_certificate_request.AssociateCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.associate_certificate_response.AssociateCertificateResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.associate_certificate

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.associate_certificate.associate_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.associate_certificate_request.AssociateCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_job(
        self,
        id: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.cancel_job_response.CancelJobResponse":
        """Permanently cancel a job. Once you have canceled a job, you can't start it again.

        Args:
            id: The Job ID of the job to be cancelled.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.cancel_job_request.CancelJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.cancel_job_response.CancelJobResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.cancel_job

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.cancel_job.cancel_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.cancel_job_request.CancelJobRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_job(
        self,
        role: "aws_sdk_mediaconvert.types.__string.__string",
        settings: "aws_sdk_mediaconvert.types.job_settings.JobSettings",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        acceleration_settings: Optional[
            "aws_sdk_mediaconvert.types.acceleration_settings.AccelerationSettings"
        ] = None,
        billing_tags_source: Optional[
            "aws_sdk_mediaconvert.types.billing_tags_source.BillingTagsSource"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_mediaconvert.types.__string.__string"
        ] = None,
        hop_destinations: Optional[
            "aws_sdk_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
        ] = None,
        job_engine_version: Optional[
            "aws_sdk_mediaconvert.types.__string.__string"
        ] = None,
        job_template: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        priority: Optional[
            "aws_sdk_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
        ] = None,
        queue: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        simulate_reserved_queue: Optional[
            "aws_sdk_mediaconvert.types.simulate_reserved_queue.SimulateReservedQueue"
        ] = None,
        status_update_interval: Optional[
            "aws_sdk_mediaconvert.types.status_update_interval.StatusUpdateInterval"
        ] = None,
        tags: Optional[
            "aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
        user_metadata: Optional[
            "aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "aws_sdk_mediaconvert.types.create_job_response.CreateJobResponse":
        """Create a new transcoding job. For information about jobs and job settings, see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        Args:
            acceleration_settings: Optional. Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, see the AWS Elemental MediaConvert User Guide.
            billing_tags_source: Optionally choose a Billing tags source that AWS Billing and Cost Management will use to display tags for individual output costs on any billing report that you set up. Leave blank to use the default value, Job.
            client_request_token: Prevent duplicate jobs from being created and ensure idempotency for your requests. A client request token can be any string that includes up to 64 ASCII characters. If you reuse a client request token within one minute of a successful request, the API returns the job details of the original request instead. For more information see https://docs.aws.amazon.com/mediaconvert/latest/apireference/idempotency.html.
            hop_destinations: Optional. Use queue hopping to avoid overly long waits in the backlog of the queue that you submit your job to. Specify an alternate queue and the maximum time that your job will wait in the initial queue before hopping. For more information about this feature, see the AWS Elemental MediaConvert User Guide.
            job_engine_version: Use Job engine versions to run jobs for your production workflow on one version, while you test and validate the latest version. Job engine versions represent periodically grouped MediaConvert releases with new features, updates, improvements, and fixes. Job engine versions are in a YYYY-MM-DD format. Note that the Job engine version feature is not publicly available at this time. To request access, contact AWS support.
            job_template: Optional. When you create a job, you can either specify a job template or specify the transcoding settings individually.
            priority: Optional. Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0.
            queue: Optional. When you create a job, you can specify a queue to send it to. If you don't specify, the job will go to the default queue. For more about queues, see the User Guide topic at https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html.
            role: Required. The IAM role you use for creating this job. For details about permissions, see the User Guide topic at the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html.
            settings: JobSettings contains all the transcode settings for a job.
            simulate_reserved_queue: Optional. Enable this setting when you run a test job to estimate how many reserved transcoding slots (RTS) you need. When this is enabled, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. This setting is disabled by default.
            status_update_interval: Optional. Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error.
            tags: Optional. The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key. Use standard AWS tags on your job for automatic integration with AWS services and for custom integrations and workflows.
            user_metadata: Optional. User-defined metadata that you want to associate with an MediaConvert job. You specify metadata in key/value pairs. Use only for existing integrations or workflows that rely on job metadata tags. Otherwise, we recommend that you use standard AWS tags.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.create_job_request.CreateJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.create_job_response.CreateJobResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.create_job

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.create_job.create_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.create_job_request.CreateJobRequest = {}  # type: ignore[typeddict-item]
        if acceleration_settings is not None:
            input_["acceleration_settings"] = acceleration_settings
        if billing_tags_source is not None:
            input_["billing_tags_source"] = billing_tags_source
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if hop_destinations is not None:
            input_["hop_destinations"] = hop_destinations
        if job_engine_version is not None:
            input_["job_engine_version"] = job_engine_version
        if job_template is not None:
            input_["job_template"] = job_template
        if priority is not None:
            input_["priority"] = priority
        if queue is not None:
            input_["queue"] = queue
        input_["role"] = role
        input_["settings"] = settings
        if simulate_reserved_queue is not None:
            input_["simulate_reserved_queue"] = simulate_reserved_queue
        if status_update_interval is not None:
            input_["status_update_interval"] = status_update_interval
        if tags is not None:
            input_["tags"] = tags
        if user_metadata is not None:
            input_["user_metadata"] = user_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_job_template(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        settings: "aws_sdk_mediaconvert.types.job_template_settings.JobTemplateSettings",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        acceleration_settings: Optional[
            "aws_sdk_mediaconvert.types.acceleration_settings.AccelerationSettings"
        ] = None,
        category: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        description: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        hop_destinations: Optional[
            "aws_sdk_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
        ] = None,
        priority: Optional[
            "aws_sdk_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
        ] = None,
        queue: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        status_update_interval: Optional[
            "aws_sdk_mediaconvert.types.status_update_interval.StatusUpdateInterval"
        ] = None,
        tags: Optional[
            "aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "aws_sdk_mediaconvert.types.create_job_template_response.CreateJobTemplateResponse":
        """Create a new job template. For information about job templates see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        Args:
            acceleration_settings: Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, see the AWS Elemental MediaConvert User Guide.
            category: Optional. A category for the job template you are creating
            description: Optional. A description of the job template you are creating.
            hop_destinations: Optional. Use queue hopping to avoid overly long waits in the backlog of the queue that you submit your job to. Specify an alternate queue and the maximum time that your job will wait in the initial queue before hopping. For more information about this feature, see the AWS Elemental MediaConvert User Guide.
            name: The name of the job template you are creating.
            priority: Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0.
            queue: Optional. The queue that jobs created from this template are assigned to. If you don't specify this, jobs will go to the default queue.
            settings: JobTemplateSettings contains all the transcode settings saved in the template that will be applied to jobs created from it.
            status_update_interval: Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error.
            tags: The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.create_job_template_request.CreateJobTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.create_job_template_response.CreateJobTemplateResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.create_job_template

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.create_job_template.create_job_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.create_job_template_request.CreateJobTemplateRequest = {}  # type: ignore[typeddict-item]
        if acceleration_settings is not None:
            input_["acceleration_settings"] = acceleration_settings
        if category is not None:
            input_["category"] = category
        if description is not None:
            input_["description"] = description
        if hop_destinations is not None:
            input_["hop_destinations"] = hop_destinations
        input_["name"] = name
        if priority is not None:
            input_["priority"] = priority
        if queue is not None:
            input_["queue"] = queue
        input_["settings"] = settings
        if status_update_interval is not None:
            input_["status_update_interval"] = status_update_interval
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_preset(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        settings: "aws_sdk_mediaconvert.types.preset_settings.PresetSettings",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        category: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        description: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        tags: Optional[
            "aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "aws_sdk_mediaconvert.types.create_preset_response.CreatePresetResponse":
        """Create a new preset. For information about job templates see the User Guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        Args:
            category: Optional. A category for the preset you are creating.
            description: Optional. A description of the preset you are creating.
            name: The name of the preset you are creating.
            settings: Settings for preset
            tags: The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.create_preset_request.CreatePresetRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.create_preset_response.CreatePresetResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.create_preset

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.create_preset.create_preset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.create_preset_request.CreatePresetRequest = {}  # type: ignore[typeddict-item]
        if category is not None:
            input_["category"] = category
        if description is not None:
            input_["description"] = description
        input_["name"] = name
        input_["settings"] = settings
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_queue(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        concurrent_jobs: Optional[
            "aws_sdk_mediaconvert.types.__integer.__integer"
        ] = None,
        description: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        maximum_concurrent_feeds: Optional[
            "aws_sdk_mediaconvert.types.__integer_min0.__integerMin0"
        ] = None,
        pricing_plan: Optional[
            "aws_sdk_mediaconvert.types.pricing_plan.PricingPlan"
        ] = None,
        reservation_plan_settings: Optional[
            "aws_sdk_mediaconvert.types.reservation_plan_settings.ReservationPlanSettings"
        ] = None,
        status: Optional["aws_sdk_mediaconvert.types.queue_status.QueueStatus"] = None,
        tags: Optional[
            "aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "aws_sdk_mediaconvert.types.create_queue_response.CreateQueueResponse":
        """Create a new transcoding queue. For information about queues, see Working With Queues in the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html

        Args:
            concurrent_jobs: Specify the maximum number of jobs your queue can process concurrently. For on-demand queues, the value you enter is constrained by your service quotas for Maximum concurrent jobs, per on-demand queue and Maximum concurrent jobs, per account. For reserved queues, specify the number of jobs you can process concurrently in your reservation plan instead.
            description: Optional. A description of the queue that you are creating.
            maximum_concurrent_feeds: Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently.
            name: The name of the queue that you are creating.
            pricing_plan: Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment. When you use the API to create a queue, the default is on-demand.
            reservation_plan_settings: Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues.
            status: Initial state of the queue. If you create a paused queue, then jobs in that queue won't begin.
            tags: The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.create_queue_request.CreateQueueRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.create_queue_response.CreateQueueResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.create_queue

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.create_queue.create_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.create_queue_request.CreateQueueRequest = {}  # type: ignore[typeddict-item]
        if concurrent_jobs is not None:
            input_["concurrent_jobs"] = concurrent_jobs
        if description is not None:
            input_["description"] = description
        if maximum_concurrent_feeds is not None:
            input_["maximum_concurrent_feeds"] = maximum_concurrent_feeds
        input_["name"] = name
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if reservation_plan_settings is not None:
            input_["reservation_plan_settings"] = reservation_plan_settings
        if status is not None:
            input_["status"] = status
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_resource_share(
        self,
        job_id: "aws_sdk_mediaconvert.types.__string.__string",
        support_case_id: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.create_resource_share_response.CreateResourceShareResponse":
        """Create a new resource share request for MediaConvert resources with AWS Support.

        Args:
            job_id: Specify MediaConvert Job ID or ARN to share
            support_case_id: AWS Support case identifier

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.create_resource_share_request.CreateResourceShareRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.create_resource_share_response.CreateResourceShareResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.create_resource_share

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.create_resource_share.create_resource_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.create_resource_share_request.CreateResourceShareRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id
        input_["support_case_id"] = support_case_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_job_template(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.delete_job_template_response.DeleteJobTemplateResponse":
        """Permanently delete a job template you have created.

        Args:
            name: The name of the job template to be deleted.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.delete_job_template_request.DeleteJobTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.delete_job_template_response.DeleteJobTemplateResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.delete_job_template

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.delete_job_template.delete_job_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.delete_job_template_request.DeleteJobTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_policy(
        self, *, config_overrides: Optional[MediaConvertClientConfig] = None
    ) -> "aws_sdk_mediaconvert.types.delete_policy_response.DeletePolicyResponse":
        """Permanently delete a policy that you created.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.delete_policy_request.DeletePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.delete_policy_response.DeletePolicyResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.delete_policy

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.delete_policy.delete_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.delete_policy_request.DeletePolicyRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_preset(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.delete_preset_response.DeletePresetResponse":
        """Permanently delete a preset you have created.

        Args:
            name: The name of the preset to be deleted.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.delete_preset_request.DeletePresetRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.delete_preset_response.DeletePresetResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.delete_preset

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.delete_preset.delete_preset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.delete_preset_request.DeletePresetRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_queue(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.delete_queue_response.DeleteQueueResponse":
        """Permanently delete a queue you have created.

        Args:
            name: The name of the queue that you want to delete.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.delete_queue_request.DeleteQueueRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.delete_queue_response.DeleteQueueResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.delete_queue

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.delete_queue.delete_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.delete_queue_request.DeleteQueueRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_endpoints(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        max_results: Optional["aws_sdk_mediaconvert.types.__integer.__integer"] = None,
        mode: Optional[
            "aws_sdk_mediaconvert.types.describe_endpoints_mode.DescribeEndpointsMode"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
    ) -> "aws_sdk_mediaconvert.types.describe_endpoints_response.DescribeEndpointsResponse":
        """Send a request with an empty body to the regional API endpoint to get your account API endpoint. Note that DescribeEndpoints is no longer required. We recommend that you send your requests directly to the regional endpoint instead.

        Args:
            max_results: Optional. Max number of endpoints, up to twenty, that will be returned at one time.
            mode: Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to return your endpoints if any exist, or to create an endpoint for you and return it if one doesn't already exist. Specify GET_ONLY to return your endpoints if any exist, or an empty list if none exist.
            next_token: Use this string, provided with the response to a previous request, to request the next batch of endpoints.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.describe_endpoints_request.DescribeEndpointsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.describe_endpoints_response.DescribeEndpointsResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.describe_endpoints

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.describe_endpoints.describe_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.describe_endpoints_request.DescribeEndpointsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if mode is not None:
            input_["mode"] = mode
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_endpoints(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        max_results: Optional["aws_sdk_mediaconvert.types.__integer.__integer"] = None,
        mode: Optional[
            "aws_sdk_mediaconvert.types.describe_endpoints_mode.DescribeEndpointsMode"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_mediaconvert.types.endpoint.Endpoint]":
        _token = next_token
        while True:
            _response = self.describe_endpoints(
                config_overrides=config_overrides,
                max_results=max_results,
                mode=mode,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def disassociate_certificate(
        self,
        arn: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.disassociate_certificate_response.DisassociateCertificateResponse":
        """Removes an association between the Amazon Resource Name (ARN) of an AWS Certificate Manager (ACM) certificate and an AWS Elemental MediaConvert resource.

        Args:
            arn: The ARN of the ACM certificate that you want to disassociate from your MediaConvert resource.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.disassociate_certificate_request.DisassociateCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.disassociate_certificate_response.DisassociateCertificateResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.disassociate_certificate

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.disassociate_certificate.disassociate_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.disassociate_certificate_request.DisassociateCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_job(
        self,
        id: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.get_job_response.GetJobResponse":
        """Retrieve the JSON for a specific transcoding job.

        Args:
            id: the job ID of the job.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.get_job_request.GetJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.get_job_response.GetJobResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.get_job

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.get_job.get_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.get_job_request.GetJobRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_jobs_query_results(
        self,
        id: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.get_jobs_query_results_response.GetJobsQueryResultsResponse":
        """Retrieve a JSON array of up to twenty of your most recent jobs matched by a jobs query.

        Args:
            id: The ID of the jobs query.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.get_jobs_query_results_request.GetJobsQueryResultsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.get_jobs_query_results_response.GetJobsQueryResultsResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.get_jobs_query_results

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.get_jobs_query_results.get_jobs_query_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.get_jobs_query_results_request.GetJobsQueryResultsRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_job_template(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.get_job_template_response.GetJobTemplateResponse":
        """Retrieve the JSON for a specific job template.

        Args:
            name: The name of the job template.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.get_job_template_request.GetJobTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.get_job_template_response.GetJobTemplateResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.get_job_template

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.get_job_template.get_job_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.get_job_template_request.GetJobTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_policy(
        self, *, config_overrides: Optional[MediaConvertClientConfig] = None
    ) -> "aws_sdk_mediaconvert.types.get_policy_response.GetPolicyResponse":
        """Retrieve the JSON for your policy.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.get_policy_request.GetPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.get_policy_response.GetPolicyResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.get_policy

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.get_policy_request.GetPolicyRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_preset(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.get_preset_response.GetPresetResponse":
        """Retrieve the JSON for a specific preset.

        Args:
            name: The name of the preset.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.get_preset_request.GetPresetRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.get_preset_response.GetPresetResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.get_preset

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.get_preset.get_preset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.get_preset_request.GetPresetRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_queue(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.get_queue_response.GetQueueResponse":
        """Retrieve the JSON for a specific queue.

        Args:
            name: The name of the queue that you want information about.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.get_queue_request.GetQueueRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.get_queue_response.GetQueueResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.get_queue

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.get_queue.get_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.get_queue_request.GetQueueRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_jobs(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
        queue: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        status: Optional["aws_sdk_mediaconvert.types.job_status.JobStatus"] = None,
    ) -> "aws_sdk_mediaconvert.types.list_jobs_response.ListJobsResponse":
        """Retrieve a JSON array of up to twenty of your most recently created jobs. This array includes in-process, completed, and errored jobs. This will return the jobs themselves, not just a list of the jobs. To retrieve the twenty next most recent jobs, use the nextToken string returned with the array.

        Args:
            max_results: Optional. Number of jobs, up to twenty, that will be returned at one time.
            next_token: Optional. Use this string, provided with the response to a previous request, to request the next batch of jobs.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
            queue: Optional. Provide a queue name to get back only jobs from that queue.
            status: Optional. A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.list_jobs_request.ListJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.list_jobs_response.ListJobsResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.list_jobs

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.list_jobs.list_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.list_jobs_request.ListJobsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order
        if queue is not None:
            input_["queue"] = queue
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_jobs(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
        queue: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        status: Optional["aws_sdk_mediaconvert.types.job_status.JobStatus"] = None,
    ) -> "Iterator[aws_sdk_mediaconvert.types.job.Job]":
        _token = next_token
        while True:
            _response = self.list_jobs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                order=order,
                queue=queue,
                status=status,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_job_templates(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        category: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        list_by: Optional[
            "aws_sdk_mediaconvert.types.job_template_list_by.JobTemplateListBy"
        ] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
    ) -> "aws_sdk_mediaconvert.types.list_job_templates_response.ListJobTemplatesResponse":
        """Retrieve a JSON array of up to twenty of your job templates. This will return the templates themselves, not just a list of them. To retrieve the next twenty templates, use the nextToken string returned with the array

        Args:
            category: Optionally, specify a job template category to limit responses to only job templates from that category.
            list_by: Optional. When you request a list of job templates, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name.
            max_results: Optional. Number of job templates, up to twenty, that will be returned at one time.
            next_token: Use this string, provided with the response to a previous request, to request the next batch of job templates.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.list_job_templates_request.ListJobTemplatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.list_job_templates_response.ListJobTemplatesResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.list_job_templates

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.list_job_templates.list_job_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.list_job_templates_request.ListJobTemplatesRequest = {}  # type: ignore[typeddict-item]
        if category is not None:
            input_["category"] = category
        if list_by is not None:
            input_["list_by"] = list_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_job_templates(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        category: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        list_by: Optional[
            "aws_sdk_mediaconvert.types.job_template_list_by.JobTemplateListBy"
        ] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
    ) -> "Iterator[aws_sdk_mediaconvert.types.job_template.JobTemplate]":
        _token = next_token
        while True:
            _response = self.list_job_templates(
                config_overrides=config_overrides,
                category=category,
                list_by=list_by,
                max_results=max_results,
                next_token=_token,
                order=order,
            )
            _page = _resolve_path(_response, ("job_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_presets(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        category: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        list_by: Optional[
            "aws_sdk_mediaconvert.types.preset_list_by.PresetListBy"
        ] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
    ) -> "aws_sdk_mediaconvert.types.list_presets_response.ListPresetsResponse":
        """Retrieve a JSON array of up to twenty of your presets. This will return the presets themselves, not just a list of them. To retrieve the next twenty presets, use the nextToken string returned with the array.

        Args:
            category: Optionally, specify a preset category to limit responses to only presets from that category.
            list_by: Optional. When you request a list of presets, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name.
            max_results: Optional. Number of presets, up to twenty, that will be returned at one time
            next_token: Use this string, provided with the response to a previous request, to request the next batch of presets.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.list_presets_request.ListPresetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.list_presets_response.ListPresetsResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.list_presets

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.list_presets.list_presets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.list_presets_request.ListPresetsRequest = {}  # type: ignore[typeddict-item]
        if category is not None:
            input_["category"] = category
        if list_by is not None:
            input_["list_by"] = list_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_presets(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        category: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        list_by: Optional[
            "aws_sdk_mediaconvert.types.preset_list_by.PresetListBy"
        ] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
    ) -> "Iterator[aws_sdk_mediaconvert.types.preset.Preset]":
        _token = next_token
        while True:
            _response = self.list_presets(
                config_overrides=config_overrides,
                category=category,
                list_by=list_by,
                max_results=max_results,
                next_token=_token,
                order=order,
            )
            _page = _resolve_path(_response, ("presets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_queues(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        list_by: Optional[
            "aws_sdk_mediaconvert.types.queue_list_by.QueueListBy"
        ] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
    ) -> "aws_sdk_mediaconvert.types.list_queues_response.ListQueuesResponse":
        """Retrieve a JSON array of up to twenty of your queues. This will return the queues themselves, not just a list of them. To retrieve the next twenty queues, use the nextToken string returned with the array.

        Args:
            list_by: Optional. When you request a list of queues, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by creation date.
            max_results: Optional. Number of queues, up to twenty, that will be returned at one time.
            next_token: Use this string, provided with the response to a previous request, to request the next batch of queues.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.list_queues_request.ListQueuesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.list_queues_response.ListQueuesResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.list_queues

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.list_queues.list_queues(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.list_queues_request.ListQueuesRequest = {}  # type: ignore[typeddict-item]
        if list_by is not None:
            input_["list_by"] = list_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_queues(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        list_by: Optional[
            "aws_sdk_mediaconvert.types.queue_list_by.QueueListBy"
        ] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
    ) -> "Iterator[aws_sdk_mediaconvert.types.queue.Queue]":
        _token = next_token
        while True:
            _response = self.list_queues(
                config_overrides=config_overrides,
                list_by=list_by,
                max_results=max_results,
                next_token=_token,
                order=order,
            )
            _page = _resolve_path(_response, ("queues",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        arn: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """Retrieve the tags for a MediaConvert resource.

        Args:
            arn: The Amazon Resource Name (ARN) of the resource that you want to list tags for. To get the ARN, send a GET request with the resource name.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.list_tags_for_resource

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_versions(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
    ) -> "aws_sdk_mediaconvert.types.list_versions_response.ListVersionsResponse":
        """Retrieve a JSON array of all available Job engine versions and the date they expire.

        Args:
            max_results: Optional. Number of valid Job engine versions, up to twenty, that will be returned at one time.
            next_token: Optional. Use this string, provided with the response to a previous request, to request the next batch of Job engine versions.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.list_versions_request.ListVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.list_versions_response.ListVersionsResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.list_versions

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.list_versions.list_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.list_versions_request.ListVersionsRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_versions(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_mediaconvert.types.job_engine_version.JobEngineVersion]":
        _token = next_token
        while True:
            _response = self.list_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def probe(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        input_files: Optional[
            "aws_sdk_mediaconvert.types.__list_of_probe_input_file.__listOfProbeInputFile"
        ] = None,
    ) -> "aws_sdk_mediaconvert.types.probe_response.ProbeResponse":
        """Use Probe to obtain detailed information about your input media files. Probe returns a JSON that includes container, codec, frame rate, resolution, track count, audio layout, captions, and more. You can use this information to learn more about your media files, or to help make decisions while automating your transcoding workflow.

        Args:
            input_files: Specify a media file to probe.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.probe_request.ProbeRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.probe_response.ProbeResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.probe

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.probe.probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.probe_request.ProbeRequest = {}  # type: ignore[typeddict-item]
        if input_files is not None:
            input_["input_files"] = input_files

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_policy(
        self,
        policy: "aws_sdk_mediaconvert.types.policy.Policy",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.put_policy_response.PutPolicyResponse":
        """Create or change your policy. For more information about policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        Args:
            policy: A policy configures behavior that you allow or disallow for your account. For information about MediaConvert policies, see the user guide at http://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.put_policy_request.PutPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.put_policy_response.PutPolicyResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.put_policy

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.put_policy.put_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.put_policy_request.PutPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_jobs(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        input_file: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
        queue: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        status: Optional["aws_sdk_mediaconvert.types.job_status.JobStatus"] = None,
    ) -> "aws_sdk_mediaconvert.types.search_jobs_response.SearchJobsResponse":
        """Retrieve a JSON array that includes job details for up to twenty of your most recent jobs. Optionally filter results further according to input file, queue, or status. To retrieve the twenty next most recent jobs, use the nextToken string returned with the array.

        Args:
            input_file: Optional. Provide your input file URL or your partial input file name. The maximum length for an input file is 300 characters.
            max_results: Optional. Number of jobs, up to twenty, that will be returned at one time.
            next_token: Optional. Use this string, provided with the response to a previous request, to request the next batch of jobs.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
            queue: Optional. Provide a queue name, or a queue ARN, to return only jobs from that queue.
            status: Optional. A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.search_jobs_request.SearchJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.search_jobs_response.SearchJobsResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.search_jobs

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.search_jobs.search_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.search_jobs_request.SearchJobsRequest = {}  # type: ignore[typeddict-item]
        if input_file is not None:
            input_["input_file"] = input_file
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order
        if queue is not None:
            input_["queue"] = queue
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_search_jobs(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        input_file: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
        queue: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        status: Optional["aws_sdk_mediaconvert.types.job_status.JobStatus"] = None,
    ) -> "Iterator[aws_sdk_mediaconvert.types.job.Job]":
        _token = next_token
        while True:
            _response = self.search_jobs(
                config_overrides=config_overrides,
                input_file=input_file,
                max_results=max_results,
                next_token=_token,
                order=order,
                queue=queue,
                status=status,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_jobs_query(
        self,
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        filter_list: Optional[
            "aws_sdk_mediaconvert.types.__list_of_jobs_query_filter.__listOfJobsQueryFilter"
        ] = None,
        max_results: Optional[
            "aws_sdk_mediaconvert.types.__integer_min1_max20.__integerMin1Max20"
        ] = None,
        next_token: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        order: Optional["aws_sdk_mediaconvert.types.order.Order"] = None,
    ) -> "aws_sdk_mediaconvert.types.start_jobs_query_response.StartJobsQueryResponse":
        """Start an asynchronous jobs query using the provided filters. To receive the list of jobs that match your query, call the GetJobsQueryResults API using the query ID returned by this API.

        Args:
            filter_list: Optional. Provide an array of JobsQueryFilters for your StartJobsQuery request.
            max_results: Optional. Number of jobs, up to twenty, that will be included in the jobs query.
            next_token: Use this string to request the next batch of jobs matched by a jobs query.
            order: Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.start_jobs_query_request.StartJobsQueryRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.start_jobs_query_response.StartJobsQueryResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.start_jobs_query

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.start_jobs_query.start_jobs_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.start_jobs_query_request.StartJobsQueryRequest = {}  # type: ignore[typeddict-item]
        if filter_list is not None:
            input_["filter_list"] = filter_list
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if order is not None:
            input_["order"] = order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        arn: "aws_sdk_mediaconvert.types.__string.__string",
        tags: "aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
    ) -> "aws_sdk_mediaconvert.types.tag_resource_response.TagResourceResponse":
        """Add tags to a MediaConvert queue, preset, job, or job template. For information about tagging, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-mediaconvert-resources.html.

        Args:
            arn: The Amazon Resource Name (ARN) of the resource that you want to tag. To get the ARN, send a GET request with the resource name.
            tags: The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.tag_resource

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        arn: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        tag_keys: Optional[
            "aws_sdk_mediaconvert.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "aws_sdk_mediaconvert.types.untag_resource_response.UntagResourceResponse":
        """Remove tags from a MediaConvert queue, preset, job, or job template. For information about tagging, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-mediaconvert-resources.html.

        Args:
            arn: The Amazon Resource Name (ARN) of the resource that you want to remove tags from. To get the ARN, send a GET request with the resource name.
            tag_keys: The keys of the tags that you want to remove from the resource.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.untag_resource

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_job_template(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        acceleration_settings: Optional[
            "aws_sdk_mediaconvert.types.acceleration_settings.AccelerationSettings"
        ] = None,
        category: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        description: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        hop_destinations: Optional[
            "aws_sdk_mediaconvert.types.__list_of_hop_destination.__listOfHopDestination"
        ] = None,
        priority: Optional[
            "aws_sdk_mediaconvert.types.__integer_min_negative50_max50.__integerMinNegative50Max50"
        ] = None,
        queue: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        settings: Optional[
            "aws_sdk_mediaconvert.types.job_template_settings.JobTemplateSettings"
        ] = None,
        status_update_interval: Optional[
            "aws_sdk_mediaconvert.types.status_update_interval.StatusUpdateInterval"
        ] = None,
    ) -> "aws_sdk_mediaconvert.types.update_job_template_response.UpdateJobTemplateResponse":
        """Modify one of your existing job templates.

        Args:
            acceleration_settings: Accelerated transcoding can significantly speed up jobs with long, visually complex content. Outputs that use this feature incur pro-tier pricing. For information about feature limitations, see the AWS Elemental MediaConvert User Guide.
            category: The new category for the job template, if you are changing it.
            description: The new description for the job template, if you are changing it.
            hop_destinations: Optional list of hop destinations.
            name: The name of the job template you are modifying
            priority: Specify the relative priority for this job. In any given queue, the service begins processing the job with the highest value first. When more than one job has the same priority, the service begins processing the job that you submitted first. If you don't specify a priority, the service uses the default value 0.
            queue: The new queue for the job template, if you are changing it.
            settings: JobTemplateSettings contains all the transcode settings saved in the template that will be applied to jobs created from it.
            status_update_interval: Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.update_job_template_request.UpdateJobTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.update_job_template_response.UpdateJobTemplateResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.update_job_template

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.update_job_template.update_job_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.update_job_template_request.UpdateJobTemplateRequest = {}  # type: ignore[typeddict-item]
        if acceleration_settings is not None:
            input_["acceleration_settings"] = acceleration_settings
        if category is not None:
            input_["category"] = category
        if description is not None:
            input_["description"] = description
        if hop_destinations is not None:
            input_["hop_destinations"] = hop_destinations
        input_["name"] = name
        if priority is not None:
            input_["priority"] = priority
        if queue is not None:
            input_["queue"] = queue
        if settings is not None:
            input_["settings"] = settings
        if status_update_interval is not None:
            input_["status_update_interval"] = status_update_interval

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_preset(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        category: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        description: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        settings: Optional[
            "aws_sdk_mediaconvert.types.preset_settings.PresetSettings"
        ] = None,
    ) -> "aws_sdk_mediaconvert.types.update_preset_response.UpdatePresetResponse":
        """Modify one of your existing presets.

        Args:
            category: The new category for the preset, if you are changing it.
            description: The new description for the preset, if you are changing it.
            name: The name of the preset you are modifying.
            settings: Settings for preset

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.update_preset_request.UpdatePresetRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.update_preset_response.UpdatePresetResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.update_preset

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.update_preset.update_preset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.update_preset_request.UpdatePresetRequest = {}  # type: ignore[typeddict-item]
        if category is not None:
            input_["category"] = category
        if description is not None:
            input_["description"] = description
        input_["name"] = name
        if settings is not None:
            input_["settings"] = settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_queue(
        self,
        name: "aws_sdk_mediaconvert.types.__string.__string",
        *,
        config_overrides: Optional[MediaConvertClientConfig] = None,
        concurrent_jobs: Optional[
            "aws_sdk_mediaconvert.types.__integer.__integer"
        ] = None,
        description: Optional["aws_sdk_mediaconvert.types.__string.__string"] = None,
        maximum_concurrent_feeds: Optional[
            "aws_sdk_mediaconvert.types.__integer_min0.__integerMin0"
        ] = None,
        reservation_plan_settings: Optional[
            "aws_sdk_mediaconvert.types.reservation_plan_settings.ReservationPlanSettings"
        ] = None,
        status: Optional["aws_sdk_mediaconvert.types.queue_status.QueueStatus"] = None,
    ) -> "aws_sdk_mediaconvert.types.update_queue_response.UpdateQueueResponse":
        """Modify one of your existing queues.

        Args:
            concurrent_jobs: Specify the maximum number of jobs your queue can process concurrently. For on-demand queues, the value you enter is constrained by your service quotas for Maximum concurrent jobs, per on-demand queue and Maximum concurrent jobs, per account. For reserved queues, update your reservation plan instead in order to increase your yearly commitment.
            description: The new description for the queue, if you are changing it.
            maximum_concurrent_feeds: Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently.
            name: The name of the queue that you are modifying.
            reservation_plan_settings: The new details of your pricing plan for your reserved queue. When you set up a new pricing plan to replace an expired one, you enter into another 12-month commitment. When you add capacity to your queue by increasing the number of RTS, you extend the term of your commitment to 12 months from when you add capacity. After you make these commitments, you can't cancel them.
            status: Pause or activate a queue by changing its status between ACTIVE and PAUSED. If you pause a queue, jobs in that queue won't begin. Jobs that are running when you pause the queue continue to run until they finish or result in an error.

        Raises:
            aws_sdk_mediaconvert.errors.bad_request_exception.BadRequestException: The service can't process your request because of a problem in the request. Please check your request form and syntax.
            aws_sdk_mediaconvert.errors.conflict_exception.ConflictException: The service couldn't complete your request because there is a conflict with the current state of the resource.
            aws_sdk_mediaconvert.errors.forbidden_exception.ForbiddenException: You don't have permissions for this action with the credentials you sent.
            aws_sdk_mediaconvert.errors.internal_server_error_exception.InternalServerErrorException: The service encountered an unexpected condition and can't fulfill your request.
            aws_sdk_mediaconvert.errors.not_found_exception.NotFoundException: The resource you requested doesn't exist.
            aws_sdk_mediaconvert.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You attempted to create more resources than the service allows based on service quotas.
            aws_sdk_mediaconvert.errors.too_many_requests_exception.TooManyRequestsException: Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests.
            aws_sdk_mediaconvert.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconvert.types.update_queue_request.UpdateQueueRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconvert.types.update_queue_response.UpdateQueueResponse"
        ]:
            import aws_sdk_mediaconvert._operations.media_convert.update_queue

            output, http_response = (
                aws_sdk_mediaconvert._operations.media_convert.update_queue.update_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediaconvert.types.update_queue_request.UpdateQueueRequest = {}  # type: ignore[typeddict-item]
        if concurrent_jobs is not None:
            input_["concurrent_jobs"] = concurrent_jobs
        if description is not None:
            input_["description"] = description
        if maximum_concurrent_feeds is not None:
            input_["maximum_concurrent_feeds"] = maximum_concurrent_feeds
        input_["name"] = name
        if reservation_plan_settings is not None:
            input_["reservation_plan_settings"] = reservation_plan_settings
        if status is not None:
            input_["status"] = status

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
