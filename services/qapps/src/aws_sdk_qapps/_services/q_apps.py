"""Generated from Smithy shape ``com.amazonaws.qapps#QAppsService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_qapps._auth._signers
import aws_sdk_qapps._auth._sigv4
from aws_sdk_qapps._auth._identity import Credentials
from aws_sdk_qapps._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_qapps._auth._zapros_handler import AuthMiddleware
from aws_sdk_qapps._pagination import resolve_path as _resolve_path
from aws_sdk_qapps._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_qapps.types.amazon_resource_name
    import aws_sdk_qapps.types.app_definition_input
    import aws_sdk_qapps.types.app_version
    import aws_sdk_qapps.types.associate_library_item_review_input
    import aws_sdk_qapps.types.associate_q_app_with_user_input
    import aws_sdk_qapps.types.batch_create_category_input
    import aws_sdk_qapps.types.batch_create_category_input_category_list
    import aws_sdk_qapps.types.batch_delete_category_input
    import aws_sdk_qapps.types.batch_update_category_input
    import aws_sdk_qapps.types.card_value_list
    import aws_sdk_qapps.types.category_id_list
    import aws_sdk_qapps.types.category_list_input
    import aws_sdk_qapps.types.create_library_item_input
    import aws_sdk_qapps.types.create_library_item_output
    import aws_sdk_qapps.types.create_presigned_url_input
    import aws_sdk_qapps.types.create_presigned_url_output
    import aws_sdk_qapps.types.create_q_app_input
    import aws_sdk_qapps.types.create_q_app_output
    import aws_sdk_qapps.types.delete_category_input_list
    import aws_sdk_qapps.types.delete_library_item_input
    import aws_sdk_qapps.types.delete_q_app_input
    import aws_sdk_qapps.types.describe_q_app_permissions_input
    import aws_sdk_qapps.types.describe_q_app_permissions_output
    import aws_sdk_qapps.types.description
    import aws_sdk_qapps.types.disassociate_library_item_review_input
    import aws_sdk_qapps.types.disassociate_q_app_from_user_input
    import aws_sdk_qapps.types.document_scope
    import aws_sdk_qapps.types.export_q_app_session_data_input
    import aws_sdk_qapps.types.export_q_app_session_data_output
    import aws_sdk_qapps.types.filename
    import aws_sdk_qapps.types.get_library_item_input
    import aws_sdk_qapps.types.get_library_item_output
    import aws_sdk_qapps.types.get_q_app_input
    import aws_sdk_qapps.types.get_q_app_output
    import aws_sdk_qapps.types.get_q_app_session_input
    import aws_sdk_qapps.types.get_q_app_session_metadata_input
    import aws_sdk_qapps.types.get_q_app_session_metadata_output
    import aws_sdk_qapps.types.get_q_app_session_output
    import aws_sdk_qapps.types.import_document_input
    import aws_sdk_qapps.types.import_document_output
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.library_item_member
    import aws_sdk_qapps.types.library_item_status
    import aws_sdk_qapps.types.list_categories_input
    import aws_sdk_qapps.types.list_categories_output
    import aws_sdk_qapps.types.list_library_items_input
    import aws_sdk_qapps.types.list_library_items_output
    import aws_sdk_qapps.types.list_q_app_session_data_input
    import aws_sdk_qapps.types.list_q_app_session_data_output
    import aws_sdk_qapps.types.list_q_apps_input
    import aws_sdk_qapps.types.list_q_apps_output
    import aws_sdk_qapps.types.list_tags_for_resource_request
    import aws_sdk_qapps.types.list_tags_for_resource_response
    import aws_sdk_qapps.types.page_limit
    import aws_sdk_qapps.types.pagination_token
    import aws_sdk_qapps.types.permissions_input_list
    import aws_sdk_qapps.types.predict_q_app_input
    import aws_sdk_qapps.types.predict_q_app_input_options
    import aws_sdk_qapps.types.predict_q_app_output
    import aws_sdk_qapps.types.session_name
    import aws_sdk_qapps.types.session_sharing_configuration
    import aws_sdk_qapps.types.start_q_app_session_input
    import aws_sdk_qapps.types.start_q_app_session_output
    import aws_sdk_qapps.types.stop_q_app_session_input
    import aws_sdk_qapps.types.tag_keys
    import aws_sdk_qapps.types.tag_map
    import aws_sdk_qapps.types.tag_resource_request
    import aws_sdk_qapps.types.tag_resource_response
    import aws_sdk_qapps.types.tags
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.untag_resource_request
    import aws_sdk_qapps.types.untag_resource_response
    import aws_sdk_qapps.types.update_library_item_input
    import aws_sdk_qapps.types.update_library_item_metadata_input
    import aws_sdk_qapps.types.update_library_item_output
    import aws_sdk_qapps.types.update_q_app_input
    import aws_sdk_qapps.types.update_q_app_output
    import aws_sdk_qapps.types.update_q_app_permissions_input
    import aws_sdk_qapps.types.update_q_app_permissions_output
    import aws_sdk_qapps.types.update_q_app_session_input
    import aws_sdk_qapps.types.update_q_app_session_metadata_input
    import aws_sdk_qapps.types.update_q_app_session_metadata_output
    import aws_sdk_qapps.types.update_q_app_session_output
    import aws_sdk_qapps.types.user_app_item
    import aws_sdk_qapps.types.uuid


class QAppsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class QAppsClient:
    """A client for the ``QApps`` service.

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
        self._config = QAppsClientConfig(
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
        self, config_overrides: Optional[QAppsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: QAppsClientConfig = config_overrides or {}
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

    def associate_library_item_review(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        library_item_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> None:
        """<p>Associates a rating or review for a library item with the user submitting the request. This increments the rating count for the specified library item.</p>

        Args:
            instance_id: <p>The unique identifier for the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the library item to associate the review with.</p>

        Examples:
            Increase the rating counter by 1 for the related app for this user

            >>> client.associate_library_item_review(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', library_item_id='cb9ecf72-8563-450d-9db9-994f98297316')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.associate_library_item_review_input.AssociateLibraryItemReviewInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.associate_library_item_review

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.associate_library_item_review.associate_library_item_review(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.associate_library_item_review_input.AssociateLibraryItemReviewInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["library_item_id"] = library_item_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_q_app_with_user(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> None:
        """<p>This operation creates a link between the user's identity calling the operation and a specific Q App. This is useful to mark the Q App as a <i>favorite</i> for the user if the user doesn't own the Amazon Q App so they can still run it and see it in their inventory of Q Apps.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The ID of the Amazon Q App to associate with the user.</p>

        Examples:
            Links an Amazon Q App to the invoker's list of apps

            >>> client.associate_q_app_with_user(app_id='393e77fb-0a30-4f47-ad30-75d71aeaed8a', instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.associate_q_app_with_user_input.AssociateQAppWithUserInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.associate_q_app_with_user

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.associate_q_app_with_user.associate_q_app_with_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.associate_q_app_with_user_input.AssociateQAppWithUserInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["app_id"] = app_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_create_category(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        categories: "aws_sdk_qapps.types.batch_create_category_input_category_list.BatchCreateCategoryInputCategoryList",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> None:
        r"""<p>Creates Categories for the Amazon Q Business application environment instance. Web experience users use Categories to tag and filter library items. For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-custom-labels.html\">Custom labels for Amazon Q Apps</a>.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            categories: <p>The list of category objects to be created</p>

        Examples:
            Creates the categories for the library

            >>> client.batch_create_category(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', categories=[{'id': '549abfe0-f5c4-45a2-bb9b-c05987a49c6d', 'title': 'HR'}, {'id': '18cbebaa-196a-4aa5-a840-88d548e07f8f', 'title': 'Marketing'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.batch_create_category_input.BatchCreateCategoryInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.batch_create_category

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.batch_create_category.batch_create_category(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.batch_create_category_input.BatchCreateCategoryInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["categories"] = categories

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_delete_category(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        categories: "aws_sdk_qapps.types.delete_category_input_list.DeleteCategoryInputList",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> None:
        r"""<p>Deletes Categories for the Amazon Q Business application environment instance. Web experience users use Categories to tag and filter library items. For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-custom-labels.html\">Custom labels for Amazon Q Apps</a>.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            categories: <p>The list of IDs of the categories to be deleted.</p>

        Examples:
            Deletes the categories in the library

            >>> client.batch_delete_category(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', categories=['9c871ed4-1c41-4065-aefe-321cd4b61cf8'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.batch_delete_category_input.BatchDeleteCategoryInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.batch_delete_category

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.batch_delete_category.batch_delete_category(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.batch_delete_category_input.BatchDeleteCategoryInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["categories"] = categories

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_category(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        categories: "aws_sdk_qapps.types.category_list_input.CategoryListInput",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> None:
        r"""<p>Updates Categories for the Amazon Q Business application environment instance. Web experience users use Categories to tag and filter library items. For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-custom-labels.html\">Custom labels for Amazon Q Apps</a>.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            categories: <p>The list of categories to be updated with their new values.</p>

        Examples:
            Updates the categories in the library

            >>> client.batch_update_category(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', categories=[{'id': '549abfe0-f5c4-45a2-bb9b-c05987a49c6d', 'title': 'HR Management'}, {'id': '18cbebaa-196a-4aa5-a840-88d548e07f8f', 'title': 'Sales'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.batch_update_category_input.BatchUpdateCategoryInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.batch_update_category

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.batch_update_category.batch_update_category(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.batch_update_category_input.BatchUpdateCategoryInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["categories"] = categories

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_library_item(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        app_version: "aws_sdk_qapps.types.app_version.AppVersion",
        categories: "aws_sdk_qapps.types.category_id_list.CategoryIdList",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> "aws_sdk_qapps.types.create_library_item_output.CreateLibraryItemOutput":
        """<p>Creates a new library item for an Amazon Q App, allowing it to be discovered and used by other allowed users. </p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Amazon Q App to publish to the library.</p>
            app_version: <p>The version of the Amazon Q App to publish to the library.</p>
            categories: <p>The categories to associate with the library item for easier discovery.</p>

        Examples:
            Create a Library Item

            >>> client.create_library_item(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', app_id='7a11f34b-42d4-4bc8-b668-ae4a788dae1e', app_version=6, categories=['9c871ed4-1c41-4065-aefe-321cd4b61cf8'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.create_library_item_input.CreateLibraryItemInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.create_library_item_output.CreateLibraryItemOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.create_library_item

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.create_library_item.create_library_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.create_library_item_input.CreateLibraryItemInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["app_id"] = app_id
        input_["app_version"] = app_version
        input_["categories"] = categories

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_presigned_url(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        card_id: "aws_sdk_qapps.types.uuid.UUID",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        file_contents_sha256: str,
        file_name: "aws_sdk_qapps.types.filename.Filename",
        scope: "aws_sdk_qapps.types.document_scope.DocumentScope",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        session_id: Optional["aws_sdk_qapps.types.uuid.UUID"] = None,
    ) -> "aws_sdk_qapps.types.create_presigned_url_output.CreatePresignedUrlOutput":
        r"""<p>Creates a presigned URL for an S3 POST operation to upload a file. You can use this URL to set a default file for a <code>FileUploadCard</code> in a Q App definition or to provide a file for a single Q App run. The <code>scope</code> parameter determines how the file will be used, either at the app definition level or the app session level.</p> <note> <p>The IAM permissions are derived from the <code>qapps:ImportDocument</code> action. For more information on the IAM policy for Amazon Q Apps, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/deploy-q-apps-iam-permissions.html\">IAM permissions for using Amazon Q Apps</a>.</p> </note>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            card_id: <p>The unique identifier of the card the file is associated with.</p>
            app_id: <p>The unique identifier of the Q App the file is associated with.</p>
            file_contents_sha256: <p>The Base64-encoded SHA-256 digest of the contents of the file to be uploaded.</p>
            file_name: <p>The name of the file to be uploaded.</p>
            scope: <p>Whether the file is associated with a Q App definition or a specific Q App session.</p>
            session_id: <p>The unique identifier of the Q App session the file is associated with, if applicable.</p>

        Examples:
            Upload a file to a specific session

            >>> client.create_presigned_url(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', file_contents_sha256='wXY7GD8m4fmHhdtuQyBdXzNQpdCseVwBcOBIlzfm+kg=', file_name='myFile.txt', card_id='82f69028-22a9-4bea-8727-0eabf58e9fed', app_id='4263767c-d889-4cb2-a8f6-8b649bc66af0', scope='SESSION', session_id='4f0e5b87-9d38-41cd-9eb4-ebce2f2917cc')
            Upload a file into a application

            >>> client.create_presigned_url(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', file_contents_sha256='wXY7GD8m4fmHhdtuQyBdXzNQpdCseVwBcOBIlzfm+kg=', file_name='anApplicationFile.txt', app_id='4263767c-d889-4cb2-a8f6-8b649bc66af0', card_id='7a11f34b-42d4-4bc8-b668-ae4a788dae1e', scope='APPLICATION')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.create_presigned_url_input.CreatePresignedUrlInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.create_presigned_url_output.CreatePresignedUrlOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.create_presigned_url

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.create_presigned_url.create_presigned_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.create_presigned_url_input.CreatePresignedUrlInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["card_id"] = card_id
        input_["app_id"] = app_id
        input_["file_contents_sha256"] = file_contents_sha256
        input_["file_name"] = file_name
        input_["scope"] = scope
        if session_id is not None:
            input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_q_app(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        title: "aws_sdk_qapps.types.title.Title",
        app_definition: "aws_sdk_qapps.types.app_definition_input.AppDefinitionInput",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        description: Optional["aws_sdk_qapps.types.description.Description"] = None,
        tags: Optional["aws_sdk_qapps.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_qapps.types.create_q_app_output.CreateQAppOutput":
        """<p>Creates a new Amazon Q App based on the provided definition. The Q App definition specifies the cards and flow of the Q App. This operation also calculates the dependencies between the cards by inspecting the references in the prompts. </p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            title: <p>The title of the new Q App.</p>
            description: <p>The description of the new Q App.</p>
            app_definition: <p>The definition of the new Q App, specifying the cards and flow.</p>
            tags: <p>Optional tags to associate with the new Q App.</p>

        Examples:
            A basic application with 1 text input card and 1 output card

            >>> client.create_q_app(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', title='Color Palette Generator', app_definition={'cards': [{'textInput': {'type': 'text-input', 'title': 'Color Base', 'id': '4cf94d96-8819-45c2-98cc-58c56b35c72f'}}, {'qQuery': {'type': 'q-query', 'title': 'Recommended Palette', 'id': '18870b94-1e63-40e0-8c12-669c90ac5acc', 'prompt': 'Recommend me a list of colors that go well with @4cf94d96-8819-45c2-98cc-58c56b35c72f'}}], 'initialPrompt': 'Create an app that recommend a list of colors based on input.'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.create_q_app_input.CreateQAppInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.create_q_app_output.CreateQAppOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.create_q_app

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.create_q_app.create_q_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.create_q_app_input.CreateQAppInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["title"] = title
        if description is not None:
            input_["description"] = description
        input_["app_definition"] = app_definition
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_library_item(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        library_item_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> None:
        """<p>Deletes a library item for an Amazon Q App, removing it from the library so it can no longer be discovered or used by other users.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the library item to delete.</p>

        Examples:
            Delete a library item

            >>> client.delete_library_item(instance_id='3642ba81-344c-42fd-a480-9119a5a5f26b', library_item_id='72088fd4-78b6-43da-bfb8-8621323c3cfb')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.delete_library_item_input.DeleteLibraryItemInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.delete_library_item

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.delete_library_item.delete_library_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.delete_library_item_input.DeleteLibraryItemInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["library_item_id"] = library_item_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_q_app(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> None:
        """<p>Deletes an Amazon Q App owned by the user. If the Q App was previously published to the library, it is also removed from the library.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Q App to delete.</p>

        Examples:
            Delete an Amazon Q App

            >>> client.delete_q_app(app_id='393e77fb-0a30-4f47-ad30-75d71aeaed8a', instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.delete_q_app_input.DeleteQAppInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.delete_q_app

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.delete_q_app.delete_q_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.delete_q_app_input.DeleteQAppInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["app_id"] = app_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_q_app_permissions(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> "aws_sdk_qapps.types.describe_q_app_permissions_output.DescribeQAppPermissionsOutput":
        """<p> Describes read permissions for a Amazon Q App in Amazon Q Business application environment instance.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Amazon Q App for which to retrieve permissions.</p>

        Examples:
            Describe permissions for the app

            >>> client.describe_q_app_permissions(instance_id='01793661-ad73-4c7d-8eaa-1c95a10151c2', app_id='fe0acf86-49e5-4def-a0c2-40ce0cafee14')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.describe_q_app_permissions_input.DescribeQAppPermissionsInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.describe_q_app_permissions_output.DescribeQAppPermissionsOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.describe_q_app_permissions

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.describe_q_app_permissions.describe_q_app_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.describe_q_app_permissions_input.DescribeQAppPermissionsInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["app_id"] = app_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_library_item_review(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        library_item_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> None:
        """<p>Removes a rating or review previously submitted by the user for a library item.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the library item to remove the review from.</p>

        Examples:
            Decrease the rating counter by 1 for the related app for this user

            >>> client.disassociate_library_item_review(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', library_item_id='cb9ecf72-8563-450d-9db9-994f98297316')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.disassociate_library_item_review_input.DisassociateLibraryItemReviewInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.disassociate_library_item_review

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.disassociate_library_item_review.disassociate_library_item_review(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.disassociate_library_item_review_input.DisassociateLibraryItemReviewInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["library_item_id"] = library_item_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_q_app_from_user(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> None:
        """<p>Disassociates a Q App from a user removing the user's access to run the Q App.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Q App to disassociate from the user.</p>

        Examples:
            Unlinks an Amazon Q App from the invoker's list of apps

            >>> client.disassociate_q_app_from_user(app_id='393e77fb-0a30-4f47-ad30-75d71aeaed8a', instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.disassociate_q_app_from_user_input.DisassociateQAppFromUserInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.disassociate_q_app_from_user

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.disassociate_q_app_from_user.disassociate_q_app_from_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.disassociate_q_app_from_user_input.DisassociateQAppFromUserInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["app_id"] = app_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def export_q_app_session_data(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        session_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> "aws_sdk_qapps.types.export_q_app_session_data_output.ExportQAppSessionDataOutput":
        """<p>Exports the collected data of a Q App data collection session.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App data collection session.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.export_q_app_session_data_input.ExportQAppSessionDataInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.export_q_app_session_data_output.ExportQAppSessionDataOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.export_q_app_session_data

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.export_q_app_session_data.export_q_app_session_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.export_q_app_session_data_input.ExportQAppSessionDataInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_library_item(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        library_item_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        app_id: Optional["aws_sdk_qapps.types.uuid.UUID"] = None,
    ) -> "aws_sdk_qapps.types.get_library_item_output.GetLibraryItemOutput":
        """<p>Retrieves details about a library item for an Amazon Q App, including its metadata, categories, ratings, and usage statistics.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the library item to retrieve.</p>
            app_id: <p>The unique identifier of the Amazon Q App associated with the library item.</p>

        Examples:
            Retrieve a library item

            >>> client.get_library_item(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', library_item_id='18cbebaa-196a-4aa5-a840-88d548e07f8f')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.get_library_item_input.GetLibraryItemInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.get_library_item_output.GetLibraryItemOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.get_library_item

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.get_library_item.get_library_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.get_library_item_input.GetLibraryItemInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["library_item_id"] = library_item_id
        if app_id is not None:
            input_["app_id"] = app_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_q_app(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        app_version: Optional["aws_sdk_qapps.types.app_version.AppVersion"] = None,
    ) -> "aws_sdk_qapps.types.get_q_app_output.GetQAppOutput":
        """<p>Retrieves the full details of an Q App, including its definition specifying the cards and flow.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Q App to retrieve.</p>
            app_version: <p>The version of the Q App.</p>

        Examples:
            A basic application with 1 text input card and 1 output card

            >>> client.get_q_app(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', app_id='3d110749-efc3-427c-87e8-15e966e5c168')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.get_q_app_input.GetQAppInput]",
        ) -> OperationResponse["aws_sdk_qapps.types.get_q_app_output.GetQAppOutput"]:
            import aws_sdk_qapps._operations.q_apps_service.get_q_app

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.get_q_app.get_q_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.get_q_app_input.GetQAppInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["app_id"] = app_id
        if app_version is not None:
            input_["app_version"] = app_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_q_app_session(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        session_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> "aws_sdk_qapps.types.get_q_app_session_output.GetQAppSessionOutput":
        """<p>Retrieves the current state and results for an active session of an Amazon Q App.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App session to retrieve.</p>

        Examples:
            Retrieves an existing session for an Amazon Q App

            >>> client.get_q_app_session(instance_id='288ae830-1df2-4871-b6c0-4314d74dadef', session_id='1fca878e-64c5-4dc4-b1d9-c93effed4e82')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.get_q_app_session_input.GetQAppSessionInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.get_q_app_session_output.GetQAppSessionOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.get_q_app_session

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.get_q_app_session.get_q_app_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.get_q_app_session_input.GetQAppSessionInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_q_app_session_metadata(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        session_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> "aws_sdk_qapps.types.get_q_app_session_metadata_output.GetQAppSessionMetadataOutput":
        """<p>Retrieves the current configuration of a Q App session.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App session.</p>

        Examples:
            Retrieves an existing session metadata for an Amazon Q App

            >>> client.get_q_app_session_metadata(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', session_id='56ae47c3-10bc-4c2c-8b27-9b9fe23b3edb')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.get_q_app_session_metadata_input.GetQAppSessionMetadataInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.get_q_app_session_metadata_output.GetQAppSessionMetadataOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.get_q_app_session_metadata

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.get_q_app_session_metadata.get_q_app_session_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.get_q_app_session_metadata_input.GetQAppSessionMetadataInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_document(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        card_id: "aws_sdk_qapps.types.uuid.UUID",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        file_contents_base64: str,
        file_name: "aws_sdk_qapps.types.filename.Filename",
        scope: "aws_sdk_qapps.types.document_scope.DocumentScope",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        session_id: Optional["aws_sdk_qapps.types.uuid.UUID"] = None,
    ) -> "aws_sdk_qapps.types.import_document_output.ImportDocumentOutput":
        """<p>Uploads a file that can then be used either as a default in a <code>FileUploadCard</code> from Q App definition or as a file that is used inside a single Q App run. The purpose of the document is determined by a scope parameter that indicates whether it is at the app definition level or at the app session level.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            card_id: <p>The unique identifier of the card the file is associated with.</p>
            app_id: <p>The unique identifier of the Q App the file is associated with.</p>
            file_contents_base64: <p>The base64-encoded contents of the file to upload.</p>
            file_name: <p>The name of the file being uploaded.</p>
            scope: <p>Whether the file is associated with a Q App definition or a specific Q App session.</p>
            session_id: <p>The unique identifier of the Q App session the file is associated with, if applicable.</p>

        Examples:
            Upload a file to a specific session

            >>> client.import_document(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', file_contents_base64='data:text/plain;base64,SomeFileEncodedInBase64', file_name='myFile.txt', card_id='82f69028-22a9-4bea-8727-0eabf58e9fed', app_id='4263767c-d889-4cb2-a8f6-8b649bc66af0', scope='SESSION', session_id='4f0e5b87-9d38-41cd-9eb4-ebce2f2917cc')
            Upload a file into a application

            >>> client.import_document(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', file_contents_base64='data:text/plain;base64,SomeFileEncodedInBase64', file_name='anApplicationFile.txt', app_id='4263767c-d889-4cb2-a8f6-8b649bc66af0', card_id='7a11f34b-42d4-4bc8-b668-ae4a788dae1e', scope='APPLICATION')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.import_document_input.ImportDocumentInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.import_document_output.ImportDocumentOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.import_document

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.import_document.import_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.import_document_input.ImportDocumentInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["card_id"] = card_id
        input_["app_id"] = app_id
        input_["file_contents_base64"] = file_contents_base64
        input_["file_name"] = file_name
        input_["scope"] = scope
        if session_id is not None:
            input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_categories(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> "aws_sdk_qapps.types.list_categories_output.ListCategoriesOutput":
        r"""<p>Lists the categories of a Amazon Q Business application environment instance. For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-custom-labels.html\">Custom labels for Amazon Q Apps</a>.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>

        Examples:
            List categories available for the library items in this instance

            >>> client.list_categories(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.list_categories_input.ListCategoriesInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.list_categories_output.ListCategoriesOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.list_categories

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.list_categories.list_categories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.list_categories_input.ListCategoriesInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_library_items(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        limit: Optional["aws_sdk_qapps.types.page_limit.PageLimit"] = None,
        next_token: Optional[
            "aws_sdk_qapps.types.pagination_token.PaginationToken"
        ] = None,
        category_id: Optional["aws_sdk_qapps.types.uuid.UUID"] = None,
    ) -> "aws_sdk_qapps.types.list_library_items_output.ListLibraryItemsOutput":
        """<p>Lists the library items for Amazon Q Apps that are published and available for users in your Amazon Web Services account.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            limit: <p>The maximum number of library items to return in the response.</p>
            next_token: <p>The token to request the next page of results.</p>
            category_id: <p>Optional category to filter the library items by.</p>

        Examples:
            List at most 3 library items for this instance

            >>> client.list_library_items(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', limit=3)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.list_library_items_input.ListLibraryItemsInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.list_library_items_output.ListLibraryItemsOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.list_library_items

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.list_library_items.list_library_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.list_library_items_input.ListLibraryItemsInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if category_id is not None:
            input_["category_id"] = category_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_library_items(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        limit: Optional["aws_sdk_qapps.types.page_limit.PageLimit"] = None,
        next_token: Optional[
            "aws_sdk_qapps.types.pagination_token.PaginationToken"
        ] = None,
        category_id: Optional["aws_sdk_qapps.types.uuid.UUID"] = None,
    ) -> "Iterator[aws_sdk_qapps.types.library_item_member.LibraryItemMember]":
        _token = next_token
        while True:
            _response = self.list_library_items(
                instance_id,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
                category_id=category_id,
            )
            _page = _resolve_path(_response, ("library_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_q_apps(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        limit: Optional["aws_sdk_qapps.types.page_limit.PageLimit"] = None,
        next_token: Optional[
            "aws_sdk_qapps.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_qapps.types.list_q_apps_output.ListQAppsOutput":
        """<p>Lists the Amazon Q Apps owned by or associated with the user either because they created it or because they used it from the library in the past. The user identity is extracted from the credentials used to invoke this operation..</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            limit: <p>The maximum number of Q Apps to return in the response.</p>
            next_token: <p>The token to request the next page of results.</p>

        Examples:
            List at most 3 Amazon Q Apps in an Q Business application

            >>> client.list_q_apps(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', limit=3)
            Retrieve the next page of Amazon Q Apps

            >>> client.list_q_apps(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', limit=3, next_token='bXlzdGVyaW91c1BhZ2luYXRpb25Ub2tlbg==')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.list_q_apps_input.ListQAppsInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.list_q_apps_output.ListQAppsOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.list_q_apps

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.list_q_apps.list_q_apps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.list_q_apps_input.ListQAppsInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_q_apps(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        limit: Optional["aws_sdk_qapps.types.page_limit.PageLimit"] = None,
        next_token: Optional[
            "aws_sdk_qapps.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_qapps.types.user_app_item.UserAppItem]":
        _token = next_token
        while True:
            _response = self.list_q_apps(
                instance_id,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("apps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_q_app_session_data(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        session_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> "aws_sdk_qapps.types.list_q_app_session_data_output.ListQAppSessionDataOutput":
        """<p>Lists the collected data of a Q App data collection session.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App data collection session.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.list_q_app_session_data_input.ListQAppSessionDataInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.list_q_app_session_data_output.ListQAppSessionDataOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.list_q_app_session_data

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.list_q_app_session_data.list_q_app_session_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.list_q_app_session_data_input.ListQAppSessionDataInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_qapps.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> "aws_sdk_qapps.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with an Amazon Q Apps resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags should be listed.</p>

        Examples:
            A call to list tags for a resource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:qapps:us-west-2:123456789012:application/3642ba81-344c-42fd-a480-9119a5a5f26b/qapp/7212ff04-de7b-4831-bd80-45d6975ba1b0')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def predict_q_app(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        options: Optional[
            "aws_sdk_qapps.types.predict_q_app_input_options.PredictQAppInputOptions"
        ] = None,
    ) -> "aws_sdk_qapps.types.predict_q_app_output.PredictQAppOutput":
        """<p>Generates an Amazon Q App definition based on either a conversation or a problem statement provided as input.The resulting app definition can be used to call <code>CreateQApp</code>. This API doesn't create Amazon Q Apps directly.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            options: <p>The input to generate the Q App definition from, either a conversation or problem statement.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.predict_q_app_input.PredictQAppInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.predict_q_app_output.PredictQAppOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.predict_q_app

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.predict_q_app.predict_q_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.predict_q_app_input.PredictQAppInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        if options is not None:
            input_["options"] = options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_q_app_session(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        app_version: "aws_sdk_qapps.types.app_version.AppVersion",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        initial_values: Optional[
            "aws_sdk_qapps.types.card_value_list.CardValueList"
        ] = None,
        session_id: Optional[str] = None,
        tags: Optional["aws_sdk_qapps.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_qapps.types.start_q_app_session_output.StartQAppSessionOutput":
        """<p>Starts a new session for an Amazon Q App, allowing inputs to be provided and the app to be run.</p> <note> <p>Each Q App session will be condensed into a single conversation in the web experience.</p> </note>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Q App to start a session for.</p>
            app_version: <p>The version of the Q App to use for the session.</p>
            initial_values: <p>Optional initial input values to provide for the Q App session.</p>
            session_id: <p>The unique identifier of the a Q App session.</p>
            tags: <p>Optional tags to associate with the new Q App session.</p>

        Examples:
            Start a session for an Amazon Q App using version 1, passing in initial values for one card

            >>> client.start_q_app_session(instance_id='4cc5e4c2-d2a2-4188-a114-9ca125b4aedc', app_id='65e7dce7-226a-47f9-b689-22850becef89', app_version=1, initial_values=[{'cardId': '6fb5b404-3b7b-48a4-8a8b-56406922a606', 'value': 'What is the circumference of Earth?'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.start_q_app_session_input.StartQAppSessionInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.start_q_app_session_output.StartQAppSessionOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.start_q_app_session

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.start_q_app_session.start_q_app_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.start_q_app_session_input.StartQAppSessionInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["app_id"] = app_id
        input_["app_version"] = app_version
        if initial_values is not None:
            input_["initial_values"] = initial_values
        if session_id is not None:
            input_["session_id"] = session_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_q_app_session(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        session_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> None:
        """<p>Stops an active session for an Amazon Q App.This deletes all data related to the session and makes it invalid for future uses. The results of the session will be persisted as part of the conversation.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App session to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.stop_q_app_session_input.StopQAppSessionInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.stop_q_app_session

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.stop_q_app_session.stop_q_app_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.stop_q_app_session_input.StopQAppSessionInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_qapps.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_qapps.types.tags.Tags",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> "aws_sdk_qapps.types.tag_resource_response.TagResourceResponse":
        """<p>Associates tags with an Amazon Q Apps resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>The tags to associate with the resource.</p>

        Examples:
            A call to tag a resource

            >>> client.tag_resource(resource_arn='arn:aws:qapps:us-west-2:123456789012:application/3642ba81-344c-42fd-a480-9119a5a5f26b/qapp/7212ff04-de7b-4831-bd80-45d6975ba1b0', tags={'department': 'HR'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.tag_resource

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_qapps.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_qapps.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
    ) -> "aws_sdk_qapps.types.untag_resource_response.UntagResourceResponse":
        """<p>Disassociates tags from an Amazon Q Apps resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to disassociate the tag from.</p>
            tag_keys: <p>The keys of the tags to disassociate from the resource.</p>

        Examples:
            A call to untag a resource

            >>> client.untag_resource(resource_arn='arn:aws:qapps:us-west-2:123456789012:application/3642ba81-344c-42fd-a480-9119a5a5f26b/qapp/7212ff04-de7b-4831-bd80-45d6975ba1b0', tag_keys=['department'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.untag_resource

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_library_item(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        library_item_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        status: Optional[
            "aws_sdk_qapps.types.library_item_status.LibraryItemStatus"
        ] = None,
        categories: Optional[
            "aws_sdk_qapps.types.category_id_list.CategoryIdList"
        ] = None,
    ) -> "aws_sdk_qapps.types.update_library_item_output.UpdateLibraryItemOutput":
        r"""<p>Updates the library item for an Amazon Q App.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the library item to update.</p>
            status: <p>The new status to set for the library item, such as \"Published\" or \"Hidden\".</p>
            categories: <p>The new categories to associate with the library item.</p>

        Examples:
            Sets the status of a library item to DISABLED

            >>> client.update_library_item(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', library_item_id='cb9ecf72-8563-450d-9db9-994f98297316', status='DISABLED')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.update_library_item_input.UpdateLibraryItemInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.update_library_item_output.UpdateLibraryItemOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.update_library_item

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.update_library_item.update_library_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.update_library_item_input.UpdateLibraryItemInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["library_item_id"] = library_item_id
        if status is not None:
            input_["status"] = status
        if categories is not None:
            input_["categories"] = categories

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_library_item_metadata(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        library_item_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        is_verified: Optional[bool] = None,
    ) -> None:
        """<p>Updates the verification status of a library item for an Amazon Q App.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the updated library item.</p>
            is_verified: <p>The verification status of the library item</p>

        Examples:
            Update a library item to be verified

            >>> client.update_library_item_metadata(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', library_item_id='cb9ecf72-8563-450d-9db9-994f98297316', is_verified=True)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.update_library_item_metadata_input.UpdateLibraryItemMetadataInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_qapps._operations.q_apps_service.update_library_item_metadata

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.update_library_item_metadata.update_library_item_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.update_library_item_metadata_input.UpdateLibraryItemMetadataInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["library_item_id"] = library_item_id
        if is_verified is not None:
            input_["is_verified"] = is_verified

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_q_app(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        title: Optional["aws_sdk_qapps.types.title.Title"] = None,
        description: Optional["aws_sdk_qapps.types.description.Description"] = None,
        app_definition: Optional[
            "aws_sdk_qapps.types.app_definition_input.AppDefinitionInput"
        ] = None,
    ) -> "aws_sdk_qapps.types.update_q_app_output.UpdateQAppOutput":
        """<p>Updates an existing Amazon Q App, allowing modifications to its title, description, and definition.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Q App to update.</p>
            title: <p>The new title for the Q App.</p>
            description: <p>The new description for the Q App.</p>
            app_definition: <p>The new definition specifying the cards and flow for the Q App.</p>

        Examples:
            Updating the title of an app

            >>> client.update_q_app(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', app_id='7212ff04-de7b-4831-bd80-45d6975ba1b0', title='This is the new title')
            Updating the app so it has a single q-query card

            >>> client.update_q_app(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', app_id='7212ff04-de7b-4831-bd80-45d6975ba1b0', app_definition={'cards': [{'qQuery': {'type': 'q-query', 'title': 'Trip Ideas', 'id': '18870b94-1e63-40e0-8c12-669c90ac5acc', 'prompt': 'Recommend me an itinerary for a trip'}}]})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.update_q_app_input.UpdateQAppInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.update_q_app_output.UpdateQAppOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.update_q_app

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.update_q_app.update_q_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.update_q_app_input.UpdateQAppInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["app_id"] = app_id
        if title is not None:
            input_["title"] = title
        if description is not None:
            input_["description"] = description
        if app_definition is not None:
            input_["app_definition"] = app_definition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_q_app_permissions(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        app_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        grant_permissions: Optional[
            "aws_sdk_qapps.types.permissions_input_list.PermissionsInputList"
        ] = None,
        revoke_permissions: Optional[
            "aws_sdk_qapps.types.permissions_input_list.PermissionsInputList"
        ] = None,
    ) -> "aws_sdk_qapps.types.update_q_app_permissions_output.UpdateQAppPermissionsOutput":
        """<p>Updates read permissions for a Amazon Q App in Amazon Q Business application environment instance.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Amazon Q App for which permissions are being updated.</p>
            grant_permissions: <p>The list of permissions to grant for the Amazon Q App.</p>
            revoke_permissions: <p>The list of permissions to revoke for the Amazon Q App.</p>

        Examples:
            Grant permissions for the app

            >>> client.update_q_app_permissions(instance_id='01793661-ad73-4c7d-8eaa-1c95a10151c2', app_id='fe0acf86-49e5-4def-a0c2-40ce0cafee14', grant_permissions=[{'action': 'read', 'principal': 'user2@example.com'}])
            Revoke permissions for the app

            >>> client.update_q_app_permissions(instance_id='01793661-ad73-4c7d-8eaa-1c95a10151c2', app_id='fe0acf86-49e5-4def-a0c2-40ce0cafee14', revoke_permissions=[{'action': 'read', 'principal': 'user2@example.com'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.update_q_app_permissions_input.UpdateQAppPermissionsInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.update_q_app_permissions_output.UpdateQAppPermissionsOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.update_q_app_permissions

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.update_q_app_permissions.update_q_app_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.update_q_app_permissions_input.UpdateQAppPermissionsInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["app_id"] = app_id
        if grant_permissions is not None:
            input_["grant_permissions"] = grant_permissions
        if revoke_permissions is not None:
            input_["revoke_permissions"] = revoke_permissions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_q_app_session(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        session_id: "aws_sdk_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        values: Optional["aws_sdk_qapps.types.card_value_list.CardValueList"] = None,
    ) -> "aws_sdk_qapps.types.update_q_app_session_output.UpdateQAppSessionOutput":
        """<p>Updates the session for a given Q App <code>sessionId</code>. This is only valid when at least one card of the session is in the <code>WAITING</code> state. Data for each <code>WAITING</code> card can be provided as input. If inputs are not provided, the call will be accepted but session will not move forward. Inputs for cards that are not in the <code>WAITING</code> status will be ignored.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App session to provide input for.</p>
            values: <p>The input values to provide for the current state of the Q App session.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.update_q_app_session_input.UpdateQAppSessionInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.update_q_app_session_output.UpdateQAppSessionOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.update_q_app_session

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.update_q_app_session.update_q_app_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.update_q_app_session_input.UpdateQAppSessionInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["session_id"] = session_id
        if values is not None:
            input_["values"] = values

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_q_app_session_metadata(
        self,
        instance_id: "aws_sdk_qapps.types.instance_id.InstanceId",
        session_id: "aws_sdk_qapps.types.uuid.UUID",
        sharing_configuration: "aws_sdk_qapps.types.session_sharing_configuration.SessionSharingConfiguration",
        *,
        config_overrides: Optional[QAppsClientConfig] = None,
        session_name: Optional["aws_sdk_qapps.types.session_name.SessionName"] = None,
    ) -> "aws_sdk_qapps.types.update_q_app_session_metadata_output.UpdateQAppSessionMetadataOutput":
        """<p>Updates the configuration metadata of a session for a given Q App <code>sessionId</code>.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App session to update configuration for.</p>
            session_name: <p>The new name for the Q App session.</p>
            sharing_configuration: <p>The new sharing configuration for the Q App data collection session.</p>

        Examples:
            Updates an existing session metadata for an Amazon Q App

            >>> client.update_q_app_session_metadata(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', session_id='56ae47c3-10bc-4c2c-8b27-9b9fe23b3edb', session_name='Trip itinerary collection session', sharing_configuration={'enabled': True, 'acceptResponses': True, 'revealCards': False})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_qapps.types.update_q_app_session_metadata_input.UpdateQAppSessionMetadataInput]",
        ) -> OperationResponse[
            "aws_sdk_qapps.types.update_q_app_session_metadata_output.UpdateQAppSessionMetadataOutput"
        ]:
            import aws_sdk_qapps._operations.q_apps_service.update_q_app_session_metadata

            output, http_response = (
                aws_sdk_qapps._operations.q_apps_service.update_q_app_session_metadata.update_q_app_session_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_qapps.types.update_q_app_session_metadata_input.UpdateQAppSessionMetadataInput = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["session_id"] = session_id
        if session_name is not None:
            input_["session_name"] = session_name
        input_["sharing_configuration"] = sharing_configuration

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
