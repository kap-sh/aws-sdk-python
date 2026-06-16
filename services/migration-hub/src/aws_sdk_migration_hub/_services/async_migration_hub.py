"""Generated from Smithy shape ``com.amazonaws.migrationhub#AWSMigrationHub``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_migration_hub._auth._signers
import aws_sdk_migration_hub._auth._sigv4
from aws_sdk_migration_hub._auth._identity import Credentials
from aws_sdk_migration_hub._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_migration_hub._auth._zapros_handler import AuthMiddleware
from aws_sdk_migration_hub._pagination import resolve_path as _resolve_path
from aws_sdk_migration_hub._services._aws_config import aaws_config
from aws_sdk_migration_hub._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.application_id
    import aws_sdk_migration_hub.types.application_ids
    import aws_sdk_migration_hub.types.application_state
    import aws_sdk_migration_hub.types.application_status
    import aws_sdk_migration_hub.types.associate_created_artifact_request
    import aws_sdk_migration_hub.types.associate_created_artifact_result
    import aws_sdk_migration_hub.types.associate_discovered_resource_request
    import aws_sdk_migration_hub.types.associate_discovered_resource_result
    import aws_sdk_migration_hub.types.associate_source_resource_request
    import aws_sdk_migration_hub.types.associate_source_resource_result
    import aws_sdk_migration_hub.types.configuration_id
    import aws_sdk_migration_hub.types.create_progress_update_stream_request
    import aws_sdk_migration_hub.types.create_progress_update_stream_result
    import aws_sdk_migration_hub.types.created_artifact
    import aws_sdk_migration_hub.types.created_artifact_name
    import aws_sdk_migration_hub.types.delete_progress_update_stream_request
    import aws_sdk_migration_hub.types.delete_progress_update_stream_result
    import aws_sdk_migration_hub.types.describe_application_state_request
    import aws_sdk_migration_hub.types.describe_application_state_result
    import aws_sdk_migration_hub.types.describe_migration_task_request
    import aws_sdk_migration_hub.types.describe_migration_task_result
    import aws_sdk_migration_hub.types.disassociate_created_artifact_request
    import aws_sdk_migration_hub.types.disassociate_created_artifact_result
    import aws_sdk_migration_hub.types.disassociate_discovered_resource_request
    import aws_sdk_migration_hub.types.disassociate_discovered_resource_result
    import aws_sdk_migration_hub.types.disassociate_source_resource_request
    import aws_sdk_migration_hub.types.disassociate_source_resource_result
    import aws_sdk_migration_hub.types.discovered_resource
    import aws_sdk_migration_hub.types.dry_run
    import aws_sdk_migration_hub.types.import_migration_task_request
    import aws_sdk_migration_hub.types.import_migration_task_result
    import aws_sdk_migration_hub.types.list_application_states_request
    import aws_sdk_migration_hub.types.list_application_states_result
    import aws_sdk_migration_hub.types.list_created_artifacts_request
    import aws_sdk_migration_hub.types.list_created_artifacts_result
    import aws_sdk_migration_hub.types.list_discovered_resources_request
    import aws_sdk_migration_hub.types.list_discovered_resources_result
    import aws_sdk_migration_hub.types.list_migration_task_updates_request
    import aws_sdk_migration_hub.types.list_migration_task_updates_result
    import aws_sdk_migration_hub.types.list_migration_tasks_request
    import aws_sdk_migration_hub.types.list_migration_tasks_result
    import aws_sdk_migration_hub.types.list_progress_update_streams_request
    import aws_sdk_migration_hub.types.list_progress_update_streams_result
    import aws_sdk_migration_hub.types.list_source_resources_request
    import aws_sdk_migration_hub.types.list_source_resources_result
    import aws_sdk_migration_hub.types.max_results
    import aws_sdk_migration_hub.types.max_results_created_artifacts
    import aws_sdk_migration_hub.types.max_results_resources
    import aws_sdk_migration_hub.types.max_results_source_resources
    import aws_sdk_migration_hub.types.migration_task_name
    import aws_sdk_migration_hub.types.migration_task_summary
    import aws_sdk_migration_hub.types.migration_task_update
    import aws_sdk_migration_hub.types.next_update_seconds
    import aws_sdk_migration_hub.types.notify_application_state_request
    import aws_sdk_migration_hub.types.notify_application_state_result
    import aws_sdk_migration_hub.types.notify_migration_task_state_request
    import aws_sdk_migration_hub.types.notify_migration_task_state_result
    import aws_sdk_migration_hub.types.progress_update_stream
    import aws_sdk_migration_hub.types.progress_update_stream_summary
    import aws_sdk_migration_hub.types.put_resource_attributes_request
    import aws_sdk_migration_hub.types.put_resource_attributes_result
    import aws_sdk_migration_hub.types.resource_attribute_list
    import aws_sdk_migration_hub.types.resource_name
    import aws_sdk_migration_hub.types.source_resource
    import aws_sdk_migration_hub.types.source_resource_name
    import aws_sdk_migration_hub.types.task
    import aws_sdk_migration_hub.types.token
    import aws_sdk_migration_hub.types.update_date_time


class AsyncMigrationHubClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncMigrationHubClient:
    """A client for the ``MigrationHub`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncMigrationHubClientConfig(
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
        self, config_overrides: Optional[AsyncMigrationHubClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMigrationHubClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def associate_created_artifact(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        created_artifact: "aws_sdk_migration_hub.types.created_artifact.CreatedArtifact",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.associate_created_artifact_result.AssociateCreatedArtifactResult":
        """<p>Associates a created artifact of an AWS cloud resource, the target receiving the migration, with the migration task performed by a migration tool. This API has the following traits:</p> <ul> <li> <p>Migration tools can call the <code>AssociateCreatedArtifact</code> operation to indicate which AWS artifact is associated with a migration task.</p> </li> <li> <p>The created artifact name must be provided in ARN (Amazon Resource Name) format which will contain information about type and region; for example: <code>arn:aws:ec2:us-east-1:488216288981:image/ami-6d0ba87b</code>.</p> </li> <li> <p>Examples of the AWS resource behind the created artifact are, AMI's, EC2 instance, or DMS endpoint, etc.</p> </li> </ul>

        Args:
            progress_update_stream: <p>The name of the ProgressUpdateStream. </p>
            migration_task_name: <p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>
            created_artifact: <p>An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.) </p>
            dry_run: <p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.associate_created_artifact_request.AssociateCreatedArtifactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.associate_created_artifact_result.AssociateCreatedArtifactResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.associate_created_artifact

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.associate_created_artifact.async_associate_created_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.associate_created_artifact_request.AssociateCreatedArtifactRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
        input_["created_artifact"] = created_artifact
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_discovered_resource(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        discovered_resource: "aws_sdk_migration_hub.types.discovered_resource.DiscoveredResource",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.associate_discovered_resource_result.AssociateDiscoveredResourceResult":
        """<p>Associates a discovered resource ID from Application Discovery Service with a migration task.</p>

        Args:
            progress_update_stream: <p>The name of the ProgressUpdateStream.</p>
            migration_task_name: <p>The identifier given to the MigrationTask. <i>Do not store personal data in this field.</i> </p>
            discovered_resource: <p>Object representing a Resource.</p>
            dry_run: <p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.associate_discovered_resource_request.AssociateDiscoveredResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.associate_discovered_resource_result.AssociateDiscoveredResourceResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.associate_discovered_resource

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.associate_discovered_resource.async_associate_discovered_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.associate_discovered_resource_request.AssociateDiscoveredResourceRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
        input_["discovered_resource"] = discovered_resource
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_source_resource(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        source_resource: "aws_sdk_migration_hub.types.source_resource.SourceResource",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.associate_source_resource_result.AssociateSourceResourceResult":
        """<p>Associates a source resource with a migration task. For example, the source resource can be a source server, an application, or a migration wave.</p>

        Args:
            progress_update_stream: <p>The name of the progress-update stream, which is used for access control as well as a namespace for migration-task names that is implicitly linked to your AWS account. The progress-update stream must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.</p>
            migration_task_name: <p>A unique identifier that references the migration task. <i>Do not include sensitive data in this field.</i> </p>
            source_resource: <p>The source resource that you want to associate.</p>
            dry_run: <p>This is an optional parameter that you can use to test whether the call will succeed. Set this parameter to <code>true</code> to verify that you have the permissions that are required to make the call, and that you have specified the other parameters in the call correctly.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.associate_source_resource_request.AssociateSourceResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.associate_source_resource_result.AssociateSourceResourceResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.associate_source_resource

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.associate_source_resource.async_associate_source_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.associate_source_resource_request.AssociateSourceResourceRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
        input_["source_resource"] = source_resource
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_progress_update_stream(
        self,
        progress_update_stream_name: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.create_progress_update_stream_result.CreateProgressUpdateStreamResult":
        """<p>Creates a progress update stream which is an AWS resource used for access control as well as a namespace for migration task names that is implicitly linked to your AWS account. It must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.</p>

        Args:
            progress_update_stream_name: <p>The name of the ProgressUpdateStream. <i>Do not store personal data in this field.</i> </p>
            dry_run: <p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.create_progress_update_stream_request.CreateProgressUpdateStreamRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.create_progress_update_stream_result.CreateProgressUpdateStreamResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.create_progress_update_stream

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.create_progress_update_stream.async_create_progress_update_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.create_progress_update_stream_request.CreateProgressUpdateStreamRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream_name"] = progress_update_stream_name
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_progress_update_stream(
        self,
        progress_update_stream_name: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.delete_progress_update_stream_result.DeleteProgressUpdateStreamResult":
        r"""<p>Deletes a progress update stream, including all of its tasks, which was previously created as an AWS resource used for access control. This API has the following traits:</p> <ul> <li> <p>The only parameter needed for <code>DeleteProgressUpdateStream</code> is the stream name (same as a <code>CreateProgressUpdateStream</code> call).</p> </li> <li> <p>The call will return, and a background process will asynchronously delete the stream and all of its resources (tasks, associated resources, resource attributes, created artifacts).</p> </li> <li> <p>If the stream takes time to be deleted, it might still show up on a <code>ListProgressUpdateStreams</code> call.</p> </li> <li> <p> <code>CreateProgressUpdateStream</code>, <code>ImportMigrationTask</code>, <code>NotifyMigrationTaskState</code>, and all Associate[*] APIs related to the tasks belonging to the stream will throw \"InvalidInputException\" if the stream of the same name is in the process of being deleted.</p> </li> <li> <p>Once the stream and all of its resources are deleted, <code>CreateProgressUpdateStream</code> for a stream of the same name will succeed, and that stream will be an entirely new logical resource (without any resources associated with the old stream).</p> </li> </ul>

        Args:
            progress_update_stream_name: <p>The name of the ProgressUpdateStream. <i>Do not store personal data in this field.</i> </p>
            dry_run: <p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.delete_progress_update_stream_request.DeleteProgressUpdateStreamRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.delete_progress_update_stream_result.DeleteProgressUpdateStreamResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.delete_progress_update_stream

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.delete_progress_update_stream.async_delete_progress_update_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.delete_progress_update_stream_request.DeleteProgressUpdateStreamRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream_name"] = progress_update_stream_name
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_application_state(
        self,
        application_id: "aws_sdk_migration_hub.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
    ) -> "aws_sdk_migration_hub.types.describe_application_state_result.DescribeApplicationStateResult":
        """<p>Gets the migration status of an application.</p>

        Args:
            application_id: <p>The configurationId in Application Discovery Service that uniquely identifies the grouped application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.describe_application_state_request.DescribeApplicationStateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.describe_application_state_result.DescribeApplicationStateResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.describe_application_state

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.describe_application_state.async_describe_application_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.describe_application_state_request.DescribeApplicationStateRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_migration_task(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
    ) -> "aws_sdk_migration_hub.types.describe_migration_task_result.DescribeMigrationTaskResult":
        """<p>Retrieves a list of all attributes associated with a specific migration task.</p>

        Args:
            progress_update_stream: <p>The name of the ProgressUpdateStream. </p>
            migration_task_name: <p>The identifier given to the MigrationTask. <i>Do not store personal data in this field.</i> </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.describe_migration_task_request.DescribeMigrationTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.describe_migration_task_result.DescribeMigrationTaskResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.describe_migration_task

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.describe_migration_task.async_describe_migration_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.describe_migration_task_request.DescribeMigrationTaskRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_created_artifact(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        created_artifact_name: "aws_sdk_migration_hub.types.created_artifact_name.CreatedArtifactName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.disassociate_created_artifact_result.DisassociateCreatedArtifactResult":
        """<p>Disassociates a created artifact of an AWS resource with a migration task performed by a migration tool that was previously associated. This API has the following traits:</p> <ul> <li> <p>A migration user can call the <code>DisassociateCreatedArtifacts</code> operation to disassociate a created AWS Artifact from a migration task.</p> </li> <li> <p>The created artifact name must be provided in ARN (Amazon Resource Name) format which will contain information about type and region; for example: <code>arn:aws:ec2:us-east-1:488216288981:image/ami-6d0ba87b</code>.</p> </li> <li> <p>Examples of the AWS resource behind the created artifact are, AMI's, EC2 instance, or RDS instance, etc.</p> </li> </ul>

        Args:
            progress_update_stream: <p>The name of the ProgressUpdateStream. </p>
            migration_task_name: <p>Unique identifier that references the migration task to be disassociated with the artifact. <i>Do not store personal data in this field.</i> </p>
            created_artifact_name: <p>An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.)</p>
            dry_run: <p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.disassociate_created_artifact_request.DisassociateCreatedArtifactRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.disassociate_created_artifact_result.DisassociateCreatedArtifactResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.disassociate_created_artifact

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.disassociate_created_artifact.async_disassociate_created_artifact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.disassociate_created_artifact_request.DisassociateCreatedArtifactRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
        input_["created_artifact_name"] = created_artifact_name
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_discovered_resource(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        configuration_id: "aws_sdk_migration_hub.types.configuration_id.ConfigurationId",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.disassociate_discovered_resource_result.DisassociateDiscoveredResourceResult":
        """<p>Disassociate an Application Discovery Service discovered resource from a migration task.</p>

        Args:
            progress_update_stream: <p>The name of the ProgressUpdateStream.</p>
            migration_task_name: <p>The identifier given to the MigrationTask. <i>Do not store personal data in this field.</i> </p>
            configuration_id: <p>ConfigurationId of the Application Discovery Service resource to be disassociated.</p>
            dry_run: <p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.disassociate_discovered_resource_request.DisassociateDiscoveredResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.disassociate_discovered_resource_result.DisassociateDiscoveredResourceResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.disassociate_discovered_resource

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.disassociate_discovered_resource.async_disassociate_discovered_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.disassociate_discovered_resource_request.DisassociateDiscoveredResourceRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
        input_["configuration_id"] = configuration_id
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_source_resource(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        source_resource_name: "aws_sdk_migration_hub.types.source_resource_name.SourceResourceName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.disassociate_source_resource_result.DisassociateSourceResourceResult":
        """<p>Removes the association between a source resource and a migration task.</p>

        Args:
            progress_update_stream: <p>The name of the progress-update stream, which is used for access control as well as a namespace for migration-task names that is implicitly linked to your AWS account. The progress-update stream must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.</p>
            migration_task_name: <p>A unique identifier that references the migration task. <i>Do not include sensitive data in this field.</i> </p>
            source_resource_name: <p>The name that was specified for the source resource.</p>
            dry_run: <p>This is an optional parameter that you can use to test whether the call will succeed. Set this parameter to <code>true</code> to verify that you have the permissions that are required to make the call, and that you have specified the other parameters in the call correctly.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.disassociate_source_resource_request.DisassociateSourceResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.disassociate_source_resource_result.DisassociateSourceResourceResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.disassociate_source_resource

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.disassociate_source_resource.async_disassociate_source_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.disassociate_source_resource_request.DisassociateSourceResourceRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
        input_["source_resource_name"] = source_resource_name
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_migration_task(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.import_migration_task_result.ImportMigrationTaskResult":
        """<p>Registers a new migration task which represents a server, database, etc., being migrated to AWS by a migration tool.</p> <p>This API is a prerequisite to calling the <code>NotifyMigrationTaskState</code> API as the migration tool must first register the migration task with Migration Hub.</p>

        Args:
            progress_update_stream: <p>The name of the ProgressUpdateStream. ></p>
            migration_task_name: <p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>
            dry_run: <p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.import_migration_task_request.ImportMigrationTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.import_migration_task_result.ImportMigrationTaskResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.import_migration_task

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.import_migration_task.async_import_migration_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.import_migration_task_request.ImportMigrationTaskRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_application_states(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        application_ids: Optional[
            "aws_sdk_migration_hub.types.application_ids.ApplicationIds"
        ] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_migration_hub.types.list_application_states_result.ListApplicationStatesResult":
        """<p>Lists all the migration statuses for your applications. If you use the optional <code>ApplicationIds</code> parameter, only the migration statuses for those applications will be returned.</p>

        Args:
            application_ids: <p>The configurationIds from the Application Discovery Service that uniquely identifies your applications.</p>
            next_token: <p>If a <code>NextToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>
            max_results: <p>Maximum number of results to be returned per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.list_application_states_request.ListApplicationStatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.list_application_states_result.ListApplicationStatesResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.list_application_states

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.list_application_states.async_list_application_states(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.list_application_states_request.ListApplicationStatesRequest = {}  # type: ignore[typeddict-item]
        if application_ids is not None:
            input_["application_ids"] = application_ids
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

    async def iter_list_application_states(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        application_ids: Optional[
            "aws_sdk_migration_hub.types.application_ids.ApplicationIds"
        ] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "AsyncIterator[aws_sdk_migration_hub.types.application_state.ApplicationState]"
    ):
        _token = next_token
        while True:
            _response = await self.list_application_states(
                config_overrides=config_overrides,
                application_ids=application_ids,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("application_state_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_created_artifacts(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results_created_artifacts.MaxResultsCreatedArtifacts"
        ] = None,
    ) -> "aws_sdk_migration_hub.types.list_created_artifacts_result.ListCreatedArtifactsResult":
        """<p>Lists the created artifacts attached to a given migration task in an update stream. This API has the following traits:</p> <ul> <li> <p>Gets the list of the created artifacts while migration is taking place.</p> </li> <li> <p>Shows the artifacts created by the migration tool that was associated by the <code>AssociateCreatedArtifact</code> API. </p> </li> <li> <p>Lists created artifacts in a paginated interface. </p> </li> </ul>

        Args:
            progress_update_stream: <p>The name of the ProgressUpdateStream. </p>
            migration_task_name: <p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>
            next_token: <p>If a <code>NextToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>
            max_results: <p>Maximum number of results to be returned per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.list_created_artifacts_request.ListCreatedArtifactsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.list_created_artifacts_result.ListCreatedArtifactsResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.list_created_artifacts

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.list_created_artifacts.async_list_created_artifacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.list_created_artifacts_request.ListCreatedArtifactsRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
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

    async def iter_list_created_artifacts(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results_created_artifacts.MaxResultsCreatedArtifacts"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_migration_hub.types.created_artifact.CreatedArtifact]":
        _token = next_token
        while True:
            _response = await self.list_created_artifacts(
                progress_update_stream,
                migration_task_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("created_artifact_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_discovered_resources(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results_resources.MaxResultsResources"
        ] = None,
    ) -> "aws_sdk_migration_hub.types.list_discovered_resources_result.ListDiscoveredResourcesResult":
        """<p>Lists discovered resources associated with the given <code>MigrationTask</code>.</p>

        Args:
            progress_update_stream: <p>The name of the ProgressUpdateStream.</p>
            migration_task_name: <p>The name of the MigrationTask. <i>Do not store personal data in this field.</i> </p>
            next_token: <p>If a <code>NextToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>
            max_results: <p>The maximum number of results returned per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.list_discovered_resources_request.ListDiscoveredResourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.list_discovered_resources_result.ListDiscoveredResourcesResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.list_discovered_resources

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.list_discovered_resources.async_list_discovered_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.list_discovered_resources_request.ListDiscoveredResourcesRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
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

    async def iter_list_discovered_resources(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results_resources.MaxResultsResources"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_migration_hub.types.discovered_resource.DiscoveredResource]":
        _token = next_token
        while True:
            _response = await self.list_discovered_resources(
                progress_update_stream,
                migration_task_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("discovered_resource_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_migration_tasks(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results.MaxResults"
        ] = None,
        resource_name: Optional[
            "aws_sdk_migration_hub.types.resource_name.ResourceName"
        ] = None,
    ) -> "aws_sdk_migration_hub.types.list_migration_tasks_result.ListMigrationTasksResult":
        """<p>Lists all, or filtered by resource name, migration tasks associated with the user account making this call. This API has the following traits:</p> <ul> <li> <p>Can show a summary list of the most recent migration tasks.</p> </li> <li> <p>Can show a summary list of migration tasks associated with a given discovered resource.</p> </li> <li> <p>Lists migration tasks in a paginated interface.</p> </li> </ul>

        Args:
            next_token: <p>If a <code>NextToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>
            max_results: <p>Value to specify how many results are returned per page.</p>
            resource_name: <p>Filter migration tasks by discovered resource name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.list_migration_tasks_request.ListMigrationTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.list_migration_tasks_result.ListMigrationTasksResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.list_migration_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.list_migration_tasks.async_list_migration_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.list_migration_tasks_request.ListMigrationTasksRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_migration_tasks(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results.MaxResults"
        ] = None,
        resource_name: Optional[
            "aws_sdk_migration_hub.types.resource_name.ResourceName"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_migration_hub.types.migration_task_summary.MigrationTaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_migration_tasks(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                resource_name=resource_name,
            )
            _page = _resolve_path(_response, ("migration_task_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_migration_task_updates(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_migration_hub.types.list_migration_task_updates_result.ListMigrationTaskUpdatesResult":
        """<p>This is a paginated API that returns all the migration-task states for the specified <code>MigrationTaskName</code> and <code>ProgressUpdateStream</code>.</p>

        Args:
            progress_update_stream: <p>The name of the progress-update stream, which is used for access control as well as a namespace for migration-task names that is implicitly linked to your AWS account. The progress-update stream must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.</p>
            migration_task_name: <p>A unique identifier that references the migration task. <i>Do not include sensitive data in this field.</i> </p>
            next_token: <p>If <code>NextToken</code> was returned by a previous call, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. To retrieve the next page of results, specify the <code>NextToken</code> value that the previous call returned. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the value that you specify here for <code>MaxResults</code>, the response will include a token that you can use to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.list_migration_task_updates_request.ListMigrationTaskUpdatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.list_migration_task_updates_result.ListMigrationTaskUpdatesResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.list_migration_task_updates

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.list_migration_task_updates.async_list_migration_task_updates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.list_migration_task_updates_request.ListMigrationTaskUpdatesRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
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

    async def iter_list_migration_task_updates(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_migration_hub.types.migration_task_update.MigrationTaskUpdate]":
        _token = next_token
        while True:
            _response = await self.list_migration_task_updates(
                progress_update_stream,
                migration_task_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("migration_task_update_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_progress_update_streams(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_migration_hub.types.list_progress_update_streams_result.ListProgressUpdateStreamsResult":
        """<p>Lists progress update streams associated with the user account making this call.</p>

        Args:
            next_token: <p>If a <code>NextToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>
            max_results: <p>Filter to limit the maximum number of results to list per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.list_progress_update_streams_request.ListProgressUpdateStreamsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.list_progress_update_streams_result.ListProgressUpdateStreamsResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.list_progress_update_streams

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.list_progress_update_streams.async_list_progress_update_streams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.list_progress_update_streams_request.ListProgressUpdateStreamsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_progress_update_streams(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_migration_hub.types.progress_update_stream_summary.ProgressUpdateStreamSummary]":
        _token = next_token
        while True:
            _response = await self.list_progress_update_streams(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("progress_update_stream_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_source_resources(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results_source_resources.MaxResultsSourceResources"
        ] = None,
    ) -> "aws_sdk_migration_hub.types.list_source_resources_result.ListSourceResourcesResult":
        """<p>Lists all the source resource that are associated with the specified <code>MigrationTaskName</code> and <code>ProgressUpdateStream</code>.</p>

        Args:
            progress_update_stream: <p>The name of the progress-update stream, which is used for access control as well as a namespace for migration-task names that is implicitly linked to your AWS account. The progress-update stream must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.</p>
            migration_task_name: <p>A unique identifier that references the migration task. <i>Do not store confidential data in this field.</i> </p>
            next_token: <p>If <code>NextToken</code> was returned by a previous call, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. To retrieve the next page of results, specify the <code>NextToken</code> value that the previous call returned. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the value that you specify here for <code>MaxResults</code>, the response will include a token that you can use to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.list_source_resources_request.ListSourceResourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.list_source_resources_result.ListSourceResourcesResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.list_source_resources

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.list_source_resources.async_list_source_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.list_source_resources_request.ListSourceResourcesRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
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

    async def iter_list_source_resources(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        next_token: Optional["aws_sdk_migration_hub.types.token.Token"] = None,
        max_results: Optional[
            "aws_sdk_migration_hub.types.max_results_source_resources.MaxResultsSourceResources"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_migration_hub.types.source_resource.SourceResource]":
        _token = next_token
        while True:
            _response = await self.list_source_resources(
                progress_update_stream,
                migration_task_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("source_resource_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def notify_application_state(
        self,
        application_id: "aws_sdk_migration_hub.types.application_id.ApplicationId",
        status: "aws_sdk_migration_hub.types.application_status.ApplicationStatus",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        update_date_time: Optional[
            "aws_sdk_migration_hub.types.update_date_time.UpdateDateTime"
        ] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.notify_application_state_result.NotifyApplicationStateResult":
        """<p>Sets the migration state of an application. For a given application identified by the value passed to <code>ApplicationId</code>, its status is set or updated by passing one of three values to <code>Status</code>: <code>NOT_STARTED | IN_PROGRESS | COMPLETED</code>.</p>

        Args:
            application_id: <p>The configurationId in Application Discovery Service that uniquely identifies the grouped application.</p>
            status: <p>Status of the application - Not Started, In-Progress, Complete.</p>
            update_date_time: <p>The timestamp when the application state changed.</p>
            dry_run: <p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.notify_application_state_request.NotifyApplicationStateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.notify_application_state_result.NotifyApplicationStateResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.notify_application_state

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.notify_application_state.async_notify_application_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.notify_application_state_request.NotifyApplicationStateRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["status"] = status
        if update_date_time is not None:
            input_["update_date_time"] = update_date_time
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def notify_migration_task_state(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        task: "aws_sdk_migration_hub.types.task.Task",
        update_date_time: "aws_sdk_migration_hub.types.update_date_time.UpdateDateTime",
        next_update_seconds: "aws_sdk_migration_hub.types.next_update_seconds.NextUpdateSeconds",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.notify_migration_task_state_result.NotifyMigrationTaskStateResult":
        """<p>Notifies Migration Hub of the current status, progress, or other detail regarding a migration task. This API has the following traits:</p> <ul> <li> <p>Migration tools will call the <code>NotifyMigrationTaskState</code> API to share the latest progress and status.</p> </li> <li> <p> <code>MigrationTaskName</code> is used for addressing updates to the correct target.</p> </li> <li> <p> <code>ProgressUpdateStream</code> is used for access control and to provide a namespace for each migration tool.</p> </li> </ul>

        Args:
            progress_update_stream: <p>The name of the ProgressUpdateStream. </p>
            migration_task_name: <p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>
            task: <p>Information about the task's progress and status.</p>
            update_date_time: <p>The timestamp when the task was gathered.</p>
            next_update_seconds: <p>Number of seconds after the UpdateDateTime within which the Migration Hub can expect an update. If Migration Hub does not receive an update within the specified interval, then the migration task will be considered stale.</p>
            dry_run: <p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.notify_migration_task_state_request.NotifyMigrationTaskStateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.notify_migration_task_state_result.NotifyMigrationTaskStateResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.notify_migration_task_state

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.notify_migration_task_state.async_notify_migration_task_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.notify_migration_task_state_request.NotifyMigrationTaskStateRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
        input_["task"] = task
        input_["update_date_time"] = update_date_time
        input_["next_update_seconds"] = next_update_seconds
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_resource_attributes(
        self,
        progress_update_stream: "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream",
        migration_task_name: "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName",
        resource_attribute_list: "aws_sdk_migration_hub.types.resource_attribute_list.ResourceAttributeList",
        *,
        config_overrides: Optional[AsyncMigrationHubClientConfig] = None,
        dry_run: Optional["aws_sdk_migration_hub.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_migration_hub.types.put_resource_attributes_result.PutResourceAttributesResult":
        r"""<p>Provides identifying details of the resource being migrated so that it can be associated in the Application Discovery Service repository. This association occurs asynchronously after <code>PutResourceAttributes</code> returns.</p> <important> <ul> <li> <p>Keep in mind that subsequent calls to PutResourceAttributes will override previously stored attributes. For example, if it is first called with a MAC address, but later, it is desired to <i>add</i> an IP address, it will then be required to call it with <i>both</i> the IP and MAC addresses to prevent overriding the MAC address.</p> </li> <li> <p>Note the instructions regarding the special use case of the <a href=\"https://docs.aws.amazon.com/migrationhub/latest/ug/API_PutResourceAttributes.html#migrationhub-PutResourceAttributes-request-ResourceAttributeList\"> <code>ResourceAttributeList</code> </a> parameter when specifying any \"VM\" related value.</p> </li> </ul> </important> <note> <p>Because this is an asynchronous call, it will always return 200, whether an association occurs or not. To confirm if an association was found based on the provided details, call <code>ListDiscoveredResources</code>.</p> </note>

        Args:
            progress_update_stream: <p>The name of the ProgressUpdateStream. </p>
            migration_task_name: <p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>
            resource_attribute_list: <p>Information about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service repository.</p> <note> <p>Takes the object array of <code>ResourceAttribute</code> where the <code>Type</code> field is reserved for the following values: <code>IPV4_ADDRESS | IPV6_ADDRESS | MAC_ADDRESS | FQDN | VM_MANAGER_ID | VM_MANAGED_OBJECT_REFERENCE | VM_NAME | VM_PATH | BIOS_ID | MOTHERBOARD_SERIAL_NUMBER</code> where the identifying value can be a string up to 256 characters.</p> </note> <important> <ul> <li> <p>If any \"VM\" related value is set for a <code>ResourceAttribute</code> object, it is required that <code>VM_MANAGER_ID</code>, as a minimum, is always set. If <code>VM_MANAGER_ID</code> is not set, then all \"VM\" fields will be discarded and \"VM\" fields will not be used for matching the migration task to a server in Application Discovery Service repository. See the <a href=\"https://docs.aws.amazon.com/migrationhub/latest/ug/API_PutResourceAttributes.html#API_PutResourceAttributes_Examples\">Example</a> section below for a use case of specifying \"VM\" related values.</p> </li> <li> <p> If a server you are trying to match has multiple IP or MAC addresses, you should provide as many as you know in separate type/value pairs passed to the <code>ResourceAttributeList</code> parameter to maximize the chances of matching.</p> </li> </ul> </important>
            dry_run: <p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_migration_hub.types.put_resource_attributes_request.PutResourceAttributesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_migration_hub.types.put_resource_attributes_result.PutResourceAttributesResult"
        ]:
            import aws_sdk_migration_hub._operations.aws_migration_hub.put_resource_attributes

            (
                output,
                http_response,
            ) = await aws_sdk_migration_hub._operations.aws_migration_hub.put_resource_attributes.async_put_resource_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migration_hub.types.put_resource_attributes_request.PutResourceAttributesRequest = {}  # type: ignore[typeddict-item]
        input_["progress_update_stream"] = progress_update_stream
        input_["migration_task_name"] = migration_task_name
        input_["resource_attribute_list"] = resource_attribute_list
        if dry_run is not None:
            input_["dry_run"] = dry_run

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
