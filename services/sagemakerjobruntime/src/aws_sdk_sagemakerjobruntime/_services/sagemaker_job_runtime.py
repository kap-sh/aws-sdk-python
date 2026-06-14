"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#AgenticRFTRuntimeService``."""

import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_sagemakerjobruntime._auth._signers
import aws_sdk_sagemakerjobruntime._auth._sigv4
from aws_sdk_sagemakerjobruntime._auth._identity import Credentials
from aws_sdk_sagemakerjobruntime._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_sagemakerjobruntime._auth._zapros_handler import AuthMiddleware
from aws_sdk_sagemakerjobruntime._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_sagemakerjobruntime.types.complete_rollout_request
    import aws_sdk_sagemakerjobruntime.types.complete_rollout_response
    import aws_sdk_sagemakerjobruntime.types.completion_status
    import aws_sdk_sagemakerjobruntime.types.double_list
    import aws_sdk_sagemakerjobruntime.types.inference_request_body
    import aws_sdk_sagemakerjobruntime.types.job_arn
    import aws_sdk_sagemakerjobruntime.types.sample_request
    import aws_sdk_sagemakerjobruntime.types.sample_response
    import aws_sdk_sagemakerjobruntime.types.sample_with_response_stream_request
    import aws_sdk_sagemakerjobruntime.types.sample_with_response_stream_response
    import aws_sdk_sagemakerjobruntime.types.trajectory_id
    import aws_sdk_sagemakerjobruntime.types.update_reward_request
    import aws_sdk_sagemakerjobruntime.types.update_reward_response


class SagemakerJobRuntimeClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class SagemakerJobRuntimeClient:
    """A client for the ``SagemakerJobRuntime`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self.config = SagemakerJobRuntimeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[SagemakerJobRuntimeClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SagemakerJobRuntimeClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def complete_rollout(
        self,
        job_arn: "aws_sdk_sagemakerjobruntime.types.job_arn.JobArn",
        trajectory_id: "aws_sdk_sagemakerjobruntime.types.trajectory_id.TrajectoryId",
        *,
        config_overrides: Optional[SagemakerJobRuntimeClientConfig] = None,
        status: Optional[
            "aws_sdk_sagemakerjobruntime.types.completion_status.CompletionStatus"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_sagemakerjobruntime.types.complete_rollout_response.CompleteRolloutResponse":
        """Marks a rollout as complete, indicating that no further turns will be appended to the trajectory. After calling this operation, the trajectory is sealed and eligible for reward submission via the UpdateReward operation.

        Args:
            job_arn: The job ARN.
            trajectory_id: The trajectory ID to mark as complete.
            status: The target status for the trajectory. Defaults to READY if not specified. Set to FAILED if the rollout encountered an error and the trajectory should not be used for processing.
            client_token: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        Examples:
            Invoke CompleteRollout
            Marks a rollout as complete so the trajectory is sealed and eligible for reward submission.

            >>> client.complete_rollout(job_arn='arn:aws:sagemaker:us-east-1:123456789012:job/AgentRFT/my-training-job', trajectory_id='trajectory-001', status='ready')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemakerjobruntime.types.complete_rollout_request.CompleteRolloutRequest]",
        ) -> OperationResponse[
            "aws_sdk_sagemakerjobruntime.types.complete_rollout_response.CompleteRolloutResponse"
        ]:
            import aws_sdk_sagemakerjobruntime._operations.agentic_rft_runtime_service.complete_rollout

            output, http_response = (
                aws_sdk_sagemakerjobruntime._operations.agentic_rft_runtime_service.complete_rollout.complete_rollout(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemakerjobruntime.types.complete_rollout_request.CompleteRolloutRequest = {}  # type: ignore[typeddict-item]
        input_["job_arn"] = job_arn
        input_["trajectory_id"] = trajectory_id
        if status is not None:
            input_["status"] = status
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def sample(
        self,
        job_arn: "aws_sdk_sagemakerjobruntime.types.job_arn.JobArn",
        trajectory_id: "aws_sdk_sagemakerjobruntime.types.trajectory_id.TrajectoryId",
        body: "aws_sdk_sagemakerjobruntime.types.inference_request_body.InferenceRequestBody",
        *,
        config_overrides: Optional[SagemakerJobRuntimeClientConfig] = None,
    ) -> "aws_sdk_sagemakerjobruntime.types.sample_response.SampleResponse":
        """Sends an inference request to the model during a job execution. The request and response bodies are forwarded to and from the model without modification. Each turn (prompt and response) is captured for later use.

        Args:
            job_arn: The job ARN that identifies which model session to route the inference request to.
            trajectory_id: The trajectory ID for grouping turns into a single rollout. Each turn (prompt and response) is captured for later use.
            body: The raw inference request body in OpenAI-compatible JSON format.

        Examples:
            Invoke Sample
            Sends an inference request to the model and receives the response.

            >>> client.sample(job_arn='arn:aws:sagemaker:us-east-1:123456789012:job/AgentRFT/my-training-job', trajectory_id='trajectory-001', body='eyJtb2RlbCI6Im15LW1vZGVsIiwibWVzc2FnZXMiOlt7InJvbGUiOiJ1c2VyIiwiY29udGVudCI6IkhlbGxvIn1dfQ==')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemakerjobruntime.types.sample_request.SampleRequest]",
        ) -> OperationResponse[
            "aws_sdk_sagemakerjobruntime.types.sample_response.SampleResponse"
        ]:
            import aws_sdk_sagemakerjobruntime._operations.agentic_rft_runtime_service.sample

            output, http_response = (
                aws_sdk_sagemakerjobruntime._operations.agentic_rft_runtime_service.sample.sample(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemakerjobruntime.types.sample_request.SampleRequest = {}  # type: ignore[typeddict-item]
        input_["job_arn"] = job_arn
        input_["trajectory_id"] = trajectory_id
        input_["body"] = body

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    @contextmanager
    def sample_with_response_stream(
        self,
        job_arn: "aws_sdk_sagemakerjobruntime.types.job_arn.JobArn",
        trajectory_id: "aws_sdk_sagemakerjobruntime.types.trajectory_id.TrajectoryId",
        body: "aws_sdk_sagemakerjobruntime.types.inference_request_body.InferenceRequestBody",
        *,
        config_overrides: Optional[SagemakerJobRuntimeClientConfig] = None,
    ) -> "Generator[aws_sdk_sagemakerjobruntime.types.sample_with_response_stream_response.SampleWithResponseStreamResponse]":
        """Sends a streaming inference request to the model during a job execution. Returns the response as a stream of payload chunks. Each turn is captured for later use.

        Args:
            job_arn: The job ARN that identifies which model session to route the inference request to.
            trajectory_id: The trajectory ID for grouping turns into a single rollout. Each turn is captured for later use.
            body: The raw inference request body in OpenAI-compatible JSON format.

        Examples:
            Invoke SampleWithResponseStream
            Sends a streaming inference request and receives the response as a stream of payload chunks.

            >>> client.sample_with_response_stream(job_arn='arn:aws:sagemaker:us-east-1:123456789012:job/AgentRFT/my-training-job', trajectory_id='trajectory-001', body='eyJtb2RlbCI6Im15LW1vZGVsIiwibWVzc2FnZXMiOlt7InJvbGUiOiJ1c2VyIiwiY29udGVudCI6IkhlbGxvIn1dfQ==')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemakerjobruntime.types.sample_with_response_stream_request.SampleWithResponseStreamRequest]",
        ) -> OperationResponse[
            "aws_sdk_sagemakerjobruntime.types.sample_with_response_stream_response.SampleWithResponseStreamResponse"
        ]:
            import aws_sdk_sagemakerjobruntime._operations.agentic_rft_runtime_service.sample_with_response_stream

            output, http_response = (
                aws_sdk_sagemakerjobruntime._operations.agentic_rft_runtime_service.sample_with_response_stream.sample_with_response_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemakerjobruntime.types.sample_with_response_stream_request.SampleWithResponseStreamRequest = {}  # type: ignore[typeddict-item]
        input_["job_arn"] = job_arn
        input_["trajectory_id"] = trajectory_id
        input_["body"] = body

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output

    def update_reward(
        self,
        job_arn: "aws_sdk_sagemakerjobruntime.types.job_arn.JobArn",
        trajectory_id: "aws_sdk_sagemakerjobruntime.types.trajectory_id.TrajectoryId",
        rewards: "aws_sdk_sagemakerjobruntime.types.double_list.DoubleList",
        *,
        config_overrides: Optional[SagemakerJobRuntimeClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "aws_sdk_sagemakerjobruntime.types.update_reward_response.UpdateRewardResponse"
    ):
        """Updates the reward values for a trajectory and transitions it to reward-received status, signaling that it is eligible for processing. Call this operation after CompleteRollout to provide the computed reward scores.

        Args:
            job_arn: The job ARN.
            trajectory_id: The trajectory ID to update with reward values.
            rewards: The list of reward values to assign to this trajectory. Provide one reward value per turn in the trajectory.
            client_token: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        Examples:
            Invoke UpdateReward
            Updates the reward values for a completed trajectory.

            >>> client.update_reward(job_arn='arn:aws:sagemaker:us-east-1:123456789012:job/AgentRFT/my-training-job', trajectory_id='trajectory-001', rewards=[0.85, 0.92, 0.78])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemakerjobruntime.types.update_reward_request.UpdateRewardRequest]",
        ) -> OperationResponse[
            "aws_sdk_sagemakerjobruntime.types.update_reward_response.UpdateRewardResponse"
        ]:
            import aws_sdk_sagemakerjobruntime._operations.agentic_rft_runtime_service.update_reward

            output, http_response = (
                aws_sdk_sagemakerjobruntime._operations.agentic_rft_runtime_service.update_reward.update_reward(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemakerjobruntime.types.update_reward_request.UpdateRewardRequest = {}  # type: ignore[typeddict-item]
        input_["job_arn"] = job_arn
        input_["trajectory_id"] = trajectory_id
        input_["rewards"] = rewards
        if client_token is not None:
            input_["client_token"] = client_token

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
