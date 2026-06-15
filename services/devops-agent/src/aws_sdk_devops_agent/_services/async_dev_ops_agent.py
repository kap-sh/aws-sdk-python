"""Generated from Smithy shape ``com.amazonaws.devopsagent#DevOpsAgent``."""

import datetime
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_devops_agent._auth._signers
import aws_sdk_devops_agent._auth._sigv4
from aws_sdk_devops_agent._auth._identity import Credentials
from aws_sdk_devops_agent._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_devops_agent._auth._zapros_handler import AuthMiddleware
from aws_sdk_devops_agent._pagination import resolve_path as _resolve_path
from aws_sdk_devops_agent._resources.dev_ops_agent.agent_space_resource import (
    AsyncAgentSpaceResource,
)
from aws_sdk_devops_agent._resources.dev_ops_agent.private_connection_resource import (
    AsyncPrivateConnectionResource,
)
from aws_sdk_devops_agent._resources.dev_ops_agent.service_resource import (
    AsyncServiceResource,
)
from aws_sdk_devops_agent._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.asset
    import aws_sdk_devops_agent.types.asset_content
    import aws_sdk_devops_agent.types.asset_file_body
    import aws_sdk_devops_agent.types.asset_file_path
    import aws_sdk_devops_agent.types.asset_file_summary
    import aws_sdk_devops_agent.types.asset_id_list
    import aws_sdk_devops_agent.types.asset_type
    import aws_sdk_devops_agent.types.asset_type_summary
    import aws_sdk_devops_agent.types.asset_version_metadata
    import aws_sdk_devops_agent.types.backlog_task_description
    import aws_sdk_devops_agent.types.backlog_task_title
    import aws_sdk_devops_agent.types.chat_execution_id
    import aws_sdk_devops_agent.types.create_asset_file_request
    import aws_sdk_devops_agent.types.create_asset_file_response
    import aws_sdk_devops_agent.types.create_asset_request
    import aws_sdk_devops_agent.types.create_asset_response
    import aws_sdk_devops_agent.types.create_backlog_task_request
    import aws_sdk_devops_agent.types.create_backlog_task_response
    import aws_sdk_devops_agent.types.create_chat_request
    import aws_sdk_devops_agent.types.create_chat_response
    import aws_sdk_devops_agent.types.delete_asset_file_request
    import aws_sdk_devops_agent.types.delete_asset_file_response
    import aws_sdk_devops_agent.types.delete_asset_request
    import aws_sdk_devops_agent.types.delete_asset_response
    import aws_sdk_devops_agent.types.execution
    import aws_sdk_devops_agent.types.get_account_usage_input
    import aws_sdk_devops_agent.types.get_account_usage_output
    import aws_sdk_devops_agent.types.get_asset_content_request
    import aws_sdk_devops_agent.types.get_asset_content_response
    import aws_sdk_devops_agent.types.get_asset_file_request
    import aws_sdk_devops_agent.types.get_asset_file_response
    import aws_sdk_devops_agent.types.get_asset_request
    import aws_sdk_devops_agent.types.get_asset_response
    import aws_sdk_devops_agent.types.get_backlog_task_request
    import aws_sdk_devops_agent.types.get_backlog_task_response
    import aws_sdk_devops_agent.types.get_recommendation_request
    import aws_sdk_devops_agent.types.get_recommendation_response
    import aws_sdk_devops_agent.types.goal
    import aws_sdk_devops_agent.types.goal_schedule_input
    import aws_sdk_devops_agent.types.goal_status
    import aws_sdk_devops_agent.types.goal_type
    import aws_sdk_devops_agent.types.journal_record
    import aws_sdk_devops_agent.types.list_asset_files_request
    import aws_sdk_devops_agent.types.list_asset_files_response
    import aws_sdk_devops_agent.types.list_asset_types_request
    import aws_sdk_devops_agent.types.list_asset_types_response
    import aws_sdk_devops_agent.types.list_asset_versions_request
    import aws_sdk_devops_agent.types.list_asset_versions_response
    import aws_sdk_devops_agent.types.list_assets_request
    import aws_sdk_devops_agent.types.list_assets_response
    import aws_sdk_devops_agent.types.list_backlog_tasks_request
    import aws_sdk_devops_agent.types.list_backlog_tasks_response
    import aws_sdk_devops_agent.types.list_chats_request
    import aws_sdk_devops_agent.types.list_chats_response
    import aws_sdk_devops_agent.types.list_executions_request
    import aws_sdk_devops_agent.types.list_executions_response
    import aws_sdk_devops_agent.types.list_goals_request
    import aws_sdk_devops_agent.types.list_goals_response
    import aws_sdk_devops_agent.types.list_journal_records_request
    import aws_sdk_devops_agent.types.list_journal_records_response
    import aws_sdk_devops_agent.types.list_pending_messages_request
    import aws_sdk_devops_agent.types.list_pending_messages_response
    import aws_sdk_devops_agent.types.list_recommendations_request
    import aws_sdk_devops_agent.types.list_recommendations_response
    import aws_sdk_devops_agent.types.list_tags_for_resource_request
    import aws_sdk_devops_agent.types.list_tags_for_resource_response
    import aws_sdk_devops_agent.types.message_content
    import aws_sdk_devops_agent.types.next_token
    import aws_sdk_devops_agent.types.order_type
    import aws_sdk_devops_agent.types.priority
    import aws_sdk_devops_agent.types.recommendation_priority
    import aws_sdk_devops_agent.types.recommendation_status
    import aws_sdk_devops_agent.types.reference_input
    import aws_sdk_devops_agent.types.resource_id
    import aws_sdk_devops_agent.types.send_message_context
    import aws_sdk_devops_agent.types.send_message_request
    import aws_sdk_devops_agent.types.send_message_response
    import aws_sdk_devops_agent.types.tag_key_list
    import aws_sdk_devops_agent.types.tag_resource_request
    import aws_sdk_devops_agent.types.tag_resource_response
    import aws_sdk_devops_agent.types.tags
    import aws_sdk_devops_agent.types.task
    import aws_sdk_devops_agent.types.task_filter
    import aws_sdk_devops_agent.types.task_sort_field
    import aws_sdk_devops_agent.types.task_sort_order
    import aws_sdk_devops_agent.types.task_status
    import aws_sdk_devops_agent.types.task_type
    import aws_sdk_devops_agent.types.untag_resource_request
    import aws_sdk_devops_agent.types.untag_resource_response
    import aws_sdk_devops_agent.types.update_asset_file_request
    import aws_sdk_devops_agent.types.update_asset_file_response
    import aws_sdk_devops_agent.types.update_asset_request
    import aws_sdk_devops_agent.types.update_asset_response
    import aws_sdk_devops_agent.types.update_backlog_task_request
    import aws_sdk_devops_agent.types.update_backlog_task_response
    import aws_sdk_devops_agent.types.update_goal_request
    import aws_sdk_devops_agent.types.update_goal_response
    import aws_sdk_devops_agent.types.update_recommendation_request
    import aws_sdk_devops_agent.types.update_recommendation_response
    import aws_sdk_devops_agent.types.user_type


class AsyncDevOpsAgentClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncDevOpsAgentClient:
    """A client for the ``DevOpsAgent`` service.

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
        self._config = AsyncDevOpsAgentClientConfig(
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
        self.private_connection_resource = AsyncPrivateConnectionResource(self)
        self.service_resource = AsyncServiceResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDevOpsAgentClientConfig = config_overrides or {}
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

    async def create_asset(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_type: "aws_sdk_devops_agent.types.asset_type.AssetType",
        content: "aws_sdk_devops_agent.types.asset_content.AssetContent",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        metadata: Optional[object] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_devops_agent.types.create_asset_response.CreateAssetResponse":
        """<p>Creates a new asset in the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space where the asset will be created</p>
            asset_type: <p>The type of asset to create</p>
            metadata: <p>The metadata describing this asset</p>
            content: <p>The content for the asset. Provide a single file or a zip bundle.</p>
            client_token: <p>A unique, case-sensitive identifier used for idempotent asset creation</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.create_asset_request.CreateAssetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.create_asset_response.CreateAssetResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.create_asset

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.create_asset.async_create_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.create_asset_request.CreateAssetRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_type"] = asset_type
        if metadata is not None:
            input_["metadata"] = metadata
        input_["content"] = content
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_asset_file(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        path: "aws_sdk_devops_agent.types.asset_file_path.AssetFilePath",
        content: "aws_sdk_devops_agent.types.asset_file_body.AssetFileBody",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        metadata: Optional[object] = None,
        client_token: Optional[str] = None,
    ) -> (
        "aws_sdk_devops_agent.types.create_asset_file_response.CreateAssetFileResponse"
    ):
        """<p>Creates a file in an asset</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset to create the file in</p>
            path: <p>The path of the file within the asset</p>
            content: <p>The content of the file to create</p>
            metadata: <p>Optional metadata describing this file</p>
            client_token: <p>A unique, case-sensitive identifier used for idempotent asset file creation</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.create_asset_file_request.CreateAssetFileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.create_asset_file_response.CreateAssetFileResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.create_asset_file

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.create_asset_file.async_create_asset_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.create_asset_file_request.CreateAssetFileRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_id"] = asset_id
        input_["path"] = path
        input_["content"] = content
        if metadata is not None:
            input_["metadata"] = metadata
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_backlog_task(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        task_type: "aws_sdk_devops_agent.types.task_type.TaskType",
        title: "aws_sdk_devops_agent.types.backlog_task_title.BacklogTaskTitle",
        priority: "aws_sdk_devops_agent.types.priority.Priority",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        reference: Optional[
            "aws_sdk_devops_agent.types.reference_input.ReferenceInput"
        ] = None,
        description: Optional[
            "aws_sdk_devops_agent.types.backlog_task_description.BacklogTaskDescription"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_devops_agent.types.create_backlog_task_response.CreateBacklogTaskResponse":
        """<p>Creates a new backlog task in the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space where the task will be created</p>
            reference: <p>Optional reference information for the task</p>
            task_type: <p>The type of task being created</p>
            title: <p>The title of the backlog task</p>
            description: <p>Optional detailed description of the task</p>
            priority: <p>The priority level of the task</p>
            client_token: <p>Client-provided token for idempotent operations</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.create_backlog_task_request.CreateBacklogTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.create_backlog_task_response.CreateBacklogTaskResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.create_backlog_task

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.create_backlog_task.async_create_backlog_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.create_backlog_task_request.CreateBacklogTaskRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if reference is not None:
            input_["reference"] = reference
        input_["task_type"] = task_type
        input_["title"] = title
        if description is not None:
            input_["description"] = description
        input_["priority"] = priority
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_chat(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        user_id: Optional["aws_sdk_devops_agent.types.resource_id.ResourceId"] = None,
        user_type: Optional["aws_sdk_devops_agent.types.user_type.UserType"] = None,
    ) -> "aws_sdk_devops_agent.types.create_chat_response.CreateChatResponse":
        """<p>Creates a new chat execution in the specified agent space</p>

        Args:
            user_id: <p>The user identifier for the chat. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.</p>
            user_type: <p>The authentication type of the user</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.create_chat_request.CreateChatRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.create_chat_response.CreateChatResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.create_chat

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.create_chat.async_create_chat(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.create_chat_request.CreateChatRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if user_id is not None:
            input_["user_id"] = user_id
        if user_type is not None:
            input_["user_type"] = user_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_asset(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.delete_asset_response.DeleteAssetResponse":
        """<p>Deletes an asset and all its files from the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset to delete</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.delete_asset_request.DeleteAssetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.delete_asset_response.DeleteAssetResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.delete_asset

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.delete_asset.async_delete_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.delete_asset_request.DeleteAssetRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_id"] = asset_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_asset_file(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        path: "aws_sdk_devops_agent.types.asset_file_path.AssetFilePath",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> (
        "aws_sdk_devops_agent.types.delete_asset_file_response.DeleteAssetFileResponse"
    ):
        """<p>Deletes a file from an asset</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset containing the file</p>
            path: <p>The path of the file within the asset to delete</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.delete_asset_file_request.DeleteAssetFileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.delete_asset_file_response.DeleteAssetFileResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.delete_asset_file

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.delete_asset_file.async_delete_asset_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.delete_asset_file_request.DeleteAssetFileRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_id"] = asset_id
        input_["path"] = path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_account_usage(
        self, *, config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None
    ) -> "aws_sdk_devops_agent.types.get_account_usage_output.GetAccountUsageOutput":
        """<p>Retrieves monthly account usage metrics and limits for the AWS account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.get_account_usage_input.GetAccountUsageInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.get_account_usage_output.GetAccountUsageOutput"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_account_usage

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.get_account_usage.async_get_account_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_account_usage_input.GetAccountUsageInput = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_asset(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_version: Optional[int] = None,
    ) -> "aws_sdk_devops_agent.types.get_asset_response.GetAssetResponse":
        """<p>Gets an asset from the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset to retrieve</p>
            asset_version: <p>The specific version of the asset to retrieve. If omitted, the latest version is returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.get_asset_request.GetAssetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.get_asset_response.GetAssetResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_asset

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.get_asset.async_get_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_asset_request.GetAssetRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_id"] = asset_id
        if asset_version is not None:
            input_["asset_version"] = asset_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_asset_content(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_version: Optional[int] = None,
    ) -> (
        "aws_sdk_devops_agent.types.get_asset_content_response.GetAssetContentResponse"
    ):
        """<p>Gets an asset's content as a zip bundle</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset</p>
            asset_version: <p>The specific asset version to export. If omitted, the latest version is returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.get_asset_content_request.GetAssetContentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.get_asset_content_response.GetAssetContentResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_asset_content

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.get_asset_content.async_get_asset_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_asset_content_request.GetAssetContentRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_id"] = asset_id
        if asset_version is not None:
            input_["asset_version"] = asset_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_asset_file(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        path: "aws_sdk_devops_agent.types.asset_file_path.AssetFilePath",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_version: Optional[int] = None,
    ) -> "aws_sdk_devops_agent.types.get_asset_file_response.GetAssetFileResponse":
        """<p>Gets a file from an asset</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset containing the file</p>
            path: <p>The path of the file within the asset to retrieve</p>
            asset_version: <p>The specific asset version to retrieve the file from. If omitted, the latest version is returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.get_asset_file_request.GetAssetFileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.get_asset_file_response.GetAssetFileResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_asset_file

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.get_asset_file.async_get_asset_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_asset_file_request.GetAssetFileRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_id"] = asset_id
        input_["path"] = path
        if asset_version is not None:
            input_["asset_version"] = asset_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_backlog_task(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        task_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.get_backlog_task_response.GetBacklogTaskResponse":
        """<p>Gets a backlog task for the specified agent space and task id</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the task</p>
            task_id: <p>The unique identifier of the task to retrieve</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.get_backlog_task_request.GetBacklogTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.get_backlog_task_response.GetBacklogTaskResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_backlog_task

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.get_backlog_task.async_get_backlog_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_backlog_task_request.GetBacklogTaskRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["task_id"] = task_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_recommendation(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        recommendation_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        recommendation_version: Optional[int] = None,
    ) -> "aws_sdk_devops_agent.types.get_recommendation_response.GetRecommendationResponse":
        """<p>Retrieves a specific recommendation by its ID</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the recommendation</p>
            recommendation_id: <p>The unique identifier for the recommendation to retrieve</p>
            recommendation_version: <p>Specific version of the recommendation to retrieve. If not specified, returns the latest version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.get_recommendation_request.GetRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.get_recommendation_response.GetRecommendationResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.get_recommendation

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.get_recommendation.async_get_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.get_recommendation_request.GetRecommendationRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["recommendation_id"] = recommendation_id
        if recommendation_version is not None:
            input_["recommendation_version"] = recommendation_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_asset_files(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_version: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_devops_agent.types.list_asset_files_response.ListAssetFilesResponse":
        """<p>Lists files in an asset</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset whose files to list</p>
            asset_version: <p>The specific asset version to list files from. If omitted, files from the latest version are returned.</p>
            next_token: <p>Pagination token from a previous response to retrieve the next page of results</p>
            max_results: <p>The maximum number of results to return in a single response</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_asset_files_request.ListAssetFilesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_asset_files_response.ListAssetFilesResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_asset_files

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_asset_files.async_list_asset_files(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_asset_files_request.ListAssetFilesRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_id"] = asset_id
        if asset_version is not None:
            input_["asset_version"] = asset_version
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

    async def iter_list_asset_files(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_version: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> (
        "AsyncIterator[aws_sdk_devops_agent.types.asset_file_summary.AssetFileSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_asset_files(
                agent_space_id,
                asset_id,
                config_overrides=config_overrides,
                asset_version=asset_version,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_assets(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_type: Optional["aws_sdk_devops_agent.types.asset_type.AssetType"] = None,
        updated_after: Optional[datetime.datetime] = None,
        updated_before: Optional[datetime.datetime] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_devops_agent.types.list_assets_response.ListAssetsResponse":
        """<p>Lists assets in the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space to list assets from</p>
            asset_type: <p>Filter results to only assets of this type</p>
            updated_after: <p>Filter results to only assets updated after this timestamp</p>
            updated_before: <p>Filter results to only assets updated before this timestamp</p>
            next_token: <p>Pagination token from a previous response to retrieve the next page of results</p>
            max_results: <p>The maximum number of results to return in a single response</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_assets_request.ListAssetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_assets_response.ListAssetsResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_assets

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_assets.async_list_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_assets_request.ListAssetsRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if asset_type is not None:
            input_["asset_type"] = asset_type
        if updated_after is not None:
            input_["updated_after"] = updated_after
        if updated_before is not None:
            input_["updated_before"] = updated_before
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

    async def iter_list_assets(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_type: Optional["aws_sdk_devops_agent.types.asset_type.AssetType"] = None,
        updated_after: Optional[datetime.datetime] = None,
        updated_before: Optional[datetime.datetime] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[aws_sdk_devops_agent.types.asset.Asset]":
        _token = next_token
        while True:
            _response = await self.list_assets(
                agent_space_id,
                config_overrides=config_overrides,
                asset_type=asset_type,
                updated_after=updated_after,
                updated_before=updated_before,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_types(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_devops_agent.types.list_asset_types_response.ListAssetTypesResponse":
        """<p>Lists the supported asset types</p>

        Args:
            next_token: <p>Pagination token from a previous response to retrieve the next page of results</p>
            max_results: <p>The maximum number of results to return in a single response</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_asset_types_request.ListAssetTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_asset_types_response.ListAssetTypesResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_asset_types

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_asset_types.async_list_asset_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_asset_types_request.ListAssetTypesRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_asset_types(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> (
        "AsyncIterator[aws_sdk_devops_agent.types.asset_type_summary.AssetTypeSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_asset_types(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_versions(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_devops_agent.types.list_asset_versions_response.ListAssetVersionsResponse":
        """<p>Lists versions of an asset in the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset whose versions to list</p>
            max_results: <p>The maximum number of results to return in a single response</p>
            next_token: <p>Pagination token from a previous response to retrieve the next page of results</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_asset_versions_request.ListAssetVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_asset_versions_response.ListAssetVersionsResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_asset_versions

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_asset_versions.async_list_asset_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_asset_versions_request.ListAssetVersionsRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_id"] = asset_id
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

    async def iter_list_asset_versions(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_devops_agent.types.asset_version_metadata.AssetVersionMetadata]":
        _token = next_token
        while True:
            _response = await self.list_asset_versions(
                agent_space_id,
                asset_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_backlog_tasks(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        filter: Optional["aws_sdk_devops_agent.types.task_filter.TaskFilter"] = None,
        limit: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        sort_field: Optional[
            "aws_sdk_devops_agent.types.task_sort_field.TaskSortField"
        ] = None,
        order: Optional[
            "aws_sdk_devops_agent.types.task_sort_order.TaskSortOrder"
        ] = None,
    ) -> "aws_sdk_devops_agent.types.list_backlog_tasks_response.ListBacklogTasksResponse":
        """<p>Lists backlog tasks in the specified agent space with optional filtering and sorting</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the tasks</p>
            filter: <p>Filter criteria to apply when listing tasks Filtering restrictions: - Each filter field list is limited to a single value - Filtering by Priority and Status at the same time when not filtering by Type is not permitted - Timestamp filters (createdAfter, createdBefore) can be combined with other filters when not sorting by priority</p>
            limit: <p>Maximum number of tasks to return in a single response (1-1000, default: 100)</p>
            next_token: <p>Token for retrieving the next page of results</p>
            sort_field: <p>Field to sort by Sorting restrictions: - Only sorting on createdAt is supported when using priority or status filters alone. - Sorting by priority is not supported when using Timestamp filters (createdAfter, createdBefore)</p>
            order: <p>Sort order for the tasks based on sortField (default: DESC)</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_backlog_tasks_request.ListBacklogTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_backlog_tasks_response.ListBacklogTasksResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_backlog_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_backlog_tasks.async_list_backlog_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_backlog_tasks_request.ListBacklogTasksRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if filter is not None:
            input_["filter"] = filter
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_field is not None:
            input_["sort_field"] = sort_field
        if order is not None:
            input_["order"] = order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_backlog_tasks(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        filter: Optional["aws_sdk_devops_agent.types.task_filter.TaskFilter"] = None,
        limit: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        sort_field: Optional[
            "aws_sdk_devops_agent.types.task_sort_field.TaskSortField"
        ] = None,
        order: Optional[
            "aws_sdk_devops_agent.types.task_sort_order.TaskSortOrder"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_devops_agent.types.task.Task]":
        _token = next_token
        while True:
            _response = await self.list_backlog_tasks(
                agent_space_id,
                config_overrides=config_overrides,
                filter=filter,
                limit=limit,
                next_token=_token,
                sort_field=sort_field,
                order=order,
            )
            _page = _resolve_path(_response, ("tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_chats(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        user_id: Optional["aws_sdk_devops_agent.types.resource_id.ResourceId"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_devops_agent.types.list_chats_response.ListChatsResponse":
        """<p>Retrieves a paginated list of the user's recent chat executions</p>

        Args:
            user_id: <p>The user identifier to list chats for. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.</p>
            max_results: <p>Maximum number of results to return</p>
            next_token: <p>Token for pagination</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_chats_request.ListChatsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_chats_response.ListChatsResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_chats

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_chats.async_list_chats(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_chats_request.ListChatsRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if user_id is not None:
            input_["user_id"] = user_id
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

    async def list_executions(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        task_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        limit: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_devops_agent.types.list_executions_response.ListExecutionsResponse":
        """<p>List executions</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space</p>
            task_id: <p>The unique identifier of the task whose executions to retrieve</p>
            limit: <p>Maximum number of executions to return</p>
            next_token: <p>Token for pagination to retrieve the next set of results</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_executions_request.ListExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_executions_response.ListExecutionsResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_executions

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_executions.async_list_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_executions_request.ListExecutionsRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["task_id"] = task_id
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_executions(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        task_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        limit: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_devops_agent.types.execution.Execution]":
        _token = next_token
        while True:
            _response = await self.list_executions(
                agent_space_id,
                task_id,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_goals(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        status: Optional["aws_sdk_devops_agent.types.goal_status.GoalStatus"] = None,
        goal_type: Optional["aws_sdk_devops_agent.types.goal_type.GoalType"] = None,
        limit: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_devops_agent.types.list_goals_response.ListGoalsResponse":
        """<p>Lists goals in the specified agent space with optional filtering</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space</p>
            status: <p>Filter goals by goal status</p>
            goal_type: <p>Filter goals by goal type</p>
            limit: <p>Maximum number of goals to return</p>
            next_token: <p>Pagination token for the next set of results</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_goals_request.ListGoalsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_goals_response.ListGoalsResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_goals

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_goals.async_list_goals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_goals_request.ListGoalsRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if status is not None:
            input_["status"] = status
        if goal_type is not None:
            input_["goal_type"] = goal_type
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_goals(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        status: Optional["aws_sdk_devops_agent.types.goal_status.GoalStatus"] = None,
        goal_type: Optional["aws_sdk_devops_agent.types.goal_type.GoalType"] = None,
        limit: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_devops_agent.types.goal.Goal]":
        _token = next_token
        while True:
            _response = await self.list_goals(
                agent_space_id,
                config_overrides=config_overrides,
                status=status,
                goal_type=goal_type,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("goals",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_journal_records(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        execution_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        limit: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        record_type: Optional[str] = None,
        order: Optional["aws_sdk_devops_agent.types.order_type.OrderType"] = None,
    ) -> "aws_sdk_devops_agent.types.list_journal_records_response.ListJournalRecordsResponse":
        """<p>List journal records for a specific execution</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the execution</p>
            execution_id: <p>The unique identifier of the execution whose journal records to retrieve</p>
            limit: <p>Maximum number of records to return in a single response (1-100, default: 100)</p>
            next_token: <p>Token for retrieving the next page of results</p>
            record_type: <p>Filter records by type (empty string returns all types)</p>
            order: <p>Sort order for the records based on timestamp (default: DESC)</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_journal_records_request.ListJournalRecordsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_journal_records_response.ListJournalRecordsResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_journal_records

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_journal_records.async_list_journal_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_journal_records_request.ListJournalRecordsRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["execution_id"] = execution_id
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if record_type is not None:
            input_["record_type"] = record_type
        if order is not None:
            input_["order"] = order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_journal_records(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        execution_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        limit: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
        record_type: Optional[str] = None,
        order: Optional["aws_sdk_devops_agent.types.order_type.OrderType"] = None,
    ) -> "AsyncIterator[aws_sdk_devops_agent.types.journal_record.JournalRecord]":
        _token = next_token
        while True:
            _response = await self.list_journal_records(
                agent_space_id,
                execution_id,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
                record_type=record_type,
                order=order,
            )
            _page = _resolve_path(_response, ("records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pending_messages(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        execution_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.list_pending_messages_response.ListPendingMessagesResponse":
        """<p>List pending messages for a specific execution.</p>

        Args:
            execution_id: <p>The unique identifier of the execution whose journal records to retrieve</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_pending_messages_request.ListPendingMessagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_pending_messages_response.ListPendingMessagesResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_pending_messages

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_pending_messages.async_list_pending_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_pending_messages_request.ListPendingMessagesRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["execution_id"] = execution_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_recommendations(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        task_id: Optional["aws_sdk_devops_agent.types.resource_id.ResourceId"] = None,
        goal_id: Optional["aws_sdk_devops_agent.types.resource_id.ResourceId"] = None,
        status: Optional[
            "aws_sdk_devops_agent.types.recommendation_status.RecommendationStatus"
        ] = None,
        priority: Optional[
            "aws_sdk_devops_agent.types.recommendation_priority.RecommendationPriority"
        ] = None,
        limit: Optional[int] = None,
        next_token: Optional["aws_sdk_devops_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_devops_agent.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>Lists recommendations for the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the recommendations</p>
            task_id: <p>Optional task ID to filter recommendations by specific task</p>
            goal_id: <p>Optional goal ID to filter recommendations by specific goal</p>
            status: <p>Optional status to filter recommendations by their current status</p>
            priority: <p>Optional priority to filter recommendations by priority level</p>
            limit: <p>Maximum number of recommendations to return in a single response</p>
            next_token: <p>Token for retrieving the next page of results</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_recommendations

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_recommendations.async_list_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_recommendations_request.ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        if task_id is not None:
            input_["task_id"] = task_id
        if goal_id is not None:
            input_["goal_id"] = goal_id
        if status is not None:
            input_["status"] = status
        if priority is not None:
            input_["priority"] = priority
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for the specified AWS DevOps Agent resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_message(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        execution_id: "aws_sdk_devops_agent.types.chat_execution_id.ChatExecutionId",
        content: "aws_sdk_devops_agent.types.message_content.MessageContent",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        context: Optional[
            "aws_sdk_devops_agent.types.send_message_context.SendMessageContext"
        ] = None,
        user_id: Optional["aws_sdk_devops_agent.types.resource_id.ResourceId"] = None,
        asset_ids: Optional[
            "aws_sdk_devops_agent.types.asset_id_list.AssetIdList"
        ] = None,
    ) -> "aws_sdk_devops_agent.types.send_message_response.SendMessageResponse":
        """<p>Sends a chat message and streams the response for the specified agent space execution</p>

        Args:
            agent_space_id: <p>The agent space identifier</p>
            execution_id: <p>The execution identifier for the chat session</p>
            content: <p>The user message content</p>
            context: <p>Optional context for the message</p>
            user_id: <p>User identifier. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.</p>
            asset_ids: <p>Optional list of asset identifiers to attach to the message</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.send_message_request.SendMessageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.send_message_response.SendMessageResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.send_message

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.send_message.async_send_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.send_message_request.SendMessageRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["execution_id"] = execution_id
        input_["content"] = content
        if context is not None:
            input_["context"] = context
        if user_id is not None:
            input_["user_id"] = user_id
        if asset_ids is not None:
            input_["asset_ids"] = asset_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "aws_sdk_devops_agent.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or overwrites tags for the specified AWS DevOps Agent resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to tag.</p>
            tags: <p>Tags to add to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: str,
        tag_keys: "aws_sdk_devops_agent.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "aws_sdk_devops_agent.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the specified AWS DevOps Agent resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to untag.</p>
            tag_keys: <p>Tag keys to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_asset(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        metadata: Optional[object] = None,
        content: Optional[
            "aws_sdk_devops_agent.types.asset_content.AssetContent"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_devops_agent.types.update_asset_response.UpdateAssetResponse":
        """<p>Updates an asset in the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset to update</p>
            metadata: <p>Metadata fields to update. Only the fields present in this document are updated. Omitted fields retain their current values.</p>
            content: <p>Optional content to set or replace. A single file adds or replaces one file; a zip replaces all files.</p>
            client_token: <p>A unique, case-sensitive identifier used for idempotent asset update</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.update_asset_request.UpdateAssetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.update_asset_response.UpdateAssetResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_asset

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.update_asset.async_update_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_asset_request.UpdateAssetRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_id"] = asset_id
        if metadata is not None:
            input_["metadata"] = metadata
        if content is not None:
            input_["content"] = content
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_asset_file(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        path: "aws_sdk_devops_agent.types.asset_file_path.AssetFilePath",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        content: Optional[
            "aws_sdk_devops_agent.types.asset_file_body.AssetFileBody"
        ] = None,
        metadata: Optional[object] = None,
        client_token: Optional[str] = None,
    ) -> (
        "aws_sdk_devops_agent.types.update_asset_file_response.UpdateAssetFileResponse"
    ):
        """<p>Updates a file in an asset</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset containing the file</p>
            path: <p>The path of the file within the asset to update</p>
            content: <p>Updated file content. If omitted, the existing content is unchanged.</p>
            metadata: <p>Metadata fields to update. Only the fields present in this document are updated. Omitted fields retain their current values.</p>
            client_token: <p>A unique, case-sensitive identifier used for idempotent asset file update</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.update_asset_file_request.UpdateAssetFileRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.update_asset_file_response.UpdateAssetFileResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_asset_file

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.update_asset_file.async_update_asset_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_asset_file_request.UpdateAssetFileRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["asset_id"] = asset_id
        input_["path"] = path
        if content is not None:
            input_["content"] = content
        if metadata is not None:
            input_["metadata"] = metadata
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_backlog_task(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        task_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        task_status: Optional[
            "aws_sdk_devops_agent.types.task_status.TaskStatus"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_devops_agent.types.update_backlog_task_response.UpdateBacklogTaskResponse":
        """<p>Update an existing backlog task.</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the task</p>
            task_id: <p>The unique identifier of the task to update</p>
            task_status: <p>Updated task status</p>
            client_token: <p>Client-provided token for idempotent operations</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.update_backlog_task_request.UpdateBacklogTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.update_backlog_task_response.UpdateBacklogTaskResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_backlog_task

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.update_backlog_task.async_update_backlog_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_backlog_task_request.UpdateBacklogTaskRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["task_id"] = task_id
        if task_status is not None:
            input_["task_status"] = task_status
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_goal(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        goal_id: str,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        evaluation_schedule: Optional[
            "aws_sdk_devops_agent.types.goal_schedule_input.GoalScheduleInput"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_devops_agent.types.update_goal_response.UpdateGoalResponse":
        """<p>Update an existing goal</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the goal</p>
            goal_id: <p>The unique identifier of the goal to update</p>
            evaluation_schedule: <p>Update goal schedule state</p>
            client_token: <p>Client-provided token for idempotent operations</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.update_goal_request.UpdateGoalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.update_goal_response.UpdateGoalResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_goal

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.update_goal.async_update_goal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_goal_request.UpdateGoalRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["goal_id"] = goal_id
        if evaluation_schedule is not None:
            input_["evaluation_schedule"] = evaluation_schedule
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_recommendation(
        self,
        agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId",
        recommendation_id: "aws_sdk_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        status: Optional[
            "aws_sdk_devops_agent.types.recommendation_status.RecommendationStatus"
        ] = None,
        additional_context: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_devops_agent.types.update_recommendation_response.UpdateRecommendationResponse":
        """<p>Updates an existing recommendation with new content, status, or metadata</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the recommendation</p>
            recommendation_id: <p>The unique identifier for the recommendation to update</p>
            status: <p>Current status of the recommendation</p>
            additional_context: <p>Additional context for recommendation</p>
            client_token: <p>A unique token that ensures idempotency of the request</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_devops_agent.types.update_recommendation_request.UpdateRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_devops_agent.types.update_recommendation_response.UpdateRecommendationResponse"
        ]:
            import aws_sdk_devops_agent._operations.dev_ops_agent.update_recommendation

            (
                output,
                http_response,
            ) = await aws_sdk_devops_agent._operations.dev_ops_agent.update_recommendation.async_update_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_devops_agent.types.update_recommendation_request.UpdateRecommendationRequest = {}  # type: ignore[typeddict-item]
        input_["agent_space_id"] = agent_space_id
        input_["recommendation_id"] = recommendation_id
        if status is not None:
            input_["status"] = status
        if additional_context is not None:
            input_["additional_context"] = additional_context
        if client_token is not None:
            input_["client_token"] = client_token

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
