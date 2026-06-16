"""Generated from Smithy shape ``com.amazonaws.qbusiness#ExpertQ``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_qbusiness._auth._signers
import aws_sdk_qbusiness._auth._sigv4
from aws_sdk_qbusiness._auth._identity import Credentials
from aws_sdk_qbusiness._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_qbusiness._auth._zapros_handler import AuthMiddleware
from aws_sdk_qbusiness._iter import ensure_async_iterator
from aws_sdk_qbusiness._pagination import resolve_path as _resolve_path
from aws_sdk_qbusiness._resources.expert_q.application_resource import (
    AsyncApplicationResource,
)
from aws_sdk_qbusiness._services._aws_config import aaws_config
from aws_sdk_qbusiness._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_execution
    import aws_sdk_qbusiness.types.action_summary
    import aws_sdk_qbusiness.types.amazon_resource_name
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.associate_permission_request
    import aws_sdk_qbusiness.types.associate_permission_response
    import aws_sdk_qbusiness.types.attachment
    import aws_sdk_qbusiness.types.attachment_id
    import aws_sdk_qbusiness.types.attachments_input
    import aws_sdk_qbusiness.types.attribute_filter
    import aws_sdk_qbusiness.types.auth_challenge_response
    import aws_sdk_qbusiness.types.batch_delete_document_request
    import aws_sdk_qbusiness.types.batch_delete_document_response
    import aws_sdk_qbusiness.types.batch_put_document_request
    import aws_sdk_qbusiness.types.batch_put_document_response
    import aws_sdk_qbusiness.types.blocked_phrases_configuration_update
    import aws_sdk_qbusiness.types.cancel_subscription_request
    import aws_sdk_qbusiness.types.cancel_subscription_response
    import aws_sdk_qbusiness.types.chat_input
    import aws_sdk_qbusiness.types.chat_input_stream
    import aws_sdk_qbusiness.types.chat_mode
    import aws_sdk_qbusiness.types.chat_mode_configuration
    import aws_sdk_qbusiness.types.chat_output
    import aws_sdk_qbusiness.types.chat_response_configuration
    import aws_sdk_qbusiness.types.chat_response_configuration_id
    import aws_sdk_qbusiness.types.chat_sync_input
    import aws_sdk_qbusiness.types.chat_sync_output
    import aws_sdk_qbusiness.types.check_document_access_request
    import aws_sdk_qbusiness.types.check_document_access_response
    import aws_sdk_qbusiness.types.client_token
    import aws_sdk_qbusiness.types.content_source
    import aws_sdk_qbusiness.types.conversation
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.create_anonymous_web_experience_url_request
    import aws_sdk_qbusiness.types.create_anonymous_web_experience_url_response
    import aws_sdk_qbusiness.types.create_chat_response_configuration_request
    import aws_sdk_qbusiness.types.create_chat_response_configuration_response
    import aws_sdk_qbusiness.types.create_subscription_request
    import aws_sdk_qbusiness.types.create_subscription_response
    import aws_sdk_qbusiness.types.create_user_request
    import aws_sdk_qbusiness.types.create_user_response
    import aws_sdk_qbusiness.types.creator_mode_configuration
    import aws_sdk_qbusiness.types.data_source_id
    import aws_sdk_qbusiness.types.data_source_ids
    import aws_sdk_qbusiness.types.data_source_sync_job
    import aws_sdk_qbusiness.types.data_source_sync_job_status
    import aws_sdk_qbusiness.types.delete_attachment_request
    import aws_sdk_qbusiness.types.delete_attachment_response
    import aws_sdk_qbusiness.types.delete_chat_controls_configuration_request
    import aws_sdk_qbusiness.types.delete_chat_controls_configuration_response
    import aws_sdk_qbusiness.types.delete_chat_response_configuration_request
    import aws_sdk_qbusiness.types.delete_chat_response_configuration_response
    import aws_sdk_qbusiness.types.delete_conversation_request
    import aws_sdk_qbusiness.types.delete_conversation_response
    import aws_sdk_qbusiness.types.delete_documents
    import aws_sdk_qbusiness.types.delete_group_request
    import aws_sdk_qbusiness.types.delete_group_response
    import aws_sdk_qbusiness.types.delete_user_request
    import aws_sdk_qbusiness.types.delete_user_response
    import aws_sdk_qbusiness.types.disassociate_permission_request
    import aws_sdk_qbusiness.types.disassociate_permission_response
    import aws_sdk_qbusiness.types.display_name
    import aws_sdk_qbusiness.types.document_details
    import aws_sdk_qbusiness.types.document_id
    import aws_sdk_qbusiness.types.documents
    import aws_sdk_qbusiness.types.execution_id
    import aws_sdk_qbusiness.types.get_chat_controls_configuration_request
    import aws_sdk_qbusiness.types.get_chat_controls_configuration_response
    import aws_sdk_qbusiness.types.get_chat_response_configuration_request
    import aws_sdk_qbusiness.types.get_chat_response_configuration_response
    import aws_sdk_qbusiness.types.get_document_content_request
    import aws_sdk_qbusiness.types.get_document_content_response
    import aws_sdk_qbusiness.types.get_group_request
    import aws_sdk_qbusiness.types.get_group_response
    import aws_sdk_qbusiness.types.get_media_request
    import aws_sdk_qbusiness.types.get_media_response
    import aws_sdk_qbusiness.types.get_policy_request
    import aws_sdk_qbusiness.types.get_policy_response
    import aws_sdk_qbusiness.types.get_user_request
    import aws_sdk_qbusiness.types.get_user_response
    import aws_sdk_qbusiness.types.group_members
    import aws_sdk_qbusiness.types.group_name
    import aws_sdk_qbusiness.types.group_summary
    import aws_sdk_qbusiness.types.hallucination_reduction_configuration
    import aws_sdk_qbusiness.types.index_id
    import aws_sdk_qbusiness.types.integer
    import aws_sdk_qbusiness.types.list_attachments_request
    import aws_sdk_qbusiness.types.list_attachments_response
    import aws_sdk_qbusiness.types.list_chat_response_configurations_request
    import aws_sdk_qbusiness.types.list_chat_response_configurations_response
    import aws_sdk_qbusiness.types.list_conversations_request
    import aws_sdk_qbusiness.types.list_conversations_response
    import aws_sdk_qbusiness.types.list_data_source_sync_jobs_request
    import aws_sdk_qbusiness.types.list_data_source_sync_jobs_response
    import aws_sdk_qbusiness.types.list_documents_request
    import aws_sdk_qbusiness.types.list_documents_response
    import aws_sdk_qbusiness.types.list_groups_request
    import aws_sdk_qbusiness.types.list_groups_response
    import aws_sdk_qbusiness.types.list_messages_request
    import aws_sdk_qbusiness.types.list_messages_response
    import aws_sdk_qbusiness.types.list_plugin_actions_request
    import aws_sdk_qbusiness.types.list_plugin_actions_response
    import aws_sdk_qbusiness.types.list_plugin_type_actions_request
    import aws_sdk_qbusiness.types.list_plugin_type_actions_response
    import aws_sdk_qbusiness.types.list_plugin_type_metadata_request
    import aws_sdk_qbusiness.types.list_plugin_type_metadata_response
    import aws_sdk_qbusiness.types.list_subscriptions_request
    import aws_sdk_qbusiness.types.list_subscriptions_response
    import aws_sdk_qbusiness.types.list_tags_for_resource_request
    import aws_sdk_qbusiness.types.list_tags_for_resource_response
    import aws_sdk_qbusiness.types.max_results
    import aws_sdk_qbusiness.types.max_results_integer_for_get_topic_configurations
    import aws_sdk_qbusiness.types.max_results_integer_for_list_attachments
    import aws_sdk_qbusiness.types.max_results_integer_for_list_conversations
    import aws_sdk_qbusiness.types.max_results_integer_for_list_data_sources_sync_jobs
    import aws_sdk_qbusiness.types.max_results_integer_for_list_documents
    import aws_sdk_qbusiness.types.max_results_integer_for_list_groups_request
    import aws_sdk_qbusiness.types.max_results_integer_for_list_messages
    import aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_actions
    import aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_type_actions
    import aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_type_metadata
    import aws_sdk_qbusiness.types.max_results_integer_for_list_subscriptions
    import aws_sdk_qbusiness.types.media_id
    import aws_sdk_qbusiness.types.membership_type
    import aws_sdk_qbusiness.types.message
    import aws_sdk_qbusiness.types.message_id
    import aws_sdk_qbusiness.types.message_usefulness_feedback
    import aws_sdk_qbusiness.types.next_token
    import aws_sdk_qbusiness.types.orchestration_configuration
    import aws_sdk_qbusiness.types.output_format
    import aws_sdk_qbusiness.types.permission_conditions
    import aws_sdk_qbusiness.types.plugin_id
    import aws_sdk_qbusiness.types.plugin_type
    import aws_sdk_qbusiness.types.plugin_type_metadata_summary
    import aws_sdk_qbusiness.types.principal_role_arn
    import aws_sdk_qbusiness.types.put_feedback_request
    import aws_sdk_qbusiness.types.put_group_request
    import aws_sdk_qbusiness.types.put_group_response
    import aws_sdk_qbusiness.types.q_iam_actions
    import aws_sdk_qbusiness.types.query_text
    import aws_sdk_qbusiness.types.relevant_content
    import aws_sdk_qbusiness.types.response_configurations
    import aws_sdk_qbusiness.types.response_scope
    import aws_sdk_qbusiness.types.role_arn
    import aws_sdk_qbusiness.types.search_relevant_content_request
    import aws_sdk_qbusiness.types.search_relevant_content_response
    import aws_sdk_qbusiness.types.session_duration_in_minutes
    import aws_sdk_qbusiness.types.start_data_source_sync_job_request
    import aws_sdk_qbusiness.types.start_data_source_sync_job_response
    import aws_sdk_qbusiness.types.statement_id
    import aws_sdk_qbusiness.types.stop_data_source_sync_job_request
    import aws_sdk_qbusiness.types.stop_data_source_sync_job_response
    import aws_sdk_qbusiness.types.string
    import aws_sdk_qbusiness.types.subscription
    import aws_sdk_qbusiness.types.subscription_id
    import aws_sdk_qbusiness.types.subscription_principal
    import aws_sdk_qbusiness.types.subscription_type
    import aws_sdk_qbusiness.types.system_message_id
    import aws_sdk_qbusiness.types.tag_keys
    import aws_sdk_qbusiness.types.tag_resource_request
    import aws_sdk_qbusiness.types.tag_resource_response
    import aws_sdk_qbusiness.types.tags
    import aws_sdk_qbusiness.types.timestamp
    import aws_sdk_qbusiness.types.topic_configuration
    import aws_sdk_qbusiness.types.topic_configurations
    import aws_sdk_qbusiness.types.untag_resource_request
    import aws_sdk_qbusiness.types.untag_resource_response
    import aws_sdk_qbusiness.types.update_chat_controls_configuration_request
    import aws_sdk_qbusiness.types.update_chat_controls_configuration_response
    import aws_sdk_qbusiness.types.update_chat_response_configuration_request
    import aws_sdk_qbusiness.types.update_chat_response_configuration_response
    import aws_sdk_qbusiness.types.update_subscription_request
    import aws_sdk_qbusiness.types.update_subscription_response
    import aws_sdk_qbusiness.types.update_user_request
    import aws_sdk_qbusiness.types.update_user_response
    import aws_sdk_qbusiness.types.user_aliases
    import aws_sdk_qbusiness.types.user_groups
    import aws_sdk_qbusiness.types.user_id
    import aws_sdk_qbusiness.types.user_message
    import aws_sdk_qbusiness.types.web_experience_id


class AsyncQBusinessClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncQBusinessClient:
    """A client for the ``QBusiness`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
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
        self._config = AsyncQBusinessClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.application_resource = AsyncApplicationResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncQBusinessClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncQBusinessClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_permission(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        statement_id: "aws_sdk_qbusiness.types.statement_id.StatementId",
        actions: "aws_sdk_qbusiness.types.q_iam_actions.QIamActions",
        principal: "aws_sdk_qbusiness.types.principal_role_arn.PrincipalRoleArn",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        conditions: Optional[
            "aws_sdk_qbusiness.types.permission_conditions.PermissionConditions"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.associate_permission_response.AssociatePermissionResponse":
        """<p>Adds or updates a permission policy for a Amazon Q Business application, allowing cross-account access for an ISV. This operation creates a new policy statement for the specified Amazon Q Business application. The policy statement defines the IAM actions that the ISV is allowed to perform on the Amazon Q Business application's resources.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>
            statement_id: <p>A unique identifier for the policy statement.</p>
            actions: <p>The list of Amazon Q Business actions that the ISV is allowed to perform.</p>
            conditions: <p>The conditions that restrict when the permission is effective. These conditions can be used to limit the permission based on specific attributes of the request.</p>
            principal: <p>The Amazon Resource Name of the IAM role for the ISV that is being granted permission.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.associate_permission_request.AssociatePermissionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.associate_permission_response.AssociatePermissionResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.associate_permission

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.associate_permission.async_associate_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.associate_permission_request.AssociatePermissionRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["statement_id"] = statement_id
        input_["actions"] = actions
        if conditions is not None:
            input_["conditions"] = conditions
        input_["principal"] = principal

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_delete_document(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        documents: "aws_sdk_qbusiness.types.delete_documents.DeleteDocuments",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        data_source_sync_id: Optional[
            "aws_sdk_qbusiness.types.execution_id.ExecutionId"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.batch_delete_document_response.BatchDeleteDocumentResponse":
        """<p>Asynchronously deletes one or more documents added using the <code>BatchPutDocument</code> API from an Amazon Q Business index.</p> <p>You can see the progress of the deletion, and any error messages related to the process, by using CloudWatch.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>
            index_id: <p>The identifier of the Amazon Q Business index that contains the documents to delete.</p>
            documents: <p>Documents deleted from the Amazon Q Business index.</p>
            data_source_sync_id: <p>The identifier of the data source sync during which the documents were deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.batch_delete_document_request.BatchDeleteDocumentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.batch_delete_document_response.BatchDeleteDocumentResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.batch_delete_document

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.batch_delete_document.async_batch_delete_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.batch_delete_document_request.BatchDeleteDocumentRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["index_id"] = index_id
        input_["documents"] = documents
        if data_source_sync_id is not None:
            input_["data_source_sync_id"] = data_source_sync_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_put_document(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        documents: "aws_sdk_qbusiness.types.documents.Documents",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        role_arn: Optional["aws_sdk_qbusiness.types.role_arn.RoleArn"] = None,
        data_source_sync_id: Optional[
            "aws_sdk_qbusiness.types.execution_id.ExecutionId"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.batch_put_document_response.BatchPutDocumentResponse":
        """<p>Adds one or more documents to an Amazon Q Business index.</p> <p>You use this API to:</p> <ul> <li> <p>ingest your structured and unstructured documents and documents stored in an Amazon S3 bucket into an Amazon Q Business index.</p> </li> <li> <p>add custom attributes to documents in an Amazon Q Business index.</p> </li> <li> <p>attach an access control list to the documents added to an Amazon Q Business index.</p> </li> </ul> <p>You can see the progress of the deletion, and any error messages related to the process, by using CloudWatch.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>
            index_id: <p>The identifier of the Amazon Q Business index to add the documents to. </p>
            documents: <p>One or more documents to add to the index.</p> <important> <p>Ensure that the name of your document doesn't contain any confidential information. Amazon Q Business returns document names in chat responses and citations when relevant.</p> </important>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket.</p>
            data_source_sync_id: <p>The identifier of the data source sync during which the documents were added.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.batch_put_document_request.BatchPutDocumentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.batch_put_document_response.BatchPutDocumentResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.batch_put_document

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.batch_put_document.async_batch_put_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.batch_put_document_request.BatchPutDocumentRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["index_id"] = index_id
        input_["documents"] = documents
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if data_source_sync_id is not None:
            input_["data_source_sync_id"] = data_source_sync_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_subscription(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        subscription_id: "aws_sdk_qbusiness.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.cancel_subscription_response.CancelSubscriptionResponse":
        """<p>Unsubscribes a user or a group from their pricing tier in an Amazon Q Business application. An unsubscribed user or group loses all Amazon Q Business feature access at the start of next month. </p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application for which the subscription is being cancelled.</p>
            subscription_id: <p>The identifier of the Amazon Q Business subscription being cancelled.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.cancel_subscription_request.CancelSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.cancel_subscription_response.CancelSubscriptionResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.cancel_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.cancel_subscription.async_cancel_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.cancel_subscription_request.CancelSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["subscription_id"] = subscription_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def chat(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
        user_groups: Optional["aws_sdk_qbusiness.types.user_groups.UserGroups"] = None,
        conversation_id: Optional[
            "aws_sdk_qbusiness.types.conversation_id.ConversationId"
        ] = None,
        parent_message_id: Optional[
            "aws_sdk_qbusiness.types.message_id.MessageId"
        ] = None,
        client_token: Optional[
            "aws_sdk_qbusiness.types.client_token.ClientToken"
        ] = None,
        input_stream: Optional[AsyncIterator[bytes] | bytes] = None,
    ) -> "aws_sdk_qbusiness.types.chat_output.ChatOutput":
        """<p>Starts or continues a streaming Amazon Q Business conversation.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application linked to a streaming Amazon Q Business conversation.</p>
            user_id: <p>The identifier of the user attached to the chat input. </p>
            user_groups: <p>The group names that a user associated with the chat input belongs to.</p>
            conversation_id: <p>The identifier of the Amazon Q Business conversation.</p>
            parent_message_id: <p>The identifier used to associate a user message with a AI generated response.</p>
            client_token: <p>A token that you provide to identify the chat input.</p>
            input_stream: <p>The streaming input for the <code>Chat</code> API.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.chat_input.ChatInput]",
        ) -> AsyncOperationResponse["aws_sdk_qbusiness.types.chat_output.ChatOutput"]:
            import aws_sdk_qbusiness._operations.expert_q.chat

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.chat.async_chat(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.chat_input.ChatInput = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if user_id is not None:
            input_["user_id"] = user_id
        if user_groups is not None:
            input_["user_groups"] = user_groups
        if conversation_id is not None:
            input_["conversation_id"] = conversation_id
        if parent_message_id is not None:
            input_["parent_message_id"] = parent_message_id
        if client_token is not None:
            input_["client_token"] = client_token
        if input_stream is not None:
            input_["input_stream"] = ensure_async_iterator(input_stream)  # type: ignore

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def chat_sync(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
        user_groups: Optional["aws_sdk_qbusiness.types.user_groups.UserGroups"] = None,
        user_message: Optional[
            "aws_sdk_qbusiness.types.user_message.UserMessage"
        ] = None,
        attachments: Optional[
            "aws_sdk_qbusiness.types.attachments_input.AttachmentsInput"
        ] = None,
        action_execution: Optional[
            "aws_sdk_qbusiness.types.action_execution.ActionExecution"
        ] = None,
        auth_challenge_response: Optional[
            "aws_sdk_qbusiness.types.auth_challenge_response.AuthChallengeResponse"
        ] = None,
        conversation_id: Optional[
            "aws_sdk_qbusiness.types.conversation_id.ConversationId"
        ] = None,
        parent_message_id: Optional[
            "aws_sdk_qbusiness.types.message_id.MessageId"
        ] = None,
        attribute_filter: Optional[
            "aws_sdk_qbusiness.types.attribute_filter.AttributeFilter"
        ] = None,
        chat_mode: Optional["aws_sdk_qbusiness.types.chat_mode.ChatMode"] = None,
        chat_mode_configuration: Optional[
            "aws_sdk_qbusiness.types.chat_mode_configuration.ChatModeConfiguration"
        ] = None,
        client_token: Optional[
            "aws_sdk_qbusiness.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.chat_sync_output.ChatSyncOutput":
        r"""<p>Starts or continues a non-streaming Amazon Q Business conversation.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application linked to the Amazon Q Business conversation.</p>
            user_id: <p>The identifier of the user attached to the chat input.</p>
            user_groups: <p>The group names that a user associated with the chat input belongs to.</p>
            user_message: <p>A end user message in a conversation.</p>
            attachments: <p>A list of files uploaded directly during chat. You can upload a maximum of 5 files of upto 10 MB each.</p>
            action_execution: <p>A request from an end user to perform an Amazon Q Business plugin action.</p>
            auth_challenge_response: <p>An authentication verification event response by a third party authentication server to Amazon Q Business.</p>
            conversation_id: <p>The identifier of the Amazon Q Business conversation.</p>
            parent_message_id: <p>The identifier of the previous system message in a conversation.</p>
            attribute_filter: <p>Enables filtering of Amazon Q Business web experience responses based on document attributes or metadata fields.</p>
            chat_mode: <p>The <code>chatMode</code> parameter determines the chat modes available to Amazon Q Business users:</p> <ul> <li> <p> <code>RETRIEVAL_MODE</code> - If you choose this mode, Amazon Q generates responses solely from the data sources connected and indexed by the application. If an answer is not found in the data sources or there are no data sources available, Amazon Q will respond with a \"<i>No Answer Found</i>\" message, unless LLM knowledge has been enabled. In that case, Amazon Q will generate a response from the LLM knowledge</p> </li> <li> <p> <code>CREATOR_MODE</code> - By selecting this mode, you can choose to generate responses only from the LLM knowledge. You can also attach files and have Amazon Q generate a response based on the data in those files. If the attached files do not contain an answer for the query, Amazon Q will automatically fall back to generating a response from the LLM knowledge.</p> </li> <li> <p> <code>PLUGIN_MODE</code> - By selecting this mode, users can choose to use plugins in chat to get their responses.</p> </li> </ul> <note> <p>If none of the modes are selected, Amazon Q will only respond using the information from the attached files.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html\">Admin controls and guardrails</a>, <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html\">Plugins</a>, and <a href=\"https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html#chat-source-scope\">Response sources</a>.</p>
            chat_mode_configuration: <p>The chat mode configuration for an Amazon Q Business application.</p>
            client_token: <p>A token that you provide to identify a chat request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.chat_sync_input.ChatSyncInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.chat_sync_output.ChatSyncOutput"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.chat_sync

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.chat_sync.async_chat_sync(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.chat_sync_input.ChatSyncInput = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if user_id is not None:
            input_["user_id"] = user_id
        if user_groups is not None:
            input_["user_groups"] = user_groups
        if user_message is not None:
            input_["user_message"] = user_message
        if attachments is not None:
            input_["attachments"] = attachments
        if action_execution is not None:
            input_["action_execution"] = action_execution
        if auth_challenge_response is not None:
            input_["auth_challenge_response"] = auth_challenge_response
        if conversation_id is not None:
            input_["conversation_id"] = conversation_id
        if parent_message_id is not None:
            input_["parent_message_id"] = parent_message_id
        if attribute_filter is not None:
            input_["attribute_filter"] = attribute_filter
        if chat_mode is not None:
            input_["chat_mode"] = chat_mode
        if chat_mode_configuration is not None:
            input_["chat_mode_configuration"] = chat_mode_configuration
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def check_document_access(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        user_id: "aws_sdk_qbusiness.types.string.String",
        document_id: "aws_sdk_qbusiness.types.document_id.DocumentId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        data_source_id: Optional[
            "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.check_document_access_response.CheckDocumentAccessResponse":
        """<p>Verifies if a user has access permissions for a specified document and returns the actual ACL attached to the document. Resolves user access on the document via user aliases and groups when verifying user access.</p>

        Args:
            application_id: <p>The unique identifier of the application. This is required to identify the specific Amazon Q Business application context for the document access check.</p>
            index_id: <p>The unique identifier of the index. Used to locate the correct index within the application where the document is stored.</p>
            user_id: <p>The unique identifier of the user. Used to check the access permissions for this specific user against the document's ACL.</p>
            document_id: <p>The unique identifier of the document. Specifies which document's access permissions are being checked.</p>
            data_source_id: <p>The unique identifier of the data source. Identifies the specific data source from which the document originates. Should not be used when a document is uploaded directly with BatchPutDocument, as no dataSourceId is available or necessary. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.check_document_access_request.CheckDocumentAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.check_document_access_response.CheckDocumentAccessResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.check_document_access

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.check_document_access.async_check_document_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.check_document_access_request.CheckDocumentAccessRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["index_id"] = index_id
        input_["user_id"] = user_id
        input_["document_id"] = document_id
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_anonymous_web_experience_url(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        web_experience_id: "aws_sdk_qbusiness.types.web_experience_id.WebExperienceId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        session_duration_in_minutes: Optional[
            "aws_sdk_qbusiness.types.session_duration_in_minutes.SessionDurationInMinutes"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.create_anonymous_web_experience_url_response.CreateAnonymousWebExperienceUrlResponse":
        """<p>Creates a unique URL for anonymous Amazon Q Business web experience. This URL can only be used once and must be used within 5 minutes after it's generated.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application environment attached to the web experience.</p>
            web_experience_id: <p>The identifier of the web experience.</p>
            session_duration_in_minutes: <p>The duration of the session associated with the unique URL for the web experience.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.create_anonymous_web_experience_url_request.CreateAnonymousWebExperienceUrlRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.create_anonymous_web_experience_url_response.CreateAnonymousWebExperienceUrlResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.create_anonymous_web_experience_url

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.create_anonymous_web_experience_url.async_create_anonymous_web_experience_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.create_anonymous_web_experience_url_request.CreateAnonymousWebExperienceUrlRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["web_experience_id"] = web_experience_id
        if session_duration_in_minutes is not None:
            input_["session_duration_in_minutes"] = session_duration_in_minutes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_chat_response_configuration(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        display_name: "aws_sdk_qbusiness.types.display_name.DisplayName",
        response_configurations: "aws_sdk_qbusiness.types.response_configurations.ResponseConfigurations",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        client_token: Optional["aws_sdk_qbusiness.types.string.String"] = None,
        tags: Optional["aws_sdk_qbusiness.types.tags.Tags"] = None,
    ) -> "aws_sdk_qbusiness.types.create_chat_response_configuration_response.CreateChatResponseConfigurationResponse":
        """<p>Creates a new chat response configuration for an Amazon Q Business application. This operation establishes a set of parameters that define how the system generates and formats responses to user queries in chat interactions.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application for which to create the new chat response configuration.</p>
            display_name: <p>A human-readable name for the new chat response configuration, making it easier to identify and manage among multiple configurations.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This helps prevent the same configuration from being created multiple times if retries occur.</p>
            response_configurations: <p>A collection of response configuration settings that define how Amazon Q Business will generate and format responses to user queries in chat interactions.</p>
            tags: <p>A list of key-value pairs to apply as tags to the new chat response configuration, enabling categorization and management of resources across Amazon Web Services services.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.create_chat_response_configuration_request.CreateChatResponseConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.create_chat_response_configuration_response.CreateChatResponseConfigurationResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.create_chat_response_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.create_chat_response_configuration.async_create_chat_response_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.create_chat_response_configuration_request.CreateChatResponseConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["display_name"] = display_name
        if client_token is not None:
            input_["client_token"] = client_token
        input_["response_configurations"] = response_configurations
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_subscription(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        principal: "aws_sdk_qbusiness.types.subscription_principal.SubscriptionPrincipal",
        type: "aws_sdk_qbusiness.types.subscription_type.SubscriptionType",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_qbusiness.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.create_subscription_response.CreateSubscriptionResponse":
        r"""<p>Subscribes an IAM Identity Center user or a group to a pricing tier for an Amazon Q Business application.</p> <p>Amazon Q Business offers two subscription tiers: <code>Q_LITE</code> and <code>Q_BUSINESS</code>. Subscription tier determines feature access for the user. For more information on subscriptions and pricing tiers, see <a href=\"https://aws.amazon.com/q/business/pricing/\">Amazon Q Business pricing</a>.</p> <note> <p>For an example IAM role policy for assigning subscriptions, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/setting-up.html#permissions\">Set up required permissions</a> in the Amazon Q Business User Guide.</p> </note>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application the subscription should be added to.</p>
            principal: <p>The IAM Identity Center <code>UserId</code> or <code>GroupId</code> of a user or group in the IAM Identity Center instance connected to the Amazon Q Business application.</p>
            type: <p>The type of Amazon Q Business subscription you want to create.</p>
            client_token: <p>A token that you provide to identify the request to create a subscription for your Amazon Q Business application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.create_subscription_request.CreateSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.create_subscription_response.CreateSubscriptionResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.create_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.create_subscription.async_create_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.create_subscription_request.CreateSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["principal"] = principal
        input_["type"] = type
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_user(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        user_id: "aws_sdk_qbusiness.types.string.String",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_aliases: Optional[
            "aws_sdk_qbusiness.types.user_aliases.UserAliases"
        ] = None,
        client_token: Optional[
            "aws_sdk_qbusiness.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.create_user_response.CreateUserResponse":
        """<p>Creates a universally unique identifier (UUID) mapped to a list of local user ids within an application.</p>

        Args:
            application_id: <p>The identifier of the application for which the user mapping will be created.</p>
            user_id: <p>The user emails attached to a user mapping.</p>
            user_aliases: <p>The list of user aliases in the mapping.</p>
            client_token: <p>A token that you provide to identify the request to create your Amazon Q Business user mapping.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.create_user_request.CreateUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.create_user_response.CreateUserResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.create_user

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.create_user.async_create_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.create_user_request.CreateUserRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["user_id"] = user_id
        if user_aliases is not None:
            input_["user_aliases"] = user_aliases
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_attachment(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        conversation_id: "aws_sdk_qbusiness.types.conversation_id.ConversationId",
        attachment_id: "aws_sdk_qbusiness.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
    ) -> "aws_sdk_qbusiness.types.delete_attachment_response.DeleteAttachmentResponse":
        """<p>Deletes an attachment associated with a specific Amazon Q Business conversation.</p>

        Args:
            application_id: <p>The unique identifier for the Amazon Q Business application environment.</p>
            conversation_id: <p>The unique identifier of the conversation.</p>
            attachment_id: <p>The unique identifier for the attachment.</p>
            user_id: <p>The unique identifier of the user involved in the conversation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.delete_attachment_request.DeleteAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.delete_attachment_response.DeleteAttachmentResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.delete_attachment

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.delete_attachment.async_delete_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.delete_attachment_request.DeleteAttachmentRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["conversation_id"] = conversation_id
        input_["attachment_id"] = attachment_id
        if user_id is not None:
            input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_chat_controls_configuration(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.delete_chat_controls_configuration_response.DeleteChatControlsConfigurationResponse":
        """<p>Deletes chat controls configured for an existing Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the application the chat controls have been configured for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.delete_chat_controls_configuration_request.DeleteChatControlsConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.delete_chat_controls_configuration_response.DeleteChatControlsConfigurationResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.delete_chat_controls_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.delete_chat_controls_configuration.async_delete_chat_controls_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.delete_chat_controls_configuration_request.DeleteChatControlsConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_chat_response_configuration(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        chat_response_configuration_id: "aws_sdk_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.delete_chat_response_configuration_response.DeleteChatResponseConfigurationResponse":
        """<p>Deletes a specified chat response configuration from an Amazon Q Business application.</p>

        Args:
            application_id: <p>The unique identifier of theAmazon Q Business application from which to delete the chat response configuration.</p>
            chat_response_configuration_id: <p>The unique identifier of the chat response configuration to delete from the specified application. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.delete_chat_response_configuration_request.DeleteChatResponseConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.delete_chat_response_configuration_response.DeleteChatResponseConfigurationResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.delete_chat_response_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.delete_chat_response_configuration.async_delete_chat_response_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.delete_chat_response_configuration_request.DeleteChatResponseConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["chat_response_configuration_id"] = chat_response_configuration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_conversation(
        self,
        conversation_id: "aws_sdk_qbusiness.types.conversation_id.ConversationId",
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
    ) -> "aws_sdk_qbusiness.types.delete_conversation_response.DeleteConversationResponse":
        """<p>Deletes an Amazon Q Business web experience conversation.</p>

        Args:
            conversation_id: <p>The identifier of the Amazon Q Business web experience conversation being deleted.</p>
            application_id: <p>The identifier of the Amazon Q Business application associated with the conversation.</p>
            user_id: <p>The identifier of the user who is deleting the conversation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.delete_conversation_request.DeleteConversationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.delete_conversation_response.DeleteConversationResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.delete_conversation

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.delete_conversation.async_delete_conversation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.delete_conversation_request.DeleteConversationRequest = {}  # type: ignore[typeddict-item]
        input_["conversation_id"] = conversation_id
        input_["application_id"] = application_id
        if user_id is not None:
            input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_group(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        group_name: "aws_sdk_qbusiness.types.group_name.GroupName",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        data_source_id: Optional[
            "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.delete_group_response.DeleteGroupResponse":
        r"""<p>Deletes a group so that all users and sub groups that belong to the group can no longer access documents only available to that group. For example, after deleting the group \"Summer Interns\", all interns who belonged to that group no longer see intern-only documents in their chat results. </p> <p>If you want to delete, update, or replace users or sub groups of a group, you need to use the <code>PutGroup</code> operation. For example, if a user in the group \"Engineering\" leaves the engineering team and another user takes their place, you provide an updated list of users or sub groups that belong to the \"Engineering\" group when calling <code>PutGroup</code>.</p>

        Args:
            application_id: <p>The identifier of the application in which the group mapping belongs.</p>
            index_id: <p>The identifier of the index you want to delete the group from.</p>
            group_name: <p>The name of the group you want to delete.</p>
            data_source_id: <p>The identifier of the data source linked to the group</p> <p>A group can be tied to multiple data sources. You can delete a group from accessing documents in a certain data source. For example, the groups \"Research\", \"Engineering\", and \"Sales and Marketing\" are all tied to the company's documents stored in the data sources Confluence and Salesforce. You want to delete \"Research\" and \"Engineering\" groups from Salesforce, so that these groups cannot access customer-related documents stored in Salesforce. Only \"Sales and Marketing\" should access documents in the Salesforce data source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.delete_group_request.DeleteGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.delete_group_response.DeleteGroupResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.delete_group

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.delete_group.async_delete_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.delete_group_request.DeleteGroupRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["index_id"] = index_id
        input_["group_name"] = group_name
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_user(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        user_id: "aws_sdk_qbusiness.types.string.String",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.delete_user_response.DeleteUserResponse":
        """<p>Deletes a user by email id.</p>

        Args:
            application_id: <p>The identifier of the application from which the user is being deleted.</p>
            user_id: <p>The user email being deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.delete_user_request.DeleteUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.delete_user_response.DeleteUserResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.delete_user

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.delete_user.async_delete_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.delete_user_request.DeleteUserRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_permission(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        statement_id: "aws_sdk_qbusiness.types.string.String",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.disassociate_permission_response.DisassociatePermissionResponse":
        """<p>Removes a permission policy from a Amazon Q Business application, revoking the cross-account access that was previously granted to an ISV. This operation deletes the specified policy statement from the application's permission policy.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>
            statement_id: <p>The statement ID of the permission to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.disassociate_permission_request.DisassociatePermissionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.disassociate_permission_response.DisassociatePermissionResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.disassociate_permission

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.disassociate_permission.async_disassociate_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.disassociate_permission_request.DisassociatePermissionRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["statement_id"] = statement_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_chat_controls_configuration(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_get_topic_configurations.MaxResultsIntegerForGetTopicConfigurations"
        ] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_qbusiness.types.get_chat_controls_configuration_response.GetChatControlsConfigurationResponse":
        """<p>Gets information about chat controls configured for an existing Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the application for which the chat controls are configured.</p>
            max_results: <p>The maximum number of configured chat controls to return.</p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business chat controls configured.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.get_chat_controls_configuration_request.GetChatControlsConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.get_chat_controls_configuration_response.GetChatControlsConfigurationResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.get_chat_controls_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.get_chat_controls_configuration.async_get_chat_controls_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.get_chat_controls_configuration_request.GetChatControlsConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
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

    async def iter_get_chat_controls_configuration(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_get_topic_configurations.MaxResultsIntegerForGetTopicConfigurations"
        ] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
    ) -> (
        "AsyncIterator[aws_sdk_qbusiness.types.topic_configuration.TopicConfiguration]"
    ):
        _token = next_token
        while True:
            _response = await self.get_chat_controls_configuration(
                application_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("topic_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_chat_response_configuration(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        chat_response_configuration_id: "aws_sdk_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.get_chat_response_configuration_response.GetChatResponseConfigurationResponse":
        """<p>Retrieves detailed information about a specific chat response configuration from an Amazon Q Business application. This operation returns the complete configuration settings and metadata.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application containing the chat response configuration to retrieve.</p>
            chat_response_configuration_id: <p>The unique identifier of the chat response configuration to retrieve from the specified application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.get_chat_response_configuration_request.GetChatResponseConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.get_chat_response_configuration_response.GetChatResponseConfigurationResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.get_chat_response_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.get_chat_response_configuration.async_get_chat_response_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.get_chat_response_configuration_request.GetChatResponseConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["chat_response_configuration_id"] = chat_response_configuration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_document_content(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        document_id: "aws_sdk_qbusiness.types.document_id.DocumentId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        data_source_id: Optional[
            "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
        output_format: Optional[
            "aws_sdk_qbusiness.types.output_format.OutputFormat"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.get_document_content_response.GetDocumentContentResponse":
        r"""<p>Retrieves the content of a document that was ingested into Amazon Q Business. This API validates user authorization against document ACLs before returning a pre-signed URL for secure document access. You can download or view source documents referenced in chat responses through the URL.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application containing the document. This ensures the request is scoped to the correct application environment and its associated security policies.</p>
            index_id: <p>The identifier of the index where documents are indexed.</p>
            data_source_id: <p>The identifier of the data source from which the document was ingested. This field is not present if the document is ingested by directly calling the BatchPutDocument API. If the document is from a file-upload data source, the datasource will be \"uploaded-docs-file-stat-datasourceid\".</p>
            document_id: <p>The unique identifier of the document that is indexed via BatchPutDocument API or file-upload or connector sync. It is also found in chat or chatSync response.</p>
            output_format: <p>Document outputFormat. Defaults to RAW if not selected.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.get_document_content_request.GetDocumentContentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.get_document_content_response.GetDocumentContentResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.get_document_content

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.get_document_content.async_get_document_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.get_document_content_request.GetDocumentContentRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["index_id"] = index_id
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id
        input_["document_id"] = document_id
        if output_format is not None:
            input_["output_format"] = output_format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_group(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        group_name: "aws_sdk_qbusiness.types.group_name.GroupName",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        data_source_id: Optional[
            "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.get_group_response.GetGroupResponse":
        """<p>Describes a group by group name.</p>

        Args:
            application_id: <p>The identifier of the application id the group is attached to.</p>
            index_id: <p>The identifier of the index the group is attached to.</p>
            group_name: <p>The name of the group.</p>
            data_source_id: <p>The identifier of the data source the group is attached to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.get_group_request.GetGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.get_group_response.GetGroupResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.get_group

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.get_group.async_get_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.get_group_request.GetGroupRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["index_id"] = index_id
        input_["group_name"] = group_name
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_media(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        conversation_id: "aws_sdk_qbusiness.types.conversation_id.ConversationId",
        message_id: "aws_sdk_qbusiness.types.message_id.MessageId",
        media_id: "aws_sdk_qbusiness.types.media_id.MediaId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.get_media_response.GetMediaResponse":
        r"""<p>Returns the image bytes corresponding to a media object. If you have implemented your own application with the Chat and ChatSync APIs, and have enabled content extraction from visual data in Amazon Q Business, you use the GetMedia API operation to download the images so you can show them in your UI with responses.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html\">Extracting semantic meaning from images and visuals</a>.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business which contains the media object.</p>
            conversation_id: <p>The identifier of the Amazon Q Business conversation.</p>
            message_id: <p>The identifier of the Amazon Q Business message.</p>
            media_id: <p>The identifier of the media object. You can find this in the <code>sourceAttributions</code> returned by the <code>Chat</code>, <code>ChatSync</code>, and <code>ListMessages</code> API responses.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.get_media_request.GetMediaRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.get_media_response.GetMediaResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.get_media

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.get_media.async_get_media(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.get_media_request.GetMediaRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["conversation_id"] = conversation_id
        input_["message_id"] = message_id
        input_["media_id"] = media_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_policy(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.get_policy_response.GetPolicyResponse":
        """<p>Retrieves the current permission policy for a Amazon Q Business application. The policy is returned as a JSON-formatted string and defines the IAM actions that are allowed or denied for the application's resources.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.get_policy_request.GetPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.get_policy_response.GetPolicyResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.get_policy

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.get_policy.async_get_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.get_policy_request.GetPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_user(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        user_id: "aws_sdk_qbusiness.types.string.String",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.get_user_response.GetUserResponse":
        """<p>Describes the universally unique identifier (UUID) associated with a local user in a data source.</p>

        Args:
            application_id: <p>The identifier of the application connected to the user.</p>
            user_id: <p>The user email address attached to the user.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.get_user_request.GetUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.get_user_response.GetUserResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.get_user

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.get_user.async_get_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.get_user_request.GetUserRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_attachments(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        conversation_id: Optional[
            "aws_sdk_qbusiness.types.conversation_id.ConversationId"
        ] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_attachments.MaxResultsIntegerForListAttachments"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.list_attachments_response.ListAttachmentsResponse":
        """<p>Gets a list of attachments associated with an Amazon Q Business web experience or a list of attachements associated with a specific Amazon Q Business conversation.</p>

        Args:
            application_id: <p>The unique identifier for the Amazon Q Business application.</p>
            conversation_id: <p>The unique identifier of the Amazon Q Business web experience conversation.</p>
            user_id: <p>The unique identifier of the user involved in the Amazon Q Business web experience conversation.</p>
            next_token: <p>If the number of attachments returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of attachments.</p>
            max_results: <p>The maximum number of attachements to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_attachments_request.ListAttachmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_attachments_response.ListAttachmentsResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_attachments

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_attachments.async_list_attachments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_attachments_request.ListAttachmentsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if conversation_id is not None:
            input_["conversation_id"] = conversation_id
        if user_id is not None:
            input_["user_id"] = user_id
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

    async def iter_list_attachments(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        conversation_id: Optional[
            "aws_sdk_qbusiness.types.conversation_id.ConversationId"
        ] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_attachments.MaxResultsIntegerForListAttachments"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.attachment.Attachment]":
        _token = next_token
        while True:
            _response = await self.list_attachments(
                application_id,
                config_overrides=config_overrides,
                conversation_id=conversation_id,
                user_id=user_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("attachments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_chat_response_configurations(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        max_results: Optional["aws_sdk_qbusiness.types.integer.Integer"] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_qbusiness.types.list_chat_response_configurations_response.ListChatResponseConfigurationsResponse":
        """<p>Retrieves a list of all chat response configurations available in a specified Amazon Q Business application. This operation returns summary information about each configuration to help administrators manage and select appropriate response settings.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application for which to list available chat response configurations.</p>
            max_results: <p>The maximum number of chat response configurations to return in a single response. This parameter helps control pagination of results when many configurations exist.</p>
            next_token: <p>A pagination token used to retrieve the next set of results when the number of configurations exceeds the specified <code>maxResults</code> value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_chat_response_configurations_request.ListChatResponseConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_chat_response_configurations_response.ListChatResponseConfigurationsResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_chat_response_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_chat_response_configurations.async_list_chat_response_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_chat_response_configurations_request.ListChatResponseConfigurationsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
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

    async def iter_list_chat_response_configurations(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        max_results: Optional["aws_sdk_qbusiness.types.integer.Integer"] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.chat_response_configuration.ChatResponseConfiguration]":
        _token = next_token
        while True:
            _response = await self.list_chat_response_configurations(
                application_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("chat_response_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_conversations(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_conversations.MaxResultsIntegerForListConversations"
        ] = None,
    ) -> (
        "aws_sdk_qbusiness.types.list_conversations_response.ListConversationsResponse"
    ):
        """<p>Lists one or more Amazon Q Business conversations.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>
            user_id: <p>The identifier of the user involved in the Amazon Q Business web experience conversation. </p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business conversations.</p>
            max_results: <p>The maximum number of Amazon Q Business conversations to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_conversations_request.ListConversationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_conversations_response.ListConversationsResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_conversations

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_conversations.async_list_conversations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_conversations_request.ListConversationsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if user_id is not None:
            input_["user_id"] = user_id
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

    async def iter_list_conversations(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_conversations.MaxResultsIntegerForListConversations"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.conversation.Conversation]":
        _token = next_token
        while True:
            _response = await self.list_conversations(
                application_id,
                config_overrides=config_overrides,
                user_id=user_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("conversations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_source_sync_jobs(
        self,
        data_source_id: "aws_sdk_qbusiness.types.data_source_id.DataSourceId",
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_data_sources_sync_jobs.MaxResultsIntegerForListDataSourcesSyncJobs"
        ] = None,
        start_time: Optional["aws_sdk_qbusiness.types.timestamp.Timestamp"] = None,
        end_time: Optional["aws_sdk_qbusiness.types.timestamp.Timestamp"] = None,
        status_filter: Optional[
            "aws_sdk_qbusiness.types.data_source_sync_job_status.DataSourceSyncJobStatus"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.list_data_source_sync_jobs_response.ListDataSourceSyncJobsResponse":
        """<p>Get information about an Amazon Q Business data source connector synchronization.</p>

        Args:
            data_source_id: <p> The identifier of the data source connector.</p>
            application_id: <p>The identifier of the Amazon Q Business application connected to the data source.</p>
            index_id: <p>The identifier of the index used with the Amazon Q Business data source connector.</p>
            next_token: <p>If the <code>maxResults</code> response was incpmplete because there is more data to retriever, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of responses.</p>
            max_results: <p>The maximum number of synchronization jobs to return in the response.</p>
            start_time: <p> The start time of the data source connector sync. </p>
            end_time: <p> The end time of the data source connector sync.</p>
            status_filter: <p>Only returns synchronization jobs with the <code>Status</code> field equal to the specified status.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_data_source_sync_jobs_request.ListDataSourceSyncJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_data_source_sync_jobs_response.ListDataSourceSyncJobsResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_data_source_sync_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_data_source_sync_jobs.async_list_data_source_sync_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_data_source_sync_jobs_request.ListDataSourceSyncJobsRequest = {}  # type: ignore[typeddict-item]
        input_["data_source_id"] = data_source_id
        input_["application_id"] = application_id
        input_["index_id"] = index_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_data_source_sync_jobs(
        self,
        data_source_id: "aws_sdk_qbusiness.types.data_source_id.DataSourceId",
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_data_sources_sync_jobs.MaxResultsIntegerForListDataSourcesSyncJobs"
        ] = None,
        start_time: Optional["aws_sdk_qbusiness.types.timestamp.Timestamp"] = None,
        end_time: Optional["aws_sdk_qbusiness.types.timestamp.Timestamp"] = None,
        status_filter: Optional[
            "aws_sdk_qbusiness.types.data_source_sync_job_status.DataSourceSyncJobStatus"
        ] = None,
    ) -> (
        "AsyncIterator[aws_sdk_qbusiness.types.data_source_sync_job.DataSourceSyncJob]"
    ):
        _token = next_token
        while True:
            _response = await self.list_data_source_sync_jobs(
                data_source_id,
                application_id,
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                start_time=start_time,
                end_time=end_time,
                status_filter=status_filter,
            )
            _page = _resolve_path(_response, ("history",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_documents(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        data_source_ids: Optional[
            "aws_sdk_qbusiness.types.data_source_ids.DataSourceIds"
        ] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_documents.MaxResultsIntegerForListDocuments"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.list_documents_response.ListDocumentsResponse":
        """<p>A list of documents attached to an index.</p>

        Args:
            application_id: <p>The identifier of the application id the documents are attached to.</p>
            index_id: <p>The identifier of the index the documents are attached to.</p>
            data_source_ids: <p>The identifier of the data sources the documents are attached to.</p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of documents.</p>
            max_results: <p>The maximum number of documents to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_documents_request.ListDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_documents_response.ListDocumentsResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_documents

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_documents.async_list_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_documents_request.ListDocumentsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["index_id"] = index_id
        if data_source_ids is not None:
            input_["data_source_ids"] = data_source_ids
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

    async def iter_list_documents(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        data_source_ids: Optional[
            "aws_sdk_qbusiness.types.data_source_ids.DataSourceIds"
        ] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_documents.MaxResultsIntegerForListDocuments"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.document_details.DocumentDetails]":
        _token = next_token
        while True:
            _response = await self.list_documents(
                application_id,
                index_id,
                config_overrides=config_overrides,
                data_source_ids=data_source_ids,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("document_detail_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_groups(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        updated_earlier_than: "aws_sdk_qbusiness.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        data_source_id: Optional[
            "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_groups_request.MaxResultsIntegerForListGroupsRequest"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.list_groups_response.ListGroupsResponse":
        """<p>Provides a list of groups that are mapped to users.</p>

        Args:
            application_id: <p>The identifier of the application for getting a list of groups mapped to users.</p>
            index_id: <p>The identifier of the index for getting a list of groups mapped to users.</p>
            updated_earlier_than: <p>The timestamp identifier used for the latest <code>PUT</code> or <code>DELETE</code> action for mapping users to their groups.</p>
            data_source_id: <p>The identifier of the data source for getting a list of groups mapped to users.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of groups that are mapped to users.</p>
            max_results: <p>The maximum number of returned groups that are mapped to users.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_groups_request.ListGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_groups_response.ListGroupsResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_groups

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_groups.async_list_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_groups_request.ListGroupsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["index_id"] = index_id
        input_["updated_earlier_than"] = updated_earlier_than
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id
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

    async def iter_list_groups(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        updated_earlier_than: "aws_sdk_qbusiness.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        data_source_id: Optional[
            "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_groups_request.MaxResultsIntegerForListGroupsRequest"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.group_summary.GroupSummary]":
        _token = next_token
        while True:
            _response = await self.list_groups(
                application_id,
                index_id,
                updated_earlier_than,
                config_overrides=config_overrides,
                data_source_id=data_source_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_messages(
        self,
        conversation_id: "aws_sdk_qbusiness.types.conversation_id.ConversationId",
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_messages.MaxResultsIntegerForListMessages"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.list_messages_response.ListMessagesResponse":
        """<p>Gets a list of messages associated with an Amazon Q Business web experience.</p>

        Args:
            conversation_id: <p>The identifier of the Amazon Q Business web experience conversation.</p>
            application_id: <p>The identifier for the Amazon Q Business application.</p>
            user_id: <p>The identifier of the user involved in the Amazon Q Business web experience conversation.</p>
            next_token: <p>If the number of messages returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of messages.</p>
            max_results: <p>The maximum number of messages to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_messages_request.ListMessagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_messages_response.ListMessagesResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_messages

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_messages.async_list_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_messages_request.ListMessagesRequest = {}  # type: ignore[typeddict-item]
        input_["conversation_id"] = conversation_id
        input_["application_id"] = application_id
        if user_id is not None:
            input_["user_id"] = user_id
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

    async def iter_list_messages(
        self,
        conversation_id: "aws_sdk_qbusiness.types.conversation_id.ConversationId",
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_messages.MaxResultsIntegerForListMessages"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.message.Message]":
        _token = next_token
        while True:
            _response = await self.list_messages(
                conversation_id,
                application_id,
                config_overrides=config_overrides,
                user_id=user_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("messages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_plugin_actions(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        plugin_id: "aws_sdk_qbusiness.types.plugin_id.PluginId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_actions.MaxResultsIntegerForListPluginActions"
        ] = None,
    ) -> (
        "aws_sdk_qbusiness.types.list_plugin_actions_response.ListPluginActionsResponse"
    ):
        """<p>Lists configured Amazon Q Business actions for a specific plugin in an Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application the plugin is attached to.</p>
            plugin_id: <p>The identifier of the Amazon Q Business plugin.</p>
            next_token: <p>If the number of plugin actions returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of plugin actions.</p>
            max_results: <p>The maximum number of plugin actions to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_plugin_actions_request.ListPluginActionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_plugin_actions_response.ListPluginActionsResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_plugin_actions

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_plugin_actions.async_list_plugin_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_plugin_actions_request.ListPluginActionsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["plugin_id"] = plugin_id
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

    async def iter_list_plugin_actions(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        plugin_id: "aws_sdk_qbusiness.types.plugin_id.PluginId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_actions.MaxResultsIntegerForListPluginActions"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.action_summary.ActionSummary]":
        _token = next_token
        while True:
            _response = await self.list_plugin_actions(
                application_id,
                plugin_id,
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

    async def list_plugin_type_actions(
        self,
        plugin_type: "aws_sdk_qbusiness.types.plugin_type.PluginType",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_type_actions.MaxResultsIntegerForListPluginTypeActions"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.list_plugin_type_actions_response.ListPluginTypeActionsResponse":
        """<p>Lists configured Amazon Q Business actions for any plugin type—both built-in and custom.</p>

        Args:
            plugin_type: <p>The type of the plugin.</p>
            next_token: <p>If the number of plugins returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of plugins.</p>
            max_results: <p>The maximum number of plugins to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_plugin_type_actions_request.ListPluginTypeActionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_plugin_type_actions_response.ListPluginTypeActionsResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_plugin_type_actions

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_plugin_type_actions.async_list_plugin_type_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_plugin_type_actions_request.ListPluginTypeActionsRequest = {}  # type: ignore[typeddict-item]
        input_["plugin_type"] = plugin_type
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

    async def iter_list_plugin_type_actions(
        self,
        plugin_type: "aws_sdk_qbusiness.types.plugin_type.PluginType",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_type_actions.MaxResultsIntegerForListPluginTypeActions"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.action_summary.ActionSummary]":
        _token = next_token
        while True:
            _response = await self.list_plugin_type_actions(
                plugin_type,
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

    async def list_plugin_type_metadata(
        self,
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_type_metadata.MaxResultsIntegerForListPluginTypeMetadata"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.list_plugin_type_metadata_response.ListPluginTypeMetadataResponse":
        """<p>Lists metadata for all Amazon Q Business plugin types.</p>

        Args:
            next_token: <p>If the metadata returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of metadata.</p>
            max_results: <p>The maximum number of plugin metadata items to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_plugin_type_metadata_request.ListPluginTypeMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_plugin_type_metadata_response.ListPluginTypeMetadataResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_plugin_type_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_plugin_type_metadata.async_list_plugin_type_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_plugin_type_metadata_request.ListPluginTypeMetadataRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_plugin_type_metadata(
        self,
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_type_metadata.MaxResultsIntegerForListPluginTypeMetadata"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.plugin_type_metadata_summary.PluginTypeMetadataSummary]":
        _token = next_token
        while True:
            _response = await self.list_plugin_type_metadata(
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

    async def list_subscriptions(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_subscriptions.MaxResultsIntegerForListSubscriptions"
        ] = None,
    ) -> (
        "aws_sdk_qbusiness.types.list_subscriptions_response.ListSubscriptionsResponse"
    ):
        """<p> Lists all subscriptions created in an Amazon Q Business application. </p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application linked to the subscription.</p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business subscriptions.</p>
            max_results: <p>The maximum number of Amazon Q Business subscriptions to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_subscriptions_request.ListSubscriptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_subscriptions_response.ListSubscriptionsResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_subscriptions

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_subscriptions.async_list_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_subscriptions_request.ListSubscriptionsRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
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

    async def iter_list_subscriptions(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_qbusiness.types.max_results_integer_for_list_subscriptions.MaxResultsIntegerForListSubscriptions"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.subscription.Subscription]":
        _token = next_token
        while True:
            _response = await self.list_subscriptions(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_qbusiness.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Gets a list of tags associated with a specified resource. Amazon Q Business applications and data sources can have tags associated with them.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Q Business application or data source to get a list of tags for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_feedback(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        conversation_id: "aws_sdk_qbusiness.types.conversation_id.ConversationId",
        message_id: "aws_sdk_qbusiness.types.system_message_id.SystemMessageId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_id: Optional["aws_sdk_qbusiness.types.user_id.UserId"] = None,
        message_copied_at: Optional[
            "aws_sdk_qbusiness.types.timestamp.Timestamp"
        ] = None,
        message_usefulness: Optional[
            "aws_sdk_qbusiness.types.message_usefulness_feedback.MessageUsefulnessFeedback"
        ] = None,
    ) -> None:
        """<p>Enables your end user to provide feedback on their Amazon Q Business generated chat responses.</p>

        Args:
            application_id: <p>The identifier of the application associated with the feedback.</p>
            user_id: <p>The identifier of the user giving the feedback.</p>
            conversation_id: <p>The identifier of the conversation the feedback is attached to.</p>
            message_id: <p>The identifier of the chat message that the feedback was given for.</p>
            message_copied_at: <p>The timestamp for when the feedback was recorded.</p>
            message_usefulness: <p>The feedback usefulness value given by the user to the chat message.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.put_feedback_request.PutFeedbackRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_qbusiness._operations.expert_q.put_feedback

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.put_feedback.async_put_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.put_feedback_request.PutFeedbackRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if user_id is not None:
            input_["user_id"] = user_id
        input_["conversation_id"] = conversation_id
        input_["message_id"] = message_id
        if message_copied_at is not None:
            input_["message_copied_at"] = message_copied_at
        if message_usefulness is not None:
            input_["message_usefulness"] = message_usefulness

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_group(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        group_name: "aws_sdk_qbusiness.types.group_name.GroupName",
        type: "aws_sdk_qbusiness.types.membership_type.MembershipType",
        group_members: "aws_sdk_qbusiness.types.group_members.GroupMembers",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        data_source_id: Optional[
            "aws_sdk_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
        role_arn: Optional["aws_sdk_qbusiness.types.role_arn.RoleArn"] = None,
    ) -> "aws_sdk_qbusiness.types.put_group_response.PutGroupResponse":
        r"""<p>Create, or updates, a mapping of users—who have access to a document—to groups.</p> <p>You can also map sub groups to groups. For example, the group \"Company Intellectual Property Teams\" includes sub groups \"Research\" and \"Engineering\". These sub groups include their own list of users or people who work in these teams. Only users who work in research and engineering, and therefore belong in the intellectual property group, can see top-secret company documents in their Amazon Q Business chat results.</p> <p>There are two options for creating groups, either passing group members inline or using an S3 file via the S3PathForGroupMembers field. For inline groups, there is a limit of 1000 members per group and for provided S3 files there is a limit of 100 thousand members. When creating a group using an S3 file, you provide both an S3 file and a <code>RoleArn</code> for Amazon Q Buisness to access the file.</p>

        Args:
            application_id: <p>The identifier of the application in which the user and group mapping belongs.</p>
            index_id: <p>The identifier of the index in which you want to map users to their groups.</p>
            group_name: <p>The list that contains your users or sub groups that belong the same group. For example, the group \"Company\" includes the user \"CEO\" and the sub groups \"Research\", \"Engineering\", and \"Sales and Marketing\".</p>
            data_source_id: <p>The identifier of the data source for which you want to map users to their groups. This is useful if a group is tied to multiple data sources, but you only want the group to access documents of a certain data source. For example, the groups \"Research\", \"Engineering\", and \"Sales and Marketing\" are all tied to the company's documents stored in the data sources Confluence and Salesforce. However, \"Sales and Marketing\" team only needs access to customer-related documents stored in Salesforce.</p>
            type: <p>The type of the group.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has access to the S3 file that contains your list of users that belong to a group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.put_group_request.PutGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.put_group_response.PutGroupResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.put_group

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.put_group.async_put_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.put_group_request.PutGroupRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["index_id"] = index_id
        input_["group_name"] = group_name
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id
        input_["type"] = type
        input_["group_members"] = group_members
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def search_relevant_content(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        query_text: "aws_sdk_qbusiness.types.query_text.QueryText",
        content_source: "aws_sdk_qbusiness.types.content_source.ContentSource",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        attribute_filter: Optional[
            "aws_sdk_qbusiness.types.attribute_filter.AttributeFilter"
        ] = None,
        max_results: Optional["aws_sdk_qbusiness.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_qbusiness.types.search_relevant_content_response.SearchRelevantContentResponse":
        """<p>Searches for relevant content in a Amazon Q Business application based on a query. This operation takes a search query text, the Amazon Q Business application identifier, and optional filters (such as content source and maximum results) as input. It returns a list of relevant content items, where each item includes the content text, the unique document identifier, the document title, the document URI, any relevant document attributes, and score attributes indicating the confidence level of the relevance.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application to search.</p>
            query_text: <p>The text to search for.</p>
            content_source: <p>The source of content to search in.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next set of results. (You received this token from a previous call.)</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.search_relevant_content_request.SearchRelevantContentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.search_relevant_content_response.SearchRelevantContentResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.search_relevant_content

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.search_relevant_content.async_search_relevant_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.search_relevant_content_request.SearchRelevantContentRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["query_text"] = query_text
        input_["content_source"] = content_source
        if attribute_filter is not None:
            input_["attribute_filter"] = attribute_filter
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

    async def iter_search_relevant_content(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        query_text: "aws_sdk_qbusiness.types.query_text.QueryText",
        content_source: "aws_sdk_qbusiness.types.content_source.ContentSource",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        attribute_filter: Optional[
            "aws_sdk_qbusiness.types.attribute_filter.AttributeFilter"
        ] = None,
        max_results: Optional["aws_sdk_qbusiness.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_qbusiness.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_qbusiness.types.relevant_content.RelevantContent]":
        _token = next_token
        while True:
            _response = await self.search_relevant_content(
                application_id,
                query_text,
                content_source,
                config_overrides=config_overrides,
                attribute_filter=attribute_filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("relevant_content",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_data_source_sync_job(
        self,
        data_source_id: "aws_sdk_qbusiness.types.data_source_id.DataSourceId",
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.start_data_source_sync_job_response.StartDataSourceSyncJobResponse":
        """<p>Starts a data source connector synchronization job. If a synchronization job is already in progress, Amazon Q Business returns a <code>ConflictException</code>.</p>

        Args:
            data_source_id: <p> The identifier of the data source connector. </p>
            application_id: <p>The identifier of Amazon Q Business application the data source is connected to.</p>
            index_id: <p>The identifier of the index used with the data source connector.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.start_data_source_sync_job_request.StartDataSourceSyncJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.start_data_source_sync_job_response.StartDataSourceSyncJobResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.start_data_source_sync_job

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.start_data_source_sync_job.async_start_data_source_sync_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.start_data_source_sync_job_request.StartDataSourceSyncJobRequest = {}  # type: ignore[typeddict-item]
        input_["data_source_id"] = data_source_id
        input_["application_id"] = application_id
        input_["index_id"] = index_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_data_source_sync_job(
        self,
        data_source_id: "aws_sdk_qbusiness.types.data_source_id.DataSourceId",
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        index_id: "aws_sdk_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.stop_data_source_sync_job_response.StopDataSourceSyncJobResponse":
        """<p>Stops an Amazon Q Business data source connector synchronization job already in progress.</p>

        Args:
            data_source_id: <p> The identifier of the data source connector. </p>
            application_id: <p>The identifier of the Amazon Q Business application that the data source is connected to.</p>
            index_id: <p>The identifier of the index used with the Amazon Q Business data source connector.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.stop_data_source_sync_job_request.StopDataSourceSyncJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.stop_data_source_sync_job_response.StopDataSourceSyncJobResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.stop_data_source_sync_job

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.stop_data_source_sync_job.async_stop_data_source_sync_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.stop_data_source_sync_job_request.StopDataSourceSyncJobRequest = {}  # type: ignore[typeddict-item]
        input_["data_source_id"] = data_source_id
        input_["application_id"] = application_id
        input_["index_id"] = index_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_qbusiness.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_qbusiness.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tag to the specified Amazon Q Business application or data source resource. If the tag already exists, the existing value is replaced with the new value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Q Business application or data source to tag.</p>
            tags: <p>A list of tag keys to add to the Amazon Q Business application or data source. If a tag already exists, the existing value is replaced with the new value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_qbusiness.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_qbusiness.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from an Amazon Q Business application or a data source.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Q Business application, or data source to remove the tag from.</p>
            tag_keys: <p>A list of tag keys to remove from the Amazon Q Business application or data source. If a tag key does not exist on the resource, it is ignored.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_chat_controls_configuration(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_qbusiness.types.client_token.ClientToken"
        ] = None,
        response_scope: Optional[
            "aws_sdk_qbusiness.types.response_scope.ResponseScope"
        ] = None,
        orchestration_configuration: Optional[
            "aws_sdk_qbusiness.types.orchestration_configuration.OrchestrationConfiguration"
        ] = None,
        blocked_phrases_configuration_update: Optional[
            "aws_sdk_qbusiness.types.blocked_phrases_configuration_update.BlockedPhrasesConfigurationUpdate"
        ] = None,
        topic_configurations_to_create_or_update: Optional[
            "aws_sdk_qbusiness.types.topic_configurations.TopicConfigurations"
        ] = None,
        topic_configurations_to_delete: Optional[
            "aws_sdk_qbusiness.types.topic_configurations.TopicConfigurations"
        ] = None,
        creator_mode_configuration: Optional[
            "aws_sdk_qbusiness.types.creator_mode_configuration.CreatorModeConfiguration"
        ] = None,
        hallucination_reduction_configuration: Optional[
            "aws_sdk_qbusiness.types.hallucination_reduction_configuration.HallucinationReductionConfiguration"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.update_chat_controls_configuration_response.UpdateChatControlsConfigurationResponse":
        """<p>Updates a set of chat controls configured for an existing Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the application for which the chat controls are configured.</p>
            client_token: <p>A token that you provide to identify the request to update a Amazon Q Business application chat configuration.</p>
            response_scope: <p>The response scope configured for your application. This determines whether your application uses its retrieval augmented generation (RAG) system to generate answers only from your enterprise data, or also uses the large language models (LLM) knowledge to respons to end user questions in chat.</p>
            orchestration_configuration: <p> The chat response orchestration settings for your application.</p>
            blocked_phrases_configuration_update: <p>The phrases blocked from chat by your chat control configuration.</p>
            topic_configurations_to_create_or_update: <p>The configured topic specific chat controls you want to update.</p>
            topic_configurations_to_delete: <p>The configured topic specific chat controls you want to delete.</p>
            creator_mode_configuration: <p>The configuration details for <code>CREATOR_MODE</code>.</p>
            hallucination_reduction_configuration: <p> The hallucination reduction settings for your application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.update_chat_controls_configuration_request.UpdateChatControlsConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.update_chat_controls_configuration_response.UpdateChatControlsConfigurationResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.update_chat_controls_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.update_chat_controls_configuration.async_update_chat_controls_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.update_chat_controls_configuration_request.UpdateChatControlsConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        if client_token is not None:
            input_["client_token"] = client_token
        if response_scope is not None:
            input_["response_scope"] = response_scope
        if orchestration_configuration is not None:
            input_["orchestration_configuration"] = orchestration_configuration
        if blocked_phrases_configuration_update is not None:
            input_["blocked_phrases_configuration_update"] = (
                blocked_phrases_configuration_update
            )
        if topic_configurations_to_create_or_update is not None:
            input_["topic_configurations_to_create_or_update"] = (
                topic_configurations_to_create_or_update
            )
        if topic_configurations_to_delete is not None:
            input_["topic_configurations_to_delete"] = topic_configurations_to_delete
        if creator_mode_configuration is not None:
            input_["creator_mode_configuration"] = creator_mode_configuration
        if hallucination_reduction_configuration is not None:
            input_["hallucination_reduction_configuration"] = (
                hallucination_reduction_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_chat_response_configuration(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        chat_response_configuration_id: "aws_sdk_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId",
        response_configurations: "aws_sdk_qbusiness.types.response_configurations.ResponseConfigurations",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        display_name: Optional[
            "aws_sdk_qbusiness.types.display_name.DisplayName"
        ] = None,
        client_token: Optional["aws_sdk_qbusiness.types.string.String"] = None,
    ) -> "aws_sdk_qbusiness.types.update_chat_response_configuration_response.UpdateChatResponseConfigurationResponse":
        """<p>Updates an existing chat response configuration in an Amazon Q Business application. This operation allows administrators to modify configuration settings, display name, and response parameters to refine how the system generates responses.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application containing the chat response configuration to update.</p>
            chat_response_configuration_id: <p>The unique identifier of the chat response configuration to update within the specified application.</p>
            display_name: <p>The new human-readable name to assign to the chat response configuration, making it easier to identify among multiple configurations.</p>
            response_configurations: <p>The updated collection of response configuration settings that define how Amazon Q Business generates and formats responses to user queries.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This helps prevent the same update from being processed multiple times if retries occur.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.update_chat_response_configuration_request.UpdateChatResponseConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.update_chat_response_configuration_response.UpdateChatResponseConfigurationResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.update_chat_response_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.update_chat_response_configuration.async_update_chat_response_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.update_chat_response_configuration_request.UpdateChatResponseConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["chat_response_configuration_id"] = chat_response_configuration_id
        if display_name is not None:
            input_["display_name"] = display_name
        input_["response_configurations"] = response_configurations
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_subscription(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        subscription_id: "aws_sdk_qbusiness.types.subscription_id.SubscriptionId",
        type: "aws_sdk_qbusiness.types.subscription_type.SubscriptionType",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "aws_sdk_qbusiness.types.update_subscription_response.UpdateSubscriptionResponse":
        r"""<p>Updates the pricing tier for an Amazon Q Business subscription. Upgrades are instant. Downgrades apply at the start of the next month. Subscription tier determines feature access for the user. For more information on subscriptions and pricing tiers, see <a href=\"https://aws.amazon.com/q/business/pricing/\">Amazon Q Business pricing</a>.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application where the subscription update should take effect.</p>
            subscription_id: <p>The identifier of the Amazon Q Business subscription to be updated.</p>
            type: <p>The type of the Amazon Q Business subscription to be updated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.update_subscription_request.UpdateSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.update_subscription_response.UpdateSubscriptionResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.update_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.update_subscription.async_update_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.update_subscription_request.UpdateSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["subscription_id"] = subscription_id
        input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_user(
        self,
        application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId",
        user_id: "aws_sdk_qbusiness.types.string.String",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        user_aliases_to_update: Optional[
            "aws_sdk_qbusiness.types.user_aliases.UserAliases"
        ] = None,
        user_aliases_to_delete: Optional[
            "aws_sdk_qbusiness.types.user_aliases.UserAliases"
        ] = None,
    ) -> "aws_sdk_qbusiness.types.update_user_response.UpdateUserResponse":
        """<p>Updates a information associated with a user id.</p>

        Args:
            application_id: <p>The identifier of the application the user is attached to.</p>
            user_id: <p>The email id attached to the user.</p>
            user_aliases_to_update: <p>The user aliases attached to the user id that are to be updated.</p>
            user_aliases_to_delete: <p>The user aliases attached to the user id that are to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_qbusiness.types.update_user_request.UpdateUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_qbusiness.types.update_user_response.UpdateUserResponse"
        ]:
            import aws_sdk_qbusiness._operations.expert_q.update_user

            (
                output,
                http_response,
            ) = await aws_sdk_qbusiness._operations.expert_q.update_user.async_update_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qbusiness.types.update_user_request.UpdateUserRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["user_id"] = user_id
        if user_aliases_to_update is not None:
            input_["user_aliases_to_update"] = user_aliases_to_update
        if user_aliases_to_delete is not None:
            input_["user_aliases_to_delete"] = user_aliases_to_delete

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
