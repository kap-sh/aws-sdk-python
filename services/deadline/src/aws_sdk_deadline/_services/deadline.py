"""Generated from Smithy shape ``com.amazonaws.deadline#Deadline``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_deadline._auth._signers
import aws_sdk_deadline._auth._sigv4
from aws_sdk_deadline._auth._identity import Credentials
from aws_sdk_deadline._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_deadline._auth._zapros_handler import AuthMiddleware
from aws_sdk_deadline._pagination import resolve_path as _resolve_path
from aws_sdk_deadline._resources.deadline.farm_resource import FarmResource
from aws_sdk_deadline._resources.deadline.license_endpoint_resource import (
    LicenseEndpointResource,
)
from aws_sdk_deadline._resources.deadline.monitor_resource import MonitorResource
from aws_sdk_deadline._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_deadline.types.aggregation_id
    import aws_sdk_deadline.types.batch_get_job_identifiers
    import aws_sdk_deadline.types.batch_get_job_request
    import aws_sdk_deadline.types.batch_get_job_response
    import aws_sdk_deadline.types.batch_get_session_action_identifiers
    import aws_sdk_deadline.types.batch_get_session_action_request
    import aws_sdk_deadline.types.batch_get_session_action_response
    import aws_sdk_deadline.types.batch_get_session_identifiers
    import aws_sdk_deadline.types.batch_get_session_request
    import aws_sdk_deadline.types.batch_get_session_response
    import aws_sdk_deadline.types.batch_get_step_identifiers
    import aws_sdk_deadline.types.batch_get_step_request
    import aws_sdk_deadline.types.batch_get_step_response
    import aws_sdk_deadline.types.batch_get_task_identifiers
    import aws_sdk_deadline.types.batch_get_task_request
    import aws_sdk_deadline.types.batch_get_task_response
    import aws_sdk_deadline.types.batch_get_worker_identifiers
    import aws_sdk_deadline.types.batch_get_worker_request
    import aws_sdk_deadline.types.batch_get_worker_response
    import aws_sdk_deadline.types.batch_update_job_items
    import aws_sdk_deadline.types.batch_update_job_request
    import aws_sdk_deadline.types.batch_update_job_response
    import aws_sdk_deadline.types.batch_update_task_items
    import aws_sdk_deadline.types.batch_update_task_request
    import aws_sdk_deadline.types.batch_update_task_response
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.create_queue_fleet_association_request
    import aws_sdk_deadline.types.create_queue_fleet_association_response
    import aws_sdk_deadline.types.create_queue_limit_association_request
    import aws_sdk_deadline.types.create_queue_limit_association_response
    import aws_sdk_deadline.types.delete_queue_fleet_association_request
    import aws_sdk_deadline.types.delete_queue_fleet_association_response
    import aws_sdk_deadline.types.delete_queue_limit_association_request
    import aws_sdk_deadline.types.delete_queue_limit_association_response
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.fleet_ids
    import aws_sdk_deadline.types.get_queue_fleet_association_request
    import aws_sdk_deadline.types.get_queue_fleet_association_response
    import aws_sdk_deadline.types.get_queue_limit_association_request
    import aws_sdk_deadline.types.get_queue_limit_association_response
    import aws_sdk_deadline.types.get_sessions_statistics_aggregation_request
    import aws_sdk_deadline.types.get_sessions_statistics_aggregation_response
    import aws_sdk_deadline.types.integer
    import aws_sdk_deadline.types.job_id
    import aws_sdk_deadline.types.limit_id
    import aws_sdk_deadline.types.list_available_metered_products_request
    import aws_sdk_deadline.types.list_available_metered_products_response
    import aws_sdk_deadline.types.list_queue_fleet_associations_request
    import aws_sdk_deadline.types.list_queue_fleet_associations_response
    import aws_sdk_deadline.types.list_queue_limit_associations_request
    import aws_sdk_deadline.types.list_queue_limit_associations_response
    import aws_sdk_deadline.types.list_tags_for_resource_request
    import aws_sdk_deadline.types.list_tags_for_resource_response
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.metered_product_summary
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.period
    import aws_sdk_deadline.types.queue_fleet_association_summary
    import aws_sdk_deadline.types.queue_id
    import aws_sdk_deadline.types.queue_ids
    import aws_sdk_deadline.types.queue_limit_association_summary
    import aws_sdk_deadline.types.search_grouped_filter_expressions
    import aws_sdk_deadline.types.search_jobs_request
    import aws_sdk_deadline.types.search_jobs_response
    import aws_sdk_deadline.types.search_sort_expressions
    import aws_sdk_deadline.types.search_steps_request
    import aws_sdk_deadline.types.search_steps_response
    import aws_sdk_deadline.types.search_tasks_request
    import aws_sdk_deadline.types.search_tasks_response
    import aws_sdk_deadline.types.search_workers_request
    import aws_sdk_deadline.types.search_workers_response
    import aws_sdk_deadline.types.sessions_statistics_resources
    import aws_sdk_deadline.types.start_sessions_statistics_aggregation_request
    import aws_sdk_deadline.types.start_sessions_statistics_aggregation_response
    import aws_sdk_deadline.types.statistics
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.string_list
    import aws_sdk_deadline.types.tag_resource_request
    import aws_sdk_deadline.types.tag_resource_response
    import aws_sdk_deadline.types.tags
    import aws_sdk_deadline.types.timestamp
    import aws_sdk_deadline.types.timezone
    import aws_sdk_deadline.types.untag_resource_request
    import aws_sdk_deadline.types.untag_resource_response
    import aws_sdk_deadline.types.update_queue_fleet_association_request
    import aws_sdk_deadline.types.update_queue_fleet_association_response
    import aws_sdk_deadline.types.update_queue_fleet_association_status
    import aws_sdk_deadline.types.update_queue_limit_association_request
    import aws_sdk_deadline.types.update_queue_limit_association_response
    import aws_sdk_deadline.types.update_queue_limit_association_status
    import aws_sdk_deadline.types.usage_group_by
    import aws_sdk_deadline.types.usage_statistics


class deadlineClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class deadlineClient:
    """A client for the ``deadline`` service.

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
        self._config = deadlineClientConfig(
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
        self.farm_resource = FarmResource(self)
        self.license_endpoint_resource = LicenseEndpointResource(self)
        self.monitor_resource = MonitorResource(self)

    def operation_options(
        self, config_overrides: Optional[deadlineClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: deadlineClientConfig = config_overrides or {}
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

    def batch_get_job(
        self,
        identifiers: "aws_sdk_deadline.types.batch_get_job_identifiers.BatchGetJobIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.batch_get_job_response.BatchGetJobResponse":
        """<p>Retrieves multiple jobs in a single request. This is a batch version of the <code>GetJob</code> API.</p> <p>The result of getting each job is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of job identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Examples:
            Get multiple jobs in a single request

            >>> client.batch_get_job(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-234567890abcdef1234567890abcdef1'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.batch_get_job_request.BatchGetJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.batch_get_job_response.BatchGetJobResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.batch_get_job

            output, http_response = (
                aws_sdk_deadline._operations.deadline.batch_get_job.batch_get_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.batch_get_job_request.BatchGetJobRequest = {}  # type: ignore[typeddict-item]
        input_["identifiers"] = identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_session(
        self,
        identifiers: "aws_sdk_deadline.types.batch_get_session_identifiers.BatchGetSessionIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.batch_get_session_response.BatchGetSessionResponse":
        """<p>Retrieves multiple sessions in a single request. This is a batch version of the <code>GetSession</code> API.</p> <p>The result of getting each session is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of session identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Examples:
            Get multiple sessions in a single request

            >>> client.batch_get_session(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'sessionId': 'session-1234567890abcdef1234567890abcdef'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'sessionId': 'session-234567890abcdef1234567890abcdef1'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.batch_get_session_request.BatchGetSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.batch_get_session_response.BatchGetSessionResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.batch_get_session

            output, http_response = (
                aws_sdk_deadline._operations.deadline.batch_get_session.batch_get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.batch_get_session_request.BatchGetSessionRequest = {}  # type: ignore[typeddict-item]
        input_["identifiers"] = identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_session_action(
        self,
        identifiers: "aws_sdk_deadline.types.batch_get_session_action_identifiers.BatchGetSessionActionIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.batch_get_session_action_response.BatchGetSessionActionResponse":
        """<p>Retrieves multiple session actions in a single request. This is a batch version of the <code>GetSessionAction</code> API.</p> <p>The result of getting each session action is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of session action identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Examples:
            Get multiple session actions in a single request

            >>> client.batch_get_session_action(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'sessionActionId': 'sessionaction-1234567890abcdef1234567890abcdef-0'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'sessionActionId': 'sessionaction-1234567890abcdef1234567890abcdef-1'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.batch_get_session_action_request.BatchGetSessionActionRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.batch_get_session_action_response.BatchGetSessionActionResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.batch_get_session_action

            output, http_response = (
                aws_sdk_deadline._operations.deadline.batch_get_session_action.batch_get_session_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.batch_get_session_action_request.BatchGetSessionActionRequest = {}  # type: ignore[typeddict-item]
        input_["identifiers"] = identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_step(
        self,
        identifiers: "aws_sdk_deadline.types.batch_get_step_identifiers.BatchGetStepIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.batch_get_step_response.BatchGetStepResponse":
        """<p>Retrieves multiple steps in a single request. This is a batch version of the <code>GetStep</code> API.</p> <p>The result of getting each step is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of step identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Examples:
            Get multiple steps in a single request

            >>> client.batch_get_step(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-1234567890abcdef1234567890abcdef'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-234567890abcdef1234567890abcdef1'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.batch_get_step_request.BatchGetStepRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.batch_get_step_response.BatchGetStepResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.batch_get_step

            output, http_response = (
                aws_sdk_deadline._operations.deadline.batch_get_step.batch_get_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.batch_get_step_request.BatchGetStepRequest = {}  # type: ignore[typeddict-item]
        input_["identifiers"] = identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_task(
        self,
        identifiers: "aws_sdk_deadline.types.batch_get_task_identifiers.BatchGetTaskIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.batch_get_task_response.BatchGetTaskResponse":
        """<p>Retrieves multiple tasks in a single request. This is a batch version of the <code>GetTask</code> API.</p> <p>The result of getting each task is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of task identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Examples:
            Get multiple tasks in a single request

            >>> client.batch_get_task(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-1234567890abcdef1234567890abcdef', 'taskId': 'task-1234567890abcdef1234567890abcdef-0'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-1234567890abcdef1234567890abcdef', 'taskId': 'task-1234567890abcdef1234567890abcdef-1'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.batch_get_task_request.BatchGetTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.batch_get_task_response.BatchGetTaskResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.batch_get_task

            output, http_response = (
                aws_sdk_deadline._operations.deadline.batch_get_task.batch_get_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.batch_get_task_request.BatchGetTaskRequest = {}  # type: ignore[typeddict-item]
        input_["identifiers"] = identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_worker(
        self,
        identifiers: "aws_sdk_deadline.types.batch_get_worker_identifiers.BatchGetWorkerIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.batch_get_worker_response.BatchGetWorkerResponse":
        """<p>Retrieves multiple workers in a single request. This is a batch version of the <code>GetWorker</code> API.</p> <p>The result of getting each worker is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of worker identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Examples:
            Get multiple workers in a single request

            >>> client.batch_get_worker(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'fleetId': 'fleet-1234567890abcdef1234567890abcdef', 'workerId': 'worker-1234567890abcdef1234567890abcdef'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'fleetId': 'fleet-1234567890abcdef1234567890abcdef', 'workerId': 'worker-234567890abcdef1234567890abcdef1'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.batch_get_worker_request.BatchGetWorkerRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.batch_get_worker_response.BatchGetWorkerResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.batch_get_worker

            output, http_response = (
                aws_sdk_deadline._operations.deadline.batch_get_worker.batch_get_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.batch_get_worker_request.BatchGetWorkerRequest = {}  # type: ignore[typeddict-item]
        input_["identifiers"] = identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_job(
        self,
        jobs: "aws_sdk_deadline.types.batch_update_job_items.BatchUpdateJobItems",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_deadline.types.batch_update_job_response.BatchUpdateJobResponse":
        """<p>Updates multiple jobs in a single request. This is a batch version of the <code>UpdateJob</code> API.</p> <p>The result of updating each job is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p> <p>When you change the status of a job to <code>ARCHIVED</code>, the job can't be scheduled or archived.</p> <important> <p>An archived job and its steps and tasks are deleted after 120 days. The job can't be recovered.</p> </important>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            jobs: <p>The list of jobs to update. You can specify up to 100 jobs per request.</p>

        Examples:
            Update multiple jobs in a single request

            >>> client.batch_update_job(jobs=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'targetTaskRunStatus': 'FAILED'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-234567890abcdef1234567890abcdef1', 'targetTaskRunStatus': 'FAILED'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.batch_update_job_request.BatchUpdateJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.batch_update_job_response.BatchUpdateJobResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.batch_update_job

            output, http_response = (
                aws_sdk_deadline._operations.deadline.batch_update_job.batch_update_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.batch_update_job_request.BatchUpdateJobRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["jobs"] = jobs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_task(
        self,
        tasks: "aws_sdk_deadline.types.batch_update_task_items.BatchUpdateTaskItems",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_deadline.types.batch_update_task_response.BatchUpdateTaskResponse":
        """<p>Updates multiple tasks in a single request. This is a batch version of the <code>UpdateTask</code> API.</p> <p>The result of updating each task is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            tasks: <p>The list of tasks to update. You can specify up to 100 tasks per request.</p>

        Examples:
            Update multiple tasks in a single request

            >>> client.batch_update_task(tasks=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-1234567890abcdef1234567890abcdef', 'taskId': 'task-1234567890abcdef1234567890abcdef-0', 'targetRunStatus': 'FAILED'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-1234567890abcdef1234567890abcdef', 'taskId': 'task-1234567890abcdef1234567890abcdef-1', 'targetRunStatus': 'FAILED'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.batch_update_task_request.BatchUpdateTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.batch_update_task_response.BatchUpdateTaskResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.batch_update_task

            output, http_response = (
                aws_sdk_deadline._operations.deadline.batch_update_task.batch_update_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.batch_update_task_request.BatchUpdateTaskRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["tasks"] = tasks

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_queue_fleet_association(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        queue_id: "aws_sdk_deadline.types.queue_id.QueueId",
        fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.create_queue_fleet_association_response.CreateQueueFleetAssociationResponse":
        """<p>Creates an association between a queue and a fleet.</p>

        Args:
            farm_id: <p>The ID of the farm that the queue and fleet belong to.</p>
            queue_id: <p>The queue ID.</p>
            fleet_id: <p>The fleet ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.create_queue_fleet_association_request.CreateQueueFleetAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.create_queue_fleet_association_response.CreateQueueFleetAssociationResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_queue_fleet_association

            output, http_response = (
                aws_sdk_deadline._operations.deadline.create_queue_fleet_association.create_queue_fleet_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_queue_fleet_association_request.CreateQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["queue_id"] = queue_id
        input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_queue_limit_association(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        queue_id: "aws_sdk_deadline.types.queue_id.QueueId",
        limit_id: "aws_sdk_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.create_queue_limit_association_response.CreateQueueLimitAssociationResponse":
        """<p>Associates a limit with a particular queue. After the limit is associated, all workers for jobs that specify the limit associated with the queue are subject to the limit. You can't associate two limits with the same <code>amountRequirementName</code> to the same queue.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the queue and limit to associate.</p>
            queue_id: <p>The unique identifier of the queue to associate with the limit.</p>
            limit_id: <p>The unique identifier of the limit to associate with the queue.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.create_queue_limit_association_request.CreateQueueLimitAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.create_queue_limit_association_response.CreateQueueLimitAssociationResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_queue_limit_association

            output, http_response = (
                aws_sdk_deadline._operations.deadline.create_queue_limit_association.create_queue_limit_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_queue_limit_association_request.CreateQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["queue_id"] = queue_id
        input_["limit_id"] = limit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_queue_fleet_association(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        queue_id: "aws_sdk_deadline.types.queue_id.QueueId",
        fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_queue_fleet_association_response.DeleteQueueFleetAssociationResponse":
        """<p>Deletes a queue-fleet association.</p>

        Args:
            farm_id: <p>The farm ID of the farm that holds the queue-fleet association.</p>
            queue_id: <p>The queue ID of the queue-fleet association.</p>
            fleet_id: <p>The fleet ID of the queue-fleet association.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.delete_queue_fleet_association_request.DeleteQueueFleetAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.delete_queue_fleet_association_response.DeleteQueueFleetAssociationResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_queue_fleet_association

            output, http_response = (
                aws_sdk_deadline._operations.deadline.delete_queue_fleet_association.delete_queue_fleet_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_queue_fleet_association_request.DeleteQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["queue_id"] = queue_id
        input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_queue_limit_association(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        queue_id: "aws_sdk_deadline.types.queue_id.QueueId",
        limit_id: "aws_sdk_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_queue_limit_association_response.DeleteQueueLimitAssociationResponse":
        """<p>Removes the association between a queue and a limit. You must use the <code>UpdateQueueLimitAssociation</code> operation to set the status to <code>STOP_LIMIT_USAGE_AND_COMPLETE_TASKS</code> or <code>STOP_LIMIT_USAGE_AND_CANCEL_TASKS</code>. The status does not change immediately. Use the <code>GetQueueLimitAssociation</code> operation to see if the status changed to <code>STOPPED</code> before deleting the association.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the queue and limit to disassociate.</p>
            queue_id: <p>The unique identifier of the queue to disassociate.</p>
            limit_id: <p>The unique identifier of the limit to disassociate.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.delete_queue_limit_association_request.DeleteQueueLimitAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.delete_queue_limit_association_response.DeleteQueueLimitAssociationResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_queue_limit_association

            output, http_response = (
                aws_sdk_deadline._operations.deadline.delete_queue_limit_association.delete_queue_limit_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_queue_limit_association_request.DeleteQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["queue_id"] = queue_id
        input_["limit_id"] = limit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_queue_fleet_association(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        queue_id: "aws_sdk_deadline.types.queue_id.QueueId",
        fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_queue_fleet_association_response.GetQueueFleetAssociationResponse":
        """<p>Gets a queue-fleet association.</p>

        Args:
            farm_id: <p>The farm ID of the farm that contains the queue-fleet association.</p>
            queue_id: <p>The queue ID for the queue-fleet association.</p>
            fleet_id: <p>The fleet ID for the queue-fleet association.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.get_queue_fleet_association_request.GetQueueFleetAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.get_queue_fleet_association_response.GetQueueFleetAssociationResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_queue_fleet_association

            output, http_response = (
                aws_sdk_deadline._operations.deadline.get_queue_fleet_association.get_queue_fleet_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_queue_fleet_association_request.GetQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["queue_id"] = queue_id
        input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_queue_limit_association(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        queue_id: "aws_sdk_deadline.types.queue_id.QueueId",
        limit_id: "aws_sdk_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_queue_limit_association_response.GetQueueLimitAssociationResponse":
        """<p>Gets information about a specific association between a queue and a limit.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the associated queue and limit.</p>
            queue_id: <p>The unique identifier of the queue associated with the limit.</p>
            limit_id: <p>The unique identifier of the limit associated with the queue.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.get_queue_limit_association_request.GetQueueLimitAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.get_queue_limit_association_response.GetQueueLimitAssociationResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_queue_limit_association

            output, http_response = (
                aws_sdk_deadline._operations.deadline.get_queue_limit_association.get_queue_limit_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_queue_limit_association_request.GetQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["queue_id"] = queue_id
        input_["limit_id"] = limit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_sessions_statistics_aggregation(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        aggregation_id: "aws_sdk_deadline.types.aggregation_id.AggregationId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.get_sessions_statistics_aggregation_response.GetSessionsStatisticsAggregationResponse":
        """<p>Gets a set of statistics for queues or farms. Before you can call the <code>GetSessionStatisticsAggregation</code> operation, you must first call the <code>StartSessionsStatisticsAggregation</code> operation. Statistics are available for 1 hour after you call the <code>StartSessionsStatisticsAggregation</code> operation.</p>

        Args:
            farm_id: <p>The identifier of the farm to include in the statistics. This should be the same as the farm ID used in the call to the <code>StartSessionsStatisticsAggregation</code> operation.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            aggregation_id: <p>The identifier returned by the <code>StartSessionsStatisticsAggregation</code> operation that identifies the aggregated statistics.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.get_sessions_statistics_aggregation_request.GetSessionsStatisticsAggregationRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.get_sessions_statistics_aggregation_response.GetSessionsStatisticsAggregationResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_sessions_statistics_aggregation

            output, http_response = (
                aws_sdk_deadline._operations.deadline.get_sessions_statistics_aggregation.get_sessions_statistics_aggregation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_sessions_statistics_aggregation_request.GetSessionsStatisticsAggregationRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["aggregation_id"] = aggregation_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_sessions_statistics_aggregation(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        aggregation_id: "aws_sdk_deadline.types.aggregation_id.AggregationId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[aws_sdk_deadline.types.statistics.Statistics]":
        _token = next_token
        while True:
            _response = self.get_sessions_statistics_aggregation(
                farm_id,
                aggregation_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("statistics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_available_metered_products(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_available_metered_products_response.ListAvailableMeteredProductsResponse":
        """<p>A list of the available metered products.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_available_metered_products_request.ListAvailableMeteredProductsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_available_metered_products_response.ListAvailableMeteredProductsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_available_metered_products

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_available_metered_products.list_available_metered_products(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_available_metered_products_request.ListAvailableMeteredProductsRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_available_metered_products(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> (
        "Iterator[aws_sdk_deadline.types.metered_product_summary.MeteredProductSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_available_metered_products(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("metered_products",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_queue_fleet_associations(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
        queue_id: Optional["aws_sdk_deadline.types.queue_id.QueueId"] = None,
        fleet_id: Optional["aws_sdk_deadline.types.fleet_id.FleetId"] = None,
    ) -> "aws_sdk_deadline.types.list_queue_fleet_associations_response.ListQueueFleetAssociationsResponse":
        """<p>Lists queue-fleet associations.</p>

        Args:
            farm_id: <p>The farm ID for the queue-fleet association list.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            queue_id: <p>The queue ID for the queue-fleet association list.</p>
            fleet_id: <p>The fleet ID for the queue-fleet association list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_queue_fleet_associations_request.ListQueueFleetAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_queue_fleet_associations_response.ListQueueFleetAssociationsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_queue_fleet_associations

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_queue_fleet_associations.list_queue_fleet_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_queue_fleet_associations_request.ListQueueFleetAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if queue_id is not None:
            input_["queue_id"] = queue_id
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_queue_fleet_associations(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
        queue_id: Optional["aws_sdk_deadline.types.queue_id.QueueId"] = None,
        fleet_id: Optional["aws_sdk_deadline.types.fleet_id.FleetId"] = None,
    ) -> "Iterator[aws_sdk_deadline.types.queue_fleet_association_summary.QueueFleetAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_queue_fleet_associations(
                farm_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                queue_id=queue_id,
                fleet_id=fleet_id,
            )
            _page = _resolve_path(_response, ("queue_fleet_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_queue_limit_associations(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
        queue_id: Optional["aws_sdk_deadline.types.queue_id.QueueId"] = None,
        limit_id: Optional["aws_sdk_deadline.types.limit_id.LimitId"] = None,
    ) -> "aws_sdk_deadline.types.list_queue_limit_associations_response.ListQueueLimitAssociationsResponse":
        """<p>Gets a list of the associations between queues and limits defined in a farm.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limits and associations.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of associations to return in each page of results.</p>
            queue_id: <p>Specifies that the operation should return only the queue limit associations for the specified queue. If you specify both the <code>queueId</code> and the <code>limitId</code>, only the specified limit is returned if it exists.</p>
            limit_id: <p>Specifies that the operation should return only the queue limit associations for the specified limit. If you specify both the <code>queueId</code> and the <code>limitId</code>, only the specified limit is returned if it exists.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_queue_limit_associations_request.ListQueueLimitAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_queue_limit_associations_response.ListQueueLimitAssociationsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_queue_limit_associations

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_queue_limit_associations.list_queue_limit_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_queue_limit_associations_request.ListQueueLimitAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if queue_id is not None:
            input_["queue_id"] = queue_id
        if limit_id is not None:
            input_["limit_id"] = limit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_queue_limit_associations(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
        queue_id: Optional["aws_sdk_deadline.types.queue_id.QueueId"] = None,
        limit_id: Optional["aws_sdk_deadline.types.limit_id.LimitId"] = None,
    ) -> "Iterator[aws_sdk_deadline.types.queue_limit_association_summary.QueueLimitAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_queue_limit_associations(
                farm_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                queue_id=queue_id,
                limit_id=limit_id,
            )
            _page = _resolve_path(_response, ("queue_limit_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_deadline.types.string.String",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for a resource.</p>

        Args:
            resource_arn: <p>The resource ARN to list tags for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_tags_for_resource

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_jobs(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        item_offset: "aws_sdk_deadline.types.integer.Integer",
        queue_ids: "aws_sdk_deadline.types.queue_ids.QueueIds",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        filter_expressions: Optional[
            "aws_sdk_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
        ] = None,
        sort_expressions: Optional[
            "aws_sdk_deadline.types.search_sort_expressions.SearchSortExpressions"
        ] = None,
        page_size: Optional["aws_sdk_deadline.types.integer.Integer"] = None,
    ) -> "aws_sdk_deadline.types.search_jobs_response.SearchJobsResponse":
        """<p>Searches for jobs.</p>

        Args:
            farm_id: <p>The farm ID of the job.</p>
            filter_expressions: <p>The search terms for a resource.</p>
            sort_expressions: <p>The search terms for a resource.</p>
            item_offset: <p>The offset for the search results.</p>
            page_size: <p>Specifies the number of results to return.</p>
            queue_ids: <p>The queue ID to use in the job search.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.search_jobs_request.SearchJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.search_jobs_response.SearchJobsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.search_jobs

            output, http_response = (
                aws_sdk_deadline._operations.deadline.search_jobs.search_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.search_jobs_request.SearchJobsRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if filter_expressions is not None:
            input_["filter_expressions"] = filter_expressions
        if sort_expressions is not None:
            input_["sort_expressions"] = sort_expressions
        input_["item_offset"] = item_offset
        if page_size is not None:
            input_["page_size"] = page_size
        input_["queue_ids"] = queue_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_steps(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        item_offset: "aws_sdk_deadline.types.integer.Integer",
        queue_ids: "aws_sdk_deadline.types.queue_ids.QueueIds",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        filter_expressions: Optional[
            "aws_sdk_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
        ] = None,
        sort_expressions: Optional[
            "aws_sdk_deadline.types.search_sort_expressions.SearchSortExpressions"
        ] = None,
        page_size: Optional["aws_sdk_deadline.types.integer.Integer"] = None,
        job_id: Optional["aws_sdk_deadline.types.job_id.JobId"] = None,
    ) -> "aws_sdk_deadline.types.search_steps_response.SearchStepsResponse":
        """<p>Searches for steps.</p>

        Args:
            farm_id: <p>The farm ID to use for the step search.</p>
            filter_expressions: <p>The search terms for a resource.</p>
            sort_expressions: <p>The search terms for a resource.</p>
            item_offset: <p>The offset for the search results.</p>
            page_size: <p>Specifies the number of results to return.</p>
            queue_ids: <p>The queue IDs in the step search.</p>
            job_id: <p>The job ID to use in the step search.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.search_steps_request.SearchStepsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.search_steps_response.SearchStepsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.search_steps

            output, http_response = (
                aws_sdk_deadline._operations.deadline.search_steps.search_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.search_steps_request.SearchStepsRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if filter_expressions is not None:
            input_["filter_expressions"] = filter_expressions
        if sort_expressions is not None:
            input_["sort_expressions"] = sort_expressions
        input_["item_offset"] = item_offset
        if page_size is not None:
            input_["page_size"] = page_size
        input_["queue_ids"] = queue_ids
        if job_id is not None:
            input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_tasks(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        item_offset: "aws_sdk_deadline.types.integer.Integer",
        queue_ids: "aws_sdk_deadline.types.queue_ids.QueueIds",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        filter_expressions: Optional[
            "aws_sdk_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
        ] = None,
        sort_expressions: Optional[
            "aws_sdk_deadline.types.search_sort_expressions.SearchSortExpressions"
        ] = None,
        page_size: Optional["aws_sdk_deadline.types.integer.Integer"] = None,
        job_id: Optional["aws_sdk_deadline.types.job_id.JobId"] = None,
    ) -> "aws_sdk_deadline.types.search_tasks_response.SearchTasksResponse":
        """<p>Searches for tasks.</p>

        Args:
            farm_id: <p>The farm ID of the task.</p>
            filter_expressions: <p>The search terms for a resource.</p>
            sort_expressions: <p>The search terms for a resource.</p>
            item_offset: <p>The offset for the search results.</p>
            page_size: <p>Specifies the number of results to return.</p>
            queue_ids: <p>The queue IDs to include in the search.</p>
            job_id: <p>The job ID for the task search.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.search_tasks_request.SearchTasksRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.search_tasks_response.SearchTasksResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.search_tasks

            output, http_response = (
                aws_sdk_deadline._operations.deadline.search_tasks.search_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.search_tasks_request.SearchTasksRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if filter_expressions is not None:
            input_["filter_expressions"] = filter_expressions
        if sort_expressions is not None:
            input_["sort_expressions"] = sort_expressions
        input_["item_offset"] = item_offset
        if page_size is not None:
            input_["page_size"] = page_size
        input_["queue_ids"] = queue_ids
        if job_id is not None:
            input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_workers(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        item_offset: "aws_sdk_deadline.types.integer.Integer",
        fleet_ids: "aws_sdk_deadline.types.fleet_ids.FleetIds",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        filter_expressions: Optional[
            "aws_sdk_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
        ] = None,
        sort_expressions: Optional[
            "aws_sdk_deadline.types.search_sort_expressions.SearchSortExpressions"
        ] = None,
        page_size: Optional["aws_sdk_deadline.types.integer.Integer"] = None,
    ) -> "aws_sdk_deadline.types.search_workers_response.SearchWorkersResponse":
        """<p>Searches for workers.</p>

        Args:
            farm_id: <p>The farm ID in the workers search.</p>
            filter_expressions: <p>The search terms for a resource.</p>
            sort_expressions: <p>The search terms for a resource.</p>
            item_offset: <p>The offset for the search results.</p>
            page_size: <p>Specifies the number of results to return.</p>
            fleet_ids: <p>The fleet ID of the workers to search for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.search_workers_request.SearchWorkersRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.search_workers_response.SearchWorkersResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.search_workers

            output, http_response = (
                aws_sdk_deadline._operations.deadline.search_workers.search_workers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.search_workers_request.SearchWorkersRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        if filter_expressions is not None:
            input_["filter_expressions"] = filter_expressions
        if sort_expressions is not None:
            input_["sort_expressions"] = sort_expressions
        input_["item_offset"] = item_offset
        if page_size is not None:
            input_["page_size"] = page_size
        input_["fleet_ids"] = fleet_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_sessions_statistics_aggregation(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        resource_ids: "aws_sdk_deadline.types.sessions_statistics_resources.SessionsStatisticsResources",
        start_time: "aws_sdk_deadline.types.timestamp.Timestamp",
        end_time: "aws_sdk_deadline.types.timestamp.Timestamp",
        group_by: "aws_sdk_deadline.types.usage_group_by.UsageGroupBy",
        statistics: "aws_sdk_deadline.types.usage_statistics.UsageStatistics",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        timezone: Optional["aws_sdk_deadline.types.timezone.Timezone"] = None,
        period: Optional["aws_sdk_deadline.types.period.Period"] = None,
    ) -> "aws_sdk_deadline.types.start_sessions_statistics_aggregation_response.StartSessionsStatisticsAggregationResponse":
        r"""<p>Starts an asynchronous request for getting aggregated statistics about queues and farms. Get the statistics using the <code>GetSessionsStatisticsAggregation</code> operation. You can only have one running aggregation for your Deadline Cloud farm. Call the <code>GetSessionsStatisticsAggregation</code> operation and check the <code>status</code> field to see if an aggregation is running. Statistics are available for 1 hour after you call the <code>StartSessionsStatisticsAggregation</code> operation.</p>

        Args:
            farm_id: <p>The identifier of the farm that contains queues or fleets to return statistics for.</p>
            resource_ids: <p>A list of fleet IDs or queue IDs to gather statistics for.</p>
            start_time: <p>The Linux timestamp of the date and time that the statistics start.</p>
            end_time: <p>The Linux timestamp of the date and time that the statistics end.</p>
            timezone: <p>The timezone to use for the statistics. Use UTC notation such as \"UTC+8.\"</p>
            period: <p>The period to aggregate the statistics.</p>
            group_by: <p>The field to use to group the statistics.</p>
            statistics: <p>One to four statistics to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.start_sessions_statistics_aggregation_request.StartSessionsStatisticsAggregationRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.start_sessions_statistics_aggregation_response.StartSessionsStatisticsAggregationResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.start_sessions_statistics_aggregation

            output, http_response = (
                aws_sdk_deadline._operations.deadline.start_sessions_statistics_aggregation.start_sessions_statistics_aggregation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.start_sessions_statistics_aggregation_request.StartSessionsStatisticsAggregationRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["resource_ids"] = resource_ids
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        if timezone is not None:
            input_["timezone"] = timezone
        if period is not None:
            input_["period"] = period
        input_["group_by"] = group_by
        input_["statistics"] = statistics

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_deadline.types.string.String",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        tags: Optional["aws_sdk_deadline.types.tags.Tags"] = None,
    ) -> "aws_sdk_deadline.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource using the resource's ARN and desired tags.</p>

        Args:
            resource_arn: <p>The ARN of the resource to apply tags to.</p>
            tags: <p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.tag_resource

            output, http_response = (
                aws_sdk_deadline._operations.deadline.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_deadline.types.string.String",
        tag_keys: "aws_sdk_deadline.types.string_list.StringList",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from a resource using the resource's ARN and tag to remove.</p>

        Args:
            resource_arn: <p>The ARN of the resource to remove the tag from.</p>
            tag_keys: <p>They keys of the tag.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.untag_resource

            output, http_response = (
                aws_sdk_deadline._operations.deadline.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_queue_fleet_association(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        queue_id: "aws_sdk_deadline.types.queue_id.QueueId",
        fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId",
        status: "aws_sdk_deadline.types.update_queue_fleet_association_status.UpdateQueueFleetAssociationStatus",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.update_queue_fleet_association_response.UpdateQueueFleetAssociationResponse":
        """<p>Updates a queue-fleet association.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            queue_id: <p>The queue ID to update.</p>
            fleet_id: <p>The fleet ID to update.</p>
            status: <p>The status to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.update_queue_fleet_association_request.UpdateQueueFleetAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.update_queue_fleet_association_response.UpdateQueueFleetAssociationResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_queue_fleet_association

            output, http_response = (
                aws_sdk_deadline._operations.deadline.update_queue_fleet_association.update_queue_fleet_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_queue_fleet_association_request.UpdateQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["queue_id"] = queue_id
        input_["fleet_id"] = fleet_id
        input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_queue_limit_association(
        self,
        farm_id: "aws_sdk_deadline.types.farm_id.FarmId",
        queue_id: "aws_sdk_deadline.types.queue_id.QueueId",
        limit_id: "aws_sdk_deadline.types.limit_id.LimitId",
        status: "aws_sdk_deadline.types.update_queue_limit_association_status.UpdateQueueLimitAssociationStatus",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.update_queue_limit_association_response.UpdateQueueLimitAssociationResponse":
        """<p>Updates the status of the queue. If you set the status to one of the <code>STOP_LIMIT_USAGE*</code> values, there will be a delay before the status transitions to the <code>STOPPED</code> state. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the associated queues and limits.</p>
            queue_id: <p>The unique identifier of the queue associated to the limit.</p>
            limit_id: <p>The unique identifier of the limit associated to the queue.</p>
            status: <p>Sets the status of the limit. You can mark the limit active, or you can stop usage of the limit and either complete existing tasks or cancel any existing tasks immediately. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.update_queue_limit_association_request.UpdateQueueLimitAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.update_queue_limit_association_response.UpdateQueueLimitAssociationResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_queue_limit_association

            output, http_response = (
                aws_sdk_deadline._operations.deadline.update_queue_limit_association.update_queue_limit_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_queue_limit_association_request.UpdateQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["farm_id"] = farm_id
        input_["queue_id"] = queue_id
        input_["limit_id"] = limit_id
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
