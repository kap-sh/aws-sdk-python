"""Generated from Smithy shape ``com.amazonaws.workdocs#AWSGorillaBoyService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_workdocs._auth._signers
import aws_sdk_workdocs._auth._sigv4
from aws_sdk_workdocs._auth._identity import Credentials
from aws_sdk_workdocs._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_workdocs._auth._zapros_handler import AuthMiddleware
from aws_sdk_workdocs._pagination import resolve_path as _resolve_path
from aws_sdk_workdocs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.abort_document_version_upload_request
    import aws_sdk_workdocs.types.activate_user_request
    import aws_sdk_workdocs.types.activate_user_response
    import aws_sdk_workdocs.types.activity
    import aws_sdk_workdocs.types.activity_names_filter_type
    import aws_sdk_workdocs.types.add_resource_permissions_request
    import aws_sdk_workdocs.types.add_resource_permissions_response
    import aws_sdk_workdocs.types.additional_response_fields_list
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.boolean_enum_type
    import aws_sdk_workdocs.types.boolean_type
    import aws_sdk_workdocs.types.comment
    import aws_sdk_workdocs.types.comment_id_type
    import aws_sdk_workdocs.types.comment_text_type
    import aws_sdk_workdocs.types.comment_visibility_type
    import aws_sdk_workdocs.types.create_comment_request
    import aws_sdk_workdocs.types.create_comment_response
    import aws_sdk_workdocs.types.create_custom_metadata_request
    import aws_sdk_workdocs.types.create_custom_metadata_response
    import aws_sdk_workdocs.types.create_folder_request
    import aws_sdk_workdocs.types.create_folder_response
    import aws_sdk_workdocs.types.create_labels_request
    import aws_sdk_workdocs.types.create_labels_response
    import aws_sdk_workdocs.types.create_notification_subscription_request
    import aws_sdk_workdocs.types.create_notification_subscription_response
    import aws_sdk_workdocs.types.create_user_request
    import aws_sdk_workdocs.types.create_user_response
    import aws_sdk_workdocs.types.custom_metadata_key_list
    import aws_sdk_workdocs.types.custom_metadata_map
    import aws_sdk_workdocs.types.deactivate_user_request
    import aws_sdk_workdocs.types.delete_comment_request
    import aws_sdk_workdocs.types.delete_custom_metadata_request
    import aws_sdk_workdocs.types.delete_custom_metadata_response
    import aws_sdk_workdocs.types.delete_document_request
    import aws_sdk_workdocs.types.delete_document_version_request
    import aws_sdk_workdocs.types.delete_folder_contents_request
    import aws_sdk_workdocs.types.delete_folder_request
    import aws_sdk_workdocs.types.delete_labels_request
    import aws_sdk_workdocs.types.delete_labels_response
    import aws_sdk_workdocs.types.delete_notification_subscription_request
    import aws_sdk_workdocs.types.delete_user_request
    import aws_sdk_workdocs.types.describe_activities_request
    import aws_sdk_workdocs.types.describe_activities_response
    import aws_sdk_workdocs.types.describe_comments_request
    import aws_sdk_workdocs.types.describe_comments_response
    import aws_sdk_workdocs.types.describe_document_versions_request
    import aws_sdk_workdocs.types.describe_document_versions_response
    import aws_sdk_workdocs.types.describe_folder_contents_request
    import aws_sdk_workdocs.types.describe_folder_contents_response
    import aws_sdk_workdocs.types.describe_groups_request
    import aws_sdk_workdocs.types.describe_groups_response
    import aws_sdk_workdocs.types.describe_notification_subscriptions_request
    import aws_sdk_workdocs.types.describe_notification_subscriptions_response
    import aws_sdk_workdocs.types.describe_resource_permissions_request
    import aws_sdk_workdocs.types.describe_resource_permissions_response
    import aws_sdk_workdocs.types.describe_root_folders_request
    import aws_sdk_workdocs.types.describe_root_folders_response
    import aws_sdk_workdocs.types.describe_users_request
    import aws_sdk_workdocs.types.describe_users_response
    import aws_sdk_workdocs.types.document_content_type
    import aws_sdk_workdocs.types.document_version_id_type
    import aws_sdk_workdocs.types.document_version_metadata
    import aws_sdk_workdocs.types.document_version_status
    import aws_sdk_workdocs.types.email_address_type
    import aws_sdk_workdocs.types.field_names_type
    import aws_sdk_workdocs.types.filters
    import aws_sdk_workdocs.types.folder_content_type
    import aws_sdk_workdocs.types.folder_metadata
    import aws_sdk_workdocs.types.get_current_user_request
    import aws_sdk_workdocs.types.get_current_user_response
    import aws_sdk_workdocs.types.get_document_path_request
    import aws_sdk_workdocs.types.get_document_path_response
    import aws_sdk_workdocs.types.get_document_request
    import aws_sdk_workdocs.types.get_document_response
    import aws_sdk_workdocs.types.get_document_version_request
    import aws_sdk_workdocs.types.get_document_version_response
    import aws_sdk_workdocs.types.get_folder_path_request
    import aws_sdk_workdocs.types.get_folder_path_response
    import aws_sdk_workdocs.types.get_folder_request
    import aws_sdk_workdocs.types.get_folder_response
    import aws_sdk_workdocs.types.get_resources_request
    import aws_sdk_workdocs.types.get_resources_response
    import aws_sdk_workdocs.types.group_metadata
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.initiate_document_version_upload_request
    import aws_sdk_workdocs.types.initiate_document_version_upload_response
    import aws_sdk_workdocs.types.limit_type
    import aws_sdk_workdocs.types.locale_type
    import aws_sdk_workdocs.types.marker_type
    import aws_sdk_workdocs.types.next_marker_type
    import aws_sdk_workdocs.types.notification_options
    import aws_sdk_workdocs.types.order_type
    import aws_sdk_workdocs.types.page_marker_type
    import aws_sdk_workdocs.types.password_type
    import aws_sdk_workdocs.types.positive_integer_type
    import aws_sdk_workdocs.types.principal
    import aws_sdk_workdocs.types.principal_type
    import aws_sdk_workdocs.types.remove_all_resource_permissions_request
    import aws_sdk_workdocs.types.remove_resource_permission_request
    import aws_sdk_workdocs.types.resource_collection_type
    import aws_sdk_workdocs.types.resource_id_type
    import aws_sdk_workdocs.types.resource_name_type
    import aws_sdk_workdocs.types.resource_sort_type
    import aws_sdk_workdocs.types.resource_state_type
    import aws_sdk_workdocs.types.response_item
    import aws_sdk_workdocs.types.restore_document_versions_request
    import aws_sdk_workdocs.types.search_marker_type
    import aws_sdk_workdocs.types.search_query_scope_type_list
    import aws_sdk_workdocs.types.search_query_type
    import aws_sdk_workdocs.types.search_resources_request
    import aws_sdk_workdocs.types.search_resources_response
    import aws_sdk_workdocs.types.search_result_sort_list
    import aws_sdk_workdocs.types.search_results_limit_type
    import aws_sdk_workdocs.types.share_principal_list
    import aws_sdk_workdocs.types.shared_labels
    import aws_sdk_workdocs.types.size_type
    import aws_sdk_workdocs.types.storage_rule_type
    import aws_sdk_workdocs.types.subscription
    import aws_sdk_workdocs.types.subscription_end_point_type
    import aws_sdk_workdocs.types.subscription_protocol_type
    import aws_sdk_workdocs.types.subscription_type
    import aws_sdk_workdocs.types.time_zone_id_type
    import aws_sdk_workdocs.types.timestamp_type
    import aws_sdk_workdocs.types.update_document_request
    import aws_sdk_workdocs.types.update_document_version_request
    import aws_sdk_workdocs.types.update_folder_request
    import aws_sdk_workdocs.types.update_user_request
    import aws_sdk_workdocs.types.update_user_response
    import aws_sdk_workdocs.types.user
    import aws_sdk_workdocs.types.user_attribute_value_type
    import aws_sdk_workdocs.types.user_filter_type
    import aws_sdk_workdocs.types.user_ids_type
    import aws_sdk_workdocs.types.user_sort_type
    import aws_sdk_workdocs.types.user_type
    import aws_sdk_workdocs.types.username_type


class WorkDocsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class WorkDocsClient:
    """A client for the ``WorkDocs`` service.

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
        self._config = WorkDocsClientConfig(
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
        self, config_overrides: Optional[WorkDocsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WorkDocsClientConfig = config_overrides or {}
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

    def abort_document_version_upload(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Aborts the upload of the specified document version that was previously initiated by <a>InitiateDocumentVersionUpload</a>. The client should make this call only when it no longer intends to upload the document version, or fails to do so.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The ID of the version.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.abort_document_version_upload_request.AbortDocumentVersionUploadRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.abort_document_version_upload

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.abort_document_version_upload.abort_document_version_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.abort_document_version_upload_request.AbortDocumentVersionUploadRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        input_["version_id"] = version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def activate_user(
        self,
        user_id: "aws_sdk_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.activate_user_response.ActivateUserResponse":
        """<p>Activates the specified user. Only active users can access Amazon WorkDocs.</p>

        Args:
            user_id: <p>The ID of the user.</p>
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.activate_user_request.ActivateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.activate_user_response.ActivateUserResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.activate_user

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.activate_user.activate_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.activate_user_request.ActivateUserRequest = {}  # type: ignore[typeddict-item]
        input_["user_id"] = user_id
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def add_resource_permissions(
        self,
        resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        principals: "aws_sdk_workdocs.types.share_principal_list.SharePrincipalList",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        notification_options: Optional[
            "aws_sdk_workdocs.types.notification_options.NotificationOptions"
        ] = None,
    ) -> "aws_sdk_workdocs.types.add_resource_permissions_response.AddResourcePermissionsResponse":
        """<p>Creates a set of permissions for the specified folder or document. The resource permissions are overwritten if the principals already have different permissions.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource.</p>
            principals: <p>The users, groups, or organization being granted permission.</p>
            notification_options: <p>The notification options.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.add_resource_permissions_request.AddResourcePermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.add_resource_permissions_response.AddResourcePermissionsResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.add_resource_permissions

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.add_resource_permissions.add_resource_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.add_resource_permissions_request.AddResourcePermissionsRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["resource_id"] = resource_id
        input_["principals"] = principals
        if notification_options is not None:
            input_["notification_options"] = notification_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_comment(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType",
        text: "aws_sdk_workdocs.types.comment_text_type.CommentTextType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        parent_id: Optional[
            "aws_sdk_workdocs.types.comment_id_type.CommentIdType"
        ] = None,
        thread_id: Optional[
            "aws_sdk_workdocs.types.comment_id_type.CommentIdType"
        ] = None,
        visibility: Optional[
            "aws_sdk_workdocs.types.comment_visibility_type.CommentVisibilityType"
        ] = None,
        notify_collaborators: Optional[
            "aws_sdk_workdocs.types.boolean_type.BooleanType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.create_comment_response.CreateCommentResponse":
        """<p>Adds a new comment to the specified document version.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The ID of the document version.</p>
            parent_id: <p>The ID of the parent comment.</p>
            thread_id: <p>The ID of the root comment in the thread.</p>
            text: <p>The text of the comment.</p>
            visibility: <p>The visibility of the comment. Options are either PRIVATE, where the comment is visible only to the comment author and document owner and co-owners, or PUBLIC, where the comment is visible to document owners, co-owners, and contributors.</p>
            notify_collaborators: <p>Set this parameter to TRUE to send an email out to the document collaborators after the comment is created.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.create_comment_request.CreateCommentRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.create_comment_response.CreateCommentResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_comment

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_comment.create_comment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.create_comment_request.CreateCommentRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        input_["version_id"] = version_id
        if parent_id is not None:
            input_["parent_id"] = parent_id
        if thread_id is not None:
            input_["thread_id"] = thread_id
        input_["text"] = text
        if visibility is not None:
            input_["visibility"] = visibility
        if notify_collaborators is not None:
            input_["notify_collaborators"] = notify_collaborators

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_custom_metadata(
        self,
        resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        custom_metadata: "aws_sdk_workdocs.types.custom_metadata_map.CustomMetadataMap",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        version_id: Optional[
            "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.create_custom_metadata_response.CreateCustomMetadataResponse":
        """<p>Adds one or more custom properties to the specified resource (a folder, document, or version).</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource.</p>
            version_id: <p>The ID of the version, if the custom metadata is being added to a document version.</p>
            custom_metadata: <p>Custom metadata in the form of name-value pairs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.create_custom_metadata_request.CreateCustomMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.create_custom_metadata_response.CreateCustomMetadataResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_custom_metadata

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_custom_metadata.create_custom_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.create_custom_metadata_request.CreateCustomMetadataRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["resource_id"] = resource_id
        if version_id is not None:
            input_["version_id"] = version_id
        input_["custom_metadata"] = custom_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_folder(
        self,
        parent_folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        name: Optional[
            "aws_sdk_workdocs.types.resource_name_type.ResourceNameType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.create_folder_response.CreateFolderResponse":
        """<p>Creates a folder with the specified name and parent folder.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            name: <p>The name of the new folder.</p>
            parent_folder_id: <p>The ID of the parent folder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.create_folder_request.CreateFolderRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.create_folder_response.CreateFolderResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_folder

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_folder.create_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.create_folder_request.CreateFolderRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if name is not None:
            input_["name"] = name
        input_["parent_folder_id"] = parent_folder_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_labels(
        self,
        resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        labels: "aws_sdk_workdocs.types.shared_labels.SharedLabels",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.create_labels_response.CreateLabelsResponse":
        """<p>Adds the specified list of labels to the given resource (a document or folder)</p>

        Args:
            resource_id: <p>The ID of the resource.</p>
            labels: <p>List of labels to add to the resource.</p>
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.create_labels_request.CreateLabelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.create_labels_response.CreateLabelsResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_labels

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_labels.create_labels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.create_labels_request.CreateLabelsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_id"] = resource_id
        input_["labels"] = labels
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_notification_subscription(
        self,
        organization_id: "aws_sdk_workdocs.types.id_type.IdType",
        endpoint: "aws_sdk_workdocs.types.subscription_end_point_type.SubscriptionEndPointType",
        protocol: "aws_sdk_workdocs.types.subscription_protocol_type.SubscriptionProtocolType",
        subscription_type: "aws_sdk_workdocs.types.subscription_type.SubscriptionType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
    ) -> "aws_sdk_workdocs.types.create_notification_subscription_response.CreateNotificationSubscriptionResponse":
        r"""<p>Configure Amazon WorkDocs to use Amazon SNS notifications. The endpoint receives a confirmation message, and must confirm the subscription.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/workdocs/latest/developerguide/manage-notifications.html\">Setting up notifications for an IAM user or role</a> in the <i>Amazon WorkDocs Developer Guide</i>.</p>

        Args:
            organization_id: <p>The ID of the organization.</p>
            endpoint: <p>The endpoint to receive the notifications. If the protocol is HTTPS, the endpoint is a URL that begins with <code>https</code>.</p>
            protocol: <p>The protocol to use. The supported value is https, which delivers JSON-encoded messages using HTTPS POST.</p>
            subscription_type: <p>The notification type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.create_notification_subscription_request.CreateNotificationSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.create_notification_subscription_response.CreateNotificationSubscriptionResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_notification_subscription

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_notification_subscription.create_notification_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.create_notification_subscription_request.CreateNotificationSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        input_["endpoint"] = endpoint
        input_["protocol"] = protocol
        input_["subscription_type"] = subscription_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_user(
        self,
        username: "aws_sdk_workdocs.types.username_type.UsernameType",
        given_name: "aws_sdk_workdocs.types.user_attribute_value_type.UserAttributeValueType",
        surname: "aws_sdk_workdocs.types.user_attribute_value_type.UserAttributeValueType",
        password: "aws_sdk_workdocs.types.password_type.PasswordType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        organization_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        email_address: Optional[
            "aws_sdk_workdocs.types.email_address_type.EmailAddressType"
        ] = None,
        time_zone_id: Optional[
            "aws_sdk_workdocs.types.time_zone_id_type.TimeZoneIdType"
        ] = None,
        storage_rule: Optional[
            "aws_sdk_workdocs.types.storage_rule_type.StorageRuleType"
        ] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.create_user_response.CreateUserResponse":
        r"""<p>Creates a user in a Simple AD or Microsoft AD directory. The status of a newly created user is \"ACTIVE\". New users can access Amazon WorkDocs.</p>

        Args:
            organization_id: <p>The ID of the organization.</p>
            username: <p>The login name of the user.</p>
            email_address: <p>The email address of the user.</p>
            given_name: <p>The given name of the user.</p>
            surname: <p>The surname of the user.</p>
            password: <p>The password of the user.</p>
            time_zone_id: <p>The time zone ID of the user.</p>
            storage_rule: <p>The amount of storage for the user.</p>
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.create_user_response.CreateUserResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_user

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.create_user_request.CreateUserRequest = {}  # type: ignore[typeddict-item]
        if organization_id is not None:
            input_["organization_id"] = organization_id
        input_["username"] = username
        if email_address is not None:
            input_["email_address"] = email_address
        input_["given_name"] = given_name
        input_["surname"] = surname
        input_["password"] = password
        if time_zone_id is not None:
            input_["time_zone_id"] = time_zone_id
        if storage_rule is not None:
            input_["storage_rule"] = storage_rule
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deactivate_user(
        self,
        user_id: "aws_sdk_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Deactivates the specified user, which revokes the user's access to Amazon WorkDocs.</p>

        Args:
            user_id: <p>The ID of the user.</p>
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.deactivate_user_request.DeactivateUserRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.deactivate_user

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.deactivate_user.deactivate_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.deactivate_user_request.DeactivateUserRequest = {}  # type: ignore[typeddict-item]
        input_["user_id"] = user_id
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_comment(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType",
        comment_id: "aws_sdk_workdocs.types.comment_id_type.CommentIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Deletes the specified comment from the document version.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The ID of the document version.</p>
            comment_id: <p>The ID of the comment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.delete_comment_request.DeleteCommentRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_comment

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_comment.delete_comment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.delete_comment_request.DeleteCommentRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        input_["version_id"] = version_id
        input_["comment_id"] = comment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_custom_metadata(
        self,
        resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        version_id: Optional[
            "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType"
        ] = None,
        keys: Optional[
            "aws_sdk_workdocs.types.custom_metadata_key_list.CustomMetadataKeyList"
        ] = None,
        delete_all: Optional["aws_sdk_workdocs.types.boolean_type.BooleanType"] = None,
    ) -> "aws_sdk_workdocs.types.delete_custom_metadata_response.DeleteCustomMetadataResponse":
        """<p>Deletes custom metadata from the specified resource.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource, either a document or folder.</p>
            version_id: <p>The ID of the version, if the custom metadata is being deleted from a document version.</p>
            keys: <p>List of properties to remove.</p>
            delete_all: <p>Flag to indicate removal of all custom metadata properties from the specified resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.delete_custom_metadata_request.DeleteCustomMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.delete_custom_metadata_response.DeleteCustomMetadataResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_custom_metadata

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_custom_metadata.delete_custom_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.delete_custom_metadata_request.DeleteCustomMetadataRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["resource_id"] = resource_id
        if version_id is not None:
            input_["version_id"] = version_id
        if keys is not None:
            input_["keys"] = keys
        if delete_all is not None:
            input_["delete_all"] = delete_all

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_document(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Permanently deletes the specified document and its associated metadata.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.delete_document_request.DeleteDocumentRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_document

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_document.delete_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.delete_document_request.DeleteDocumentRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_document_version(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType",
        delete_prior_versions: "aws_sdk_workdocs.types.boolean_type.BooleanType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Deletes a specific version of a document.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document associated with the version being deleted.</p>
            version_id: <p>The ID of the version being deleted.</p>
            delete_prior_versions: <p>Deletes all versions of a document prior to the current version.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.delete_document_version_request.DeleteDocumentVersionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_document_version

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_document_version.delete_document_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.delete_document_version_request.DeleteDocumentVersionRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        input_["version_id"] = version_id
        input_["delete_prior_versions"] = delete_prior_versions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_folder(
        self,
        folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Permanently deletes the specified folder and its contents.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.delete_folder_request.DeleteFolderRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_folder

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_folder.delete_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.delete_folder_request.DeleteFolderRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["folder_id"] = folder_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_folder_contents(
        self,
        folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Deletes the contents of the specified folder.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.delete_folder_contents_request.DeleteFolderContentsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_folder_contents

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_folder_contents.delete_folder_contents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.delete_folder_contents_request.DeleteFolderContentsRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["folder_id"] = folder_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_labels(
        self,
        resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        labels: Optional["aws_sdk_workdocs.types.shared_labels.SharedLabels"] = None,
        delete_all: Optional["aws_sdk_workdocs.types.boolean_type.BooleanType"] = None,
    ) -> "aws_sdk_workdocs.types.delete_labels_response.DeleteLabelsResponse":
        """<p>Deletes the specified list of labels from a resource.</p>

        Args:
            resource_id: <p>The ID of the resource.</p>
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            labels: <p>List of labels to delete from the resource.</p>
            delete_all: <p>Flag to request removal of all labels from the specified resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.delete_labels_request.DeleteLabelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.delete_labels_response.DeleteLabelsResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_labels

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_labels.delete_labels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.delete_labels_request.DeleteLabelsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_id"] = resource_id
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if labels is not None:
            input_["labels"] = labels
        if delete_all is not None:
            input_["delete_all"] = delete_all

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_notification_subscription(
        self,
        subscription_id: "aws_sdk_workdocs.types.id_type.IdType",
        organization_id: "aws_sdk_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified subscription from the specified organization.</p>

        Args:
            subscription_id: <p>The ID of the subscription.</p>
            organization_id: <p>The ID of the organization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.delete_notification_subscription_request.DeleteNotificationSubscriptionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_notification_subscription

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_notification_subscription.delete_notification_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.delete_notification_subscription_request.DeleteNotificationSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["subscription_id"] = subscription_id
        input_["organization_id"] = organization_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_user(
        self,
        user_id: "aws_sdk_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Deletes the specified user from a Simple AD or Microsoft AD directory.</p> <important> <p>Deleting a user immediately and permanently deletes all content in that user's folder structure. Site retention policies do NOT apply to this type of deletion.</p> </important>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using Amazon Web Services credentials.</p>
            user_id: <p>The ID of the user.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_user

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.delete_user.delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.delete_user_request.DeleteUserRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_activities(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        start_time: Optional[
            "aws_sdk_workdocs.types.timestamp_type.TimestampType"
        ] = None,
        end_time: Optional[
            "aws_sdk_workdocs.types.timestamp_type.TimestampType"
        ] = None,
        organization_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        activity_types: Optional[
            "aws_sdk_workdocs.types.activity_names_filter_type.ActivityNamesFilterType"
        ] = None,
        resource_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        user_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        include_indirect_activities: Optional[
            "aws_sdk_workdocs.types.boolean_type.BooleanType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.search_marker_type.SearchMarkerType"
        ] = None,
    ) -> (
        "aws_sdk_workdocs.types.describe_activities_response.DescribeActivitiesResponse"
    ):
        """<p>Describes the user activities in a specified time period.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            start_time: <p>The timestamp that determines the starting time of the activities. The response includes the activities performed after the specified timestamp.</p>
            end_time: <p>The timestamp that determines the end time of the activities. The response includes the activities performed before the specified timestamp.</p>
            organization_id: <p>The ID of the organization. This is a mandatory parameter when using administrative API (SigV4) requests.</p>
            activity_types: <p>Specifies which activity types to include in the response. If this field is left empty, all activity types are returned.</p>
            resource_id: <p>The document or folder ID for which to describe activity types.</p>
            user_id: <p>The ID of the user who performed the action. The response includes activities pertaining to this user. This is an optional parameter and is only applicable for administrative API (SigV4) requests.</p>
            include_indirect_activities: <p>Includes indirect activities. An indirect activity results from a direct activity performed on a parent resource. For example, sharing a parent folder (the direct activity) shares all of the subfolders and documents within the parent folder (the indirect activity).</p>
            limit: <p>The maximum number of items to return.</p>
            marker: <p>The marker for the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.describe_activities_request.DescribeActivitiesRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.describe_activities_response.DescribeActivitiesResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_activities

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_activities.describe_activities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.describe_activities_request.DescribeActivitiesRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if activity_types is not None:
            input_["activity_types"] = activity_types
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if user_id is not None:
            input_["user_id"] = user_id
        if include_indirect_activities is not None:
            input_["include_indirect_activities"] = include_indirect_activities
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_activities(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        start_time: Optional[
            "aws_sdk_workdocs.types.timestamp_type.TimestampType"
        ] = None,
        end_time: Optional[
            "aws_sdk_workdocs.types.timestamp_type.TimestampType"
        ] = None,
        organization_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        activity_types: Optional[
            "aws_sdk_workdocs.types.activity_names_filter_type.ActivityNamesFilterType"
        ] = None,
        resource_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        user_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        include_indirect_activities: Optional[
            "aws_sdk_workdocs.types.boolean_type.BooleanType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.search_marker_type.SearchMarkerType"
        ] = None,
    ) -> "Iterator[aws_sdk_workdocs.types.activity.Activity]":
        _token = marker
        while True:
            _response = self.describe_activities(
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                start_time=start_time,
                end_time=end_time,
                organization_id=organization_id,
                activity_types=activity_types,
                resource_id=resource_id,
                user_id=user_id,
                include_indirect_activities=include_indirect_activities,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("user_activities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_comments(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["aws_sdk_workdocs.types.marker_type.MarkerType"] = None,
    ) -> "aws_sdk_workdocs.types.describe_comments_response.DescribeCommentsResponse":
        """<p>List all the comments for the specified document version.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The ID of the document version.</p>
            limit: <p>The maximum number of items to return.</p>
            marker: <p>The marker for the next set of results. This marker was received from a previous call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.describe_comments_request.DescribeCommentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.describe_comments_response.DescribeCommentsResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_comments

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_comments.describe_comments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.describe_comments_request.DescribeCommentsRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        input_["version_id"] = version_id
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_comments(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["aws_sdk_workdocs.types.marker_type.MarkerType"] = None,
    ) -> "Iterator[aws_sdk_workdocs.types.comment.Comment]":
        _token = marker
        while True:
            _response = self.describe_comments(
                document_id,
                version_id,
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("comments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_document_versions(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        include: Optional[
            "aws_sdk_workdocs.types.field_names_type.FieldNamesType"
        ] = None,
        fields: Optional[
            "aws_sdk_workdocs.types.field_names_type.FieldNamesType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.describe_document_versions_response.DescribeDocumentVersionsResponse":
        r"""<p>Retrieves the document versions for the specified document.</p> <p>By default, only active versions are returned.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            limit: <p>The maximum number of versions to return with this call.</p>
            include: <p>A comma-separated list of values. Specify \"INITIALIZED\" to include incomplete versions.</p>
            fields: <p>Specify \"SOURCE\" to include initialized versions and a URL for the source document.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.describe_document_versions_request.DescribeDocumentVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.describe_document_versions_response.DescribeDocumentVersionsResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_document_versions

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_document_versions.describe_document_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.describe_document_versions_request.DescribeDocumentVersionsRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit
        if include is not None:
            input_["include"] = include
        if fields is not None:
            input_["fields"] = fields

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_document_versions(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        include: Optional[
            "aws_sdk_workdocs.types.field_names_type.FieldNamesType"
        ] = None,
        fields: Optional[
            "aws_sdk_workdocs.types.field_names_type.FieldNamesType"
        ] = None,
    ) -> "Iterator[aws_sdk_workdocs.types.document_version_metadata.DocumentVersionMetadata]":
        _token = marker
        while True:
            _response = self.describe_document_versions(
                document_id,
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                marker=_token,
                limit=limit,
                include=include,
                fields=fields,
            )
            _page = _resolve_path(_response, ("document_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_folder_contents(
        self,
        folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        sort: Optional[
            "aws_sdk_workdocs.types.resource_sort_type.ResourceSortType"
        ] = None,
        order: Optional["aws_sdk_workdocs.types.order_type.OrderType"] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
        type: Optional[
            "aws_sdk_workdocs.types.folder_content_type.FolderContentType"
        ] = None,
        include: Optional[
            "aws_sdk_workdocs.types.field_names_type.FieldNamesType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.describe_folder_contents_response.DescribeFolderContentsResponse":
        r"""<p>Describes the contents of the specified folder, including its documents and subfolders.</p> <p>By default, Amazon WorkDocs returns the first 100 active document and folder metadata items. If there are more results, the response includes a marker that you can use to request the next set of results. You can also request initialized documents.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>
            sort: <p>The sorting criteria.</p>
            order: <p>The order for the contents of the folder.</p>
            limit: <p>The maximum number of items to return with this call.</p>
            marker: <p>The marker for the next set of results. This marker was received from a previous call.</p>
            type: <p>The type of items.</p>
            include: <p>The contents to include. Specify \"INITIALIZED\" to include initialized documents.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.describe_folder_contents_request.DescribeFolderContentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.describe_folder_contents_response.DescribeFolderContentsResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_folder_contents

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_folder_contents.describe_folder_contents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.describe_folder_contents_request.DescribeFolderContentsRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["folder_id"] = folder_id
        if sort is not None:
            input_["sort"] = sort
        if order is not None:
            input_["order"] = order
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker
        if type is not None:
            input_["type"] = type
        if include is not None:
            input_["include"] = include

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_groups(
        self,
        search_query: "aws_sdk_workdocs.types.search_query_type.SearchQueryType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        organization_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        marker: Optional["aws_sdk_workdocs.types.marker_type.MarkerType"] = None,
        limit: Optional[
            "aws_sdk_workdocs.types.positive_integer_type.PositiveIntegerType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.describe_groups_response.DescribeGroupsResponse":
        """<p>Describes the groups specified by the query. Groups are defined by the underlying Active Directory.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            search_query: <p>A query to describe groups by group name.</p>
            organization_id: <p>The ID of the organization.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            limit: <p>The maximum number of items to return with this call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.describe_groups_request.DescribeGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.describe_groups_response.DescribeGroupsResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_groups

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_groups.describe_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.describe_groups_request.DescribeGroupsRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["search_query"] = search_query
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_groups(
        self,
        search_query: "aws_sdk_workdocs.types.search_query_type.SearchQueryType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        organization_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        marker: Optional["aws_sdk_workdocs.types.marker_type.MarkerType"] = None,
        limit: Optional[
            "aws_sdk_workdocs.types.positive_integer_type.PositiveIntegerType"
        ] = None,
    ) -> "Iterator[aws_sdk_workdocs.types.group_metadata.GroupMetadata]":
        _token = marker
        while True:
            _response = self.describe_groups(
                search_query,
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                organization_id=organization_id,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_notification_subscriptions(
        self,
        organization_id: "aws_sdk_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
    ) -> "aws_sdk_workdocs.types.describe_notification_subscriptions_response.DescribeNotificationSubscriptionsResponse":
        """<p>Lists the specified notification subscriptions.</p>

        Args:
            organization_id: <p>The ID of the organization.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            limit: <p>The maximum number of items to return with this call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.describe_notification_subscriptions_request.DescribeNotificationSubscriptionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.describe_notification_subscriptions_response.DescribeNotificationSubscriptionsResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_notification_subscriptions

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_notification_subscriptions.describe_notification_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.describe_notification_subscriptions_request.DescribeNotificationSubscriptionsRequest = {}  # type: ignore[typeddict-item]
        input_["organization_id"] = organization_id
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_notification_subscriptions(
        self,
        organization_id: "aws_sdk_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
    ) -> "Iterator[aws_sdk_workdocs.types.subscription.Subscription]":
        _token = marker
        while True:
            _response = self.describe_notification_subscriptions(
                organization_id,
                config_overrides=config_overrides,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_resource_permissions(
        self,
        resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        principal_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.describe_resource_permissions_response.DescribeResourcePermissionsResponse":
        """<p>Describes the permissions of a specified resource.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource.</p>
            principal_id: <p>The ID of the principal to filter permissions by.</p>
            limit: <p>The maximum number of items to return with this call.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call)</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.describe_resource_permissions_request.DescribeResourcePermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.describe_resource_permissions_response.DescribeResourcePermissionsResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_resource_permissions

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_resource_permissions.describe_resource_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.describe_resource_permissions_request.DescribeResourcePermissionsRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["resource_id"] = resource_id
        if principal_id is not None:
            input_["principal_id"] = principal_id
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_resource_permissions(
        self,
        resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        principal_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
    ) -> "Iterator[aws_sdk_workdocs.types.principal.Principal]":
        _token = marker
        while True:
            _response = self.describe_resource_permissions(
                resource_id,
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                principal_id=principal_id,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("principals",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_root_folders(
        self,
        authentication_token: "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.describe_root_folders_response.DescribeRootFoldersResponse":
        r"""<p>Describes the current user's special folders; the <code>RootFolder</code> and the <code>RecycleBin</code>. <code>RootFolder</code> is the root of user's files and folders and <code>RecycleBin</code> is the root of recycled items. This is not a valid action for SigV4 (administrative API) clients.</p> <p>This action requires an authentication token. To get an authentication token, register an application with Amazon WorkDocs. For more information, see <a href=\"https://docs.aws.amazon.com/workdocs/latest/developerguide/wd-auth-user.html\">Authentication and Access Control for User Applications</a> in the <i>Amazon WorkDocs Developer Guide</i>.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token.</p>
            limit: <p>The maximum number of items to return.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.describe_root_folders_request.DescribeRootFoldersRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.describe_root_folders_response.DescribeRootFoldersResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_root_folders

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_root_folders.describe_root_folders(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.describe_root_folders_request.DescribeRootFoldersRequest = {}  # type: ignore[typeddict-item]
        input_["authentication_token"] = authentication_token
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_root_folders(
        self,
        authentication_token: "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
    ) -> "Iterator[aws_sdk_workdocs.types.folder_metadata.FolderMetadata]":
        _token = marker
        while True:
            _response = self.describe_root_folders(
                authentication_token,
                config_overrides=config_overrides,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("folders",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_users(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        organization_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        user_ids: Optional["aws_sdk_workdocs.types.user_ids_type.UserIdsType"] = None,
        query: Optional[
            "aws_sdk_workdocs.types.search_query_type.SearchQueryType"
        ] = None,
        include: Optional[
            "aws_sdk_workdocs.types.user_filter_type.UserFilterType"
        ] = None,
        order: Optional["aws_sdk_workdocs.types.order_type.OrderType"] = None,
        sort: Optional["aws_sdk_workdocs.types.user_sort_type.UserSortType"] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        fields: Optional[
            "aws_sdk_workdocs.types.field_names_type.FieldNamesType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.describe_users_response.DescribeUsersResponse":
        r"""<p>Describes the specified users. You can describe all users or filter the results (for example, by status or organization).</p> <p>By default, Amazon WorkDocs returns the first 24 active or pending users. If there are more results, the response includes a marker that you can use to request the next set of results.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            organization_id: <p>The ID of the organization.</p>
            user_ids: <p>The IDs of the users.</p>
            query: <p>A query to filter users by user name. Remember the following about the <code>Userids</code> and <code>Query</code> parameters:</p> <ul> <li> <p>If you don't use either parameter, the API returns a paginated list of all users on the site.</p> </li> <li> <p>If you use both parameters, the API ignores the <code>Query</code> parameter.</p> </li> <li> <p>The <code>Userid</code> parameter only returns user names that match a corresponding user ID.</p> </li> <li> <p>The <code>Query</code> parameter runs a \"prefix\" search for users by the <code>GivenName</code>, <code>SurName</code>, or <code>UserName</code> fields included in a <a href=\"https://docs.aws.amazon.com/workdocs/latest/APIReference/API_CreateUser.html\">CreateUser</a> API call. For example, querying on <code>Ma</code> returns Márcia Oliveira, María García, and Mateo Jackson. If you use multiple characters, the API only returns data that matches all characters. For example, querying on <code>Ma J</code> only returns Mateo Jackson.</p> </li> </ul>
            include: <p>The state of the users. Specify \"ALL\" to include inactive users.</p>
            order: <p>The order for the results.</p>
            sort: <p>The sorting criteria.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            limit: <p>The maximum number of items to return.</p>
            fields: <p>A comma-separated list of values. Specify \"STORAGE_METADATA\" to include the user storage quota and utilization information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.describe_users_request.DescribeUsersRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.describe_users_response.DescribeUsersResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_users

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.describe_users.describe_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.describe_users_request.DescribeUsersRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if user_ids is not None:
            input_["user_ids"] = user_ids
        if query is not None:
            input_["query"] = query
        if include is not None:
            input_["include"] = include
        if order is not None:
            input_["order"] = order
        if sort is not None:
            input_["sort"] = sort
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit
        if fields is not None:
            input_["fields"] = fields

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_describe_users(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        organization_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        user_ids: Optional["aws_sdk_workdocs.types.user_ids_type.UserIdsType"] = None,
        query: Optional[
            "aws_sdk_workdocs.types.search_query_type.SearchQueryType"
        ] = None,
        include: Optional[
            "aws_sdk_workdocs.types.user_filter_type.UserFilterType"
        ] = None,
        order: Optional["aws_sdk_workdocs.types.order_type.OrderType"] = None,
        sort: Optional["aws_sdk_workdocs.types.user_sort_type.UserSortType"] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        fields: Optional[
            "aws_sdk_workdocs.types.field_names_type.FieldNamesType"
        ] = None,
    ) -> "Iterator[aws_sdk_workdocs.types.user.User]":
        _token = marker
        while True:
            _response = self.describe_users(
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                organization_id=organization_id,
                user_ids=user_ids,
                query=query,
                include=include,
                order=order,
                sort=sort,
                marker=_token,
                limit=limit,
                fields=fields,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def get_current_user(
        self,
        authentication_token: "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
    ) -> "aws_sdk_workdocs.types.get_current_user_response.GetCurrentUserResponse":
        r"""<p>Retrieves details of the current user for whom the authentication token was generated. This is not a valid action for SigV4 (administrative API) clients.</p> <p>This action requires an authentication token. To get an authentication token, register an application with Amazon WorkDocs. For more information, see <a href=\"https://docs.aws.amazon.com/workdocs/latest/developerguide/wd-auth-user.html\">Authentication and Access Control for User Applications</a> in the <i>Amazon WorkDocs Developer Guide</i>.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.get_current_user_request.GetCurrentUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.get_current_user_response.GetCurrentUserResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_current_user

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_current_user.get_current_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.get_current_user_request.GetCurrentUserRequest = {}  # type: ignore[typeddict-item]
        input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_document(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        include_custom_metadata: Optional[
            "aws_sdk_workdocs.types.boolean_type.BooleanType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.get_document_response.GetDocumentResponse":
        """<p>Retrieves details of a document.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            include_custom_metadata: <p>Set this to <code>TRUE</code> to include custom metadata in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.get_document_request.GetDocumentRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.get_document_response.GetDocumentResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_document

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_document.get_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.get_document_request.GetDocumentRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        if include_custom_metadata is not None:
            input_["include_custom_metadata"] = include_custom_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_document_path(
        self,
        document_id: "aws_sdk_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        fields: Optional[
            "aws_sdk_workdocs.types.field_names_type.FieldNamesType"
        ] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.get_document_path_response.GetDocumentPathResponse":
        """<p>Retrieves the path information (the hierarchy from the root folder) for the requested document.</p> <p>By default, Amazon WorkDocs returns a maximum of 100 levels upwards from the requested document and only includes the IDs of the parent folders in the path. You can limit the maximum number of levels. You can also request the names of the parent folders.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            limit: <p>The maximum number of levels in the hierarchy to return.</p>
            fields: <p>A comma-separated list of values. Specify <code>NAME</code> to include the names of the parent folders.</p>
            marker: <p>This value is not supported.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.get_document_path_request.GetDocumentPathRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.get_document_path_response.GetDocumentPathResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_document_path

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_document_path.get_document_path(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.get_document_path_request.GetDocumentPathRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        if limit is not None:
            input_["limit"] = limit
        if fields is not None:
            input_["fields"] = fields
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_document_version(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        fields: Optional[
            "aws_sdk_workdocs.types.field_names_type.FieldNamesType"
        ] = None,
        include_custom_metadata: Optional[
            "aws_sdk_workdocs.types.boolean_type.BooleanType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.get_document_version_response.GetDocumentVersionResponse":
        r"""<p>Retrieves version metadata for the specified document.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The version ID of the document.</p>
            fields: <p>A comma-separated list of values. Specify \"SOURCE\" to include a URL for the source document.</p>
            include_custom_metadata: <p>Set this to TRUE to include custom metadata in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.get_document_version_request.GetDocumentVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.get_document_version_response.GetDocumentVersionResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_document_version

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_document_version.get_document_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.get_document_version_request.GetDocumentVersionRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        input_["version_id"] = version_id
        if fields is not None:
            input_["fields"] = fields
        if include_custom_metadata is not None:
            input_["include_custom_metadata"] = include_custom_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_folder(
        self,
        folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        include_custom_metadata: Optional[
            "aws_sdk_workdocs.types.boolean_type.BooleanType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.get_folder_response.GetFolderResponse":
        """<p>Retrieves the metadata of the specified folder.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>
            include_custom_metadata: <p>Set to TRUE to include custom metadata in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.get_folder_request.GetFolderRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.get_folder_response.GetFolderResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_folder

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_folder.get_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.get_folder_request.GetFolderRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["folder_id"] = folder_id
        if include_custom_metadata is not None:
            input_["include_custom_metadata"] = include_custom_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_folder_path(
        self,
        folder_id: "aws_sdk_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        fields: Optional[
            "aws_sdk_workdocs.types.field_names_type.FieldNamesType"
        ] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.get_folder_path_response.GetFolderPathResponse":
        r"""<p>Retrieves the path information (the hierarchy from the root folder) for the specified folder.</p> <p>By default, Amazon WorkDocs returns a maximum of 100 levels upwards from the requested folder and only includes the IDs of the parent folders in the path. You can limit the maximum number of levels. You can also request the parent folder names.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>
            limit: <p>The maximum number of levels in the hierarchy to return.</p>
            fields: <p>A comma-separated list of values. Specify \"NAME\" to include the names of the parent folders.</p>
            marker: <p>This value is not supported.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.get_folder_path_request.GetFolderPathRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.get_folder_path_response.GetFolderPathResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_folder_path

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_folder_path.get_folder_path(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.get_folder_path_request.GetFolderPathRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["folder_id"] = folder_id
        if limit is not None:
            input_["limit"] = limit
        if fields is not None:
            input_["fields"] = fields
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resources(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        user_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        collection_type: Optional[
            "aws_sdk_workdocs.types.resource_collection_type.ResourceCollectionType"
        ] = None,
        limit: Optional["aws_sdk_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.page_marker_type.PageMarkerType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.get_resources_response.GetResourcesResponse":
        """<p>Retrieves a collection of resources, including folders and documents. The only <code>CollectionType</code> supported is <code>SHARED_WITH_ME</code>.</p>

        Args:
            authentication_token: <p>The Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            user_id: <p>The user ID for the resource collection. This is a required field for accessing the API operation using IAM credentials.</p>
            collection_type: <p>The collection type.</p>
            limit: <p>The maximum number of resources to return.</p>
            marker: <p>The marker for the next set of results. This marker was received from a previous call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.get_resources_request.GetResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.get_resources_response.GetResourcesResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_resources

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.get_resources.get_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.get_resources_request.GetResourcesRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if user_id is not None:
            input_["user_id"] = user_id
        if collection_type is not None:
            input_["collection_type"] = collection_type
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def initiate_document_version_upload(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        id: Optional["aws_sdk_workdocs.types.resource_id_type.ResourceIdType"] = None,
        name: Optional[
            "aws_sdk_workdocs.types.resource_name_type.ResourceNameType"
        ] = None,
        content_created_timestamp: Optional[
            "aws_sdk_workdocs.types.timestamp_type.TimestampType"
        ] = None,
        content_modified_timestamp: Optional[
            "aws_sdk_workdocs.types.timestamp_type.TimestampType"
        ] = None,
        content_type: Optional[
            "aws_sdk_workdocs.types.document_content_type.DocumentContentType"
        ] = None,
        document_size_in_bytes: Optional[
            "aws_sdk_workdocs.types.size_type.SizeType"
        ] = None,
        parent_folder_id: Optional[
            "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.initiate_document_version_upload_response.InitiateDocumentVersionUploadResponse":
        """<p>Creates a new document object and version object.</p> <p>The client specifies the parent folder ID and name of the document to upload. The ID is optionally specified when creating a new version of an existing document. This is the first step to upload a document. Next, upload the document to the URL returned from the call, and then call <a>UpdateDocumentVersion</a>.</p> <p>To cancel the document upload, call <a>AbortDocumentVersionUpload</a>.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            id: <p>The ID of the document.</p>
            name: <p>The name of the document.</p>
            content_created_timestamp: <p>The timestamp when the content of the document was originally created.</p>
            content_modified_timestamp: <p>The timestamp when the content of the document was modified.</p>
            content_type: <p>The content type of the document.</p>
            document_size_in_bytes: <p>The size of the document, in bytes.</p>
            parent_folder_id: <p>The ID of the parent folder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.initiate_document_version_upload_request.InitiateDocumentVersionUploadRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.initiate_document_version_upload_response.InitiateDocumentVersionUploadResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.initiate_document_version_upload

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.initiate_document_version_upload.initiate_document_version_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.initiate_document_version_upload_request.InitiateDocumentVersionUploadRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if id is not None:
            input_["id"] = id
        if name is not None:
            input_["name"] = name
        if content_created_timestamp is not None:
            input_["content_created_timestamp"] = content_created_timestamp
        if content_modified_timestamp is not None:
            input_["content_modified_timestamp"] = content_modified_timestamp
        if content_type is not None:
            input_["content_type"] = content_type
        if document_size_in_bytes is not None:
            input_["document_size_in_bytes"] = document_size_in_bytes
        if parent_folder_id is not None:
            input_["parent_folder_id"] = parent_folder_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_all_resource_permissions(
        self,
        resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Removes all the permissions from the specified resource.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.remove_all_resource_permissions_request.RemoveAllResourcePermissionsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.remove_all_resource_permissions

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.remove_all_resource_permissions.remove_all_resource_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.remove_all_resource_permissions_request.RemoveAllResourcePermissionsRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["resource_id"] = resource_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_resource_permission(
        self,
        resource_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        principal_id: "aws_sdk_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        principal_type: Optional[
            "aws_sdk_workdocs.types.principal_type.PrincipalType"
        ] = None,
    ) -> None:
        """<p>Removes the permission for the specified principal from the specified resource.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource.</p>
            principal_id: <p>The principal ID of the resource.</p>
            principal_type: <p>The principal type of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.remove_resource_permission_request.RemoveResourcePermissionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.remove_resource_permission

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.remove_resource_permission.remove_resource_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.remove_resource_permission_request.RemoveResourcePermissionRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["resource_id"] = resource_id
        input_["principal_id"] = principal_id
        if principal_type is not None:
            input_["principal_type"] = principal_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def restore_document_versions(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Recovers a deleted version of an Amazon WorkDocs document.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.restore_document_versions_request.RestoreDocumentVersionsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.restore_document_versions

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.restore_document_versions.restore_document_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.restore_document_versions_request.RestoreDocumentVersionsRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_resources(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        query_text: Optional[
            "aws_sdk_workdocs.types.search_query_type.SearchQueryType"
        ] = None,
        query_scopes: Optional[
            "aws_sdk_workdocs.types.search_query_scope_type_list.SearchQueryScopeTypeList"
        ] = None,
        organization_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        additional_response_fields: Optional[
            "aws_sdk_workdocs.types.additional_response_fields_list.AdditionalResponseFieldsList"
        ] = None,
        filters: Optional["aws_sdk_workdocs.types.filters.Filters"] = None,
        order_by: Optional[
            "aws_sdk_workdocs.types.search_result_sort_list.SearchResultSortList"
        ] = None,
        limit: Optional[
            "aws_sdk_workdocs.types.search_results_limit_type.SearchResultsLimitType"
        ] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.next_marker_type.NextMarkerType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.search_resources_response.SearchResourcesResponse":
        """<p>Searches metadata and the content of folders, documents, document versions, and comments.</p>

        Args:
            authentication_token: <p>WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            query_text: <p>The String to search for. Searches across different text fields based on request parameters. Use double quotes around the query string for exact phrase matches.</p>
            query_scopes: <p>Filter based on the text field type. A Folder has only a name and no content. A Comment has only content and no name. A Document or Document Version has a name and content</p>
            organization_id: <p>Filters based on the resource owner OrgId. This is a mandatory parameter when using Admin SigV4 credentials.</p>
            additional_response_fields: <p>A list of attributes to include in the response. Used to request fields that are not normally returned in a standard response.</p>
            filters: <p>Filters results based on entity metadata.</p>
            order_by: <p>Order by results in one or more categories.</p>
            limit: <p>Max results count per page.</p>
            marker: <p>The marker for the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.search_resources_request.SearchResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.search_resources_response.SearchResourcesResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.search_resources

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.search_resources.search_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.search_resources_request.SearchResourcesRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if query_text is not None:
            input_["query_text"] = query_text
        if query_scopes is not None:
            input_["query_scopes"] = query_scopes
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if additional_response_fields is not None:
            input_["additional_response_fields"] = additional_response_fields
        if filters is not None:
            input_["filters"] = filters
        if order_by is not None:
            input_["order_by"] = order_by
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_search_resources(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        query_text: Optional[
            "aws_sdk_workdocs.types.search_query_type.SearchQueryType"
        ] = None,
        query_scopes: Optional[
            "aws_sdk_workdocs.types.search_query_scope_type_list.SearchQueryScopeTypeList"
        ] = None,
        organization_id: Optional["aws_sdk_workdocs.types.id_type.IdType"] = None,
        additional_response_fields: Optional[
            "aws_sdk_workdocs.types.additional_response_fields_list.AdditionalResponseFieldsList"
        ] = None,
        filters: Optional["aws_sdk_workdocs.types.filters.Filters"] = None,
        order_by: Optional[
            "aws_sdk_workdocs.types.search_result_sort_list.SearchResultSortList"
        ] = None,
        limit: Optional[
            "aws_sdk_workdocs.types.search_results_limit_type.SearchResultsLimitType"
        ] = None,
        marker: Optional[
            "aws_sdk_workdocs.types.next_marker_type.NextMarkerType"
        ] = None,
    ) -> "Iterator[aws_sdk_workdocs.types.response_item.ResponseItem]":
        _token = marker
        while True:
            _response = self.search_resources(
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                query_text=query_text,
                query_scopes=query_scopes,
                organization_id=organization_id,
                additional_response_fields=additional_response_fields,
                filters=filters,
                order_by=order_by,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def update_document(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        name: Optional[
            "aws_sdk_workdocs.types.resource_name_type.ResourceNameType"
        ] = None,
        parent_folder_id: Optional[
            "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
        ] = None,
        resource_state: Optional[
            "aws_sdk_workdocs.types.resource_state_type.ResourceStateType"
        ] = None,
    ) -> None:
        """<p>Updates the specified attributes of a document. The user must have access to both the document and its parent folder, if applicable.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            name: <p>The name of the document.</p>
            parent_folder_id: <p>The ID of the parent folder.</p>
            resource_state: <p>The resource state of the document. Only ACTIVE and RECYCLED are supported.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.update_document_request.UpdateDocumentRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.update_document

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.update_document.update_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.update_document_request.UpdateDocumentRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        if name is not None:
            input_["name"] = name
        if parent_folder_id is not None:
            input_["parent_folder_id"] = parent_folder_id
        if resource_state is not None:
            input_["resource_state"] = resource_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_document_version(
        self,
        document_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "aws_sdk_workdocs.types.document_version_id_type.DocumentVersionIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        version_status: Optional[
            "aws_sdk_workdocs.types.document_version_status.DocumentVersionStatus"
        ] = None,
    ) -> None:
        """<p>Changes the status of the document version to ACTIVE. </p> <p>Amazon WorkDocs also sets its document container to ACTIVE. This is the last step in a document upload, after the client uploads the document to an S3-presigned URL returned by <a>InitiateDocumentVersionUpload</a>. </p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The version ID of the document.</p>
            version_status: <p>The status of the version.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.update_document_version_request.UpdateDocumentVersionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.update_document_version

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.update_document_version.update_document_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.update_document_version_request.UpdateDocumentVersionRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["document_id"] = document_id
        input_["version_id"] = version_id
        if version_status is not None:
            input_["version_status"] = version_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_folder(
        self,
        folder_id: "aws_sdk_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        name: Optional[
            "aws_sdk_workdocs.types.resource_name_type.ResourceNameType"
        ] = None,
        parent_folder_id: Optional[
            "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
        ] = None,
        resource_state: Optional[
            "aws_sdk_workdocs.types.resource_state_type.ResourceStateType"
        ] = None,
    ) -> None:
        """<p>Updates the specified attributes of the specified folder. The user must have access to both the folder and its parent folder, if applicable.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>
            name: <p>The name of the folder.</p>
            parent_folder_id: <p>The ID of the parent folder.</p>
            resource_state: <p>The resource state of the folder. Only ACTIVE and RECYCLED are accepted values from the API.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.update_folder_request.UpdateFolderRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.update_folder

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.update_folder.update_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.update_folder_request.UpdateFolderRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["folder_id"] = folder_id
        if name is not None:
            input_["name"] = name
        if parent_folder_id is not None:
            input_["parent_folder_id"] = parent_folder_id
        if resource_state is not None:
            input_["resource_state"] = resource_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_user(
        self,
        user_id: "aws_sdk_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        given_name: Optional[
            "aws_sdk_workdocs.types.user_attribute_value_type.UserAttributeValueType"
        ] = None,
        surname: Optional[
            "aws_sdk_workdocs.types.user_attribute_value_type.UserAttributeValueType"
        ] = None,
        type: Optional["aws_sdk_workdocs.types.user_type.UserType"] = None,
        storage_rule: Optional[
            "aws_sdk_workdocs.types.storage_rule_type.StorageRuleType"
        ] = None,
        time_zone_id: Optional[
            "aws_sdk_workdocs.types.time_zone_id_type.TimeZoneIdType"
        ] = None,
        locale: Optional["aws_sdk_workdocs.types.locale_type.LocaleType"] = None,
        grant_poweruser_privileges: Optional[
            "aws_sdk_workdocs.types.boolean_enum_type.BooleanEnumType"
        ] = None,
    ) -> "aws_sdk_workdocs.types.update_user_response.UpdateUserResponse":
        """<p>Updates the specified attributes of the specified user, and grants or revokes administrative privileges to the Amazon WorkDocs site.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            user_id: <p>The ID of the user.</p>
            given_name: <p>The given name of the user.</p>
            surname: <p>The surname of the user.</p>
            type: <p>The type of the user.</p>
            storage_rule: <p>The amount of storage for the user.</p>
            time_zone_id: <p>The time zone ID of the user.</p>
            locale: <p>The locale of the user.</p>
            grant_poweruser_privileges: <p>Boolean value to determine whether the user is granted Power user privileges.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_workdocs.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_workdocs.types.update_user_response.UpdateUserResponse"
        ]:
            import aws_sdk_workdocs._operations.aws_gorilla_boy_service.update_user

            output, http_response = (
                aws_sdk_workdocs._operations.aws_gorilla_boy_service.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_workdocs.types.update_user_request.UpdateUserRequest = {}  # type: ignore[typeddict-item]
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        input_["user_id"] = user_id
        if given_name is not None:
            input_["given_name"] = given_name
        if surname is not None:
            input_["surname"] = surname
        if type is not None:
            input_["type"] = type
        if storage_rule is not None:
            input_["storage_rule"] = storage_rule
        if time_zone_id is not None:
            input_["time_zone_id"] = time_zone_id
        if locale is not None:
            input_["locale"] = locale
        if grant_poweruser_privileges is not None:
            input_["grant_poweruser_privileges"] = grant_poweruser_privileges

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
