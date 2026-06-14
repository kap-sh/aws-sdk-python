"""Generated from Smithy shape ``com.amazonaws.securityagent#SecurityAgent``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_securityagent._auth._signers
import aws_sdk_securityagent._auth._sigv4
from aws_sdk_securityagent._auth._identity import Credentials
from aws_sdk_securityagent._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_securityagent._auth._zapros_handler import AuthMiddleware
from aws_sdk_securityagent._pagination import resolve_path as _resolve_path
from aws_sdk_securityagent._resources.security_agent.agent_space_resource import (
    AsyncAgentSpaceResource,
)
from aws_sdk_securityagent._resources.security_agent.application_resource import (
    AsyncApplicationResource,
)
from aws_sdk_securityagent._resources.security_agent.integration_resource import (
    AsyncIntegrationResource,
)
from aws_sdk_securityagent._resources.security_agent.target_domain_resource import (
    AsyncTargetDomainResource,
)
from aws_sdk_securityagent._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.add_artifact_input
    import aws_sdk_securityagent.types.add_artifact_output
    import aws_sdk_securityagent.types.agent_space_id
    import aws_sdk_securityagent.types.application_id
    import aws_sdk_securityagent.types.artifact_id
    import aws_sdk_securityagent.types.artifact_ids
    import aws_sdk_securityagent.types.artifact_summary
    import aws_sdk_securityagent.types.artifact_type
    import aws_sdk_securityagent.types.assets
    import aws_sdk_securityagent.types.batch_delete_code_reviews_input
    import aws_sdk_securityagent.types.batch_delete_code_reviews_output
    import aws_sdk_securityagent.types.batch_delete_pentests_input
    import aws_sdk_securityagent.types.batch_delete_pentests_output
    import aws_sdk_securityagent.types.batch_get_artifact_metadata_input
    import aws_sdk_securityagent.types.batch_get_artifact_metadata_output
    import aws_sdk_securityagent.types.batch_get_code_review_job_tasks_input
    import aws_sdk_securityagent.types.batch_get_code_review_job_tasks_output
    import aws_sdk_securityagent.types.batch_get_code_review_jobs_input
    import aws_sdk_securityagent.types.batch_get_code_review_jobs_output
    import aws_sdk_securityagent.types.batch_get_code_reviews_input
    import aws_sdk_securityagent.types.batch_get_code_reviews_output
    import aws_sdk_securityagent.types.batch_get_findings_input
    import aws_sdk_securityagent.types.batch_get_findings_output
    import aws_sdk_securityagent.types.batch_get_pentest_job_tasks_input
    import aws_sdk_securityagent.types.batch_get_pentest_job_tasks_output
    import aws_sdk_securityagent.types.batch_get_pentest_jobs_input
    import aws_sdk_securityagent.types.batch_get_pentest_jobs_output
    import aws_sdk_securityagent.types.batch_get_pentests_input
    import aws_sdk_securityagent.types.batch_get_pentests_output
    import aws_sdk_securityagent.types.cloud_watch_log
    import aws_sdk_securityagent.types.code_remediation_strategy
    import aws_sdk_securityagent.types.code_review_id_list
    import aws_sdk_securityagent.types.code_review_job_id_list
    import aws_sdk_securityagent.types.code_review_job_summary
    import aws_sdk_securityagent.types.code_review_job_task_summary
    import aws_sdk_securityagent.types.code_review_summary
    import aws_sdk_securityagent.types.confidence_level
    import aws_sdk_securityagent.types.create_code_review_input
    import aws_sdk_securityagent.types.create_code_review_output
    import aws_sdk_securityagent.types.create_membership_request
    import aws_sdk_securityagent.types.create_membership_response
    import aws_sdk_securityagent.types.create_pentest_input
    import aws_sdk_securityagent.types.create_pentest_output
    import aws_sdk_securityagent.types.delete_artifact_input
    import aws_sdk_securityagent.types.delete_artifact_output
    import aws_sdk_securityagent.types.delete_membership_request
    import aws_sdk_securityagent.types.delete_membership_response
    import aws_sdk_securityagent.types.discovered_endpoint
    import aws_sdk_securityagent.types.finding_id_list
    import aws_sdk_securityagent.types.finding_status
    import aws_sdk_securityagent.types.finding_summary
    import aws_sdk_securityagent.types.get_artifact_input
    import aws_sdk_securityagent.types.get_artifact_output
    import aws_sdk_securityagent.types.initiate_provider_registration_input
    import aws_sdk_securityagent.types.initiate_provider_registration_output
    import aws_sdk_securityagent.types.integrated_resource_input_item_list
    import aws_sdk_securityagent.types.integrated_resource_summary
    import aws_sdk_securityagent.types.integration_id
    import aws_sdk_securityagent.types.list_artifacts_input
    import aws_sdk_securityagent.types.list_artifacts_output
    import aws_sdk_securityagent.types.list_code_review_job_tasks_input
    import aws_sdk_securityagent.types.list_code_review_job_tasks_output
    import aws_sdk_securityagent.types.list_code_review_jobs_for_code_review_input
    import aws_sdk_securityagent.types.list_code_review_jobs_for_code_review_output
    import aws_sdk_securityagent.types.list_code_reviews_input
    import aws_sdk_securityagent.types.list_code_reviews_output
    import aws_sdk_securityagent.types.list_discovered_endpoints_input
    import aws_sdk_securityagent.types.list_discovered_endpoints_output
    import aws_sdk_securityagent.types.list_findings_input
    import aws_sdk_securityagent.types.list_findings_output
    import aws_sdk_securityagent.types.list_integrated_resources_input
    import aws_sdk_securityagent.types.list_integrated_resources_output
    import aws_sdk_securityagent.types.list_memberships_request
    import aws_sdk_securityagent.types.list_memberships_response
    import aws_sdk_securityagent.types.list_pentest_job_tasks_input
    import aws_sdk_securityagent.types.list_pentest_job_tasks_output
    import aws_sdk_securityagent.types.list_pentest_jobs_for_pentest_input
    import aws_sdk_securityagent.types.list_pentest_jobs_for_pentest_output
    import aws_sdk_securityagent.types.list_pentests_input
    import aws_sdk_securityagent.types.list_pentests_output
    import aws_sdk_securityagent.types.list_tags_for_resource_input
    import aws_sdk_securityagent.types.list_tags_for_resource_output
    import aws_sdk_securityagent.types.max_results
    import aws_sdk_securityagent.types.membership_config
    import aws_sdk_securityagent.types.membership_id
    import aws_sdk_securityagent.types.membership_summary
    import aws_sdk_securityagent.types.membership_type
    import aws_sdk_securityagent.types.membership_type_filter
    import aws_sdk_securityagent.types.network_traffic_config
    import aws_sdk_securityagent.types.next_token
    import aws_sdk_securityagent.types.pentest_id_list
    import aws_sdk_securityagent.types.pentest_job_id_list
    import aws_sdk_securityagent.types.pentest_job_summary
    import aws_sdk_securityagent.types.pentest_summary
    import aws_sdk_securityagent.types.provider
    import aws_sdk_securityagent.types.resource_arn
    import aws_sdk_securityagent.types.resource_type
    import aws_sdk_securityagent.types.risk_level
    import aws_sdk_securityagent.types.risk_type_list
    import aws_sdk_securityagent.types.service_role
    import aws_sdk_securityagent.types.start_code_remediation_input
    import aws_sdk_securityagent.types.start_code_remediation_output
    import aws_sdk_securityagent.types.start_code_review_job_input
    import aws_sdk_securityagent.types.start_code_review_job_output
    import aws_sdk_securityagent.types.start_pentest_job_input
    import aws_sdk_securityagent.types.start_pentest_job_output
    import aws_sdk_securityagent.types.step_name
    import aws_sdk_securityagent.types.stop_code_review_job_input
    import aws_sdk_securityagent.types.stop_code_review_job_output
    import aws_sdk_securityagent.types.stop_pentest_job_input
    import aws_sdk_securityagent.types.stop_pentest_job_output
    import aws_sdk_securityagent.types.tag_key_list
    import aws_sdk_securityagent.types.tag_map
    import aws_sdk_securityagent.types.tag_resource_input
    import aws_sdk_securityagent.types.tag_resource_output
    import aws_sdk_securityagent.types.target_domain_id
    import aws_sdk_securityagent.types.task_id_list
    import aws_sdk_securityagent.types.task_summary
    import aws_sdk_securityagent.types.untag_resource_input
    import aws_sdk_securityagent.types.untag_resource_output
    import aws_sdk_securityagent.types.update_code_review_input
    import aws_sdk_securityagent.types.update_code_review_output
    import aws_sdk_securityagent.types.update_finding_input
    import aws_sdk_securityagent.types.update_finding_output
    import aws_sdk_securityagent.types.update_integrated_resources_input
    import aws_sdk_securityagent.types.update_integrated_resources_output
    import aws_sdk_securityagent.types.update_pentest_input
    import aws_sdk_securityagent.types.update_pentest_output
    import aws_sdk_securityagent.types.verify_target_domain_input
    import aws_sdk_securityagent.types.verify_target_domain_output
    import aws_sdk_securityagent.types.vpc_config


class AsyncSecurityAgentClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
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


class AsyncSecurityAgentClient:
    """A client for the ``SecurityAgent`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncSecurityAgentClientConfig(
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

        # resources
        self.agent_space_resource = AsyncAgentSpaceResource(self)
        self.application_resource = AsyncApplicationResource(self)
        self.integration_resource = AsyncIntegrationResource(self)
        self.target_domain_resource = AsyncTargetDomainResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSecurityAgentClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSecurityAgentClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def add_artifact(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        artifact_content: bytes,
        artifact_type: "aws_sdk_securityagent.types.artifact_type.ArtifactType",
        file_name: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.add_artifact_output.AddArtifactOutput":
        """<p>Uploads an artifact to an agent space. Artifacts provide additional context for security testing, such as architecture diagrams, API specifications, or configuration files.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to add the artifact to.</p>
            artifact_content: <p>The binary content of the artifact to upload.</p>
            artifact_type: <p>The file type of the artifact. Valid values include TXT, PNG, JPEG, MD, PDF, DOCX, DOC, JSON, and YAML.</p>
            file_name: <p>The file name of the artifact.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.add_artifact_input.AddArtifactInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.add_artifact_output.AddArtifactOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.add_artifact

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.add_artifact.async_add_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.add_artifact_input.AddArtifactInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["artifact_content"] = artifact_content
        input_["artifact_type"] = artifact_type
        input_["file_name"] = file_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_delete_code_reviews(
        self,
        code_review_ids: "aws_sdk_securityagent.types.code_review_id_list.CodeReviewIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_delete_code_reviews_output.BatchDeleteCodeReviewsOutput":
        """<p>Deletes one or more code reviews from an agent space.</p>

        Args:
            code_review_ids: <p>The list of code review identifiers to delete.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the code reviews to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_delete_code_reviews_input.BatchDeleteCodeReviewsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_delete_code_reviews_output.BatchDeleteCodeReviewsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_delete_code_reviews

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_delete_code_reviews.async_batch_delete_code_reviews(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_delete_code_reviews_input.BatchDeleteCodeReviewsInput = {}  # type: ignore[typeddict-item]
        input_["code_review_ids"] = code_review_ids
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_delete_pentests(
        self,
        pentest_ids: "aws_sdk_securityagent.types.pentest_id_list.PentestIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_delete_pentests_output.BatchDeletePentestsOutput":
        """<p>Deletes one or more pentests from an agent space.</p>

        Args:
            pentest_ids: <p>The list of pentest identifiers to delete.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the pentests to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_delete_pentests_input.BatchDeletePentestsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_delete_pentests_output.BatchDeletePentestsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_delete_pentests

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_delete_pentests.async_batch_delete_pentests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_delete_pentests_input.BatchDeletePentestsInput = {}  # type: ignore[typeddict-item]
        input_["pentest_ids"] = pentest_ids
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_artifact_metadata(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        artifact_ids: "aws_sdk_securityagent.types.artifact_ids.ArtifactIds",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_artifact_metadata_output.BatchGetArtifactMetadataOutput":
        """<p>Retrieves metadata for one or more artifacts in an agent space.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the artifacts.</p>
            artifact_ids: <p>The list of artifact identifiers to retrieve metadata for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_get_artifact_metadata_input.BatchGetArtifactMetadataInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_get_artifact_metadata_output.BatchGetArtifactMetadataOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_artifact_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_get_artifact_metadata.async_batch_get_artifact_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_artifact_metadata_input.BatchGetArtifactMetadataInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["artifact_ids"] = artifact_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_code_review_jobs(
        self,
        code_review_job_ids: "aws_sdk_securityagent.types.code_review_job_id_list.CodeReviewJobIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_code_review_jobs_output.BatchGetCodeReviewJobsOutput":
        """<p>Retrieves information about one or more code review jobs in an agent space.</p>

        Args:
            code_review_job_ids: <p>The list of code review job identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the code review jobs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_get_code_review_jobs_input.BatchGetCodeReviewJobsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_get_code_review_jobs_output.BatchGetCodeReviewJobsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_code_review_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_get_code_review_jobs.async_batch_get_code_review_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_code_review_jobs_input.BatchGetCodeReviewJobsInput = {}  # type: ignore[typeddict-item]
        input_["code_review_job_ids"] = code_review_job_ids
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_code_review_job_tasks(
        self,
        agent_space_id: str,
        code_review_job_task_ids: "aws_sdk_securityagent.types.task_id_list.TaskIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_code_review_job_tasks_output.BatchGetCodeReviewJobTasksOutput":
        """<p>Retrieves information about one or more tasks within a code review job.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the tasks.</p>
            code_review_job_task_ids: <p>The list of task identifiers to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_get_code_review_job_tasks_input.BatchGetCodeReviewJobTasksInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_get_code_review_job_tasks_output.BatchGetCodeReviewJobTasksOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_code_review_job_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_get_code_review_job_tasks.async_batch_get_code_review_job_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_code_review_job_tasks_input.BatchGetCodeReviewJobTasksInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["code_review_job_task_ids"] = code_review_job_task_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_code_reviews(
        self,
        code_review_ids: "aws_sdk_securityagent.types.code_review_id_list.CodeReviewIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_code_reviews_output.BatchGetCodeReviewsOutput":
        """<p>Retrieves information about one or more code reviews in an agent space.</p>

        Args:
            code_review_ids: <p>The list of code review identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the code reviews.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_get_code_reviews_input.BatchGetCodeReviewsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_get_code_reviews_output.BatchGetCodeReviewsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_code_reviews

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_get_code_reviews.async_batch_get_code_reviews(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_code_reviews_input.BatchGetCodeReviewsInput = {}  # type: ignore[typeddict-item]
        input_["code_review_ids"] = code_review_ids
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_findings(
        self,
        finding_ids: "aws_sdk_securityagent.types.finding_id_list.FindingIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_findings_output.BatchGetFindingsOutput":
        """<p>Retrieves information about one or more security findings in an agent space.</p>

        Args:
            finding_ids: <p>The list of finding identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the findings.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_get_findings_input.BatchGetFindingsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_get_findings_output.BatchGetFindingsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_findings

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_get_findings.async_batch_get_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_findings_input.BatchGetFindingsInput = {}  # type: ignore[typeddict-item]
        input_["finding_ids"] = finding_ids
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_pentest_jobs(
        self,
        pentest_job_ids: "aws_sdk_securityagent.types.pentest_job_id_list.PentestJobIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_pentest_jobs_output.BatchGetPentestJobsOutput":
        """<p>Retrieves information about one or more pentest jobs in an agent space.</p>

        Args:
            pentest_job_ids: <p>The list of pentest job identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the pentest jobs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_get_pentest_jobs_input.BatchGetPentestJobsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_get_pentest_jobs_output.BatchGetPentestJobsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_pentest_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_get_pentest_jobs.async_batch_get_pentest_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_pentest_jobs_input.BatchGetPentestJobsInput = {}  # type: ignore[typeddict-item]
        input_["pentest_job_ids"] = pentest_job_ids
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_pentest_job_tasks(
        self,
        agent_space_id: str,
        task_ids: "aws_sdk_securityagent.types.task_id_list.TaskIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_pentest_job_tasks_output.BatchGetPentestJobTasksOutput":
        """<p>Retrieves information about one or more tasks within a pentest job.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the tasks.</p>
            task_ids: <p>The list of task identifiers to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_get_pentest_job_tasks_input.BatchGetPentestJobTasksInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_get_pentest_job_tasks_output.BatchGetPentestJobTasksOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_pentest_job_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_get_pentest_job_tasks.async_batch_get_pentest_job_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_pentest_job_tasks_input.BatchGetPentestJobTasksInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["task_ids"] = task_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_pentests(
        self,
        pentest_ids: "aws_sdk_securityagent.types.pentest_id_list.PentestIdList",
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.batch_get_pentests_output.BatchGetPentestsOutput":
        """<p>Retrieves information about one or more pentests in an agent space.</p>

        Args:
            pentest_ids: <p>The list of pentest identifiers to retrieve.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the pentests.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.batch_get_pentests_input.BatchGetPentestsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.batch_get_pentests_output.BatchGetPentestsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.batch_get_pentests

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.batch_get_pentests.async_batch_get_pentests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.batch_get_pentests_input.BatchGetPentestsInput = {}  # type: ignore[typeddict-item]
        input_["pentest_ids"] = pentest_ids
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_code_review(
        self,
        title: str,
        agent_space_id: str,
        assets: "aws_sdk_securityagent.types.assets.Assets",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        service_role: Optional[
            "aws_sdk_securityagent.types.service_role.ServiceRole"
        ] = None,
        log_config: Optional[
            "aws_sdk_securityagent.types.cloud_watch_log.CloudWatchLog"
        ] = None,
        code_remediation_strategy: Optional[
            "aws_sdk_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
        ] = None,
    ) -> "aws_sdk_securityagent.types.create_code_review_output.CreateCodeReviewOutput":
        """<p>Creates a new code review configuration in an agent space. A code review defines the parameters for automated security-focused code analysis.</p>

        Args:
            title: <p>The title of the code review.</p>
            agent_space_id: <p>The unique identifier of the agent space to create the code review in.</p>
            assets: <p>The assets to include in the code review, such as documents and source code.</p>
            service_role: <p>The IAM service role to use for the code review.</p>
            log_config: <p>The CloudWatch Logs configuration for the code review.</p>
            code_remediation_strategy: <p>The code remediation strategy for the code review. Valid values are AUTOMATIC and DISABLED.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.create_code_review_input.CreateCodeReviewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.create_code_review_output.CreateCodeReviewOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.create_code_review

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.create_code_review.async_create_code_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.create_code_review_input.CreateCodeReviewInput = {}  # type: ignore[typeddict-item]
        input_["title"] = title
        input_["agent_space_id"] = agent_space_id
        input_["assets"] = assets
        if service_role is not None:
            input_["service_role"] = service_role
        if log_config is not None:
            input_["log_config"] = log_config
        if code_remediation_strategy is not None:
            input_["code_remediation_strategy"] = code_remediation_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_membership(
        self,
        application_id: "aws_sdk_securityagent.types.application_id.ApplicationId",
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        membership_id: "aws_sdk_securityagent.types.membership_id.MembershipId",
        member_type: "aws_sdk_securityagent.types.membership_type.MembershipType",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        config: Optional[
            "aws_sdk_securityagent.types.membership_config.MembershipConfig"
        ] = None,
    ) -> "aws_sdk_securityagent.types.create_membership_response.CreateMembershipResponse":
        """<p>Creates a new membership, granting a user access to an agent space within an application.</p>

        Args:
            application_id: <p>The unique identifier of the application that contains the agent space.</p>
            agent_space_id: <p>The unique identifier of the agent space to grant access to.</p>
            membership_id: <p>The unique identifier for the membership.</p>
            member_type: <p>The type of member. Currently, only USER is supported.</p>
            config: <p>The configuration for the membership, such as the user role.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.create_membership_request.CreateMembershipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.create_membership_response.CreateMembershipResponse"
        ]:
            import aws_sdk_securityagent._operations.security_agent.create_membership

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.create_membership.async_create_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.create_membership_request.CreateMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["agent_space_id"] = agent_space_id
        input_["membership_id"] = membership_id
        input_["member_type"] = member_type
        if config is not None:
            input_["config"] = config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_pentest(
        self,
        title: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        assets: Optional["aws_sdk_securityagent.types.assets.Assets"] = None,
        exclude_risk_types: Optional[
            "aws_sdk_securityagent.types.risk_type_list.RiskTypeList"
        ] = None,
        service_role: Optional[
            "aws_sdk_securityagent.types.service_role.ServiceRole"
        ] = None,
        log_config: Optional[
            "aws_sdk_securityagent.types.cloud_watch_log.CloudWatchLog"
        ] = None,
        vpc_config: Optional["aws_sdk_securityagent.types.vpc_config.VpcConfig"] = None,
        network_traffic_config: Optional[
            "aws_sdk_securityagent.types.network_traffic_config.NetworkTrafficConfig"
        ] = None,
        code_remediation_strategy: Optional[
            "aws_sdk_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
        ] = None,
    ) -> "aws_sdk_securityagent.types.create_pentest_output.CreatePentestOutput":
        """<p>Creates a new pentest configuration in an agent space. A pentest defines the security test parameters, including target assets, risk type exclusions, and logging configuration.</p>

        Args:
            title: <p>The title of the pentest.</p>
            agent_space_id: <p>The unique identifier of the agent space to create the pentest in.</p>
            assets: <p>The assets to include in the pentest, such as endpoints, actors, documents, and source code.</p>
            exclude_risk_types: <p>The list of risk types to exclude from the pentest.</p>
            service_role: <p>The IAM service role to use for the pentest.</p>
            log_config: <p>The CloudWatch Logs configuration for the pentest.</p>
            vpc_config: <p>The VPC configuration for the pentest.</p>
            network_traffic_config: <p>The network traffic configuration for the pentest, including custom headers and traffic rules.</p>
            code_remediation_strategy: <p>The code remediation strategy for the pentest. Valid values are AUTOMATIC and DISABLED.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.create_pentest_input.CreatePentestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.create_pentest_output.CreatePentestOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.create_pentest

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.create_pentest.async_create_pentest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.create_pentest_input.CreatePentestInput = {}  # type: ignore[typeddict-item]
        input_["title"] = title
        input_["agent_space_id"] = agent_space_id
        if assets is not None:
            input_["assets"] = assets
        if exclude_risk_types is not None:
            input_["exclude_risk_types"] = exclude_risk_types
        if service_role is not None:
            input_["service_role"] = service_role
        if log_config is not None:
            input_["log_config"] = log_config
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if network_traffic_config is not None:
            input_["network_traffic_config"] = network_traffic_config
        if code_remediation_strategy is not None:
            input_["code_remediation_strategy"] = code_remediation_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_artifact(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        artifact_id: "aws_sdk_securityagent.types.artifact_id.ArtifactId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.delete_artifact_output.DeleteArtifactOutput":
        """<p>Deletes an artifact from an agent space.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the artifact.</p>
            artifact_id: <p>The unique identifier of the artifact to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.delete_artifact_input.DeleteArtifactInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.delete_artifact_output.DeleteArtifactOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.delete_artifact

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.delete_artifact.async_delete_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.delete_artifact_input.DeleteArtifactInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["artifact_id"] = artifact_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_membership(
        self,
        application_id: "aws_sdk_securityagent.types.application_id.ApplicationId",
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        membership_id: "aws_sdk_securityagent.types.membership_id.MembershipId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        member_type: Optional[
            "aws_sdk_securityagent.types.membership_type.MembershipType"
        ] = None,
    ) -> "aws_sdk_securityagent.types.delete_membership_response.DeleteMembershipResponse":
        """<p>Deletes a membership, revoking a user's access to an agent space.</p>

        Args:
            application_id: <p>The unique identifier of the application that contains the agent space.</p>
            agent_space_id: <p>The unique identifier of the agent space to revoke access from.</p>
            membership_id: <p>The unique identifier of the membership to delete.</p>
            member_type: <p>The type of member to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.delete_membership_request.DeleteMembershipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.delete_membership_response.DeleteMembershipResponse"
        ]:
            import aws_sdk_securityagent._operations.security_agent.delete_membership

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.delete_membership.async_delete_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.delete_membership_request.DeleteMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["agent_space_id"] = agent_space_id
        input_["membership_id"] = membership_id
        if member_type is not None:
            input_["member_type"] = member_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_artifact(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        artifact_id: "aws_sdk_securityagent.types.artifact_id.ArtifactId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.get_artifact_output.GetArtifactOutput":
        """<p>Retrieves an artifact from an agent space.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space that contains the artifact.</p>
            artifact_id: <p>The unique identifier of the artifact to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.get_artifact_input.GetArtifactInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.get_artifact_output.GetArtifactOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.get_artifact

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.get_artifact.async_get_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.get_artifact_input.GetArtifactInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["artifact_id"] = artifact_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def initiate_provider_registration(
        self,
        provider: "aws_sdk_securityagent.types.provider.Provider",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.initiate_provider_registration_output.InitiateProviderRegistrationOutput":
        """<p>Initiates the OAuth registration flow with a third-party provider. Returns a redirect URL and CSRF state token for completing the authorization.</p>

        Args:
            provider: <p>The provider to initiate registration with. Currently, only GITHUB is supported.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.initiate_provider_registration_input.InitiateProviderRegistrationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.initiate_provider_registration_output.InitiateProviderRegistrationOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.initiate_provider_registration

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.initiate_provider_registration.async_initiate_provider_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.initiate_provider_registration_input.InitiateProviderRegistrationInput = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_artifacts(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityagent.types.list_artifacts_output.ListArtifactsOutput":
        """<p>Returns a paginated list of artifact summaries for the specified agent space.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to list artifacts for.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_artifacts_input.ListArtifactsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_artifacts_output.ListArtifactsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_artifacts

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_artifacts.async_list_artifacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_artifacts_input.ListArtifactsInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_artifacts(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.artifact_summary.ArtifactSummary]":
        _token = next_token
        while True:
            _response = await self.list_artifacts(
                agent_space_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("artifact_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_code_review_jobs_for_code_review(
        self,
        code_review_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_securityagent.types.list_code_review_jobs_for_code_review_output.ListCodeReviewJobsForCodeReviewOutput":
        """<p>Returns a paginated list of code review job summaries for the specified code review configuration.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            code_review_id: <p>The unique identifier of the code review to list jobs for.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_code_review_jobs_for_code_review_input.ListCodeReviewJobsForCodeReviewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_code_review_jobs_for_code_review_output.ListCodeReviewJobsForCodeReviewOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_code_review_jobs_for_code_review

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_code_review_jobs_for_code_review.async_list_code_review_jobs_for_code_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_code_review_jobs_for_code_review_input.ListCodeReviewJobsForCodeReviewInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        input_["code_review_id"] = code_review_id
        input_["agent_space_id"] = agent_space_id
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_code_review_jobs_for_code_review(
        self,
        code_review_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.code_review_job_summary.CodeReviewJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_code_review_jobs_for_code_review(
                code_review_id,
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("code_review_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_code_review_job_tasks(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        code_review_job_id: Optional[str] = None,
        step_name: Optional["aws_sdk_securityagent.types.step_name.StepName"] = None,
        category_name: Optional[str] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_securityagent.types.list_code_review_job_tasks_output.ListCodeReviewJobTasksOutput":
        """<p>Returns a paginated list of task summaries for the specified code review job, optionally filtered by step name or category.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            code_review_job_id: <p>The unique identifier of the code review job to list tasks for.</p>
            step_name: <p>Filter tasks by step name.</p>
            category_name: <p>Filter tasks by category name.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_code_review_job_tasks_input.ListCodeReviewJobTasksInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_code_review_job_tasks_output.ListCodeReviewJobTasksOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_code_review_job_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_code_review_job_tasks.async_list_code_review_job_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_code_review_job_tasks_input.ListCodeReviewJobTasksInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if max_results is not None:
            input_["max_results"] = max_results
        if code_review_job_id is not None:
            input_["code_review_job_id"] = code_review_job_id
        if step_name is not None:
            input_["step_name"] = step_name
        if category_name is not None:
            input_["category_name"] = category_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_code_review_job_tasks(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        code_review_job_id: Optional[str] = None,
        step_name: Optional["aws_sdk_securityagent.types.step_name.StepName"] = None,
        category_name: Optional[str] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.code_review_job_task_summary.CodeReviewJobTaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_code_review_job_tasks(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                code_review_job_id=code_review_job_id,
                step_name=step_name,
                category_name=category_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("code_review_job_task_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_code_reviews(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_securityagent.types.list_code_reviews_output.ListCodeReviewsOutput":
        """<p>Returns a paginated list of code review summaries for the specified agent space.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            agent_space_id: <p>The unique identifier of the agent space to list code reviews for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_code_reviews_input.ListCodeReviewsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_code_reviews_output.ListCodeReviewsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_code_reviews

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_code_reviews.async_list_code_reviews(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_code_reviews_input.ListCodeReviewsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_code_reviews(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.code_review_summary.CodeReviewSummary]":
        _token = next_token
        while True:
            _response = await self.list_code_reviews(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("code_review_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_discovered_endpoints(
        self,
        pentest_job_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        prefix: Optional[str] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_securityagent.types.list_discovered_endpoints_output.ListDiscoveredEndpointsOutput":
        """<p>Returns a paginated list of endpoints discovered during a pentest job execution.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            pentest_job_id: <p>The unique identifier of the pentest job to list discovered endpoints for.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            prefix: <p>A prefix to filter discovered endpoints by URI.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_discovered_endpoints_input.ListDiscoveredEndpointsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_discovered_endpoints_output.ListDiscoveredEndpointsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_discovered_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_discovered_endpoints.async_list_discovered_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_discovered_endpoints_input.ListDiscoveredEndpointsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        input_["pentest_job_id"] = pentest_job_id
        input_["agent_space_id"] = agent_space_id
        if prefix is not None:
            input_["prefix"] = prefix
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_discovered_endpoints(
        self,
        pentest_job_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        prefix: Optional[str] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.discovered_endpoint.DiscoveredEndpoint]":
        _token = next_token
        while True:
            _response = await self.list_discovered_endpoints(
                pentest_job_id,
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                prefix=prefix,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("discovered_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_findings(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        pentest_job_id: Optional[str] = None,
        code_review_job_id: Optional[str] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        risk_type: Optional[str] = None,
        risk_level: Optional["aws_sdk_securityagent.types.risk_level.RiskLevel"] = None,
        status: Optional[
            "aws_sdk_securityagent.types.finding_status.FindingStatus"
        ] = None,
        confidence: Optional[
            "aws_sdk_securityagent.types.confidence_level.ConfidenceLevel"
        ] = None,
        name: Optional[str] = None,
    ) -> "aws_sdk_securityagent.types.list_findings_output.ListFindingsOutput":
        """<p>Lists the security findings for a pentest job.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            pentest_job_id: <p>The unique identifier of the pentest job to list findings for.</p>
            code_review_job_id: <p>The unique identifier of the code review job to list findings for. Mutually exclusive with pentestJobId.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            risk_type: <p>Filter findings by risk type.</p>
            risk_level: <p>Filter findings by risk level.</p>
            status: <p>Filter findings by status.</p>
            confidence: <p>Filter findings by confidence level.</p>
            name: <p>Filter findings by name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_findings_input.ListFindingsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_findings_output.ListFindingsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_findings

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_findings.async_list_findings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_findings_input.ListFindingsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if pentest_job_id is not None:
            input_["pentest_job_id"] = pentest_job_id
        if code_review_job_id is not None:
            input_["code_review_job_id"] = code_review_job_id
        input_["agent_space_id"] = agent_space_id
        if next_token is not None:
            input_["next_token"] = next_token
        if risk_type is not None:
            input_["risk_type"] = risk_type
        if risk_level is not None:
            input_["risk_level"] = risk_level
        if status is not None:
            input_["status"] = status
        if confidence is not None:
            input_["confidence"] = confidence
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_findings(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        pentest_job_id: Optional[str] = None,
        code_review_job_id: Optional[str] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        risk_type: Optional[str] = None,
        risk_level: Optional["aws_sdk_securityagent.types.risk_level.RiskLevel"] = None,
        status: Optional[
            "aws_sdk_securityagent.types.finding_status.FindingStatus"
        ] = None,
        confidence: Optional[
            "aws_sdk_securityagent.types.confidence_level.ConfidenceLevel"
        ] = None,
        name: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.finding_summary.FindingSummary]":
        _token = next_token
        while True:
            _response = await self.list_findings(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                pentest_job_id=pentest_job_id,
                code_review_job_id=code_review_job_id,
                next_token=_token,
                risk_type=risk_type,
                risk_level=risk_level,
                status=status,
                confidence=confidence,
                name=name,
            )
            _page = _resolve_path(_response, ("findings_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_integrated_resources(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        integration_id: Optional[
            "aws_sdk_securityagent.types.integration_id.IntegrationId"
        ] = None,
        resource_type: Optional[
            "aws_sdk_securityagent.types.resource_type.ResourceType"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityagent.types.list_integrated_resources_output.ListIntegratedResourcesOutput":
        """<p>Lists the integrated resources for an agent space, optionally filtered by integration or resource type.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space to list integrated resources for.</p>
            integration_id: <p>The unique identifier of the integration to filter by.</p>
            resource_type: <p>The type of resource to filter by.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_integrated_resources_input.ListIntegratedResourcesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_integrated_resources_output.ListIntegratedResourcesOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_integrated_resources

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_integrated_resources.async_list_integrated_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_integrated_resources_input.ListIntegratedResourcesInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if integration_id is not None:
            input_["integration_id"] = integration_id
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_integrated_resources(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        integration_id: Optional[
            "aws_sdk_securityagent.types.integration_id.IntegrationId"
        ] = None,
        resource_type: Optional[
            "aws_sdk_securityagent.types.resource_type.ResourceType"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.integrated_resource_summary.IntegratedResourceSummary]":
        _token = next_token
        while True:
            _response = await self.list_integrated_resources(
                agent_space_id,
                config_overrides=config_overrides,
                integration_id=integration_id,
                resource_type=resource_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("integrated_resource_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_memberships(
        self,
        application_id: "aws_sdk_securityagent.types.application_id.ApplicationId",
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        member_type: Optional[
            "aws_sdk_securityagent.types.membership_type_filter.MembershipTypeFilter"
        ] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> (
        "aws_sdk_securityagent.types.list_memberships_response.ListMembershipsResponse"
    ):
        """<p>Returns a paginated list of membership summaries for the specified agent space within an application.</p>

        Args:
            application_id: <p>The unique identifier of the application that contains the agent space.</p>
            agent_space_id: <p>The unique identifier of the agent space to list memberships for.</p>
            member_type: <p>Filter memberships by member type.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_memberships_request.ListMembershipsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_memberships_response.ListMembershipsResponse"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_memberships

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_memberships.async_list_memberships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_memberships_request.ListMembershipsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["agent_space_id"] = agent_space_id
        if member_type is not None:
            input_["member_type"] = member_type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_memberships(
        self,
        application_id: "aws_sdk_securityagent.types.application_id.ApplicationId",
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        member_type: Optional[
            "aws_sdk_securityagent.types.membership_type_filter.MembershipTypeFilter"
        ] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.membership_summary.MembershipSummary]":
        _token = next_token
        while True:
            _response = await self.list_memberships(
                application_id,
                agent_space_id,
                config_overrides=config_overrides,
                member_type=member_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("membership_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pentest_jobs_for_pentest(
        self,
        pentest_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_securityagent.types.list_pentest_jobs_for_pentest_output.ListPentestJobsForPentestOutput":
        """<p>Returns a paginated list of pentest job summaries for the specified pentest configuration.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            pentest_id: <p>The unique identifier of the pentest to list jobs for.</p>
            agent_space_id: <p>The unique identifier of the agent space.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_pentest_jobs_for_pentest_input.ListPentestJobsForPentestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_pentest_jobs_for_pentest_output.ListPentestJobsForPentestOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_pentest_jobs_for_pentest

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_pentest_jobs_for_pentest.async_list_pentest_jobs_for_pentest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_pentest_jobs_for_pentest_input.ListPentestJobsForPentestInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        input_["pentest_id"] = pentest_id
        input_["agent_space_id"] = agent_space_id
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_pentest_jobs_for_pentest(
        self,
        pentest_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.pentest_job_summary.PentestJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_pentest_jobs_for_pentest(
                pentest_id,
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pentest_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pentest_job_tasks(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        pentest_job_id: Optional[str] = None,
        step_name: Optional["aws_sdk_securityagent.types.step_name.StepName"] = None,
        category_name: Optional[str] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_securityagent.types.list_pentest_job_tasks_output.ListPentestJobTasksOutput":
        """<p>Returns a paginated list of task summaries for the specified pentest job, optionally filtered by step name or category.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            pentest_job_id: <p>The unique identifier of the pentest job to list tasks for.</p>
            step_name: <p>Filter tasks by step name. Valid values include PREFLIGHT, STATIC_ANALYSIS, PENTEST, and FINALIZING.</p>
            category_name: <p>Filter tasks by category name.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_pentest_job_tasks_input.ListPentestJobTasksInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_pentest_job_tasks_output.ListPentestJobTasksOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_pentest_job_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_pentest_job_tasks.async_list_pentest_job_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_pentest_job_tasks_input.ListPentestJobTasksInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if max_results is not None:
            input_["max_results"] = max_results
        if pentest_job_id is not None:
            input_["pentest_job_id"] = pentest_job_id
        if step_name is not None:
            input_["step_name"] = step_name
        if category_name is not None:
            input_["category_name"] = category_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_pentest_job_tasks(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        pentest_job_id: Optional[str] = None,
        step_name: Optional["aws_sdk_securityagent.types.step_name.StepName"] = None,
        category_name: Optional[str] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.task_summary.TaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_pentest_job_tasks(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                pentest_job_id=pentest_job_id,
                step_name=step_name,
                category_name=category_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("task_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pentests(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_securityagent.types.list_pentests_output.ListPentestsOutput":
        """<p>Returns a paginated list of pentest summaries for the specified agent space.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            agent_space_id: <p>The unique identifier of the agent space to list pentests for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_pentests_input.ListPentestsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_pentests_output.ListPentestsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_pentests

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_pentests.async_list_pentests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_pentests_input.ListPentestsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["agent_space_id"] = agent_space_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_pentests(
        self,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_securityagent.types.pentest_summary.PentestSummary]":
        _token = next_token
        while True:
            _response = await self.list_pentests(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pentest_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_securityagent.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns the tags associated with the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_code_remediation(
        self,
        agent_space_id: str,
        finding_ids: "aws_sdk_securityagent.types.finding_id_list.FindingIdList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        pentest_job_id: Optional[str] = None,
        code_review_job_id: Optional[str] = None,
    ) -> "aws_sdk_securityagent.types.start_code_remediation_output.StartCodeRemediationOutput":
        """<p>Initiates code remediation for one or more security findings. This creates pull requests in integrated repositories to fix the identified vulnerabilities.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            pentest_job_id: <p>The unique identifier of the pentest job that produced the findings. Mutually exclusive with <code>codeReviewJobId</code>.</p>
            code_review_job_id: <p>The unique identifier of the code review job that produced the findings. Mutually exclusive with <code>pentestJobId</code>.</p>
            finding_ids: <p>The list of finding identifiers to initiate code remediation for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.start_code_remediation_input.StartCodeRemediationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.start_code_remediation_output.StartCodeRemediationOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.start_code_remediation

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.start_code_remediation.async_start_code_remediation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.start_code_remediation_input.StartCodeRemediationInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if pentest_job_id is not None:
            input_["pentest_job_id"] = pentest_job_id
        if code_review_job_id is not None:
            input_["code_review_job_id"] = code_review_job_id
        input_["finding_ids"] = finding_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_code_review_job(
        self,
        agent_space_id: str,
        code_review_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.start_code_review_job_output.StartCodeReviewJobOutput":
        """<p>Starts a new code review job for a code review configuration. The job executes the security-focused code analysis defined in the code review.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            code_review_id: <p>The unique identifier of the code review to start a job for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.start_code_review_job_input.StartCodeReviewJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.start_code_review_job_output.StartCodeReviewJobOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.start_code_review_job

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.start_code_review_job.async_start_code_review_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.start_code_review_job_input.StartCodeReviewJobInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["code_review_id"] = code_review_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_pentest_job(
        self,
        agent_space_id: str,
        pentest_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.start_pentest_job_output.StartPentestJobOutput":
        """<p>Starts a new pentest job for a pentest configuration. The job executes the security tests defined in the pentest.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            pentest_id: <p>The unique identifier of the pentest to start a job for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.start_pentest_job_input.StartPentestJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.start_pentest_job_output.StartPentestJobOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.start_pentest_job

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.start_pentest_job.async_start_pentest_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.start_pentest_job_input.StartPentestJobInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["pentest_id"] = pentest_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_code_review_job(
        self,
        agent_space_id: str,
        code_review_job_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.stop_code_review_job_output.StopCodeReviewJobOutput":
        """<p>Stops a running code review job. The job transitions to a stopping state and then to stopped after cleanup completes.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            code_review_job_id: <p>The unique identifier of the code review job to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.stop_code_review_job_input.StopCodeReviewJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.stop_code_review_job_output.StopCodeReviewJobOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.stop_code_review_job

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.stop_code_review_job.async_stop_code_review_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.stop_code_review_job_input.StopCodeReviewJobInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["code_review_job_id"] = code_review_job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_pentest_job(
        self,
        agent_space_id: str,
        pentest_job_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.stop_pentest_job_output.StopPentestJobOutput":
        """<p>Stops a running pentest job. The job transitions to a stopping state and then to stopped after cleanup completes.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            pentest_job_id: <p>The unique identifier of the pentest job to stop.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.stop_pentest_job_input.StopPentestJobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.stop_pentest_job_output.StopPentestJobOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.stop_pentest_job

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.stop_pentest_job.async_stop_pentest_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.stop_pentest_job_input.StopPentestJobInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["pentest_job_id"] = pentest_job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_securityagent.types.resource_arn.ResourceArn",
        tags: "aws_sdk_securityagent.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.tag_resource_output.TagResourceOutput":
        """<p>Adds tags to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>The tags to add to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_securityagent.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_securityagent.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_code_review(
        self,
        code_review_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        title: Optional[str] = None,
        assets: Optional["aws_sdk_securityagent.types.assets.Assets"] = None,
        service_role: Optional[
            "aws_sdk_securityagent.types.service_role.ServiceRole"
        ] = None,
        log_config: Optional[
            "aws_sdk_securityagent.types.cloud_watch_log.CloudWatchLog"
        ] = None,
        code_remediation_strategy: Optional[
            "aws_sdk_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
        ] = None,
    ) -> "aws_sdk_securityagent.types.update_code_review_output.UpdateCodeReviewOutput":
        """<p>Updates an existing code review configuration.</p>

        Args:
            code_review_id: <p>The unique identifier of the code review to update.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the code review.</p>
            title: <p>The updated title of the code review.</p>
            assets: <p>The updated assets for the code review.</p>
            service_role: <p>The updated IAM service role for the code review.</p>
            log_config: <p>The updated CloudWatch Logs configuration for the code review.</p>
            code_remediation_strategy: <p>The updated code remediation strategy for the code review.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.update_code_review_input.UpdateCodeReviewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.update_code_review_output.UpdateCodeReviewOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.update_code_review

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.update_code_review.async_update_code_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.update_code_review_input.UpdateCodeReviewInput = {}  # type: ignore[typeddict-item]
        input_["code_review_id"] = code_review_id
        input_["agent_space_id"] = agent_space_id
        if title is not None:
            input_["title"] = title
        if assets is not None:
            input_["assets"] = assets
        if service_role is not None:
            input_["service_role"] = service_role
        if log_config is not None:
            input_["log_config"] = log_config
        if code_remediation_strategy is not None:
            input_["code_remediation_strategy"] = code_remediation_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_finding(
        self,
        finding_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        risk_level: Optional["aws_sdk_securityagent.types.risk_level.RiskLevel"] = None,
        status: Optional[
            "aws_sdk_securityagent.types.finding_status.FindingStatus"
        ] = None,
    ) -> "aws_sdk_securityagent.types.update_finding_output.UpdateFindingOutput":
        """<p>Updates the status or risk level of a security finding.</p>

        Args:
            finding_id: <p>The unique identifier of the finding to update.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the finding.</p>
            risk_level: <p>The updated risk level for the finding.</p>
            status: <p>The updated status for the finding.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.update_finding_input.UpdateFindingInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.update_finding_output.UpdateFindingOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.update_finding

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.update_finding.async_update_finding(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.update_finding_input.UpdateFindingInput = {}  # type: ignore[typeddict-item]
        input_["finding_id"] = finding_id
        input_["agent_space_id"] = agent_space_id
        if risk_level is not None:
            input_["risk_level"] = risk_level
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_integrated_resources(
        self,
        agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId",
        integration_id: "aws_sdk_securityagent.types.integration_id.IntegrationId",
        items: "aws_sdk_securityagent.types.integrated_resource_input_item_list.IntegratedResourceInputItemList",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.update_integrated_resources_output.UpdateIntegratedResourcesOutput":
        """<p>Updates the integrated resources for an agent space, including their capabilities.</p>

        Args:
            agent_space_id: <p>The unique identifier of the agent space.</p>
            integration_id: <p>The unique identifier of the integration.</p>
            items: <p>The list of integrated resource items to update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.update_integrated_resources_input.UpdateIntegratedResourcesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.update_integrated_resources_output.UpdateIntegratedResourcesOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.update_integrated_resources

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.update_integrated_resources.async_update_integrated_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.update_integrated_resources_input.UpdateIntegratedResourcesInput = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["integration_id"] = integration_id
        input_["items"] = items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_pentest(
        self,
        pentest_id: str,
        agent_space_id: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        title: Optional[str] = None,
        assets: Optional["aws_sdk_securityagent.types.assets.Assets"] = None,
        exclude_risk_types: Optional[
            "aws_sdk_securityagent.types.risk_type_list.RiskTypeList"
        ] = None,
        service_role: Optional[
            "aws_sdk_securityagent.types.service_role.ServiceRole"
        ] = None,
        log_config: Optional[
            "aws_sdk_securityagent.types.cloud_watch_log.CloudWatchLog"
        ] = None,
        vpc_config: Optional["aws_sdk_securityagent.types.vpc_config.VpcConfig"] = None,
        network_traffic_config: Optional[
            "aws_sdk_securityagent.types.network_traffic_config.NetworkTrafficConfig"
        ] = None,
        code_remediation_strategy: Optional[
            "aws_sdk_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
        ] = None,
    ) -> "aws_sdk_securityagent.types.update_pentest_output.UpdatePentestOutput":
        """<p>Updates an existing pentest configuration.</p>

        Args:
            pentest_id: <p>The unique identifier of the pentest to update.</p>
            agent_space_id: <p>The unique identifier of the agent space that contains the pentest.</p>
            title: <p>The updated title of the pentest.</p>
            assets: <p>The updated assets for the pentest.</p>
            exclude_risk_types: <p>The updated list of risk types to exclude from the pentest.</p>
            service_role: <p>The updated IAM service role for the pentest.</p>
            log_config: <p>The updated CloudWatch Logs configuration for the pentest.</p>
            vpc_config: <p>The updated VPC configuration for the pentest.</p>
            network_traffic_config: <p>The updated network traffic configuration for the pentest.</p>
            code_remediation_strategy: <p>The updated code remediation strategy for the pentest.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.update_pentest_input.UpdatePentestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.update_pentest_output.UpdatePentestOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.update_pentest

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.update_pentest.async_update_pentest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.update_pentest_input.UpdatePentestInput = {}  # type: ignore[typeddict-item]
        input_["pentest_id"] = pentest_id
        input_["agent_space_id"] = agent_space_id
        if title is not None:
            input_["title"] = title
        if assets is not None:
            input_["assets"] = assets
        if exclude_risk_types is not None:
            input_["exclude_risk_types"] = exclude_risk_types
        if service_role is not None:
            input_["service_role"] = service_role
        if log_config is not None:
            input_["log_config"] = log_config
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if network_traffic_config is not None:
            input_["network_traffic_config"] = network_traffic_config
        if code_remediation_strategy is not None:
            input_["code_remediation_strategy"] = code_remediation_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def verify_target_domain(
        self,
        target_domain_id: "aws_sdk_securityagent.types.target_domain_id.TargetDomainId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.verify_target_domain_output.VerifyTargetDomainOutput":
        """<p>Initiates verification of a target domain. This checks whether the domain ownership verification token has been properly configured.</p>

        Args:
            target_domain_id: <p>The unique identifier of the target domain to verify.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.verify_target_domain_input.VerifyTargetDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.verify_target_domain_output.VerifyTargetDomainOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.verify_target_domain

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.verify_target_domain.async_verify_target_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.verify_target_domain_input.VerifyTargetDomainInput = {}  # type: ignore[typeddict-item]
        input_["target_domain_id"] = target_domain_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
